2026-10-12 01:33

Status: #baby

Tags: [[Enhanced Feature Quantum Autoencoders]]

# Linear Feature Reuploading in EF-QAE

Linear feature reuploading inserts a classical feature repeatedly into the rotation gates of an enhanced feature quantum autoencoder. Each relevant rotation angle is an affine function of one feature component, with learned coefficients playing roles analogous to a weight and bias.

Repeating this construction across layers allows the circuit to process the same classical information at multiple stages. The paper compares the pattern to a feed-forward neural network in which data are reintroduced and transformed through successive layers, although the EF-QAE transformations are quantum gates and can act on entangled states.

Because the feature changes gate angles, two inputs processed with the same trained parameters can still receive different unitaries. This is the mechanism by which the [[Model Feature Vector for Quantum Compression]] tailors compression to each state. The authors use a linear rule in their experiments but explicitly leave nonlinear encoding strategies open for later study.

# References

[[2021 - Quantum autoencoders with enhanced data encoding.pdf]]
