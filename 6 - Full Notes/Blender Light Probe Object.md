2026-10-02 18:09

Status: #baby

Tags: [[Blender Scene Object Types]]

# Blender Light Probe Object

A Blender light probe is a non-rendered support object that records local lighting information for Eevee. It helps the real-time renderer approximate indirect illumination or reflections that rasterization does not calculate through the same full light-transport process as a path tracer.

Probe placement is therefore part of scene lighting rather than visible geometry. The probe samples a region and supplies reusable environmental information to nearby surfaces. Its value depends on the kind of lighting effect needed and on whether its captured area represents the scene accurately; a probe is an approximation aid, not an emitting [[Blender Light Types|light object]].

# References

[[modelingandanimationusingblender.pdf]]
