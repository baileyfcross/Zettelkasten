2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Java Package Namespace

A Java package groups related types under a qualified namespace. The package declaration appears before imports and type declarations, and its dot-separated name conventionally corresponds to nested source directories. A reverse-domain prefix helps independent organizations avoid naming collisions.

Packages provide organization and an access boundary, but they are not independently deployable units. Imports only shorten references to accessible types; they do not copy code or bypass [[Java Access Control Levels]]. Modules can group several packages and make only selected packages visible outside that larger unit.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
