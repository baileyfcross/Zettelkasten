2026-10-02 18:09

Status: #baby

Tags: [[Blender Scene Object Types]]

# Blender Force Field Object

A Blender force field object introduces an influence that can alter particles, cloth, soft bodies, and rigid-body simulations. Its type determines whether the effect attracts, repels, swirls, drags, guides, or otherwise changes simulated motion, while its object transform establishes the field's position and orientation.

The object provides a shared scene-level cause that several simulations can respond to. Strength, shape, falloff, noise, and distance bounds control how that cause is distributed. Because fields may affect many eligible systems automatically, their scope and weights should be checked when an apparently unrelated simulation begins moving differently.

# References

[[modelingandanimationusingblender.pdf]]
