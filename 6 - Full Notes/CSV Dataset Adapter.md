2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# CSV Dataset Adapter

DatasetReader is a DataAdapter that reads a schema description and a comma-separated data file into a ClusLib Dataset. It identifies label and record-ID columns, creates the schema, splits each row, validates column counts, and constructs typed records.

Categorical strings, identifiers, and labels are converted to stable integer codes through their metadata. The adapter boundary keeps parsing rules outside Dataset and allows another reader to implement the same fill interface.

# References

[[dataclusteringincplusplus.pdf]]

