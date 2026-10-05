2026-09-06 18:44

Status: #baby

Tags: [[Health Data Visualization]] · [[R Statistical Graphics and Export]]

# Histogram

A histogram displays the distribution of a continuous variable by dividing its range into intervals and drawing a bar for the frequency or proportion in each interval. It reveals concentration, skewness, gaps, and possible outliers.

The choice of breaks can change the apparent shape, so it should be explored rather than treated as neutral. Axis limits and labels should reflect the valid measurement range, especially after special missing codes have been removed.

R can return the breakpoints and bin counts as well as draw the histogram, making the grouping rule inspectable. Frequency and density scales answer different questions; the density scale is required when a fitted distribution or kernel curve is overlaid for comparison.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[rprimer.pdf]]
