2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# CDR-Mitigated MaxCut QAOA Evidence

Simulated MaxCut QAOA benchmarks compare noisy optimization with optimization of a Clifford-data-regression-corrected cost. For five-qubit Erdős-Rényi graphs under a gate-set-tomography model of IBM's Ourense device, CDR produces higher mean approximation ratios for every tested QAOA depth and total-shot budget.

At eight qubits, CDR usually retains an advantage, but the gap is smaller. The eight-qubit noise model is deliberately weakened to one fifth of the device-derived strength because deeper compiled circuits would otherwise be untrainable. Performance of both noisy and mitigated optimization falls for the deeper $p=3$ and $p=4$ ansätze.

These simulations support the [[Clifford Data Regression Trainability Window]] outside the NIBP regime: mitigation can repair landscape corruption while the cost still has resolvable structure. They do not demonstrate hardware performance or establish that CDR is optimal for other problems and noise models.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
