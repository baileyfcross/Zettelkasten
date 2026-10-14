2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Selection Connections and Evaluation]]

# Feature Redundancy Rate

A feature redundancy rate summarizes the average pairwise correlation among selected features. A high rate indicates that the subset repeatedly represents similar variation, even if each feature is individually relevant to the target.

Redundancy should be evaluated separately from predictive accuracy or similarity preservation. A selector can preserve the target well while returning many interchangeable variables, and a very low-redundancy subset can still omit important signal. The measure is most informative when interpreted alongside task performance and the requested subset size.

# References

[[spectralfeatureselectionfordatamining.pdf]]

