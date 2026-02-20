# Icons Directory

Place your app icons here for building executables.

## Recommended Icon Sizes

- `icon_16.png` - 16x16px (favicon small)
- `icon_32.png` - 32x32px (favicon)
- `icon_128.png` - 128x128px (macOS)
- `icon_256.png` - 256x256px (macOS, Windows)
- `icon_512.png` - 512x512px (high DPI)
- `icon_1024.png` - 1024x1024px (app store)

## For Windows (.ico)
Create a multi-size .ico file containing:
16x16, 32x32, 48x48, 256x256 pixels

## For macOS (.icns)
Use iconutil to create .icns from iconset:
```bash
mkdir icon.iconset
# Copy icons as icon_16x16.png, icon_32x32.png, etc.
iconutil -c icns icon.iconset
```

## Update build.json
After adding your icon, update build.json:
```json
{
  "icon": "static/icons/icon_256.png"
}
```
