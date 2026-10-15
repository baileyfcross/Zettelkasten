2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Quantum Optical Neuron Training

Training presents labeled objects one at a time, converts each coincidence measurement into a predicted probability, and minimizes mean binary cross-entropy over the training set. [[Gradient Descent]] updates the probe parameters and scalar bias. The model-dependent probe derivative is determined by the overlap of the input field with both the probe and the probe's parameter derivative.

If a usable analytic or experimental gradient is unavailable, the paper proposes coordinate descent: evaluate the loss over a discrete neighborhood in parameter space and choose the lowest-loss setting for the next epoch. For a real spatial-light-modulator model, the parameter derivative can be approximated from the classifier score and an amplitude measurement made in the input branch before the beam splitter. That measurement can be collected offline once per training object, separating training diagnostics from later inference.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
