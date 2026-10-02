2026-10-02 14:51

Status: #baby

Tags: [[Excel Financial Database and Lookup Functions]]

# Excel Database Counting Functions

Excel DCOUNT counts numeric entries in a chosen database field for records meeting an [[Excel Database Criteria Range]]. DCOUNTA counts nonblank entries instead. DGET retrieves the field value from the single record that matches the criteria.

DGET expects exactly one qualifying record and signals a problem when none or more than one match, making it useful when uniqueness is part of the model. DCOUNT and DCOUNTA differ in the same way as their ordinary counting counterparts, so the field's data type matters. All require a structured database range whose first row contains field names.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
