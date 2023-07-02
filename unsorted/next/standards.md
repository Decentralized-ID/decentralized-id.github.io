---
published: false
---

# Web Standards

## Explainers
* [The Time for Self-Sovereign Identity is Now](https://medium.com/learning-machine-blog/the-time-for-self-sovereign-identity-is-now-222aab97041b) Kim Hamilton Duffy, Learning Machine (Now Hyland Credentials)
Oldie but Goodie by Kim Hamilton Duffy from when she worked at Learning Machines
  > Technically, Verifiable Claims are claims made about a “subject” (identified by a digital identifier such as a DID) that are rendered tamper proof through digital signatures. The authenticity of digital signatures may, in turn, be established through issuer identifiers, which may also be expressed as DIDs.
* [Decentralized identity: What it is, why it matters](https://www.scmagazine.com/resource/identity-and-access/infographic-key-stats-on-the-passwordless-future) 2022-09-15 SC Magazine
  > ![](https://www.scmagazine.com/_next/image?url=https%3A%2F%2Ffiles.scmagazine.com%2Fwp-content%2Fuploads%2F2022%2F08%2FPingDecentralizedIdentity-4.jpg&w=750&q=75)
* [The Journey of Decentralized Identity: Where It’s Been and Where It’s Going](https://trinsic.id/the-journey-of-decentralized-identity-where-its-been-and-where-its-going/) 2022-07-14 Trinsic
  > Our goal has been to completely abstract away the complexity of the ever-changing landscape so organizations can focus on the important stuff—what product to build, and how to take it to market. Teams shouldn’t have to “pick winners” and wager what to build on. Their products should be interoperable with multiple ecosystems. That’s what Trinsic is providing, out-of-the-box.

## DIDs
* [https://www.w3.org/2019/did-wg/](https://www.w3.org/2019/did-wg/) - Website
* [https://lists.w3.org/Archives/Public/public-did-wg/](https://lists.w3.org/Archives/Public/public-did-wg/) - LIst Archives

W3C Press Release - [Decentralized Identifiers (DIDs) v1.0 becomes a W3C Recommendation](https://www.w3.org/2022/07/pressrelease-did-rec) worth reading to see who contributed comments (and notice who didn’t)

For individuals in particular, DIDs can put them back in control of their personal data and consent, and also enable more respectful bi-directional trust relationships where forgery is prevented, privacy is honored, and usability is enhanced.
* [DID, in short for Decentralized Identifier, is basically a unique string of random numbers and letters](https://twitter.com/fennykyun/status/1564249472053514240) fennykyun
  > tldr\
  > :: DID is just an URI\
  > :: VC is a cryptographically verifiable credential using DID\ 
  > :: SSI is a self-sovereign and privacy-preserving identity 
  > :: Non-human (Machines, Bots, Goods, anything) also able to have DID, VC, and SSIs
* [Decentralized identifiers - Self-Sovereign Identity livebook](https://livebook.manning.com/book/self-sovereign-identity/chapter-8/) Manning
* [Video] [Identity Insights - Basics of Verifiable Credentials](https://www.youtube.com/watch?v=RCCatllgNv4) Indicio, Youtube
  > What are verifiable credentials? In this episode we are joined by Indicio software engineer Char Howland for an introduction to what this technology is and what it can do.

* <a href="https://github.com/decentralized-identity/did-common-typescript" />/decentralized-identity/did-common-typescript</a> - A common bundle of shared code and modules for working with DIDs, DID Documents, and other DID-related activities

Decentralized Identifiers (DIDs): The Fundamental Building Block of Self-Sovereign Identity (SSI)	Drummond Reed, Chief Trust Officer at Evernym, will explain in our second Webinar "Decentralized Identifiers (DIDs) - Building Block of Self-Sovereign Identity (SSI)" giving us the background on how DIDs work, where they come from and why they are important for Blockchain based Digital Identity.	https://www.slideshare.net/SSIMeetup/decentralized-identifiers-dids-the-fundamental-building-block-of-selfsovereign-identity-ssi	2018-05-09

* [decentralized-identity/did-common-typescript](https://github.com/decentralized-identity/did-common-typescript) 2019-05-20 - A common bundle of shared code and modules for working with DIDs, DID Documents, and other DID-related activities
* [decentralized-identity/did-security-csharp](https://github.com/decentralized-identity/did-security-csharp) 2020-07-31 - C# implementation of DID security and privacy controls
* [decentralized-identity/did-common-java](https://github.com/decentralized-identity/did-common-java) 2023-05-13 - Shared DID Java library.
* [decentralized-identity/ua-web-extension](https://github.com/decentralized-identity/ua-web-extension) 2018-10-23 - Basic web extension version of a DID User Agent
* [decentralized-identity/did-recovery](https://github.com/decentralized-identity/did-recovery) - Various methods for DID recovery
* [decentralized-identity/web-polyfills](https://github.com/decentralized-identity/web-polyfills) - Polyfills for proposed or emerging DID-centric Web APIs
* [decentralized-identity/http-did-auth-proxy](https://github.com/decentralized-identity/http-did-auth-proxy) - Forked from bcgov/http-did-auth-proxy
DID Auth HTTP proxy.

* [Public profile - Machine-readable, cryptographially-verifiable imprint linked to a DID](https://hackmd.io/4oZOgwFOQDSFUuu3ruN-_g)
  > a simple mechanism to provide public information concerning an entity by advertising a public profile service in the DID document of a public DID. A good analogy for this public identity information would be a machine-readable and cryptographically-verifiable imprint.

### Verifiable Credentials

* [What Are Verifiable Credentials? And How Can They Build Digital Trust?](https://www.salesforce.com/blog/verifiable-credentials/) 2022-02-01 Salesforce
  > Verifiable credentials and verifiable credential management technology offer a direct and secure channel between an organization and its stakeholders. Learn how they bring control over digital identity and build trust with organizations – from health credentials to college degrees.
* [What are Verifiable Credentials? Why do they matter?](https://flur.ee/2022/01/10/what-are-verifiable-credentials-why-do-they-matter/) 2022-01-10 Fluree
  > Authority Does Not Require Centralized Power
  > 
  > As mentioned in my previous article, the trouble with centralization is that data is stored in a database. Once breached, a database can yield a treasure chest of information to be sold on the dark web.
* [Essential Services Delivery coordination using Digitally Verifiable Credentials](https://github.com/bcgov/essential-services-delivery)
  > This repository contains the build, deployment, and application configurations needed to pull a number of separate applications into a single environment and deploy them as a group of interrelated services.
* [bcgov/vc-visual-verifier](https://github.com/bcgov/vc-visual-verifier) - Verifiable Credential Visual Verifier
* [Verifiable Credential Authentication with OpenID Connect (VC-AuthN OIDC)](https://github.com/bcgov/vc-authn-oidc)
  > The integration this document defines is how holders of verifiable credentials can leverage these to authenticate with parties. Note, how the holder became in possession of supported verifiable credentials is out of scope for this integration.
  > 
  > Like any new technology there is adoption required of new concepts, this particular integration aims to provide an easy integration path that allows parties to start leveraging the power of verifiable credentials for user authentication in a non-disruptive fashion. This is achieved by extending the vastly popular OpenID Connect family of specifications.

<iframe src="//www.slideshare.net/slideshow/embed_code/key/2FQiXCaqgTJvrQ" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> 

[Verifiable Credentials 101 for SSI and Decentralized Digital Identity - Tyler Ruff](https://www.slideshare.net/SSIMeetup/verifiable-credentials-101-for-ssi-and-decentralized-digital-identity-tyler-ruff)

* [The Verifiable Credential’s Model](https://trinsic.id/trinsic-basics-the-verifiable-credentials-model/)
  > At the core of every self-sovereign identity (SSI) use case is what we call the verifiable credentials model. This simple yet effective model helps conceptualize how verifiable credentials are exchanged between people and organizations.
* [According to](https://www.w3.org/TR/vc-data-model/) W3: "Verifiable credentials represent statements made by an issuer in a tamper-evident and privacy-respecting manner."
* [Understanding Verifiable Credentials](https://www.credivera.com/blog/understanding-verifiable-credentials) Credivera
  > The value of verifiable credentials and the critical role they will play to our future digital identities is undeniable. As we enter a new era of online representation, trust in the internet will need to be vigorously robust.
* [New search engine, mobile wallet, verifiable credentials and delivery technologies.](https://twitter.com/HUMBLPay/status/1574454647384813568) via Twitter ([ANN](https://www.globenewswire.com/en/news-release/2022/04/13/2421969/0/en/HUMBL-Selected-To-Pilot-Digital-Wallet-Program-On-Behalf-of-The-County-of-Santa-Cruz-California.html) 2022-04-13 HUMBL @HUMBLPay
*using verifiable credentials in their wallet.*
  > #HUMBL x GF2GO - San Diego, CA - [Pilot Program](https://www.youtube.com/watch?v=H_HAFEzmkWU) 

### WebAuthn

* [W3C WebAuthn V2 Now a Standard](https://self-issued.info/?p=2160) Mike Jones
  > While remaining compatible with the original standard, this second version adds additional features, among them for user verification enhancements, manageability, enterprise features, and an Apple attestation format. ([Recommendation](https://www.w3.org/TR/2021/REC-webauthn-2-20210408/)) ([CTAP also approaching standardization](https://self-issued.info/?p=2155).
* [Web Authentication: An API for accessing Public Key Credentials Level 2](https://www.w3.org/TR/2021/PR-webauthn-2-20210225/). This specification defines an API enabling the creation and use of strong, attested, scoped, public key-based credentials by web applications, for the purpose of strongly authenticating users.
* [Second Version of W3C Web Authentication (WebAuthn) advances to Proposed Recommendation (PR)](https://self-issued.info/?p=2149)
  > The World Wide Web Consortium (W3C) has published this [Proposed Recommendation (PR)](https://www.w3.org/TR/2021/PR-webauthn-2-20210225/) Level 2 specification, bringing the second version of WebAuthn one step closer to becoming a completed standard. While remaining compatible with the original standard, this second version adds additional features, among them for user verification enhancements, manageability, enterprise features, and an Apple attestation format.
* [Near-Final Second W3C WebAuthn and FIDO2 CTAP Specifications](https://self-issued.info/?p=2143)
  > The [W3C WebAuthn](https://www.w3.org/blog/webauthn/) and [FIDO2](https://fidoalliance.org/fido2/) working groups have been busy this year preparing to finish second versions of the W3C Web Authentication (WebAuthn) and FIDO2 Client to Authenticator Protocol (CTAP) specifications

