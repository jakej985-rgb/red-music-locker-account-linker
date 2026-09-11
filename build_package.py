#!/usr/bin/env python3
"""
Red Music Locker Account Linker — Packaging Script
Produces clean packages for:
1. Firefox (AMO) — Strictly adheres to Mozilla MV3 (no service_worker warning)
2. Chrome (Web Store / Unpacked) — Strictly adheres to Chrome MV3 (no background.scripts warning, no pem files)
"""

import copy
import json
import shutil
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

COMMON_FILES = [
    "background.js",
    "content.js",
    "popup.html",
    "popup.js",
    "README.md",
]

def build_target(target_name: str, manifest_data: dict, output_zip: Path, unpacked_dir: Path = None):
    print(f"\n--- Building {target_name} Package ---")
    
    if unpacked_dir:
        if unpacked_dir.exists():
            shutil.rmtree(unpacked_dir)
        unpacked_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED) as z:
        # Write modified manifest
        manifest_str = json.dumps(manifest_data, indent=2)
        z.writestr("manifest.json", manifest_str)
        if unpacked_dir:
            (unpacked_dir / "manifest.json").write_text(manifest_str, encoding="utf-8")
        print("  + manifest.json")

        # Write common files
        for f in COMMON_FILES:
            p = ROOT_DIR / f
            if p.exists():
                z.write(p, arcname=f)
                if unpacked_dir:
                    shutil.copy2(p, unpacked_dir / f)
                print(f"  + {f}")

        # Write icons
        icons_dir = ROOT_DIR / "icons"
        if icons_dir.exists():
            if unpacked_dir:
                (unpacked_dir / "icons").mkdir(exist_ok=True)
            for icon in sorted(icons_dir.glob("icon*.png")):
                z.write(icon, arcname=f"icons/{icon.name}")
                if unpacked_dir:
                    shutil.copy2(icon, unpacked_dir / "icons" / icon.name)
                print(f"  + icons/{icon.name}")

    size_kb = output_zip.stat().st_size / 1024
    print(f"  => Created {output_zip.name} ({size_kb:.1f} KB)")
    if unpacked_dir:
        print(f"  => Unpacked folder for testing: {unpacked_dir}")

# 1. Firefox Target: Use scripts, remove service_worker
firefox_manifest = copy.deepcopy(manifest)
if "background" in firefox_manifest and "service_worker" in firefox_manifest["background"]:
    del firefox_manifest["background"]["service_worker"]

firefox_zip = DIST_DIR / f"red-music-locker-account-linker-firefox-v{version}.zip"
build_target("Firefox (AMO)", firefox_manifest, firefox_zip)

# 2. Chrome Target: Use service_worker, remove scripts and browser_specific_settings
chrome_manifest = copy.deepcopy(manifest)
if "background" in chrome_manifest and "scripts" in chrome_manifest["background"]:
    del chrome_manifest["background"]["scripts"]
if "browser_specific_settings" in chrome_manifest:
    del chrome_manifest["browser_specific_settings"]

chrome_zip = DIST_DIR / f"red-music-locker-account-linker-chrome-v{version}.zip"
chrome_unpacked = DIST_DIR / "chrome-unpacked"
build_target("Chrome (Web Store / Unpacked)", chrome_manifest, chrome_zip, unpacked_dir=chrome_unpacked)

print("\n========================================================")
print(" Build Complete!")
print(f" Firefox package : {firefox_zip}")
print(f" Chrome package  : {chrome_zip}")
print(f" Chrome unpacked : {chrome_unpacked} (Load this in chrome://extensions)")
print("========================================================\n")
