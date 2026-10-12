2026-09-22 23:04

Status: #baby

Tags: [[Xamarin Application Architecture]]

# Xamarin Shared Project

A Xamarin shared project is a collection of source files linked into each consuming platform project. Its code is compiled as part of every target rather than emitted as an independent assembly, allowing conditional compilation to vary behavior by platform.

This flexibility also weakens isolation: the shared project cannot be tested as a standalone library and may compile differently under each target. A .NET Standard library provides a firmer reusable boundary when conditional source inclusion is unnecessary.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
