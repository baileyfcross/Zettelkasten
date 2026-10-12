2026-10-12 01:03

Status: #baby

Tags: [[Unity Deployment and Runtime Persistence]]

# Unity SceneManager

Unity SceneManager provides runtime operations for moving between [[Unity Scene|scenes]]. `LoadScene` can select a scene by its build index or name, unloading the current context and loading the requested one immediately.

Scripts using SceneManager import the scene-management namespace. Because an immediate load destroys ordinary objects from the departing scene, state that must survive needs an explicit persistence strategy such as [[Unity DontDestroyOnLoad]] or external saved data.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

