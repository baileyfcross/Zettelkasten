2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Evaluation and Observability]]

# Java LLM Continuous Evaluation

Java LLM continuous evaluation runs representative quality checks whenever prompts, models, retrieval data, tools, or application code change. It extends ordinary build verification with assertions about generated behavior that compilation and deterministic unit tests cannot cover.

The suite should control cost and variance while retaining meaningful failure artifacts. A small stable gate can run in continuous integration, while broader scheduled evaluations and production sampling detect regressions that a fixed test set misses.

The current source implements one such gate as a Spring Boot JUnit test. It sends a question through a RAG advisor, passes the question, retrieved documents, and response to a relevancy evaluator, and asserts that the evaluation passes. A separate administrative endpoint exposes the answer, pass state, score, and feedback for investigation, while role-based access in the production example keeps evaluation controls separate from ordinary user queries.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
