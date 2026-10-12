2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Ingress Controller

An ingress controller is the running component that watches Ingress and related resources and configures a reverse proxy or load balancer to implement their routes. It terminates or passes through connections and forwards accepted requests to Kubernetes Services.

The controller is part of the application's availability and security boundary. Its exposed address, replicas, certificate handling, class selection, default backend, non-HTTP capabilities, and upgrade process need explicit ownership rather than being treated as incidental plumbing.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

