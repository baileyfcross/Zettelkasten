2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]]

# Self-Organizing Search

Self-organizing search changes the order of a collection in response to successful searches. Frequently requested items gradually move toward the beginning, reducing the average work when popularity is uneven.

The [[Move-to-Front Algorithm]] immediately moves a found item to the head, while the [[Transposition Method]] swaps it with only its predecessor. Both require a warm-up period in which repeated access reveals the popularity pattern.

# References

[[algorithms.epub]]
