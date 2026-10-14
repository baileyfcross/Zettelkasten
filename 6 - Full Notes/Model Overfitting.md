2026-09-15 02:18

Status: #baby

Tags: [[Machine Learning Foundations]]

# Model Overfitting

Overfitting occurs when a model fits idiosyncrasies or noise in its training examples so closely that it performs less well on new examples. A flexible candidate function can match the observed sample without capturing the broader relationship the sample was meant to represent.

Kelleher relates this to a weak [[Inductive Bias in Machine Learning|inductive bias]] and limited data: the learner has many ways to explain the training set, including accidental correlations. A large training set can provide more evidence for a flexible neural network, but the data and assumptions still need to be balanced. [[Model Underfitting]] is the contrasting failure in which restrictions make the model too simple to fit the real pattern.

A complicated rule that explains every noisy sequence value can be less credible than a simpler rule that treats a few values as errors. [[Model Regularization]] formalizes this preference by balancing fit against complexity. The decisive evidence is performance on unused cases, because perfect training agreement alone cannot distinguish structure from memorized noise.

# References

[[deeplearning_mit.epub]]

[[machinelearning_mit.epub]]
