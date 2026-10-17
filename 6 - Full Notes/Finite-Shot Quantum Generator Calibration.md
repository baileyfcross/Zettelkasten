2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Finite-Shot Quantum Generator Calibration

The image experiments use 3,000 shots both to read generator probabilities and to estimate parameter-shift gradients. To justify that budget, the study separately trains the same five-qubit generator family to approximate a discrete Gaussian distribution over 32 computational-basis outcomes.

The calibration minimizes maximum mean discrepancy between the circuit distribution and the target Gaussian. With a five-layer circuit, learning rate $0.01$, 800 iterations, and 3,000 shots, the generated distribution follows the target and the sampled training loss decreases, although it remains noisier than the ideal target curve.

This experiment shows that 3,000 shots can provide usable optimization information for one controlled five-qubit distribution. It does not establish that this is an optimal or universally sufficient budget for adversarial image training. Shot needs depend on circuit depth, postselection probability, gradient scale, and the number of generator parameters evaluated through [[Hybrid Quantum Generator Gradient Estimation]].

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
