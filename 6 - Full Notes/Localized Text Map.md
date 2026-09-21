2026-09-20 23:34

Status: #baby

Tags: [[Game User Interface Programming]]

# Localized Text Map

A localized text map associates stable program keys with translated Unicode strings for one language. Interface code requests a key rather than embedding display text, and changing the active map switches the visible language.

Missing keys should be detectable and can fall back to a base language. The renderer must load a font containing the translated glyphs, and layouts must tolerate strings whose length differs from the source.

# References

[[gameprogrammingincplusplus.pdf]]
