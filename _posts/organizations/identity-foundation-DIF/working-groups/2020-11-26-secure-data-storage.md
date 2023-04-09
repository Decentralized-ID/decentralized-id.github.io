---
date: 2020-11-26
title: Secure Data Storage WG - DIF 
description: data models for storage and transport, syntax, data at rest protection, CRUD API, access control, synchronization, and at least a minimum viable HTTP-based interface compatible with W3C DIDs/VCs.
excerpt: >
  Secure, encrypted, privacy-preserving storage and computation of data is a critical component of decentralized identity systems. As with identifiers and names must be self-sovereign to the owning entity, a user's identity data must remain private, only accessible to the entities they allow. DIF members are actively developing specs and reference implementations for provider-agnostic, run-anywhere solutions that provides these features.
permalink: organizations/decentralized-identity-foundation/wg/secure-data-storage/
canonical_url: https://decentralized-id.com/organizations/decentralized-identity-foundation/wg/secure-data-storage/
redirect_from: 
  - organizations/identity-foundation/wg/secure-data-storage/
categories: [Identity Foundation (DIF),Web Standards]
tags: ["Storage and Compute WG","DIF","Secure Data Storage","Data Hubs","W3C","Encrypted Data Vaults"]
header:
  image: /images/secure-data-storage-head.webp
  teaser: /images/secure-data-storage-teaser.webp
last_modified_at: 2020-11-26
---

[Webpage](https://identity.foundation/working-groups/storage-compute.html) - [Wiki](https://dif.groups.io/g/sds-wg/wiki) - [GitHub](https://github.com/decentralized-identity/confidential-storage/)

> Secure, encrypted, privacy-preserving storage and computation of data is a critical component of decentralized identity systems. As with identifiers and names must be self-sovereign to the owning entity, a user's identity data must remain private, only accessible to the entities they allow. DIF members are actively developing specs and reference implementations for provider-agnostic, run-anywhere solutions that provides these features.

- [Mailing List](https://dif.groups.io/g/sds-wg/wiki/home)
  - [Working Group Wiki](https://lists.identity.foundation/g/sds-wg/wiki)
    > Create one or more specifications to establish a foundational layer for secure data storage (including personal data), specifically data models for storage and transport, syntax, data at rest protection, CRUD HTTP API, access control, synchronization, and a minimum viable HTTP-based interface compatible with W3C DIDs/VCs.
- [Secure Data Storage Working Group Charter](https://drive.google.com/file/d/1vf2CsD9QZstzrd6CJ4WFVHw0WKwwNLHf/view)
  > - Create one or more specifications to establish a foundational layer for secure data storage (including personal data), specifically data models for storage and transport, syntax, data at rest protection, CRUD API, access control, synchronization, and at least a minimum viable HTTP-based interface compatible with W3C DIDs/VCs.
  > - The [Identity Hubs](https://github.com/decentralized-identity/identity-hub/blob/master/explainer.md) and [Encrypted Data Vaults](https://digitalbazaar.github.io/encrypted-data-vaults/) documents will be used as a use case, requirements, and technical input for the collaborative effort.

## Specs & Projects

The active work items that are underway in the DIF Storage and Compute Working Group

### Confidential Storage

- [decentralized-identity/confidential-storage/](https://github.com/decentralized-identity/confidential-storage/)
- [Latest Editors Draft](https://identity.foundation/confidential-storage/)
  > We store a significant amount of sensitive data online, such as personally identifying information (PII), trade secrets, family pictures, and customer information. The data that we store is often not protected in an appropriate manner.
  > 
  > This specification describes a privacy-respecting mechanism for storing, indexing, and retrieving encrypted data at a storage provider. It is often useful when an individual or organization wants to protect data in a way that the storage provider cannot view, analyze, aggregate, or resell the data. This approach also ensures that application data is portable and protected from storage provider data breaches.
* [DIF SDS/CS WG: CS Refactoring Proposal 0.2](https://hyperonomy.com/2021/03/28/cs-refactoring-proposal/) Hyperonomy
  > 1. Latest Version of the Proposal (0.2 – March 24, 2021)
  > 2. Agent-Hub-EDV Architecture Reference Model (AHE-ARM) 0.1
  > 3. Transcription of Selected Parts of the DIF SDS/CS March 11, 2021 Zoom Call
  > 4. OSI Stack Proposal for Confidential Storage Specification
  > 
  > Based on the March 11 Zoom discussion where we worked hard to discern the differences between Agents, Hubs, and EDVs (and I believe were largely successful IMO), I’ve like to propose to the SDS/CS WG that we refactor the current Confidential Storage specification into 3 separable parts/specifications.  I also present a high-level roadmap (simple ordering) for how the WG might proceed if this refactoring is accepted (or at least, if the first part/first new specification is accepted).

### Identity Hubs (Archived)

Encrypted personal datastore for identity interactions and decentralized apps.

* [Identity Hubs](https://github.com/decentralized-identity/identity-hub/)
  * [Explainer](https://github.com/decentralized-identity/identity-hub/blob/master/explainer.md)  
    > Hubs let you securely store and share data. A Hub is a datastore containing semantic data objects at well-known locations. Each object in a Hub is signed by an identity and accessible via a globally recognized API format that explicitly maps to semantic data objects. Hubs are addressable via unique identifiers maintained in a global namespace.     
* [System Diagram](https://raw.githubusercontent.com/decentralized-identity/hubs/master/diagrams/full-system.png)

[![](https://raw.githubusercontent.com/decentralized-identity/hubs/master/diagrams/full-system.png)](https://raw.githubusercontent.com/decentralized-identity/hubs/master/diagrams/full-system.png)

### Encrypted Data Vaults (Archived)

* [Encrypted Data Vaults](https://digitalbazaar.github.io/encrypted-data-vaults/)
  > We store a significant amount of sensitive data online, such as personally identifying information (PII), trade secrets, family pictures, and customer information. The data that we store is often not protected in an appropriate manner.
  > 
  > Legislation, such as the General Data Protection Regulation (GDPR), incentivizes service providers to better preserve individuals' privacy, primarily through making the providers liable in the event of a data breach. This liability pressure has revealed a technological gap, whereby providers are often not equipped with technology that can suitably protect their customers. Encrypted Data Vaults fill this gap and provide a variety of other benefits.
