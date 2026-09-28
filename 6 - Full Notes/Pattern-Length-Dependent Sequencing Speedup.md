2026-09-28 03:43

Status: #baby

Tags: [[Genome Sequencing Acceleration]]

# Pattern-Length-Dependent Sequencing Speedup

Pattern-length-dependent sequencing speedup occurs when the accelerator's fixed setup and transfer cost is amortized over more comparison work. Longer source data or larger batches can keep a streaming matcher busy enough for its parallel datapath to dominate overhead.

The book reports different gains for KMP and BWA and notes that workload size changes the result. A benchmark should therefore disclose source length, pattern length, batch size, and whether preprocessing and transfer are included.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

