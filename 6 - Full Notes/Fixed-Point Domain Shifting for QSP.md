2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Fixed-Point Domain Shifting for QSP

Comparator-based amplitude encoding interprets an $n$-bit fixed-point register as an unsigned binary fraction. If the stored value has $p$ bits to the left of the binary point, the encoded good-state probability becomes $x/2^p$, so the target polynomial must absorb the same scale factor.

Signed inputs are handled by choosing a shift $s\geq|x|$, reversibly computing $x+s$ in a new register, and encoding $(x+s)/2^p$. The payoff polynomial compensates for the shift and normalization; for exponential functions this introduces the corresponding factor $e^{-s}$.

The construction guarantees that the amplitude presented to QSP lies in $[0,1]$. The target function can then be extended to $[-1,1]$ with even or odd symmetry to meet QSP's parity requirement, even when the original payoff formula has no definite parity.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
