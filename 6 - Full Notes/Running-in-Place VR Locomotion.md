2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Running-in-Place VR Locomotion

Running-in-place VR locomotion maps rhythmic vertical headset motion to forward virtual movement. Each frame, the system subtracts the previous tracked head position from the current position and divides by frame time to estimate velocity. Averaging a short history suppresses high-frequency tracking noise and irregular single-frame movement.

The absolute vertical component is scaled into a candidate running speed. A threshold suppresses ordinary head motion while allowing stronger jogging motion to drive the pawn along the headset's forward vector. The threshold, smoothing window, and multiplier jointly determine how easily movement starts and how stable its speed feels.

The physical action can make the resulting motion easier to anticipate than thumbstick movement, but the user's vestibular system still lacks matching forward acceleration. It therefore reduces neither [[Cybersickness]] nor accessibility risk automatically. The technique also depends on positional head tracking and must distinguish intentional jogging from crouching, nodding, or other task motion.

# References

[[unrealenginevrcookbook.pdf]]

