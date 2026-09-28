2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# AWS Glue Data Catalog

The AWS Glue Data Catalog is a centralized metadata repository for datasets. Tables record properties such as storage location, schema, and data format so analytics services can interpret files without embedding those details in every query.

Glue crawlers can inspect data sources and populate or update catalog definitions. Services such as [[Amazon Athena]] and Amazon EMR can reuse the catalog, making it a shared structural map for a data lake rather than the place where the underlying data itself is stored.

The catalog also becomes a governance junction for [[AWS Lake Formation]], Glue jobs, and Redshift Spectrum. Because several engines depend on the same definitions, table ownership, partition updates, schema evolution, and business meaning must be controlled; automating discovery does not guarantee that inferred metadata is correct.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
