2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN LHC Event Representation

The collider benchmark learns three continuous observables from leading-order proton-proton production of a top-antitop pair at $\sqrt{s}=13$ TeV. MadGraph supplies the reference Monte Carlo events, and each event is represented by the Mandelstam variables $s=(p_1+p_2)^2$ and $t=(p_1-p_3)^2$ together with rapidity $y$.

These variables combine non-Gaussian kinematic scales with a more Gaussian-like rapidity distribution and nontrivial correlations, making them a compact test of multivariate event generation. The model trains on $10^4$ events drawn from a $10^5$-event reference set rather than attempting detector-level simulation.

The benchmark therefore addresses surrogate generation of selected parton-level event features. It does not replace a complete Monte Carlo chain containing showering, hadronization, detector response, selection effects, and systematic uncertainties, as considered more broadly in [[Quantum Generative Detector Simulation]].

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

