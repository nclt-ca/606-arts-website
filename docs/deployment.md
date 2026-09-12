# GitHub Pages and DNSimple

## GitHub

- Repository: <https://github.com/nclt-ca/606-arts-website>
- Pages settings: <https://github.com/nclt-ca/606-arts-website/settings/pages>
- Source: GitHub Actions
- Production branch: `main`
- Custom domain: `606arts.ca`
- Workflow: `.github/workflows/gh-pages.yaml`

The build/deploy workflow follows `nclt-ca/website`, but pins Hugo Extended to 0.152.2. Configure the custom domain in GitHub before pointing DNS at Pages. An Actions deployment does not require a `CNAME` file; GitHub Pages settings own the custom-domain association.

## DNSimple

Edit the DNS zone for **606arts.ca**, not nclt.ca. Add these records (a blank name denotes the root/apex in DNSimple):

| Type  | Name       | Content           | TTL  |
| ----- | ---------- | ----------------- | ---- |
| A     | blank/root | 185.199.108.153   | 3600 |
| A     | blank/root | 185.199.109.153   | 3600 |
| A     | blank/root | 185.199.110.153   | 3600 |
| A     | blank/root | 185.199.111.153   | 3600 |
| CNAME | www        | nclt-ca.github.io | 3600 |

These are the same IPv4 addresses used by nclt.ca. The `www` target is the organisation's GitHub Pages hostname, not `nclt.ca`, a repository URL, or a hostname with a path.

Optional IPv6 records, if desired:

| Type | Name       | Content             | TTL  |
| ---- | ---------- | ------------------- | ---- |
| AAAA | blank/root | 2606:50c0:8000::153 | 3600 |
| AAAA | blank/root | 2606:50c0:8001::153 | 3600 |
| AAAA | blank/root | 2606:50c0:8002::153 | 3600 |
| AAAA | blank/root | 2606:50c0:8003::153 | 3600 |

Inspect the existing zone before saving. Do not add duplicate records or leave conflicting old web-host records. Preserve unrelated MX, TXT, verification, and other service records. Do not change nameservers or add wildcard records.

## HTTPS and checks

1. Confirm the GitHub Actions deployment succeeds.
2. After DNS propagates, check that GitHub Pages reports the domain's DNS as valid.
3. GitHub automatically provisions a TLS certificate. It can take up to 24 hours for **Enforce HTTPS** to become available; enable it once the certificate is ready.
4. Confirm `https://606arts.ca/` serves the homepage and local CSS. Confirm `www.606arts.ca` redirects to the apex and that HTTP redirects to HTTPS after enforcement.

```sh
dig +short 606arts.ca A
dig +short www.606arts.ca CNAME
curl -I https://606arts.ca/
curl -I http://606arts.ca/
curl -I https://www.606arts.ca/
```

GitHub also recommends domain verification under [organisation Settings → Pages](https://github.com/organizations/nclt-ca/settings/pages). Add `606arts.ca`, copy GitHub's generated TXT challenge into DNSimple, and verify it. Do not invent the token; retain the TXT record after verification.

## References

- [GitHub: Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [GitHub: Verifying a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-your-github-pages-site)
