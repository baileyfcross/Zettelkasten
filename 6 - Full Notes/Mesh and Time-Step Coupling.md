2026-09-14 00:55

Status: #baby

Tags: [[Finite Element Thermal Modeling]]

# Mesh and Time-Step Coupling

Spatial element size and temporal step size jointly control a transient finite-element solution. A fine mesh cannot recover a rapid event skipped by coarse time steps, while very small time steps cannot resolve a steep spatial gradient on an inadequate mesh.

Both settings affect cost and convergence, and adaptive solvers may vary the actual step during a run. Separate [[Mesh Independence Study|mesh]] and [[Time-Step Independence Study|time-step]] checks help identify which discretization limits the accuracy of a reported peak or history.

# References

[[cosmolheattransfermodels.pdf]]

