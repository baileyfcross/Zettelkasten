2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Middle-Square Method

The middle-square method squares a fixed-width integer state and takes the middle digits of the result as the next state. It is historically important as an early attempt to generate random-looking numbers directly by computer.

The method readily falls into short cycles or the absorbing zero state, and its output does not meet modern statistical standards. It illustrates why apparent irregularity is not enough: generator structure, period, and dependence must be examined.

# References

[[statisticalcomputingincplusplusandr.pdf]]
