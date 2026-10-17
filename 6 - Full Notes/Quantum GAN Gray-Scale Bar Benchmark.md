2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum GAN Gray-Scale Bar Benchmark

The gray-scale bar benchmark defines a continuous but exactly specified image distribution for comparing quantum and classical GANs. In each $2\times2$ image, one pixel is sampled uniformly from $[0.4,0.6]$, a second is its complement, and the remaining two are zero. The experiment trains on 1,000 examples.

The construction serves two purposes. Its known distribution supports direct [[Frechet Distance Evaluation for Quantum GANs|distributional evaluation]], and its samples can be amplitude encoded with a single layer of $R_Y$ gates. This keeps quantum state preparation shallow enough that the benchmark emphasizes generator and discriminator behavior rather than a deep input-loading circuit.

The simple constraint also gives an informal training diagnostic: a generated sample should preserve the complementary pair and the allowed intensity range. The task is intentionally tiny, so competitive results show that the qGAN learned this controlled distribution but do not establish performance on natural images or high-dimensional data.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
