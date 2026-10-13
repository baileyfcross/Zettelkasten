2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Hidden Area Mesh Optimization

A hidden area mesh marks regions of an eye render target that the headset's lens and distortion process will never show. Rejecting those pixels before expensive shading avoids rendering into the corners and other portions outside the usable optical field.

The optimization can also limit post-processing to the visible region. Its mask is device-dependent because lens shape, field of view, and distortion determine which source pixels survive the final warp. The runtime or engine can supply this geometry automatically, so application content does not need to approximate it.

Hidden-area culling saves work without changing the intended visible image, but it addresses only overdraw outside the lens-visible region. It does not reduce the cost of complex visible materials, excessive draw calls, or an unnecessarily high screen percentage, all of which require separate profiling and rendering decisions.

# References

[[unrealenginevrcookbook.pdf]]

