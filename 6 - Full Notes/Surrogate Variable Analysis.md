2026-09-14 20:21

Status: #baby

Tags: [[Batch Effects and Latent Factor Adjustment]]

# Surrogate Variable Analysis

Surrogate variable analysis estimates latent sources of unwanted variation while protecting the modeled outcome of interest. It iteratively weights features according to whether they are associated with hidden structure but not with the biological contrast, then estimates surrogate factors from the weighted data.

The resulting variables enter the model beside the biological predictor. This outcome-aware construction reduces the risk of deleting the target signal when batch labels are incomplete or unknown.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
