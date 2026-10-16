2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Comparator-Based Square-Root Amplitude Encoding

The $U_{\mathrm{sqrt}}$ driver encodes an $n$-bit number $x\in[0,1)$ as an amplitude using a uniform reference register and a reversible comparator. Starting from $|x\rangle|+\rangle^{\otimes n}$, the comparator flags which reference integers lie outside the first $2^n x$ values.

Exactly a fraction $x$ of the reference basis states place the flag in the good state. The resulting amplitude is therefore $\sqrt{x}$, with its complementary amplitude equal to $\sqrt{1-x}$, and no arithmetic circuit has to calculate a square root.

This driver uses ancillary qubits for the reference register but relies mainly on comparison logic instead of synthesized rotations. [[Usqrt versus Usin QSP Drivers]] shows why that tradeoff dramatically reduces T-depth in the derivative benchmark, while [[Fixed-Point Domain Shifting for QSP]] extends the encoding beyond nonnegative fractional inputs.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
