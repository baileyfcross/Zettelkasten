2026-09-27 21:45

Status: #baby

Tags: [[Azure Data Platform Architecture]]

# Azure Data Ingestion Layer

An Azure data ingestion layer accepts batch files, database changes, events, or device telemetry and delivers them to processing or durable storage. Event Hubs serves general high-throughput streams, IoT Hub adds device-oriented bidirectional communication, and Data Factory or transfer tools handle batch movement. Selection depends on arrival mode, ordering, replay, protocol, volume, backpressure, and whether the source can connect directly to the cloud.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

