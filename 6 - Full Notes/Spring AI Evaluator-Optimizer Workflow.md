2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# Spring AI Evaluator-Optimizer Workflow

An evaluator-optimizer workflow alternates between generating a candidate result and evaluating it against explicit criteria. Feedback from the evaluator becomes input to a revision step until the result passes, reaches an iteration limit, or follows a defined failure path.

The loop is most useful when evaluation criteria can be stated more reliably than a perfect first answer can be generated. Limits and independent checks are necessary because a model-based evaluator may share the generator's blind spots and otherwise create an expensive nonterminating cycle.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
