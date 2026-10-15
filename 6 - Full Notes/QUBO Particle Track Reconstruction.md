2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# QUBO Particle Track Reconstruction

Particle tracking reconstructs charged-particle trajectories from detector hits. A QUBO formulation first groups hits from successive detector layers into candidate doublets or triplets and assigns a binary variable to each candidate. Linear terms score an individual segment, while pairwise couplings reward geometrically compatible segments or penalize conflicting assignments.

The resulting binary quadratic Hamiltonian has its low-energy configuration at the selected set of track segments. Quantum annealing, QAOA, or variational eigensolvers can then be used as optimization mechanisms. The formulation exposes the combinatorial structure, but a realistic event produces far more candidates than current devices can represent: even relatively favorable scenarios can require hundreds of binary sites, and general cases reach tens of thousands.

Partitioning the QUBO into smaller subproblems is therefore part of the algorithm, not a neutral implementation detail. It may discard global consistency or shift substantial work to classical preprocessing. Quantum results should be compared with graph neural networks and established combinatorial Kalman-filter pipelines on reconstruction efficiency, false tracks, scaling, and total compute cost. A 100-qubit device tests larger local subproblems without by itself solving full-event tracking.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
