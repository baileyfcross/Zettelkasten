2026-09-15 09:29

Status: #baby

Tags: [[Data Science Deployment and Renewal]]

# Model Renewal Trigger

A model renewal trigger is an agreed condition for revisiting a production model. Depending on the project, it may be a periodic review or a detected change in input distributions, outcomes, or predictive performance. Different domains require different refresh intervals.

Building the check into deployment prevents a model from quietly becoming stale. Renewal can involve new data, revised attributes, a changed target definition, or a different algorithm; simply rerunning the original training procedure is not always enough if the business problem itself has shifted.

# References

[[datascience_mit.epub]]
