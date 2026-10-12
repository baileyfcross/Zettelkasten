2026-10-12 01:03

Status: #baby

Tags: [[Unity Deployment and Runtime Persistence]]

# Unity DontDestroyOnLoad

Unity `DontDestroyOnLoad` marks a runtime object to survive when [[Unity SceneManager]] replaces the current scene. It is useful for managers, audio, or player state stored on an object that must remain available across several scene contexts.

Persistence also creates responsibility: loading a new copy in every scene can produce duplicates. A persistent object should have clear lifetime and ownership, and scene-specific references may need to be re-established after a transition.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

