---
title: "Verifiable Credentials with JOSE (JWT) / COSE (CBOR)"
layout: single
description: "enables the Verifiable Credential data model [VC-DATA-MODEL] to be implemented with standards for signing and encryption that are widely adopted."
excerpt: >
  Digital proof mechanisms, a subset of which are digital signatures, are required to ensure the protection of a verifiable credential. Having and validating proofs, which may be dependent on the syntax of the proof (for example, using the JSON Web Signature of a JSON Web Token for proofing a key holder), are an essential part of processing a verifiable credential.
tags: ["W3C","Verifiable Credentials","JWT","IANA","JOSE","COSE"]
categories: ["Verifiable Credentials and Decentralized Identifiers"]
permalink: /web-standards/w3c/verifiable-credentials/jose-jwt+cose-cbor/
header:
  image: /images/Verifiable-Credentials-Flavors-Explained_jwt.webp
  caption: "[[**Verifiable Credentials Flavors Explained**]](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf) 2021 CCI Kaliya 'Identity Woman' Young [[**Infographic**](https://www.lfph.io/wp-content/uploads/2021/04/Verifiable-Credentials-Flavors-Explained-Infographic.pdf)]"
  teaser: /images/Verifiable-Credentials-Flavors-Explained_jwt-teaser.webp
last_modified_at: 2023-09-09
---

## Main
* [Working Draft] [Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/) 2023-09-08 Orie Steele, Michael Jones, Michael Prorock
  >  This specification defines how to secure credentials and presentations conforming to the [VC-DATA-MODEL](https://www.w3.org/TR/vc-jose-cose/#bib-vc-data-model), with JSON Object Signing and Encryption (JOSE), and CBOR Object Signing and Encryption ([COSE](https://datatracker.ietf.org/wg/jose/about/)) [RFC9052](https://www.w3.org/TR/vc-jose-cose/#bib-rfc9052). This enables the Verifiable Credential data model [VC-DATA-MODEL] to be implemented with standards for signing and encryption that are widely adopted. 
* [Native JWT Representation for Verifiable Credentials](https://self-issued.info/?p=2316) 2023-02-10 Mike Jones
  > For the first time, there is now a native JSON Web Token (JWT) representation for Verifiable Credentials. This representation uses IANA-registered JWT claims whenever applicable. 
* [Editors Draft] [Verifiable Credentials Data Model v2.0](https://w3c.github.io/vc-data-model/) 2023-09-09
  > Digital proof mechanisms, a subset of which are digital signatures, are required to ensure the protection of a verifiable credential. Having and validating proofs, which may be dependent on the syntax of the proof (for example, using the JSON Web Signature of a JSON Web Token for proofing a key holder), are an essential part of processing a verifiable credential. At the time of publication, Working Group members had implemented verifiable credentials using at least three proof mechanisms:
  > - Securing Verifiable Credentials using JOSE and COSE [[VC-JOSE-COSE](https://w3c.github.io/vc-data-model/#bib-vc-jose-cose)].
  > - Securing Verifiable Credentials using Data Integrity Proofs [[VC-DATA-INTEGRITY](https://w3c.github.io/vc-data-model/#bib-vc-jose-cose)].
  > - Camenisch-Lysyanskaya Zero-Knowledge Proofs [[CL-SIGNATURES](https://w3c.github.io/vc-data-model/#bib-cl-signatures)].
* [Misinformation Stops Here: W3C VC 2.0 Supports JSON](https://identitywoman.net/misinformation-stops-here-w3c-vc-2-0-supports-json/) 2023-07-21 Kaliya Young 
  > There is one “extra” field that JSON-LD requires/needs which is @context and if you didn’t want to use it and simply wanted to ignore it and just do JSON you could. The VC would be entirely compliant and thus both data expression formats could live in the same specification. JSON-LD credentials that did have an @context that were being read by tooling that just did JSON could still read the credentials – it did nothing to interfere. This seems like a pretty good “let’s figure out how to live with each other” solution. 
* [Draft] [JSON Web Proof](https://www.ietf.org/archive/id/draft-jmiller-jose-json-web-proof-00.html) 2022-07-24 IETF
  > This document defines a new container format similar in purpose and design to JSON Web Signature (JWS) called a JSON Web Proof (JWP). Unlike JWS, which integrity-protects only a single payload, JWP can integrity-protect multiple payloads in one message. It also specifies a new presentation form that supports selective disclosure of individual payloads, enables additional proof computation, and adds a protected header to prevent replay and support binding mechanisms.
* [JSON Web Proof (JWP)](https://hackmd.io/@quartzjer/JSON_Web_Proof) 2021-06-29 QuartzJer
  > A JSON Web Proof (JWP) is very similar to a JWS, with the addition that it can contain multiple individual payloads instead of a singular one. New JWP-supporting algorithms are then able to separate and act on the individual payloads contained within.

## Verifiable Credentials with JSON Web Token (JOSE)
* [Verifiable Credentials Deep Dive](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/decentralized-identity-verifiable-credentials-deep-dive/ba-p/3690641) 2022-12-09 Pamela Dingle, Microsoft
  > A JWT-VC has three parts, and the payload contains what I would call envelope information: the data needed to know who the credential is is bound to, who made the credential, when it was made and how it can be identified.  Additionally, there is a JSON object called “vc”. Claims information is embedded inside the vc object.  A JWT-VC uses an external proof, meaning in this case that signature data is not embedded inline with the credential, the signature is detached from the credential. 
  > ![](https://i.imgur.com/ZBlDL7f.png)
* [Verifiable Credentials Flavors Explained](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf) 2021 CCI Kaliya 'Identity Woman' Young
  > JWT takes a different approach to determining the meaning of claim terms in credentials. There is an [IANA registry for JWT claims](https://www.iana.org/assignments/jwt/jwt.xhtml) as a first place to look for JWT claim definitions. If the claim name isn’t in the IANA register, then the claim can be given a “give it a public name (i.e., a URI), [or] a local name (i.e., any string)”. The meaning of the terms is decided between the issuers and verifiers.
  > 
  > In the VC Implementation Guidelines, there is a long list of the different characterizations of methods: JSON with JWT’s support vs JSON-LD with LD Signatures, [Benefits of JWT](https://www.w3.org/TR/vc-imp-guide/#benefits-of-jwts), [Benefits of JSON-LD and LD-Proofs](https://www.w3.org/TR/vc-imp-guide/#benefits-of-json-ld-and-ld-proofs).
* [JWT vs Linked Data Proofs: comparing Verifiable Credentials](https://medium.com/mattr-global/jwt-vs-linked-data-proofs-comparing-vc-assertion-formats-a2a4e6671d57) 2020-05-7 Nader Helmy, Mattr
  > JWTs have the benefit of already being widely used in today’s identity technologies, most notably in the framework used by OAuth 2.0 and OpenID Connect. Because of this, there are a number of existing software libraries and tools that developers can use immediately to begin building out their implementations. In addition, due to the fact that JWT-based credentials rely on a shared assertion format with existing identity technologies, it may be an easier mental model for newcomers to adopt when starting to experiment with VCs.

### VC-JWT Selective Disclosure
* [Standards Track] [SD-JWT-based Verifiable Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) 2023-08-16 Oliver Terbu, Daniel Fett IETF 
  > JSON Web Tokens (JWTs) [RFC7519] can in principle be used to express Verifiable Credentials in a way that is easy to understand and process as it builds upon established web primitives.
  > 
  > Selective Disclosure JWT (SD-JWT) [I-D.ietf-oauth-selective-disclosure-jwt] is a specification that introduces conventions to support selective disclosure for JWTs: For an SD-JWT document, a Holder can decide which claims to release (within bounds defined by the Issuer).
  > 
  > SD-JWT is a superset of JWT as it can also be used when there are no selectively disclosable claims and also supports JWS JSON serialization, which is useful for long term archiving and multi signatures. However, SD-JWT itself does not define the claims that must be used within the payload or their semantics.
  > 
  > This specification therefore uses SD-JWT and the well-established JWT content rules and extensibility model as basis for representing Verifiable Credentials with JSON payload. Those Verifiable Credentials are called SD-JWT VCs.
* [Selective Disclosure with SD-JWT](https://api-pilot.ebsi.eu/docs/specs/guidelines/selective-disclosure-sd-jwt) 2023
  > The purpose of this guideline is to document how to use SD-JWT with both versions V1.1 and V2.0 of the W3C Verifiable Credentials Data Model (VCDM). The document also covers application of these models in either JSON or JSON-LD format, and methods for protecting them using JWS signatures (compact or JSON serialised).

### VC-JWT Presentation
* [JWT VC Presentation Profile](https://identity.foundation/jwt-vc-presentation-profile/) 2023-08-07 DIF
  > The JWT VC Presentation Profile defines a set of requirements against existing specifications to enable the interoperable presentation of Verifiable Credentials (VCs) between Wallets and Verifiers.
  > 
  > This document is not a specification, but a profile. It outlines existing specifications required for implementations to interoperate among each other. It also clarifies mandatory to implement features for the optionalities mentioned in the referenced specifications.
  > 
  > The profile uses OpenID for Verifiable Presentations (OpenID4VP ID1) as the base protocol for the request and verification of W3C JWT VCs as W3C Verifiable Presentations (VC Data Model v1.1).
* [MDL, JWT-VC, LD-Proofs] [OpenID for Verifiable Presentations](https://openid.net/specs/openid-4-verifiable-presentations-1_0-14.html) 2022-12-30 OpenID
  > This specification defines mechanisms to 
  > - request presentation of Verifiable Credentials in arbitrary formats. 
  > - provide a verifier with one or more Verifiable Presentations in a secure fashion. 
  > - customize the protocol to the specific needs of a particular credential format. Examples are given for credential formats as specified in [VC_DATA], [ISO.18013-5] and [Hyperledger.Indy]. 
  > - combine the credential presentation with user authentication through [SIOPv2]. 
  > - combine the credential presentation with the issuance of OAuth access tokens.
* [Let’s (actually) Share Our Verifiable Credentials - Introducing the JWT VC Presentation Profile](https://medium.com/workday-engineering/lets-actually-share-our-verifiable-credentials-7ab1b4c73079) 2022-07-25 Jen Schreiber, Workday Technology
  > In order to tackle the problem of how we actually share credentials, Workday teamed up with Microsoft, Ping Identity, and MATTR to develop a [specification profile](https://identity.foundation/jwt-vc-presentation-profile) that outlines a list of standards and, once adopted by providers, would enable seamless verification of VCs. Development of the profile continues within the Decentralized Identity Foundation (DIF).
  > 
  > In this blog post, we will give an overview of why specification profiles are required, what this profile involves, and what it means for the adoption of VCs.

### VC-JWT Development
* [GitHub, NPM] [did-jwt-vc](https://github.com/decentralized-identity/did-jwt-vc) 2023-09-04 DIF
  > Create and verify W3C Verifiable Credentials and Presentations in JWT format
* [Web Tool] [Transmute JSON Web Tokens into Verifiable Credentials](https://jwt.vc/)
  > Encoded PASTE A TOKEN HERE
* [Web Tool] [JWT VC Interop Profile](https://vcinteroptesting.azurewebsites.net/) Microsoft
  > Verifiable Credential Issuance and Verifier Sample
* [Web Tool] [VC validator](https://api-pilot.ebsi.eu/docs/tools/vc-validator) EBSI
  > Validate a Verifiable Credential (VC) or a Verifiable Presentation (VP) using the [@cef-ebsi/verifiable-credential](https://api-pilot.ebsi.eu/docs/libraries/verifiable-credential) and [@cef-ebsi/verifiable-presentation](https://api-pilot.ebsi.eu/docs/libraries/verifiable-presentation) libraries.
* [Spec v3] [Open Badges Specification - JSON Web Token Proof Format](https://www.imsglobal.org/spec/ob/v3p0#jwt-proof) 2023-09-08 Open Badges, IMS Global
  > This proof format relies on the well established JWT (JSON Web Token) [RFC7519] and JWS (JSON Web Signature) [RFC7515] specifications. A JSON Web Token Proof is a JWT signed and encoded as a Compact JWS string. The proof format is described in detail in Section 6.3.1 "JSON Web Token" of Verifiable Credentials Data Model v1.1. That description allows several options which may inhibit interoperability. This specification limits the options while maintaining compatibility with [VC-DATA-MODEL] to help ensure interoperability.
* [GitHub] [sd_jwt](https://github.com/kushaldas/sd_jwt) 2022-06-12 Kushaldas
  > This is an implementation of the SD-JWT draft, revision 2.\
  > Do not use it in production yet.
* [GitHub] [kotlin-did-jwt](https://github.com/uport-project/kotlin-did-jwt) 2020-03-21 uPort Project
  > The kotlin-did-JWT library allows you to sign and verify JSON Web Tokens (JWT) using ES256K, and ES256K-R algorithms.

## Verifiable Credentials with Concise Binary Object Representation (COSE)

* [Unofficial Draft] [Verifiable Credentials with CBOR Object Signatures](https://transmute-industries.github.io/vc-cose/) 2023-01-18 Transmute
  > This specification introduces a (Content Type) Header Parameter that is used to define the content type for Verifiable Credentials that utilize CBOR Object Signing to provide signing and verification in a Verifiable Credential.
  > 
  > This approach, of utilizing to a (Content Type) Header Parameter to specify a discrete set of mappings and expected behaviors in translation between formats or representations of data is used commonly in other groups to secure arbitrary content using COSE and other document and data encoding formats. This approach is extensible to other data encodings and may be extended to provide a mechanism for use of CBOR encodings for Verifiable Credentials. 

### CBOR Explainer
* [Why CBOR?](https://www.blockchaincommons.com/introduction/Why-CBOR/) 2022-12-07 Blockchain Commons
  > we have decided to use the IETF CBOR (Concise Binary Object Representation) standard in our specifications, including Gordian Envelope.
  > 
  > We chose CBOR as our serialization format choice for several key reasons
* [Working Group] [Concise Binary Object Representation Maintenance and Extensions (cbor)](https://datatracker.ietf.org/wg/cbor/about/) 2023-06-07
  > Concise Binary Object Representation (CBOR, RFC 7049) extends the JavaScript Object Notation (JSON, RFC 8259) data interchange format to include binary data and an extensibility model, using a binary representation format that is easy to parse correctly. It has been picked up by a number of IETF efforts (e.g., CORE, ANIMA GRASP) as a message format.
* [W3C Editor's Draft] [CBOR-LD 1.0 - A CBOR-based Serialization for Linked Data](https://digitalbazaar.github.io/cbor-ld-spec/) 2022-09-06 Digital Bazaar, 
  > CBOR is a compact binary data serialization and messaging format. This specification defines CBOR-LD 1.0, a CBOR-based format to serialize Linked Data. The encoding is designed to leverage the existing JSON-LD ecosystem, which is deployed on hundreds of millions of systems today, to provide a compact serialization format for those seeking efficient encoding schemes for Linked Data. By utilizing semantic compression schemes, compression ratios in excess of 60% better than generalized compression schemes are possible. This format is primarily intended to be a way to use Linked Data in storage and bandwidth constrained programming environments, to build interoperable semantic wire-level protocols, and to efficiently store Linked Data in CBOR-based storage engines. 
* [RFC 9052] [CBOR Object Signing and Encryption (COSE): Structures and Process](https://www.rfc-editor.org/rfc/rfc9052) 2022-08
  > Concise Binary Object Representation (CBOR) is a data format designed for small code size and small message size. There is a need to be able to define basic security services for this data format. This document defines the CBOR Object Signing and Encryption (COSE) protocol. This specification describes how to create and process signatures, message authentication codes, and encryption using CBOR for serialization. This specification additionally describes how to represent cryptographic keys using CBOR.
* [RFC 9053] [CBOR Object Signing and Encryption (COSE): Initial Algorithms](https://www.rfc-editor.org/rfc/rfc9053)
  > Concise Binary Object Representation (CBOR) is a data format designed for small code size and small message size. There is a need to be able to define basic security services for this data format. This document defines a set of algorithms that can be used with the CBOR Object Signing and Encryption (COSE) protocol (RFC 9052).
* [Compact Credentials](https://learn.mattr.global/docs/vii-platform/compact-credentials/) Mattr
  > CBOR is a binary data format derived from JSON that allows it to utilizes data types like numbers, strings & arrays, however, due to being binary, it offers a much more compact message size. Often when CBOR is being discussed or documented, we can represent the data model using JSON to simplify the way the data can be viewed and modelled. 

### VC-CBOR Development

* ["mDL","eID"] [The Developers’ Dilemma (why mdoc credentials)](https://walt.id/blog/p/mdl-eid-and-beyond) 2023-08-11 WaltID
  > Though, as it is with many new technologies. Before they can reach the masses, they share a common trait: building with them is challenging and time-consuming, which is based on the lack of developer tools making usage easy and implementation quick.
  > 
  > Which is why we build the [mdoc lib](https://github.com/walt-id/waltid-mdoc), as an addition to our open-source identity stack. Proving our commitment to deliver on the latest developments in the industry. Offering tools that let you build compliant solutions across identity ecosystems using different identity flavors with ease, whether that be on- or off-chain identity like Tokens/NFTs,  W3C Verifiable Credentials or now mdoc credentials. mdoc is a binary highly storage efficient credential format leveraging CBOR, standardized through ISO/IEC 18013-5:2021 mDL specification. 
* [@mattrglobal/vc-cwt-verifier](https://www.npmjs.com/package/@mattrglobal/vc-cwt-verifier) NPMJS
  - Verify a credential
  - Verify a credential with a list of trusted issuers
  - Verify a credential skipping expiry and not before checks
  - Provide custom cache for issuer resolution
