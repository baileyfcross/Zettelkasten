2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Policy-Gradient Diffusion at a Barren-Plateau Edge

In an exponentially flat region, nearly constant rewards turn the sampled REINFORCE update into a random walk of the Gaussian mean. The paper derives mean-square displacement proportional to the iteration count, learning-rate squared, reward squared, inverse episode count, and the trace of the inverse covariance.

Near a plateau's edge, this diffusion can sample configurations across the boundary into a nonzero-slope region. Their higher rewards then bias subsequent updates, giving policy gradient a route that local gradient-free searches may miss. The numerical trajectories display alternating exploration and exploitation consistent with this interpretation.

Deep inside a high-dimensional plateau, the mechanism still stalls. The explored hyperball's radius grows only with the square root of the number of iterations, while its volume becomes a vanishing fraction of the surrounding parameter hypercube as dimension rises. The claimed benefit is therefore edge navigation, not a general cure for barren plateaus, and differs from the depth-control strategy in [[VAns Barren Plateau Mitigation]].

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
