2026-09-28 04:01

Status: #baby

Tags: [[JPEG Encoding and Optimization]]

# MozJPEG Optimization

MozJPEG is an encoder focused on producing smaller, web-oriented JPEGs through improved quantization, entropy optimization, and progressive scan choices. It can spend more computation during encoding to reduce transfer size or improve visual quality at a target size.

That extra computation is attractive in an offline build pipeline but may be costly in a latency-sensitive dynamic image service. Encoder selection should therefore consider both output efficiency and throughput. See [[Image Encoder Throughput Tradeoff]] and [[Static Derivative Image Build Pipeline]].

# References

[[highperformanceimages.pdf]]
