2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Independent Quantum Dropout

Independent quantum dropout removes rotation and entangling gates through separate random decisions. After a layer is selected with probability $p_L$, rotation gates use a within-layer ratio $p_R$ and entanglers use $p_E$, giving effective probabilities $p_Lp_R$ and $p_Lp_E$ for the two operation types.

Separating the probabilities lets training disturb parameterized transformations and quantum connections at different rates instead of forcing them into one gate group. This matters because circuit architectures assign different roles and parameterizations to their entanglers; the regression circuit studied in the paper uses fixed CNOTs, whereas its classification circuit uses parameterized controlled rotations.

Independent dropout had the best average test performance among the evaluated strategies on the noisy sine, noisy absolute-value, and Moons tasks. That empirical ranking comes from small noiseless simulations rather than quantum hardware, but it suggests that separately tuning the two operation classes can be more useful than applying only [[Single-Gate Quantum Dropout]] or a fixed canonical grouping.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
