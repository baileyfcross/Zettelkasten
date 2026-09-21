2026-09-18 17:13

Status: #baby

Tags: [[Game User Interface Programming]]

# Game UI Button State

A game UI button state records whether a button is normal, highlighted, pressed, or disabled. Input and focus transitions change the state, and each state can select different visual and audio feedback.

The button's activation event should remain separate from its appearance. This lets keyboard, gamepad, pointer, or touch navigation drive the same command while preserving appropriate feedback for the current interaction.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
