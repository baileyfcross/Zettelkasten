2026-09-30 17:53

Status: #baby

Tags: [[LLM-Assisted Software Testing]]

# LLM Testing Context Management

LLM testing context management selects and structures the requirements, source modules, analysis findings, tests, and history that fit within a model's bounded input. Functional decomposition and staged retrieval are often more reliable than sending an entire large codebase.

The workflow must preserve relationships that cross chunks and prevent omitted context from being mistaken for absence. Context selection should be logged because different evidence can lead the same model to produce different tests or repair advice.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
