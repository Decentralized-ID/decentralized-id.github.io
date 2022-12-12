---
date: 2020-01-10
title: Verifiable Credentials
description: a standard way to express credentials on the Web in a way that is cryptographically secure, privacy respecting, and machine-verifiable.
excerpt: >
  Verifiable credentials (VCs) are the electronic equivalent of the physical credentials that we all possess today, such as: plastic cards, passports, driving licenses, qualifications and awards, etc. The data model for verifiable credentials is a World Wide Web Consortium Recommendation, "Verifiable Credentials Data Model 1.0 - Expressing verifiable information on the Web" published 19 November 2019.
tags: ["W3C","Verifiable Credentials","Credentials Community Group","VC-WG","JSON-LD","OAuth","FIDO","Claims and Credentials WG"]
categories: ["Web Standards"]
permalink: web-standards/w3c/wg/vc/verifiable-credentials/
header:
  image: /images/verifiable-credentials_head.webp
  caption: "[Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/)"
  teaser: /images/verifiable-credentials-teaser.webp
redirect_from: 
  - web-standards/w3c/vc-wg/verifiable-credentials/
  - specs-standards/verifiable-credentials/
  - web-standards/verifiable-credentials/
  - specs-standards/verifiable credentials/
last_modified_at: 2022-12-12
---

> Verifiable credentials (VCs) are the electronic equivalent of the physical credentials that we all possess today, such as: plastic cards, passports, driving licences, qualifications and awards, etc. The data model for verifiable credentials is a World Wide Web Consortium Recommendation, "Verifiable Credentials Data Model 1.0 - Expressing verifiable information on the Web" published 19 November 2019. - [Wikipedia](https://en.wikipedia.org/wiki/Verifiable_credentials)

## Specification
* [Verifiable Credentials Data Model v1.1 is an official W3C standard!](https://lists.w3.org/Archives/Public/public-credentials/2022Mar/0005.html)  Manu Sporny (Thursday, 3 March, 2022)
  > [Verifiable Credentials Data Model v1.1](https://www.w3.org/TR/2022/REC-vc-data-model-20220303/)
* [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (DRAFT)
  > - The components that constitute a [verifiable credential](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-credentials)
  > - The components that constitute a [verifiable presentation](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-presentations)
  > - An ecosystem where [verifiable credentials](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-credentials) and [verifiable presentations](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-presentations) are expected to be useful
  > - The use cases and requirements that informed this specification.

## Explainer

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
* [What are Verifiable Credentials](https://academy.affinidi.com/what-are-verifiable-credentials-79f1846a7b9)
* [How W3C Verifiable Credentials (VC) Work: Part 1 – Issuance](https://blockster.global/self-sovereign-identity/)
  > When an issuer creates a verifiable credential, it contains following information –
  > 
  > - Who has issued – DID of the Issuer
  > - To whom it is issued – User Identifier
  > - Attributes of the credential – Details of the credential being Issued
  > - When it is Issued – Date of issuance
  > - Credential proof with Issuer signature that makes it tamper evident
  > - Revocation details
* [The Role of Witness Organizations in Verifiable Credentials](https://medium.com/@m.ruminer/on-the-role-of-witness-organizations-in-self-sovereign-identity-or-vcs-aren-t-just-p2p-e2cbafce6928)
  >  The basis is that not every source of a verifiable credential has an interest in issuing verifiable credentials and that it is not only logical but beneficial to the ecosystem of trust that witness organizations will issue on behalf of these sources.
* [An introductory dive into VCs (verifiable credentials)](https://hackernoon.com/understanding-the-verifiable-credentials-vcs-it1535e9) HackerNoon
  > Verifiable Credentials heavily utilize Decentralized Identifiers to identify people, organizations, and things and to achieve a number of security and privacy-protecting guarantees. They are issued and cryptographically signed documents, intended to be understood by computers rather than people.
* [How Does a Verifier Know the Credential is Yours?](https://www.evernym.com/blog/how-does-a-verifier-know-the-credential-is-yours/) Evernym
  > A link secret is a large random number, wrapped in a way that allows the holder to prove that they know the secret.
* [Introduction to Verifiable Credentials](https://www.ubisecure.com/identity-management/verifiable-credentials/) Ubisecure
  > The Verifiable Credentials specification is quite new, and many pieces that are required to create interoperable solutions are still incomplete or missing at time of writing. However, there is significant momentum around verifiable credentials (VCs). This is partly attributed to VCs being part of the solution for blockchain-based decentralised identity.
* [8 Reasons to use Verifiable Credentials](https://academy.affinidi.com/8-reasons-to-use-verifiable-credentials-300833276b52) Affinidi
  > VCs are interoperable across many systems and can be used in almost every possible scenario.
* [What are Verifiable Credentials in 3 Minutes](https://www.youtube.com/watch?v%3Ds5h7OgmnrxE) Affinidi (video)
* [The VC Lifecycle](https://credentialmaster.com/the-vc-lifecycle/) Credential Master
  > In 1956 the switch to consistent shipping containers began, and it changed the physical world [profoundly](https://www.economist.com/finance-and-economics/2013/05/18/the-humble-hero); the switch to consistent, authenticatable digital data containers [will do the same for cyberspace](https://rufftimo.medium.com/like-shipping-containers-verifiable-credentials-will-economically-transform-the-world-fece2b9da14a).
* [Verifiable Credentials Aren’t Credentials. And They’re Not Verifiable In the Way You Might Think](https://credentialmaster.com/verifiable-credentials-arent-credentials-theyre-containers/) Timothy Ruff
  > think “authenticatable data container” [...]
  > 
  > VCs can carry any sort of data payload, and that isn’t just a good thing, it’s a great one. [Part two](https://medium.com/@rufftimo/like-shipping-containers-verifiable-credentials-will-economically-transform-the-world-fece2b9da14a) of my container series covers how such fluid data portability could economically affect cyberspace to a degree comparable to how shipping containers affected global trade.
* [Verifiable credentials are key to the future of online privacy](https://www.helpnetsecurity.com/2021/07/26/verifiable-credentials/) HelpNetSecurity
  > - All the data is decentralized, meaning there’s no need for a database of student records that could be jeopardized. Alice’s data lives with her.
  > - The employer doesn’t need to keep a copy of Alice’s transcript to verify her education.
  > - The college doesn’t play intermediary and doesn’t have access to the list of organizations Alice shares her data with. Other parties have no way of correlating this data as each exchange is private and unique.
  > - If desired, Alice could pick and choose what she wants to share. She could prove her degree without sharing her date of graduation or GPA, for example.
* [What are Verifiable Credentials?](https://medium.com/affinidi/what-are-verifiable-credentials-79f1846a7b9)
  > At the most basic level, verifiable credentials, or VC in short, are tamper-proof credentials that can be verified cryptographically.
* [Self Attested vs Chain of Custody - assurance levels in data provenance in VCs](https://iiw.idcommons.net/23G/_Self_Attested_vs_Chain_of_Custody_-_assurance_levels_in_data_provenance_in_VCs) by Stew Whitman & Alka Lachhwani
  > There are two important factors in establishing “truth” or the trustworthiness of the information. Attributional and Reputational. You need to have both to have trust.
  > 
  > Digital needs higher level of attestation because it is easier to forge and easier to propagate that forgery.
* [VerifiableCredential.io](https://verifiablecredential.io/learn)
  > Learn about verifiable credentials, then head to the playground to view examples, explore multiple use-cases and start using them.
* [Do I Need a Verifiable Credential?](https://community.rsa.com/t5/rsa-labs-blog/do-i-need-a-verifiable-credential/ba-p/610241) RSA
* [How a combination of Federated identity and Verifiable Credentials can help with Customer onboarding](https://pranavkirtani.medium.com/how-a-combination-of-federated-identity-and-verifiable-credentials-can-help-with-customer-7e6518feb018) Pranav Kirtani
  > Before we dive into how Federated systems like OIDC and SAML along with Verifiable Credentials (VC) can help improve customer onboarding to your application, let us first understand what are the current methods being used for onboarding.

## Comparisons with other Tech
* [Compare and Contrast: OpenBadges vs Verifiable Credentials](https://academy.affinidi.com/compare-and-contrast-openbadges-vs-verifiable-credentials-d504c054d5db) Affinidi 
  > As we move towards a world of digital identity, many ways of sharing and verifying Personally Identifiable Information are emerging. Two such modes that we’ll talk about today are Open Badges and Verifiable Credentials.
* [Non-Fungible Tokens (NFTs) vs Verifiable Credentials (VCs)](https://academy.affinidi.com/non-fungible-tokens-nfts-vs-verifiable-credentials-vcs-cd0ebb13f1fb) Affinidi
  > A common thread that connects both NFTs and VCs is that they leverage the potential benefits of the digital world to give users more security, flexibility, and freedom to monetize.
* [ERC-721 Non-Fungible Token Standard on Ethereum vs. VCs on Hyperledger Indy](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0059.html) Michael Herman
  > When are Hyperledger Indy/Sovrin VCs better than Ethereum smart contracts for NFEs/NFTs (non-fungible entities/tokens)?
  > 
  > It seems obvious but I don't have a detailed/worked out answer.  One project I'm associated with wants to use the [ERC-721 Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) on Ethereum but I believe VCs are a better route to take. Part of the desire to stay on Ethereum is there is quite a vibrant NFT community on Ethereum and lots of different EC-721 tokens.
* [Compare and Contrast — IRMA vs Verifiable Credentials](https://academy.affinidi.com/compare-and-contrast-irma-vs-verifiable-credentials-58e4b30d85f1)
* [Could an NFT be a VC?](https://iiw.idcommons.net/20I/_Could_an_NFT_be_a_VC%253F) by Grace Rachmany
  > Case discussed: A group of villages in Africa using a cryptocurrency platform for alternative currencies. Different organizations issue the coins under different circumstances. When you accept a currency, you want to know who is the issuer. The Red Cross might be more or less trusted than the local leader or agricultural cooperative as the issuer of a currency that is supposedly equivalent to a shilling.
  > 
  > What types of tech could be used for this?
  > 
  > - Multiple currencies on the blockchains
  > - Certifications in the form of some kind of NFT issued by the issuer.
  > - Limited supply tokens or NFTs that are “expired” when you use them
  > - Open Credential Publisher framework was suggested
  > - VCs are generally authorizations associated with a person, so maybe a person could have the VC and show their credit rating in some way while they are making a transaction
  > - Similarly maybe the VC belongs to the organization that is issuing the coin, proving its reputation over time.
* [How does VC Functional Stack compare to #ToIP Stack?](https://twitter.com/rufftimo/status/1301314001251438593) @rufftimo
  > 1. ToIP Layers 2 & 3 compare to Functional Layer 2
  > 2. ToIP Layer 4 compares to Functional Layers 3 & 4 (horizontal layer for VC Management, vertical layer for Applications)
  > 3. Functional stack doesn't require #blockchain
  > 4. Functional Stack doesn't detail steps for trust or verification; ToIP Stack doesn't separate management or storage
  > 5. Functional Stack clarifies functions, roles, and potential business models; ToIP stack clarifies trust & security They are complementary, not contradictory.
  > ![](https://i.imgur.com/8zakrMQ.png)
* [What are VCs similar to?](https://lists.w3.org/Archives/Public/public-credentials/2021Aug/0338.html) Michael Herman (Trusted Digital Web) (Monday, 23 August)
  > The chip in your e-passport is the analogy I’ve been most successful with\
  > An issuer gives it to you.\
  > You carry it around and show to whom you choose\
  > The verifier can check its integrity without contacting the issuer\
  > “A VC is like the chip in your passport - bit for any document type”\
  > So far the best analogy I’ve found.  Policy makers say “ah, I see”…
* [Hygiene for a computing pandemic](https://fossandcrafts.org/episodes/20-hygiene-for-a-computing-pandemic.html)
  > This episode of FOSS and Crafts features Christopher Lemmer Webber discussing the object capability security approach. Its a generalization not specific to VCs, continuing from the conversation on the CCG mailinglist, [Hygiene for a computing pandemic: separation of VCs and ocaps/zcaps](https://lists.w3.org/Archives/Public/public-credentials/2020Dec/0028.html), we shared last month.
The podcast *show-notes include an epic list of references* supporting the discussion.
* [Re: The dangers of using VCs as permission tokens (was: PROPOSALs for VC HTTP API call on 2021-06-22)](https://lists.w3.org/Archives/Public/public-credentials/2021Jun/0244.html) Manu Sporny
  > On 6/24/21 12:35 PM, Kyle Den Hartog wrote:
  > > Agreed, when it comes to the number of checks that occur it's much greater
  > > because of the delegation. With that in mind, looking at the semantics only
  > > of the system VCs in my opinion weren't optimally designed for permission
  > > tokens. This difference between the two requires that an implementation
  > > that wants to support both claims tokens and permissions tokens has to
  > > grapple with the different mental model that arise when trying to stuff
  > > these things together. This introduces additional complexity. Additionally
  > > it leads to weird statements that are being made where it's difficult to
  > > tell if the VC is behaving like a claims token or a permissions token.
  > 
  > Yes, exactly this. Exactly what Kyle states above is the reason why it's so complicated (and thus dangerous) to use VCs as permissions tokens.
  > 
  > This is one of the primary reasons that we separated out the Authorization Capabilities work from the Verifiable Credentials work. Things get really complicated when you start mixing authz/authn/claims/permissions into a Verifiable Credential. Just because you can do it doesn't mean you should.
  > 
  > [https://kyledenhartog.com/example-authz-with-VCs/](https://kyledenhartog.com/example-authz-with-VCs/)
* [Comparing VCs to ZCAP-LD](https://kyledenhartog.com/comparing-VCs-with-zcaps/) Kyle Den Hartog
  > Why make the investment then to put the time and effort into ZCAPs when we’ve already got VCs? Simply put because security is hard and trying to push square pegs into round holes often times leads to bugs which are elevated to mission critical authentication/authorization bypass vulnerabilities. By designing around a fit for purpose data model with a well defined problem being solved it allows for us to be much more precise about where we believe extensibility is important versus where normative statements should be made to simplify the processing of the data models. By extension this leads to a simpler security model and likely a much more robust design with fewer vulnerabilities.
- [Re: VCs - zCaps / OCap a Discussion](https://lists.w3.org/Archives/Public/public-credentials/2020Dec/0027.html) Dave Longley 12/5
  > TL; DR: My current view is that the main confusion here may be over the difference between VCs and LD Proofs, not VCs and ZCAPs. VCs are not a generalized container for attaching a cryptographic proof to a document. That's what LD proofs (or JOSE style proofs) are for. VCs *use* LD proofs (or JOSE style proofs) to attach an assertion proof to a document that specifically models statements made by an issuer about some subject, which is therefore inherently about the identity of that subject.

## Development
* [Example Design of an Authorization System with Verifiable Credentials and the Tradeoffs](https://kyledenhartog.com/example-authz-with-VCs/) Kyle Den Hartog
  > The primary focus of this blog post is to highlight the different problems that are likely to occur when going down the path of building an authorization system with verifiable credentials. I’ll be sure to keep things at a higher level so that anyone can understand these tradeoffs, but take you through the details that would be thought through by an architect designing the system.
* [Managing VCs at scale & the VC Stack](https://iiw.idcommons.net/index.php?title%3D12L/_Managing_VCs_at_Scale_%2526_the_VC_Stack%26action%3Dedit%26redlink%3D1) by Timothy Ruff & Alan Davies
* [Indexing and Querying Revoked Verifiable Credentials](https://medium.com/51nodes/indexing-and-querying-revoked-verifiable-credentials-e229dc2781d4) 51 Nodes
  > this article describes a simple approach to revoke verifiable credentials and a decentralized and efficient way to index and query those revoked credentials using the [Graph protocol](https://thegraph.com/en/).


## Literature

* [VC Spec Enhancement Proposal](https://github.com/SmithSamuelM/Papers/blob/master/whitepapers/VC_Enhancement_Strategy.md) Sam Smith
  > the VC standard appears to be an adoption vector for Linked Data, not the other way around. My overriding interest is that the concept of a VC as a securely attributable statement is a very powerful and attractive one and therefore should be widely adopted. We should therefore be picking the best technologies that best support broad VC adoption, not the other way around.
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


#### Verifiable Credentials Extension Registry

* [Verifiable Credentials Extension Registry](https://w3c-ccg.github.io/vc-extension-registry/) - This document contains a list of all known Verifiable Credential extensions and their associated specifications. 

##### 3.1 Proof Methods

> This table summarizes the Proof Method specifications currently in development. The table lists the method name, associated specification, authors, stability of the specification, and conformance test suite (if applicable).

* [Ed25519Signature2018](https://w3c-dvcg.github.io/lds-ed25519-2018/) by Markus Sabadello 	
* [RsaSignature2018](https://w3c-dvcg.github.io/lds-rsa2018/) - Manu Sporny, Dave Longley

##### 3.2 Status Methods

* [CredentialStatusList2017](https://w3c-ccg.github.io/vc-csl2017/) - Manu Sporny, Dave Longley

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

## Interoperability

* [Verifiable Credentials Specification Relationships](https://github.com/decentralized-identity/vc-spec-map) ([ANN](https://lists.w3.org/Archives/Public/public-credentials/2020Nov/0100.html))
  > diagrams and documentation on the relationship of verfiable credential specifications
  > 
  > The current release contains some of the most core specifications and their related specs in a diagram. It does not yet address some of the items especially under DIF work groups for secure data storage, SIOP, Sidetree etc.

[![]({{ site.baseurl }}/images/VC-spec-map.webp)](https://github.com/decentralized-identity/vc-spec-map/releases/tag/v1.2.0)

[Distributed ID Learning Path](https://translate.google.com/translate?sl=auto&tl=en&u=https://kristinayasuda.com/posts/decentralized-identity-catch-up-path/) by Christina Yasuda (based on above spec map)
  * Pre-Requisite Knowledge: [JSON](https://www.json.org/json-en.html), [JSON-LD](https://json-ld.org), [JWT](https://jwt.io/introduction/), [JWS](https://w3c-ccg.github.io/lds-jws2020/), [JWK](https://tools.ietf.org/html/rfc7517), [JWA](https://tools.ietf.org/html/rfc7518), and sometimes [CBOR](https://cbor.io/). 
  * Decentralized Identifiers: [DID-Core](https://www.w3.org/TR/did-core/), [DID-Resolution](https://w3c-ccg.github.io/did-resolution/), [DID-Spec](https://www.w3.org/TR/did-spec-registries/), [DID Use-Cases](https://www.w3.org/TR/did-use-cases/). 
  * Verifiable Credentials: [VC-Data Model](https://www.w3.org/TR/vc-data-model/), [VC Use-Cases](https://www.w3.org/TR/vc-use-cases/), and [VC-Implementors Guide](https://www.w3.org/TR/vc-imp-guide/)
  * Transport: HTMl, [DID-Comm](https://identity.foundation/working-groups/did-comm.html)
  * Credential Presentation: [Presentation Exchange](https://identity.foundation/presentation-exchange/), [Credential Manifest](https://identity.foundation/credential-manifest/)
  * Optional: [Well-known-did](https://identity.foundation/.well-known/resources/did-configuration/)
  * Other Data Formats: [Open Badges](https://openbadges.org/)
    * Independent DID Methods: [DID-method-key](https://w3c-ccg.github.io/did-method-key/), [DID-method-peer](https://identity.foundation/peer-did-method-spec/), DID-method-web
* [Categorizing Verifiable Credentials - Evernym](https://www.evernym.com/blog/categorizing-verifiable-credentials/)
  > Not all verifiable credentials are created the same. This post examines the categories of credentials and the architectural choices driving this variation.
* [SSI Architectural Stack and Community Efforts Overview](https://github.com/decentralized-identity/interoperability/blob/master/assets/ssi-architectural-stack--and--community-efforts-overview.pdf)
  > While a more thorough (and competitive) separation of concerns might slice today’s and tomorrow’s identity systems into more modular and interchangeable parts at many more layers, the diagram used here organizes the space into just three broad divisions, which map roughly to the bottom three in the mapping dominant in the Aries & ToIP communities. For a more detailed and complex mapping, see the forthcoming map by the DIF interoperability working group. 
* [Interoperability Mapping Exercise](https://github.com/decentralized-identity/interoperability/blob/master/assets/interoperability-mapping-exercise-10-12-20.pdf)
* [creatornader/Decentralized Identity Standards.md](https://gist.github.com/creatornader/c8a20c534d3cf8f65a9b34ce2ad81725)

## Use Case 

* [Better digital living with blockchain-backed verifiable credentials](https://thepaypers.com/expert-opinion/better-digital-living-with-blockchain-backed-verifiable-credentials--1250869) The Paypers
  > The NHS can now provide you with a digital verifiable credential to prove your vaccination status, securely stored in the NHS app and easily accessible, generating a QR code to prove to airlines and employers that you are fit to fly or work. But this is just the first step in the development of an enabling technology that can bring benefits to many areas of modern life.
* [On Climate Crisis and Self-Sovereign Verifiable Career Credentials](https://www.velocitynetwork.foundation/on-climate-crisis-and-self-sovereign-verifiable-career-credentials/) Velocity Network
  > This rich verifiable self-sovereign career identity will be the ‘great transformer’ of the global labor market. It will change the way people navigate their careers and livelihoods, and how employers make talent decisions.
* [The World of Anonymous Credentials](https://blog.dock.io/anonymous-credentials/) Dock
  > A credential is called a verifiable credential when its authenticity can be cryptographically checked by anyone because the credential contains a cryptographic signature by the issuer, and the issuer's public key is well known.
* [25 Use Cases for Verifiable Credentials](https://drive.google.com/file/d/1BrFjh6-TVkJ4Rfllh5fUTjh6hkYtPbR_/view) LTO Network and Sphereon
* [Verifiable Credentials For Travel & Hospitality](https://www.youtube.com/watch?v%3DXxd56y2mhFQ) Evernym
  > verifiable credentials and digital wallets can reduce fraud, automate workflows, and transform customer experiences across the travel and hospitality industries.
* [The Power of Verifiable Credentials](https://credentialmaster.com/the-power-of-vcs/) Credential Master
  For the first time ever, data from one ecosystem can be instantly authenticated in any other, online or off, without a direct connection to the source.
* [Verifiable Credential Notarization and Third-Party Notary Services Providers: User Scenarios](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0109.html) Michael Herman 7/15
* [Verifiable Credentials for Authentic Data in the Supply Chain](https://iiw.idcommons.net/10G/_Verifiable_Credentials_for_Authentic_Data_in_the_Supply_Chain) by Gena Morgan, Kevin Dean
  > Using DiDs and VCs for verifiable product data in supply chains, leveraging the largest supply chain standard system in the world,
  > 
  > 2.5 million users companies, over 6 billion product scans per day
  > 
  > Product data and attestations from a number of various authoritative sources
  > 
  > Leverage DIDs/VCs for distributed data sharing, verification
* [Verifiable Credentials for Assets <30 min](https://iiw.idcommons.net/21E/_Verifiable_Credentials_for_Assets_30_min) by Mahmoud Alkhraishi
  > General Framework on how to think of VCs for Assets including leveraging GS1 and other vocabularies in the traceability vocab.
  > 
  > Requirements and Opportunities that block adoption of VCs in Supply chains
  > * [Traceability Vocabulary v0.0](https://w3c-ccg.github.io/traceability-vocab/)
  > * [VC HTTP API (0.0.2-unstable)](https://w3c-ccg.github.io/vc-http-api)
  > * [Status List 2021](https://w3c-ccg.github.io/vc-status-list-2021/)

## User Experience
* [Video] [Using Paper-based Structured Credentials to Humanize Verifiable Credentials [Rough Cut]](https://www.youtube.com/watch?v%3DkM30pd3w8qE%26list%3DPLU-rWqHm5p45dzXF2LJZjuNVJrOUR6DaD%26index%3D2) Michael Herman (Trusted Digital Web) (Friday, 19 November)
  > User Scenario: ABC Grocery wants to use the Trusted Digital Web to issue a Purchase Order for 10 cabbages from David's Cabbages.
* [Rendering Verifiable Credentials](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md) Manu Sporny
  > This paper explores ways in which the Verifiable Credentials data model could be extended to support visual, audio, and physical renderings for Verifiable Credentials.

## Critique

### Thread: VCs need Threat Modeling

* [Thread started by Pamela Dingle](https://twitter.com/pamelarosiedee/status/1537233243086327812?s%3D20%26t%3DWWt14_H4AXgtn09xb5-yew)
  > Another pre-read recommendation for @identiverse: the @openid for Verifiable Credentials Whitepaper.  It is a great high level explanation of decentralized benefits and use cases, both @kristinayasuda & @tlodderstedt contributed! OpenID for Verifiable Credentials
    * [Firstyear Replying to @Erstejahre @pamelarosiedee and 4 others](https://twitter.com/Erstejahre/status/1537615778106658816)
      > It also seems to lack any sections about threat modelling and possible risks, making it hard to trust since risks are not directly and clearly addressed.
    * [Torsten Lodderstedt Replying to @Erstejahre @pamelarosiedee and 3 others](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)
      > I agree. We [threat] model while we are designing the protocol, we also need to add it to the spec. Please note: we build on existing work. There is an extensive thread model for OAuth and countermeasures that we built on ([datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics). Feel free to contribute.
