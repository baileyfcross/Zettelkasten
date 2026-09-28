2026-09-28 03:43

Status: #baby

Tags: [[FPGA Accelerator Co-Design]]

# FPGA Hardware-Software Co-Design

FPGA hardware-software co-design treats the host program, accelerator logic, interfaces, and data movement as one system from the beginning. Fixed, compute-intensive functions move into programmable logic while control-heavy or changeable work remains in software.

Early partitioning reveals interface and resource conflicts before either side is frozen. The design then iterates through modeling, [[Accelerator Hot-Code Profiling]], circuit synthesis, verification, integration, and deployment rather than developing hardware first and adapting software afterward.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

