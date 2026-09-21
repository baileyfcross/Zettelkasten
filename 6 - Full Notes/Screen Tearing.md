2026-09-18 17:13

Status: #baby

Tags: [[2D Game Rendering]]

# Screen Tearing

Screen tearing occurs when the displayed image contains portions of different rendered frames. It happens when the front and back buffers are exchanged while the display is partway through scanning a frame.

Synchronizing the swap with the [[Vertical Blank Interval]] prevents the buffer change from becoming visible in the middle of the image. [[Double Buffering]] supplies the complete alternate frame that is presented at that safe point.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
