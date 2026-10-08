2026-09-21 22:12

Status: #baby

Tags: [[Software Design Principles]] [[R Software Testing]]

# Don't Repeat Yourself Principle

Don't Repeat Yourself (DRY) asks that a single rule or behavior have one authoritative representation. Copying code into several classes makes a change require coordinated edits and creates opportunities for the copies to diverge. A shared abstraction can remove that burden when the copies express the same underlying requirement; superficially similar code should not be forced together if it changes for different reasons.

In R analysis code, duplicated plot settings or calculations can diverge when a later change reaches only some copies. A repeated value can become a variable or deliberate global setting, while a repeated procedure can become an [[R Function]]. The useful abstraction is the shared decision itself: consolidating accidental surface similarity can make code harder to understand, but leaving one policy in many locations invites inconsistent results and tests.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[testingrcode.pdf]]
