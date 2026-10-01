2026-09-30 21:11

Status: #baby

Tags: [[Deep Feature Representation]]

# End-to-End Learning

End-to-end learning trains a connected system directly from its original input to its final desired output. Intermediate representations and transformations are adjusted together instead of being specified and optimized as independent handcrafted stages.

An encoder can transform an image or sentence into a latent representation while a decoder turns that representation into a caption or translation. Supplying only paired inputs and final targets lets [[Backpropagation]] coordinate the entire mapping, but the result still depends on the architecture's assumptions and on training examples that cover the intended use.

# References

[[machinelearning_mit.epub]]
