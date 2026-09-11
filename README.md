# Red Music Locker — Account Linker

A lightweight browser companion extension for **1-click YouTube Music Account Linking** with your self-hosted [Red Music Locker](https://github.com/jakej985-rgb/red-music-locker) server.

---

## Why Is This Needed?

Google does not provide public OAuth scopes for YouTube Music cloud locker uploads. Uploading private music files requires browser-session authentication tokens (`SAPISIDHASH` and session cookies). 

With this companion extension:
- **No F12 / DevTools needed.**
- **No header copying or pasting.**
- **1-Click account linking directly to your server.**

---

## Installation & Stores

### Option 1: Firefox Add-ons (AMO)
Install the **Red Music Locker — Account Linker** directly from the [Firefox Add-ons Marketplace](https://addons.mozilla.org/).

### Option 2: Chrome / Brave / Edge / Chromium (Developer Mode)
Because Chromium browsers strictly block silent background side-loading of local extensions:
1. Open `chrome://extensions` (or `edge://extensions` / `brave://extensions`).
2. Enable **Developer mode** (toggle in top-right corner).
3. Click **Load unpacked** (top-left button).
4. Select this directory.
5. Pin **Red Music Locker** to your toolbar if desired.

### Option 3: Automated Zero-Install CLI (No Extension Needed)
If you are already signed into YouTube Music in your browser:
```bash
python3 scripts/auto_link_ytm.py
```
This directly connects via the DevTools Protocol and links your account in 1 second.

---

## Packaging for Store Submission

To create a clean submission package validated against Mozilla Add-ons linter:

```bash
./build_package.py
```

The ready-to-upload ZIP package is generated in:
```
dist/red-music-locker-account-linker-v1.1.0.zip
```

- **Submit to Firefox**: [Mozilla Add-on Developer Hub](https://addons.mozilla.org/developers/addon/submit/distribution)
- **Submit to Chrome**: [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole)

---

## Privacy & Permissions

This extension does not track you or collect telemetry. It only accesses `music.youtube.com` cookies locally when you explicitly request an account link, transmitting authentication tokens directly to your self-hosted Red Music Locker server.
