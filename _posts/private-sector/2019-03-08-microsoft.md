---
date: 2019-03-08
title: Microsoft Identity
excerpt: >
  Microsoft believes everyone has the right to own their digital identity, one that securely and privately stores all personal data. This ID must seamlessly integrate into daily life and give complete control over data access and use.
layout: single
permalink: private-sector/microsoft/
canonical_url: 'https://decentralized-id.com/id-initiatives/microsoft/'
redirect_from: 
  - id-initiatives/microsoft/
  - id-initiatives/microsoft
categories: ["Private-sector"]
tags: ["Microsoft","DID","ION"]
last_modified_at: 2019-07-11
---

![](https://i.imgur.com/MEN8iSn.png)


[![](https://imgur.com/l0NEfjrl.png)](https://www.microsoft.com/en-us/security/technology/own-your-identity)
* [microsoft.com/en-us/security/technology/own-your-identity](https://www.microsoft.com/en-us/security/technology/own-your-identity)


[![](https://imgur.com/K7sw9qp.png)](https://twitter.com/csuwildcat/status/1069890896504606720)

>[Just had an excellent convo](https://twitter.com/csuwildcat/status/1073690535838117889) with Dr. @BobMcElrath about the Layer 2 decentralized identifier protocol we're building (among other topics). Dude is smart and fun to talk with, check him out.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Good for Microsoft. Hopefully they can solve the daunting UX issues for personal data management at scale. <a href="https://t.co/jmMqz9fAfY">https://t.co/jmMqz9fAfY</a></p>&mdash; Evernym, Inc. (@evernym) <a href="https://twitter.com/evernym/status/1081019896207560704?ref_src=twsrc%5Etfw">January 4, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

* [Mastercard, Microsoft Join Forces to Advance Digital Identity Innovations](https://newsroom.mastercard.com/press-releases/mastercard-microsoft-join-forces-to-advance-digital-identity-innovations/)
* [Decentralized digital identities and blockchain: The future as we see it](https://www.microsoft.com/en-us/microsoft-365/blog/2018/02/12/decentralized-digital-identities-and-blockchain-the-future-as-we-see-it/)
* [Microsoft is quietly testing a project that aims to hand people complete control over their online data](http://www.businessinsider.fr/us/microsoft-working-on-project-bali-to-give-people-control-over-data-2019-1)


## didproject.azurewebsites.net

* [didproject.azurewebsites.net](https://didproject.azurewebsites.net/)
* [Microsoft Azure Own your identity](https://azure.microsoft.com/en-us/overview/decentralized-identity/)
* [didproject.azurewebsites.net/docs](https://didproject.azurewebsites.net/docs/overview.html) 
  >We plan to add new technologies and features to this website over time. Here are some investments we currently have planned:

* DID standards & test methods - The W3C CCG has a draft spec for representing decentralized identities, allowing identities to be registered on different distributed ledgers while maintaining compatibility. To provide a reference implementation, a test DID method is built that allows temporary creation and usage of decentralized identities. This allows additional development to continue while progress is made on real DID methods.
* Authentication & initial APIs - Protocols for authenticating decentralized identities using public key credentials are proposed. A reference implementation with javascript APIs is built that allows a website to authenticate a decentralized identity. A sample user agent application is open sourced that demonstrates proper usage of the proposed protocols using a test DID method.
Standardization continues
* Ongoing -  Work continues between members of the decentralized identity foundation and other standards bodies to revise, refine, and formalize standards for decentralized identities. Topics include identifiers names & discovery, authentication protocols, storage and compute, claims and credentials, and more.
* Data storage in identity hubs - Identity hubs provide secure data storage for any information associated with an identity. Profile information, personal files, government issued documents, and more. Identity hubs offer users tools for controlling and reviewing access to their data, so that information can be confidently and privately shared with other parties. Data storage and retreival is based on industry standards to ensure that users have their choice of how and where to run their identity hub. Information in identity hubs can also be replicated to multiple instances of hubs to maintain the advantages of decentralization.
* Scaling registration of identities -Registration of identities on a distributed ledger typically requires a transaction to be submitted to the ledger's network. To offer decentralized identities to users at scale, a solution is needed to increase the throughput and or latency of an identity registration. SideTree is a proposed layer two protocol that can help address these problems and enable identity registration that works at real world scale.
* Key recovery mechanisms - To use decentralized identities, users must be able to secure private keys while using them to perform daily tasks and operations. Should a private key be lost or compromise, users run the risk of losing access to all of their online assests and personal data. Mechanisms are needed to help users avoid problems with their private keys and to recover from problems when they do happen.
* Mobile user agents - Easy to use and secure user agents are a critical component to decentralized identity. Mobile applications can help users secure their identity's private keys, respond to incoming requests, and manage access to their personal data.

* [DID Registration](https://didproject.azurewebsites.net/docs/registration.html)
  >The way you claim a DID and publish your public keys depends on which distributed ledger you use to register your DID. Each ledger has its own rules, formats, and quirks. Thankfully, the DID standard defines common ways to deal with DIDs, and our services expose the standard to you in a simple web API. Currently, we're developing support for the following ledgers:
  >
  >* Bitcoin
  >* Ethereum, via uPort
  >* Sovrin
  >
  >Our intention is to be chain agnostic, enabling users to choose a DID variant that runs on their preferred ledger. Each ledger that is compliant with DID standards has an associated DID "method" - a set of rules that govern how DIDs are anchored onto a the ledger.

## Whitepaper
* [Microsoft’s strategy for Decentralized Identity](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE2DjfY)] **to empower every person on the planet to achieve more.**
  >Microsoft cloud identity systems already empower developers, organizations, and billions of people to work, play, and achieve more, but there’s so much more we can do to create a world where each of us, even in displaced populations, can pursue our life goals, including educating our children, improving our quality of life, and starting a business.To achieve this vision, we need to augment existing cloud identity systems with one that individuals, organizations, and devices can own so they can control their digital identity and data. This self-owned identity must seamlessly integrate into our daily lives, providing complete control over what we share and with whom we share it, and—when necessary—provide the ability to take it back. Instead of granting broad consent to countless apps and services and spreading their identity data across numerous providers, individuals need a secure, encrypted digital hub where they can store their identity data and easily control access to it.

## [Microsoft Identity Standards Blog](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/bg-p/IdentityStandards)

* [All about FIDO2, CTAP2 and WebAuthn](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/All-about-FIDO2-CTAP2-and-WebAuthn/ba-p/288910)
  >This is a great week to be working in Identity Standards, as we at Microsoft celebrate the release of our first ever WebAuthn Relying Party.  This one relying party enables standards-based passwordless authentication at Xbox, Skype, Outlook.com and more. But what are the actual pieces of the puzzle and how do they fit?  Read on for the big picture of how the W3C WebAuthn and FIDO2 CTAP2 specifications interact. We will start with the industry standards perspective, and then at the end we will summarize how Microsoft implements the various roles.
  > 
  >To understand how FIDO2 authenticators work, you need knowledge of two specifications in two different standards bodies.  The WebAuthentication (aka WebAuthn) spec lives at W3C (where the browser makers meet) while the Client-to-Authenticator (aka CTAP2) spec lives at the FIDO Alliance (where hardware and platform folks have joined to solve the problem of Fast IDentity Online). 

* [Why does standards certification matter?](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/Why-does-standards-certification-matter/ba-p/638937)
  >It’s a good month for identity certification at Microsoft! We are excited to have achieved two important goals: OpenID Certification for Azure Active Directory and also FIDO Certification for Windows 10. You may or may not know what these particular protocols do, but even if you don’t, it’s worth talking about what these certification programs accomplish.
  > 
  > The goal of certification in the standards world is to ensure conformance to protocols. In FIDO Certification, the tests are both physical and digital; for example, authenticators must prove that they are storing keys and secrets in a secure environment, such as a trusted platform module (TPM), and that the secure environment can only be used when a user gesture is performed. Resistance to physical attacks, such as side-channel attacks, must be demonstrated, as well as protocol conformance. A third party performs this certification, with the goal that anyone who uses a certified product can have reasonable confidence that the solution hasn’t cut any corners.
  >
  >The OpenID Certification is a different beast from FIDO Certification. Because OpenID Connect is a web protocol, there are fewer hidden parts; it’s easier for anyone to inspect and validate the protocol messages exchanged. The OpenID Certification process is therefore lighter weight and uses self-certification. With self-certification, those seeking certification run their own tests. The results of those tests are then published for scrutiny by all. In this case, the certifying organization is putting their reputation on the line. It isn’t a third party that claims adherence, it’s the owner of the implementation themselves. While those organizations could lie, most prioritize their reputation over any short-term gain that could come from misrepresentation.


* [Why WebAuthn will change the world](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/Why-WebAuthn-will-change-the-world/ba-p/482286)
  >A little over a month ago, W3C WebAuthn became a real internet specification.  Most of you don’t know what WebAuthn is yet, but many of you will feel the impact in short order.  In fact, I will go so far as to say that WebAuthn may change how we all authenticate to the resources we use every day. 
  >
  >We live in a world where the best parts of our individual local hardware and software collection are rarely leveraged to make cloud security decisions.  This is because there has never been a vendor-agnostic and privacy-preserving way for cloud resources to interact with individual hardware configurations in any generic way.  Until now! 
  >
  >With WebAuthn, any web entity can call a simple Javascript API and ask for a cryptographically secure credential.   What happens next is pretty cool – the world’s browsers have worked with the world’s operating system makers and the world’s hardware manufacturers, so that when a website asks for a credential, the browsers work with the underlying platform to securely locate compliant local hardware and talk to it!   

* [To Understand WebAuthn, Read CredMan](https://techcommunity.microsoft.com/t5/Identity-Standards-Blog/To-Understand-WebAuthn-Read-CredMan/ba-p/339652)
  >The holidays are well and truly over, time to get serious - now is the perfect time to read specifications! If you are planning to read the WebAuthn specification, you can ease into the terminology in a simple way - take a cruise through the [W3C Credential Management (aka CredMan) specification](https://www.w3.org/TR/credential-management-1/) first.  CredMan sets up the object model for the Credential object model that WebAuthn's PublicKeyCredential extends.  This post will be an overview of the CredMan spec, geared for folks who want to call the API as clients, not for those few and proud who are tasked with implementation of the API within a user agent.  
  >
  >**CredMan Base Definitions**
  >
  >CredMan unsurprisingly centers on the concept of a Credential.  Actions on Credentials are requested by a relying party using JavaScript and fulfilled by a user agent (generally a browser). Credentials can be created stored, retrieved for validation by a relying party and so on.  In addition to actions, CredMan defines standardized dictionaries that communicate context.  Note that the CredMan API itself does not use the term ‘relying party’ but instead refers to a developer that would write code using the navigator.credentials JavaScript control.  Since we are identity architects, we will assume that developed code is deployed and running as a service at a specific origin and that the developed code will call the CredMan API as part of user registration and authentication activities.   


 