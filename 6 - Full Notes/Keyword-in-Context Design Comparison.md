2026-11-11 18:27

Status: #baby

Tags: [[Structured and Modular Software Design]]

# Keyword-in-Context Design Comparison

The keyword-in-context design comparison contrasts two correct decompositions of the same indexing problem. A top-down design follows the operations of reading text, generating shifted lines, sorting them, and printing the result; the alternative defines modules for lines, keyword-line pairs, the index, shifting, and output formatting.

The comparison demonstrates that decomposition is not neutral. A control-flow structure concentrates attention on the current algorithm, while a modular structure can hide storage and sorting decisions so they can change without altering every other stage.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

