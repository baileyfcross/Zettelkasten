2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Software Architecture]]

# User Interface Abstraction

User interface abstraction represents an intended interaction independently of one input or output device. A logical selection or manipulation can be bound to tracked props, touch, gesture, or another modality appropriate to the active AR platform.

Separating meaning from device events supports reuse and multimodal alternatives. The binding still needs access to physical context, because an interaction mapped without regard to tracking, feedback, and environment may no longer preserve its intended behavior.

# References

[[augmentedreality_pearson.pdf]]
