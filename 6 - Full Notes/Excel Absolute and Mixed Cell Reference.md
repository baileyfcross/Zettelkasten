2026-10-02 14:51

Status: #baby

Tags: [[Excel Formula Foundations]]

# Excel Absolute and Mixed Cell Reference

An absolute Excel reference places dollar signs before both the column and row, as in `$B$1`, so copying a formula does not move that reference. A mixed reference anchors only one dimension: `$B1` fixes the column, while `B$1` fixes the row. The F4 key cycles through these forms while editing a reference.

Anchoring is essential when many calculations share one tax rate, conversion factor, or lookup boundary. Mixed references are especially useful in two-dimensional calculation tables because a formula can follow row inputs in one direction and column inputs in the other. The anchor should express the intended copying behavior, not merely repair a single result.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
