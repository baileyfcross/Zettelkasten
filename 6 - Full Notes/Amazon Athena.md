2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# Amazon Athena

Amazon Athena is a serverless interactive query service that uses SQL to analyze data stored in Amazon S3. Instead of loading the data into a dedicated database server, a query reads the relevant objects using table metadata, often supplied by the [[AWS Glue Data Catalog]].

Athena is well suited to ad hoc analysis, logs, and data-lake exploration. Query cost and speed depend partly on the volume scanned, so partitioning data and using efficient columnar formats can reduce unnecessary reads.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
