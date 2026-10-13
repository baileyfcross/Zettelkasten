2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Unreal Engine VR Rendering Configuration

Unreal Engine's target-hardware and scalability presets establish a conservative starting point for VR by disabling costly defaults such as motion blur, auto exposure, bloom, ambient occlusion, mobile HDR, or separate translucency according to the selected platform. These are initial policy choices, not proof that the project meets its frame budget.

Packaged behavior must be recorded in project configuration rather than relying on editor-only scalability controls. Console variables in `DefaultEngine.ini` can set screen percentage, anti-aliasing quality, or occlusion behavior. Screen percentage is especially important because lens-distortion compensation often renders above the display's native resolution; lowering it trades image detail for GPU time.

Screen-space effects deserve extra scrutiny in stereo because an effect calculated independently from the two eye images can produce a binocular mismatch. [[Forward Rendering]] can provide a sharper multisample anti-aliasing path at high frame rates, whereas [[Deferred Shading]] retains effects and many-light flexibility through its [[G-Buffer]]. The correct configuration follows measurement, target hardware, and the visual needs of the experience.

# References

[[unrealenginevrcookbook.pdf]]

