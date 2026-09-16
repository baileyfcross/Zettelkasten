2026-09-15 02:20

Status: #baby

Tags: [[Artificial Neural Network Structure]] · [[Deep Feature Representation]]

# Autoencoder

An autoencoder is a neural network trained to reconstruct its input at its output. An encoding hidden layer transforms the input into an internal representation, and a decoding layer uses that representation to rebuild the original values.

The architecture must avoid a trivial copy path if its representation is to be informative. Kelleher gives a narrower hidden layer as one bottleneck: the network has to retain useful structure while discarding some redundant information. [[Layer-Wise Autoencoder Pretraining]] once used successive encoders to initialize deep networks, though the book notes that most deep networks no longer require that particular procedure.

As a feature learner, the encoder maps observations into a latent representation while the decoder supplies a reconstruction objective. Sparse, denoising, stacked, and variational variants constrain that representation in different ways.

# References

[[deeplearning_mit.epub]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]
