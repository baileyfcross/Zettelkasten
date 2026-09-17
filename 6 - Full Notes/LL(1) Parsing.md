2026-09-16 22:54

Status: #baby

Tags: [[Context-Free Languages and Parsing]]

# LL(1) Parsing

LL(1) parsing reads input from left to right and constructs a left [[Derivation]] while using at most one lookahead symbol to select each [[Production Rule]]. It is a top-down method because it expands the start symbol toward the input string.

An LL(1) grammar must make the correct alternative identifiable from the current nonterminal and next input token. This restriction excludes some unambiguous grammars but makes predictive parsers straightforward to implement.

# References

[[FoundationsOfComputation_2.3.2.pdf]]
