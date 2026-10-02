2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Evaluation and Monitoring]]

# AI Response Quality Evaluators

AI response quality evaluators examine distinct properties of an answer, such as whether it addresses the request, remains coherent, and is supported by the supplied context. Separating these dimensions matters because a fluent response can be irrelevant, and a relevant response can still introduce unsupported claims.

In Microsoft Foundry, evaluators can be applied to evaluation datasets and compared across runs. Their scores are most useful when paired with row-level inspection, because a single average hides which prompts failed and how. Quality evaluation should guide concrete prompt, retrieval, model, or workflow changes rather than operate as a decorative dashboard.

# References

[[microsoftfoundryinaction.pdf]]
