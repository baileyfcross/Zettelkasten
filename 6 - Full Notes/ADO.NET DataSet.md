2026-09-26 22:56

Status: #baby

Tags: [[ADO.NET Database Access]]

# ADO.NET DataSet

An ADO.NET `DataSet` is a disconnected in-memory container for one or more data tables and their relationships. A [[ADO.NET DataAdapter|data adapter]] can populate it from a provider, after which code can work with the data without holding the database connection open.

This model favors editable, transportable tabular state over the sequential streaming of an [[ADO.NET DataReader]]. Reconnecting changes to the data source requires explicit adapter commands and conflict-aware update behavior.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

