2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# Image Decode Throughput

Decode throughput relates the number of pixels reconstructed to the time spent decoding them. It exposes a cost that compressed byte size alone hides: a very small file may require substantial computation to expand.

Throughput varies by format, decoder implementation, hardware, and image content. Comparing candidates on the target device is more useful than assuming the format with the best transfer ratio also displays fastest. See [[Image Encoder Throughput Tradeoff]].

# References

[[highperformanceimages.pdf]]
