2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Re-Uploading Depth as Model Capacity

In a one-qubit re-uploading classifier, each additional layer supplies another data-dependent rotation and another set of trainable parameters. Depth therefore acts as model capacity: more layers allow the circuit to trace more complicated mappings from feature space to the Bloch sphere.

The circle experiment visibly improves from one through four layers. With four layers, the ion-trap classifier reaches $93\pm2$ percent accuracy on 1,000 test points, compared with 97 percent for the exact simulation. The experimental boundary remains less sharp because finite sampling and hardware errors create locally inconsistent labels.

Increasing depth is not free. The controller's on-chip memory permits only 16 phase-modulation steps and limits this implementation to six layers, while longer sequences accumulate additional opportunities for drift and gate error. The observed improvement therefore illustrates a capacity-resource tradeoff rather than a claim that arbitrary depth is practical.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
