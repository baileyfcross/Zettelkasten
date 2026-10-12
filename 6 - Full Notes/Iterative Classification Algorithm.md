2026-09-14 21:00

Status: #baby

Tags: [[Sequence and Network Classification]]

# Iterative Classification Algorithm

An iterative classification algorithm for networks alternates between predicting node labels and rebuilding relational features from the current predictions of neighboring nodes. Initial labels usually come from a classifier using only local attributes.

Iteration lets mutually dependent predictions reinforce one another until a stopping condition is reached. It can also amplify an early mistake, so confidence controls, update ordering, and convergence behavior matter.

# References

[[dataclassification.pdf]]
