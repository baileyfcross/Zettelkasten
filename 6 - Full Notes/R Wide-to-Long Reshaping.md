2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Wide-to-Long Reshaping

R wide-to-long reshaping converts repeated measurements stored in separate columns into multiple rows with identifier, occasion, and value fields. The reverse operation spreads occasion values back across columns and therefore requires the identifier-occasion pairs to determine cells unambiguously.

Long form often makes grouping, plotting, and repeated-measure modeling easier, while wide form can suit reporting or algorithms that expect one row per subject. A reshape specification must distinguish identifier variables from the columns whose names encode measurement conditions.

# References

[[rprimer.pdf]]
