2026-09-27 20:01

Status: #baby

Tags: [[AWS Data Lake Architecture and Governance]]

# Data Lake Landing Zone

The landing zone is a temporary intake area where newly arrived data undergoes basic validation, duplicate checks, type checks, and initial processing before moving deeper into the lake. It gives ingestion failures a visible boundary instead of mixing them with accepted analytical data. The zone needs explicit success, quarantine, retry, and expiration rules so temporary arrivals do not accumulate indefinitely.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

