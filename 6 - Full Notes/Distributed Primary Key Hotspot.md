2026-11-08 16:45

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Distributed Primary Key Hotspot

A distributed primary-key hotspot occurs when a monotonically increasing key sends every new row to the same ordered key range. The node holding that range's lease receives most writes while other nodes remain underused, defeating the intended horizontal distribution.

Random UUIDs scatter inserts across the keyspace. Time-ordered UUIDs retain some chronological locality while preserving enough variation to distribute work, and a hash-sharded index can spread a required sequential business identifier internally. The appropriate key therefore depends on both identity semantics and the database's physical range layout.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
