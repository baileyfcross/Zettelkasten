2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Event Stream

An event stream is an ordered sequence of events associated with a known identity, commonly one [[Aggregate]] instance. Events must be read in the same strict order in which they were written because replay uses that order to reconstruct state. A stream name can combine the aggregate type and identity. Appending to one stream forms the aggregate's [[Transaction Boundary]], and its revision supplies the expected version for [[Optimistic Concurrency]].

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
