2026-09-28 03:19

Status: #baby

Tags: [[Health Data Privacy and Integration]]

# Intermediate Clinicogenomic Integration

Intermediate clinicogenomic integration transforms one or both data sources into learned or selected representations before combining them in a final model. Genomic variables may first become pathway scores, clusters, or a reduced feature set that can be joined with clinical covariates.

This design balances source-specific processing with joint prediction. Its main risk is hidden leakage: representation learning and feature selection are part of the model and must be repeated within each training fold. The chosen intermediate representation should also retain a clinically interpretable connection to the original measurements when possible.

# References

[[healthcaredataanalytics.pdf]]
