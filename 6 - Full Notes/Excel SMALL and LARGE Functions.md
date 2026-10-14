2026-10-02 14:51

Status: #baby

Tags: [[Excel Statistical and Forecast Functions]]

# Excel SMALL and LARGE Functions

Excel SMALL returns the kth smallest numeric value in a dataset, and LARGE returns the kth largest. Setting k to one reproduces the minimum or maximum; larger ranks retrieve values farther from the endpoint. These functions support top-N and bottom-N analysis without sorting the source range.

The rank argument refers to a position among values, so ties can produce repeated results. The source range and k should be validated because a rank outside the number of available numeric values causes an error. When the desired output is a record label rather than the value itself, an additional lookup is needed.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
