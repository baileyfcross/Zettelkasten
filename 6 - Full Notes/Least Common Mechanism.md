2026-09-13 20:16

Status: #baby

Tags: [[Large-Scale Software Engineering]]

# Least Common Mechanism

The least common mechanism principle minimizes state and mechanisms shared among users or processes. A shared component can become a channel through which one participant corrupts, observes, or interferes with another.

Isolation reduces unintended coupling and simplifies reasoning about failures. Some sharing is necessary, but each common mechanism should have an explicit purpose and strong mediation.

# References

[[computationalthinking.epub]]
