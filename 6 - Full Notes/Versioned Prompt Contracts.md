2026-09-27 12:11

Status: #baby

Tags: [[AI Pipeline Engineering]]

# Versioned Prompt Contracts

A versioned prompt contract stores operational instructions in source control and defines the model's role, trusted instruction source, prohibited behavior, and required output structure. It is a dependency of the workflow, not transient text pasted into a chat.

The contract can require exact headings or a JSON schema, forbid invention, and identify untrusted fields as data. Because validation logic depends on the same structure, a prompt change must be reviewed and tested together with its parser and checks. Versioning makes behavioral changes traceable and reversible.

The current source frames prompt version control as one element of prompt governance alongside testing, fairness review, evaluation metrics, and end-user feedback. Its `RelevancyEvaluator` example makes this concrete: a prompt-backed application change can be exercised against a question, the retrieved context, and the generated response, with a failed relevance result becoming release evidence rather than an anecdotal manual observation.

# References

[[agenticaifordevopsengineers.pdf]]
[[masteringspringai.epub]]
