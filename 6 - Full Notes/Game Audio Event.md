2026-09-20 23:34

Status: #baby

Tags: [[Game Audio Programming]]

# Game Audio Event

A game audio event is an authored playback definition referenced by a stable name. It can select sounds and control looping, variation, parameters, routing, and effects beyond a single raw file.

Playing the event creates an instance represented by a [[Sound Event Handle]]. The distinction lets many simultaneous instances share one event definition while keeping their position, parameters, playback state, and lifetime independent.

# References

[[gameprogrammingincplusplus.pdf]]
