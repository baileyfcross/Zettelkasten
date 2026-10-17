2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Oversampled F1 Evaluation for Fraud Detection

The fraud benchmark evaluates anomaly detection with the F1 score, the harmonic mean of precision and recall. To make repeated evaluation computationally manageable on a dataset with only 0.172 percent fraud, it oversamples fraudulent transactions until they form one quarter of the evaluation sample.

Changing class prevalence changes precision and therefore changes F1. Under the benchmark mixture, a classifier that labels every transaction as fraud has precision $1/4$, recall $1$, and F1 $0.4$; a useful model should exceed that reference. Applying the same mixture to quantum and classical AnoGAN permits an internal comparison, but the absolute F1 value does not directly predict performance at the real fraud rate.

The anomaly threshold is selected to optimize F1 using labeled fraudulent and nonfraudulent examples while the trained GAN remains fixed. Thus the generator is trained without anomaly labels, but the final operating point is label-informed. A deployment would need threshold calibration that reflects its real class prevalence and false-positive cost.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
