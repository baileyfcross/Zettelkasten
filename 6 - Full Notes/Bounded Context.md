2026-09-22 20:53

Status: #baby

Tags: [[Bounded Context and Organizational Design]]

# Bounded Context

A bounded context is the explicit boundary within which one [[Domain Model]] and [[Ubiquitous Language]] are internally consistent. The same word can represent different concepts in other contexts without forcing one object to contain every possible meaning. Inside the boundary, code, tests, data, and conversation share the model; across it, relationships and translations must be deliberate. Clear [[Bounded Context Ownership]] gives a team autonomy to change the model without continuous coordination over its internals.

The architecture source uses bounded contexts to divide a complex solution where the same word can carry different meanings for different expert groups. A domain map then records relationships and translation responsibilities between those models.

The AWS solutions source connects this boundary to microservice design: each service can own the model and data for one business capability, while a context map makes upstream, downstream, partnership, shared-kernel, and translation relationships visible. Splitting services without preserving these semantic boundaries merely distributes one coupled model.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-ondomain-drivendesignwithnetcore.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
