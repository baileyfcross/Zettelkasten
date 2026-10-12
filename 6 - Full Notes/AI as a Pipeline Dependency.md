2026-09-27 12:11

Status: #baby

Tags: [[AI Pipeline Engineering]]

# AI as a Pipeline Dependency

An AI service inside CI/CD is a production dependency rather than an informal assistant. Its model endpoint, credentials, latency, availability, cost, output behavior, and failure modes can affect the delivery path and therefore require explicit engineering controls.

The integration should define fixed inputs, scoped secrets, versioned prompts, validation, retry limits, observable results, and clear failure behavior. Treating the service like any other dependency shifts attention from the novelty of generated text to the reliability of the contract through which the pipeline uses it.

# References

[[agenticaifordevopsengineers.pdf]]
