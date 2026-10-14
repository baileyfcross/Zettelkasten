2026-09-16 00:09

Status: #baby

Tags: [[Data Quality and Missing Data]] · [[R Data Transformation and Reshaping]]

# Factor Level Normalization

Factor level normalization maps inconsistent labels, capitalization, or rare spellings to a deliberate set of categorical values. It prevents semantically identical records from being counted or modeled as separate groups.

The mapping should preserve an audit trail and avoid collapsing distinctions that matter to the analysis.

R factor maintenance also includes adding a legitimate new level before assignment, combining levels that share meaning, and dropping levels left unused after subsetting. These operations change the allowed category set and should be separated from choosing the [[R Factor Reference Level|model reference level]].

# References

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]
