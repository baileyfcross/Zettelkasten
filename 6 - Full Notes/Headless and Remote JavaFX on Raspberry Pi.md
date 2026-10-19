2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# Headless and Remote JavaFX on Raspberry Pi

Raspberry Pi development can be performed over SSH so the target does not need a dedicated keyboard or development environment. A developer builds on a faster workstation, copies artifacts to the Pi, and starts the application remotely. NetBeans remote platforms or a Gradle SSH plugin can integrate deployment and execution into the build, avoiding repeated manual SCP steps. Disabling host-key checking may ease a demo but is not appropriate for production.

JavaFX can also render without a conventional window manager through Monocle and the Linux Direct Rendering Manager. Monocle supplies embedded Glass-windowing behavior, while DRM exposes the graphics infrastructure used by the Pi's VC4/V3D driver. This path is distinct from running under Wayland or X11 and is useful for appliance-style interfaces. Architecture-specific native-image delivery is covered by [[JavaFX Raspberry Pi Native Images]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
