2026-11-11 18:27

Status: #baby

Tags: [[Structured and Modular Software Design]]

# Change-Oriented Decomposition

Change-oriented decomposition groups a representation or design decision with the operations that depend on it. Other parts of the program use a defined interface, so replacing the hidden decision does not require rewriting every stage that previously knew its details.

This criterion complements execution-oriented structure. A system still has a control flow, but module boundaries are chosen by anticipated change and [[Information Hiding]], allowing a different indexing, storage, or formatting implementation to remain local to its owner.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

