2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Evaluation and Observability]]

# Spring AI Relevancy Evaluator

Spring AI's relevancy evaluator assesses whether a generated response addresses the supplied user question. The source presents it as an automated way to make response relevance part of repeatable Java evaluation rather than an informal visual judgment.

Relevance is only one quality dimension: an answer can be on topic yet unsupported or false. Evaluation suites should combine this signal with groundedness, factual checks, safety criteria, and representative human-reviewed cases.

In the current source, `RelevancyEvaluator` builds an evaluation prompt from the user's question, the retrieved documents stored in response metadata, and the generated response. It interprets the evaluator model's yes-or-no judgment as a pass and a score. Examples with an in-domain bike question and an unrelated corporate question show how the check can reject a response whose retrieved context does not support the requested subject.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
