2026-09-28 03:19

Status: #baby

Tags: [[Clinical Prediction and Temporal Analytics]]

# Brier Score for Clinical Prediction

The Brier score measures the mean squared difference between predicted probabilities and observed binary outcomes. It rewards probabilities that are both well calibrated and discriminative, while confident incorrect predictions incur a large penalty.

Because it evaluates probabilities rather than only class labels, it can distinguish two models that make the same thresholded decisions with different confidence. Its value is influenced by outcome prevalence, so comparisons should use the same population and prediction horizon and should be accompanied by measures that expose the model's clinical operating behavior.

# References

[[healthcaredataanalytics.pdf]]
