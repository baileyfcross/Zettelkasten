2026-09-06 22:09

Status: #baby

Tags: [[Scalable Social Data Processing]]

# MapReduce

MapReduce is a distributed computation pattern that maps input partitions into intermediate records and reduces grouped records into results. Systems such as Pig and Hive can generate sequences of these jobs from higher-level transformations.

The model automates parallel work and data redistribution, but separate jobs impose overhead and typically reread intermediate state. Algorithms with repeated rounds therefore benefit from caching and long-running workers.

# References

[[bigdataincomplexandsocialnetworks.pdf]]
