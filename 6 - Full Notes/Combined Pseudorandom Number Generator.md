2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Combined Pseudorandom Number Generator

A combined pseudorandom number generator forms one output stream from two or more component generator states. Combining streams with distinct moduli or recurrences can produce a period and statistical behavior superior to those of an individual component.

The components must not simply repeat the same defects in synchrony. Their periods and update rules are selected so the joint state cycles slowly, while the final combination maps component values back into a uniform value on the unit interval.

# References

[[statisticalcomputingincplusplusandr.pdf]]
