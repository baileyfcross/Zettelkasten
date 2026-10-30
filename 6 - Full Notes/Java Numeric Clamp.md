2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java Numeric Clamp

Java's numeric clamp operation confines a value to an inclusive lower and upper bound. It returns the lower bound when the input is smaller, the upper bound when it is larger, and the original value when it already lies in range.

The named `Math` and `StrictMath` operation replaces nested minimum and maximum expressions whose order is easy to misread. It is useful for bounded coordinates, intensities, scores, and other values where saturation is intended instead of rejection.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
