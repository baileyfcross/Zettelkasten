2026-10-04 22:56

Status: #baby

Tags: [[R Iteration Logic and Control Flow]]

# R Missing Value

An R missing value is represented by `NA` and denotes an observation whose value is unknown. Arithmetic and comparisons usually propagate the uncertainty, so testing `x == NA` does not produce an ordinary true-or-false answer; a dedicated missingness test is required.

Summary functions may remove missing values only when explicitly requested. That option changes the set of observations entering the result and should therefore be treated as an analytic decision rather than a cosmetic fix.

# References

[[rstudentcompanion.pdf]]
