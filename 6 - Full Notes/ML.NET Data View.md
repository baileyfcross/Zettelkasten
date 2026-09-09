2026-09-08 21:16

Status: #baby

Tags: [[ML.NET Recommendation Applications]]

# ML.NET Data View

`IDataView` is ML.NET's tabular data abstraction for columns with defined names and types. It supports lazy, cursor-based access so pipelines can work with datasets that need not be fully loaded into memory.

Loaders create data views from files or in-memory objects, and transformations produce new logical views without immediately materializing every value. The schema connects application data to pipeline stages and must match the columns an estimator expects.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
