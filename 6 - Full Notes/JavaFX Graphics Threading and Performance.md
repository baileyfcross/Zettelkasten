2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Graphics and 3D]]

# JavaFX Graphics Threading and Performance

Hardware acceleration does not prevent an application from stalling if calculation and drawing monopolize the JavaFX Application Thread. Particle simulations and fractal generation expose this limit as their workloads grow. Heavy processing should occur on a separate producer thread, leaving the UI thread available for input and presentation.

The computed result must still be applied to the canvas or controls on the FX thread. `Platform.runLater` schedules such a UI update; directly invoking the graphics context from a worker can fail with a not-on-FX-thread exception. Performance therefore depends on both representation and scheduling: use one canvas instead of an enormous node population when immediate rendering fits, minimize the work transferred per frame, and respect the ownership rule described in [[JavaFX Application Thread]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
