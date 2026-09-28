2026-09-28 03:19

Status: #baby

Tags: [[Clinical Prediction and Temporal Analytics]]

# Cost-Sensitive Clinical Learning

Cost-sensitive clinical learning assigns different consequences to different prediction errors. Missing a dangerous condition and falsely flagging a healthy patient may have unequal harms, so optimizing raw accuracy can choose the wrong operating behavior.

A cost matrix makes those asymmetries explicit during training or decision threshold selection. The values should reflect the clinical pathway, including follow-up tests, delayed treatment, and alarm burden. Because costs can vary by setting and patient, a model's best threshold is not a universal property of its score.

# References

[[healthcaredataanalytics.pdf]]
