2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Topological State-Ensemble Learning

The topology benchmark uses a one-qubit ensemble forming a ring in the Bloch sphere's $X$-$Z$ plane. States are generated as $e^{-ixY}|0\rangle$ with $x$ uniform over $[0,2\pi)$, a simple model of continuously encoded classical data.

Because fidelity-kernel MMD cannot distinguish this ring from Haar noise, training uses [[Quantum State-Ensemble Wasserstein Distance]]. Forty diffusion steps transform the ring toward random states and the learned reverse process restores the circular support.

The squared $Y$ expectation measures deviation from the plane. Its target value is zero; generated training and test ensembles reach approximately $0.00367\pm0.0251$ and $0.00506\pm0.0439$. The experiment demonstrates topology-sensitive loss selection on one qubit, not large-scale topological learning.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

