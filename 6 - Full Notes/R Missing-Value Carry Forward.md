2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Missing-Value Carry Forward

R missing-value carry forward replaces each missing entry with the most recent preceding observed value. It is appropriate only when row order has a real meaning and the prior observation is a defensible state for the current position, such as a value recorded once for a run of subsequent rows.

Leading missing values remain unresolved because no earlier value exists. The method should not be treated as a neutral imputation rule: sorting errors or unjustified persistence assumptions can propagate an incorrect value through many observations.

# References

[[rprimer.pdf]]
