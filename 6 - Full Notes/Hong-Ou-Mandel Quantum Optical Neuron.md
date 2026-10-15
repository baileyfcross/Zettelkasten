2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Hong-Ou-Mandel Quantum Optical Neuron

A Hong-Ou-Mandel quantum optical neuron uses two single photons and a balanced beam splitter as a binary classifier. One photon carries an object-dependent spatial field, while the other carries a [[Trainable Single-Photon Probe State]]. Their interference turns spatial similarity into a [[Two-Photon Coincidence Similarity Readout]], which is converted into a class probability by scalar post-processing.

The learned probe is held fixed during inference, so a new object is classified by sending its photon through the same interferometer and estimating the output coincidence rate. The device acts like a unit-depth neuron rather than a general optical network: the interference supplies an overlap operation and a square-magnitude nonlinearity, while a bias and sigmoid complete the response. Its distinctive feature is that the prediction can be obtained with non-imaging detectors instead of reconstructing the object's pixels.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
