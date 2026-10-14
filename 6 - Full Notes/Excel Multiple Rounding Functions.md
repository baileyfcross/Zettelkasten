2026-10-02 14:51

Status: #baby

Tags: [[Excel Mathematical and Conditional Aggregation]]

# Excel Multiple Rounding Functions

Excel MROUND rounds a number to the nearest chosen multiple. CEILING rounds toward the next permitted multiple in its defined direction, while FLOOR rounds toward the preceding one. These functions support packaging quantities, billing increments, price steps, and time intervals that do not align with ordinary decimal places.

Times are fractions of a day, so rounding them to minutes or hours requires a multiple expressed in compatible time units. The required direction matters: capacity planning may need an upward result while conservative availability may need a downward one. Sign behavior and function variants can differ by Excel version, so boundary cases should be tested.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
