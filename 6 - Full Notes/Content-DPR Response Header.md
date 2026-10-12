2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Content-DPR Response Header

When an image service returns a representation at a density different from the density implied by the request, Content-DPR can communicate the density actually selected in the response model described by the book.

That feedback lets the client calculate the image’s intrinsic CSS dimensions consistently instead of treating physical pixels as one-to-one CSS pixels. It is particularly relevant when the server deliberately reduces density for bandwidth or memory reasons. See [[Device-Pixel-Ratio Client Hint]].

# References

[[highperformanceimages.pdf]]
