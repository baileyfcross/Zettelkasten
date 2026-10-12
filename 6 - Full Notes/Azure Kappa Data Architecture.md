2026-09-27 21:45

Status: #baby

Tags: [[Azure Data Platform Architecture]]

# Azure Kappa Data Architecture

An Azure Kappa data architecture treats the event stream as the primary processing path and omits a separate batch computation layer. Durable events are processed or replayed through streaming logic and placed into a serving store. The book’s sensor example uses IoT Hub, Event Hubs, Stream Analytics, and Data Explorer. Kappa reduces duplicate pipelines but requires sufficient retention, deterministic replay, and controlled evolution of stream logic.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

