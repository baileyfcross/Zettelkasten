2026-11-11 18:27

Status: #baby

Tags: [[Parallel Program Design]]

# Flynn's Taxonomy

Flynn's taxonomy classifies computer architectures by the number of instruction streams and data streams they process. SISD describes one instruction stream operating on one data stream, SIMD applies one instruction stream across multiple data elements, MISD applies multiple instruction streams to one data stream, and MIMD permits multiple instructions over multiple data streams.

The classification connects an algorithm's form to a target machine. Data-parallel work maps naturally to SIMD-style execution, while independently executing tasks and distributed processes generally require the looser coordination available in MIMD systems.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

