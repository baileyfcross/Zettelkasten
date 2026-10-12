2026-10-11 12:45

Status: #baby

Tags: [[Search Log and Web Text Mining]]

# Web Crawling and Scraping Separation

Web crawling discovers pages by following links, while web scraping extracts selected content from pages already found. Separating the tasks clarifies whether a failure came from navigation and coverage or from an extraction rule that no longer matches a page.

A collection system may coordinate both: the [[Web Crawler]] maintains a frontier and visited set, and the scraper converts each response into structured records. Independent logs and tests make changes in site structure easier to diagnose.

# References

[[textminingandvisualization.pdf]]
