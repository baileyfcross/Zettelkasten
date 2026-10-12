2026-09-15 18:17

Status: #baby

Tags: [[Rotoscopy and Motion Tracking]]

# Tracker Search Window Tuning

The search region must be large enough to contain the feature's next-frame motion but not so large that a similar feature elsewhere becomes a tempting match. A tiny pattern may lock onto grain rather than a durable image detail, while an oversized pattern includes changing material that weakens recognition. When a track fails, inspect both the selected feature and its search boundary before assuming the entire shot is untrackable. The pattern, search, and anchor roles are separated in [[Tracking Pattern Search and Anchor Regions]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
