2026-10-12 01:03

Status: #baby

Tags: [[Unity Deployment and Runtime Persistence]]

# Unity PlayerPrefs Data Security

Unity PlayerPrefs data is stored locally without encryption and can be inspected or modified by a player. It should therefore be treated as convenient client-side preference storage rather than a secure or authoritative record.

Saving a display option or volume setting is appropriate; placing secrets, purchases, competitive scores, or trusted progression solely in PlayerPrefs is not. [[Unity PlayerPrefs]] reduces serialization effort, but security and integrity requirements call for a stronger design.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

