2026-10-02 14:51

Status: #baby

Tags: [[Excel Formula Analysis and Automation]]

# Excel Conditional Formatting Duplicate Detection

Excel can detect duplicates with a formula-based conditional formatting rule that counts how often the current value appears in the full comparison range. A count greater than one marks every repeated occurrence rather than only the later copy.

The comparison range should be absolute while the tested cell remains relative as the rule moves through the selection. Blank cells may need an additional condition so empty positions are not highlighted as duplicates. The rule is a visual audit, not a uniqueness constraint; [[Spreadsheet Data Validation Rule]] is needed when duplicate entry must be actively rejected.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
