2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns Informed Circuit Simplification

VAns simplifies a proposed circuit by commuting compatible gates and then applying structural identities. For an all-zero input, the paper removes leading CNOTs and leading z rotations, cancels consecutive identical CNOTs, merges consecutive same-axis rotations, and reduces long single-qubit rotation strings to a three-rotation Euler form.

Those five transformations use only classical inspection of the circuit. A sixth rule tentatively deletes gates whose removal does not worsen the cost beyond a threshold; evaluating that rule requires quantum cost estimates and adds overhead proportional to the number of deletion candidates. Gradient information from the inner optimizer can help identify candidates with little apparent influence.

For a circuit with M gates, the paper assigns the overall simplification pass O(M) scaling, excluding the shared optimizer cost. Simplification both controls resources and enables architecture jumps: after an inserted identity block is rearranged and partially deleted, the survivor need not have appeared in the initial circuit or the original dictionary.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
