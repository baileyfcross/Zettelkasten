2026-09-28 03:19

Status: #baby

Tags: [[Health Data Privacy and Integration]]

# Late Clinicogenomic Integration

Late clinicogenomic integration builds separate models for clinical and genomic data and combines their predictions or scores. Each source can use methods suited to its own scale and structure before the outputs are fused.

Separation reduces direct competition between a small clinical feature set and a large genomic one, and it makes each source's contribution easier to inspect. It may miss interactions that require joint features, however. The combining rule and both component models must be trained inside the same validation framework to avoid optimistic performance.

# References

[[healthcaredataanalytics.pdf]]
