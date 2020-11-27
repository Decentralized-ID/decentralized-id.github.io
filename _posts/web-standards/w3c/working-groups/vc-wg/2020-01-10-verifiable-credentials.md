---
date: 2020-01-10
title: Verifiable Credentials
description: a standard way to express credentials on the Web in a way that is cryptographically secure, privacy respecting, and machine-verifiable.
excerpt: >
  Verifiable credentials (VCs) are the electronic equivalent of the physical credentials that we all possess today, such as: plastic cards, passports, driving licenses, qualifications and awards, etc. The data model for verifiable credentials is a World Wide Web Consortium Recommendation, "Verifiable Credentials Data Model 1.0 - Expressing verifiable information on the Web" published 19 November 2019.
tags: ["W3C","Verifiable Credentials","Credentials Community Group","VC-WG"]
categories: ["Web Standards"]
permalink: web-standards/w3c/wg/vc/verifiable-credentials/
redirect_from: 
  - web-standards/w3c/vc-wg/verifiable-credentials/
header:
  image: /images/verifiable-credentials_head.webp
  caption: "[Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/)"
  teaser: /images/verifiable-credentials-teaser.webp
redirect_from: 
  - web-standards/verifiable-credentials/
  - specs-standards/verifiable credentials/
last_modified_at: 2020-11-25
---

> Verifiable credentials (VCs) are the electronic equivalent of the physical credentials that we all possess today, such as: plastic cards, passports, driving licences, qualifications and awards, etc. The data model for verifiable credentials is a World Wide Web Consortium Recommendation, "Verifiable Credentials Data Model 1.0 - Expressing verifiable information on the Web" published 19 November 2019. - [Wikipedia](https://en.wikipedia.org/wiki/Verifiable_credentials)

## 101

[![IIW26 Primer On DIDs and VCs](https://i.imgur.com/TeMxwwW.png)](https://docs.google.com/presentation/d/1GMQy4rI093c_9zojwLRgp2r-fTscpDUSfX-wqwBk4j4/edit#slide=id.g3605fe1474_2_0)
  > A new type of globally resolvable, cryptographically-verifiable identifier, registered directly on a distributed ledger (aka Blockchain)

* [A Gentle Introduction to Verifiable Credentials](https://www.evernym.com/blog/gentle-introduction-verifiable-credentials/)
  > But while digital records are nothing new, today’s credentials come with certain ‘cryptographic superpowers’ that make them tamperproof, secure, and verifiable. Whereas a simple digital copy of a car title can easily be edited, a verifiable digital credential is one that has been issued by a trusted authority for, and only for, its holder.
* [A Verifiable Credentials Primer](https://github.com/WebOfTrustInfo/rwot7-toronto/blob/master/topics-and-advance-readings/verifiable-credentials-primer.md)
  > NOTE: "Verifiable Claims" are now known as "Verifiable Credentials". The W3C Verifiable Claims Working Group's experience with using the term "Verifiable Claims" demonstrated that it led to confusion in the marketplace. The group has since found consensus in shifting to use the term "Verifiable Credentials", which contain "Claims".
* [Verifiable Credentials 101 for SSI - Tyler Ruff - Webinar 11](http://ssimeetup.org/verifiable-credentials-101-ssi-tyler-ruff-webinar-11/)
  > Tyler Ruff, product manager at Evernym, will be our next guest to walk us through Verifiable Credentials in the context of Self-Sovereign Identity. He will cover how they are created, issued and shared, as well as cover some common technical questions.
* [Verifiable Credentials—A Quick Overview](https://vonx.io/safeentry/vcs/) (VonX)
  > The following is a brief overview of the technology underlying SafeEntryBC—Verifiable Credentials. In reading this, think of the process you went through to get an official government document, like a drivers license.
* [Verifiable Credentials: What They Are, Why They Matter](https://hackernoon.com/verifiable-credentials-what-they-are-why-they-matter-kl133t3d) (Hackernoon)
  > From permanent resident cards to anonymous payments to automatic notarization, verifiable credentials and DIDs are a technology whose time has arrived. Use cases are currently being piloted; many will surface in coming months and years. Security on the internet as we know it may be broken, but it is not beyond saving. A touch of the cryptographic wand, and we'll be able to repair trust once more. 
* [Understand Verifiable Cresidentials in 10 Minutes](https://www.arcblock.io/en/post/2020/04/15/verifiable-credentials)
  > This article is a soft introduction into Verifiable Credentials and the potential use cases for organizations, businesses and government institutions and creating new levels of trust for individuals and the services/institutions they use.


## Working Groups
### Verifiable Claims Working Group

* [W3C Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/) 
* [Verifiable Credentials Data Model 1.0](https://www.w3.org/TR/vc-data-model/)
  >  Credentials are a part of our daily lives; driver's licenses are used to assert that we are capable of operating a motor vehicle, university degrees can be used to assert our level of education, and government-issued passports enable us to travel between countries. This specification provides a mechanism to express these sorts of credentials on the Web in a way that is cryptographically secure, privacy respecting, and machine-verifiable. 
* [Verifiable Credentials Implementation Guidelines 1.0](https://w3c.github.io/vc-imp-guide/)
  > This guide provides some examples and resources for implementing protocols which make use of verifiable credentials, beyond those available in the core specification. 
* [W3C Verifiable Claims Working Group Test Suite](https://w3c.github.io/vc-test-suite/)
* [Verifiable Credentials Use Cases](https://www.w3.org/TR/vc-use-cases/)
  > This document does NOT attempt to define an architecture for the support of Verifiable Claims. Instead it expresses the sorts of needs that real users have that could be addressed through support for some sort of self-sovereign claim environment. It attempts to use terminology that is consistent with the other deliverables of the Verifiable Claims Working Group (you can see the relevant terms in Appendix A).

[![](https://i.imgur.com/J2IgVgl.png)](https://www.w3.org/TR/vc-use-cases/)

### Credentials Community Group

* [Credentials Community Group](https://www.w3.org/community/credentials/) • [Website](https://w3c-ccg.github.io/) • [Mail archive](http://lists.w3.org/Archives/Public/public-credentials/)
  > The mission of the Credentials Community Group is to explore the creation, storage, presentation, verification, and user control of credentials. We focus on a verifiable credential (a set of claims) created by an issuer about a subject—a person, group, or thing—and seek solutions inclusive of approaches such as: self-sovereign identity; presentation of proofs by the bearer; data minimization; and centralized, federated, and decentralized registry and identity systems. Our tasks include drafting and incubating Internet specifications for further standardization and prototyping and testing reference implementations.
* [w3c-ccg/vc-extension-registry](https://github.com/w3c-ccg/vc-extension-registry)
REGISTRY: The Verifiable Credentials Extension Registry - w3c-ccg/vc-extension-registry
* [w3c-ccg/edu_occ_verifiable_credentials](https://github.com/w3c-ccg/edu_occ_verifiable_credentials)
WORK ITEM: Drafts and Ideas of Educational and Occupational Verifiable Credentials - w3c-ccg/edu_occ_verifiable_credentials
* [w3c-ccg/vc-examples](https://github.com/w3c-ccg/vc-examples)
WORK ITEM: Verifiable Credentials Examples. 

### Claims and Credentials Working Group

[Claims and Credentials Working Group](https://identity.foundation/working-groups/claims-credentials.html) - Decentralized Identity Foundation

* [2019 JSON-LD Signature Suite](https://github.com/decentralized-identity/lds-ecdsa-secp256k1-2019.js)
  * [Ecdsa Secp256k1 Signature 2019](https://w3c-ccg.github.io/lds-ecdsa-secp256k1-2019/) - CCG Draft Community Group Report 08 April 2020
* [presentation-exchange](https://github.com/decentralized-identity/presentation-exchange)
  > Specification that codifies an inter-related pair of data formats for defining proof presentations (Presentation Definition) and subsequent proof submissions
 (Presentation Submission)
* [presentation-request](https://github.com/decentralized-identity/presentation-request)
  > Requirements Analysis and Protocol Design for a VC Presentation Request Format
* [Credential Manifest](https://github.com/decentralized-identity/credential-manifest)  
  * [Explainer](https://github.com/decentralized-identity/credential-manifest/blob/master/explainer.md)
    > Creating trust between DIDs and gaining access to products, services, and systems with DIDs requires the acquisition, generation, and inspection of credentials (DID-signed data objects).
* [Specification](https://w3c-ccg.github.io/vc-json-schemas/) - [GitHub](https://github.com/w3c-ccg/vc-json-schemas) 
  > The [VC_DATA_MODEL](https://www.w3.org/TR/vc-data-model/) specifies the models used for Verifiable Credentials and Verifiable Presentations, and explains the relationships between three parties: issuer, holder, and verifier. A critical piece of infrastructure out of the scope of those specifications is the Credential Schema. 

## Literature

* [Verifiable Credential Exchange](https://www.windley.com/archives/2018/12/verifiable_credential_exchange.shtml)
  > Multi-source identity (MSI) depends on issuing, exchanging, and verifying digital credentials. The specification for verifiable credentials is being formulated by the World Wide Web Consortium’s Verifiable Credentials Working Group. Verifiable credentials provide a standard way to express credentials in a way that is cryptographically secure, privacy respecting, and automatically verifiable.
* [Full-text Search for Verifiable Credential Metadata on Distributed Ledgers](https://arxiv.org/abs/1909.02895)
  > The proposed solution is able to find credential types based on textual input from the user by using a full-text search engine and maintaining a local copy of the ledger. Thus, we do not need to rely on information about credentials coming from a very large candidate pool of third parties we would need to trust, such as the website of a company displaying its own identifier and a list of issued credentials. We have also proven the feasiblity of the concept by implementing and evaluating a prototype of the full-text credential metadata search service.
* [Enabling Decentralised Identifiers and Verifiable Credentials for Constrained IoT Devices using OAuth-based Delegation](https://www.ndss-symposium.org/wp-content/uploads/diss2019_05_Lagutin_paper.pdf)
  > Abstract—Decentralised identifiers (DIDs) and verifiable credentials (VCs) are upcoming standards for self-sovereign privacypreserving identifiers and authorisation, respectively. This focus on privacy can help improve many services and open up new business models, but using DIDs and VCs directly on constrained IoT devices can be problematic due to the management and resource overhead. This paper presents an OAuth-based method to delegate the processing and access policy management to the Authorisation Server thus allowing also systems with constrained IoT devices to benefit from DIDs and VCs.
* [Distributed-Ledger-based Authentication with Decentralized Identifiers and Verifiable Credentials](https://arxiv.org/abs/2006.04754)
  >      Authentication with username and password is becoming an inconvenient process for the user. End users typically have little control over their personal privacy, and data breaches effecting millions of users have already happened several times. We have implemented a proof of concept decentralized OpenID Connect Provider by marrying it with Self-Sovereign Identity, which gives users the freedom to choose from a very large pool of identity providers instead of just a select few corporations, thus enabling the democratization of the highly centralized digital identity landscape. Furthermore, we propose a verifiable credential powered decentralized Public Key Infrastructure using distributed ledger technologies, which creates a straightforward and verifiable way for retrieving digital certificates. 
* [Addition of Proof Request/Response to a formal Verifiable Credentials specification](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/verifiable-credentials-proof-request.md)
  > The W3C Verifiable Credentials (hereafter VC) specification does not currently outline how credential data should be requested by a Verifier. This document outlines the approach taken at Workday and proposes it as an addition or companion to the VC spec.
  > 
  > At RWoT we wish to present our approach in order to get community feedback and consensus. Workday recently announced our credentialing platform and will shortly begin to issue credentials within our market verticals. We fully intend to support the community standards around credentialing and therefore wish to drive consensus in the community on a simple, standard approach for requesting and sharing VCs between a holder and verifier.
* [Verifiable Credentials (DID Credential Flows) : Technical Overview](https://tsmatz.wordpress.com/2020/06/25/what-is-verifiable-credentials/)
  > In the perspective of W3C specification, verifiable credential (VC) doesn’t rely on DID specification. (i.e, The “id” property used in VC shouldn’t be necessarily a DID.) However, in its real implementations, it might be expected that verifiable credentials will resolve DIDs with consistent decentralized manners and technologies. Then, in this post, we also assume that DID is used with verifiable credentials.
  > 
  > In order to explain things plainly, I’ll include not only VC flows, but also other parts of flows, such as, DID flows or OpenID compliant flows.

### FIDO

* [Integrating W3C Web Authentication (FIDO2) and Verifiable Credentials](https://www.youtube.com/watch?v=62IYP1XtTYU)
  > This is the presentation that I gave on 21 and 22 September 2020 to the UK NHS\
  > "INTEROPen Presents: Staff Access Hackathon" virtual workshop
* [W3C Verifiable Credentials - Kent Branch](https://www.bcs.org/events/2019/october/w3c-verifiable-credentials-kent-branch/) • [pdf](https://cdn.bcs.org/bcs-org-media/4653/kent-w3c-verifiable-credentials-031019.pdf)
  > The speaker will introduce the W3C Verifiable Credentials Data Model, which was published as a Proposed Recommendation in September 2019. Verifiable Credentials are the latest development in identity management and are fundamentally different from today's federated identity management systems such as SAML and OpenID Connect.
  > 
  > David will describe the VC ecosystem and data model. He will then describe the prototype implementation which was built with colleagues from the University of Toulouse. They built a prototype system, which uses Fast Identity Online (FIDO) for user authentication, meaning that usernames and passwords are no longer needed. A pilot application was tested with a small sample of NHS patients and the speaker will present the results of this trial.
* [Improved Identity Management with Verifiable Credentials and FIDO](https://ieeexplore.ieee.org/document/9031543)
  > We describe how FIDO and W3C VCs can overcome the problems of existing identity management systems. We describe our conceptual model and architecture, and the protocol we used by extending FIDO's UAF in order to provide both strong authentication and strong authorization. We built a pilot implementation for U.K. NHS patients to validate our implementation. Patients were able to use a mobile phone with a fingerprint reader to access restricted NHS sites in order to make and cancel appointments and order repeat prescription drugs. Our initial user trials with 10 U.K. NHS patients found the system to be easy to use, and fingerprints to be preferable to using usernames and passwords for authentication.

## Interoperability

* [Verifiable Credentials Specification Relationships](https://github.com/manicprogrammer/vc-spec-rel) ([ANN](https://lists.w3.org/Archives/Public/public-credentials/2020Nov/0100.html))
  > diagrams and documentation on the relationship of verfiable credential specifications
  > 
  > The current release contains some of the most core specifications and their related specs in a diagram. It does not yet address some of the items especially under DIF work groups for secure data storage, SIOP, Sidetree etc.

![](https://github.com/manicprogrammer/vc-spec-rel/releases/download/v1.1.0/VC.Spec.Relationships.Diagram.png)

* [Categorizing Verifiable Credentials - Evernym](https://www.evernym.com/blog/categorizing-verifiable-credentials/)
  > Not all verifiable credentials are created the same. This post examines the categories of credentials and the architectural choices driving this variation.
* [SSI Architectural Stack and Community Efforts Overview](https://github.com/decentralized-identity/interoperability/blob/master/assets/ssi-architectural-stack--and--community-efforts-overview.pdf)
  > While a more thorough (and competitive) separation of concerns might slice today’s and tomorrow’s identity systems into more modular and interchangeable parts at many more layers, the diagram used here organizes the space into just three broad divisions, which map roughly to the bottom three in the mapping dominant in the Aries & ToIP communities. For a more detailed and complex mapping, see the forthcoming map by the DIF interoperability working group. 
* [Interoperability Mapping Exercise](https://github.com/decentralized-identity/interoperability/blob/master/assets/interoperability-mapping-exercise-10-12-20.pdf)
* [creatornader/Decentralized Identity Standards.md](https://gist.github.com/creatornader/c8a20c534d3cf8f65a9b34ce2ad81725)
