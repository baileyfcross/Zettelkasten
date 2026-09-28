2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# No-Allocate Store Policy

A no-allocate store policy avoids loading a cache line on a write miss when the program will overwrite the relevant region. Under ordinary write allocation, fetching the old line consumes bandwidth even though its contents are not needed.

The policy is valuable for an out-of-place stencil's destination array. It is a narrow optimization, but the book's measurements show that eliminating unnecessary transfers can improve both runtime and energy without the area cost of a larger cache.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

