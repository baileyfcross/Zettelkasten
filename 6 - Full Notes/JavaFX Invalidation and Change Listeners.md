2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Reactive UI Composition]]

# JavaFX Invalidation and Change Listeners

JavaFX distinguishes invalidation from value change. An `InvalidationListener` is notified when an observable becomes invalid, allowing a lazily computed value to postpone recomputation until it is requested. Repeated setters do not necessarily fire repeated invalidations while the value remains unobserved and invalid. A `ChangeListener` receives the old and new values after the observable value has been recomputed, which makes observation eager.

The distinction lets [[JavaFX Properties]] and bindings avoid work when nobody needs a current result. Weak listener variants can reduce the risk that a long-lived observable retains an otherwise unreachable listener, although lifecycle management is still important. For newer callback-oriented registration, [[JavaFX Subscription Listeners]] provides an explicit object that can be canceled.

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
