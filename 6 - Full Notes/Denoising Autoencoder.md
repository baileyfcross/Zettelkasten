2026-09-16 01:48

Status: #baby

Tags: [[Deep Feature Representation]]

# Denoising Autoencoder

A denoising autoencoder receives a corrupted version of an input but is trained to reconstruct the clean original. Successful reconstruction requires learning stable structure rather than simply copying individual values.

The corruption process defines which variations the representation should ignore. Features learned this way can be more robust and can initialize deeper models or support downstream tasks.

Training two perturbed versions toward the same clean output pressures the encoder to assign them similar codes. A face representation can therefore learn to ignore glasses, small translations, or rotations when those changes are included deliberately in the corruption process. The selected perturbations define the intended invariance.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]

[[machinelearning_mit.epub]]
