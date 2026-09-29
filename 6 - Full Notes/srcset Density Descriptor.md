2026-09-28 04:01

Status: #baby

Tags: [[Responsive Image Selection]]

# srcset Density Descriptor

The `x` descriptor in `srcset` associates each candidate with a pixel-density multiplier such as 1x or 2x. It is appropriate when the image’s CSS display dimensions are effectively fixed.

The browser compares candidates with the device’s density and other internal constraints, then chooses one URL. The descriptor does not force an exact choice and should not be used to describe arbitrary source widths for a fluid slot. See [[Fixed and Variable Responsive Image Dimensions]].

# References

[[highperformanceimages.pdf]]
