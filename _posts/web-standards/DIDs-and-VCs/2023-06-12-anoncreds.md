---
title: "Hyperledger Anoncreds: Attribute Based Credentials"
description: Anoncreds has been modularized from the Hyperledger Indy blockchain framework. 
excerpt: > 
  Hyperledger AnonCreds – short for “Anonymous Credentials”- is the most commonly used Verifiable Credential (VC) format in the world. Ledger agnostic and with a formal open specification, AnonCreds is a VC format that adds important privacy-protecting ZKP (zero-knowledge proof) capabilities to the core VC assurances.
layout: single
categories: ["Verifiable Credentials and Decentralized Identifiers"]
tags: ["Hyperledger Foundation","IBM","IDEMIX","Anoncreds","Sovrin Foundation","Evernym","ZKP-CL"]
permalink: /projects/hyperledger/anoncreds/
canonical_url: 'https://decentralized-id.com/projects/hyperledger/anoncreds/'
last_modified_at: 2023-07-02
---

## Main
[Website](https://www.hyperledger.org/use/anoncreds) - [Specification](https://github.com/hyperledger/anoncreds-spec) - [Specification V2](https://github.com/hyperledger/anoncreds-spec-v2)

> Hyperledger AnonCreds – short for “Anonymous Credentials”- is the most commonly used Verifiable Credential (VC) format in the world. Ledger agnostic and with a formal open specification, AnonCreds is a VC format that adds important privacy-protecting ZKP (zero-knowledge proof) capabilities to the core VC assurances.

* [anoncreds-rs](https://github.com/hyperledger/anoncreds-rs) 2023-06-02 Hyperledger 
  > Rust library and reference implementation of the [Anoncreds V1.0](https://hyperledger.github.io/anoncreds-spec/) specification.
* [Hyperledger launches new digital identity project, AnonCreds](https://www.ledgerinsights.com/hyperledger-digital-identity-anoncreds-verifiable-credentials-privacy/) 2022-11-15
  > The technology itself is not new, as it was originally part of Hyperledger Indy, the digital identity ledger project. However, it has now been separated from Indy so that it can be used for verifiable credentials on ledgers such as Hyperledger Fabric or Ethereum-based Hyperledger Besu, or others.

## Working Group

* [AnonCreds Specification Working Group](https://wiki.hyperledger.org/display/ANONCREDS/AnonCreds+Specification+Working+Group) 2022-11-02
  > The AnonCreds Specification Working Group operates under the Community Specification License v1.0 to create the AnonCreds Specification. Current work is focused on Version 1.0 of the specification that covers the current CL-Signatures-based implementation of AnonCreds agnostic to the underlying ledger.
* [Video] [Hyperledger AnonCreds Specification Working Group](https://www.youtube.com/watch?v=sUcstipdEm8) 2023-06-19 Hyperledger Foundation
  > The big thing I want to talk about was a couple of things on revocation approaches and and go over possibilities. There, there's a few things happening that I wanted to share. [...] as I mentioned in our credits announcements, the 0.1.0 rust implementation was officially released

## Development

* [Hyperledger AnonCreds Workshop: Using ZKP Verifiable Credentials Everywhere](https://www.youtube.com/watch?v=1RrJky42dvg) Hyperledger Foundation
  > AnonCreds was accepted as an Incubated project at Hyperledger in late 2022. This is the first workshop developed by this community and it is intended for anyone interested in using Zero Knowledge Proofs (ZKPs) in a wide variety of contexts. 

## Background
- [Anonymous Credential Part 1: Brief Overview and History](https://medium.com/finema/anonymous-credential-part-1-brief-overview-and-history-c6679034c914) 2020-10-01
  > An anonymous credential (Anoncred), which is also known as an attribute-based credential (ABC), is a concept for a digital credential that provides a credential holder maximal privacy and an ability to selectively disclose their personal information.
- [Anonymous Credential Part 2: Selective Disclosure and CL Signature](https://medium.com/finema/anonymous-credential-part-2-selective-disclosure-and-cl-signature-b904a93a1565) 2021-02-04
  > selective disclosure and an anonymous credential (Anoncred) relies on an efficient signature scheme that supports multiple messages with a single signature. One such signature scheme is known as CL signature that is named after its Jan Camenisch and Anna Lysyanskaya […] CL signature popularized Anoncreds, and it also served as a cryptographic building block in Identity Mixer (Idemix) and Hyperledger Indy projects.
* [Wrapping Indy Credentials (AnonCreds) in W3C VCs](https://hackmd.io/S6e2MeSWTICnV9lD9OukKg) 2021-04-12
  > AnonCreds are typically bound to a holder by using a link secret and not by issuing a credential to a public DID. In order to add such a credential (or a subset of attributes) to the public profile, we suggest the following mechanism which expresses the intent: I self-attest that I have this credential with the specific attribute values, if you require a proof you can ask me using the Aries present proof protocol.

## Critique

* [Being “Real” about Hyperledger Indy & Aries / Anoncreds](https://identitywoman.net/being-real-about-hyperledger-indy-aries-anoncreds/) 2022-09-10 IdentityWoman
  > This article surfaces a synthesis of challenges / concerns about Hyperledger Indy & Aries / Anoncreds, the most marketed Self-Sovereign Identity technical stack. It is aimed to provide both business and technical decision makers a better understanding of the real technical issues and related business risks of Hyperledger Indy & Aries / Anoncreds, which have not been shared and discussed openly or publicly as the author believes need to be.

### Response

* [Hyperledger launches new digital identity project, AnonCreds](https://www.ledgerinsights.com/hyperledger-digital-identity-anoncreds-verifiable-credentials-privacy/) 2022-11-15
  > The technology itself is not new, as it was originally part of Hyperledger Indy, the digital identity ledger project. However, it has now been separated from Indy so that it can be used for verifiable credentials on ledgers such as Hyperledger Fabric or Ethereum-based Hyperledger Besu, or others.
* [A response to Identity Woman's recent blog post about Anoncreds](https://kyledenhartog.com/response-to-anoncreds-criticism/) 2022-09-08 Kyle Den Hartog
  > It’s only when I started to take a step back that I realized that the architecture of Indy being a private, permissioned ledger leaves it heading in the same direction as many large corporations now extinct browser and intranet projects for many of the same reasons.
* [Moving Toward Identity Technology Ready for Mass Adoption](https://trinsic.id/moving-toward-identity-technology-ready-for-mass-adoption/) 2022-09-09 Trinsic
  > when we realized our customers were facing critical limitations caused by the underlying tech stack, we began developing an updated version of our platform that would reduce our dependency on these technologies and enable a better platform for our customers.

## Prior Work
* [How is IDEMix Implemented?](https://forum.sovrin.org/t/how-idemex-is-implemented-in-sovrin-indy/)
  > Identity Mixer is not directly (re)implemented by Sovrin, but its cryptographic foundations are very similar, and Sovrin’s implementation includes most of its extended features (predicates, multi-credential, revocation, advanced issuance…). One of the researchers who helped to create Identity Mixer is on Sovrin’s Technical Governance Board and has offered insight to keep the implementations aligned on goals and methods. 
* [IDEMIX Blog](https://idemix.wordpress.com/) 
* [ABC4Trust—Attribute-based Credentials for Trust](https://abc4trust.eu/)
* [Concepts and Features of Privacy-Preserving Attribute-Based Credentials](https://github.com/p2abcengine/p2abcengine/wiki/Concepts-and-features)
* [Concepts and Languages for Privacy-Preserving Attribute-Based Authentication](http://dl.ifip.org/db/conf/idman/idman2013/CamenischDLNPP13.pdf)