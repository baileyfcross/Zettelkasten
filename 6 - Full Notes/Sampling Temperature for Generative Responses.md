2026-10-18 16:07

Status: #baby

Tags: [[Prompt-Controlled Generative AI Applications]]

# Sampling Temperature for Generative Responses

Sampling temperature controls how strongly a generative model favors its highest-probability next-token choices. The source presents lower values as producing more predictable responses and higher values as allowing more varied output within the endpoint's supported range.

Temperature is a response-generation parameter, not a property of the prompt text. A summarizer that needs stable, concise language may use a different setting from an image-description brainstorm. Results still require evaluation because lower randomness does not make an answer factually correct. The book recommends tuning either temperature or [[Nucleus Sampling for Generative Responses|top-p nucleus sampling]] rather than changing both at once, so an observed effect can be attributed to one control.

# References

[[chatgptforjava.epub]]
