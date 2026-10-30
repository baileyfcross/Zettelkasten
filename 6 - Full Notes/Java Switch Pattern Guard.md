2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Switch Pattern Guard

A Java switch pattern guard adds a Boolean condition to a type or record pattern with `when`. The type match establishes and binds the pattern variable; the guard then refines that match using the variable's value, such as a string length or a numeric range.

Only the first condition is introduced by `when`; additional conditions use ordinary logical operators. Guards make [[Java Pattern Matching for switch]] more expressive, but the compiler cannot prove the semantic ordering of arbitrary Boolean conditions, so developers must place stricter guarded cases before broader ones.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
