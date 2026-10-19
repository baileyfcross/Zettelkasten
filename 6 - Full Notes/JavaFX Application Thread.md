2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Application Architecture]]

# JavaFX Application Thread

JavaFX has a single-threaded UI model. A live stage, scene, and scene graph must be constructed or modified on the JavaFX Application Thread. Event handlers and animation callbacks therefore share the thread responsible for presenting and updating the interface.

Long-running calculation, I/O, or model training should run on background threads so the UI remains responsive. A background task must not update controls or a canvas directly; doing so can raise an `IllegalStateException` because the caller is not on the FX thread. Results that affect the interface can be scheduled with `Platform.runLater`, or coordinated through JavaFX concurrency facilities. This boundary is essential in [[JavaFX Graphics Threading and Performance]] and becomes more complex when combined with Swing's separate event-dispatch thread in [[JavaFX and Swing Integration Threads]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
