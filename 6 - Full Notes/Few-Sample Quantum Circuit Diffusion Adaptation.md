2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Few-Sample Quantum Circuit Diffusion Adaptation

Few-sample circuit diffusion adaptation extends a pretrained generator to a larger circuit size using a small set of expensive new examples instead of rebuilding the full training corpus. The paper starts from an entanglement model trained on three through eight qubits and fine-tunes separate variants for nine- and ten-qubit circuits.

Before adaptation, average performance on the larger sizes appears reasonable but hides complete failure on some target Schmidt-rank vectors. Fine-tuning with far fewer circuits per target than the tens of thousands used originally increases mean accuracy and, more importantly, removes the target patterns for which no correct sample was found in the reported evaluation.

Adapting only to the new size can reduce performance on older sizes. The authors suggest mixing new examples with previously known tasks if retaining old behavior matters. The method makes extension to tens of qubits more plausible, but it does not overcome the large-system data and conditioning bottlenecks in [[Quantum Circuit Diffusion Scalability Limits]].

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
