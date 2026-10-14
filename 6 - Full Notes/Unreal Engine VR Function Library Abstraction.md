2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Unreal Engine VR Function Library Abstraction

Unreal Engine exposes a generic head-mounted-display function library for capabilities shared by multiple runtimes and narrower vendor libraries for device-specific behavior. Generic operations include reading headset pose, testing whether an HMD is active, changing [[Unreal Engine VR Tracking Origins|tracking origin]], resetting orientation, and changing world-to-meters scale.

Vendor layers expose features that cannot be expressed uniformly, such as a runtime's loading splash screens, raw sensors, tracked-device identifiers, or user profile. Code can therefore use the generic layer for normal play and enter a vendor path only when the experience actually depends on a platform feature.

This boundary limits device assumptions and helps one pawn work with several headsets. It does not guarantee identical capability: a generic-looking operation may be unsupported, deprecated, or interpreted differently by a runtime. The book's function tables describe Unreal Engine 4.11-4.13 and should be used as an architectural example rather than a current API reference.

# References

[[unrealenginevrcookbook.pdf]]

