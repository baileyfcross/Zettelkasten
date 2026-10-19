2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Reactive UI Composition]]

# JavaFX Subscription Listeners

The JavaFX subscription API wraps listener registration in a lifecycle object. An observable can accept a `Runnable` for invalidation-style notification, a `Consumer` for an eagerly initialized current value, or a `BiConsumer` for old-and-new value changes without eager initialization. The registration returns a `Subscription` rather than requiring the caller to retain the original listener instance.

Calling `unsubscribe()` cancels the observation. This makes temporary controllers, views, and derived behaviors easier to detach than paired `addListener` and `removeListener` calls. The underlying distinction between invalidation and change remains the one described in [[JavaFX Invalidation and Change Listeners]], but cleanup becomes an explicit part of the object returned by the registration operation.

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
