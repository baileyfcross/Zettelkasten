2026-09-22 20:53

Status: #baby

Tags: [[Domain Model Building Blocks]]

# Domain Object Factory

A domain object factory is a named function or method that creates a valid [[Value Object]] or [[Domain Entity]]. It can validate input, convert an external representation, and choose a construction path while keeping an invalid intermediate object from escaping. Multiple factories can make different sources explicit, such as constructing a title from plain text or from sanitized HTML. The factory belongs with the domain type when the creation rules are part of the type's meaning.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
