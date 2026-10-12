2026-09-28 03:19

Status: #baby

Tags: [[Health Data Privacy and Integration]]

# Early Clinicogenomic Integration

Early clinicogenomic integration joins clinical and genomic variables before model construction. A single learner receives the combined feature representation and can estimate interactions across the two sources directly.

The approach exposes all information to one model, but the much larger genomic feature set can dominate learning and increase overfitting. Scaling, missingness, and dimensionality reduction must be handled consistently within validation. Selecting genomic variables on the full dataset before evaluating the combined model would leak outcome information into the test cases.

# References

[[healthcaredataanalytics.pdf]]
