2026-10-18 16:07

Status: #baby

Tags: [[Prompt-Controlled Generative AI Applications]]

# Nucleus Sampling for Generative Responses

Nucleus sampling, exposed as top-p in the source's 2024 chat request, limits next-token selection to a probability mass chosen by the parameter. Lower values consider a narrower set of likely continuations, while higher values admit a broader set.

It is another way to control response variety alongside [[Sampling Temperature for Generative Responses]]. The book advises adjusting one of those controls at a time rather than combining changes whose effects are hard to interpret. A chosen value should be evaluated on the actual task: diversity that helps brainstorming can make a factual summary less consistent, while narrow sampling can reduce variation without guaranteeing correctness.

# References

[[chatgptforjava.epub]]
