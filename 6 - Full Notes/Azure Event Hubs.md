2026-09-27 21:45

Status: #baby

Tags: [[Azure Data Platform Architecture]]

# Azure Event Hubs

Azure Event Hubs is a high-throughput event-ingestion service that stores an ordered stream in partitions for independent consumer groups. Producers append events and consumers track their own positions, allowing several analytical or operational pipelines to replay the same data. Partition-key choice, retention, throughput capacity, checkpointing, and consumer lag determine whether the stream can absorb load and recover from processing interruptions.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

