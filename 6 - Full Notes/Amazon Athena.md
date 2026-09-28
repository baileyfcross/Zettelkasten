2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# Amazon Athena

Amazon Athena is a serverless interactive query service that uses SQL to analyze data stored in Amazon S3. Instead of loading the data into a dedicated database server, a query reads the relevant objects using table metadata, often supplied by the [[AWS Glue Data Catalog]].

Athena is well suited to ad hoc analysis, logs, and data-lake exploration. Query cost and speed depend partly on the volume scanned, so partitioning data and using efficient columnar formats can reduce unnecessary reads.

Workgroups add usage and configuration boundaries for teams or applications. Within a dataset, partition pruning, compression, and columnar formats such as Parquet reduce unnecessary reads, while avoiding `SELECT *` limits columns scanned. These physical data choices are part of query design because Athena charges according to data processed.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
