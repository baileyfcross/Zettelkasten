2026-09-27 21:45

Status: #baby

Tags: [[Azure Data Platform Architecture]]

# Azure Medallion Architecture

Azure medallion architecture organizes lakehouse data into progressively refined layers, commonly bronze, silver, and gold. Bronze preserves source-oriented inputs, silver applies cleaning and integration, and gold presents curated business-ready structures. The layers make quality and lineage transitions visible, but their value depends on enforceable entry criteria and reproducible transformations rather than merely naming three folders or tables.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

