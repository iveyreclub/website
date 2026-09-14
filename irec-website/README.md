# Ivey Real Estate Club — website

Plain static HTML. No build step, no framework, no dependencies. Open
`index.html` in a browser to preview it locally.

```
index.html      Home
about.html      About IREC
events.html     Events + Day on Bay
team.html       2026/27 executive team
partners.html   Sponsors and partnership formats
join.html       Roles, application process, key dates
css/style.css   All styling
js/main.js      Nav, role tabs, application countdown
assets/         Headshots, photography, logos
```

## Deploying

**GitHub Pages (free).** Create a repository, drop these files in the root,
then Settings → Pages → Source: `main` / root. The site goes live at
`username.github.io/repo` within a minute.

**Custom domain.** `iveyrealestateclub.com` is currently live on another
platform. Once you have registrar access, add a `CNAME` file to this
repository containing `iveyrealestateclub.com`, then point the domain's DNS
at GitHub Pages. Cloudflare Pages works the same way and is also free.

## What to update each year

1. **`build.py`** (one level up from this folder) regenerates all six pages
   from a single template. Edit it and run `python3 build.py` rather than
   editing six HTML files by hand.
2. **Application deadline.** `APP_CLOSE` in `build.py`. The countdown banner
   switches to a closed message on its own once the date passes.
3. **Application link.** `APPLY_URL` in `build.py`.
4. **Executive team.** The `TEAM` list in `build.py`, plus square headshots
   at `assets/team/<slug>.jpg` (560×560, centred on the face).
5. **Events, panellists, partners, and club statistics** are written inline
   in `build.py` under the matching page.

## Notes

- Club statistics currently use the 2026/27 information session figures
  (150+ members, 700+ alumni, 15+ firm partners). The 2025/26 year-end
  report gives different numbers. Pick one canonical set.
- The placements section lists firms only — no student names alongside
  employers. Adding names should be opt-in.
- Fonts load from Google Fonts. If you would rather not depend on that,
  download EB Garamond and Archivo into `assets/fonts/` and swap the
  `<link>` in `build.py` for an `@font-face` block.
