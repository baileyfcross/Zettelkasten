2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Architectures]]

# Segment-Based Machine Translation

Segment-based machine translation learns correspondences between variable-length sequences rather than translating isolated words. These segments, often called phrases in the statistical literature, need not be complete syntactic phrases; frequent fragments such as “table of” may be useful precisely because the data support them.

Longer units preserve more local context and allow many-to-many mappings that the original IBM models cannot express. The decoder must still select compatible fragments, order them, and use a language model to assemble a fluent sentence. Segment models improve idioms and local structure but require substantially more parallel data and still have trouble with discontinuous dependencies.

# References

[[machinetranslation.epub]]
