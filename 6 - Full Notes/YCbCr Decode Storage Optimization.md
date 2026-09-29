2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# YCbCr Decode Storage Optimization

JPEG is encoded in luminance and chrominance components. A browser may retain decoded data in a YCbCr layout rather than immediately expanding every pixel to four-byte RGBA storage.

Keeping the native component structure can reduce memory and postpone or accelerate color conversion during GPU presentation. The benefit is greatest when the chroma planes are subsampled, because fewer color samples need to be stored. See [[JPEG Chroma Subsampling]] and [[Chroma Subsampling Decode Efficiency]].

# References

[[highperformanceimages.pdf]]
