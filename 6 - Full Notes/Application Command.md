2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]]

# Application Command

An application command is a message that asks the system to perform an action that may change state. It captures [[Command Intent]] in a serializable form, such as creating an item or changing its price, without containing the business behavior itself. A [[Command Handler]] or [[Application Service]] converts command values into domain types and invokes an [[Aggregate]]. Successful processing can produce one or more [[Domain Event]]s; rejection leaves the model in a valid state.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
