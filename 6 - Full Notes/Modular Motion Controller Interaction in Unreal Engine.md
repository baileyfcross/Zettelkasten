2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Modular Motion Controller Interaction in Unreal Engine

A modular motion-controller interactor uses a scene component to detect nearby candidates and a Blueprint interface to express hover, unhover, use, pickup, drop, drag-start, drag, and drag-end. The component keeps references to the hovered and held actors, while each actor decides how those messages affect its own state.

A small sphere overlap around the tracked hand offers forgiving near-field acquisition. Highlighting or haptic feedback can reveal which candidate will be selected; a directed sphere cast can combine controller pointing with the headset-to-hand direction when proximity alone is ambiguous. The best heuristic depends on object density and the expected hand action.

The interface separates user intent from object mechanics. The pawn maps semantic actions from [[Unreal Engine Motion Controller Input Abstraction|controller input]], the interactor manages state transitions, and targets implement their own physics or constrained motion. This supports pickups, [[Procedural VR Push Button|buttons]], and [[Procedural VR Lever|levers]] without adding class-specific behavior to the controller and helps preserve each object's [[Affordance]].

# References

[[unrealenginevrcookbook.pdf]]

