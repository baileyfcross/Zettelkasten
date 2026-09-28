2026-09-27 20:01

Status: #baby

Tags: [[AWS Data Lake Architecture and Governance]]

# Data Lake Data Mart Zone

The data mart zone contains curated subsets shaped for a particular business domain, team, report, or decision process. A mart can present only the dimensions, measures, history, and access appropriate to its consumers rather than exposing the full lake. This improves usability and isolation, but each mart should retain lineage to shared source data so local definitions do not silently diverge.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

