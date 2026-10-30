2026-10-30 15:57

Status: #baby

Tags: [[Java Control Flow and Exceptions]]

# Java Pattern Matching for switch

Pattern matching lets a Java switch select branches by runtime type and bind the matched value. A guarded pattern adds a `when` condition after the type match, and record patterns can destructure components directly in a case.

Case order matters when one pattern dominates another more specific pattern. Exhaustiveness becomes especially useful with a [[Java Sealed Type Hierarchy]], because the compiler can verify that all permitted alternatives are covered. A null case must be treated deliberately when null is a possible selector.

A `when` guard participates only after the case's type pattern has matched, so it can use the bound variable. An unguarded broad type case must follow narrower cases it would dominate, while enum constants may be qualified when several enum types participate in a pattern-oriented switch.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
