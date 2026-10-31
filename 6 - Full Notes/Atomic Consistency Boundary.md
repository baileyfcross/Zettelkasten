2026-10-30 17:24

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Atomic Consistency Boundary

An atomic consistency boundary encloses changes that can commit or roll back as one ACID transaction. In the book's monolithic example, booking and inventory modules update tables inside one database transaction, so either both changes persist or neither does.

Splitting those modules and tables into independently deployed services also splits this boundary. Treating the old transaction as if it still exists hides failure cases between successful local commits.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

