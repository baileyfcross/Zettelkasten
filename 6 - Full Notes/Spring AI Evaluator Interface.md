2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Evaluation and Observability]]

# Spring AI Evaluator Interface

Spring AI's evaluator interface represents a check over an AI response and its supporting context. An evaluation request can carry the user input, generated answer, and other material needed for an implementation to return an assessment.

The interface makes evaluation composable with Java tests and application workflows, but the meaning of a pass depends on the chosen evaluator and threshold. Teams should preserve the tested prompt, model, evidence, and evaluator version so results remain interpretable.

The current source describes an `EvaluationRequest` carrying the original user text, a list of supporting `Content`, and the response under review. An evaluator returns an `EvaluationResponse` with a pass flag, score, feedback, and metadata. This shape lets the same semantic check run inside JUnit or an administrative endpoint without confusing evaluation output with the generated answer itself.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
