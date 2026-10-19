2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Reactive UI Composition]]

# JavaFX Property Binding

A unidirectional JavaFX binding makes one property depend on an observable value. `bind()` establishes the relationship, `unbind()` releases it, and `isBound()` reports it. While bound, the target reflects the source and cannot be assigned independently. A property can have at most one active unidirectional binding; binding it to a new source replaces the previous one.

A bidirectional binding synchronizes two properties so changing either updates both, and multiple bidirectional relationships may exist. Bindings let UI rules be expressed as state relationships rather than repeated event-handler assignments—for example, disabling an update button when no item is selected, a form is unmodified, or required text is empty. More complex computed relationships are built through [[JavaFX Binding Expressions]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
