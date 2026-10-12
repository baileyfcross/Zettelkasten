2026-10-12 01:03

Status: #baby

Tags: [[Unity Animation Audio and Effects]]

# Unity Animator State Machine

A Unity Animator state machine models animation as named states connected by conditional transitions. Each state usually plays a motion clip or blend tree, while parameters and exit-time rules govern when control moves elsewhere.

The graph makes animation flow visible and separates it from gameplay code. Transitions can blend between motions rather than switching abruptly, and a default state establishes initial behavior. The state machine lives inside an [[Unity Animator Controller]] evaluated by an [[Unity Animator Component]].

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

