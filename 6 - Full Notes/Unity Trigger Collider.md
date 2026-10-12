2026-10-12 01:03

Status: #baby

Tags: [[Unity Physics and Gameplay Interaction]]

# Unity Trigger Collider

A Unity trigger collider detects overlap without acting as a solid physical barrier. Enabling the trigger property changes the collider from a contact surface into a sensing volume that reports objects entering, remaining, or leaving.

Triggers are useful for finish zones, hazards, pickups, doors, and cleanup regions because they separate detection from visible geometry. A script attached to the trigger or interacting object interprets the event, often using [[Unity Tag and Layer|classification]] to decide which overlaps matter.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

