2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Module Stacking

Kernel module stacking lets one module consume symbols exported by another module. The provider becomes a dependency of the consumer, so module tools must load them in dependency order and refuse to remove the provider while a dependent user remains.

Stacking can emulate a library-like boundary across separately loadable objects, but it also enlarges lifecycle and ABI coordination. When components always deploy together, linking several source files into one composite module is often simpler than creating a runtime dependency.

# References

[[linuxkernelprogramming_secondedition.pdf]]
