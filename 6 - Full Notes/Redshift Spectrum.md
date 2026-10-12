2026-09-27 20:01

Status: #baby

Tags: [[AWS Data Engineering and Analytics Optimization]]

# Redshift Spectrum

Redshift Spectrum lets Amazon Redshift issue SQL queries against external data stored in Amazon S3 rather than loading every dataset into warehouse storage first. External table definitions connect object data to the query engine, often through the Glue Data Catalog. Spectrum supports joining lake data with warehouse tables, but file format, partitioning, predicate selectivity, and scanned bytes strongly affect both performance and cost.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

