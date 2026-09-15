2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Object Model]]

# Mutable Algorithm Working State

Mutable state permits selected data members to change inside a const member function. ClusLib uses it for results and intermediate memberships because a clustering computation updates its output while treating its configured parameters as logically fixed.

The keyword should mark a deliberate distinction between configuration and computed state, not bypass const discipline generally. Reset behavior must clear every mutable artifact that could contaminate a later run.

# References

[[dataclusteringincplusplus.pdf]]

