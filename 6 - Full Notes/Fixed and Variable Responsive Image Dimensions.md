2026-09-28 04:01

Status: #baby

Tags: [[Responsive Image Selection]]

# Fixed and Variable Responsive Image Dimensions

A fixed-dimension image occupies a known CSS width, so responsive selection mainly needs to account for device pixel density. A variable-dimension image changes with viewport or layout, so the browser must also estimate the rendered width.

These cases require different candidate descriptions. Density descriptors suit a stable slot, while width descriptors plus a `sizes` expression describe a fluid slot. Treating every image as one case can cause unnecessary bytes or visible undersampling. See [[srcset Density Descriptor]] and [[srcset Width Descriptor]].

# References

[[highperformanceimages.pdf]]
