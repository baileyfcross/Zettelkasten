2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Game Property Saving Hook

A game property saving hook is a virtual operation that writes an actor's or component's type-specific state into a level record. Base implementations emit shared properties before derived implementations add their own fields.

Using a hook mirrors [[Game Property Loading Hook|loading]] and keeps the world serializer independent from concrete classes. Only durable authoring state should be written; runtime caches and temporary values can be reconstructed.

# References

[[gameprogrammingincplusplus.pdf]]
