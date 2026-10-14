2026-10-12 01:03

Status: #baby

Tags: [[Unity Physics and Gameplay Interaction]]

# Unity Collision Callback

A Unity collision callback lets a MonoBehaviour respond when its collider participates in a physical contact. Entry, continued contact, and exit phases support behaviors that begin, persist, or end with the collision.

The callback carries information about the other participant and the contact. Scripts should use that data to express gameplay consequences rather than replacing the physics solver itself. Tags or components can identify the contacted object, while [[Unity Trigger Collider|triggers]] are preferable when overlap should be detected without a blocking response.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

