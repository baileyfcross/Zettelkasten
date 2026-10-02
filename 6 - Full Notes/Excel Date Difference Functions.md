2026-10-02 14:51

Status: #baby

Tags: [[Excel Logical Text and Date Functions]]

# Excel Date Difference Functions

Excel can subtract one date from another to obtain elapsed days, but specialized functions express other conventions. DATEDIF returns differences in chosen units such as years, months, or days. YEARFRAC returns the fraction of a year between dates, and DAYS360 uses a standardized 360-day year for certain financial calculations.

The choice of function is a modeling decision because calendar days, completed calendar units, fractional years, and 360-day conventions are not interchangeable. Start and end dates should be true [[Excel Date and Time Serial Value]] values, and the workbook should state which convention a duration represents so downstream calculations remain interpretable.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
