2026-09-22 23:04

Status: #baby

Tags: [[Xamarin Application Architecture]]

# Event Aggregator Pattern

An event aggregator receives categorized messages from publishers and forwards them to interested subscribers. Publishers and subscribers do not need direct references to one another, so interface components can react to application events without introducing a web of point-to-point dependencies.

Xamarin.Forms provides `MessagingCenter` as one implementation of this publisher-subscriber arrangement. Message names, payload meanings, subscription lifetime, and unsubscription still need deliberate management because the aggregator hides the direct call path.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
