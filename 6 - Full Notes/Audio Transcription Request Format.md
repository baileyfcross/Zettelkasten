2026-10-18 16:07

Status: #baby

Tags: [[Multimodal Generative AI Media Pipelines]]

# Audio Transcription Request Format

An audio transcription request format carries a binary media file and transcription options in a multipart form submission. In the source's 2024 Whisper interface, the file and model are required form parts, while language, prompt, response format, and sampling temperature are optional.

This differs from the JSON body used by the book's chat and image-generation examples. A Java client must therefore choose an HTTP library and request builder that can stream file bytes and text fields with the correct multipart boundaries. Serializing the same values as JSON is not an equivalent request. The transport representation is part of the endpoint contract and should be tested independently of the transcription result.

# References

[[chatgptforjava.epub]]
