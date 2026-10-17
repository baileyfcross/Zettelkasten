2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Sequential QuDDPM Training Cycles

A $T$-step QuDDPM is trained from the noisiest reverse step toward the final data step. At cycle $k$, the forward scrambling process supplies the true intermediate ensemble $S_k$, while the already trained reverse suffix transforms fresh terminal noise into a generated ensemble at the same diffusion level.

The next denoising circuit is optimized so that this generated ensemble matches $S_k$. Repeating the procedure converts one difficult transport from full noise to structured data into $T$ local ensemble-matching tasks.

The sawtooth training curve is a direct consequence of this schedule: inserting a newly initialized denoising circuit temporarily increases the distance, after which optimization brings the generated trajectory back toward the forward-diffusion trajectory. Independent test samples follow the same path in the reported small simulations.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

