2026-10-12 01:03

Status: #baby

Tags: [[Unity Prefab and Asset Workflow]]

# Unity Import Settings

Unity import settings describe how a source file should become an engine-ready asset. Selecting a model, texture, audio file, or sprite in the [[Unity Project View]] exposes type-specific options in the [[Unity Inspector]].

These settings are part of the asset pipeline rather than scene-instance data. Changing them can update every use of the imported resource. Decisions such as model scale, texture interpretation, sprite slicing, audio loading, or animation rig type should therefore be made with all downstream references in mind.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

