2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Responsible AI Controls]]

# Responsible AI Layered Prompts

Responsible AI layered prompts distribute behavioral controls across system instructions, task-specific instructions, retrieved context, and user interaction rather than relying on one warning sentence. The system layer establishes enduring boundaries, while more local layers define the current task, approved evidence, tool constraints, and response expectations.

Layering improves clarity and maintainability, but it is not a substitute for external enforcement. Prompts can guide refusal, disclosure, and uncertainty behavior; identity controls, tool permissions, content filters, and evaluation provide separate defenses. Each layer should have a defined purpose so conflicting instructions do not create an accidental bypass or unusable assistant.

# References

[[microsoftfoundryinaction.pdf]]
