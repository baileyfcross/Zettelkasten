2026-10-01 00:39

Status: #baby

Tags: [[2D Game Rendering]]

# Bresenham Line Rasterization

Bresenham's line algorithm selects the next raster pixel by testing an incremental decision parameter proportional to the difference between the candidate pixels' distances from the ideal line. For a positive slope below one, every step advances x and either retains y or increments it according to the sign of the parameter.

The next decision value is obtained by adding a constant derived from dx and dy, with a second correction when the diagonal pixel is chosen. Because the recurrence uses integer addition and comparison, it avoids the floating-point accumulation and rounding used by [[Digital Differential Analyzer Line Rasterization]]. Sign choices extend the same idea to other octants.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
