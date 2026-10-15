2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Qubit Assignment Averaging

Qubit assignment averaging executes a logical circuit under several connectivity-preserving mappings to physical qubits and averages the results. This reduces sensitivity to one device region's systematic bias while preserving the circuit topology and avoiding routing overhead.

For a logical ring of $n$ qubits mapped to a physical ring, cyclic shifts and reflection produce $2n$ connectivity-preserving assignments. The experiment evaluates four assignments selected for the largest predicted damping factor, based on products of reported gate fidelities, rather than drawing mappings randomly.

The selection avoids especially poor qubits and couplers, while averaging still spreads residual calibration errors. Variation across assignments is treated as systematic because the same assignments are reused in target and calibration circuits; it is not included in the plotted statistical error bars.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
