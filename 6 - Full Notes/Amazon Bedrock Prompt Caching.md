2026-09-27 20:01

Status: #baby

Tags: [[AWS Generative AI and ML Infrastructure]]

# Amazon Bedrock Prompt Caching

Amazon Bedrock prompt caching reuses frequently repeated prompt context so the model does not need to process the same tokens from scratch on every request. Reuse can lower latency and inference cost for applications with stable instructions, documents, or repeated prefixes. Cache design must respect freshness and data boundaries: content that changes or differs by user should not be reused merely because it looks similar.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

