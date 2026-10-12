2026-09-16 01:48

Status: #baby

Tags: [[Deep Feature Representation]]

# Convolutional Feature Transfer

Convolutional feature transfer reuses internal activations from a neural network trained on one image task as features for another. Earlier layers often capture broadly useful edges and textures, while later layers are more specialized.

A target task may freeze the pretrained network, extract fixed feature maps, or fine-tune selected layers. Transfer is strongest when the source and target visual domains share relevant structure.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]
