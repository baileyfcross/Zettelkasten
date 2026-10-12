2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# cuDNN

cuDNN is NVIDIA's CUDA Deep Neural Network library for GPU-optimized neural-network primitives such as convolution, pooling, activation, and normalization. Supported frameworks can call the library automatically instead of implementing and tuning every primitive themselves.

cuDNN is also part of the deployment compatibility chain. A framework or container is built against particular CUDA and cuDNN versions, so validated combinations of host driver, runtime, library, framework, and GPU reduce runtime failures and inconsistent execution.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

