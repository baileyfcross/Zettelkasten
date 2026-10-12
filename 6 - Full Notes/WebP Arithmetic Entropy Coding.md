2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# WebP Arithmetic Entropy Coding

After prediction and transform coding, lossy WebP uses arithmetic entropy coding to represent symbols according to their probabilities. The output approaches the information content of the symbol stream more closely than a code restricted to an integral number of bits per symbol.

JPEG standardized an arithmetic option, but the broadly deployed JPEG ecosystem centered on Huffman decoding. WebP could adopt arithmetic coding from the start because its compatibility baseline was new. See [[JPEG Huffman Entropy Coding]].

# References

[[highperformanceimages.pdf]]
