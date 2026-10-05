2026-09-15 23:23

Status: #baby

Tags: [[Annotated Time-Series Displays]] · [[R Base Graphics Composition]]

# Time Plot

A time plot places a [[Time Index]] on the horizontal axis and observation values on the vertical axis, usually joining successive observations with a line. It makes direction, cycles, abrupt changes, and gaps visible in their temporal order. Multiple variables may require separate panels with [[Independent Panel Scales]], while annotations such as an [[Average-Comparison Time Plot]] can give the line a meaningful reference.

The student companion constructs the display in base R by pairing an ordered time variable with measurements and selecting a line-oriented plot type. Joining observations is justified by their temporal sequence, and the axis label should identify the actual time unit rather than rely on row number.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]

[[rstudentcompanion.pdf]]
