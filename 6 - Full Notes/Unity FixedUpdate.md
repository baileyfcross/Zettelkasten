2026-10-12 01:03

Status: #baby

Tags: [[Unity Physics and Gameplay Interaction]]

# Unity FixedUpdate

Unity FixedUpdate is a lifecycle callback scheduled on a fixed time step associated with physics simulation rather than once per rendered frame. It is the appropriate phase for applying forces or performing other repeated operations that directly drive [[Unity Rigidbody|Rigidbody]] behavior.

Rendering frequency can vary with hardware and workload, while the physics step aims for stable simulation intervals. Keeping physics work in the fixed-step loop reduces frame-rate-dependent results. Visual or ordinary input response can still occur in Update and pass decisions to the next physics step.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

