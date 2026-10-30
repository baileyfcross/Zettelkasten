2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Record Shallow Immutability

Java records prevent their component references from being reassigned, but they do not automatically make referenced objects immutable. An array, mutable date, list, or map stored in a record can still be changed through an alias or through the record's accessor.

True value-like behavior therefore depends on component types and defensive copying. A [[Java Record Compact Constructor]] can copy a collection with `copyOf`, while an accessor may need to return a copy of a legacy mutable value. Prefer intrinsically immutable types such as `LocalDate` when the model permits them.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
