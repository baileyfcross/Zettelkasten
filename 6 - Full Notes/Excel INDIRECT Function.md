2026-10-02 14:51

Status: #baby

Tags: [[Excel Financial Database and Lookup Functions]]

# Excel INDIRECT Function

The Excel INDIRECT function converts text into a cell or range reference. A formula can assemble an address from labels, worksheet names, or user selections and then retrieve the value at the resulting location. This enables references whose destination is chosen at calculation time.

Because the dependency is hidden inside text, INDIRECT formulas are harder to trace than ordinary references and can break when names or sheet labels change. External-workbook behavior also has limitations. The function is best reserved for genuinely dynamic reference selection, with the constructed text made visible during testing so malformed addresses can be diagnosed.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
