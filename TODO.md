# 606 Art Space website — TODO

Project checklist for the 606 Art Space website. Keep private source material out of this public checklist and website copy.

## Current decisions

- Hugo, hosted on GitHub Pages at <https://606arts.ca>.
- Repository: <https://github.com/nclt-ca/606-arts-website>.
- Text-first site with Home, About, Organisations, and Find us pages. Reuse the NCLT visual foundation; no new brand system required.
- Decap CMS is iteration 2, not a prerequisite for the current site.
- No dependency on Eden's draft, photography, or a logo.
- Email capture and a privacy policy are required follow-up work. Consider Sender.net or a similar provider; no provider has been chosen yet.
- NCLT is the building steward; tenant organisations remain independent. Link to NCLT in the content/footer, not the main navigation.

## Iteration 1 — completed

- [x] Import the Hugo foundation and NCLT styling without changing the sibling website.
- [x] Add a short introduction, address, and editable Markdown pages.
- [x] Explain NCLT's stewardship and the independent tenant organisations.
- [x] Link to Kootenay School of the Arts Society, Nearside Arts, and NCLT using the existing public NCLT source.
- [x] Include the operational feasibility study and its context on About.
- [x] Remove NCLT from the main navigation while retaining its footer/content links.
- [x] Add a “Use the space” section on Find us linking to `hello@nclt.ca`, as requested by Matt.
- [x] Remove the redundant “The building” section from About.
- [x] Check the Hugo build, formatting, navigation, links, and generated HTML.

## Hosting

- [x] Create the public GitHub repository, excluding internal briefs, plans, and generated files.
- [x] Configure GitHub Actions to build Hugo and deploy pushes to `main` to Pages.
- [x] Configure `606arts.ca` as the GitHub Pages custom domain.
- [x] Add four apex A records and the `www` CNAME in DNSimple; verify authoritative records and GitHub's DNS health checks.
- [x] Wait for GitHub's TLS certificate, then enable Enforce HTTPS. Confirmed done by Matt.
- [x] Verify the live HTTPS site and the HTTP/www redirects after certificate provisioning. Confirmed done by Matt.
- [ ] Remove the `noindex` guard when search indexing is approved; update the matching smoke-test assertion at the same time.

## Content and operational follow-up

- [ ] Independently confirm current tenant names, URLs, and public claims. Existing NCLT website copy is the source so far, not a fresh verification.
- [ ] Confirm who receives `hello@nclt.ca`, who can access it, and who owns replies. The published role address is confirmed by Matt; inbox arrangements have not been checked.
- [ ] Have a nontechnical collaborator review the site.
- [ ] Confirm visitor access information before adding any opening hours or accessibility claims. Do not invent these details.

## Iteration 2 — Decap editing test

- [ ] Add Decap with editable homepage fields and the About, Organisations, and Find us pages.
- [ ] Test editing, saving, previewing, and publishing without changing the GitHub Pages hosting choice.
- [ ] Configure and test the GitHub backend and its authentication requirements; choose an appropriate OAuth service before inviting editors.
- [ ] Validate that Git-backed content and the proposed permissions work for Matt and collaborators.
- [ ] Have at least one nontechnical collaborator complete an edit successfully.

## Optional later work — not launch blockers

- Eden's narrative draft, if useful for a later copy revision.
- Blaine's shared asset folder; Rheagan's permission-cleared photographs; Rhea's identity ideas.
- Exterior/common-space imagery or art-making photos only with appropriate permission. Coordinate before using identifiable-person, studio, or student images.
- Community Futures B-roll only with explicit permission.

## Email capture and privacy policy

There is currently no signup or collection form; the contact route is a mailto link. Agree the privacy arrangements and publish the policy before enabling collection.

- [ ] Choose Sender.net or a similar email capture provider, checking pricing, GitHub Pages integration, consent/unsubscribe support, and data handling.
- [ ] Name the responsible privacy contact/organisation and confirm who owns and can access the email platform account and subscriber list.
- [ ] Agree signup purpose wording and consent language.
- [ ] Agree retention, deletion, and unsubscribe handling; confirm provider storage locations and any cross-border processing.
- [ ] Draft, review, and publish a privacy policy reflecting the actual collection, use, service providers, and handling of personal information. Link it from the footer and signup form; do not treat generated policy text as a compliance guarantee.
- [ ] Add a lightweight “stay in the know” email signup using the chosen provider.
- [ ] Test signup, consent recording, confirmation, error states, and unsubscribe end to end before enabling public collection.

## Out of scope

- Netlify hosting or pricing research: GitHub Pages is the chosen host.
- Purchasing `606.art`, a logo competition, or a final brand system.
- Membership/governance decisions, large physical signs, complex events integration, or video production.

## References

- Public site: <https://606arts.ca>
- Deployment and DNS instructions: `docs/deployment.md`
- Decap CMS Hugo guide: <https://decapcms.org/docs/hugo/>
- BC OIPC private organisations: <https://www.oipc.bc.ca/for-private-organizations/>
- BC PIPA guide: <https://www.oipc.bc.ca/documents/guidance-documents/1371>
