2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Unreal Engine VR Performance Diagnosis

VR performance diagnosis begins by identifying which thread or processor determines frame time. Unreal Engine's `Stat Unit` separates the game thread, draw thread, and GPU. The largest time identifies whether optimization should begin with gameplay simulation, draw submission, or rendering rather than with an arbitrary graphics setting.

A GPU-bound frame can be decomposed with the GPU Visualizer or `ProfileGPU` to find expensive passes and effects. A draw-thread bottleneck suggests excessive draw calls or object count and can be inspected with `Stat SceneRendering`; merging suitable geometry or using [[Unreal Engine Instanced Stereo Rendering|stereo instancing]] may help. A game-thread bottleneck instead requires examining gameplay work with `Stat Game`.

The method is evidence driven: establish the headset's frame-time budget, locate the limiting stage, make one targeted change, and measure again. Runtime features such as reprojection may conceal occasional misses, but they do not turn an over-budget application into a consistently comfortable one.

# References

[[unrealenginevrcookbook.pdf]]

