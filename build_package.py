#!/usr/bin/env python3
"""
Red Music Locker Account Linker — Packaging Script
Creates a clean, production-ready .zip package for submission to:
- Mozilla Firefox Add-ons (AMO)
- Chrome Web Store / Edge Add-ons
"""

import json
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()
MANIFEST_PATH = ROOT_DIR / "manifest.json"

if not MANIFEST_PATH.exists():
    raise FileNotFoundError(f"manifest.json not found in {ROOT_DIR}")

manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
version = manifest.get("version", "1.0.0")

DIST_DIR = ROOT_DIR / "dist"
DIST_DIR.mkdir(exist_ok=True)
ZIP_NAME = f"red-music-locker-account-linker-v{version}.zip"
ZIP_PATH = DIST_DIR / ZIP_NAME

# Files and directories to package
FILES_TO_PACK = [
    "manifest.json",
    "background.js",
    "content.js",
    "popup.html",
    "popup.js",
    "README.md",
]

print("========================================================")
print(f"  Packaging Red Music Locker Account Linker v{version}")
print("========================================================")

with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for f in FILES_TO_PACK:
        p = ROOT_DIR / f
        if p.exists():
            z.write(p, arcname=f)
            print(f"  + {f}")
        else:
            print(f"  ⚠️ Warning: {f} not found!")

    # Include all icons except master/raw files
    icons_dir = ROOT_DIR / "icons"
    if icons_dir.exists():
        for icon in sorted(icons_dir.glob("icon*.png")):
            z.write(icon, arcname=f"icons/{icon.name}")
            print(f"  + icons/{icon.name}")

size_kb = ZIP_PATH.stat().st_size / 1024
print("========================================================")
print(f"🎉 Successfully built package:")
print(f"   👉 {ZIP_PATH} ({size_kb:.1f} KB)")
print("========================================================")
print("Ready for upload to:")
print("  • Firefox Add-on Developer Hub: https://addons.mozilla.org/developers/addon/submit/distribution")
print("  • Chrome Web Store Developer Dashboard: https://chrome.google.com/webstore/devconsole")
print("========================================================")
