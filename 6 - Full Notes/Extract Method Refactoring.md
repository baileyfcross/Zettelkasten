2026-11-11 18:27

Status: #baby

Tags: [[Software Construction and Refactoring]]

# Extract Method Refactoring

Extract method refactoring moves a coherent group of statements into a separately named function and replaces the original statements with a call. It reduces the size and number of abstraction levels in the caller while turning the extracted operation into an explicit concept.

The boundary should have a clear purpose and manageable inputs and outputs. Extracting arbitrary fragments can replace one long routine with a maze of tiny calls, so the new method's name and responsibility must make the larger algorithm easier to read.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

