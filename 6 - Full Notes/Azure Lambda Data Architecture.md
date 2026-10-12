2026-09-27 21:45

Status: #baby

Tags: [[Azure Data Platform Architecture]]

# Azure Lambda Data Architecture

An Azure Lambda data architecture maintains a batch path for complete historical recomputation and a speed path for low-latency updates, then exposes results through a serving layer. The source illustrates Event Hubs with streaming computation beside Data Factory and data-lake batch processing. Two paths improve freshness without abandoning replay, but they duplicate logic and require a defined way to reconcile their outputs.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

