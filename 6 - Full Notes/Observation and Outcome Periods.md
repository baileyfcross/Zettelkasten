2026-09-15 09:20

Status: #baby

Tags: [[Data Science Deployment and Renewal]]

# Observation and Outcome Periods

In a propensity model, the observation period supplies the input attributes, while a later outcome period determines whether the predicted event occurred. The interval between them defines how far ahead the prediction is meant to work.

For churn, a model intended to warn two months before departure must train on information that would have been available two months before each historic customer's departure. Using later activity in the inputs would create a misleadingly easy task and leave too little time for an actual retention intervention.

# References

[[datascience_mit.epub]]
