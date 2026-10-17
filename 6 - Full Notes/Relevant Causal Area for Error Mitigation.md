2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# Relevant Causal Area for Error Mitigation

An observable does not necessarily depend on noise from the entire $N\times L$ circuit. The relevant area $A$ is the intersection between the observable's backward causal cone and the forward causal cone of the nontrivial part of the initial state. Errors outside this intersection cannot affect the measured expectation value.

When $|A|\ll NL$, the appropriate noise exponent is $\epsilon|A|$ rather than $\epsilon NL$. Both signal attenuation and mitigation overhead can then be exponentially smaller than a whole-circuit estimate suggests. Resource forecasts should therefore use causal coverage for the actual observable and state, while retaining full circuit volume for nonlocal observables whose cones spread across the computation.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

