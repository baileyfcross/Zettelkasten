2026-10-02 18:09

Status: #baby

Tags: [[Blender Animation Editors and Timing]]

# Blender Keyframe Types

Blender keyframe types attach semantic labels and distinct display shapes or colors to keys without changing the underlying ability to store a value. Standard keys mark ordinary poses, Breakdown keys identify transitions, Moving Hold keys preserve slight motion around a hold, Extreme keys identify important limits, and Jitter keys mark filler or densely baked motion.

These types make a Dope Sheet easier to read because timing intent remains visible among many channels. They are organizational annotations rather than interpolation modes: a Breakdown key can still use different curve interpolation, and an Extreme does not automatically change motion. Consistent use helps animators distinguish structural poses from generated or transitional detail.

# References

[[modelingandanimationusingblender.pdf]]
