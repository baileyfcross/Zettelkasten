2026-10-01 00:39

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# OpenGL Mouse and Keyboard Callbacks

GLUT connects an OpenGL application to user input by registering callback functions. A mouse callback receives the button, press or release state, and pixel coordinates. A motion callback receives updated pointer coordinates, while a keyboard callback receives the key and the pointer location associated with the event.

The utility toolkit invokes these functions from its event loop when the corresponding event occurs. Drawing code can therefore remain separate from interaction logic: callbacks update application state or request a redraw, and the display callback renders the resulting state through OpenGL.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
