2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]] [[CQRS Query and Read Model Design]]

# Command Query Responsibility Segregation

Command Query Responsibility Segregation (CQRS) separates operations that change state from operations that retrieve it. An inventory application can use command handlers for saving or deleting a product and query handlers for listing or finding products. Separate models can be optimized for writes and reads, even in different services or stores, but the added coordination is justified only when a simpler shared model is insufficient.

The separation can begin in one application and one database. The command side loads an [[Aggregate]] through the [[Repository Pattern]] and protects its invariants, while an [[Application Query]] returns a purpose-specific [[Read Model]] without reconstructing the behavioral model. Separate storage is an optional later optimization, not part of the definition.

The book describes CQRS as separating update commands from read queries when their specifications and performance needs differ. Its strongest form can give each side distinct models or stores, accepting synchronization cost for independent optimization.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-ondomain-drivendesignwithnetcore.pdf]]
