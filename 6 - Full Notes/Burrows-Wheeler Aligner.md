2026-09-28 03:43

Status: #baby

Tags: [[Genome Sequencing Acceleration]]

# Burrows-Wheeler Aligner

The Burrows-Wheeler Aligner, or BWA, preprocesses a reference sequence into a Burrows-Wheeler-based index and searches patterns through that transformed structure. This reverses the emphasis of [[KMP Sequence Matching]], which preprocesses the query pattern.

Index construction has a cost, but the same reference can support many searches. The accelerator must therefore distinguish one-time preprocessing from the repeated indexed lookup it is intended to speed up.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

