2026-09-21 00:45

Status: #baby

Tags: [[CAD and FEM Geometry Exchange]]

# Native CAD Kernel Interoperability

Native CAD kernel interoperability lets two applications interpret geometry through the same underlying boundary-representation engine. Sharing a kernel can preserve richer surfaces, topology, and feature behavior than conversion through a simpler interchange format.

Kernel compatibility does not guarantee analysis readiness. The receiving FEM tool still applies its own tolerance, domain, and meshing requirements, and optional interface modules may be required to access the native representation.

# References

[[geometrycreationandimport.pdf]]
