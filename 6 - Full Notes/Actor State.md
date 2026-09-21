2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Actor State

Actor state records whether a [[Game Actor]] is active, paused, or awaiting removal. Active actors process input and update normally, paused actors remain registered without advancing, and dead actors are removed at a safe point.

Representing lifecycle state explicitly avoids deleting an actor while its update function or the world's actor loop is still using it. State therefore governs both behavior and ownership transitions.

# References

[[gameprogrammingincplusplus.pdf]]
