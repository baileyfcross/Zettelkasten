2026-10-07 17:18

Status: #baby

Tags: [[R Programming Environment]]

# R Native Code Interface

The R native code interface lets an R session call compiled C or C++ routines from a dynamically loaded shared library. The source is compiled into a platform library, loaded with dyn.load, and checked before an R wrapper invokes its exported routine.

The .C interface passes atomic data in a C-compatible form and returns modified arguments to R. The boundary requires compatible symbol names, types, dimensions, and memory expectations; it is useful when a computational kernel is better expressed or executed in compiled code while R retains orchestration and analysis.

# References

[[statisticalcomputingincplusplusandr.pdf]]
