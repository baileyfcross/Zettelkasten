2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Unnamed Variable and Pattern

Java uses the single underscore to mark a binding or pattern component as intentionally unused and unusable. It can replace an unused local, catch variable, lambda parameter, pattern variable, or an entire component of a record pattern, depending on the construct.

The notation communicates that a value participates in the required shape but not in the calculation. It avoids misleading placeholder names such as `ignored` and lets a [[Java Nested Record Pattern]] focus on the one coordinate or component the operation actually needs.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
