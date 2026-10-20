2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon MongoDB Reactive Driver

Helidon DB Client supports MongoDB through a natively reactive driver. Configuration selects `mongoDb` as the database source and supplies its connection URL, while the application continues to create and use the common `DbClient` abstraction.

MongoDB operations can be expressed as configured JSON statements naming a collection, query, operation, and value. This differs internally from the [[Helidon JDBC Reactive Bridge]] but retains the same configuration-selected application boundary.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
