2026-10-04 22:56

Status: #baby

Tags: [[R Probability Simulation and Curve Fitting]] [[Pseudorandom Number Generation Methods]] [[Cryptographic Randomness and Hashing]]

# Pseudorandom Number Generation

Pseudorandom number generation uses a deterministic algorithm to produce a sequence that behaves like draws from a specified distribution. Recording the generator state or seed makes a simulation repeatable even though the values are used as random outcomes.

Different distribution functions transform the generator into uniform, normal, binomial, and other draws. Reusing a seed can aid debugging, but repeated scientific runs should not accidentally reuse identical streams when independence is intended.

A generator advances through a finite deterministic state space, so it eventually repeats after its [[Random Number Generator Period]]. Statistical quality therefore requires more than a long cycle: successive values should avoid visible structure, and separate workers must receive nonoverlapping streams in [[Parallel Random Number Generation]].

For cryptography, a sequence must also resist efficient prediction. The seed determines the sequence, so reproducibility that is useful in a simulation becomes a weakness when the values protect keys or sessions. Tests such as the [[Next-Bit Test]] and resistance to a [[State Compromise Extension Attack]] evaluate an adversary's ability to exploit observed output or disclosed internal state rather than only the sequence's visible distribution.

# References

[[rstudentcompanion.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]

[[cryptographyandcryptanalysisinjava.epub]]
