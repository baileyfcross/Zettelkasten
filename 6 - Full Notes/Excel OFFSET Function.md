2026-10-02 14:51

Status: #baby

Tags: [[Excel Financial Database and Lookup Functions]]

# Excel OFFSET Function

The Excel OFFSET function returns a reference displaced by a specified number of rows and columns from a starting reference. Optional height and width arguments let it return a resized range rather than a single cell.

OFFSET can create rolling windows, dynamic ranges, and references controlled by other calculations. Its result is a reference, so aggregation functions can operate directly on the returned range. The flexibility also obscures dependencies and may increase recalculation cost; boundaries must be checked so the displacement does not produce an invalid reference or include unintended cells.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
