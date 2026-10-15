2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Circuit-Depth Damping Extrapolation

Circuit-depth damping extrapolation fits the observed suppression factor of shallow, classically simulable ansatz circuits as an exponential function of ansatz depth. The fitted curve is then used to predict a rescaling factor for deeper circuits that are no longer simulated exactly.

For a one-dimensional nearest-neighbor circuit and an observable supported on $m$ adjacent qubits, only the backward light cone of at most $m+2l$ qubits is needed to simulate $l$ layers. If 36 qubits are classically tractable and $m=2$, calibration can reach 17 layers even when the full system is arbitrarily wide. In the experiment, a fit through at most 15 layers remains useful to about 25 layers.

The method does not require a perturbative Hamiltonian limit, but it depends on local observables, local circuit connectivity, and approximately exponential damping with depth. Nonlocal Hamiltonian terms can make the backward light cone large enough to remove the classical-calibration advantage.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
