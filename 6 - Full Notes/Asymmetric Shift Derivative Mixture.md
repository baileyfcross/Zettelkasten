2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Asymmetric Shift Derivative Mixture

Unequal positive and negative parameter shifts do not generally isolate a first derivative. For a two-eigenvalue quantum cost, their difference returns a known linear combination

$$
a(\gamma_1,\gamma_2)f'(\theta)+b(\gamma_1,\gamma_2)f''(\theta).
$$

The curvature term vanishes when the shifts are equal, explaining why the centered parameter-shift rule is an exact first-derivative identity. A one-sided choice leaves both slope and curvature in the measured quantity, which is the exact source of one-sided finite-difference bias in this circuit family.

This perspective treats the second derivative as information naturally present in asymmetric measurements rather than only as an error term. An optimizer could potentially consume the mixture directly instead of first reconstructing its components.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

