2026-09-18 17:13

Status: #baby

Tags: [[Game User Interface Programming]]

# Game Menu State Machine

A game menu state machine represents each menu screen as a state and navigation actions as transitions. Only the active state receives input and determines which interface elements are updated and drawn.

This model makes legal transitions explicit and works well when navigation has a controlled structure. A [[Game Menu Stack]] is useful when screens frequently overlay one another and need automatic return to the previous screen.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
