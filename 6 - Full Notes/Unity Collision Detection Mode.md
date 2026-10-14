2026-10-12 01:03

Status: #baby

Tags: [[Unity Physics and Gameplay Interaction]]

# Unity Collision Detection Mode

Unity collision detection mode controls how a Rigidbody checks motion for contacts. Discrete detection is the normal, less expensive choice, while continuous modes perform additional work to reduce the chance that a fast-moving body crosses a thin collider between simulation steps.

Continuous detection should be applied selectively because reliability has a computational cost. A projectile or unusually fast ball may justify it; ordinary slow objects often do not. Correct scale, collider thickness, and [[Unity FixedUpdate|fixed-step]] behavior remain important even when a continuous mode is enabled.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

