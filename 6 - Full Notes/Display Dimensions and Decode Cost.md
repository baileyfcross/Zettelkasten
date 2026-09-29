2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# Display Dimensions and Decode Cost

Sending an image with far more pixels than its rendered dimensions makes the browser decode and often retain samples that cannot contribute to the displayed result. CSS scaling does not recover the wasted transfer, decode, or memory work.

Delivering a source near the needed physical-pixel size reduces all three costs. Responsive candidates and server-side breakpoints make that possible across varied viewports and densities. See [[Responsive Image Selection]] and [[Image Width Breakpoint Budget]].

# References

[[highperformanceimages.pdf]]
