2026-09-28 20:13

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Animation Workflow]] [[Blender Animation Editors and Timing]]

# Blender Auto-Keyframing

Auto-keyframing inserts keys when an editable animated property changes, reducing the need to create every key manually. The Blender 2.7x workflow required both the relevant preference and the Timeline's Auto-Key control to be active.

Color feedback on keyed fields helps confirm that a change was recorded. Automation also increases the risk of accidental keys, so the feature should be enabled deliberately and the resulting timeline inspected after broad edits.

The modern Timeline control records changes to properties that already have animation channels, helping limit completely unrelated keys. It remains important to watch the current frame and recording state while posing a rig, because an intended temporary adjustment can otherwise become part of the action.

Blender 2.80 further distinguishes Add and Replace from Replace-only behavior and can combine auto-keying with the active keying set. Layered Recording creates a new nonlinear-animation track and strip for each pass, while cycle-aware keying preserves simple loop continuity. These options change the scope of automatic recording and should be selected before an editing pass begins.

# References

[[howtocheatinblender27x.pdf]]
[[learningblender3e.pdf]]
[[modelingandanimationusingblender.pdf]]
