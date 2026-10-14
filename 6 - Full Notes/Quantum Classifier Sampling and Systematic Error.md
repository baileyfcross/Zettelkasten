2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Quantum Classifier Sampling and Systematic Error

Repeated measurement reduces the statistical uncertainty of a one-qubit classifier only until hardware systematics dominate. In the circle experiment, classification error relative to simulation falls from about 12 percent at low repetition count to about 4 percent around 100 repetitions, then remains near that level despite further sampling.

The residual error comes from phase and timing jitter, laser-qubit detuning, intensity fluctuations, beam pointing, and occasional background-gas collisions that erase the final state. The frequency shift varies by roughly 2 kilohertz over a typical ten-minute experiment, and detuning or intensity scans change classification error by several percentage points.

The experiment reduces its Rabi frequency from 312 to 40 kilohertz so absolute fluctuations have less influence, reporting an overall classifier-output error near 2 percent after this adjustment. These observations explain why the hardware decision boundaries in [[Single-Qubit Re-Uploading Classifier Benchmark]] are less sharp than their exact simulations even when the underlying parameters match.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
