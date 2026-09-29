2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Model Selection]]

# Forward-Backward Model Search

Forward-backward model search approximately minimizes a selection criterion by alternating single-variable additions and deletions. Starting from an empty model, each step takes the local change that most improves the criterion and stops when neither direction helps.

The procedure avoids enumerating all $2^p$ coordinate subsets and often converges quickly. Its efficiency does not itself provide the statistical guarantees of exact [[Penalized Model Selection]]: the search can stop at a poor local solution. It is best understood as a computational approximation whose quality depends on the criterion and design.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
