2026-09-28 03:43

Status: #baby

Tags: [[Text and Multimedia Classification]]

# Rocchio Classifier

The Rocchio classifier represents each class by a central vector formed from its training examples. A new instance is assigned to the class whose center has the greatest similarity to the instance.

The small set of class centers makes training and prediction simple, and vector-similarity hardware can accelerate the comparison. Performance depends on whether a single center describes each class well; irregular, multimodal, noisy, or outlier-heavy classes can violate that assumption.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
