2026-09-05 16:28

Status: #baby

Tags: [[Dialog Management Systems]] · [[Machine Translation Architectures]]

# Ambiguity Resolution

Ambiguity resolution selects among multiple plausible interpretations of a user's input. Evidence can come from recognition confidence, syntax, domain knowledge, prior turns, personal context, and available actions.

When the evidence is insufficient, the safest resolution is often a [[Clarification Question]]. The cost of an extra turn should be weighed against the consequence of executing the wrong service action.

Translation exposes ambiguity at every level: a word may have several senses, a phrase may attach to different parts of a sentence, and an idiom may not mean what its component words suggest. Dictionaries can enumerate possibilities but cannot select among them. Statistical translation uses domain and neighboring expressions as evidence, while neural translation learns contextual representations; both work best on frequent patterns and can still fail when the needed world knowledge is absent.

# References

[[aiassistants.epub]]

[[machinetranslation.epub]]
