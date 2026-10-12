2026-10-12 01:03

Status: #baby

Tags: [[Unity Prefab and Asset Workflow]]

# Unity Runtime Instantiation

Unity runtime instantiation creates a new object while the game is running, commonly by cloning a [[Unity Prefab]]. The operation can supply a position and rotation so projectiles, enemies, effects, or other repeated entities appear in the correct context.

Instantiation separates the reusable definition from the timing of creation. A script can keep a prefab reference as data and create instances only when gameplay demands them. The spawned object is a distinct runtime instance, so later changes to its state do not directly alter the prefab asset.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

