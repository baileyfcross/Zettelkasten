2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Direct Amplitude Transformation for Payoff Functions

When an algorithm ultimately needs a function value only as a measurement amplitude, computing that value digit by digit can be unnecessary. A direct amplitude transformation starts from an easily encoded scalar amplitude and uses QSP to approximate the entire function composition needed by the final observable.

For the derivative payoffs in the paper, one polynomial simultaneously represents exponentiation of a log-return, subtraction of a strike-dependent term, normalization, and the square root required by [[Quantum Payoff Amplitude Encoding]]. The circuit never materializes separate asset-price and payoff registers.

This principle explains the resource improvement more directly than “faster arithmetic”: the digital intermediate representation is removed. It remains applicable only when the composed target can be approximated by an allowed bounded polynomial at acceptable degree, as constrained by [[Single-Variable QSP Limitation]].

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
