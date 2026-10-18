2026-10-18 16:07

Status: #baby

Tags: [[Multimodal Generative AI Media Pipelines]]

# Generated Image Response Encoding

Generated image response encoding determines how the source's 2024 image endpoint returns the artifact reference. The response can contain a URL from which the image is retrieved or a base64-encoded representation embedded in JSON, according to the requested format.

The two forms lead to different Java workflows. A URL requires a second retrieval step and has its own lifetime and network failure behavior; embedded base64 increases response size and must be decoded before ordinary image processing. The client should branch on the declared format instead of guessing from the value, validate successful decoding, and keep the generation metadata associated with the resulting file.

# References

[[chatgptforjava.epub]]
