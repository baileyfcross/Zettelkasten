2026-09-28 04:01

Status: #baby

Tags: [[Digital Image Representation and Quality]]

# RGB and Luma-Chroma Color Spaces

RGB represents a pixel through red, green, and blue intensities. Luma-chroma spaces such as YCbCr instead separate a brightness-like component from color-difference components.

That separation is useful for compression because human vision is generally more sensitive to changes in brightness than to equally fine changes in color. Formats such as JPEG can retain full luma detail while reducing chroma resolution through [[JPEG Chroma Subsampling]]. The conversion is a representational step; the displayed result is converted back to RGB.

# References

[[highperformanceimages.pdf]]
