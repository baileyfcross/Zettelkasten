2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Global Level Properties

Global level properties are settings that apply to the whole loaded world rather than one actor. Examples include ambient light, directional light, clear color, or other environment configuration.

They are loaded before actors so newly created objects encounter the intended world context. Saving them separately also prevents the same global value from being duplicated across many actor records.

# References

[[gameprogrammingincplusplus.pdf]]
