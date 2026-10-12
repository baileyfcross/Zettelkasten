2026-10-03 22:06

Status: #baby

Tags: [[Transportation and Transshipment Optimization]]

# MODI Method

The modified distribution, or MODI, method computes row potentials $u_i$ and column potentials $v_j$ from occupied cells using $u_i+v_j=c_{ij}$. It then evaluates each empty cell by comparing its cost with the corresponding potential sum.

These improvement indices identify whether any unused route can lower total cost without drawing a loop for every cell. After selecting an improving cell, only its adjustment loop is needed, making MODI more efficient than the [[Stepping-Stone Method]] on large tables.

# References

[[optimizationusinglinearprogramming.pdf]]

