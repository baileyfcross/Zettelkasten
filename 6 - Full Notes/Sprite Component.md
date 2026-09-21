2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Sprite Component

A sprite component attaches a two-dimensional image and drawing behavior to a [[Game Actor]]. It derives its position, scale, and rotation from the actor while storing presentation-specific data such as texture, dimensions, and draw order.

The renderer maintains sprite components in sorted order so the [[2D Painter's Algorithm]] produces the intended layering. An animated specialization can change texture regions over time without altering the actor model.

# References

[[gameprogrammingincplusplus.pdf]]
