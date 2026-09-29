2026-09-28 04:01

Status: #baby

Tags: [[JPEG Encoding and Optimization]]

# Progressive JPEG Scan Design

Progressive JPEG scans can divide information by spectral selection, transmitting groups of DCT coefficients, or by successive approximation, transmitting coarse coefficient bits before refinements. Encoders can combine these strategies.

A good scan script puts visually important low-frequency information early while preserving efficient entropy coding across later scans. Too many poorly chosen scans add headers and work without improving the useful preview. Progressive optimization is therefore about ordering information, not merely flipping a format flag. See [[Sequential and Progressive JPEG]].

# References

[[highperformanceimages.pdf]]
