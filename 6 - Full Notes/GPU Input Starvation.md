2026-10-03 16:51

Status: #baby

Tags: [[Accelerated GPU Storage and Networking]]

# GPU Input Starvation

GPU input starvation occurs when an accelerator has runnable work but waits because storage, preprocessing, decoding, transfer, or request delivery cannot supply data at the required rate. Low device utilization is the visible symptom, not proof that the GPU is too slow or oversized.

Diagnosis compares the GPU timeline with CPU work, storage throughput, queue behavior, transfers, and batch formation. Increasing accelerator capacity cannot fix a slower input pipeline; the remedy belongs at the stage that fails to keep the device supplied.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

