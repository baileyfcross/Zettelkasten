2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Two-Photon Coincidence Similarity Readout

For input field $I$ and probe field $U$, a balanced Hong-Ou-Mandel interferometer produces the coincidence probability

$$p(1_a\cap 1_b)=\frac{1}{2}\left(\lVert I\rVert^2\lVert U\rVert^2-|\langle I,U\rangle|^2\right).$$

The squared overlap $f=|\langle I,U\rangle|^2$ acts as the classifier's similarity score. Indistinguishable normalized states suppress coincidences and give maximal overlap, whereas increasing distinguishability reduces the overlap and raises the coincidence rate. Thus the desired score can be recovered from an aggregate two-detector statistic rather than from spatially resolved measurements.

Optical loss changes the norm product, represented by a factor below one, so the raw coincidence rate is not automatically a calibrated probability of class membership. The [[Quantum Optical Neuron Nonlinear Post-Processing]] stage supplies a learned bias and sigmoid after the overlap is inferred.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
