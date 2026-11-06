2026-09-06 00:13

Status: #baby

Tags: [[Algorithm Complexity Analysis]]

# Big O Notation

Big O notation expresses an upper bound on how an algorithm's resource requirement grows for sufficiently large inputs. Writing $O(f(n))$ means that beyond some input threshold, the requirement is no more than a constant multiple of $f(n)$.

The notation emphasizes growth rather than exact machine time or small-input details. It makes complexity families such as [[Linear Time Complexity|$O(n)$]], [[Loglinear Time Complexity|$O(n\log n)$]], and [[Exponential Time Complexity|$O(a^n)$]] directly comparable.

Asymptotic class is a scaling signal, not a complete engineering verdict. Constants, memory locality, data volume, allocation, and how often the operation runs can make a simple linear method preferable for a tiny input even when a more elaborate structure offers a better class at large scale.

# References

[[algorithms.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
