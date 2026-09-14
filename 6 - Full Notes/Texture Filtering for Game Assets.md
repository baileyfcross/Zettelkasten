2026-09-14 01:18

Status: #baby

Tags: [[Low-Poly Game Environment Art]]

# Texture Filtering for Game Assets

Texture filtering determines how stored texels contribute to pixels when a texture is enlarged, reduced, or viewed at an angle. Bilinear filtering samples nearby texels, trilinear filtering blends between mip levels, and anisotropic filtering improves oblique surfaces such as ground planes.

Filtering trades additional sampling work for smoother and more stable image quality. The appropriate settings depend on target hardware and camera behavior, while [[Mipmap Chains for Distant Assets|mipmaps]] provide the prefiltered levels needed for efficient minification.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

