2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Data-Oriented Tech Stack

Unity's Data-Oriented Tech Stack organizes computation around the data being transformed rather than around feature-rich object instances. Jobs can divide independent work across processor cores, native arrays store tightly packed values, and the Burst compiler can optimize constrained code into efficient machine instructions.

The approach targets workloads where ordinary object-oriented layouts cause poor data locality or leave parallel hardware unused. It imposes stricter memory and API rules, so it is not automatically appropriate for every system. Performance gains come from contiguous data, predictable access, and parallelizable work, not from adopting new terminology alone.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

