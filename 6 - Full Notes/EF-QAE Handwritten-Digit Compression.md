2026-10-12 01:33

Status: #baby

Tags: [[Enhanced Feature Quantum Autoencoders]]

# EF-QAE Handwritten-Digit Compression

The paper's second experiment compresses 8-by-8 grayscale images of handwritten zeros and ones. Pixel values are normalized and encoded as amplitudes of a six-qubit quantum state, and both the standard and enhanced autoencoders use four circuit layers.

The training set contains twenty images, ten from each class. The enhanced model receives a scalar feature of 1 for a zero and 2 for a one; these values are class identifiers rather than features derived from the image geometry. The evaluation includes thirty test images from each class in addition to the training examples.

The enhanced feature quantum autoencoder reaches a lower training cost and produces visibly better reconstructions and higher output fidelities than the standard QAE in the reported simulation. Unlike the Ising case, it surpasses the standard model with fewer function evaluations, which the authors attribute to feature conditioning making the optimization landscape easier to navigate.

# References

[[2021 - Quantum autoencoders with enhanced data encoding.pdf]]
