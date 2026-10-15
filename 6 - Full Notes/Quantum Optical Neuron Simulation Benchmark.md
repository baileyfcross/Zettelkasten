2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Quantum Optical Neuron Simulation Benchmark

The paper numerically benchmarks a $32\times32$ amplitude-modulated quantum optical neuron on two binary tasks. MNIST images are padded from $28\times28$ to $32\times32$ for zero-versus-one classification, while CIFAR-10 images are converted to greyscale for cat-versus-dog classification. An approximately 85:15 train-test split, binary cross-entropy, and full-batch gradient descent are used.

With roughly $10^3$ trainable parameters in every compared model, the simulated optical neuron exceeds 99% test accuracy on the MNIST task and 58% on the harder CIFAR-10 task. Its MNIST result is comparable to a single artificial neuron and a small convolutional network; on the constrained CIFAR-10 comparison it performs better. These are TensorFlow simulations in which a second modulator directly encodes digital images, not measurements from a constructed interferometer, so the results establish model behavior rather than experimental speedup.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
