2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Mersenne Twister

The Mersenne Twister is a word-oriented pseudorandom generator whose state recurrence and output transformation are designed to provide a very long [[Random Number Generator Period]] and strong equidistribution over many dimensions.

Its standard form has period $2^{19937}-1$. The large internal state makes it unsuitable as a cryptographic generator and requires deliberate stream management in parallel programs, even though it is a widely used default for serial statistical simulation.

# References

[[statisticalcomputingincplusplusandr.pdf]]
