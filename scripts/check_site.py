"""Smoke-test a built local draft: python3 scripts/check_site.py [output-dir]."""

from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.text = []
        self.main_nav_links = []
        self.in_main_nav = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == "nav" and attrs.get("aria-label") == "Main navigation":
            self.in_main_nav = True
        if tag == "a" and self.in_main_nav:
            self.main_nav_links.append(attrs.get("href"))

    def handle_endtag(self, tag):
        if tag == "nav":
            self.in_main_nav = False

    def handle_data(self, data):
        self.text.append(data)

    def elements(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]


root = Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
required = ["index.html", "about/index.html", "organisations/index.html", "visit/index.html"]
for name in required:
    assert (root / name).is_file(), f"Missing built page: {name}"

paths = sorted(root.rglob("*.html"))
for path in paths:
    page = Page(path)
    assert len(page.elements("h1")) == 1, f"{path}: expected one H1"
    assert len(page.elements("main")) == 1, f"{path}: expected one main landmark"
    assert page.elements("footer"), f"{path}: missing footer"
    assert any(a.get("href") == "#main" for a in page.elements("a")), path
    assert any(n.get("aria-label") == "Main navigation" for n in page.elements("nav")), path
    assert "https://nclt.ca/" not in page.main_nav_links, f"{path}: NCLT is still in the main nav"
    assert any(m.get("name") == "robots" and m.get("content") == "noindex, nofollow"
               for m in page.elements("meta")), f"{path}: missing publication guard"
    assert not any(page.elements(t) for t in ["script", "form", "img"]), path
    ids = [a["id"] for _, a in page.tags if "id" in a]
    assert len(ids) == len(set(ids)), f"{path}: duplicate IDs"
    for _, attrs in page.tags:
        for target in attrs.get("aria-labelledby", "").split():
            assert target in ids, f"{path}: missing accessible label {target}"
    assert any(a.get("href") == "https://nclt.ca/" for a in page.elements("a")), path
    active = [a for a in page.elements("a") if a.get("aria-current") == "page"]
    if str(path.relative_to(root)) in required[1:]:
        expected = "/" + str(path.parent.relative_to(root)) + "/"
        assert len(active) == 1 and active[0]["href"] == expected, (path, active)
    if path == root / "index.html":
        assert not active, "Homepage must not highlight an inner-page menu link"
        assert any("hero-section" in a.get("class", "").split() for _, a in page.tags)
    for tag, attrs in page.tags:
        if tag not in ("a", "link") or "href" not in attrs:
            continue
        url = urlsplit(attrs["href"])
        if url.scheme or url.netloc:
            assert attrs.get("rel") != "stylesheet", "Styles must be local"
            continue
        if url.path:
            target = (root / unquote(url.path).lstrip("/") if url.path.startswith("/")
                      else path.parent / unquote(url.path))
            if target.is_dir():
                target = target / "index.html"
        else:
            target = path
        assert target.is_file(), f"{path}: broken link {attrs['href']}"
        if url.fragment:
            target_ids = [a.get("id") for _, a in Page(target).tags]
            assert unquote(url.fragment) in target_ids, f"{path}: broken fragment {attrs['href']}"

organisations = Page(root / "organisations/index.html")
for url in ["https://ksarts.ca/", "https://www.nearsidearts.org/"]:
    assert any(a.get("href") == url for a in organisations.elements("a")), url
visit = Page(root / "visit/index.html")
assert "606 Victoria Street" in " ".join(visit.text)
assert any(a.get("href") == "mailto:hello@nclt.ca" for a in visit.elements("a")), "Missing space enquiry email"
about = Page(root / "about/index.html")
assert "The building" not in [t.strip() for t in about.text], "Redundant building section remains"
print(f"Passed: {len(paths)} pages; structure, navigation, links, local assets, and publication guard.")
