2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Usqrt versus Usin QSP Drivers

Two QSP drivers can expose a fixed-point value for polynomial transformation. $U_{\mathrm{sin}}$ uses controlled $R_y$ rotations to encode $\sin(x)$, so its polynomial must approximate a composition with $\arcsin$. $U_{\mathrm{sqrt}}$ uses a comparator to encode $\sqrt{x}$, so its polynomial instead approximates the target function evaluated at $x^2$.

$U_{\mathrm{sin}}$ can use fewer ancillary qubits in the transformation itself, but every invocation requires many accurately synthesized rotations. In the 15-bit, degree-20 benchmark, distributing a $10^{-3}$ payoff-error budget over all controlled rotations makes one $U_{\mathrm{sin}}$ invocation about 74 times deeper in T gates than the comparator-based $U_{\mathrm{sqrt}}$ implementation.

The choice of block encoding therefore changes both polynomial degree and gate-synthesis cost. For the autocallable benchmark, [[Comparator-Based Square-Root Amplitude Encoding]] yields the best balance and underpins the improvements in [[QSP Derivative Pricing Resource Advantage]].

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
