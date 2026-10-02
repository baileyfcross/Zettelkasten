2026-10-02 14:51

Status: #baby

Tags: [[Excel Formula Foundations]]

# Excel Relative Cell Reference

An Excel relative cell reference changes in relation to the destination when a formula is copied or filled. If a formula in row 2 refers to `A2`, copying it down one row changes the reference to `A3`. The formula preserves a spatial relationship rather than a fixed address.

Relative references are appropriate when each row or column should perform the same calculation on its own inputs. Their convenience also creates risk: a copied formula can silently point to the wrong place if a rate, threshold, or other constant was supposed to remain fixed. Those inputs require an [[Excel Absolute and Mixed Cell Reference]].

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
