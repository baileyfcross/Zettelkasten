2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# Spring AI Tool Calling Manager

Spring AI's tool calling manager coordinates the application side of a tool-call exchange. It resolves a model-requested tool, executes the corresponding callback, and prepares the result that is returned to the conversation for a subsequent model response.

Central coordination makes error behavior and execution policy easier to control than scattering calls across controllers. The manager does not make a requested action safe by itself; resolution, authorization, timeouts, and result validation remain explicit application responsibilities.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
