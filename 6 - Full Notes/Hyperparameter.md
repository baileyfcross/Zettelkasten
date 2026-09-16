2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]]

# Hyperparameter

A hyperparameter is a modeling choice set outside the ordinary parameter-fitting step. The neighbor count in [[K-Nearest Neighbors]], the span in LOESS, and the number of retained dimensions are examples that control flexibility or representation.

Choosing the value by minimizing training error creates optimistic bias. [[Cross-Validation]] estimates performance on held-out folds so competing hyperparameters can be compared without using the final test set for tuning.

Kelleher contrasts manually fixed neural-network choices with weights fitted during training. The selected [[Activation Function|activation function]], [[Convolutional Stride|convolution stride]], and [[Learning Rate|learning rate]] are examples of choices that shape the training procedure or architecture rather than being adjusted by the ordinary parameter update.

The book tunes decision-tree complexity and loss choices by comparing held-out behavior, and it controls ensemble capacity through settings such as feature sampling, tree count, depth, learning rate, and boosting rounds. These choices shape the fitted procedure without being ordinary learned coefficients.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[deeplearning_mit.epub]]

[[essentialsofdatascience.pdf]]
