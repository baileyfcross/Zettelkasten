2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Spatial-Light-Modulator Probe Parameterization

An amplitude spatial light modulator provides a concrete parameter layer for a [[Trainable Single-Photon Probe State]]. Each greyscale cell carries a real parameter, and the probe field is modeled as a normalized sum of square top-hat functions centered on the modulator pixels. Normalization makes the pattern a valid single-photon spatial state while coupling every effective weight through the parameter norm.

With this model, the classifier score becomes the squared magnitude of a weighted sum of local cross-correlations between the input field and a pixel aperture. The construction turns a two-dimensional modulator pattern directly into the optical analogue of a weight vector. The paper uses a $32\times32$ amplitude-modulated probe in simulation, while noting that phase-only modulators are another possible implementation and may tolerate loss better.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
