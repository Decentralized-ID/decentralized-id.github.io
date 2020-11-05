---
date: 2019-03-08
title: Microsoft Identity
excerpt: >
  Microsoft believes everyone has the right to own their digital identity, one that securely and privately stores all personal data. This ID must seamlessly integrate into daily life and give complete control over data access and use.
layout: single
permalink: companies/microsoft/
canonical_url: 'https://decentralized-id.com/companies/microsoft/'
redirect_from: 
  - private-sector/microsoft/
  - id-initiatives/microsoft/
  - id-initiatives/microsoft
categories: ["Companies"]
tags: ["Microsoft","DID","ION","DIF","Transmute","Consensys","Blockstack"]
last_modified_at: 2020-11-05
---

![](https://i.imgur.com/MEN8iSn.png)


## News

> Today, we’re announcing an early preview of a [Sidetree-based DID network, called ION](https://techcommunity.microsoft.com/t5/Azure-Active-Directory-Identity/Toward-scalable-decentralized-identifier-systems/ba-p/560168) (Identity Overlay Network) which runs atop the Bitcoin blockchain based on an emerging set of open standards that we’ve developed working with many of our partners in the Decentralized Identity Foundation. This approach greatly improves the throughput of DID systems to achieve tens-of-thousands of operations per second

* [Introducing Element](https://medium.com/transmute-techtalk/introducing-element-328b4260e757)
  > Transmute is excited to announce Element, an implementation of the Sidetree Protocol on top of Ethereum and IPFS. This work was done in collaboration with Microsoft and Consensys under the Decentralized Identity Foundation (DIF)


## didproject.azurewebsites.net

* [didproject.azurewebsites.net](https://didproject.azurewebsites.net/)
* [Microsoft Azure Own your identity](https://azure.microsoft.com/en-us/overview/decentralized-identity/)
* [didproject.azurewebsites.net/docs](https://didproject.azurewebsites.net/docs/overview.html) 
  >We plan to add new technologies and features to this website over time. Here are some investments we currently have planned:
  > * DID standards & test methods - The W3C CCG has a draft spec for representing decentralized identities, allowing identities to be registered on different distributed ledgers while maintaining compatibility. To provide a reference implementation, a test DID method is built that allows temporary creation and usage of decentralized identities. This allows additional development to continue while progress is made on real DID methods.
  > * Authentication & initial APIs - Protocols for authenticating decentralized identities using public key credentials are proposed. A reference implementation with javascript APIs is built that allows a website to authenticate a decentralized identity. A sample user agent application is open sourced that demonstrates proper usage of the proposed protocols using a test DID method.
Standardization continues
  > * Ongoing -  Work continues between members of the decentralized identity foundation and other standards bodies to revise, refine, and formalize standards for decentralized identities. Topics include identifiers names & discovery, authentication protocols, storage and compute, claims and credentials, and more.
  > * Data storage in identity hubs - Identity hubs provide secure data storage for any information associated with an identity. Profile information, personal files, government issued documents, and more. Identity hubs offer users tools for controlling and reviewing access to their data, so that information can be confidently and privately shared with other parties. Data storage and retreival is based on industry standards to ensure that users have their choice of how and where to run their identity hub. Information in identity hubs can also be replicated to multiple instances of hubs to maintain the advantages of decentralization.
  > * Scaling registration of identities -Registration of identities on a distributed ledger typically requires a transaction to be submitted to the ledger's network. To offer decentralized identities to users at scale, a solution is needed to increase the throughput and or latency of an identity registration. SideTree is a proposed layer two protocol that can help address these problems and enable identity registration that works at real world scale.
  > * Key recovery mechanisms - To use decentralized identities, users must be able to secure private keys while using them to perform daily tasks and operations. Should a private key be lost or compromise, users run the risk of losing access to all of their online assests and personal data. Mechanisms are needed to help users avoid problems with their private keys and to recover from problems when they do happen.
  > * Mobile user agents - Easy to use and secure user agents are a critical component to decentralized identity. Mobile applications can help users secure their identity's private keys, respond to incoming requests, and manage access to their personal data.

* [DID Registration](https://didproject.azurewebsites.net/docs/registration.html)
  >The way you claim a DID and publish your public keys depends on which distributed ledger you use to register your DID. Each ledger has its own rules, formats, and quirks. Thankfully, the DID standard defines common ways to deal with DIDs, and our services expose the standard to you in a simple web API. Currently, we're developing support for the following ledgers:
  >
  >* Bitcoin
  >* Ethereum, via uPort
  >* Sovrin

## Whitepaper
* [Microsoft’s strategy for Decentralized Identity](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE2DjfY)] **to empower every person on the planet to achieve more.**
  >Microsoft cloud identity systems already empower developers, organizations, and billions of people to work, play, and achieve more, but there’s so much more we can do to create a world where each of us, even in displaced populations, can pursue our life goals, including educating our children, improving our quality of life, and starting a business.To achieve this vision, we need to augment existing cloud identity systems with one that individuals, organizations, and devices can own so they can control their digital identity and data. This self-owned identity must seamlessly integrate into our daily lives, providing complete control over what we share and with whom we share it, and—when necessary—provide the ability to take it back. Instead of granting broad consent to countless apps and services and spreading their identity data across numerous providers, individuals need a secure, encrypted digital hub where they can store their identity data and easily control access to it.

## [Microsoft Identity Standards Blog](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/bg-p/IdentityStandards)

* [All about FIDO2, CTAP2 and WebAuthn](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/All-about-FIDO2-CTAP2-and-WebAuthn/ba-p/288910)
  > To understand how FIDO2 authenticators work, you need knowledge of two specifications in two different standards bodies.  The WebAuthentication (aka WebAuthn) spec lives at W3C (where the browser makers meet) while the Client-to-Authenticator (aka CTAP2) spec lives at the FIDO Alliance (where hardware and platform folks have joined to solve the problem of Fast IDentity Online). 
* [Why does standards certification matter?](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/Why-does-standards-certification-matter/ba-p/638937)
  > It’s a good month for identity certification at Microsoft! We are excited to have achieved two important goals: OpenID Certification for Azure Active Directory and also FIDO Certification for Windows 10. You may or may not know what these particular protocols do, but even if you don’t, it’s worth talking about what these certification programs accomplish.
* [Why WebAuthn will change the world](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/Why-WebAuthn-will-change-the-world/ba-p/482286)
  >With WebAuthn, any web entity can call a simple Javascript API and ask for a cryptographically secure credential.   What happens next is pretty cool – the world’s browsers have worked with the world’s operating system makers and the world’s hardware manufacturers, so that when a website asks for a credential, the browsers work with the underlying platform to securely locate compliant local hardware and talk to it!   
* [To Understand WebAuthn, Read CredMan](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/To-Understand-WebAuthn-Read-CredMan/ba-p/339652)
  > take a cruise through the [W3C Credential Management (aka CredMan) specification](https://www.w3.org/TR/credential-management-1/) first.  CredMan sets up the object model for the Credential object model that WebAuthn's PublicKeyCredential extends.  
  >
  > **CredMan Base Definitions**
  >
  > CredMan unsurprisingly centers on the concept of a Credential.  Actions on Credentials are requested by a relying party using JavaScript and fulfilled by a user agent (generally a browser). Credentials can be created stored, retrieved for validation by a relying party and so on.  In addition to actions, CredMan defines standardized dictionaries that communicate context.

## History


6/16 — [Microsoft Building Open Blockchain-Based Identity System With Blockstack, ConsenSys](https://bitcoinmagazine.com/articles/microsoft-building-open-blockchain-based-identity-system-with-blockstack-consensys-1464968713/)

[![](https://imgur.com/l0NEfjrl.png)](https://www.microsoft.com/en-us/security/technology/own-your-identity)
* [microsoft.com/en-us/security/technology/own-your-identity](https://www.microsoft.com/en-us/security/technology/own-your-identity)
* [Mastercard, Microsoft Join Forces to Advance Digital Identity Innovations](https://newsroom.mastercard.com/press-releases/mastercard-microsoft-join-forces-to-advance-digital-identity-innovations/)
* [Decentralized digital identities and blockchain: The future as we see it](https://www.microsoft.com/en-us/microsoft-365/blog/2018/02/12/decentralized-digital-identities-and-blockchain-the-future-as-we-see-it/)
* [Microsoft is quietly testing a project that aims to hand people complete control over their online data](http://www.businessinsider.fr/us/microsoft-working-on-project-bali-to-give-people-control-over-data-2019-1)
 

