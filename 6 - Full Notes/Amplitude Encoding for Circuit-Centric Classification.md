2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Amplitude Encoding for Circuit-Centric Classification

Amplitude encoding associates a classical feature vector with the computational-basis amplitudes of a quantum state. An $N$-component real input is normalized and embedded into a $2^n$-component state with $n=\lceil\log_2 N\rceil$ qubits, padding the vector when its length is not a power of two.

This encoding makes the classifier narrow in qubit count because a register of $n$ qubits stores $2^n$ amplitudes. It does not make arbitrary data loading efficient: preparing a general amplitude vector still requires resources linear in the feature dimension. Efficient or approximate preparation therefore depends on exploitable input structure.

Normalization can distort datasets whose relevant information includes vector length rather than only direction. [[Noninformative Padding for Quantum Amplitude Encoding]] offers one response, while [[Tensorial Quantum Feature Map]] uses multiple encoded copies to create higher-degree features at the cost of more qubits and preparation work.

Image encodings make the loading bottleneck concrete. Exact preparation of an arbitrary pixel-amplitude state has gate complexity proportional to the number of pixels, while [[Flexible Representation of Quantum Images]] stores intensity in a separate color qubit and can require quadratically many CNOTs in the pixel count when prepared exactly. [[Variational FRQI State Preparation]] trades exactness for circuits that exploit image structure.

A later EuroSAT study shows that amplitude encoding is also sensitive to circuit placement. It works well after classical convolutions have compressed an image into a global feature vector, but performs poorly when each small raw-image patch is normalized and encoded independently in an early quanvolution. Patch normalization can suppress local magnitude and contrast, while [[Amplitude-Ordering Shaped Quantum Kernels]] shows that the pixel-to-amplitude index map determines which neighborhoods later two-qubit gates can mix.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
