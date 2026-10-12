2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Dataset Merge

An R dataset merge combines rows from two data frames by matching one or more key columns. Inner and outer forms determine whether unmatched keys are discarded or retained, and duplicate keys can multiply rows because every matching combination is represented.

Before merging, the analyst should verify key uniqueness, type compatibility, and missing-key behavior. Row binding and column binding are simpler positional operations; a key-based merge is safer when the two tables may not share the same order.

# References

[[rprimer.pdf]]
