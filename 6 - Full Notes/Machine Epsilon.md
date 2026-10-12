2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# Machine Epsilon

Machine epsilon is a small positive floating-point number that characterizes the spacing near one: adding a smaller increment may produce no representable change.

It provides a scale for expected [[Round-Off Error]] and for numerical tolerance choices. A test should usually compare errors relative to problem magnitude rather than treating machine epsilon as a universal stopping threshold.

The spacing implied by machine epsilon explains why adding a sufficiently small value to a much larger floating-point number can leave the stored value unchanged. Increasing precision reduces that local spacing but does not remove unstable formulations or [[Catastrophic Cancellation]].

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
