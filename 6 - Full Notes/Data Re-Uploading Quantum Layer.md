2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Data Re-Uploading Quantum Layer

A data re-uploading layer is a one-qubit unitary whose angles combine input features with trainable weights and offsets. Stacking these layers reintroduces the same sample at successive circuit times, allowing later rotations to transform feature information that earlier rotations have already mixed.

The paper evaluates two forms. Ansatz A supports an arbitrary-dimensional feature vector by using $R_z(\phi)R_y(\omega\cdot x+\alpha)$, so a learned projection of all features enters the $Y$ rotation. Ansatz B is restricted to two-dimensional data and uses $R_z(\omega x_2+\beta)R_y(\nu x_1+\alpha)$, placing a separate feature in each rotation.

Both constructions make the executed unitary depend on the current example even after training. This is the classifier counterpart of [[Linear Feature Reuploading in EF-QAE]], although here the repeated encoding drives a one-qubit decision state rather than an autoencoder's compression circuit.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
