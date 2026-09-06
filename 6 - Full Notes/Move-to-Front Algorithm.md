2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]]

# Move-to-Front Algorithm

The move-to-front algorithm performs a [[Linear Search]] and, after finding the target, moves that item to the head of the list. Repeated access therefore gives popular items positions that can be reached sooner.

An infrequently used item may be promoted once, but later successful searches push it backward again. Compared with the [[Transposition Method]], move-to-front adapts quickly but makes a more abrupt change after every match.

# References

[[algorithms.epub]]
