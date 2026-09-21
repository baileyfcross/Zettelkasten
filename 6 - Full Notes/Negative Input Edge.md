2026-09-20 23:34

Status: #baby

Tags: [[Game Input Systems]]

# Negative Input Edge

A negative input edge occurs when a digital control was pressed in the previous frame and is released in the current frame. It identifies the end of one held interval.

Release-sensitive actions can charge while held and resolve on this edge, or stop a mode exactly when control ends. Like the [[Positive Input Edge]], it depends on retaining both current and previous states.

# References

[[gameprogrammingincplusplus.pdf]]
