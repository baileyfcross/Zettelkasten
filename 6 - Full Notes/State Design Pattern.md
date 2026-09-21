2026-09-18 17:13

Status: #baby

Tags: [[Game Artificial Intelligence]]

# State Design Pattern

The State design pattern represents each behavior state as an object with its own entry, update, exit, and transition logic. The owning agent delegates state-specific behavior to the active object instead of maintaining one large conditional function.

This structure makes a [[Game Behavior State Machine]] easier to extend and test. Changing states replaces the active state object while preserving the agent's shared data and identity.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
