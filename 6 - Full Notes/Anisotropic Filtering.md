2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Anisotropic Filtering

Anisotropic filtering improves texture sampling when a surface is viewed at an oblique angle and its footprint is stretched differently along two directions. It samples a non-square region instead of relying only on one isotropic mip level.

The method preserves distant angled detail that otherwise becomes overly blurred. Higher anisotropy levels use more texture samples and therefore trade additional work for improved quality.

# References

[[gameprogrammingincplusplus.pdf]]
