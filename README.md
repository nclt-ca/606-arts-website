# 606 Art Space website

Hugo website for `606arts.ca`, using the NCLT site's warm off-white palette, large centred hero, minimal top navigation, and shared page layout. It is not a final 606 identity.

The homepage introduces the space and links to three editable pages: About, Organisations, and Find us. Copy is adapted from the existing public NCLT source at `../website/content/606.md`; its claims have not been independently reverified. No opening hours, contact addresses, additional tenants, or programmes have been invented.

**Hosting:** GitHub Pages, matching NCLT. Decap remains a later step; its GitHub backend will need an external OAuth service, and editors will need GitHub accounts with repository write access. Netlify hosting is not required.

Internal briefs and planning notes are kept locally and excluded from this public repository.

## Preview and build

Requires **Hugo Extended 0.152.2**, with LibSass support, matching the pinned CI version:

```sh
hugo server --bind 127.0.0.1
```

Open <http://localhost:1313/>. To build:

```sh
hugo --minify
```

Local output goes to `public/`. Pushes to `main` deploy automatically via GitHub Actions, as described below.

```sh
npm ci
npm run format:check
python3 scripts/check_site.py
```

Run the content checks after building. `npm run dev` and `npm run build` also wrap Hugo, but need the correct `hugo` binary on your PATH. There is no `justfile`.

## Editing content

All page copy lives in Markdown, not templates:

| File                       | Editable content                                                                                          |
| -------------------------- | --------------------------------------------------------------------------------------------------------- |
| `content/_index.md`        | Hero title, subtitle and location; introduction heading and body; featured section heading and page order |
| `content/about.md`         | About 606 and NCLT’s role                                                                                 |
| `content/organisations.md` | Organisation names and links                                                                              |
| `content/visit.md`         | Location and visitor information                                                                          |

Each inner page has a `title`, `description`, and Markdown body. The description appears beneath its page title and in its homepage card. `menus.main.name` controls its top-menu label; `menus.main.weight` controls order. Hugo marks the current page in the navigation.

To add a page, create `content/your-page.md` with this front matter and a Markdown body:

```yaml
---
title: "Your page title"
description: "A short introduction to the page."
menus:
  main:
    name: "Menu label"
    weight: 35
---
```

Add `/your-page` to `featured_pages` in `content/_index.md` if it should have a homepage card. Cards use the linked page's title and description, so editors only update them once. Remove the page's `menus` field if it should not appear in the top menu.

`hugo.toml` contains the site name, fallback metadata, external NCLT menu link, footer steward link, and `params.noindex` guard. The footer reuses the homepage's location. No CMS or `/admin/` is installed yet; these fields are ready to map into Decap collections later.

## Templates and styling

- `layouts/baseof.html`: shared navigation, skip link, main landmark, and footer.
- `layouts/home.html`: hero, introduction, and featured page cards.
- `layouts/_default/single.html`: shared inner-page title, summary, and body.
- `layouts/_partials/footer.html`: site name, location, and steward link.
- `assets/scss/main.scss`: NCLT-derived palette, typography, spacing, and responsive layout.

The small-screen menu wraps and stays visible. It needs no JavaScript. Stylesheets are served locally, with no third-party runtime requests, photos, forms, or CMS scripts.

## Deployment

Repository: <https://github.com/nclt-ca/606-arts-website>

Pushes to `main` trigger `.github/workflows/gh-pages.yaml`: build with Hugo Extended 0.152.2, check the generated pages, upload a Pages artifact, and deploy through GitHub Actions. Manual workflow runs are also supported. This follows the NCLT website's deployment pattern, with a pinned Hugo version and an updated checkout action.

GitHub Pages uses **GitHub Actions** as its source and **606arts.ca** as its custom domain. DNSimple records and HTTPS setup are documented in [docs/deployment.md](docs/deployment.md).

## Indexing guard and source boundaries

`params.noindex = true` keeps `noindex, nofollow` in page metadata for the initial public review. This is not access control: anyone can visit the deployed site. Removing this guard later also requires updating the publication-guard assertion in `scripts/check_site.py`.

The sibling NCLT site is a read-only reference. Internal briefs, planning notes, generated output, dependencies, and caches are excluded from the public repository. Only Hugo's generated `public/` directory is deployed.

The copied foundation retains the original MIT licence. Bootstrap 5.3.2 is vendored locally with its licence notice; its SHA-384 matches the source site's integrity value:

```text
T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN
```
