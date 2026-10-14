2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Trapped-Ion Single-Qubit Classifier Implementation

The experimental classifier encodes its qubit in the $S_{1/2,-1/2}$ and $D_{5/2,-1/2}$ states of one trapped $^{138}\mathrm{Ba}^+$ ion. A 1762-nanometer quadrupole transition implements rotations with a measured coherence time of 5 milliseconds and a Rabi $\pi$ time of 12 microseconds.

Each run Doppler-cools and optically pumps the ion to $|0\rangle$, applies the re-uploading pulse sequence, projects into a chosen label basis, and detects the final state through fluorescence. State initialization is reported at least 99 percent fidelity within 50 microseconds, and a 2-millisecond photon-count window cleanly distinguishes the bright and dark states.

Accurate phase control is crucial because the classifier trades qubit count for a sequence of rotations. A rubidium-disciplined synthesizer, FPGA timing, pulse shaping, and preloaded control words reduce drift and latency, while [[Ion-Trap Re-Uploading Circuit Compression]] further shortens the active sequence.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
