2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Tag and Layer

Unity tags and layers classify GameObjects for different runtime purposes. A tag gives an object a named identity used by gameplay queries, while a layer places it into a bit-addressable group used by systems such as rendering and physics filtering.

They should not be treated as interchangeable labels. Tags answer questions such as what kind of object was contacted; layers answer which groups should interact or be visible to a camera. Central configuration and stable names keep these classifications from becoming hidden coupling across scenes and scripts.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

