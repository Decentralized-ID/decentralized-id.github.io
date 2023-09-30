---
title: "Verifiable Credentials with JSON-LD and Linked Data Proofs"
layout: single
description: An embedded proof is a mechanism where the proof is included in the data model, such as a Data Integrity Proof
excerpt: >
  Starting with the name, JSON-LD stands for JavaScript Object Notation with Linked Data. JSON-LD is a method of encoding linked data using JSON. The term “JSON-LD Credential” alone is somewhat ambiguous but the way it is colloquially used, it means a W3C Verifiable Credential Data Model compliant credential signed using Linked Data Proofs. These are more precisely referred to as ~~Linked Data Proof~~ [Data Integrity Proofs] Verifiable Credentials (LDP-VCs).
header:
  image: "/images/Verifiable-Credentials-Flavors-Explained_JSON-LD_LD-Proof.webp"
  caption: "[[**Verifiable Credentials Flavors Explained**]](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf) 2021 CCI Kaliya 'Identity Woman' Young [[**infographic**]](https://www.lfph.io/wp-content/uploads/2021/04/Verifiable-Credentials-Flavors-Explained-Infographic.pdf)"
  teaser: /images/Verifiable-Credentials-Flavors-Explained_jsonld-lds-teaser.webp
tags: ["W3C","Verifiable Credentials","JSON-LD","Data Integrity"]
categories: ["Verifiable Credentials and Decentralized Identifiers"]
permalink: /web-standards/w3c/verifiable-credentials/data-integrity_ld-proofs/
last_modified_at: 2023-09-29
---

## Main
* [Working Draft] [Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/) 2023-09-02 - Securing the Integrity of Verifiable Credential Data
  >  This specification describes mechanisms for ensuring the authenticity and integrity of Verifiable Credentials and similar types of constrained digital documents using cryptography, especially through the use of digital signatures and related mathematical proofs. Cryptographic proofs enable functionality that is useful to implementors of distributed systems. 
* [Editors Draft] [Verifiable Credentials Data Model v2.0](https://w3c.github.io/vc-data-model/#securing-verifiable-credentials) 2023-09-09
  > This specification recognizes two classes of securing mechanisms: those that use external proofs and those that use embedded proofs. An external proof is one that wraps an expression of this data model, such as via a JSON Web Token, which is elaborated on in the Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE] specification. An embedded proof is a mechanism where the proof is included in the data model, such as a Data Integrity Proof, which is elaborated on in Verifiable Credential Data Integrity [[VC-DATA-INTEGRITY](https://www.w3.org/TR/vc-data-integrity/)].
  > 
  > It should be noted that these two classes of securing mechanisms are not mutually exclusive. 
* [Final Community Group Report] [JSON Web Signature 2020](https://w3c-ccg.github.io/lds-jws2020/) 2022-07-21
  >  This specification describes a JSON Web Signature Suite created in 2020 for the Linked Data Proof specification. The Signature Suite utilizes Detached JWS signatures to provide support for a subset of the digital signature algorithms registered with IANA. 
* [Verifiable data](https://learn.mattr.global/docs/concepts/verifiable-data) 2020-12-12 Mattr
  > Verifiable credentials make use of JSON-LD to extend the data model to support dynamic data vocabularies and schemas. This allows us to not only use existing JSON-LD schemas, but to utilize the mechanism defined by JSON-LD to create and share new schemas as well. To a large extent this is what JSON-LD was designed for; the adoption and reuse of common data vocabularies.
  > 
  > This type of verifiable credential is best characterised as a kind of Linked Data Proof. It allows issuers to make statements that can be shared without loss of trust because their authorship can be verified by a third party.

## About
* [Linked Data Proofs - A new pathway for verifiable credentials](https://www.linkedin.com/pulse/linked-data-proofs-new-pathway-verifiable-credentials-gokul-alex) 2023-05-13 Gokul Alex
  > It is portable because it provides a standard vocabulary. JSON-LD configuration files are human readable unlike the JWT. Data schema emerge as important paradigms in this model. VCs based on Linked Data Proofs use Linked Data Signatures for security. They are more granular as they are attribute based rather than credential based.
* [Five Things You Need to Know About JSON-LD Credentials in Hyperledger Aries Cloudagent Python](https://indicio.tech/five-things-you-need-to-know-about-json-ld-credentials-in-hyperledger-aries-cloudagent-python/) 2022-12-07 Tim Spring, Indicio
  > Starting with the name, JSON-LD stands for JavaScript Object Notation with Linked Data. JSON-LD is a method of encoding linked data using JSON. The term “JSON-LD Credential” alone is somewhat ambiguous but the way it is colloquially used, it means a W3C Verifiable Credential Data Model compliant credential signed using Linked Data Proofs. These are more precisely referred to as Linked Data Proof Verifiable Credentials (LDP-VCs).
* [Verifying Verifiable Credentials](https://grotto-networking.com/blog/posts/jsonldProofs.html) 2022-11-11 Grotto Networking
  > A number of specifications and emerging specifications explain and specify how VCs can be “secured”. Here we will look at the “digital signing” of VCs and draw upon the following specifications:
  > - Verifiable Credential Data Integrity 1.0 Securing the Integrity of Verifiable Credential Data Latest as of October 2022.
  > - JSON-LD Website
  > - JSON-LD 1.1 A JSON-based Serialization for Linked Data, W3C Recommendation 16 July 2020.
  > - EdDSA Cryptosuite v2020 Draft Community Group Report 31 October 2022
* [notes] [Verifiable Credentials & Linked Data Proofs](https://hackmd.io/@animo/HJn4Mioku) 2021-04-01
  > Linked Data Proofs provide a mechanism to for ensuring the authenticity and integrity of Linked Data documents using mathematical proofs.
  * [Notes on Linked Data Proofs](https://hackmd.io/inzaVCAtSdWQxzmw8doNGg) 2021-01-24
    > Linked Data Proofs can be used to:
    > - Make statements without the loss of trust (e.g. VCs or social media posts)
    > - Authenticate an entity is identified by a certain identifier (e.g. DIDs)
    > - Delegate authorization for actions to remote environments (e.g. ZCAP-LD)
    > - Agree to contracts (where agreement can be verified by other parties)
    > - Integrity protection (e.g. making document tamper-evident)
* [Verifiable Credentials Flavors Explained](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf) 2021 CCI Kaliya 'Identity Woman' Young [Presentation](https://www.slideshare.net/Kaliya/verifiable-credentials-explained-by-cci)
  > In the VC Implementation Guidelines, there is a long list of the different characterizations of methods: JSON with JWT’s support vs JSON-LD with LD Signatures, [Benefits of JWT](https://www.w3.org/TR/vc-imp-guide/#benefits-of-jwts), [Benefits of JSON-LD and LD-Proofs](https://www.w3.org/TR/vc-imp-guide/#benefits-of-json-ld-and-ld-proofs).
  > 
  > To summarize the most salient points:
  > 
  > JSON is an older standard, officially recognized as a standard in 2013. JSON-LD 1.0 was formally standardized in 2014. The version and standard was updated to JSON-LD 1.1 and ratified in 2020.
  > 
  > That being said, one can use JSON libraries to process JSON-LD objects/documents, and conversely, [interpret JSON documents as JSON-LD](https://www.w3.org/TR/json-ld11/#interpreting-json-as-json-ld) by providing a context.
* [JWT vs Linked Data Proofs: comparing Verifiable Credentials](https://medium.com/mattr-global/jwt-vs-linked-data-proofs-comparing-vc-assertion-formats-a2a4e6671d57) 2020-05-7 Nader Helmy, Mattr
  > Linked Data Signatures provide a simple security protocol which is native to JSON-LD. They are built to compactly represent proof chains and allow a VC to be easily protected on a more granular basis; per-attribute, instead of per-credential. These features support a much more robust security model which has broader implications downstream from VCs, especially in terms of size and efficiency.

## Development

* [MDL, JWT-VC, LD-Proofs] [OpenID for Verifiable Presentations](https://openid.net/specs/openid-4-verifiable-presentations-1_0-ID2.html#name-ldp-vcs) 2022-12-30 OpenID
  > This specification defines mechanisms to 
  > - request presentation of Verifiable Credentials in arbitrary formats. 
  > - provide a verifier with one or more Verifiable Presentations in a secure fashion. 
  > - customize the protocol to the specific needs of a particular credential format. Examples are given for credential formats as specified in [VC_DATA], [ISO.18013-5] and [Hyperledger.Indy]. 
  > - combine the credential presentation with user authentication through [SIOPv2]. 
  > - combine the credential presentation with the issuance of OAuth access tokens.