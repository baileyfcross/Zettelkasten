2026-10-11 12:45

Status: #baby

Tags: [[Search Log and Web Text Mining]]

# Fault-Tolerant Web Scraping

Fault-tolerant web scraping records request, authentication, status-code, parsing, and storage failures while allowing the remaining collection to continue. A single malformed or unavailable page should not erase progress across a large crawl.

Logging the URL, failure type, and time supports retries and exposes systematic gaps. Silent exception handling is dangerous because it can turn a biased partial corpus into an apparently successful data set.

# References

[[textminingandvisualization.pdf]]
