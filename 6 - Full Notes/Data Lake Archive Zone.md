2026-09-27 20:01

Status: #baby

Tags: [[AWS Data Lake Architecture and Governance]]

# Data Lake Archive Zone

The archive zone retains data that is no longer needed for active analysis but must remain available for historical, legal, or compliance reasons. It favors low storage cost over immediate retrieval and should have retention and deletion rules derived from policy. Moving data to archive is a lifecycle transition: catalogs and consumers must know its availability and retrieval delay rather than treating it as silently missing.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

