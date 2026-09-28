2026-09-27 18:30

Status: #baby

Tags: [[Network AI Model and Prompt Engineering]]

# Network Engineering System Message

A network engineering system message establishes the assistant's persistent role, audience, tone, and response obligations. It can require platform-aware explanations, practical examples, explicit assumptions, or a machine-readable return format before the user supplies a particular task.

This message is a behavioral contract, not an access-control mechanism. Telling a model to act as a senior engineer may improve framing but does not give it verified experience or current device state. The system instruction should work with a [[Task-Specific Network Prompt]] and downstream validation rather than being treated as authority.

For a tool-using network assistant, the system message can state the known device context, exact tool-request syntax, obligation to use evidence, and rule to separate confirmed facts from likely causes. It may instruct the model to ask for another tool or return a structured answer. Tool maps, argument validation, loop limits, and command policy still enforce the behavior that text alone cannot guarantee.

# References

[[ainetworkingcookbook.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]
