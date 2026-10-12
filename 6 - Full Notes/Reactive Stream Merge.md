2026-09-21 22:12

Status: #baby

Tags: [[Reactive Programming in .NET]]

# Reactive Stream Merge

Merging reactive streams forms one output sequence from notifications arriving on several input sequences. The book combines two ticket-counter streams so one observer can consume both. The resulting interleaving follows arrival and scheduling rather than a guaranteed sorted order, so a consumer that needs global ordering must establish that separately.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

