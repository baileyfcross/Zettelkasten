2026-09-16 00:09

Status: #baby

Tags: [[Exploratory Data Visualization in R]] · [[R Statistical Graphics and Export]]

# Plot Export Device

A plot export device writes an R graphic to a file format such as PNG, PDF, or SVG with specified dimensions and resolution. Explicit export settings make the result more reproducible than manually copying a display pane.

The chosen device should suit its destination: raster output for pixel-based use and vector output for scalable lines and text.

The primer makes the device lifecycle explicit: open the file device with its dimensions and format options, issue the plotting commands, and close the device so the file is finalized. Replaying the plotting code inside that device makes export reproducible and avoids dependence on the size of an interactive window.

# References

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]
