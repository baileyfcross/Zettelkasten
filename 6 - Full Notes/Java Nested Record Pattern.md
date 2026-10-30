2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Nested Record Pattern

A nested Java record pattern deconstructs a record and records contained within it in one declarative pattern. It replaces a chain of accessor calls, temporary variables, and intermediate null checks with a structural description of the components needed by the operation.

Matching fails when a required nested record is absent, while matched component variables become directly available to the guarded block or switch arm. Components that are present but themselves contain `null` can still fail when used, so deconstruction does not make every component value intrinsically null-safe.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
