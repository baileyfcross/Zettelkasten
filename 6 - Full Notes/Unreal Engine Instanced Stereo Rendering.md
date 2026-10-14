2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Unreal Engine Instanced Stereo Rendering

Instanced stereo rendering reduces the CPU work of preparing two eye views by submitting geometry for both eyes together rather than building two independent draw streams. The GPU still produces distinct left- and right-eye images, but shared scene work and draw submission can be reused across the pair.

The optimization primarily targets draw-thread overhead, so its benefit depends on where the frame is bound. It may not improve a scene dominated by pixel shading, and the book warns that unsupported rendering features or particular content can make performance worse. It was optional rather than universally enabled in the Unreal Engine version described.

Instanced stereo should therefore be measured in the target project, not assumed to halve rendering cost. [[Unreal Engine VR Performance Diagnosis]] can distinguish a CPU draw bottleneck from a GPU bottleneck before and after enabling it, while visual testing must confirm that both eye views and dependent effects remain correct.

# References

[[unrealenginevrcookbook.pdf]]

