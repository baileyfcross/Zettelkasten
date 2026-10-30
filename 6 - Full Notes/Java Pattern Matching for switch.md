2026-10-30 15:57

Status: #baby

Tags: [[Java Control Flow and Exceptions]]

# Java Pattern Matching for switch

Pattern matching lets a Java switch select branches by runtime type and bind the matched value. A guarded pattern adds a `when` condition after the type match, and record patterns can destructure components directly in a case.

Case order matters when one pattern dominates another more specific pattern. Exhaustiveness becomes especially useful with a [[Java Sealed Type Hierarchy]], because the compiler can verify that all permitted alternatives are covered. A null case must be treated deliberately when null is a possible selector.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
