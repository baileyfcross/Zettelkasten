2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Unreal Engine VR Editor Interaction Model

The experimental Unreal Engine 4.13 VR Editor mapped scene authoring onto two tracked controllers. A controller laser selected objects; a half trigger exposed a transform gizmo, while a full trigger entered freeform manipulation. A second hand could then scale by changing controller separation or rotate by changing their relative orientation.

World navigation inverted the usual travel metaphor: holding a grip pulled the world past the user. Using both grips allowed the world to be scaled or yawed, letting the author inspect a level at different apparent sizes without changing the authored geometry. Radial and quick-select menus placed common commands on the controllers, and conventional 2D editor panels could be docked to one hand and operated by the other.

The exact controls are version-specific, but the interaction model illustrates [[Bimanual Interaction]] and [[3D Manipulation]] in an authoring tool. One hand can establish a frame, object, or panel while the other performs a precise action, and scale changes let the same physical reach support both world-scale navigation and local editing.

# References

[[unrealenginevrcookbook.pdf]]

