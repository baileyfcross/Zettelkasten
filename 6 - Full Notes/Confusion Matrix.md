2026-09-06 22:09

Status: #baby

Tags: [[Social Content Popularity Prediction]] · [[Classification Evaluation and Visualization]]

# Confusion Matrix

A confusion matrix counts how often each actual class is assigned to each predicted class. For a chosen positive class, its cells yield true positives, false positives, false negatives, and true negatives.

Those counts support accuracy, precision, recall, specificity, and F-measure. Inspecting the matrix is especially important when one class is rare because a high overall accuracy can conceal failure to identify that class.

The book derives held-out counts from predicted and observed classes, then uses them to interpret precision, recall, and the F-measure. Keeping the chosen positive class explicit prevents the same table from being read in contradictory ways.

For sentiment models, the matrix also makes the asymmetry between positive and negative errors visible. This matters when class frequencies differ or when a lexicon returns a neutral outcome for messages it does not cover.

# References

[[bigdataincomplexandsocialnetworks.pdf]]

[[essentialsofdatascience.pdf]]

[[textminingandvisualization.pdf]]
