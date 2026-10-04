2026-09-17 09:48

Status: #baby

Tags: [[Recommender System Evolution]]

# Content-Based Recommendation

Content-based recommendation suggests items whose features resemble items a user liked in the past. Similarity is calculated from item attributes, such as terms in a document or other descriptive properties.

The method can operate without preferences from other users, but it is limited by the quality of the item representation and may repeatedly recommend things too similar to what is already known.

An item profile encodes descriptive features, while a user profile weights those same features according to the items the user preferred. Comparing the two profiles turns attributes such as genre, author, or acoustic properties into candidate scores. This dependence on declared features makes representation quality as important as the similarity calculation itself.

# References

[[frontiersofdatascience.pdf]]

[[recommendationengines.epub]]
