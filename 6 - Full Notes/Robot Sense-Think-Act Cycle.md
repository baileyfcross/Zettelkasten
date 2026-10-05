2026-10-04 21:57

Status: #baby

Tags: [[Robot Architecture and Autonomy]]

# Robot Sense-Think-Act Cycle

The sense-think-act cycle describes a robot as a physical system with sensors, computation, and actuators. Sensors measure the robot and its environment, computation turns measurements and goals into commands, and actuators change the physical world.

Each stage constrains the others. High-quality sensing is useless if processing is too slow, while a correct plan cannot compensate for an actuator that lacks force or precision. Feedback closes the cycle because action changes what the robot senses next. [[Behavior-Based Robotics]] shortens this loop, while [[Hierarchical Robot Control]] divides it across strategic and motor-level decisions.

# References

[[robots.epub]]

