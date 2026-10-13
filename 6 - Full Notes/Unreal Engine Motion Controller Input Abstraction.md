2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Unreal Engine Motion Controller Input Abstraction

Unreal Engine's Motion Controller Component represents a tracked hand independently of a particular controller model. A pawn selects left or right hand, receives the runtime's pose, and attaches meshes or interaction components beneath that transform. This lets the same high-level interaction operate across controllers whose tracking systems and physical layouts differ.

Cross-device actions should be mapped to capabilities genuinely shared by the target hardware. The book identifies an analog trigger across the Vive, Oculus Touch, and PlayStation Move, and a grip-like input shared by the Vive and Touch. Trigger can express use or drag, while grip can express pickup, but device-specific buttons require an explicit alternate mapping.

The abstraction removes many vendor checks from gameplay code; it does not make every controller equivalent. Available degrees of freedom, buttons, hand poses, haptics, and tracking bounds still affect the experience. A reusable pawn should keep semantic actions such as use, grab, and release separate from the raw device event that invokes them.

# References

[[unrealenginevrcookbook.pdf]]

