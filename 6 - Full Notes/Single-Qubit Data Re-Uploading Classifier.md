2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Single-Qubit Data Re-Uploading Classifier

A single-qubit data re-uploading classifier encodes classical features repeatedly throughout a parameterized rotation circuit rather than loading the input once. Starting from $|0\rangle$, each layer applies a one-qubit unitary that depends on both the sample $x$ and trainable parameters, producing a final state $|\psi(x,\Theta)\rangle$.

Classification compares that state with a set of class-specific targets on the Bloch sphere. The label whose state has the greatest squared overlap with the output is selected, and training adjusts the circuit so examples approach their assigned label states.

Repeated encoding lets one qubit perform nontrivial binary, multiclass, and multidimensional classification while using minimal quantum width. The tradeoff is that capacity and accuracy depend on repeated high-fidelity operations, as described by [[Re-Uploading Depth as Model Capacity]] and demonstrated in the paper's trapped-ion experiment.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
