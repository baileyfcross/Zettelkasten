# Cybersecurity Foundations and Defense

Parent topic: [[Computer Science]]

Cybersecurity Foundations and Defense is the chapter-level topic for protecting digital assets through security goals, cryptography, access control, layered defenses, threat analysis, malware understanding, practical safeguards, and adaptive response. Full Notes should link to one of the focused child topics rather than directly to this chapter tag.

## Overview Chapter

[[Cybersecurity Goals and Trust]] defines the outcomes a security program is trying to preserve. Confidentiality restricts disclosure, integrity preserves trustworthy systems and data, and availability keeps resources usable by authorized parties. Authentication establishes an identity, authorization constrains what that identity may do, and nonrepudiation supplies evidence that an action or message came from its claimed source. These goals interact, so one flaw can undermine several of them at once.

Several of those goals depend on [[Applied Cryptography and PKI]]. Encryption translates plaintext into ciphertext under a key, symmetric cryptography handles substantial data efficiently, and asymmetric cryptography supports exchanges between parties that do not already share a secret. Hashes produce one-way fixed-size representations for integrity checks, salts distinguish password verifiers, and message authentication codes or digital signatures add evidence about origin. Public key infrastructure connects public keys to identities through certificates and certificate authorities.

Protection within a host belongs to [[Operating System Security and Access Control]]. The operating system separates users, objects, processes, and memory so one execution context cannot silently corrupt another. Physical, temporal, sandboxed, and cryptographic separation provide different strengths and costs. Mandatory, discretionary, role-based, and rule-based access controls then decide which identities may reach particular resources. These mechanisms make authorization enforceable beneath individual applications.

[[Layered Cyber Defense and Secure Development]] treats no single safeguard as sufficient. People, networks, hosts, applications, data, cloud services, and mobile devices form successive defensive boundaries, with redundant controls limiting the effect of a failure at one layer. Firewalls, detection and prevention systems, and event monitoring protect and observe network activity. Secure development moves penetration testing, code review, and architecture analysis earlier into planning, construction, and deployment instead of waiting for a completed application to reveal its weaknesses.

Defenders prioritize their effort through [[Cyber Threat Vulnerability and Risk Analysis]]. A threat describes potential harm, a vulnerability is an exploitable weakness, and risk combines threat, vulnerability, likelihood, and impact around a valued asset. Attribution asks who performed an attack and how, while vulnerability catalogs and web-risk categories provide shared names for known weaknesses. The cyber kill chain breaks an intrusion into reconnaissance, weaponization, delivery, exploitation, installation, command and control, and actions on objectives so defenses can interrupt more than the final step.

[[Malware Types and Propagation]] distinguishes malicious programs by dependence, replication, disguise, and objective. Viruses attach to hosts, worms execute and spread independently, Trojans masquerade as legitimate software, and logic bombs wait for a trigger. Bots form remotely controlled networks, while spyware, rootkits, backdoors, adware, and ransomware specialize in observation, concealment, access, unwanted advertising, or denial through extortion. Component models expose the search, copying, propagation, control, triggering, tracking, and payload stages behind those labels.

Security appears in ordinary technology through [[Everyday Cybersecurity Applications]]. Passwords, additional factors, biometrics, virtual private networks, and tokens establish or protect access. E-commerce and payment systems depend on protected identities and transaction data, while blockchains use cryptographic records to make transactions difficult to alter or deny. Smart devices and Internet of Things equipment extend the same concerns to constrained, always-connected hardware whose default credentials and long service lives can make large botnets possible.

[[Adaptive and Outcome-Based Cyber Defense]] looks beyond fixed attack signatures. Computer immunology models a system as distinguishing legitimate self from dangerous nonself, remembering earlier infections, detecting novel behavior, and protecting its own defensive mechanisms. Outcome-based defense assumes attacks may occur and focuses resources on preventing denial of service, data theft, or deception that would defeat the system's mission. Behavioral baselines, anomaly detection, extrusion detection, and preserved multi-day context support responses to changing and persistent threats.

Together, these topics connect security objectives to concrete controls and observable attack behavior. Trust is not produced by one device or algorithm: it emerges from protected identities and keys, constrained execution, layered monitoring, secure development, risk-informed priorities, informed users, and recovery mechanisms aligned with the outcomes a system exists to deliver.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Cybersecurity Foundations and Defense]]"
```
