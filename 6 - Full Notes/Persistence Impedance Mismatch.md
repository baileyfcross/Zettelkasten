2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Persistence Impedance Mismatch

Persistence impedance mismatch is the tension between a domain object's natural structure and the shapes or construction rules required by a storage system. A document database may require a string identity or serializer-friendly constructor, while a relational database maps object composition into tables and foreign keys. An object-relational mapper reduces some mechanical work but does not remove the mismatch. The model should keep storage compromises explicit so persistence concerns do not quietly turn a [[Domain Model]] into an [[Anemic Domain Model]].

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
