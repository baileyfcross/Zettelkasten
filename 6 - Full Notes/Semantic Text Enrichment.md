2026-10-11 12:45

Status: #baby

Tags: [[Text Analytics Philosophy and Methods]]

# Semantic Text Enrichment

Semantic text enrichment attaches linguistic labels such as parts of speech or named-entity types to tokens before statistical processing. The annotations allow later rules to distinguish a word’s grammatical role or preserve a recognized person, place, or organization as a meaningful unit.

Enrichment changes the data passed downstream and can create conflicts when several taggers assign incompatible labels. A workflow needs an explicit precedence rule and may mark recognized entities as unmodifiable so later filtering or [[Text Stemming]] does not destroy them.

# References

[[textminingandvisualization.pdf]]
