2026-09-13 10:20

Status: #baby

Tags: [[Association Rule Discovery]]

# Apriori Algorithm

Apriori discovers frequent itemsets level by level. It finds frequent one-item sets, joins the frequent sets of length k minus one to form length-k candidates, scans the transactions for support, and repeats until no candidates qualify.

The algorithm relies on downward closure to prune any candidate containing an infrequent subset before expensive counting.

# References

[[clusteranalysisanddatamining.pdf]]
