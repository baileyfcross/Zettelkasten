2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Scripting Environment]] · [[Blender Embedded Python Internals]]

# Blender Python Script Execution

Running a script from Blender's Text Editor executes its statements in sequence and writes changes into the current scene. The 3D Viewport reflects the resulting data after the script yields control, so a computational loop may finish before all of its visible consequences appear.

Execution context matters. A development guard such as `if __name__ == "__main__"` can trigger setup when a file is run directly, whereas an installed add-on is activated through its registration functions. Recognizing these entry paths prevents development-only behavior from being mistaken for the add-on lifecycle.

Inside Blender's core, file and Text-datablock execution enter through the [[Blender Python Execution API]]. Source that has not already been compiled becomes cached bytecode through the [[Blender Python Script Compilation Cache]], then CPython evaluates it within the application's embedded interpreter and current context.

# References

[[blenderpythonapi.pdf]]

[[coreblenderdevelopment.pdf]]
