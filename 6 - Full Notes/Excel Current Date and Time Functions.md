2026-10-02 14:51

Status: #baby

Tags: [[Excel Logical Text and Date Functions]]

# Excel Current Date and Time Functions

Excel TODAY returns the current date, while NOW returns the current date and time. Both produce numeric [[Excel Date and Time Serial Value]] results and recalculate with the workbook, so they represent the present at calculation time rather than a permanently recorded timestamp.

These functions support age, deadline, and elapsed-time formulas, but their volatility means results can change when the file is opened on another day. A business process that needs an immutable event date should store a fixed value instead. Formatting determines which portions of NOW are visible, but the underlying result still includes both date and fractional time.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
