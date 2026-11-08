2026-11-08 16:00

Status: #baby

Tags: [[REST Framework and Serverless Implementations]]

# Experience Process and System API Layers

An API portfolio can separate system, process, and experience interfaces. System APIs hide databases, legacy applications, SaaS products, files, and other systems of record behind stable capabilities. Process APIs compose those capabilities through direct orchestration or distributed choreography to implement a business process.

Experience APIs adapt process and system capabilities to the needs of one channel or digital touchpoint, often through a [[Facade Pattern]]. The layers assign different accessibility and ownership boundaries: central technology teams protect systems of record, line-of-business teams compose processes, and application teams consume tailored experiences without depending directly on every backend detail.

# References

[[prorestfulapiswithmicronaut.epub]]
