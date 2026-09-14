2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Module API Boundary

Blender modules distinguish externally callable functions from internal helpers through placement and naming. Public functions are declared in interface headers above an `intern` directory and commonly use an uppercase module prefix such as `WM_`, `BKE_`, `BLI_`, or `BLO_`.

Lowercase functions with the same abbreviation usually remain implementation details inside the module. This boundary lets callers depend on a stable [[Blender Source Module]] interface while its [[Blender Intern Directory Convention]] hides lower-level branching, static helpers, and data-handling steps.

# References

[[coreblenderdevelopment.pdf]]

