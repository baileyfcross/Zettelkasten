2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Autocallable Payoff Logic with QSP

An autocallable combines early binary coupons with a path-dependent terminal payoff. For each observation time, a comparison qubit records whether the return crosses its call threshold and no earlier coupon has triggered. A separate barrier register records whether the asset crossed a barrier during the path while all early-call indicators remained false.

These conditions use CNOT and Toffoli logic on log-return registers. Known binary coupon amounts are encoded with controlled rotations, while QSP handles the terminal clause by transforming the final shifted log-return directly into the required payoff amplitude.

The method eliminates repeated exponentiation of asset-price registers but retains probability preparation and Boolean payoff conditions. Multi-asset BestOf and WorstOf variants can first compare relative performance and then apply the same terminal transformation to the selected asset, although general multivariate payoffs remain subject to [[Single-Variable QSP Limitation]].

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
