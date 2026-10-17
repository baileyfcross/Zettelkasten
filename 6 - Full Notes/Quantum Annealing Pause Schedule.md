2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Quantum Annealing Pause Schedule

A pause schedule follows the usual anneal to a selected location $s_p$, holds the Hamiltonian fixed for a duration $t_p$, and then resumes the remaining schedule. It adds two controls beyond total anneal time: where the pause occurs and how long the system is allowed to relax there.

The pause is useful only in a limited region. Early in the schedule the system may already track equilibrium, while late in the schedule transition rates can be too slow for the hold to change populations. The useful window lies between those regimes, where relaxation remains possible but is no longer instantaneous.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

