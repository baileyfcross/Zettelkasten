2026-10-02 14:51

Status: #baby

Tags: [[Excel Logical Text and Date Functions]]

# Excel Text Search Functions

Excel SEARCH and FIND functions return the starting position of one text fragment within another. SEARCH is case-insensitive and supports wildcard matching, while FIND is case-sensitive and treats the search more literally. Both return an error when the fragment is absent.

The returned position can drive [[Excel Text Extraction Functions]] or replacement formulas. Choosing between SEARCH and FIND depends on whether capitalization and wildcard behavior are part of the data's meaning. When absence is an expected possibility, [[Excel IFERROR Function]] can convert the no-match error into a deliberate outcome rather than leaving the worksheet unexplained.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
