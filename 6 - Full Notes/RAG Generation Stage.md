2026-09-30 17:53

Status: #baby

Tags: [[Enterprise RAG and Multi-Agent Applications]] [[Microsoft Foundry Data and Model Design]]

# RAG Generation Stage

The RAG generation stage combines the query, instructions, and retrieved evidence in a prompt so a language model can compose an answer. It may also use ranked context, response templates, citations, and post-processing to make the output useful to an enterprise workflow.

Generation remains probabilistic even when retrieval is accurate. A model can omit or distort evidence, so the system should expose sources, constrain the requested task, and evaluate whether the answer is grounded in the supplied material.

A Foundry agent can reinforce this stage with a system prompt that forbids unsupported extrapolation, requires concise source-aware answers, and defines escalation when retrieved documents do not contain a clear answer. Output groundedness evaluation and guardrails then check whether the generation remained traceable to the evidence rather than merely sounding plausible.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[microsoftfoundryinaction.pdf]]
