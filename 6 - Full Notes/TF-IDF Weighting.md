2026-09-16 01:05

Status: #baby

Tags: [[Text Feature Representation]]

# TF-IDF Weighting

TF-IDF weighting combines a term's frequency within a document with an inverse measure of how many documents contain it. Repeated terms gain weight as evidence about one document, while terms appearing throughout the collection are discounted because they discriminate poorly.

The weighted vector improves dot-product or cosine-style similarity over raw counts in many information-retrieval and text-learning tasks. Variants also normalize for document length and dampen the effect of very large term counts.

Operationally, the vocabulary and inverse-document frequencies are fitted on training documents, then the same transformation is applied to test documents. Recomputing them on the test set would change the feature space and leak information from evaluation data into the model.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]

[[textminingandvisualization.pdf]]
