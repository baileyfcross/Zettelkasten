2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Mixed Coherent and Relaxation Noise Mitigation

Randomized compiling directly tailors coherent error but does not remove incoherent relaxation. In a mixed model containing coherent crosstalk and generalized qubit relaxation, the benefit of RC alone therefore decreases as relaxation accounts for more of the fixed total entangling-gate error.

Zero-noise extrapolation behaves in the complementary direction: its results improve as the noise becomes more strongly incoherent and hence more regular under scaling. Combining RC and ZNE retains a mitigation benefit even when coherent crosstalk contributes only 10 percent of the overall error rate in the paper's simulation.

The experiment shows that RC-ZNE need not require purely coherent noise, but it does not establish robustness to arbitrary device noise. Measurement error is omitted, the relaxation channel uses selected parameters, and the protocol's advantage depends on the remaining coherent component and the chosen scaling procedure.

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
