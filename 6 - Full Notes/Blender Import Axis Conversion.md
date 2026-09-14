2026-09-14 01:18

Status: #baby

Tags: [[Portable 3D Model Data]]

# Blender Import Axis Conversion

Graphics applications may disagree about which axis points up or forward and about the unit scale represented by one coordinate. Import and export conversion maps those conventions so an asset arrives with the intended orientation and size.

Changing axes is not merely cosmetic when animation, cameras, armatures, or parent-child transforms are present. A pipeline should test a reference object with known dimensions and direction before transferring a complete environment.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

