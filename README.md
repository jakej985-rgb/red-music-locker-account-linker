# Red Music Locker — Companion Extension

A lightweight browser companion extension for **1-click YouTube Music Account Linking** with your self-hosted Red Music Locker server.

---

## Why Is This Needed?

Google does not provide public OAuth scopes for YouTube Music cloud locker uploads. Uploading private music files requires browser-session authentication tokens (`SAPISIDHASH` and session cookies). 

With this companion extension:
- **No F12 / DevTools needed.**
- **No header copying or pasting.**
- **1-Click account linking directly to your server.**

---

## Installation

### Option 1: Automated Zero-Install CLI (No Extension Needed — Fastest)
If you are already signed into YouTube Music in your browser, you can link without installing any extensions:
```bash
python3 scripts/auto_link_ytm.py
```
This directly reads the active session via the Chrome DevTools Protocol and links your account in 1 second.

### Option 2: Firefox Add-on (Marketplace)
Install the **Red Music Locker — Account Linker** extension directly from the Firefox Add-ons store with 1 click.

### Option 3: Chrome / Brave / Edge / Chromium (Developer Mode)
Because Chromium browsers strictly block silent background side-loading of local extensions:
1. Open `chrome://extensions` (or `edge://extensions` / `brave://extensions`).
2. Enable **Developer mode** (toggle in top-right corner).
3. Click **Load unpacked** (top-left button).
4. Select this folder:
   ```
   /home/m3tal/Workspaces/ytmusic_sync_helper_ext
   ```
5. Pin **Red Music Locker** to your toolbar if desired.

---

## Usage

### Method A: Direct Sync from Red Music Locker Web UI (Recommended)
1. In Red Music Locker, navigate to **Settings** $\rightarrow$ **1. YouTube Music Connection**.
2. Click **Connect YouTube Music**.
3. A browser tab opens to `music.youtube.com`.
4. The companion extension automatically captures authorization and securely links your account.
5. Return to Red Music Locker — your account is now **Connected**.

### Method B: 1-Click from Extension Popup
1. Sign in to [music.youtube.com](https://music.youtube.com).
2. Click the **Red Music Locker** icon in your browser toolbar.
3. Enter your Red Music Locker server address (e.g. `http://localhost:8080` or `http://localhost:6969`).
4. Click **Link Account Now**.
