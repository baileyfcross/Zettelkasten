2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Forward Rendering

Forward rendering shades geometry as it is drawn, producing final color directly rather than first storing surface properties in a [[G-Buffer]]. Each object or material evaluates the lights assigned to that pass.

It handles transparency naturally and avoids the memory overhead of deferred shading. It may be preferable when scenes have few lights or when very high frame rates make the setup and bandwidth of multiple deferred targets too costly.

VR can favor a forward path because its strict frame budget limits the expensive screen-space effects that motivate a full deferred pipeline, and hardware multisample anti-aliasing can preserve sharp geometric edges without the softness of temporal post-processing. The tradeoff remains light complexity: a basic forward shader may revisit many lights for every fragment. Tiled or clustered light assignment narrows that loop to lights affecting a screen region or view-space cluster.

# References

[[gameprogrammingincplusplus.pdf]]
[[unrealenginevrcookbook.pdf]]
