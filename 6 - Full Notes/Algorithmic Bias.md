2026-09-05 23:09

Status: #baby

Tags: [[Algorithmic Fairness and Justice]]

# Algorithmic Bias

Algorithmic bias is a systematic tendency for an automated system to produce distorted or unequally harmful outcomes. Bias can enter through the population sampled, labels, variables, model objective, deployment data, or the way people interpret and act on the output.

The source is not always a prejudiced programmer. A model trained on historical practice may accurately reproduce an unjust pattern, and an apparently neutral variable may act as a social proxy. Because bias can emerge throughout the [[Data Science Pipeline]], mitigation requires technical testing together with judgment about which differences are ethically relevant.

Sampling creates another route: a face dataset with fewer examples from some populations gives the learner less evidence and less incentive to correct those groups' errors. Training data should match the distribution and conditions of real use, while evaluation should report subgroup behavior. Recommendation systems also need deliberate diversity so optimizing past preference does not trap a person inside an ever-narrower history.

# References

[[aiethics.epub]]

[[machinelearning_mit.epub]]
