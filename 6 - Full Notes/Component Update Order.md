2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Component Update Order

Component update order determines the sequence in which a [[Game Actor]] invokes its attached behaviors. An order value can keep input, movement, animation, collision, and presentation dependencies stable without hard-coding every component type.

The actor inserts components according to this priority and iterates them consistently each frame. When one component consumes state produced by another, their ordering becomes part of the actor's runtime contract.

# References

[[gameprogrammingincplusplus.pdf]]
