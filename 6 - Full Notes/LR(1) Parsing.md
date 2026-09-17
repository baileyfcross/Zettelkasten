2026-09-16 22:54

Status: #baby

Tags: [[Context-Free Languages and Parsing]]

# LR(1) Parsing

LR(1) parsing reads input from left to right and reconstructs a right [[Derivation]] in reverse while looking ahead at most one symbol. Its shift operation advances over input, and its reduce operation replaces a recognized production right side with the corresponding nonterminal.

Because reductions build from tokens toward the start symbol, LR(1) is a bottom-up method. It handles useful grammars that are not suitable for [[LL(1) Parsing]] and is a common foundation for compiler parsers.

# References

[[FoundationsOfComputation_2.3.2.pdf]]
