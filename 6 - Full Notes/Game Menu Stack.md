2026-09-18 17:13

Status: #baby

Tags: [[Game User Interface Programming]]

# Game Menu Stack

A game menu stack stores interface screens in navigation order. Pushing a screen places it above the current one, while popping it reveals the previous screen without requiring every overlay to know its caller.

Pause dialogs and nested option screens fit this structure naturally. The system must define whether covered screens continue updating or drawing and how input is restricted to the topmost active layer.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
