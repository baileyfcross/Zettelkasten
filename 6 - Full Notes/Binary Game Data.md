2026-09-18 17:13

Status: #baby

Tags: [[Game Scripting and Data Formats]]

# Binary Game Data

Binary game data stores values in a compact machine-oriented representation. It is generally smaller and faster to load than [[Text-Based Game Data]] because the runtime performs less parsing and numeric conversion.

The format is difficult to inspect or merge directly and must manage version, byte order, and structural compatibility. A common pipeline authors readable source data and converts it into a validated binary form for distribution.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
