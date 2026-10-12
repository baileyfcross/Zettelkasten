2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Package Test Structure

An R package test structure places development-time tests in the package's conventional test directories so package tools can discover and execute them automatically. With testthat, test files live under `tests/testthat`, use names beginning with `test-`, and are launched by `tests/testthat.R` through a package-level test check.

The testing framework is declared as a suggested package dependency because it is needed for development and checking rather than ordinary use. Following this structure connects individual [[Unit Test]] files to the broader [[R Package Check]] process and keeps test execution reproducible for maintainers and automated services.

# References

[[testingrcode.pdf]]
