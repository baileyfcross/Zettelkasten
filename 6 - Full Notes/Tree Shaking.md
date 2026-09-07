2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]]

# Tree Shaking

Tree shaking is a build optimization that removes unused code from the final JavaScript bundle. Smaller bundles reduce code transferred to and processed by the browser.

Angular services provided through root-level injectable metadata can participate in this optimization because the build system can determine whether the service is used. Registering code in ways that create unavoidable references can prevent removal.

# References

[[aspnetcore3andangular9_3ed.pdf]]
