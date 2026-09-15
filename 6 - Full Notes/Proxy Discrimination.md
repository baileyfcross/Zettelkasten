2026-09-05 23:09

Status: #baby

Tags: [[Algorithmic Fairness and Justice]]

# Proxy Discrimination

Proxy discrimination occurs when a model does not use a protected characteristic directly but relies on another variable that closely tracks it. Location, purchasing behavior, language, or social connections can reproduce distinctions associated with race, gender, class, or another protected group.

Removing the explicit characteristic therefore does not guarantee fairness. It may make discrimination harder to detect while leaving the underlying relationship intact. Evaluation should compare outcomes across groups, inspect correlated features, and ask whether each variable has a legitimate connection to the decision. The problem shows the limits of [[Fairness Through Unawareness]].

The book poses a practical dilemma in which several interacting fields collectively act as a proxy for race. Excluding the race field while keeping those proxies can improve a model's measured performance precisely because historic discrimination is present in the data. The model objective must therefore be tested against the social consequences of its predictions, not just predictive accuracy.

# References

[[aiethics.epub]]

[[datascience_mit.epub]]
