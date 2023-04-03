---
date: 2019-03-03
title:  Web Standards and the Emerging Decentralized ID Stack
excerpt: >
  If you’re willing to put up with a lot of work for incremental improvements then step up and join a standard. Whether that is a (relatively) fast moving standard group like OASIS (www.oasis-open.org) or a slower but more international group like ISO you will learn. You’ll also benefit from working with experts. These experts donate their time and are more than happy to provide ideas, guidance, and leadership.
layout: single
permalink: web-standards/
canonical_url: 'https://decentralized-id.com/web-standards/'
redirect_from: 
  - standards
  - standards/
  - specs-standards/
categories: ["Web Standards"]
tags: ["W3C","Credentials Community Group","Hyperledger Foundation","FIDO","OpenID","XDI","OASIS","JSON-LD","Verifiable Credentials","Ethereum","Blockcerts","OAuth","OIDC","DKMS","ERC725","Rebooting WoT","Schema.org","Learning Machine"]
last_modified_at: 2022-12-16
header: 
  og_image: /images/Who-Runs-the-Internet-graphic.webp
---

Check out this [twitter list](https://twitter.com/i/lists/1322229268252950531) I made for identity related standards development bodies.

## Big Picture
* [Why Engage with Standards?](https://www.continuumloop.com/why-engage-with-standards/)
  > too many people complain about problems but don’t step to Fix It!. There are certainly a lot of flawed standards – but they make interoperability possible – not perfect – but possible. If you haven’t used them then you have no right to complain that they are too complex, too simple (even in the same standard) or too domain specific – or any of the other rants and raves that go on.
  > 
  > If you’re willing to put up with a lot of work for incremental improvements then step up and join a standard. Whether that is a (relatively) fast moving standard group like OASIS (www.oasis-open.org) or a slower but more international group like ISO you will learn. You’ll also benefit from working with experts. These experts donate their time and are more than happy to provide ideas, guidance, and leadership.
* [Who Are the Identerati? - ForgeRock](https://www.forgerock.com/blog/who-are-the-identerati)
  > You’re familiar with digital identity standards like OpenID Connect, OAuth, and User-Managed Access, fundamental elements of privacy and security on the internet. But have you ever wondered how they came to be? A lot of work on these protocols went on (and goes on) behind the scenes at the Internet Identity Workshop (IIW), a bi-annual gathering of identity experts where we work on improving the identity systems that make the web run. It’s a great event that’s flown under the radar, so I’m excited to share a new documentary on IIW,  “Not Just Who They Say We Are: Claiming our identity on the Internet”. This short film shines a light on the stealth community of “Identerati” at IIW that are defining and refining digital identity.
* [Manifesto: Rules for standards-makers](http://scripting.com/2017/05/09/rulesForStandardsmakers.html) by Dave Winer
  > I've used all kinds of formats and protocols in a long career as a software developer, even created a few. My new manifesto summarizes what I've learned about what works and what doesn't.

{% include figure image_path="/images/Who-Runs-the-Internet-graphic.webp" alt="https://es.wikipedia.org/wiki/Archivo:Who-Runs-the-Internet-graphic.png" caption="[*Internet Governance*](https://en.wikipedia.org/wiki/Internet_governance)" %}

## Decentralized Identity Stack

* [**Hyperledger Identity Working Group - Identity Standards**](https://wiki.hyperledger.org/display/IWG/Identity+Standards)
* [**_A Taxonomic Approach to Understanding Emerging Blockchain Identity Management Systems_**](https://arxiv.org/pdf/1908.00929.pdf) NIST CYBERSECURITY WHITE PAPER (DRAFT) BLOCKCHAIN IDENTITY MANAGEMENT APPROACHES JULY 9, 2019
  > Identity management systems (IDMSs) are widely used to provision user identities while managing authentication, authorization, and data sharing both within organizations as well as on the Internet more broadly. Traditional identity systems typically suffer from single points of failure, lack of interoperability, and privacy issues such as encouraging mass data collection and user tracking. Blockchain technology has the potential to support novel data ownership and governance models with built-in control and consent mechanisms, which may benefit both users and businesses by alleviating these concerns; as a result, blockchain-based IDMSs are beginning to proliferate. This work categorizes these systems into a taxonomy based on differences in architecture, governance models, and other salient features. We provide context for the taxonomy by describing related terms, emerging standards, and use cases, while highlighting relevant security and privacy considerations.
* [Building Blocks for a New Architecture](https://medium.com/@trbouma/building-blocks-for-a-new-architecture-fda2238ac005) by Tim Bouma
  > First, you will see the Issuer, Holder and Verifier. This is the archetypal pattern of the decentralized architecture. An issuer issues something to a holder, who then presents it to a verifier, who make a decision. A simple example: government(issuer) issues you a passport (holder), which you present to a border control officer (verifier) who lets you through the gate. When you look at all the use cases (described above), they all fall into this pattern.\
  >![](https://i.imgur.com/qGXEnW1.png)
* [The Self-Sovereign Identity Stack by Oliver Terbu OSI](https://medium.com/decentralized-identity/the-self-sovereign-identity-stack-8a2cc95f2d45)
  > | Layer | Examples |
  > | --- | --- |
  > | Application | Selective Disclosure, music app, rideshare service, extensions, etc. |
  > | Implementation | DIF Hubs, Indy Agents, uPort app, etc. |
  > | Payload | JSON-LD, JWT, CWT |
  > | Encoding | ProtoBuf, Cap'n Proto, MessagePack, JSON, CBOR, etc. | 
  > | Encryption | Ciphersuite, JWE, etc. |
  > | DID AuthN | Key ownership, verification, challenge/response, etc. | 
  > | Transport | QR Code, HTTP, BLE, NFC, FTP, SMTP, etc. |
  > | DID Resolution | DID -> DID Doc / service and key resolution | 
  > | DID Operations | CRUD support for a DID Doc | 
  > | Storage | Optional, separate storage of DID metadata |
  > | Anchor | Bitcoin, Ethereum, Veres One, Sovrin, etc. |  
* [Overview of Decentralized Identity Standards](https://medium.com/decentralized-identity/overview-of-decentralized-identity-standards-f82efd9ab6c7), Nader Helmy
  > we can think of each specification as addressing one or more of the SSI “building blocks” that we described above. In some cases a standard may be a bridge between layers, enabling a closer link between connections, data, and keys, making the ecosystem more secure as a whole. What you will find below is a list of all relevant standards, links to every specification, the organizations they belong to, their relationship to the ecosystem, and their relative maturity as internet technologies.
  > {% gist c8a20c534d3cf8f65a9b34ce2ad81725 Decentralized%20Identity%20Standards.md %}
- [Distributed ID learning path](https://translate.google.com/translate?sl%3Dauto%26tl%3Den%26u%3Dhttps://kristinayasuda.com/posts/decentralized-identity-catch-up-path/) – [Christina Yasuda](https://twitter.com/kristinayasuda) (from work navigating the [VC-Spec Map](https://github.com/decentralized-identity/vc-spec-map))
  > Describes pre-requisite knowledge, including JSON, JSON-LD, JWT, JWS, JWK, JWA, and sometimes CBOR. She then goes on to break down knowledge areas beginning with the basics: DID-Core, DID-Resolution, DID-Spec, DID Use-Cases. Next, she covers Verifiable Credentials with VC-Data Model, VC Use-Cases, and VC-Implementors Guide, and also Transport, Credential Presentation, and Other Data Formats.
- [The Flavors of Verifiable Credentials](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf)  – [Linux Foundation Public Health Blog](https://www.google.com/url?q=https://www.lfph.io/2021/02/11/cci-verifiable-credentials-flavors-and-interoperability-paper/&sa=D&source=editors&ust=1618469203874000&usg=AOvVaw15dEyc58aXz83CrftEoj4Z).
  > The differences between the different flavors of VCs for technically inclined readers. It elaborated on the differences between JSON and JSON-LD and articulated differences between the two different implementations of ZKP style credentials. The ‘Journey of a VC’ section articulated all steps where VCs are active and highlighted the differences in how different VC flavors ’behave’.

[![](https://imgur.com/6MLNgXal.png)](https://www.youtube.com/watch?v=RllH91rcFdE)\
<sup><a href="https://www.youtube.com/watch?v=RllH91rcFdE">The Story of Open SSI Standards - Drummond Reed/Evernym SSIMeetup.org</a>[<b><a href="https://www.slideshare.net/SSIMeetup/self-sovereign-identity-ssi-open-standards-with-drummond-reed">ϟ</a></b>]</sup>

### Learn
- [Anonymous Credential Part 1: Brief Overview and History](https://medium.com/finema/anonymous-credential-part-1-brief-overview-and-history-c6679034c914) – Finema
  > An anonymous credential (Anoncred), which is also known as an attribute-based credential (ABC), is a concept for a digital credential that provides a credential holder maximal privacy and an ability to selectively disclose their personal information.
- [Anonymous Credential Part 2: Selective Disclosure and CL Signature](https://medium.com/finema/anonymous-credential-part-2-selective-disclosure-and-cl-signature-b904a93a1565) – Finema
  > selective disclosure and an anonymous credential (Anoncred) relies on an efficient signature scheme that supports multiple messages with a single signature. One such signature scheme is known as CL signature that is named after Jan Camenisch and Anna Lysyanskaya […] CL signature popularized Anoncreds, and it also served as a cryptographic building block in Identity Mixer (Idemix) and Hyperledger Indy projects.
- [Anonymous Credential Part 3:](https://medium.com/finema/anonymous-credential-part-3-bbs-signature-26797721ca74-gw1VZGjA3wNv) [BBS+ Signature](https://medium.com/finema/anonymous-credential-part-3-bbs-signature-26797721ca74-gw1VZGjA3wNv) – Finema
  > Compared to the CL signature, the BBS+ signature has much shorter keys and signatures for a comparable level of security. As a result, the BBS+ signature enables fast implementation for anonymous credentials. It can be used in combination with signature proof of knowledge to hide some of credential attributes/messages in a zero-knowledge fashion.
- [Web of Trust 101](https://medium.com/mattr-global/learn-concepts-web-of-trust-101-77120941ea6c) – Mattr
  > The emerging “Web of Trust” is an idea that has been around since the dawn of the internet. To explain what motivated its creation, let’s take a look at how trust on the internet functions today.
- [Verifiable Data](https://medium.com/mattr-global/learn-concepts-verifiable-data-4515a62c8e40) – Mattr (and Verifiable Relationships, Verifiable Processes, Verifiable Credentials, Semantics and Schemas)
  > refers to the authenticity and integrity of the actual data elements being shared.
- [Semantic Web](https://medium.com/mattr-global/learn-concepts-semantic-web-250784d6a49f) – Mattr
  > The semantic web is a set of technologies whose goal is to make all data on the web machine-readable. Its usage allows for a shared understanding around data that enables a variety of real-world applications and use cases.
- [Selective Disclosure](https://medium.com/mattr-global/learn-concepts-selective-disclosure-4b9bf4e5c887) – Mattr
  > An important principle that we want to achieve when designing any system that involves handling Personally Identifiable Information (PII) is to minimize the data disclosed in a given interaction. When users share information, they should be able to choose what and how much they share on a case-by-case basis
- [Trust Frameworks](https://medium.com/mattr-global/learn-concepts-trust-frameworks-ad96a4427991) – Mattr
  > Trust frameworks are a foundational component of the web of trust. A trust framework is a common set of best practice standards-based rules that ensure minimum requirements are met for security, privacy, identification management and interoperability through accreditation and governance.
- [Beginners Guide to JWTs](https://developer.okta.com/blog/2020/12/21/beginners-guide-to-jwt) – Okta
  > A JWT is a structured security token format used to encode JSON data. The main reason to use JWT is to exchange JSON data in a way that can be cryptographically verified. There are two types of JWTs:JSON Web Signature (JWS)JSON Web Encryption (JWE)The data in a JWS is public—meaning anyone with the token can read the data—whereas a JWE is encrypted and private. To read data contained within a JWE, you need both the token and a secret key.
- [Verifiable Credentials Issuance](https://blockster.global/self-sovereign-identity/) – Blockster
  > When an issuer creates a verifiable credential, it contains following information:
  > 
  > - Who has issued – DID of the Issuer
  > - To whom it is issued – User Identifier
  > - Attributes of the credential – Details of the credential being Issued
  > - When it is Issued – Date of issuance


## Assorted
### NIST

- [FIPS PUB 201-3 (DRAFT) Federal Information Processing Standards Publication](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.201-3-draft.pdf) (Supersedes FIPS 201-2) 
  > Personal Identity Verification (PIV) of Federal Employees and Contractors

### Decentralized Key Management

<img src="https://i.imgur.com/0SLcjUv.png"/>

* [Decentralized Key Management (DKMS): An Essential Missing Piece of the SSI Puzzle - Drummond Reed](https://www.slideshare.net/SSIMeetup/decentralized-key-management-dkms-an-essential-missing-piece-of-the-ssi-puzzle-drummond-reed)
* [Recommendations for Decentralized Key Management Systems](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/dkms-recommendations.md)

![](https://i.imgur.com/5qc1qrG.png)\
<sup><a href="http://ssimeetup.org/decentralized-key-management-dkms-essential-missing-piece-ssi-puzzle-drummond-reed-webinar-8/">DKMS - An Essential Missing Piece of the SSI Puzzle. Drummond Reed. SSIMeetup.org</a></sup>

* [Agent to Agent Communication](https://drive.google.com/file/d/1PHAy8dMefZG9JNg87Zi33SfKkZvUvXvx/view): Daniel Hardman explains the goals of agent to agent communication
