2026-10-18 23:53

Status: #baby

Tags: [[Java Model Hosting and Native Inference]]

# DJL ONNX Model Inference

DJL can use an ONNX-oriented engine to load a compatible ONNX model and expose its inference through Java predictors. A translator defines how application inputs become tensors and how raw model outputs become Java results.

This separates business code from low-level tensor handling while preserving an explicit preprocessing contract. Correctness depends on matching the model's names, shapes, data types, scaling, and output interpretation, not merely on successfully opening the file.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
