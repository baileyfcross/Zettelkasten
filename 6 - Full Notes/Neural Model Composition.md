2026-09-15 02:18

Status: #baby

Tags: [[Machine Learning and Neural Networks]]

# Neural Model Composition

Model composition feeds the output of one learned mapping into another mapping. Kelleher first illustrates this by passing a weighted credit score into a decision rule; the combined process answers a more complex question than either component alone.

An [[Artificial Neural Network]] repeats this principle: each neuron computes a comparatively simple function, and successive layers use earlier activations as their inputs. The network's overall input-to-output function emerges from those connected transformations. Nonlinear [[Activation Function|activation functions]] are crucial because composing weighted sums without nonlinear steps would still produce only a linear mapping.

# References

[[deeplearning_mit.epub]]
