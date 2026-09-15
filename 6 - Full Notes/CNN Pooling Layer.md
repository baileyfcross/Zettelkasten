2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# CNN Pooling Layer

A pooling layer downsamples a [[Convolutional Feature Map]] by applying the same summary operation to successive local regions. Max pooling keeps the largest response in a region; average pooling keeps its mean. This reduces the amount of positional detail carried to the next stage.

Pooling can help a [[Convolutional Neural Network]] recognize a feature without depending on its exact location. The tradeoff is that detailed spatial relationships may be lost. Kelleher uses this limitation to motivate later models that aim to preserve how object parts are arranged, rather than treating the mere presence of parts as sufficient.

# References

[[deeplearning_mit.epub]]
