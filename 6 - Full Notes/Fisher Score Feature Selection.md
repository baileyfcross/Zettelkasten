2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Selection Connections and Evaluation]]

# Fisher Score Feature Selection

Fisher Score ranks a feature by comparing the separation of class means with the variation inside each class. A high score favors features whose values are compact within a class and distinct across classes.

When the target similarity matrix assigns normalized positive similarity to members of the same class and zero similarity across classes, Fisher Score is equivalent to a transformed [[Laplacian Score]]. This places it inside a similarity-preserving spectral framework while retaining its supervised dependence on class labels.

# References

[[spectralfeatureselectionfordatamining.pdf]]

