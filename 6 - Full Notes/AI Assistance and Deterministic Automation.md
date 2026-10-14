2026-09-27 12:11

Status: #baby

Tags: [[AI-Assisted DevOps Practice]]

# AI Assistance and Deterministic Automation

Generative AI produces new text, code, and configuration from learned patterns, while conventional [[Automation]] executes predefined rules. The first is probabilistic and context-dependent; the second should be repeatable enough that the same conditions produce an expected result or failure.

A safe DevOps workflow uses each where its character is useful. AI may interpret a log or draft a pipeline, but deterministic code validates the syntax, enforces policy, and performs approved execution. Treating an LLM as interchangeable with automation hides uncertainty inside a system that depends on predictability.

In NetOps, a mature script should continue collecting interface or BGP state predictably, while the agent decides which approved observation would help an investigation and summarizes the results. Fixed checks, policy enforcement, filtering, and execution remain deterministic. Agents are justified when the next information need depends on changing evidence; replacing a reliable fixed workflow with model reasoning only enlarges the failure surface.

The same selection rule applies to Linux operations: use deterministic automation for stable, frequent, low-latency work with defined inputs and outcomes, and introduce AI where unstructured evidence, changing requirements, or contextual interpretation genuinely matter. Even then, the model should propose an artifact or plan that ordinary syntax, policy, dry-run, diff, and post-condition checks can verify.

# References

[[agenticaifordevopsengineers.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]

[[ultimateaiguideforlinuxengineers.pdf]]
