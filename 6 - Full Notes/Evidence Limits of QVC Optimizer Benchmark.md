2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Evidence Limits of QVC Optimizer Benchmark

The optimizer review is broad in configurations but thin in repeated evidence: each problem variation used only three random initializations. Its VQE objectives were random ten-term Hamiltonians rather than molecular Hamiltonians, its QAOA study used only MaxCut, and most circuits belonged to the hardware-efficient family.

The noise evidence came from simulation rather than hardware, and the largest VQE cases removed both shot noise and derivative-free competitors. The study also focused on final performance rather than scaling, circuit evaluations, or total shots. These choices limit both statistical confidence and external validity.

The paper estimates that one excited-state optimization routine could cost more than one million dollars on contemporary hardware, illustrating why direct validation was omitted. The resulting guidance is valuable for choosing candidates, but it remains a hypothesis for realistic hardware rather than a definitive universal ranking.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

