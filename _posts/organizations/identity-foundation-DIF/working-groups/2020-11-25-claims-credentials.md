---
date: 2020-11-25
title: DIF - Claims and Credentials Working Group
description: Standards and technology that create, exchange, and verify claims and credentials in a decentralized identity ecosystem. 
excerpt: >
    Join this group to contribute to the standards and technology that create, exchange, and verify claims and credentials in a decentralized identity ecosystem. For example, a cryptographically verifiable credential that proves an individual has a college degree or is of a certain age. Our members focus on specs that are vendor agnostic and based on industry standards.
permalink: organizations/identity-foundation/wg/claims-and-credentials/
canonical_url: https://decentralized-id.com/organizations/identity-foundation/wg/claims-and-credentials/
redirect_from: organizations/identity-foundation/claims-and-credentials-wg/
categories: ["Identity Foundation (DIF)","Web Standards"]
tags: ["Verifiable Credentials","Claims and Credentials WG","JSON-LD","Credentials Community Group","DIF"]
header:
  image: /images/claims-credentials-header.webp 
  teaser: /images/claims-credentials-teaser.webp
last_modified_at: 2020-11-25
---

[DIF - Claims and Credentials Working Group](https://identity.foundation/working-groups/claims-credentials.html) - [GitHub](https://github.com/decentralized-identity/claims-credentials)

> Join this group to contribute to the standards and technology that create, 
exchange, and verify claims and credentials in a decentralized identity 
ecosystem. For example, a cryptographically verifiable credential that 
proves an individual has a college degree or is of a certain age. Our 
members focus on specs that are vendor agnostic and based on industry 
standards.

## Claims and Credentials WG documentation
                                              
* [C&C WG Charter](https://github.com/decentralized-identity/org/blob/master/Org%20documents/WG%20documents/DIF_CC_WG_charter_v1.pdf)
  > **Working Group Scope​.**
  > - Claims & Credential Interoperable Formats: ​Develop interoperable formats for broad adoption around Claim & Credential processes within SSI. These include
  >   - Static Payload Formats like: Verifiable Credential, Verifiable Presentation, CredentialSubject Schemas (building on top of the W3C formats - only if the extension is a requirement by DIF partners, see “out of scope”)
  >   - Data formats that support the communication between one and more participants in regard to Credential processes. For Example: Credential Manifest (Requirements for Issuing a new Credential), Presentation Definition (Requirements for presenting existing proofs, (partial, verifiable) credentials and unverifiable data), Presentation Submission (Response format to a Presentation Definition).
  >   - Documentation of existing formats and protocols that are in use or under active development by existing SSI ecosystems and industry partners. Support in unifying migrating those to more interoperable formats / standards.
  > - Claims & Credential Taxonomies: ​There is currently no coordinated effort to align the contexts used in the highly-flexible verifiable credentials format. For example, what is the best way to encode a KYC check, credit score, user consent, or proof of employment?
* [CC WG Operating Addendum](https://github.com/decentralized-identity/org/blob/master/Org%20documents/WG%20documents/DIF_CC_WG_Operating_Addendum_V1.pdf)
  > **Core Principles**
  > - Work on the request, creation, exchange, and verification of identity credentials or claims in avendor-agnostic manner​
  > - Support the development of DIDs and Verifiable Credentials​
  > - Actively support projects that demonstrate interoperable use-cases within the space of claims andcredentials utilization within self-sovereign identity systems
  > - Help community members advocate for the mainstream adoption of blockchain identity and credentials​.
  > - Support industry-specific taxonomy development around credentials other identity-centric data formats
* [Mailing list](https://dif.groups.io/g/cc-wg) - Develop interoperable formats for broad adoption around Claim & Credential processes within SSI. 
* [Meeting notes](https://www.notion.so/dif/Claims-and-Credentials-d236ac4366d54c76ba85c2f521c003e0)

## Specs and Projects

* [2019 JSON-LD Signature Suite](https://github.com/decentralized-identity/lds-ecdsa-secp256k1-2019.js)
  * [Ecdsa Secp256k1 Signature 2019](https://w3c-ccg.github.io/lds-ecdsa-secp256k1-2019/) - CCG Draft Community Group Report 08 April 2020
* [presentation-exchange](https://github.com/decentralized-identity/presentation-exchange)
  > Specification that codifies an inter-related pair of data formats for defining proof presentations (Presentation Definition) and subsequent proof submissions
 (Presentation Submission)
* [presentation-request](https://github.com/decentralized-identity/presentation-request)
  > Requirements Analysis and Protocol Design for a VC Presentation Request Format

### [Credential Manifest](https://github.com/decentralized-identity/credential-manifest)  

> The DID Credential Manifest is a format that aims to normalize the process of credential acquisition, wherein the issuer is able to describe the requirements the subject or participant in the credential generation process must meet for the issuer to generate the desired credential. 

* [Explainer](https://github.com/decentralized-identity/credential-manifest/blob/master/explainer.md)
  > Creating trust between DIDs and gaining access to products, services, and systems with DIDs requires the acquisition, generation, and inspection of credentials (DID-signed data objects).

### [VC JSON Schemas](https://github.com/w3c-ccg/vc-json-schemas) 

> The VC JSON Schema specification aims to provide a standardized mechanism to use JSON Schemas as the data backing for Verifiable Credentials. Though the repository lives in the W3C-CCG, this working group contains key contributors and has a vested interest in contributing to the development of the specification. 

* [Specification](https://w3c-ccg.github.io/vc-json-schemas/) 
  > The [VC_DATA_MODEL](https://www.w3.org/TR/vc-data-model/) specifies the models used for Verifiable Credentials and Verifiable Presentations, and explains the relationships between three parties: issuer, holder, and verifier. A critical piece of infrastructure out of the scope of those specifications is the Credential Schema. 
