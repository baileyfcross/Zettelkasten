2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Foundations and Hardware Portability]]

# Java Vector Species Selection

Java vector species selection chooses the primitive element type and requested vector shape for an algorithm. A fixed 128-bit species favors broad portability and stable layout, a wider fixed species targets known hardware, and `SPECIES_PREFERRED` asks the runtime for its favored shape.

The preferred choice supports [[Vector-Length-Agnostic Programming]] but increases the number of shapes that logic and tests must cover. A fixed wide choice may achieve peak throughput on a controlled server fleet yet scalarize elsewhere. The book therefore treats selection as an empirical design decision: preserve correctness at every width and benchmark the machines that will actually run the code.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
