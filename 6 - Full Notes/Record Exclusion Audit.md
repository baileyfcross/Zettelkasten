2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]] · [[Data Quality and Missing Data]]

# Record Exclusion Audit

A record exclusion audit preserves or counts observations removed by each filtering rule. Instead of viewing exclusion as a silent side effect, the analyst records why rows left the analysis and how many were affected.

The audit can reveal selection bias, especially when a required measure is missing for most people with the outcome. It also supports rollback and verification by showing that retained and excluded partitions reconcile with the input dataset.

Removing observations with a missing target is a consequential modeling decision in the book's preparation workflow. Recording the affected rows and counts distinguishes a justified analytic population from an accidental loss of data.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[essentialsofdatascience.pdf]]
