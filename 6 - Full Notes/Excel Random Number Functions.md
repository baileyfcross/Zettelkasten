2026-10-02 14:51

Status: #baby

Tags: [[Excel Mathematical and Conditional Aggregation]] [[Game Probability and Simulation]]

# Excel Random Number Functions

Excel RAND returns a pseudo-random decimal between zero and one, while RANDBETWEEN returns a pseudo-random integer within inclusive lower and upper bounds. They support sampling, simulations, randomized assignments, and test data.

Both functions are volatile, so their results can change whenever the workbook recalculates. A random draw that must become a permanent record should be copied and pasted as values after generation. Randomness also does not guarantee a balanced small sample, unique results, or reproducibility, so additional logic or documentation may be required for those constraints.

For [[Spreadsheet Simulation]], the volatility is useful because recalculation generates another trial. A one-way data table can capture many such trials for summary, while the formula translating random values into outcomes must preserve the intended probability intervals.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]

[[playersmakingdecisions.pdf]]
