2026-09-30 17:53

Status: #baby

Tags: [[Enterprise RAG and Multi-Agent Applications]] [[Microsoft Foundry Data and Model Design]]

# RAG Generation Stage

The RAG generation stage combines the query, instructions, and retrieved evidence in a prompt so a language model can compose an answer. It may also use ranked context, response templates, citations, and post-processing to make the output useful to an enterprise workflow.

Generation remains probabilistic even when retrieval is accurate. A model can omit or distort evidence, so the system should expose sources, constrain the requested task, and evaluate whether the answer is grounded in the supplied material.

A Foundry agent can reinforce this stage with a system prompt that forbids unsupported extrapolation, requires concise source-aware answers, and defines escalation when retrieved documents do not contain a clear answer. Output groundedness evaluation and guardrails then check whether the generation remained traceable to the evidence rather than merely sounding plausible.

Production evaluation should distinguish context relevance, answer correctness, and faithfulness to the supplied evidence. These measures expose different defects: a generator cannot repair a missing document reliably, and a relevant document does not prevent the model from adding an unsupported conclusion.

The current source's Spring AI example builds a system message from the retrieved document text, appends the current user message, and sends both as one prompt. This makes the boundary visible: search supplies context, prompt construction integrates it, and the model produces the response. Redundant or disjointed retrieved passages can still degrade the answer even when every chunk is individually related to the query.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[microsoftfoundryinaction.pdf]]

[[ultimateaiguideforlinuxengineers.pdf]]
[[masteringspringai.epub]]
