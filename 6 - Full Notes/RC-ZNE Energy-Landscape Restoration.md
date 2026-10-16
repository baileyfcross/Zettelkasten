2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# RC-ZNE Energy-Landscape Restoration

Error mitigation for VQE must preserve useful variation across parameter space, not only improve one optimized energy. Under coherent over-rotation, magnifying noise without randomized compiling both flattens the H2 energy landscape and changes its characteristic shape, leaving zero-noise extrapolation with a distorted family of surfaces.

Randomized compiling largely preserves the landscape's shape as the noise is magnified, although it does not remove the energy deviation by itself. Applying zero-noise extrapolation after that tailoring produces a surface whose pointwise deviation from the ideal landscape is small across the inspected two-parameter slice. Similar restoration occurs for the $XI$- and $IZ$-rotation models.

Landscape restoration provides stronger evidence than agreement at a single minimum because it indicates that the classical optimizer receives a more faithful ordering of candidate parameters. Finite ensembles can still introduce the convergence spread discussed in [[Optimizer Sensitivity under Finite Randomization]].

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
