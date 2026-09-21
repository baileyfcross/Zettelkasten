2026-09-20 23:34

Status: #baby

Tags: [[Game Input Systems]]

# Relative Mouse Motion

Relative mouse motion reports displacement since the previous input update instead of an absolute cursor position. It supports continuous camera rotation because movement can continue after the pointer would otherwise reach a screen boundary.

A first-person controller commonly hides or captures the cursor and converts horizontal and vertical deltas into yaw and pitch. Sensitivity and frame handling determine how physical motion maps to angular change.

# References

[[gameprogrammingincplusplus.pdf]]
