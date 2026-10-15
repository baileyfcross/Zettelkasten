2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Virtual Distillation Purity-Resolvability Bound

For noisy states sharing a spectrum, the [[Basis-Averaged Relative Resolvability]] of virtual distillation is bounded by a function of qubit count, copy count, and state purity. The bound is at most one and decreases monotonically as the number of copies increases.

Outside the most strongly mixed corner of the state space, the bound also decreases as purity falls. The same decoherence that makes distillation desirable therefore tends to make the mitigated cost landscape harder to resolve with finite samples. Equality occurs for pure states because taking powers does not change an already rank-one state; a special single-qubit, two-copy case also saturates the bound.

The result is an average over eigenbases, so an individual structured problem can behave differently. Its value is to show that poorer purity does not generally supply a trainability advantage merely because virtual distillation more strongly filters the spectrum.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
