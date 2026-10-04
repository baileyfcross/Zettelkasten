2026-09-13 10:20

Status: #baby

Tags: [[Association Rule Discovery]]

# Association Rule

An association rule is an implication from one itemset to another, written as an antecedent leading to a consequent. It summarizes how often the sets occur together in transaction data.

Support measures prevalence and confidence measures conditional co-occurrence. The rule is an observed association and does not by itself show causation.

In recommendation, a rule such as “people who buy X also tend to buy Y” identifies customers who have X but not Y as candidates. Pairwise and small-itemset rules can be efficient on transaction data, but a [[Generative Model]] with latent factors may explain many related purchases more compactly than a large collection of product-to-product implications.

Association analysis can summarize products held by the same customer across time, while market-basket analysis focuses on items appearing in the same transaction. Both support inexpensive co-occurrence recommendations, but their purchase-centered evidence says more about what sells together than about whether the customer will value the suggestion.

# References

[[clusteranalysisanddatamining.pdf]]

[[machinelearning_mit.epub]]

[[recommendationengines.epub]]
