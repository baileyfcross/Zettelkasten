2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java String Split with Delimiters

Java's delimiter-preserving split operations divide text with a regular expression while retaining the matched separators in the result. Ordinary split discards the boundaries, which loses information needed by tokenizers, editors, or round-trip transformations.

Both string- and pattern-oriented forms expose the same idea. The caller receives alternating content and matched delimiter pieces and can decide whether to interpret, replace, or reproduce each separator.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
