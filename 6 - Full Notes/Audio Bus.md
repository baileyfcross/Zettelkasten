2026-09-20 23:34

Status: #baby

Tags: [[Game Audio Programming]]

# Audio Bus

An audio bus groups sound events into a mix category such as music, dialogue, effects, or ambience. Changing a bus affects every routed event, allowing independent volume control, muting, or processing without visiting each instance.

Buses can form a hierarchy so a master bus governs the full mix while child buses retain category control. An [[Audio Snapshot]] can change several bus settings together for a temporary game state.

# References

[[gameprogrammingincplusplus.pdf]]
