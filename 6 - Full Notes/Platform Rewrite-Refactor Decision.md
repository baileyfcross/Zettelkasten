2026-10-03 22:25

Status: #baby

Tags: [[Platform Technical Debt and Evolution]]

# Platform Rewrite-Refactor Decision

A platform rewrite-refactor decision asks whether an existing component can reach the desired state through bounded internal change or must be replaced with a new implementation. Refactoring is appropriate when interfaces, efficiency, security, or maintainability can improve without discarding the working base.

Rewrite or replacement becomes plausible when the current system cannot satisfy required behavior without expanding brittle glue, when its dependency path is untenable, or when operating toil prevents the team from scaling. The decision must include user migration, overlap, lost functionality, cost, new maintenance, and rollback; starting fresh does not erase those transition obligations.

# References

[[platformengineeringforarchitects.pdf]]
