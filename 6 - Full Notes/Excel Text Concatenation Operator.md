2026-10-02 14:51

Status: #baby

Tags: [[Excel Formula Foundations]]

# Excel Text Concatenation Operator

The Excel concatenation operator `&` joins text, cell values, and literal strings into one result. Literal spaces and punctuation must be included inside quotation marks, because Excel does not insert separators automatically. Concatenation can build names, labels, messages, or identifiers from distributed fields.

When a referenced number, date, or time needs a particular appearance inside the result, the TEXT function should convert it using an explicit number format. Otherwise, concatenation may expose the underlying serial value rather than the displayed form. For joining entire ranges with a consistent delimiter, [[Excel Text Joining Functions]] provides more scalable options.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
