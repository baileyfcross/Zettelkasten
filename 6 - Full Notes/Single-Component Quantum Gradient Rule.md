2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Single-Component Quantum Gradient Rule

A single-component quantum gradient rule varies one circuit parameter while holding every other parameter fixed. It reduces the full variational objective to a one-variable function

$$
f(\theta)=F(\theta_1,\ldots,\theta_{i-1},\theta,\theta_{i+1},\ldots,\theta_n),
$$

then estimates $f'(\theta)$ from evaluations at shifted values of that one coordinate.

Centered and one-sided finite differences and the centered parameter-shift rule all belong to this family. Their shared structure makes them comparable through a [[Generalized Parameter-Shift Rule]].

The restriction distinguishes these methods from the [[Simultaneous Perturbation Gradient Estimator]], which perturbs many coordinates in one random direction. Single-component rules expose an individual derivative cleanly but usually require work that grows with the number of parameters.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

