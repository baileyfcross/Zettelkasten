2026-09-15 02:18

Status: #baby

Tags: [[Machine Learning Foundations]]

# Model Input Space

The input space of a model contains the possible combinations of values for its input variables. Each variable supplies an axis, and each example occupies a point whose coordinates are its observed inputs. Kelleher uses income and debt as two axes to display example loan applications.

This is different from [[Model Weight Space]], whose coordinates specify possible models rather than possible cases. A learned mapping moves an input point into an activation or output representation; a [[Decision Boundary]] can then separate regions assigned different decisions. Keeping these spaces distinct prevents a change in a data point from being confused with a change in the model's parameters.

Input choice controls what regularities can be learned. Attributes that describe general characteristics can let examples share evidence across brands or individual identities, while an overly broad representation may combine populations governed by different processes. Unobserved factors remain a source of uncertainty even after many measured coordinates are added.

# References

[[deeplearning_mit.epub]]

[[machinelearning_mit.epub]]
