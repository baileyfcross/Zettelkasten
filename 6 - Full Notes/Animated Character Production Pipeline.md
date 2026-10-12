2026-09-29 23:09

Status: #baby

Tags: [[3D Character Preproduction and Design]]

# Animated Character Production Pipeline

An animated character production pipeline connects design, modeling, UV unwrapping, texture painting, shading, rigging, and animation in a dependency order. Later stages rely on earlier representations: deformation requires suitable topology, painting requires UVs, and animation requires an understandable rig.

If the character will enter live-action footage, the pipeline extends through camera tracking, matched lighting, rendering, and compositing. Treating these as one chain encourages decisions such as simplifying hair or preserving joint loops before their downstream cost becomes visible.

# References

[[learningblender3e.pdf]]
