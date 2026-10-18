2026-10-18 16:07

Status: #baby

Tags: [[Multimodal Generative AI Media Pipelines]]

# Text-to-Image Request Parameters

Text-to-image request parameters describe an image and configure how the source's 2024 image endpoint should generate it. The prompt is the required semantic input; optional fields select the model, number of results, quality, dimensions, style, response representation, and an end-user identifier.

Compatibility depends on the chosen model, so a Java request should validate combinations rather than expose every field indiscriminately. Dimensions and quality affect the artifact requested, while style changes its visual treatment. The end-user identifier is operationally important when an application lets other people generate images through its API credential because it connects misuse investigation to the initiating user. These details are source-versioned and should be checked during API migration.

# References

[[chatgptforjava.epub]]
