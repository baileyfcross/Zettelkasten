2026-09-15 18:17

Status: #baby

Tags: [[Compositing and Keying]]

# Holdout Mattes in Layered Composites

When a foreground element covers part of a background, the foreground's matte identifies where it contributes and a complementary holdout removes that same region from the background. These paired masks let the images meet without both contributing full intensity at an overlap. Their edge values should agree: mismatched mattes create seams even if the RGB colors are well matched. The arrangement is the geometric side of an over composite, distinct from later color and lighting corrections. It relies on the coverage represented by an [[Alpha Channel as Compositing Matte]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
