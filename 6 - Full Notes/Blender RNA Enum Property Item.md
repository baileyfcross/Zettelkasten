2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA Enum Property Item

An RNA enum property item describes one choice through an internal integer value, a unique identifier, an optional icon, a user-facing name, and a longer description. Arrays of these records define the options shared by the RNA, interface, and Python APIs.

Empty identifiers can represent menu separators, while a null identifier terminates the array. As part of a [[Blender RNA Typed Property]], the item list separates stable program values from the labels and explanations shown to users.

# References

[[coreblenderdevelopment.pdf]]

