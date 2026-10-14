2026-10-02 14:51

Status: #baby

Tags: [[Excel Statistical and Forecast Functions]]

# Excel Conditional Extrema Functions

Excel MINIFS returns the smallest value whose record satisfies specified criteria, and MAXIFS returns the largest. A target range supplies the values to compare, while one or more paired criteria ranges and criteria determine which rows participate.

The target and criteria ranges must align so each criterion is evaluated against the correct record. Multiple criteria act together, narrowing the eligible set in the manner of [[Excel AND Function]]. Conditional extrema avoid helper columns for common filtered summaries, but a workbook should still handle the case in which no record matches and distinguish that absence from a genuine zero.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
