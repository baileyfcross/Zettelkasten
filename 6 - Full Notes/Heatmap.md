2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]] · [[R Statistical Graphics and Export]]

# Heatmap

A heatmap represents the entries of a data matrix with color and commonly reorders its rows and columns through clustering. It lets many features and samples be viewed at once so blocks, gradients, outliers, and possible group structure become visible.

Color scale, transformation, feature selection, and clustering distance all affect the pattern. The source cautions that red-green palettes are difficult for many color-blind readers, making accessible encoding part of analytical communication.

The primer's R heat-map workflow can reorder rows and columns by hierarchical clustering and display the associated dendrograms beside the color matrix. Turning clustering off preserves the supplied order, which is preferable when row or column sequence already carries scientific meaning.

For trace and metric analysis, a heatmap can place latency buckets on one axis and time on the other, with color representing frequency. This keeps the distribution visible and can expose a tail, cluster, or time-dependent shift that a single average or percentile line conceals. Bucket boundaries and color scaling remain analytical choices rather than neutral presentation details.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[rprimer.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
