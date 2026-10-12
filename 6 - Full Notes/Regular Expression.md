2026-09-16 22:54

Status: #baby

Tags: [[Regular Languages and Finite Automata]] [[Regular Expressions and Stream Editing]]

# Regular Expression

A regular expression is built from ∅, ε, alphabet symbols, union, concatenation, [[Kleene Star]], and grouping. It generates a [[Formal Language]] by interpreting those constructors as the corresponding operations on sets of strings.

A language is regular when some regular expression generates it. Practical search patterns add conveniences such as character classes, optional items, and one-or-more repetition, but features such as backreferences can exceed the power of formal regular expressions.

In Unix text tools, the selected engine and mode determine how the practical pattern is written. Grep and sed distinguish basic and extended regular expressions, while anchors and character classes let a script constrain line positions and sets of characters. Literal input should use fixed-string matching when regex interpretation is unnecessary.

# References

[[ultimatelinuxshellscriptingguide.pdf]]

[[FoundationsOfComputation_2.3.2.pdf]]
