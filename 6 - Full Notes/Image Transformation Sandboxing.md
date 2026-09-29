2026-09-28 04:01

Status: #baby

Tags: [[Image Derivative Workflows]]

# Image Transformation Sandboxing

Image decoders and transformation engines process complex, potentially hostile inputs. A compromised image can exploit a parser or library, so workers should be isolated from other jobs, persistent state, unrestricted files, and arbitrary network access.

The book recommends isolation around connection handling, the transformation engine, and shared encoding or decoding components. Exclusive scratch space, strict resource limits, validated sources, and disposable workers reduce the chance that one malicious file affects later images or the wider asset store.

# References

[[highperformanceimages.pdf]]
