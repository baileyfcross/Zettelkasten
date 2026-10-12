# Kubernetes Generative AI Operations

Parent topic: [[Kubernetes Enterprise Operations]]

Kubernetes Generative AI Operations is the chapter-level topic for adapting, deploying, scaling, securing, accelerating, observing, and recovering generative-AI applications on Kubernetes. Full Notes should link to a focused child topic rather than directly to this chapter tag.

## Overview Chapter

Generative-AI systems combine an ordinary distributed application with unusually large artifacts, accelerator-dependent computation, probabilistic output, and a feedback loop between production behavior and model adaptation. Kubernetes supplies a common control plane for those pieces, but useful orchestration depends on understanding where model concerns differ from conventional stateless services. Training jobs are finite and often bursty; inference endpoints are long-running and sensitive to latency; retrieval services depend on data freshness and vector search; and GPU memory can be more restrictive and expensive than CPU capacity. A production design must connect the model lifecycle to scheduling, security, cost, telemetry, and recovery rather than treating deployment as the final step.

### Adapt the model to a measurable use case

[[Generative AI Model Adaptation and Serving]] begins with a business objective and measurable criteria such as cost per inference, response latency, throughput, answer quality, and expected business value. Most teams select an existing foundation model and adapt it instead of training one from the beginning. Parameter-efficient fine-tuning methods such as LoRA update a compact low-rank representation, while QLoRA combines that approach with quantized weights to reduce memory demand. Prompt tuning changes learned prompt tokens, and direct preference optimization learns from preferred and rejected answer pairs without constructing a separate reinforcement-learning loop.

Retrieval-augmented generation addresses a different problem. Documents and queries are embedded into a vector space, an index retrieves semantically similar context, and the retrieved material is included in the answer prompt. A conversational pipeline may first rewrite the current input using chat history, retrieve evidence for that contextualized question, then ask the model to answer from the evidence and conversation. RAG can supply current or private knowledge without changing model weights, while fine-tuning changes model behavior. Both approaches still require evaluation. Compression techniques such as quantization, distillation, and pruning trade some fidelity or flexibility for lower memory, latency, and cost, so deployment optimization must be checked against task-specific acceptance criteria.

### Turn artifacts into a Kubernetes application

[[Kubernetes GenAI Deployment Architecture]] maps the model system onto infrastructure, orchestration, and application layers. Compute may include CPUs, GPUs, or specialized accelerators; storage holds training data, model weights, notebooks, and vector indexes; and high-throughput networking connects distributed workers and services. Containers make code and dependencies reproducible, while Kubernetes separates short-lived fine-tuning Jobs from replicated inference Deployments and supporting web, retrieval, and data services.

An end-to-end chatbot illustrates the composition. A user interface selects between a fine-tuned model endpoint and a RAG service. The RAG path calls an embedding or language-model API and a vector store; the fine-tuned path loads model assets produced by a training job and stored in durable object storage or an image registry. JupyterHub gives experimenters isolated notebook pods, but notebooks, data, parameters, and output artifacts need versioned storage if an experiment is to become a repeatable pipeline. Infrastructure as code makes the EKS cluster, node groups, identities, add-ons, and application prerequisites reconstructable rather than leaving the environment dependent on manual console history.

### Scale useful work and expose its cost

[[Kubernetes GenAI Autoscaling and Cost Control]] connects scaling to the resource that actually limits service. HPA changes replica count from conventional or custom metrics. VPA recommends or changes pod requests, but automatic VPA changes can interfere with utilization-based HPA because the denominator used by HPA moves when requests are rewritten. KEDA translates events such as queue depth, request rate, or Prometheus GPU utilization into an HPA-managed replica target and can scale an inactive consumer to zero.

Pod scaling and node scaling form a handoff. When new replicas cannot be scheduled, Cluster Autoscaler adds capacity from predefined node groups. Karpenter instead evaluates pending-pod constraints, selects fitting instance types, creates just-in-time nodes, and consolidates empty or replaceable capacity. Separate NodePools can express GPU and ordinary compute constraints, but overlapping pools make placement ambiguous. Kubecost attributes CPU, GPU, memory, storage, network, and shared platform cost to workload boundaries, while right-sizing tools compare observed use with requests. Cost optimization therefore joins measurement, requests, scheduling, storage lifecycle, network locality, and service objectives; simply choosing a cheaper node can make inference slower or unavailable.

### Protect data, artifacts, and model endpoints

[[Kubernetes GenAI Network and Endpoint Security]] treats the user data, configuration, application code, dependencies, images, runtime, and host as nested defense layers. Supply-chain controls scan dependencies and images, use minimal multi-stage builds, preserve immutable tags or digests, and restrict the registry. Host and runtime controls reduce the consequences of a compromised container, while workload identity gives a pod short-lived, least-privilege access to training data and model artifacts without embedding cloud keys.

Network design affects both performance and exposure. Native CNI routing avoids overlay encapsulation overhead for data-intensive training and inference, while eBPF can reduce packet-processing cost and SR-IOV can provide high-throughput device access for specialized distributed workloads. NetworkPolicy restricts which chatbot, retrieval, vector-database, and model pods may communicate. A service mesh adds request routing, retries, encryption, identity, authorization, and telemetry, but does not replace basic segmentation. Public model endpoints need TLS, authentication, authorization, rate and input controls, protected artifacts, and an application firewall or equivalent edge policy. Health checks must allow enough time for large models to load before an endpoint is considered ready.

### Schedule and share accelerators deliberately

[[Kubernetes GPU Allocation and Sharing]] explains how a vendor device plugin registers accelerator resources with the kubelet and advertises them through node status. GPU nodes can be tainted and labeled, while model pods use tolerations, selectors, and extended-resource limits such as `nvidia.com/gpu`. The NVIDIA GPU Operator can automate drivers, runtime support, device plugins, labeling, and monitoring; DCGM Exporter makes utilization, memory, temperature, power, and health metrics available to Prometheus.

Default Kubernetes allocation reserves a whole GPU for a pod, even when a small model uses only part of its memory or alternates between computation and data loading. MIG divides supported hardware into isolated instances with dedicated memory and compute slices. MPS lets compatible CUDA processes execute concurrently while retaining separate address spaces but sharing more of the device. Time-slicing rotates whole-device access among replicas with less isolation and no guaranteed fractional capacity. These mechanisms solve different problems, so the choice must consider predictable performance, fault isolation, supported workloads, and the consequences of overcommit. NVIDIA NIM packages optimized inference software and model-serving interfaces, but it still depends on correct GPU profiles and Kubernetes scheduling.

### Make experimentation reproducible and operational

[[GenAIOps Pipeline Automation]] closes the path from data to production. Data management ingests, cleans, normalizes, and versions source material. Experimentation compares foundation models and configurations in notebooks or tracked runs. Adaptation performs fine-tuning, prompt engineering, distillation, or another optimization. Serving publishes real-time or batch inference, and monitoring feeds quality and drift observations back into the pipeline.

Kubeflow combines managed notebooks, Katib tuning, DAG-based pipelines, artifact metadata, and KServe deployment. MLflow records parameters, code versions, metrics, artifacts, and registered model versions without requiring one full platform. Argo Workflows expresses container steps as Kubernetes custom resources and supplies parallelism, retries, conditional paths, and artifact movement. Ray provides distributed Python data processing, training, tuning, reinforcement learning, and model serving; KubeRay manages those clusters through Kubernetes operators. An automated drift response should gather and preprocess new data, run bias and quality gates, compare the candidate to an accepted baseline, deploy only an accepted version, and preserve every artifact and decision for diagnosis or rollback.

### Observe the model path as well as the cluster

[[GenAI Observability on Kubernetes]] combines logs, metrics, and traces. Fluent Bit can collect node and container logs with a small footprint; Loki indexes their Kubernetes labels rather than every word and correlates them with Grafana views. OpenTelemetry collectors receive, process, and export multiple signal types to backends such as Prometheus, Jaeger, or X-Ray. Prometheus discovers dynamic targets and scrapes both application and accelerator metrics, including DCGM series that reveal GPU use, memory pressure, temperature, and power.

LLM applications need another layer of context. LangChain callbacks and tracers record chain starts, tool calls, timing, retries, outputs, and errors. Langfuse associates prompts, responses, token use, model parameters, vector-database calls, latency, and errors with an end-to-end user interaction. This information is valuable but sensitive: prompts and retrieved context may contain private data, and unbounded high-cardinality traces can become expensive. Useful observability therefore preserves correlation while applying access controls, retention, redaction, and sampling.

### Align availability with recovery objectives

[[GenAI Resilience and Disaster Recovery]] starts by distinguishing the maximum acceptable data loss from the maximum acceptable outage. RPO determines replication or backup frequency, RTO determines how much capacity and automation must be ready, and maximum tolerable downtime states the outer business limit beyond which harm becomes unacceptable. Model-serving replicas need probes, disruption budgets, and topology spreading across nodes and zones. GPU node health requires extra attention because driver or device faults can strand expensive inference capacity.

Recovery strategies trade cost for speed. Backup and restore recreates clusters, objects, persistent data, model artifacts, and identity policy after failure. A pilot light keeps critical data and a minimal base running. Warm standby operates a reduced environment that can scale rapidly. Multi-site active-active serves traffic from multiple clusters or regions and aims for near-real-time recovery at the price of full replication, routing, consistency, and operational complexity. Infrastructure as code and GitOps reconstruct configuration, while rehearsed failover, chaos experiments, and recovery validation demonstrate that artifacts, vector data, secrets, and dependencies can actually be restored.

Across the chapter, the governing idea is feedback. Business criteria determine adaptation; adaptation creates artifacts; deployments expose real traffic; metrics and traces reveal performance, cost, bias, and drift; autoscaling changes capacity; and recovery testing reveals hidden dependencies. Kubernetes provides the mechanism for declaring and reconciling these components, but the system becomes production-ready only when the model, data, accelerator, and platform lifecycles are designed together.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Kubernetes Generative AI Operations]]"
```

