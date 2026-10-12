2026-09-05 16:28

Status: #baby

Tags: [[Natural Language Understanding Systems]] · [[Context-Free Languages and Parsing]]

# Context-Free Grammar

A context-free grammar describes how symbols can be combined using production rules. Terminal symbols correspond to words or tokens, while nonterminal symbols represent categories such as phrases, slots, or requests.

For a narrow assistant domain, a grammar can both recognize valid utterances and construct a [[Meaning Representation]]. Coverage and maintenance become difficult as users introduce unanticipated wording.

Formally, a context-free grammar is a four-tuple containing nonterminal symbols, terminal symbols, [[Production Rule|production rules]], and a start symbol. Starting from that symbol, a [[Derivation]] generates a language by repeatedly replacing a nonterminal without regard to its surrounding context.

# References

[[aiassistants.epub]]

[[FoundationsOfComputation_2.3.2.pdf]]
