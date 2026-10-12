2026-09-27 20:01

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon EBS Snapshot

An Amazon EBS snapshot is a point-in-time backup of an EBS volume stored durably by AWS. The first snapshot captures used blocks and later snapshots are incremental, although each snapshot can restore a complete volume. Snapshots can be copied across regions or accounts and automated through lifecycle policies. Application-consistent recovery may require quiescing writes because block capture alone does not understand application transactions.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

