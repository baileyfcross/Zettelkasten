2026-10-02 14:51

Status: #baby

Tags: [[Excel Formula Foundations]]

# Excel Date and Time Serial Value

Excel stores a date as a serial day number and a time as a fractional part of a day. A value containing both uses the integer portion for the date and the decimal portion for the clock time. This representation lets formulas add durations, subtract timestamps, and compare calendar values numerically.

Formatting determines whether the underlying number appears as a date, a time, or an elapsed duration. A result that looks wrong may therefore have a correct stored value but an unsuitable format. Long elapsed times need a format that does not wrap after twenty-four hours, while text-formatted dates no longer behave like numeric dates in calculations.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
