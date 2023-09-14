---
title: "Verifiable Credentials with JSON-LD + Data-Integrity Proofs (Linked Data Proofs / BBS)"
layout: single
description: An embedded proof is a mechanism where the proof is included in the data model, such as a Data Integrity Proof
excerpt: >
  Starting with the name, JSON-LD stands for JavaScript Object Notation with Linked Data. JSON-LD is a method of encoding linked data using JSON. The term “JSON-LD Credential” alone is somewhat ambiguous but the way it is colloquially used, it means a W3C Verifiable Credential Data Model compliant credential signed using Linked Data Proofs. These are more precisely referred to as ~~Linked Data Proof~~ [Data Integrity Proofs] Verifiable Credentials (LDP-VCs).
header:
  image: "/images/Verifiable-Credentials-Flavors-Explained_jsonld-data-integrity_lds_bbs+.webp"
  caption: "[[**Verifiable Credentials Flavors Explained**]](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf) 2021 CCI Kaliya 'Identity Woman' Young [[**infographic**]](https://www.lfph.io/wp-content/uploads/2021/04/Verifiable-Credentials-Flavors-Explained-Infographic.pdf)"
  teaser: /images/Verifiable-Credentials-Flavors-Explained_jsonld-lds-teaser.webp
tags: ["W3C","Verifiable Credentials","JSON-LD","LD-Proof","Data Integrity","BBS"]
categories: ["Verifiable Credentials and Decentralized Identifiers"]
permalink: /web-standards/w3c/verifiable-credentials/data-integrity_ld-proofs+bbs/
last_modified_at: 2023-09-09
---

## Main
* [Working Draft] [Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/) 2023-09-02 - Securing the Integrity of Verifiable Credential Data
  >  This specification describes mechanisms for ensuring the authenticity and integrity of Verifiable Credentials and similar types of constrained digital documents using cryptography, especially through the use of digital signatures and related mathematical proofs. Cryptographic proofs enable functionality that is useful to implementors of distributed systems. 
* [Editors Draft] [Verifiable Credentials Data Model v2.0](https://w3c.github.io/vc-data-model/#securing-verifiable-credentials) 2023-09-09
  > This specification recognizes two classes of securing mechanisms: those that use external proofs and those that use embedded proofs. An external proof is one that wraps an expression of this data model, such as via a JSON Web Token, which is elaborated on in the Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE] specification. An embedded proof is a mechanism where the proof is included in the data model, such as a Data Integrity Proof, which is elaborated on in Verifiable Credential Data Integrity [[VC-DATA-INTEGRITY](https://www.w3.org/TR/vc-data-integrity/)].
  > 
  > It should be noted that these two classes of securing mechanisms are not mutually exclusive. 
* [BBS+, Data Integrity] [Formalising Linked-Data based Verifiable Credentials for Selective Disclosure](https://sako-lab.jp/download.php?article=ssr2022_proceedings_dan.pdf) 2022 Dan Yamamoto, Yuji Suga, Kazue Sako IEEE
  > Abstract—In this paper, we propose a formal definition for Linked-Data based verifiable credential to enable secure selective disclosure among one or multiple verifiable credentials a user has. Previous schemes considered using a single verifiable credential and could not hide the user’s identifying information when performing selective disclosure. We propose the first Linked-Data based verifiable credentials that can perform selective disclosure free from the restrictions the previous scheme had, and prove its property. We also discuss a novel use of combining multiple certificates issued by independent issuers to still allow users to perform selective disclosure on the set of credentials. Our scheme has been implemented as an open source Web-based application that generates a verifiable presentation for a given selection of attributes. The performance evaluation is also provided in the paper.
* [Final Community Group Report] [JSON Web Signature 2020](https://w3c-ccg.github.io/lds-jws2020/) 2022-07-21
  >  This specification describes a JSON Web Signature Suite created in 2020 for the Linked Data Proof specification. The Signature Suite utilizes Detached JWS signatures to provide support for a subset of the digital signature algorithms registered with IANA. 

## Verifiable Credentials with Linked Data Proofs
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
* [Verifiable data](https://learn.mattr.global/docs/concepts/verifiable-data) 2020-12-12 Mattr
  > Verifiable credentials make use of JSON-LD to extend the data model to support dynamic data vocabularies and schemas. This allows us to not only use existing JSON-LD schemas, but to utilize the mechanism defined by JSON-LD to create and share new schemas as well. To a large extent this is what JSON-LD was designed for; the adoption and reuse of common data vocabularies.
  > 
  > This type of verifiable credential is best characterised as a kind of Linked Data Proof. It allows issuers to make statements that can be shared without loss of trust because their authorship can be verified by a third party.
* [JWT vs Linked Data Proofs: comparing Verifiable Credentials](https://medium.com/mattr-global/jwt-vs-linked-data-proofs-comparing-vc-assertion-formats-a2a4e6671d57) 2020-05-7 Nader Helmy, Mattr
  > Linked Data Signatures provide a simple security protocol which is native to JSON-LD. They are built to compactly represent proof chains and allow a VC to be easily protected on a more granular basis; per-attribute, instead of per-credential. These features support a much more robust security model which has broader implications downstream from VCs, especially in terms of size and efficiency.

## LD-Proofs Development

* [MDL, JWT-VC, LD-Proofs] [OpenID for Verifiable Presentations](https://openid.net/specs/openid-4-verifiable-presentations-1_0-ID2.html#name-ldp-vcs) 2022-12-30 OpenID
  > This specification defines mechanisms to 
  > - request presentation of Verifiable Credentials in arbitrary formats. 
  > - provide a verifier with one or more Verifiable Presentations in a secure fashion. 
  > - customize the protocol to the specific needs of a particular credential format. Examples are given for credential formats as specified in [VC_DATA], [ISO.18013-5] and [Hyperledger.Indy]. 
  > - combine the credential presentation with user authentication through [SIOPv2]. 
  > - combine the credential presentation with the issuance of OAuth access tokens.
* [Verifiable Credentials Data Integrity Naming Conventions](https://socialhub.activitypub.rocks/t/verifiable-credentials-data-integrity-naming-conventions/3421/1) 2023-07-17 SocialHub 
  > Basically, the question boils down to: If you read __ eddsa-jcs-2022__, do you understand that it is about signing with an Edwards curve based algorithm after normalizing the data with the JSON Canonicalization Scheme?
  > 
  > Note: Edwards Curve + JCS is not enough to build an algorithm. There’s at least a hashing algorithm missing (and specifying the curve 25519). For details see here 1

## Verifiable Credentials with JSON-LD + BBS+ Signatures
* [Verifiable Credentials Flavors Explained](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf) 2021 CCI Kaliya 'Identity Woman' Young
  > JSON-LD ZKP with BBS+ Signatures. This approach to VCs is innovative because it brings together different elements from several of the existing approaches to VCs. It is based on the usage of [BBS+ JSON-LD Signatures](https://github.com/mattrglobal/jsonld-signatures-bbs), which is a subclass of [LD Signatures](https://w3c-ccg.github.io/ld-proofs/), in combination with a JSON-LD credential schema. The cryptography behind this mechanism is BBS+ Signatures, which require what’s called a pairing-friendly curve. Existing implementations in the VC ecosystem use the elliptic curve BLS12–381
* [BBS+, JSON-LD and Interoperability of Verifiable Credentials](https://medium.com/coinmonks/bbs-json-ld-and-interoperability-of-verifiable-credentials-8bd26b4d3261) 2021-06-20 Coinmonks
  > In order to request attributes from the credentials JSON-LD frames are used. The credentials and the proofs created by BBS+ signatures are self-describing and do not require a ledger(unlike CL signature based systems like Hyperledger Indy).
* [Working Draft] [BBS Cryptosuite v2023 - Securing Verifiable Credentials with Selective Disclosure using BBS Signatures](https://www.w3.org/TR/vc-di-bbs/) 2023-05-24 W3C 
  >  This specification defines a set of cryptographic suites for the purpose of creating, verifying and deriving proofs for BBS+ Signatures in conformance with the Data Integrity [VC-DATA-INTEGRITY] specification.
  > 
  > In general the suites uses the RDF Dataset Normalization Algorithm [RDF-DATASET-NORMALIZATION] to transform an input document into its canonical form. It then uses the statement digest algorithm to digest each statement to be signed individually, finally the digested statements are signed using the defined signature algorithm.
  > 
  > BBS+ signatures [CFRG-BBS-SIGNATURE] are compatible with any pairing friendly elliptic curve, however the cryptographic suites defined in this document elect to only allow the usage of the BLS12-381 for interoperability purposes. 
* [Literature] [Revisiting BBS Signatures](https://eprint.iacr.org/2023/275.pdf) 2023, Stefano Tessaro and Chenzhi Zhu
  > BBS signatures were implicitly proposed by Boneh, Boyen, and Shacham (CRYPTO ’04) as part of their group signature scheme, and explicitly cast as stand-alone signatures by Camenisch and Lysyanskaya (CRYPTO ’04). A provably secure version, called BBS+, was then devised by Au, Susilo, and Mu (SCN ’06), and is currently the object of a standardization effort which has led to a recent RFC draft. BBS+ signatures are suitable for use within anonymous credential and DAA systems, as their algebraic structure enables efficient proofs of knowledge of message-signature pairs that support partial disclosure.
  > 
  > BBS+ signatures consist of one group element and two scalars. As our first contribution, we prove that a variant of BBS+ producing shorter signatures, consisting only of one group element and one scalar, is also secure. The resulting scheme is essentially the original BBS proposal, which was lacking a proof of security. Here we show it satisfies, under the q-SDH assumption, the same provable security guarantees as BBS+. We also provide a complementary tight analysis in the algebraic group model, which heuristically justifies instantiations with potentially shorter signatures.
* [SSI Essentials: Zero Knowledge Proof (ZKP) and Selective Disclosure, till death do us part?](https://gataca.io/blog/ssi-essentials-which-selective-disclosure-protocol-will-succeed/) 2022-01-23 Gataca
  > Selective disclosure via BBS+ signatures [...]
  >
  > Like monoclaim credentials allow users to share specific claims from a VC, BBS+ Signatures is a multi-message digital signature scheme (named after its creators Boneh, Boyen, and Shacham) that gives users the possibility of sharing VCs with only specific attributes revealed. How does it work?
  > 
  > BBS+ signatures allow a VC holder to derive proofs from the original signature:
  > - Deriving a proof: When a holder takes the signed VC and hides one, several, or none of the containing claims, creating a new signature (a derived proof) using the Issuer's public key. This derived proof can prove that the holder knows all of the original claims contained in the VC but chooses only to reveal the required ones.
  > - Verifying a proof: The verifier validates the derived proof using the Issuer's public key. This process enables the verifier to confirm the validity of the proof, proving that the subset of claims was part of an original message signed by the Issuer.
* [Why the Verifiable Credentials Community Should Converge on BBS+](https://www.evernym.com/blog/bbs-verifiable-credentials/) 2021-03-24 Evernym
  > BBS+ LD-Proofs use JSON-LD schemas, so credentials that use them can have a rich, hierarchical set of attributes. Instead of the heavy-handed mechanism for the encoding and canonicalization of attributes values that we’d imagined for Rich Schemas, they use RDF canonicalization and a hash function. Rather than expanding the credential definition, they discarded it, taking advantage of some properties of BBS+ keys which allow for deterministic expansion. 

### VC with BBS+ Development
* [Code] [jsonld-signatures-bbs](https://www.npmjs.com/package/@mattrglobal/jsonld-signatures-bbs) 2022-12-18 Mattr Global, NPMJS
  > The following repository contains a linked data proof implementation for creating BBS+ Signatures using BLS12-381 key pairs.
  > 
  > Due to the properties of a BBS+ Signatures, zero knowledge proof can be derived from the signature, where-by the party generating the proof can elect to selectively disclose statements from the originally signed payload.
* [GitHub] [bbs-signatures](https://github.com/mattrglobal/bbs-signatures) 2022-12-21 Mattr Global
  > BBS+ Signatures are a digital signature algorithm originally born from the work on Short group signatures by Boneh, Boyen, and Shachum which was later improved on in Constant-Size Dynamic k-TAA as BBS+ and touched on again in section 4.3 in Anonymous Attestation Using the Strong Diffie Hellman Assumption Revisited .
  > 
  > BBS+ signatures require a pairing-friendly curve, this library includes support for BLS12-381.
  > 
  > BBS+ Signatures allow for multi-message signing whilst producing a single output signature. With a BBS signature, a proof of knowledge based proof can be produced where only some of the originally signed messages are revealed at the discretion of the prover.
* [GitHub] [jsonld-signatures-bbs](https://github.com/mattrglobal/jsonld-signatures-bbs) Mattr Global
  > The following repository contains a linked data proof implementation for creating BBS+ Signatures using BLS12-381 key pairs.
  > 
  > Due to the properties of a BBS+ Signatures, zero knowledge proof can be derived from the signature, where-by the party generating the proof can elect to selectively disclose statements from the originally signed payload.
  > 
  > This library is runnable in browser and Node.js through the WASM based crypto implementation provided by bbs-signatures. Note bbs-signatures also has an optional dependency on node-bbs-signatures which can be used when running in Node.JS environments to obtain better performance. For environments that do not feature WASM support such as react native, bbs-signatures includes an automatic roll back to an asm.js version but note however the performance difference between asm.js and WASM is significant, for those inclined there are runnable benchmarks in bbs-signatures.
* [GitHub] [jsonld-signatures-bbs](https://github.com/zkp-ld/jsonld-signatures-bbs) 2023-02-23 ZKP-LD
  > Experimental: do not use in production
  > - Based on MATTR's jsonld-signatures-bbs
  > - Supports termwise selective disclosure, proof of termwise equality, and credential aggregation
  > - dependencies upgraded
  > - WASM only; Neon is currently not supported
* [GitHub] [bbs-signatures](https://github.com/zkp-ld/bbs-signatures) ZKP-LD
  > Experimental: do not use in production
  > - Based on MATTR's bbs-signatures
  > - Supports termwise selective disclosure, proof of termwise equality, and credential aggregation
  > - WASM only; Neon is currently not supported
* [Implement Compound Proof BBS+ verifiable credentials using ASP.NET Core and MATTR](https://damienbod.com/2021/12/13/implement-compound-proof-bbs-verifiable-credentials-using-asp-net-core-and-mattr/) 2021-12-13 damienbod
  > This article shows how Zero Knowledge Proofs BBS+ verifiable credentials can be used to verify credential subject data from two separate verifiable credentials implemented in ASP.NET Core and MATTR. The ZKP BBS+ verifiable credentials are issued and stored on a digital wallet using a Self-Issued Identity Provider (SIOP) and OpenID Connect. A compound proof presentation template is created to verify the user data in a single verify.
  > 
  > Code: https://github.com/swiss-ssi-group/MattrAspNetCoreCompoundProofBBS