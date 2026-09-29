2026-09-28 04:01

Status: #baby

Tags: [[Responsive Image Selection]]

# srcset Width Descriptor

The `w` descriptor states a candidate image’s intrinsic pixel width. Combined with the predicted rendered width from `sizes`, it lets the browser calculate the density each candidate would provide.

Width descriptors avoid hardcoding one density mapping when the slot changes across layouts. Candidate widths must accurately describe the files; incorrect values corrupt the selection calculation. See [[sizes Attribute]] and [[Responsive Image Candidate Selection]].

# References

[[highperformanceimages.pdf]]
