2026-09-27 21:45

Status: #baby

Tags: [[Azure Data Platform Architecture]]

# Azure Synapse Link for Cosmos DB

Azure Synapse Link for Cosmos DB maintains an analytical store alongside the transactional store so analytical engines can query operational data without running heavy scans against the serving path. The platform propagates changes into the column-oriented analytical representation without a customer-managed ETL pipeline. It improves freshness and workload isolation, but analytical-store support, synchronization behavior, schema, region, and cost constraints must fit the use case.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

