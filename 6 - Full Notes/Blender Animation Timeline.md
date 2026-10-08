2026-10-02 18:09

Status: #baby

Tags: [[Blender Animation Editors and Timing]]

# Blender Animation Timeline

The Blender Timeline gives a broad view of scene time: the current frame, the animation start and end, keyframes for the active object, and named markers. Transport controls move the playhead, jump between keys or range boundaries, and play forward or backward, while a preview range limits interactive review without changing final render bounds.

Playback settings determine how Blender behaves when the scene cannot update at the requested frame rate. No Sync preserves every frame, Frame Dropping favors elapsed time, and audio/video synchronization follows the audio clock while dropping frames when necessary. Editor-update switches control which parts of the interface refresh during playback.

In Blender 2.77, the Timeline transport controls start, stop, jump to the beginning or end, and move the current-frame cursor. The book relates a 250-frame range at 24 frames per second to roughly ten seconds, making frame range and frame rate separate parts of an animation's duration.

# References

[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
