2026-09-22 20:53

Status: #baby

Tags: [[Domain Model Building Blocks]]

# Domain Service

A domain service expresses domain behavior that does not naturally belong to one entity or value object. Its interface is defined inside the domain model using the [[Ubiquitous Language]], while an implementation that calls a database or remote system can remain in the [[Application Layer]]. This direction keeps the model free of infrastructure dependencies. Domain services should not become a place to move all behavior out of entities; they are for genuine domain operations whose responsibility spans or sits outside individual objects.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
