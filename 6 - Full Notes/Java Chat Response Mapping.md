2026-10-18 16:07

Status: #baby

Tags: [[Java OpenAI API Integration]]

# Java Chat Response Mapping

Java chat response mapping converts the JSON returned by the book's 2024 chat interface into typed application data. The response identifies the request and model, contains one or more indexed choices with generated messages, records a [[Chat Completion Finish Reason]], and reports [[API Token Usage Metadata]].

Mapping the envelope prevents application code from treating a raw JSON string as if it were only generated text. The caller can select the intended choice, check whether generation completed normally, and account for usage before exposing the content. The mapping must remain version-aware because renamed fields or a different response shape can otherwise fail silently or extract the wrong node.

# References

[[chatgptforjava.epub]]
