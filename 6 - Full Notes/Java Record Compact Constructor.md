2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Record Compact Constructor

A Java record compact constructor validates or normalizes record components without repeating the canonical constructor's parameter list or field assignments. Its body runs during construction, and the compiler assigns the final component values after that body completes.

The form is useful for enforcing invariants such as an interval's lower bound not exceeding its upper bound or RGB components remaining in range. Parameters may also be reassigned to normalized values before the implicit assignment, but a compact constructor should keep the value semantics of the surrounding [[Java Record Type]] clear.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
