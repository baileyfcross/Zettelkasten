2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Snap Turning for VR

Snap turning replaces continuous artificial yaw with discrete angular steps. Because the visual world does not sweep smoothly around a physically stationary user, the technique removes much of the rotational acceleration that can contribute to [[Cybersickness]]. The jump may feel less natural, but it provides a comfort option for users who cannot tolerate smooth turning.

The Unreal implementation accumulates analog turn input in a yaw-offset variable. When its magnitude crosses a configurable threshold, the camera root rotates by the accumulated amount and the offset resets. Stopping the stick or mouse also clears the residual offset so a later movement does not trigger a stale partial turn. Digital shoulder inputs can invoke fixed positive or negative steps directly.

The tracked Camera Component itself should not be treated like an ordinary game camera, because the HMD runtime owns its local head pose. Rotating the camera's parent preserves physical head motion inside the newly chosen virtual heading. Turn amount and activation policy should remain configurable because comfort and orientation tradeoffs vary among users.

# References

[[unrealenginevrcookbook.pdf]]

