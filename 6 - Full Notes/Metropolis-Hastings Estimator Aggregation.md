2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Model Selection]]

# Metropolis-Hastings Estimator Aggregation

Metropolis-Hastings estimator aggregation approximates a Gibbs-weighted estimator by sampling models from a Markov chain whose stationary distribution is the desired model-weight distribution. Averaging the visited estimators avoids calculating the intractable normalizing sum over every model.

Local proposals can add or remove one variable, making each transition inexpensive. The method is a stochastic analogue of [[Forward-Backward Model Search]], but it averages rather than chooses the best visited model. Its limitation is finite-time uncertainty: asymptotic convergence does not guarantee that the important weights have been estimated accurately within a practical run.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
