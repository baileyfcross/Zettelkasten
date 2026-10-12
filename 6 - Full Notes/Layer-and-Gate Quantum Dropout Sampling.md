2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Layer-and-Gate Quantum Dropout Sampling

Layer-and-gate quantum dropout separates the random selection process into a layer probability and a within-layer gate probability. At a training step, layers are selected with ratio $p_L$; eligible gates or gate groups inside those layers are then removed with ratio $p_G$. The effective probability for an eligible operation is therefore $p=p_Lp_G$.

The resulting dropout circuit is used to compute the loss, gradient, and parameter update for that step. A new layout can be sampled on the next step, so [[Training Epoch|training]] covers an ensemble of related subcircuits while updating one shared parameter set. Gates are dropped by substituting the identity, and parameterized operations must be eligible if the procedure is to prevent the model from relying on particular trainable parameters.

This factorization lets a strategy control where structural variation occurs separately from how aggressively it acts inside a chosen layer. [[Independent Quantum Dropout]] extends the scheme with distinct probabilities for rotation and entangling gates.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
