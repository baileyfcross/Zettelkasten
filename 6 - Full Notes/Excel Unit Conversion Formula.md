2026-10-02 14:51

Status: #baby

Tags: [[Excel Formula Foundations]]

# Excel Unit Conversion Formula

An Excel unit conversion formula multiplies or divides a measurement by a conversion factor. Placing that factor in its own labeled cell makes the assumption visible and allows many values to use the same rate. The factor is normally anchored with an absolute reference while the measurement reference changes from row to row.

The direction of the factor matters: a formula converting from source units to target units must use a ratio whose source units cancel. Labels should accompany both input and result columns because a numerically correct value without its unit is ambiguous. Centralizing the factor also makes later corrections propagate through the model.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
