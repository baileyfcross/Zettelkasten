2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Component Type Dispatch

Component type dispatch maps a serialized component name to a construction function that attaches the correct [[Game Component]] subclass to an actor. It allows a level file to compose behavior without hard-coding each combination as a distinct actor class.

After construction, a property-loading hook applies component-specific values. The registry must prevent duplicate or incompatible components when the actor model imposes such constraints.

# References

[[gameprogrammingincplusplus.pdf]]
