2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Near-Term Quantum Resource Benchmarks for HEP

The QC4HEP report frames selected applications against a 2023-era target of circuits with roughly 100 qubits and 100 layers of gate operations. The purpose is not to claim full physical precision, but to identify reduced systems large enough to preserve a scientifically meaningful difficulty while remaining near a plausible hardware envelope.

Its estimates place static $(2+1)$-dimensional QED on $4\times4$ to $8\times8$ lattices at about 30 to 160 qubits and roughly 10 to 100 CNOT layers using VQE or variational imaginary-time evolution. A $(1+1)$-dimensional QED scattering model with 12 to 20 sites is estimated at 30 to 100 qubits and 20 to 100 layers. Collective neutrino models map 10 to 40 neutrinos to 10 to 40 qubits, with 30 to 120 layers for variational or product-formula evolution.

These figures are problem-selection guides rather than end-to-end cost guarantees. They omit accuracy targets, sampling time, state preparation, and some compilation overheads; for example, the 40-neutrino first-order product formula still entails 2,340 CNOTs. A benchmark must therefore report physical size, logical representation, depth, gate count, measurements, and achieved error together.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
