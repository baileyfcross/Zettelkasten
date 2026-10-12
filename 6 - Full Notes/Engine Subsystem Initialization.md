2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Engine Subsystem Initialization

Engine subsystem initialization creates platform, graphics, audio, input, and data services in dependency order before gameplay begins. Each step reports success so the [[Game Class Lifecycle]] can stop cleanly when a required capability is unavailable.

Shutdown generally reverses the order: game objects release their resources before the renderer, audio system, window, and platform libraries disappear. This prevents destructors from calling services that have already been destroyed.

# References

[[gameprogrammingincplusplus.pdf]]
