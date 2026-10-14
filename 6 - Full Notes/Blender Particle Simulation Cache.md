2026-10-02 18:09

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Particle Simulation Cache

The Blender particle simulation cache stores calculated frames so playback and rendering can reuse a stable result instead of recomputing particle motion every time. Cache start, end, and step settings define the recorded interval and sampling, while baking protects a completed result from ordinary parameter changes.

Caching is order-sensitive. Playback must pass through the simulation range to populate an unbaked cache, relevant changes may require manually freeing stale data, and disk caching requires a writable location. Geometry or modifier differences between viewport and render can also produce divergent results. A cache is therefore a reproducibility artifact tied to a particular simulation configuration, not generic acceleration.

The source applies the same principle to smoke and fire: playing the sequence creates cache data, and changing the cache start frame delays when emission begins in the final project. A cached result therefore contains temporal decisions as well as calculated motion and must be invalidated when those decisions change.

# References

[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
