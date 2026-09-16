2026-09-15 23:23

Status: #baby

Tags: [[R Time Series Data Structures]]

# zoo Core Data

The core data of a [[zoo Time Series Object]] are its observation values without the attached [[Time Index]]. The `coredata` operation exposes these values for computations that do not need time coordinates, while the index remains separately accessible. This separation makes it possible to apply matrix or vector operations to measurements and then restore or preserve their temporal organization rather than confusing time with an ordinary data column.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
