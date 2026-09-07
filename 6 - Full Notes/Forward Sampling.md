2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]]

# Forward Sampling

Forward sampling draws root variables first and then samples dependent variables in an order consistent with a model's decomposition. Each new value is conditioned on the already sampled values of its parents.

The procedure directly simulates the joint distribution described by the Bayesian program. It is simple, but rare evidence may be poorly represented when the desired query conditions on unlikely observations.

# References

[[bayesianprogramming.pdf]]
