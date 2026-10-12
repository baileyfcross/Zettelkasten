2026-09-28 03:19

Status: #baby

Tags: [[Health Data Privacy and Integration]]

# Clinicogenomic Prevalidation

Clinicogenomic prevalidation creates out-of-sample genomic predictions for patients in the development data and then assesses those predictions alongside clinical variables. Each patient's genomic score is produced by a model that was trained without that patient.

This prevents an overfit genomic model from appearing to add value merely because it predicts the same cases used for feature discovery. The resulting score can be tested against a clinical-only model, but the full procedure still requires independent validation. Prevalidation protects one comparison inside the development sample; it does not prove transportability.

# References

[[healthcaredataanalytics.pdf]]
