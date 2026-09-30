2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Surface Development]]

# Cross-Engine Character Shader Validation

Cross-engine character shader validation compares a material in [[Eevee and Cycles Render Engines|Eevee and Cycles]] before the asset is considered finished. Shared nodes can produce broadly similar results, but screen-space refraction, shadows, caustics, sampling, and other engine-specific effects may require different settings or deliberate workarounds.

Eyes are a useful stress test because a refractive cornea can reveal missing off-screen information in Eevee or overly dark transmission shadows in Cycles. Validation should use representative lighting and camera angles so a successful material-preview thumbnail is not mistaken for production compatibility.

# References

[[learningblender3e.pdf]]
