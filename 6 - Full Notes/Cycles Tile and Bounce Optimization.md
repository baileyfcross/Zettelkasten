2026-09-28 20:13

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Cycles Tile and Bounce Optimization

Cycles render time can be reduced by limiting how many times rays bounce and by choosing tile dimensions suited to the rendering device. The book recommends testing lower maximum, diffuse, glossy, transmission, and volume bounce limits rather than assuming the highest defaults are visibly necessary.

For the Blender 2.7x tile renderer, power-of-two tile sizes were efficient, with larger tiles generally favored for GPU work. These are tuning rules, not guarantees; representative scene tests should decide the final settings.

# References

[[howtocheatinblender27x.pdf]]
