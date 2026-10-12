2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Game Property Loading Hook

A game property loading hook is a virtual operation through which an actor or component reads its type-specific fields from parsed level data. Base implementations load common properties, and derived implementations extend that behavior.

The hook separates object construction from configuration and keeps the central loader from depending on every concrete field. Missing optional values can retain defaults, while required values should be validated explicitly.

# References

[[gameprogrammingincplusplus.pdf]]
