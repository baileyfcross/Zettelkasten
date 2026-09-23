2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]]

# Command Dispatch

Command dispatch selects the [[Command Handler]] or [[Application Service]] operation responsible for an [[Application Command]]. A dispatcher can keep controllers from depending on every handler directly and can resolve only the dependency needed for the current request. This indirection should remain mechanical: it routes the command but does not decide whether the requested business transition is valid. That decision belongs to the target [[Aggregate]] and its invariants.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
