2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Shader Program Linking

Shader program linking combines separately compiled shader stages into one executable GPU program. The linker verifies that stage interfaces agree, such as a vertex shader output matching a fragment shader input.

After a successful link, the engine can query attribute and uniform locations and bind the program for drawing. Compile and link logs must be checked because a created object can still contain invalid source or incompatible stages.

# References

[[gameprogrammingincplusplus.pdf]]
