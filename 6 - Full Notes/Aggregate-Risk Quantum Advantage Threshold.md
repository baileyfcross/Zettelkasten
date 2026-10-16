2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Aggregate-Risk Quantum Advantage Threshold

Applying a pricing oracle inside a higher-level risk calculation can change the practical threshold for quantum advantage because one coherent computation replaces many repeated classical prices. The paper benchmarks QSP VaR for an autocallable whose pricing oracle has T-depth 3,900 and whose classical price takes one second at error $2\times10^{-3}$.

For 50,000 sampled scenarios, the simulation finds that the risk calculation can beat the previously estimated single-derivative threshold while scenario preparation remains below roughly $8\times10^7$ T-depth. If preparation is below roughly $3\times10^5$ T-depth, the required logical T-gate clock rate is reduced by as much as about 30 times relative to the 45 MHz single-price estimate. These figures assume the chosen contract, normal scenario-price model, error matching, fault-tolerant gate costs, and efficient state preparation; they are conditions for advantage, not a hardware demonstration.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
