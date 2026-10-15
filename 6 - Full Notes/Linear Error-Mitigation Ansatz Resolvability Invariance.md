2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Linear Error-Mitigation Ansatz Resolvability Invariance

Suppose the same affine mitigation map $C_m=a_1\widetilde C+a_2$ is applied to two noisy cost values. Their separation is multiplied by $a_1$, while the standard deviation of their estimators is multiplied by the same factor. The additive term cancels in the comparison, giving pairwise relative resolvability $\chi=1$ for any noise process.

The result means that a shared linear correction is neutral with respect to cost concentration: it neither reduces nor increases the shots needed to resolve those two points. Under global depolarizing noise, the optimal affine map can even correct every mean value exactly while leaving this finite-shot resolution unchanged.

Neutral resolvability does not mean the method is useless. By correcting [[Noise-Driven Cost Landscape Corruption]], a learned linear map can improve optimization when concentration is not dominant. Nor does the calculation include the samples required to learn the affine parameters.

The 20-qubit Ising experiments instantiate the same affine idea for traceless Hamiltonian terms as $\langle O\rangle_{\mathrm{noisy}}\approx C\langle O\rangle_{\mathrm{exact}}$. They estimate $C$ from perturbative, shallow-depth, or zero-angle calibration circuits and divide the measured energy by it. [[Twenty-Five-Layer Error-Mitigation Frontier]] shows that this can extend useful output estimation even though a shared rescaling cannot improve pairwise trainability by itself.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
