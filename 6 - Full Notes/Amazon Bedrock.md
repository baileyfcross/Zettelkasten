2026-09-27 20:01

Status: #baby

Tags: [[AWS Generative AI and ML Infrastructure]]

# Amazon Bedrock

Amazon Bedrock is a managed service for building generative-AI applications with foundation models from AWS and other providers through a common service layer. It supports model selection, inference, customization, agents, knowledge retrieval, evaluation, and safety controls without requiring customers to operate the model-serving infrastructure. Managed access reduces operational burden, but prompt design, data authorization, output evaluation, and application decisions remain customer responsibilities.

Java applications can reach Bedrock through the AWS SDK or through a framework adapter such as Spring AI. The former exposes service-specific request contracts directly; the latter provides a common model interface. Both approaches still depend on configured AWS identity, region, model access, limits, and provider-aware testing.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]

