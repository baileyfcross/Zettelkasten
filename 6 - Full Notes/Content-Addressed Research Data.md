2026-09-28 21:33

Status: #baby

Tags: [[Scientific Workflow Provenance]]

# Content-Addressed Research Data

Content-addressed research data identifies an artifact with a hash derived from its bytes. A path can describe where the file is expected, while the hash verifies which exact content was used and reveals silent overwriting or corruption.

The identifier does not require every large file to be copied into the experiment record. A data store can retain or retrieve the artifact separately while the computation record preserves its relative location and hash. This strengthens [[Result-to-Computation Traceability]] and lets [[Provenance Query and Comparison]] distinguish runs that used files with the same name but different contents.

# References

[[implementingreproducableresearch.pdf]]
