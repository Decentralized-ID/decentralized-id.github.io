---
title: Blockchain and Self Sovereign Identity
description: "Why Blockchain for Identity? + Assorted Blockchain ID Initiatives"
excerpt: "Traditional identity systems typically suffer from single points of failure, lack of interoperability, and privacy issues such as encouraging mass data collection and user tracking. Blockchain technology has the potential to support novel data ownership and governance models with built-in control and consent mechanisms, which may benefit both users and businesses by alleviating these concerns; as a result, blockchain-based IDMSs are beginning to proliferate."
header: 
  image: /images/blockchain-id-header.webp
  caption: "[NIST Cybersecurity (DRAFT) Blockchain Identity Management Approaches](https://arxiv.org/pdf/1908.00929.pdf)" 
  teaser: /images/blockchain-Tumisu_3019121.webp
layout: single
permalink: /tech/blockchain/
canonical_url: "https://decentralized-id.com/tech/blockchain/"
redirect_from:  /blockchain/
categories: ["Technologies"]
tags: ["NIST","Identiverse",Authenteq,Blockstack,Civic,Microsoft,Datum,ProCivis]
last_modified_at: 2023-06-09
toc: true
toc_sticky: true
---

## Literature

* [ISO/TR 23249:2022 – Overview of existing DLT systems for identity management](https://www.iso.org/standard/80805.html) 2022-05 ISO
  > This document covers the following topics:
  > - Managing identity for individuals, organizations, things (IoT & objects), functions and processes and other entities including within and across DLT systems.
  > - Description of the actors and their interactions and common interfaces.
  > - Architectures.
  > - Existing relevant standards and frameworks.
* [NIST CYBERSECURITY WHITE PAPER] [**_A Taxonomic Approach to Understanding Emerging Blockchain Identity Management Systems_**](https://arxiv.org/pdf/1908.00929.pdf) 2019-06-09
  > Identity management systems (IDMSs) are widely used to provision user identities while managing authentication, authorization, and data sharing both within organizations as well as on the Internet more broadly. Traditional identity systems typically suffer from single points of failure, lack of interoperability, and privacy issues such as encouraging mass data collection and user tracking. Blockchain technology has the potential to support novel data ownership and governance models with built-in control and consent mechanisms, which may benefit both users and businesses by alleviating these concerns; as a result, blockchain-based IDMSs are beginning to proliferate. This work categorizes these systems into a taxonomy based on differences in architecture, governance models, and other salient features. We provide context for the taxonomy by describing related terms, emerging standards, and use cases, while highlighting relevant security and privacy considerations.
* [Towards Self-Sovereign Identity using Blockchain Technology](https://essay.utwente.nl/71274/1/Baars_MA_BMS.pdf) 2016-10-26
  > Blockchain technology could function as the foundation of such system being a network for decentralized trust and exchange. Because everyone can participate as issuer or acquirer (and both), there are low adoption barriers and low costs. This allows new business opportunities for governments, banks and other authorities and more transparency and control for end-users.

## General
* [12 Ways Crypto and Blockchain Tech Will Change the World (and Boost Your Bottom Line)](https://moneymorning.com/2022/04/08/12-ways-crypto-and-blockchain-tech-will-change-the-world-and-boost-your-bottom-line/) 2022-04-08
  > No. 7: Protecting Our Personal Data\
  > Called a "self-sovereign identity," it would keep the data with the individual. People would use the Secure ID for online interactions; any data sent would be encrypted. But the key is that those online entities would not store the data themselves. So, there would be no more huge, centralized places where personal data could be stolen.
* [curated list] [Peacekeeper's Blockchain and Identity](https://github.com/peacekeeper/blockchain-identity) 2021-11-23
* [Three approaches to Self-Sovereign Identity based on blockchain](https://medium.com/coinmonks/three-approaches-to-self-sovereign-identity-based-on-blockchain-301b18a49345) 2021-10-20 Rosario De Chiara Coinmonks
  > The third approach is, in a way, derived from the previous one, and is the one pursued by [uPort/Serto](https://www.uport.me/): the blockchain has one single registry that tracks down just the revocation of credentials,
* [Identity Blockchains and Energy Consumption](https://indicio.tech/identity-blockchains-and-energy-consumption/) 2021-10-19 Indicio
  A decentralized network using a blockchain-based distributed ledger means you can use [Peer DIDs](https://identity.foundation/peer-did-method-spec/) to move most “transactions” and their cryptographic proofing off ledger. This means that for those peer-to-peer interactions, identity blockchains don’t need to do any ledger transactions at all.
* [Legitimacy and Decentralized Systems](https://www.windley.com/archives/2021/04/legitimacy_and_decentralized_systems.shtml) 2021-04 Windley
  > Why are some decentralized systems accepted and widely used while others wither? Why do some “hard forks” succeed while others fail? It all comes down to legitimacy.
* [Why Distributed Ledger Technology (DLT) for Identity?](https://www.hyperledger.org/blog/2021/04/21/why-distributed-ledger-technology-dlt-for-identity) 2021-04-21 Hyperledger
  > So why DLT? First, we can get the good parts of paper credentials—private transactions between holders and verifiers and no callback to the issuer. Second, the issuer gets a trusted, open and transparent way to publish the cryptographic material needed for those private holder-verifier transactions. Third, there is no need to have a “Trusted Third Party” participating in the interactions.
  > 
  > And did I mention, no private data goes on the DLT!!!
* [Digital Identity and Blockchain – Its Place in Newer Identity Models](https://cyber.ee/blog/2021/04-21/) 2021-04-21
  > In the [first part of this series](https://cyber.ee/blog/2021/04-14/), we introduced the idea that traditional PKI-based digital identity solutions can potentially benefit from blockchain technology.
  > [...]
  > For this next part of the series, we’ll touch on the relatively new idea of self-sovereign identity, or SSI.
* [Blockchain is the Least Interesting Thing About Self-sovereign Identity](https://medium.com/trinsic/blockchain-is-the-least-interesting-thing-about-self-sovereign-identity-75c1b56ce497) 2020-09-23 Riley Huges
  > as useful as blockchain is for SSI, it’s nowhere near as interesting as:
  > - The impact on the internet
  > - The benefits of technical standards
  > - The economic opportunity for early innovators
* [Video] [Identity and Distributed Ledger - Today and Tomorrow - June 26 - Identiverse 2019](https://www.youtube.com/watch?v=l04AHP7kPPw) 2019-06-26
  > Join our expert panel, moderated by Paul Madsen, as they discuss and debate the future of distributed identity technology and its applications in solving identity problems.
* [If ledger isn’t used, then every issuer of a credential has to maintain infrastructure](https://twitter.com/windley/status/1071469217650638848) 2018-12-09 Phil Windley
  > or contract service provider to respond to DID resolution & revocation requests. And, credential issuers would know when the credential was used, impacting privacy.
* [Part 3: Blockchange and Identity – The Foundational Use Case](https://blockchan.ge/fieldreport/identity.html) GovLab 2018-11-01
  > The contemporary IAM literature focuses on two central types of identity. The first is foundational identity, which is usually equated with legal identity. Here, after collecting attributes, individuals are issued a unique ID that is legally recognized at the national level and can be used to access different services. Legal IDs are almost always issued by the state in a centralized fashion. National ID cards are perhaps the best example of a foundational identity.
  > 
  > The second type is called functional or transactional ID. In this case, a particular entity, public or private, issues individuals or customers a unique ID that is only valid for the specific purposes previously established by the issuing entity. Electoral identities, health or car insurance cards, and ecommerce login credentials are good examples.
* [Blockchain Identity – Success Factors and Challenges](https://www.kuppingercole.com/blog/kuppinger/blockchain-identity-success-factors-and-challenges) 2018-05-16 Martin Kuppinger
  > When new things arrive, which are still in the pioneering stage and far from reaching maturity, there is always a lot of discussion. This is even more true for Blockchain Identity, where the massive hype around Blockchains, a long history of clever ideas failing, and a few interesting technical and security challenges come together. During my keynote at this year’s EIC, I addressed the challenges and success factors for Blockchain ID as well. That led to a discussion on Twitter about whether some of these success factors are contradictory.
  ![](https://i.imgur.com/bMbh6N7.png)
* [Is putting hashed PII on any immutable ledger(blockchain) is a bad Idea](https://identitywoman.net/putting-hashed-pii-immutable-ledgerblockchain-bad-idea/) 2018-02-03 Identity Woman
  > I decided to open a thread On Twitter for ID & security professionals to share why (/if) putting hashed PII on any immutable ledger(blockchain) is a bad Idea.\
  > Not everyone agreed that it was bad if certain things were done right.\
  > There were 15 direct responses and then a whole lot of subthreads.
* [Video] [Blockchain-Anchored Identity – A Gateway to Decentralized Apps and Services](https://www.youtube.com/watch?v=hUYpvI43bHA) 2017-05-10 Daniel Buchner
  > Blockchains possess unique properties that can be used to build systems that significantly impact our world. Perhaps no area of utilization, besides raw value exchange, is as intriguing as decentralized identity. In this talk we will discuss how blockchain-anchored decentralized identity can be used as a substrate for secure, user-centric apps and services.
* [Self-Sovereign Identity and the Legitimacy of Permissioned Ledgers](http://www.windley.com/archives/2016/09/self-sovereign_identity_and_the_legitimacy_of_permissioned_ledgers.shtml) 2016-09
  > This post justifies the claim that an identity system based on a permissioned distributed ledger is legitimately self-sovereign. The post also examines the claims to legitimacy that social login and distributed ledger identity systems make.
* [Blockchain for Identity - Myth or Potential](https://www.kuppingercole.com/blog/kuppinger/blockchain-for-identity-myth-or-potential) 2018-06-16
  > Authentication might definitely become simpler, by having various authenticators and IDs, from eIDs to social logins, associated with a wallet. Just one simple store to get access. Yes, there are challenges in creating secure, easy-to-use wallets, but there is potential as well.
  ![](https://i.imgur.com/YSyv11h.png)

## Do you need a blockchain?

* [SSI-on-Blockchain is Objectively a Bad Thing](https://weh.wtf/ssi.html) 2022-07-08 Niko
  > “Blockchain” in SSI exists for PR only, not for engineering reasons.\
  > Note: I am only going to talk about the “blockchain” part of Self-sovereign Identity. Many things, good and bad, can be said about self-sovereign identity, but in order to keep the scope of this document manageable, I’ll leave the broader SSI-discussion to others.
* [Self Sovereign Identity ≠ Blockchain](http://web.archive.org/web/20211205223357/https://jolocom.io/blog/dezentrale-identitaten-%E2%89%A0-blockchain-2/) 2021-11-09 Jolocom
  > Due to the ID-Wallet project in Germany, some articles and comments have equated Self Sovereign Identity (SSI) with blockchain technology in the last few weeks. The impression is given that SSI only works in conjunction with a blockchain. Spoiler, that’s not the case.
* [Do You Need Blockchain for Enabling SSI?](https://academy.affinidi.com/do-you-need-blockchain-for-enabling-ssi-452d62b34890) 2021-08-13 Affinidi
  > We hope this will get you thinking about enabling SSI using an option that best suits your application or business requirement.
* [tweet thread] [Technically you're right. Blockchain is not inherent to DIDs](https://twitter.com/Steve_Lockstep/status/1425924860312645633) 2021-08-13 Steve Wilson
  > Most DID presentations (as with much SSI) open with a bit of a disclaimer that these technologies don't need blockchain. And yet the word-association is strong. Many DID block diagrams feature a blockchain. -/2