---
title: "Principles and Characteristics of Self Sovereign Identity"
description: This page is devoted to leading thought around what are the most important characteristics of Self Sovereign Identity.
excerpt: >
  There are a few different ways to approach and describe SSI. What I aim to do is come up with a list of different "SSI Cases" to modularize the treatment of the subject. This will allow each to contribute in the way that makes most sense for themselves, rather than trying to discuss SSI as a whole in a single whitepaper.
layout: single
redirect_from:
  - /self-sovereign-identity/ssi-principles-vs-characteristics
  - /self-sovereign-identity/ssi-principles-vs-characteristics/
  - /literature/self-sovereign-identity/ssi-principles-vs-characteristics/ 
  - /self-sovereign-identity/evolution-of-ssi/
  - /self-sovereign-identity/evolution-of-ssi
  - /literature/self-sovereign-identity/evolution-of-ssi
  - /literature/self-sovereign-identity/evolution-of-ssi/
permalink: /self-sovereign-identity/characteristics/
canonical_url: 'https://decentralized-id.com/self-sovereign-identity/characteristics/'
categories: ["About"]
tags: ["Self Sovereign Identity","notes","Literature","lifeID","RWoT","Laws of Identity","Literature","UNSDGs","Windhover Principles","History"]
last_modified_at: 2023-06-24
---

## The Path to Self Sovereign Identity
Christopher Allen's seminal work, [The Path to Self Sovereign Identity](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html), helped to concretize and proliferate the ideals behind, and movement towards, Self Sovereign Identity. 

His article details the history of digital identity standards, and the user experience accompanying those standards. After describing from where we've come, Allen draws from leading thought on digital identity to compose the [Principles of Self Sovereign Identity](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md). 

### Principles of Self Sovereign Identity

1. **Existence.** *Users must have an independent existence.* Any self-sovereign identity is ultimately based on the ineffable “I” that’s at the heart of identity. It can never exist wholly in digital form. This must be the kernel of self that is upheld and supported. A self-sovereign identity simply makes public and accessible some limited aspects of the “I” that already exists.
2. **Control.** *Users must control their identities.* Subject to well-understood and secure algorithms that ensure the continued validity of an identity and its claims, the user is the ultimate authority on their identity. They should always be able to refer to it, update it, or even hide it. They must be able to choose celebrity or privacy as they prefer. This doesn’t mean that a user controls all of the claims on their identity: other users may make claims about a user, but they should not be central to the identity itself. 
3. **Access.** *Users must have access to their own data.* A user must always be able to easily retrieve all the claims and other data within his identity. There must be no hidden data and no gatekeepers. This does not mean that a user can necessarily modify all the claims associated with his identity, but it does mean they should be aware of them. It also does not mean that users have equal access to others’ data, only to their own.
4. **Transparency**. *Systems and algorithms must be transparent.* The systems used to administer and operate a network of identities must be open, both in how they function and in how they are managed and updated. The algorithms should be free, open-source, well-known, and as independent as possible of any particular architecture; anyone should be able to examine how they work.
5. **Persistence.** *Identities must be long-lived.* Preferably, identities should last forever, or at least for as long as the user wishes. Though private keys might need to be rotated and data might need to be changed, the identity remains. In the fast-moving world of the Internet, this goal may not be entirely reasonable, so at the least identities should last until they’ve been outdated by newer identity systems. This must not contradict a “right to be forgotten”; a user should be able to dispose of an identity if he wishes and claims should be modified or removed as appropriate over time. To do this requires a firm separation between an identity and its claims: they can't be tied forever.
6. **Portability.** *Information and services about identity must be transportable.* Identities must not be held by a singular third-party entity, even if it's a trusted entity that is expected to work in the best interest of the user. The problem is that entities can disappear — and on the Internet, most eventually do. Regimes may change, users may move to different jurisdictions. Transportable identities ensure that the user remains in control of his identity no matter what, and can also improve an identity’s persistence over time.
7. **Interoperability.** *Identities should be as widely usable as possible.* Identities are of little value if they only work in limited niches. The goal of a 21st-century digital identity system is to make identity information widely available, crossing international boundaries to create global identities, without losing user control. Thanks to persistence and autonomy these widely available identities can then become continually available.
8. **Consent.** *Users must agree to the use of their identity.* Any identity system is built around sharing that identity and its claims, and an interoperable system increases the amount of sharing that occurs. However, sharing of data must only occur with the consent of the user. Though other users such as an employer, a credit bureau, or a friend might present claims, the user must still offer consent for them to become valid. Note that this consent might not be interactive, but it must still be deliberate and well-understood.
9. **Minimalization.** *Disclosure of claims must be minimized.* When data is disclosed, that disclosure should involve the minimum amount of data necessary to accomplish the task at hand. For example, if only a minimum age is called for, then the exact age should not be disclosed, and if only an age is requested, then the more precise date of birth should not be disclosed. This principle can be supported with selective disclosure, range proofs, and other zero-knowledge techniques, but non-correlatibility is still a very hard (perhaps impossible) task; the best we can do is to use minimalization to support privacy as best as possible. 
10. **Protection.** *The rights of users must be protected.* When there is a conflict between the needs of the identity network and the rights of individual users, then the network should err on the side of preserving the freedoms and rights of the individuals over the needs of the network. To ensure this, identity authentication must occur through independent algorithms that are censorship-resistant and force-resilient and that are run in a decentralized manner. 

#### Related

* [Principles or Cult - An Irreverant Discussion on the Principles of SSI](https://www.thedinglegroup.com/blog/2021/9/1/principles-or-cult-an-irreverant-discussion-on-the-principles-of-ssi) 2021-09-01 Dingle Group
  > The evolution of the Principles of SSI came about through the need to differentiate what is ‘true’ SSI versus marketing forces twisting the concept. This market driven motivator can bring cultish overtones to the process.
* [Self-Sovereign Bill of Rights](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-bill-of-rights.md) 2019-07-05 lifeID [Article](https://medium.com/@lifeID_io/lifeid-self-sovereign-identity-bill-of-rights-d2acafa1de8b)
  >  There is a definitional gap to be filled, establishing what we think are the foundational attributes of a truly self-sovereign identity. It is our goal to inspire discussion and agreement within our community for what comprises a self-sovereign identity to ensure the success, integrity and sustainability of these solutions for people throughout the world.
  > 
  > In light of this, we hold these truths to be self-evident features of any self-sovereign identity solution.
* [Schutte’s Critique of the Self-Sovereign Identity Principles](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/Schutte-on-SSI.md) 2016-10-26 Rebooting Web of Trust
  > I’m taking a quick pass through Christopher Allen’s 10 principles for Self-Sovereign Identity, with an eye toward highlighting the primary shortcomings that I perceive. Note: I have a very unusual take on this. I understand that. I’m trying to be guided primarily by how mechanisms of coherence formation, perception and interaction amongst agents operate in complex adaptive systems.

## Opening Up the Conversation

> The idea of digital identity has been evolving for a few decades now, from centralized identities to federated identities to user-centric identities to self-sovereign identities. However, even today exactly what a self-sovereign identity is, and what rules it should recognize, aren’t well-known.
> 
> This article seeks to begin a dialogue on that topic, by offering up a definition and a set of principles as a starting point for this new form of user-controlled and persistent identity of the 21st century. - [The Path to Self Sovereign Identity](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/ThePathToSelf-SovereignIdentity.md) 2016-04 Rebooting Web of Trust

It was intended for that article to help open the conversation, not necessarily define the movement. All the same, the [Principles of Self Sovereign Identity](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md) have remained a guiding beacon for the development of Self Sovereign Identity systems.

That, said, the principles don't represent the entirety of thought on necessary characteristics for Sovereign identity systems. This page is devoted to continued thought around what are the most important characteristics of Self Sovereign Identity.

### A Technology Free Definition of Self Sovereign Identity
That October, [Joe Andrieu](https://github.com/jandrieu) submitted [A Technology‐Free Definition of Self‐Sovereign Identity](https://github.com/jandrieu/rebooting-the-web-of-trust-fall2016/raw/master/topics-and-advance-readings/a-technology-free-definition-of-self-sovereign-identity.pdf) to the third Rebooting the Web of Trust Design Workshop. Within it, he describes the Characteristics of SSI: **Control**, **Acceptance**, and **Zero Cost**.

>1 No disrespect to Christopher Allen’s opening to the conversation, The Path to Self Sovereign Identity [...] It gets a lot right, but leaves a few requirements out, e.g., recoverability and zero cost, and conflates “identities” and claims in an ambiguous manner.

#### Fundamental Characteristics of Self-Sovereign Identity
* **CONTROL** - Self‐sovereign identities are controlled by the individual
   * **Self‐generatable and Independent** 
     > Individuals must be able to create identity information without asking for permission and be able to assert identity information from any authority.
   * **Opt‐in**
     > The affordance for asserting identity information starts with the individual. 
   * **Minimal Disclosure**
     > Individuals should be able to use services with minimal identity information. 
   * **Non‐participation**
     > Individuals must be able to choose to not provide identity information for services where it isn’t absolutely required. 
   * **Opt‐out**
     > Individuals should be able to opt‐out of identifying records post‐facto as a matter of course.
   * **Recoverable** 
     > Sovereign identities must be robust enough to be recovered even if hard drives are lost, wallets stolen, or birth certificates lost in a fire. 
* **ACCEPTANCE** - Self‐sovereign identities are accepted wherever observers correlate individuals across contexts.
   * **Standard**: 
     > The core standard (schema, serialization, and protocols) must be atomically minimal, providing the barest data set, allowing complexity to emerge not from a complicated data model but from a multiplicity of information types, authorities, and observations. 
   * **Non‐repudiatable**: 
     > Self‐sovereign identities, at a minimum depend on cryptographic assurances, and most likely will be further enabled by non‐repudiatable public ledgers. 
   * **Reliable**: 
     > Access to self‐sovereign identities must be at least as reliable as access to the Internet.
* **ZERO COST** - Finally, any proposed standard for self‐sovereign identity must be adoptable at absolutely minimal cost. 
  > The systems we use to make sense of the resulting identity transactions will provide more than enough consulting, software, and hardware revenue to finance the development of the core enabling technology. Just as the web browser was a zero cost entry into a vast economic and innovation engine of the world‐wide web, so too must self‐sovereign identity begin with the most cost‐effective on‐ramp that can be engineered. 

## Furthering the Discussion
* [The Mental Models of Identity Enabled by SSI](https://ssi-ambassador.medium.com/the-mental-models-of-identity-enabled-by-ssi-d3e2d8d0f2b6) 2020-12-03 Adrian Doerk 
*The Models: Space Time • Presentation • Attribute • Relationship • Capability*
  > The following five mental models describe what people refer to, when speaking about identity and provide a useful structure of how these models can be executed in a digital environment leveraging SSI infrastructure and components.
* [The Three Pillars of Self-Sovereign Identity](https://www.evernym.com/blog/the-three-pillars-of-self-sovereign-identity/) 2019-12-10 Evernym
  > When implemented for the purpose of identity, everyone everywhere can issue, hold, and verify any credentials about anything. This means no more proprietary silos “owning” your identity. The combination of human and cryptographic trust in this environment means that you can finally get increased security and reduced friction at the same time.
* [The 5P’s of a Self-Sovereign Identity](https://markvanrijmenam.medium.com/the-5ps-of-a-self-sovereign-identity-e6f6eb802d75) 2019-06-05 Dr Mark van Rijmenam
  > A self-sovereign identity can be defined by the 5P’s as it is personal (it is about you), portable (meaning you can take your identity and data from one platform to another), private (you control your identity and data), persistent (it does not change without your consent) and protected (they cannot steal your identity).
* [LESS identity](https://medium.com/@trbouma/less-identity-65f65d87f56b) 2018-12-09 Tim Bouma
  > I arrived at the term ‘Less Identity’ through some fun wordplay (yes, I do this stuff in my spare time). I was thinking about ‘Trust Frameworks’ and ‘Trustless Networks.’ When I factored out the common ‘Trust’, I arrived at ‘Trust[Less Networks and Frameworks].’
* [The Domains of Identity & Self-Sovereign Identity -- Presentation from Kaliya Young](https://www.youtube.com/watch?v=U8bZ4GYFwKY) 2018-11-06 New America
  > Kaliya Young (“The Identity Woman”) explains 16 domains of identity ~~-variously related to government, civil society, commerce, employment, and the data broker industry-~~ as presented in her [recent report](https://www.amazon.com/Domains-Identity-Understanding-Contemporary-Collection/dp/1785274910). Kaliya then explains how SSI can fundamentally alter the relationships within these domains.
* [A Primer on Functional Identity](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/functional-identity-primer.md) 2017-08-26 Joe Andrieu rwot05-boston
  > Unfortunately, digital systems can unwittingly compromise real-world identity. Sometimes this occurs because digital identity systems neglect to consider external effects. Other times, it happens with systems that didn’t even realize they were dealing with identity-related personal information. A functional perspective allows engineers to see beyond static attributes and traditional notions of “Personally Identifiable Information” to better understand how engineering choices can impact identity, even outside their systems.

## Background
**Greatly influential on later thinking around digital identity and the development of Self Sovereign Identity**
* [Kim Cameron Identity Laws](https://www.identityblog.com/?p=352) 2005-05-13 IdentityBlog [Whitepaper](https://www.identityblog.com/stories/2005/05/13/TheLawsOfIdentity.pdf)
  > Summary: Understand the dynamics causing digital identity systems to succeed or fail in various contexts, expressed as the Laws of Identity. Together these laws define a unifying identity metasystem that can offer the Internet the identity layer it needs. (14 printed pages)

**Shows an early use of 'sovereign' in relation to our internet identities**
* [*What is Sovereign Source Authority?*](https://www.moxytongue.com/2012/02/what-is-sovereign-source-authority.html) 2012-02
  > What is required for structural integrity of a Sovereign domain originated of, by, for people?\
  > A [recursive signatory](https://www.moxytongue.com/2021/07/recursive-signatory.html) is starting point for an accurate self-sourced method that repeats, generation after generation, person after person, such that no second-class process supersedes the inherent requirement for functional Rights.

**The term "Self Sovereign Identity" started becoming widely used in 2014**
* [The Windhover Principles for Digital Identity, Trust, and Data](https://www.scribd.com/document/335386296/Windhover-Principles) 2014-09-21 Institute for Data Driven Design 
  > 1. Self-Sovereignty of Digital Identity and Personal Data:
  > Individuals and groups should have control of their digital personal identities and personal data. 
* [HubID First to Deploy Windhover Principles and Framework for Digital Identity, Trust and Open Data](https://hubculture.com/hubs/47/news/689/) 2014-10-20
  > HubID, the self-sovereign digital identity system at the core of Hub Culture and the Ven currency, is the first consumer application to deploy the Windhover Principles and new frameworks for digital identity, trust and open data. The core technology has been in development with the Open Mustard Seed framework and quietly began use in July 2014 following a development announcement with ID3 in January 2014 at the World Economic Forum in Davos.

**This article popularized the idea and term Self Sovereign Identity**
* [The Path to Self-Sovereign Identity](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/ThePathToSelf-SovereignIdentity.md) 2016-04-25 Christopher Allen Popularized the concept of Self-Sovereign Identity
  > Since then, the idea of self-sovereign identity has proliferated. Loffreto has blogged how the term has evolved13. As a developer, he shows one way to address self-sovereign identity: as a mathematical policy, where cryptography is used to protect a user’s autonomy and control. However, that’s not the only model. Respect Network instead addresses self-sovereign identity as a legal policy; they define contractual rules and principles that members of their network agree to follow14. The Windhover Principles For Digital Identity, Trust and Data15 and Everynym’s Identity System Essentials16 offer some additional perspectives on the rapid advent of self-sovereign identity since 2012.