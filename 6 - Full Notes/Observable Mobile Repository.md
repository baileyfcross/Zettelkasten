2026-09-22 23:04

Status: #baby

Tags: [[Mobile Data Synchronization and Notifications]]

# Observable Mobile Repository

An observable mobile repository exposes a stream of data results rather than returning only one final collection. It can publish a cached local result immediately and later publish a refreshed remote result, allowing the view model to react without coordinating both stores directly.

This arrangement separates storage selection from presentation logic. Subscribers still need clear rules for ordering, completion, errors, and whether a later result replaces or merges with the earlier value.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
