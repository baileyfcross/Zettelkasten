2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]]

# Integer Overflow

Integer overflow occurs when an arithmetic result lies outside the range of integer values a computer representation can store. A mathematically valid expression can therefore produce an incorrect machine result.

A common [[Binary Search]] implementation calculated the midpoint of lower and upper positions as $(low+high)/2$. Even when both positions were valid, their sum could overflow. The equivalent form $low+(high-low)/2$ avoids forming that excessive intermediate value.

# References

[[algorithms.epub]]
