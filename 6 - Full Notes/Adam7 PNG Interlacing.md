2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# Adam7 PNG Interlacing

Adam7 interlacing divides a PNG into seven passes that progressively fill positions across the image. A decoder can show a coarse approximation before all data arrives and refine it as later passes add samples.

The improved early preview comes with structural overhead and can weaken compression because neighboring data are separated into passes. Interlacing is therefore a delivery tradeoff, not an automatic optimization: it changes presentation order without changing final pixels.

# References

[[highperformanceimages.pdf]]
