2026-09-14 00:55

Status: #baby

Tags: [[Thermal Model Verification and Sensitivity]]

# Auxiliary Sweep in COMSOL

An auxiliary sweep repeats a study step across values of one or more auxiliary parameters. It is useful when parameter continuation should occur within the solver sequence or when combinations of inputs must be explored alongside the primary study definition.

Continuation can also help a nonlinear problem converge by solving an easier condition first and using that solution as the initial estimate for the next value. The resulting family should still be checked for failed cases and interpreted like a [[Parametric Sweep in COMSOL|controlled parameter study]].

# References

[[cosmolheattransfermodels.pdf]]

