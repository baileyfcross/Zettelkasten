2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Evaluation and Observability]]

# Spring AI ChatModel Observation

Spring AI ChatModel observation instruments the model invocation beneath the ChatClient layer. The source associates it with telemetry such as provider and model identifiers, duration, token usage, request options, errors, and response metadata.

This boundary helps distinguish orchestration delay from provider-call delay and connects resource use to a model request. Attribute selection must balance diagnosis with cardinality, cost, and the sensitivity of prompt-related content.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
