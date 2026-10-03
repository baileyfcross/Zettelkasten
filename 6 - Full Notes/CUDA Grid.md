2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# CUDA Grid

A CUDA grid is the complete collection of [[CUDA Thread Block|thread blocks]] created for one [[CUDA Kernel]] launch. It describes the total parallel work while leaving the runtime free to assign blocks dynamically to available streaming multiprocessors.

This separation between logical structure and physical placement makes a kernel portable across NVIDIA GPUs with different numbers of execution engines. New blocks can be scheduled as earlier blocks finish without changing the program's grid definition.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

