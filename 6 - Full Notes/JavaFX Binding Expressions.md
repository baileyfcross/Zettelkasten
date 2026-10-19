2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Reactive UI Composition]]

# JavaFX Binding Expressions

A JavaFX `Binding` represents a lazily evaluated value with one or more observable dependencies. When a dependency is invalidated, the binding becomes invalid. A later `get()` recomputes and caches the value until another dependency changes. Attaching a change listener forces eager evaluation because old and new values must be available.

Bindings can be created by extending a type-specific binding class, by calling the many factory methods in `Bindings`, or through fluent operations on observable expressions. Bindings can depend on other bindings, producing expression trees, but deep or high-frequency graphs require performance care. Primitive-specialized expressions avoid unnecessary boxing, and conditional or collection-aware factory methods extend the same model to UI decisions and data structures. See [[JavaFX Observable Collections]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
