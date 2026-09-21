2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Animation Clip

An animation clip stores a named sequence of skeletal poses over a duration and sampling rate. Playback converts elapsed time into neighboring frame indices and a fractional interpolation amount.

Looping wraps time back into the clip's duration, while one-shot playback clamps or transitions when the end is reached. The clip supplies local bone transforms rather than final skinned vertex positions.

# References

[[gameprogrammingincplusplus.pdf]]
