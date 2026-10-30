2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java Ceiling Division and Modulus

Java ceiling-division and ceiling-modulus methods define integer quotient and remainder relative to rounding toward positive infinity. They complement floor-based operations and make the intended rounding rule explicit when negative operands are possible.

Using a named operation avoids rebuilding the rule from ordinary truncating division and sign corrections. The quotient and remainder belong to the same ceiling convention, so callers should choose them as a pair when reconstructing or partitioning values.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
