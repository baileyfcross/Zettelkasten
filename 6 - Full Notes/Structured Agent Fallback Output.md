2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Safety and Autonomy]]

# Structured Agent Fallback Output

A structured agent fallback preserves the output contract when model output is invalid. If JSON parsing, required-field checks, enumeration checks, or range checks fail, application code emits a known safe result with an unknown or medium-risk classification, zero confidence, and a recommendation for manual inspection.

The fallback prevents downstream parsers from failing unpredictably or treating missing data as success. It does not disguise the model error: the output explicitly records that validation failed and directs the workflow toward a conservative path.

# References

[[agenticaifordevopsengineers.pdf]]
