2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Deferred Shading

Deferred shading separates surface rendering from lighting. The first pass writes visible surface properties into a [[G-Buffer]], and a later pass reads those screen-space values to evaluate global and local lights.

The approach avoids repeating complex geometry work for every light and performs well with many lights. It consumes substantial render-target memory and complicates transparency, which is commonly handled later with forward rendering.

# References

[[gameprogrammingincplusplus.pdf]]
