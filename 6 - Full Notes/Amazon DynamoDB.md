2026-09-27 18:58

Status: #baby

Tags: [[AWS Managed Database Services]]

# Amazon DynamoDB

Amazon DynamoDB is a managed NoSQL key-value and document database designed for low-latency access at scale. Tables use a partition key and optional sort key rather than relational joins and a fixed cross-item schema.

Provisioned or on-demand capacity determines how throughput is consumed, and applications must design keys to distribute load. Features such as streams, backup, and DAX extend the service, but data modeling begins from access patterns rather than normalizing relations.

Global secondary indexes introduce alternate partition and sort keys for access patterns the base table cannot serve efficiently, while global tables replicate multi-active data across regions. Both extend the original key design and therefore add write, consistency, and cost implications that should be planned before traffic makes a poor partitioning choice difficult to change.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
