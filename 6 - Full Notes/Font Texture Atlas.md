2026-09-20 23:34

Status: #baby

Tags: [[Game User Interface Programming]]

# Font Texture Atlas

A font texture atlas packs many pre-rendered glyphs into one texture. Text rendering submits character-sized quads whose texture coordinates select the required glyph regions.

The atlas reduces texture creation and switching when strings change. It must cover the needed writing systems or support additional pages, since localization can require far more glyphs than a small Latin-only set.

# References

[[gameprogrammingincplusplus.pdf]]
