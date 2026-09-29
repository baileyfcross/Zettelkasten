2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Lifecycle Methods

Unity lifecycle methods are specially named callbacks that the engine invokes at defined phases. `Start()` runs once when an enabled object begins participating, while `Update()` runs once per rendered frame; physics work commonly uses the fixed-step phase instead.

The distinction prevents initialization from being repeated and separates frame-dependent behavior from physics timing. Disabling a script stops its active callbacks without removing its data. Because many objects receive these methods independently, code should not assume an arbitrary ordering between peer scripts unless the dependency is made explicit.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

