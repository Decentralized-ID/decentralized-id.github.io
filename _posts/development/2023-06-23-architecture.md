---
title: System Architecture and Self Sovereign Identity
excerpt: >
  In chaotic systems such as those that the discipline of physics seeks to describe, there is also the concept of the “self-organizing principle,” which dictates a tendency for chaotic systems to organize themselves. While this might be a tendency in physics, organization usually needs a nudge in the right direction in the identity world.
description: Authentication and authorization both fall under identity and access management (IAM) but serve different purposes.
layout: single
toc: false
permalink: /development/architecture/
canonical_url: 'https://decentralized-id.com/development/architecture/'
categories: ["Development"]
tags: ["Architecture"]
last_modified_at: 2023-06-23
---

* [Centralized\Federated vs Self Sovereign](https://twitter.com/dominiumssi/status/1564188374529081345) 2022-08-29 dominiumssi
  > Anyone who wants to understand DID and Self Sovereign Identity should begin by understanding the graph below. We are shifting the power from the companies to the users.  That's it in a nutshell.
  > ![](https://pbs.twimg.com/media/FbUcnNNacAAUnAs?format=png&name=small)
* [Good Welfare, Bad Platforms?: The Risks of Centralized Digital Identity Systems](https://points.datasociety.net/good-welfare-bad-platforms-d65b412d962e) 2022-02-02 OpenID
  > As S. Shakthi and I noted in a recent [research paper](https://journals.openedition.org/samaj/6279), digital identity systems are widely seen as datafiers by virtue of their core property of reducing the person to machine-readable data. A datafier is a system that performs the crucial operation of converting the physical into digital. A different, contrasting view is also emerging in research: digital identity systems are increasingly seen as platforms, i.e. “technological building blocks” on which different types of complements can be constructed.
* [Leveraging the Identity Metasystem](https://www.windley.com/archives/2021/12/leveraging_the_identity_metasystem.shtml) 2021-12 Phil Windley
  > the [metasystem guarantees the fidelity of the credential exchange](https://www.windley.com/archives/2021/06/ssi_interaction_patterns.shtml). Credential fidelity comprises four important attributes. Credential exchange on the identity metasystem:
  > 
  > 1. Reveals the identifier of the issuer
  > 2. Ensures the credential was issued to the party presenting it
  > 3. Ensures the credential has not been tampered with
  > 4. Reveals whether or not the credential has been revoked
* [Token-Based Identity](https://www.windley.com/archives/2021/10/token-based_identity.shtml) 2021-10 Phil Windley
  > Token-based identity systems move us from talking about who, to thinking about what, so that people can operationalize their digital lives. Token-based identity systems support complex online interactions that are flexible, ad hoc, and cross-domain.
* [The Basic Building Blocks of SSI](https://freecontent.manning.com/the-basic-building-blocks-of-ssi/) 2020-07-29 Drummond Reed, Alex Preukschat Manning
  > In many cases these core concepts have been established for decades. What’s new is how they’re put together to create a new model for digital identity management. The purpose of this article is to quickly familiarize you with these seven basic building blocks from a conceptual and technical point-of-view.
  > - Verifiable credentials (aka digital credentials)
  > - Issuers, holders, and verifiers
  > - Digital wallets
  > - Digital agents and hubs
  > - Decentralized identifiers (DIDs)
  > - Blockchains
  > - Governance frameworks (aka trust frameworks)
* [Your User is Your API](https://www.evernym.com/blog/your-user-is-your-api/) 2021-05-17 Evernym
  > The customer becomes the integration point. The customer is the API. Rather than having one huge, expensive, and probably illegal data hub, every customer becomes a data hub in their own right. They provide the data needed, just-in-time, under their control.
* [The Unbundling of Authentication vs Authorization - What You Need to Know](https://www.pingidentity.com/en/company/blog/posts/2021/authentication-vs-authorization.html) 2021-09-08 Ping Identity
  > Authentication and authorization are both processes that fall under the category of [identity and access management (IAM)](https://www.pingidentity.com/en/company/blog/posts/2017/what-is-identity-and-access-management-iam.html), but they serve different purposes.
* [The Buzz Behind Zero Trust](https://stateofidentity.libsyn.com/zero-trust-architecture) 2021-10-21 State of Identity
  > The Zero Trust model is the belief that no one should be trusted from inside or outside your network, until their identity has been verified. Zero trust refers to the alignment of maturing identity practices, an established understanding of user behaviors, and the application of least-privilege access security policy decisions to trust boundOaries
* [What Is Zero Trust?](https://www.pingidentity.com/en/company/blog/posts/2021/what-is-zero-trust.html) 2021 Ping
  > 1. The network is always assumed to be hostile.
  > 2. External and internal threats exist on the network at all times.
  > 3. Network locality is not sufficient for deciding trust in a network.
  > 4. Every device, user and network flow is authenticated and authorized.
  > 5. Policies must be dynamic and calculated from as many sources of data as possible.
* [Compare and Contrast — Federated Identity vs Self-sovereign Identity](https://academy.affinidi.com/compare-and-contrast-federated-identity-vs-self-sovereign-identity-227a85cbab18) 2021-04-26 Affinidi
  > The next step was a federated form of identity where third parties issued digital identity credentials using which users could log into other websites or services. Typically, these were your Google and Facebook logins. In the process, these third parties that issued federated identities became the middlemen.
* [The SSO Practitioner’s Introduction to Decentralized Identity](https://www.pingidentity.com/en/resources/blog/post/sso-practitioners-introduction-decentralized-identity.html) 2020-10-13
*Written for IAM professionals familiar with federations.*
  > In most self-sovereign and decentralized identity systems the trust model is  fundamentally unidirectional, where a verifier will trust the issuer, but the issuer may have no knowledge of the verifier.
* [The Architecture of Identity Systems](https://www.windley.com/archives/2020/09/the_architecture_of_identity_systems.shtml) 2020-09 Phil Windley 
  >  We can broadly classify identity systems into one of three types based on their architectures and primary root of trust:
  > - Administrative
  > - Algorithmic
  > - Autonomic
* [Never mind who I am, ask me about my credentials](https://www.linkedin.com/pulse/never-mind-who-i-am-ask-me-my-credentials-john-phillips/) 2020-02-09 John Phillips
  > Many (most) identity systems make a fundamental assumption that is built into their very architecture. This assumption creates three significant problems: privacy erosion; toxic data stores; and poor security.
* [Decentralized Identity Trilemma](https://maciek.blog/p/dit) 2018-08-13 Maciek Laskus
  > 1. Self-sovereignty — anybody can create and control as many identities1 as they wish without 3rd party involvement.
  > 2. Privacy-preserving — one can acquire and utilize an identifier without revealing their ‘real name’ or other personality identifying information.
  > 3. Sybil-resistant — identity is subject to scarcity; i.e., creating more identifiers cannot be used to manipulate a system2.
* [Self-Sovereign vs Administrative Identity](http://blogs.harvard.edu/vrm/2012/03/25/ssi/) 2012-03-25 Doc Searls 
  > The problem I’m trying to surface here is that we need full respect for self-sovereign identities, and identifiers, before we can solve the problem of highly fractured and incompatible administrative identifiers — a problem that has only become worse with the growth of the Web, where by design we are always the submissive and dependent party: calves to administrative cows.
