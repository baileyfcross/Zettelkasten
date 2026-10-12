2026-10-12 01:03

Status: #baby

Tags: [[Unity Object Architecture and Scripting]]

# Unity Script Component Attachment

A Unity C# script becomes active scene behavior when it is attached to a [[Unity GameObject]] as a component. A MonoBehaviour-derived class can then expose serialized fields in the [[Unity Inspector]] and receive engine callbacks such as those described by [[Unity Lifecycle Methods]].

The script file is an asset, while each attached component is an instance with its own field values. This allows one implementation to control many objects differently. The script name and class name must agree so Unity can recognize and attach the component reliably.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

