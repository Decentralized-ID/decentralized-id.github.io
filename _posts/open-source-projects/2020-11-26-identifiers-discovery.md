---
date: 2020-11-26
title: Identifiers & Discovery Working Group - DIF 
description: Specifications, implementations, test suites, etc. related to creation, derivation, resolution, management, use of all forms of decentralized identifiers 
excerpt: >
    Members of the Working Group are engaged in development of protocols and systems that enable creation, resolution, and discovery of decentralized identifiers and names across underlying decentralized systems, like blockchains and distributed ledgers.
permalink: organizations/identity-foundation/identifiers-and-discovery-wg/wg/identifiers-and-discovery/
redirect_from: 
  - organizations/identity-foundation/identifiers-and-discovery-wg/
  - organizations/identity-foundation/wg/identifiers-and-discovery/
canonical_url: https://decentralized-id.com/organizations/identity-foundation/wg/identifiers-and-discovery/
categories: ["Open Source Projects"]
tags: ["Identifiers and Discovery WG","DID","DIF","Universal Resolver","Universal Registrar","KERI","Verifiable Credentials","JSON-LD","Ethereum","ION","BTCR","DID:PEER","ERC725","Linked Data"]
header:
  image: /images/identifiers-discovery-head.webp
  teaser: /images/identifiers-discovery-teaser.webp
last_modified_at: 2020-11-26
---

[Webpage](https://identity.foundation/working-groups/identifiers-discovery.html) - [GitHub](https://github.com/decentralized-identity/identifiers-discovery) - [Slack](https://difdn.slack.com/messages/C4WED8JSH)

> Members of the Working Group are engaged in development of protocols and systems that enable creation, resolution, and discovery of decentralized identifiers and names across underlying decentralized systems, like blockchains and distributed ledgers.

* [I&D WG Charter](https://github.com/decentralized-identity/org/blob/master/Org%20documents/WG%20documents/DIF_ID_WG_charter_v1.pdf)
  - Specifications, implementations, test suites, etc. related to creation, derivation, resolution, management, use of all forms of decentralized identifiers (i.e. including, but not limited to W3C DIDs)
  - Relationship between identifier systems (e.g. DID and domain names)
  - Relationship between identifiers and other decentralized identity building blocks (e.g. EDV)
  - Discovery protocols (e.g. for hubs, agents)
  - Establishment and maintenance of control authority over an identifier (e.g. KERI)
  - Security and trust in identifier infrastructure (e.g. Linked Data Security)
  - Work on concrete DID methods   
* [Mailing list](https://lists.identity.foundation/g/id-wg)
  > A key piece of the decentralized identity equation is how people, organizations, and devices can be identified and located without centralized systems of identifiers (e.g. email addresses). DIF members are actively working on protocols and implementations that enable creation, resolution, and discovery of decentralized identifiers and names across decentralized systems, like blockchains and distributed ledgers.
* [Meeting page](https://github.com/decentralized-identity/identifiers-discovery/blob/main/agenda.md)
  > For this call, you are encouraged to turn your video on. This is a good way to build rapport given we are a large, disparate group experiencing a lot of churn.
  > 
  > This document is live-edited DURING each call, and stable/authoritative copies live on our github repo under /agenda.md . Please note that we might not notice a pullrequest in time, but you are free to propose agenda items for future meetings via hackmd.

## Specs & Projects
### [Universal Resolver](https://uniresolver.io/)

Spec and implementation of a driver-based framework that enables resolution of DIDs.
                  
* [decentralized-identity/universal-resolver](https://github.com/decentralized-identity/universal-resolver)
  > A Universal Resolver is an identifier resolver that works with any decentralized identifier system, including Decentralized Identifiers (DIDs).
  * [Driver Development](https://github.com/decentralized-identity/universal-resolver/blob/master/docs/driver-development.md)
    > The Universal Resolver's function is wrapping an API around a number of co-located Docker containers running DID-method-specific drivers. The Universal Resolver is designed to support additional DID methods as they are developed by the community. The contribution for a new DID method driver consists of a Docker image which exposes an HTTP interface for resolving DIDs. New contributions are submitted as Pull Requests to the Universal Resolver (this) repository.
* [decentralized-identity/universal-resolver-frontend](https://github.com/decentralized-identity/universal-resolver-frontend) - Frontend web UI for Universal Resolver.
* [decentralized-identity/universal-resolver-java](https://github.com/decentralized-identity/universal-resolver-java)
* [decentralized-identity/universal-resolver-python](https://github.com/decentralized-identity/universal-resolver-python)

#### Resolver Drivers

* [decentralized-identity/uni-resolver-driver-did-erc725](https://github.com/decentralized-identity/uni-resolver-driver-did-erc725) - A Universal Resolver driver for did:erc725 identifiers.
* [decentralized-identity/uni-resolver-driver-did-ion](https://github.com/decentralized-identity/uni-resolver-driver-did-ion) - Universal Resolver Driver for Identity Overlay Network (ION) DIDs
* [decentralized-identity/uni-resolver-driver-did-key](https://github.com/decentralized-identity/uni-resolver-driver-did-key) - A Universal Resolver driver for did:key identifiers.
* [decentralized-identity/uni-resolver-driver-did-sov](https://github.com/decentralized-identity/uni-resolver-driver-did-sov) - A Universal Resolver driver for did:sov identifiers.
* [decentralized-identity/uni-resolver-driver-did-stack](https://github.com/decentralized-identity/uni-resolver-driver-did-stack) - A Universal Resolver driver for did:stack identifiers.
* [decentralized-identity/uni-resolver-driver-did-work](https://github.com/decentralized-identity/uni-resolver-driver-did-work) - A Universal Resolver driver for did:work identifiers.
* [decentralized-identity/uni-resolver-driver-dns](https://github.com/decentralized-identity/uni-resolver-driver-dns) - A Universal Resolver driver for domain names.

### [Universal Registrar](https://uniregistrar.io/)
Spec and implementation of a driver-based framework that enables creation/updates/deactivation of DIDs.
                  
* [decentralized-identity/universal-registrar](https://github.com/decentralized-identity/universal-registrar)
  > A Universal Registrar is an identifier registrar that works with any decentralized identifier system, including Decentralized Identifiers (DIDs).
  * [Driver Development](https://github.com/decentralized-identity/universal-registrar/blob/master/docs/driver-development.md)
    > The Universal Registrar's function is wrapping an API around a number of co-located Docker containers running DID-method-specific drivers. The Universal Registrar is designed to support additional DID methods as they are developed by the community. The contribution for a new DID method driver consists of a Docker image which exposes an HTTP interface for creating/updating/deactivating DIDs. New contributions are submitted as Pull Requests to the Universal Registrar (this) repository. 
* [decentralized-identity/universal-registrar-frontend](https://github.com/decentralized-identity/universal-registrar-frontend) - Frontend web UI for Universal Registrar.

#### Registrar Drivers

* [decentralized-identity/uni-registrar-driver-did-btcr](https://github.com/decentralized-identity/uni-registrar-driver-did-btcr) - A Universal Registrar driver for did:btcr identifiers.
* [decentralized-identity/uni-registrar-driver-did-key](https://github.com/decentralized-identity/uni-registrar-driver-did-key) - A Universal Registrar driver for did:key identifiers.
* [decentralized-identity/uni-registrar-driver-did-sov](https://github.com/decentralized-identity/uni-registrar-driver-did-sov) - A Universal Registrar driver for did:sov identifiers.
* [decentralized-identity/uni-registrar-driver-did-v1](https://github.com/decentralized-identity/uni-registrar-driver-did-v1) - A Universal Registrar driver for did:v1 identifiers.
* [decentralized-identity/uni-resolver-driver-did-btcr](https://github.com/decentralized-identity/uni-resolver-driver-did-btcr) - A Universal Resolver driver for did:btcr identifiers.
* [decentralized-identity/uni-resolver-driver-did-ccp](https://github.com/decentralized-identity/uni-resolver-driver-did-ccp) - A Universal Resolver driver for Baidu did:ccp identifiers.
* [decentralized-identity/uni-resolver-driver-did-dom](https://github.com/decentralized-identity/uni-resolver-driver-did-dom) - A Universal Resolver driver for did:dom identifiers.

### .well-known DID configuration
Spec, docs, and implementations for discovering DIDs from .well-known HTTP(S) URIs.
                  
* [decentralized-identity/.well-known/](https://github.com/decentralized-identity/.well-known/)
  * [Repo Webpage](https://identity.foundation/.well-known/)
  > Making it possible to connect existing systems and Decentralized Identifiers (DIDs) is an important undertaking that can aid in bootstrapping adoption and usefulness of DIDs. One such form of connection is the ability of a DID controller to prove they are the same entity that controls an origin.
  > 
  > The DID Configuration resource provides proof of a bi-directional relationship between the controller of an origin and a DID via cryptographically verifiable signatures that are linked to a DID's key material. This document describes the data format of the resource and the resource location at which origin controllers can publish their DID Configuration.
* [Spec](https://identity.foundation/specs/did-configuration/)
  > Making it possible to connect existing systems and Decentralized Identifiers (DIDs) is an important undertaking that can aid in bootstrapping adoption and usefulness of DIDs. One such form of connection is the ability of a DID controller to prove they are the same entity that controls an Internet domain.
  > 
  > The DID Configuration resource provides proof of a bi-directional relationship between the controller of an Internet domain and a DID via cryptographically verifiable signatures that are linked to a DID's key material. This document describes the data format of the resource and the resource location at which Internet domain controllers can publish their DID Configuration.
  > 
  > Due to the location of the DID Configuration resource, discovery of associated Decentralized Identifiers against a domain is trivial. However, the inverse (i.e given a DID-URI discover the associated domains) is deemed out of scope.
 
                  
### KERI - Key Event Receipt InfrastructureSpec and implementation of an identifier and key 
rotation technology, where your primary root of trust is entropy, not 
any particular ledger.
                  
* [decentralized-identity/keri](https://github.com/decentralized-identity/keri) - Key Event Receipt Infrastructure - the spec and implementation of the KERI protocol
* [decentralized-identity/kerigo](https://github.com/decentralized-identity/kerigo) - Go implementation of KERI  (Key Event Receipt Infrastructure)
* [decentralized-identity/kerijs](https://github.com/decentralized-identity/kerijs) - JavaScript (nodes) Implementation of the KERI core library.
* [decentralized-identity/keriox](https://github.com/decentralized-identity/keriox) - Rust Implementation of the KERI Core Library
* [decentralized-identity/keripy](https://github.com/decentralized-identity/keripy) - Python Implementation of the KERI Core Libraries

### Peer DID Method Specification

A rich DID method that has no blockchain dependencies. The verifiable data registry is a synchronization protocol between peers.

* [decentralized-identity/peer-did-method-spec](https://github.com/decentralized-identity/peer-did-method-spec)
* [Spec](https://identity.foundation/peer-did-method-spec/)
  > This document defines a "peer" DID Method that conforms to the DID Spec. The method can be used independent of any central source of truth, and is intended to be cheap, fast, scalable, and secure. It is suitable for most private relationships between people, organizations, and things. We expect that peer-to-peer relationships in every blockchain ecosystem can benefit by offloading pairwise and n-wise relationships to peer DIDs.

### DID Spec Extensions 

Extension parameters, properties, and values for the DID spec registries.
                   
* [decentralized-identity/did-spec-extensions](https://github.com/decentralized-identity/did-spec-extensions)

### Other Repositories

* [decentralized-identity/did-common-java](https://github.com/decentralized-identity/did-common-java) - Shared DID Java library.
* [decentralized-identity/did-jwt](https://github.com/decentralized-identity/did-jwt) - Create and verify DID verifiable JWT's in Javascript
* [decentralized-identity/did-jwt-vc](https://github.com/decentralized-identity/did-jwt-vc) - Create and verify W3C Verifiable Credentials and Presentations in JWT format
* [decentralized-identity/did-resolver](https://github.com/decentralized-identity/did-resolver) - Universal did-resolver for javascript environments
* [decentralized-identity/did-spec-extensions](https://github.com/decentralized-identity/did-spec-extensions) - Extension parameters, properties, and values for the DID spec registries.
* [decentralized-identity/ethr-did-resolver](https://github.com/decentralized-identity/ethr-did-resolver) - DID resolver for Ethereum Addresses with support for key management
* [decentralized-identity/horcrux](https://github.com/decentralized-identity/horcrux) - Horcrux Protocol
* [activestorage-horcrux](https://github.com/decentralized-identity/activestorage-horcrux)
  > An ActiveStorage service option that uploads shares across one or more other storage services using Shamir Secret Sharing (via the tss-rb gem). Use it in your storage.yml file. It is not a mirror, but can be named as a storage service.
* [decentralized-identity/context](https://github.com/decentralized-identity/context) - DIF Security Contexts & Schemas for Linked Data
* [decentralized-identity/fuzzy-encryption](https://github.com/decentralized-identity/fuzzy-encryption) - A variant of a Fuzzy Vault cryptographic scheme designed for encrypting data with better human recovery features.
* [decentralized-identity/jsonld-common-java](https://github.com/decentralized-identity/jsonld-common-java) - Shared JSON-LD Java library.
* [jsonld-document-loader](https://github.com/decentralized-identity/jsonld-document-loader)
  > Document loaders enable decentralized security, interoperability and extensibility while gaurding against vendor lock in.
