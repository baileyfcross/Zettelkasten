2026-10-02 14:51

Status: #baby

Tags: [[Excel Financial Database and Lookup Functions]]

# Excel Interest Rate Function

The Excel RATE function estimates the periodic interest rate that makes a series of payments, a present value, and an optional future value financially consistent. It solves iteratively rather than by a simple direct arithmetic expression and can accept a starting guess.

The returned rate corresponds to the period used for payments and the period count, so it must be converted carefully before being described as annual or monthly. Cash-flow signs must represent opposing directions. Because iterative solutions may fail or converge unexpectedly for inconsistent inputs, the result should be checked by placing it back into the related present-value or payment model.

# References

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
