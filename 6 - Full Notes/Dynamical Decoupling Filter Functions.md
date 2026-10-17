2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# Dynamical Decoupling Filter Functions

Dynamical decoupling applies refocusing pulses during free evolution to change how a qubit accumulates phase from time-dependent noise. A Hahn echo uses one $\pi$ pulse; Carr-Purcell and CPMG sequences use many approximately equally spaced pulses.

In the frequency domain, each sequence has a filter function that weights the environmental spectrum. Adding pulses suppresses sensitivity to very slow fluctuations and moves the dominant passband to higher frequency. When the environment is dominated by $1/f$ noise, this can extend coherence toward the $2T_1$ relaxation limit.

The improvement is conditional. Pulse imperfections, finite pulse duration, high-frequency noise, and energy relaxation remain, and a passband can amplify sensitivity to a spectral feature instead of suppressing it. Varying pulse number and spacing turns the same control idea into [[Superconducting-Qubit Noise Spectroscopy]], because measured decay then samples different regions of the noise spectrum.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
