2026-09-20 23:34

Status: #baby

Tags: [[Game Audio Programming]]

# Audio Bank

An audio bank is a packaged collection of authored sound events, samples, and metadata loaded by an audio middleware system. Banks let the game request logical events without constructing every DSP setting or asset path in code.

The audio system loads required banks during startup or content transitions and unloads them when no longer needed. Event names and bank versions become a contract between the audio-authoring project and the engine.

# References

[[gameprogrammingincplusplus.pdf]]
