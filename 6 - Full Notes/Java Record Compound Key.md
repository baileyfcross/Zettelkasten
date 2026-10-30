2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Record Compound Key

A Java record can combine several values into a single map key. The record supplies component-based `equals` and `hashCode` implementations, so a key such as a person's name and age can be looked up as one typed unit without maintaining a handwritten key class.

Every component participating in the key should remain stable after insertion. [[Java Record Shallow Immutability]] explains why placing mutable arrays or collections inside the record can still break lookup expectations even though the record's own fields are final.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
