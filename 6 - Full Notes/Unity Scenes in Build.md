2026-10-12 01:03

Status: #baby

Tags: [[Unity Deployment and Runtime Persistence]]

# Unity Scenes in Build

Unity's Scenes in Build list defines which scenes are packaged and assigns their build indexes by order. Runtime scene loading by numeric index depends on this configuration, so reordering the list changes what a given index means.

Only scenes intended for the final player should be included, and startup content normally occupies index zero. Keeping the list aligned with [[Unity SceneManager]] calls prevents a project from working in the editor yet failing to load a scene in the built game.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

