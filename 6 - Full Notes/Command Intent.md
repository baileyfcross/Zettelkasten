2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]]

# Command Intent

Command intent is the requested action expressed by an actor, another system, or a timer. It differs from a [[Domain Event]]: a command can be rejected, while an event states that something already happened. Naming an [[Application Command]] with an imperative verb makes the desired action explicit and lets the domain decide whether its current state permits it. This preserves the distinction between asking for a transition and recording the resulting fact.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
