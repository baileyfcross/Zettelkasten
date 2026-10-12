2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Forward Rendering

Forward rendering shades geometry as it is drawn, producing final color directly rather than first storing surface properties in a [[G-Buffer]]. Each object or material evaluates the lights assigned to that pass.

It handles transparency naturally and avoids the memory overhead of deferred shading. It may be preferable when scenes have few lights or when very high frame rates make the setup and bandwidth of multiple deferred targets too costly.

# References

[[gameprogrammingincplusplus.pdf]]
