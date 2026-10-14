2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Circuit-Centric Quantum Classifier Noise Robustness

Unitary model layers do not amplify the norm distance between an ideal input state and a perturbed one. Likewise, the deviation caused by imperfect gates is bounded by the accumulated deviations of the individual operations rather than being multiplied from layer to layer. The paper gives a loose worst-case state-error bound of $4L\delta$ for $L$ parameterized gates whose parameter errors are each bounded by $\delta$.

Simulations on the eight-qubit SEMEION and reduced MNIST classifiers found that 0.1 percent uncorrelated parameter noise had no classification effect in about 60 percent of runs and a mean relative test-error impact of 1 percent. At 1 percent noise the mean impact rose to 7 percent, while 10 percent noise caused unstable and often severe degradation, with a 60.2 percent mean relative impact.

These results support tolerance to small input and parameter perturbations in the simulated architecture, not fault tolerance. They omit many correlated, decoherence, and measurement errors that a physical device can introduce, and large perturbations can require retraining. Resource and sampling limitations remain separate concerns described by [[Circuit-Centric Quantum Classifier Resource Scaling]].

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
