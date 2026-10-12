2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Nested Error Correction and Renormalization Flow

Successive QCNN pooling layers can be interpreted as nested quantum error correction. Measurements identify local deviations from a representative many-body state, and conditioned unitaries prevent those deviations from propagating into the smaller state passed to the next scale.

For phase recognition, the representative state acts as a stable renormalization fixed point. States in the same phase are treated as that fixed point plus sufficiently sparse local errors; repeated convolution and pooling reduces their error density and makes them flow toward the same coarse state. Classification then depends on the fixed point reached rather than on microscopic details.

The paper uses this connection to guide exact circuit construction: a convolution-pooling unit should map the fixed-point state to a shorter copy of itself and should detect and correct an allowed local error. Training can then adjust the nested correction scheme so its effective threshold approaches the target phase boundary.

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]
