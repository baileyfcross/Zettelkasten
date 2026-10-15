2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Optimal Parameter Resilience Is Not Trainability

Optimal parameter resilience means that a noisy cost function and its ideal counterpart share the same minimizing parameters. A common example is global depolarizing noise that applies the same positive rescaling and constant shift throughout the landscape, leaving the argmin unchanged.

This property does not guarantee that the minimum can be found efficiently. The rescaling can compress all cost differences until finite-shot estimates cannot reliably distinguish candidate parameters, producing the sampling burden described by [[Noise-Induced Barren Plateau Shot Complexity]]. The optimum may remain in the same location while becoming statistically inaccessible.

The distinction separates geometric correctness from operational learnability. It also limits what can be inferred from results such as [[QAE Local Cost Depolarizing-Noise Resilience]]: preservation of the minimizing parameters is valuable, but it is not by itself a trainability guarantee.

Hardware evidence provides the complementary case. [[Unmitigated SPSA VQE under Observable Damping]] often converges below the first excited-state energy even though the energy is damped and the damping factor varies with parameters. This shows that approximate resilience can be sufficient at small depth, while the observed parameter dependence prevents assuming that the same behavior persists for every problem or deeper circuit.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
