2026-09-18 17:13

Status: #baby

Tags: [[Game User Interface Programming]]

# Game UI Coordinate Conversion

Game UI coordinate conversion maps positions between a reference interface layout and the actual screen resolution. Scaling and offset rules preserve intended placement across displays with different dimensions and aspect ratios.

The conversion should distinguish absolute pixel artwork from elements that anchor to edges, centers, or safe regions. Pointer input must use the inverse mapping so visual and interactive bounds continue to agree.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
