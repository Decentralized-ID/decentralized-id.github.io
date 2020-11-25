---
date: 2020-01-10
title: Verifiable Credentials
tags: ["W3C", "CCG","VC-WG"]
categories: ["Web Standards"]
permalink: /web-standards/w3c/vc-wg/verifiable-credentials/
redirect_from: 
  - web-standards/verifiable-credentials/
  - specs-standards/verifiable credentials/
last_modified_at: 2020-11-25
toc: true
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

## Verifiable Claims Working Group

* [W3C Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/) 
* [Verifiable Credentials Data Model 1.0](https://www.w3.org/TR/vc-data-model/)
  >  Credentials are a part of our daily lives; driver's licenses are used to assert that we are capable of operating a motor vehicle, university degrees can be used to assert our level of education, and government-issued passports enable us to travel between countries. This specification provides a mechanism to express these sorts of credentials on the Web in a way that is cryptographically secure, privacy respecting, and machine-verifiable. 
* [W3C Verifiable Credentials - Kent Branch](https://www.bcs.org/events/2019/october/w3c-verifiable-credentials-kent-branch/) • [pdf](https://cdn.bcs.org/bcs-org-media/4653/kent-w3c-verifiable-credentials-031019.pdf)
  > The speaker will introduce the W3C Verifiable Credentials Data Model, which was published as a Proposed Recommendation in September 2019. Verifiable Credentials are the latest development in identity management and are fundamentally different from today's federated identity management systems such as SAML and OpenID Connect.
  > 
  > David will describe the VC ecosystem and data model. He will then describe the prototype implementation which was built with colleagues from the University of Toulouse. They built a prototype system, which uses Fast Identity Online (FIDO) for user authentication, meaning that usernames and passwords are no longer needed. A pilot application was tested with a small sample of NHS patients and the speaker will present the results of this trial.
* [Verifiable Credentials Implementation Guidelines 1.0](https://w3c.github.io/vc-imp-guide/)
  > This guide provides some examples and resources for implementing protocols which make use of verifiable credentials, beyond those available in the core specification. 
* [W3C Verifiable Claims Working Group Test Suite](https://w3c.github.io/vc-test-suite/)
* [Verifiable Credentials Use Cases](https://www.w3.org/TR/vc-use-cases/)
  > This document does NOT attempt to define an architecture for the support of Verifiable Claims. Instead it expresses the sorts of needs that real users have that could be addressed through support for some sort of self-sovereign claim environment. It attempts to use terminology that is consistent with the other deliverables of the Verifiable Claims Working Group (you can see the relevant terms in Appendix A).

[![](https://i.imgur.com/J2IgVgl.png)](https://www.w3.org/TR/vc-use-cases/)

## Literature

* [Verifiable Credential Exchange](https://www.windley.com/archives/2018/12/verifiable_credential_exchange.shtml)
  > Multi-source identity (MSI) depends on issuing, exchanging, and verifying digital credentials. The specification for verifiable credentials is being formulated by the World Wide Web Consortium’s Verifiable Credentials Working Group. Verifiable credentials provide a standard way to express credentials in a way that is cryptographically secure, privacy respecting, and automatically verifiable.
* [Full-text Search for Verifiable Credential Metadata on Distributed Ledgers](https://arxiv.org/abs/1909.02895)
  > The proposed solution is able to find credential types based on textual input from the user by using a full-text search engine and maintaining a local copy of the ledger. Thus, we do not need to rely on information about credentials coming from a very large candidate pool of third parties we would need to trust, such as the website of a company displaying its own identifier and a list of issued credentials. We have also proven the feasiblity of the concept by implementing and evaluating a prototype of the full-text credential metadata search service.
* [Enabling Decentralised Identifiers and Verifiable Credentials for Constrained IoT Devices using OAuth-based Delegation](https://www.ndss-symposium.org/wp-content/uploads/diss2019_05_Lagutin_paper.pdf)
  > Abstract—Decentralised identifiers (DIDs) and verifiable credentials (VCs) are upcoming standards for self-sovereign privacypreserving identifiers and authorisation, respectively. This focus on privacy can help improve many services and open up new business models, but using DIDs and VCs directly on constrained IoT devices can be problematic due to the management and resource overhead. This paper presents an OAuth-based method to delegate the processing and access policy management to the Authorisation Server thus allowing also systems with constrained IoT devices to benefit from DIDs and VCs.
* [Addition of Proof Request/Response to a formal Verifiable Credentials specification](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/verifiable-credentials-proof-request.md)
  > The W3C Verifiable Credentials (hereafter VC) specification does not currently outline how credential data should be requested by a Verifier. This document outlines the approach taken at Workday and proposes it as an addition or companion to the VC spec.
  > 
  > At RWoT we wish to present our approach in order to get community feedback and consensus. Workday recently announced our credentialing platform and will shortly begin to issue credentials within our market verticals. We fully intend to support the community standards around credentialing and therefore wish to drive consensus in the community on a simple, standard approach for requesting and sharing VCs between a holder and verifier.

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

## Adoption

* [SolidVC : a decentralized framework for Verifiable Credentials on the web](https://dspace.mit.edu/handle/1721.1/121667)
  > SolidVC is a decentralized Verifiable Credentials platform built with the open protocols of the Web. It is implemented on top of Solid, a Web framework developed at MIT in 2016 that allows decentralized applications to interact with personal user data to provide services in an access controlled environment.
* [Blockcerts V3 Proposal - Verifiable Credentials & Decentralized Identifiers](https://community.blockcerts.org/t/blockcerts-v3-proposal-verifiable-credentials-decentralized-identifiers/2221)
  > As the standards around Verifable Credentials are starting to take form, different favors of "verifiable credentials-like" data structures need to make necessary changes to leverage on the rulesets outlined and constantly reviewed by knowledgeable communities such as the W3C. The purpose of this paper is to identify all of the changes needed for Blockcerts to comply with the Verifiable Credentials (VCs) and Decentralized Identifers (DIDs) standards and to expand upon the additional benefits of using a blockchain in combination with Verifiable Credentials. This paper is meant to act as an explainer in which a formal specification can be created. This paper proposes multiple implementation options for several properties. The intention is that we can engage the Blockcerts / Verifiable Credential communities and see what fts best.
* [mattr.global/Verifiable Credential based Authentication via OpenID Connect](https://mattr.global/verifiable-credential-based-authentication-via-openid-connect/)
  > At MATTR, we’ve been working hard on an exciting opportunity with the Government of British Columbia (BC Gov) in Canada. In June 2019, the BC Gov Verifiable Organisations Network team put out a “Code With Us” development bounty to integrate KeyCloak, their chosen enterprise Identity and Access Management (IAM) solution, with a new W3C standard called Verifiable Credentials. This work led to a solution that enables the use of Verifiable Credentials (VC) as a means of authentication that is interoperable with OpenID Connect (OIDC). We call this work VC-AuthN-OIDC. The output is an adapter that bridges these standards and enables a whole new set of capabilities through a simple extension of most modern IAM solutions.
* [Blockstack and Verifiable Credentials - Paris P2P Festival](https://p2p.paris/gen/attADzQJ92rNIv6B3-Blockstack_and_Verifiable_Credentials_-_Paris_P2P_Festival_.pdf)
  > • Keep auth and smart contracts on-chain\
  > • Keep encrypted data off-chain\
  > • Wrap everything in an easy JavaScript API
* [IBM Verify Credentials](https://docs.info.verify-creds.com)
  > With IBM Verify Credentials and our alpha components, you can begin your journey of exploring the benefits of decentralized identity. We have provided an interactive experience centered around the challenge of proving your identity while opening a financial account. Additionally, we will walk you through the development of your first end-to-end decentralized identity solution.
* [Verifiable credentials and libp2p](https://discuss.libp2p.io/t/verifiable-credentials-and-libp2p/206)
  > Hi - we’re looking into libp2p as a network stack for our application and exploring how we could integrate verifiable credentials (https://w3c.github.io/vc-data-model/ 2) infrastructure. A basic use case is that of a node being challenged to provide some specific credential to join the network. The bootstrap node handling the incoming connection should verify the credential with the issuer and complete the connection/bootstrap or terminate it.
* [Open Badges are Verifable Credentials](https://nbviewer.jupyter.org/github/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/open-badges-are-verifiable-credentials.pdf)
  > The Blockcerts Open Badges Draft Extension introduced a verifcation method based on those used by Verifable Credentials for the specifc use case of blockchain-anchored credentials. This paper expands that work and proposes a new option that can reside alongside existing Open Badges verifcation methods.
* [Workday Credentials & WayTo™ By Workday](https://credentials.workday.com/docs/overview/)
  > An issuer is any entity that wishes to relinqiush and publicly attest to the veracity of data pertaining to a user. Public attestation comes in the form of a digital signature. When an issuer offers a credential to a user, Workday Credentials cryptographically signs the data in each credential with the issuer's private key before offering it to the user. The signing key's corresponding public key is written to a public ledger and is declared as belonging to the issuer, so that anyone can use that public key to verify the signature embedded in a user's digital credentials and establish trust in a credential's authenticity.

## Code

* [Identity.com Verifiable Credential Library](https://www.npmjs.com/package/@identity.com/credential-commons)
  > This Javascript Library provides functionality around Verifiable Credentials (VC), a W3C standard. Enables Validators to issue, Credential Wallets to verify, filter and Requesters to verify credentials.
* [EDCI-Data-Model](https://github.com/european-commission-europass/EDCI-Data-Model)
  > The European Commission is developing the Europass Digital Credentials Infrastructure (EDCI) – a set of tools, services and software to support the issuance of authentic, tamper-proof digital credentials (such as qualifications and other learning achievements) across Europe. The EDCI is being developed as part of ongoing work to implement the new Europass Framework for supporting transparency of skills and qualifications in Europe.
* [gautamdhameja/substrate-verifiable-credentials](https://github.com/gautamdhameja/substrate-verifiable-credentials)
  > A minimal Substrate runtime for verifiable credentials' issuance and verification.
* [bcgov/TheOrgBook](https://github.com/bcgov/TheOrgBook)
  > A public repository of verifiable claims about organizations. A key component of the Verifiable Organization Network.
* [bcgov/vc-authn-oidc](https://github.com/bcgov/vc-authn-oidc)
  > Verifiable Credential Authentication with OpenID Connect (VC-AuthN OIDC)

### Credentials Community Group

* [Credentials Community Group](https://www.w3.org/community/credentials/) • [Website](https://w3c-ccg.github.io/) • [Mail archive](http://lists.w3.org/Archives/Public/public-credentials/)
  > The mission of the Credentials Community Group is to explore the creation, storage, presentation, verification, and user control of credentials. We focus on a verifiable credential (a set of claims) created by an issuer about a subject—a person, group, or thing—and seek solutions inclusive of approaches such as: self-sovereign identity; presentation of proofs by the bearer; data minimization; and centralized, federated, and decentralized registry and identity systems. Our tasks include drafting and incubating Internet specifications for further standardization and prototyping and testing reference implementations.
* [w3c-ccg/vc-extension-registry](https://github.com/w3c-ccg/vc-extension-registry)
REGISTRY: The Verifiable Credentials Extension Registry - w3c-ccg/vc-extension-registry
* [w3c-ccg/edu_occ_verifiable_credentials](https://github.com/w3c-ccg/edu_occ_verifiable_credentials)
WORK ITEM: Drafts and Ideas of Educational and Occupational Verifiable Credentials - w3c-ccg/edu_occ_verifiable_credentials
* [w3c-ccg/vc-examples](https://github.com/w3c-ccg/vc-examples)
WORK ITEM: Verifiable Credentials Examples. 
