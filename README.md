# matchcam-site

Static pages for the MatchCam app, served with GitHub Pages.

**Home:** https://danielosorio83.github.io/matchcam-site/

## Pages

| Page | URL | Used for |
|---|---|---|
| `index.html` | https://danielosorio83.github.io/matchcam-site/ | Home page (Google OAuth consent screen homepage, store listings) |
| `features.html` | https://danielosorio83.github.io/matchcam-site/features.html | Full feature list with Free vs Pro comparison (linked from the home page and the menu) |
| `privacy.html` | https://danielosorio83.github.io/matchcam-site/privacy.html | Privacy policy (App Store, Google Play, Google OAuth, in-app links) |
| `terms.html` | https://danielosorio83.github.io/matchcam-site/terms.html | Terms of use (required for auto-renewable subscriptions) |
| `support.html` | https://danielosorio83.github.io/matchcam-site/support.html | Support page (App Store support URL) |

Contact: matchcam2026@gmail.com

## Structure

```
.
├── index.html, features.html, privacy.html, terms.html, support.html   # generated pages
├── assets/
│   ├── css/style.css          # site styles (brand colors from the in-app watermark)
│   ├── images/                # logo.png (app icon), wordmark.png (header logo)
│   └── icons/                 # favicon.png, apple-touch-icon.png
├── scripts/build_site.py      # generates the HTML pages
├── .nojekyll                  # serve files as-is on GitHub Pages
└── README.md
```

The HTML pages stay at the repository root on purpose: their URLs are registered in App Store Connect, Google Play Console, the Google OAuth consent screen and the app itself. Moving or renaming a page breaks those links.

## Editing

Page content lives in `scripts/build_site.py` (shared header, menu and footer included). Edit it, then rebuild and publish:

```bash
python3 scripts/build_site.py
git add -A && git commit -m "Describe the change" && git push
```

GitHub Pages publishes `main` within a minute or two. Styles are edited directly in `assets/css/style.css`; images go in `assets/images/` and icons in `assets/icons/`, referenced with paths relative to the page (for example `assets/images/logo.png`).

The privacy policy and terms are versioned (`PRIVACY_VERSION` / `POLICY_VERSION` in the script). When either changes, bump the version, set the new effective date, and add a row to its "Version history" table so users can see what changed and when.
