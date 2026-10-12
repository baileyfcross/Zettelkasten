2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Game Component

A game component is a reusable behavior object owned by a [[Game Actor]]. It can update, process input, draw, play audio, or expose collision data while relying on the actor for shared transform and lifetime.

Components reduce duplication across unrelated actor types. They also need an explicit interface and update order so several components can modify or consume actor state predictably during the same frame.

# References

[[gameprogrammingincplusplus.pdf]]
