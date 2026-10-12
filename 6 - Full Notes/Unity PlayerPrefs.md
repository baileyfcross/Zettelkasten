2026-10-12 01:03

Status: #baby

Tags: [[Unity Deployment and Runtime Persistence]]

# Unity PlayerPrefs

Unity PlayerPrefs stores simple integer, floating-point, and string values in a local platform-specific file. Named keys let a later scene or session retrieve preferences or small pieces of state without keeping a GameObject alive.

The API is convenient for settings such as volume or display choices. It is not a general structured save system, and [[Unity PlayerPrefs Data Security]] limits what should be trusted to it. Key naming, defaults, and deliberate save timing make even small preference data easier to maintain.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

