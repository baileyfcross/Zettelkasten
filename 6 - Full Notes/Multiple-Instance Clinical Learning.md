2026-09-28 03:19

Status: #baby

Tags: [[Clinical Prediction and Temporal Analytics]]

# Multiple-Instance Clinical Learning

Multiple-instance clinical learning represents a patient or case as a bag of observations while the outcome label applies to the bag rather than to each observation. A positive scan, encounter sequence, or record may contain only a few instances that explain the label.

This formulation avoids pretending that every image patch or visit has its own known outcome. The model must learn both which instances are informative and how they combine. Its interpretation should distinguish evidence localized to one instance from a patient-level conclusion, especially when the clinically relevant instance is rare.

# References

[[healthcaredataanalytics.pdf]]
