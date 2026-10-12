2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Aggregate Reference by Identity

Aggregate reference by identity stores the identifier of another [[Aggregate]] instead of holding a navigable object reference to it. This makes the [[Consistency Boundary]] explicit: loading one aggregate does not silently load or lock another, and no database foreign-key graph implies that both must change together. Coordination across the identities occurs in the application workflow or through events. Some information may be duplicated when a local snapshot is needed, with synchronization handled explicitly.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
