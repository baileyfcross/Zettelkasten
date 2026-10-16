2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Quantum Payoff Amplitude Encoding

Quantum payoff amplitude encoding maps a path $|\omega\rangle$ to a state whose designated ancilla has amplitude $\sqrt{f(\omega)}$ in the good state and $\sqrt{1-f(\omega)}$ in the complementary state. After normalization to $f(\omega)\in[0,1]$, the good-state measurement probability is exactly the path payoff.

Conventional constructions first compute a binary register $|f(\omega)\rangle$ with coherent arithmetic and then rotate an ancilla according to that digital value. The register is only an intermediate representation; amplitude estimation ultimately consumes the ancilla probability.

[[Direct Amplitude Transformation for Payoff Functions]] removes that intermediate register by applying a polynomial directly to an already encoded amplitude. This preserves the expectation-estimation interface of the [[Quantum Derivative Pricing Pipeline]] while changing the resource profile of the payoff oracle.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
