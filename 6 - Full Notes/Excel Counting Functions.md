2026-10-02 14:51

Status: #baby

Tags: [[Excel Statistical and Forecast Functions]]

# Excel Counting Functions

Excel COUNT counts cells containing numbers, COUNTA counts nonempty cells, and COUNTBLANK counts empty cells. They answer different questions about a range: how many numeric observations exist, how many entries of any kind exist, and how many positions contain no value.

Choosing the wrong counting function can distort rates and completeness checks. Dates and times count as numbers because Excel stores them numerically, while labels contribute to COUNTA but not COUNT. Formulas returning an empty-looking string may not behave like truly blank cells, so data-cleaning and audit formulas should test the workbook's actual inputs.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
