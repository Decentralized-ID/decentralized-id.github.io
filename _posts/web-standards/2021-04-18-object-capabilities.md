---
date: 2021-04-18
title: "Object Capability Model"
description: in which a capability describes a transferable right to perform one (or more) operations on a given object.
excerpt: >
  Computer scientist E. Dean Tribble stated that in smart contracts, identity-based access control did not support well dynamically changing permissions, compared to the object-capability model. He analogized the ocap model with giving a valet the key to one's car, without handing over the right to car ownership.
categories: ["Web Standards"]
tags: ["oCap","JSON-LD","zCap","Cosmos"]
permalink: web-standards/object-capabilities/
last_modified_at: 2021-04-19
---

* [Awesome Object Capabilities and Capability-based Security](https://github.com/dckc/awesome-ocap)
  > Capability-based security enables the concise composition of powerful [patterns](https://github.com/dckc/awesome-ocap/wiki) of cooperation without vulnerability. [What Are Capabilities?](http://habitatchronicles.com/2017/05/what-are-capabilities/) explains in detail.
* [Object Capabilities - SourceCrypto](https://sourcecrypto.pub/#object-capabilities)
* [Object Capability Model](https://en.wikipedia.org/wiki/Object-capability_model) • [wiki.c2](https://wiki.c2.com/?ObjectCapabilityModel)
  > Computer scientist E. Dean Tribble stated that in smart contracts, identity-based access control did not support well dynamically changing permissions, compared to the object-capability model. He analogized the ocap model with giving a valet the key to one's car, without handing over the right to car ownership.
  > 
  > The structural properties of object capability systems favor modularity in code design and ensure reliable encapsulation in code implementation.
  > 
  > These structural properties facilitate the analysis of some security properties of an object-capability program or operating system. Some of these – in particular, information flow properties – can be analyzed at the level of object references and connectivity, independent of any knowledge or analysis of the code that determines the behavior of the objects. As a consequence, these security properties can be established and maintained in the presence of new objects that contain unknown and possibly malicious code.
* [Object Capabilities](http://erights.org/elib/capability/ode/ode-capabilities.html) eRights
  > The capability model is, in a sense, the object model taken to its logical extreme. Where object programmers seek modularity -- a decrease in the dependencies between separately thought-out units -- capability programmers seek security, recognizing that required trust is a form of dependency. Object programmers wish to guard against bugs: a bug in module A should not propagate to module B. Capability programmers wish to guard against malice. However, if B is designed to be invulnerable to A's malice, it is likely also invulnerable to A's bugs. 

## Literature

* [Authorization Capabilities for Linked Data v0.3](https://w3c-ccg.github.io/zcap-ld/) - An object capability framework for linked data systems CCG
  >  Authorization Capabilities for Linked Data (ZCAP-LD for short) provides a secure way for linked data systems to grant and express authority utilizing the object capability model. Capabilities are represented as linked data objects which are signed with Linked Data Proofs. ZCAP-LD supports delegating authority to other entities on the network by chaining together capability documents. "Caveats" may be attached to capability documents which may be used to restrict the scope of their use, for example to restrict the actions which may be used or providing a mechanism by which the capability may be later revoked. 
* [DIDAuth_%2B_Obj._Cap.](https://iiw.idcommons.net/DIDAuth_%2B_Obj._Cap.)
  > What is DIDAuth and how is it compatible with Object Capabilities?\
  > We started by defining and describing object capabilities:
  > - A Capability is a Transferable Unforgeable Permission. It can be implemented with unguessable URLS or signed objects.
  > - A Java Program object reference is a capability, it allows for actions on the subject (the object instance).
  > - A stronger implementation of object capabilities involves a digital certificate issued by a public key, for a resource with a set of supported methods:\
  > `Issuer: AlicePubKey`\
  > `Resource: did:dad:0x123`\
  > `Actions: Read,Write`\
  > `Signature: 0x456`
* [Applying the Principle of Least Authority to User Interaction](https://github.com/WebOfTrustInfo/rwot8-barcelona/blob/master/topics-and-advance-readings/Applying_POLA_to_User_Interaction.md) by Bill Tulloh - RWoT 8
  > Object capabilities (ocaps) are increasingly recognized as an important tool for achieving the goals of self-sovereign identity. Many of the principles of self-sovereign identity, such as minimization and protection, can best be achieved through the disciplined pursuit of the principle of least authority that ocaps enable. This paper examines how POLA can be extended to better protect users when exercising their self-sovereign identity.
* [Introductory Capability DHT](https://github.com/WebOfTrustInfo/rwot8-barcelona/blob/master/topics-and-advance-readings/introductory-capability-dht-concept.md) James Foley - RWoT 8
  > The Object Capability software design paradigm is a powerful philosophy for the programming of decentralized applications particularly in the realms of security and rights management.
* [Models of Identity](https://github.com/WebOfTrustInfo/rwot7-toronto/blob/master/final-documents/mental-models.md) by, Joe Andrieu, Nathan George, Christophe Macintosh, Ouri Poupko, Antoine Rondelet, Andrew Hughes – RWoT 7
**Security** • **Liberty** • **Data** • **Relationship** • **Capability**
  > Considering different models for handling identity information allows reconciliation, and creates opportunities to address primary use cases across paradigms, increasing overall strength and security of a solution.\
  > [...]\
  > In the Object Capabilities model, authorization is managed by creating, sharing, attenuating, and using “capabilities” instead of, for example, access control lists. If you have a valid “capability”, you have the authorization. Like a car key, Object Capabilities may be used no matter who you are. This model shifts the burden of identification from error-prone correlations to directly work with individuals’ actual capabilities.
* [Cryptographic and Data Modeling Requirements from RWoT](https://github.com/WebOfTrustInfo/rwot7-toronto/blob/master/topics-and-advance-readings/crypto-data-model-requirements.md) by Manu Sporny, Dave Longley, and Chris Webber - RWoT 7
  > This paper introduces the uninitiated to the requirements that have been identified over the years that are driving the community toward certain technological solutions.
  > 
  > Rebooting the Web of Trust is a community that is attempting to create a decentralized ecosystem that enables people to be in control of various aspects of their data and identity information. The group often talks about Decentralized Identifiers, Verifiable Credentials, Object Capabilities, ed25519 keys, cryptographic identifiers, and other technologies but rarely spends time documenting how we got here.
* [Recent happenings with Linked Data Capabilities](https://github.com/WebOfTrustInfo/rwot6-santabarbara/blob/master/topics-and-advance-readings/ld-ocap-recent-happenings.md) By Christopher Lemmer Webber – RWoT 6
  > One of the outputs from Rebooting Web of Trust Fall 2017 was a writeup on Linked Data Capabilities based on discussions from the workshop (and particularly thanks to the guide of Mark S. Miller's longstanding work on object capabilities). While the writeup speaks for itself, in short Linked Data Capabilities provide a way to encode object capability security to linked data systems. Much has happened since then.
  > 
  > After the workshop ideas from the paper were reified into specification form and the W3C Credentials Community Group has taken on the specification as an official work item of the group. Some changes have happened in the design of Linked Data Capabilities from the initial Rebooting Web of Trust paper
* [Credentials CG Telecon Minutes for 2017-11-14](https://w3c-ccg.github.io/meetings/2017-11-14/) The W3C Credentials Community Group
  > Topics
  > - Introduction to Mark Miller (Google)
  > - DID Spec Review
  > - Capabilities in Verifiable Credentials
  > - W3C TPAC 2017 Update
* [Smarm: Requirements for a smart-signatures Scheme](https://github.com/WebOfTrustInfo/rwot5-boston/blob/master/draft-documents/smarm.md) By Christopher Lemmer Webber and Christopher Allen - RWoT 5
  > [Smart signatures](https://github.com/WebOfTrustInfo/rwot5-boston/blob/master/draft-documents/smarm.md) are desirable, but how to implement them? We need a language that is powerful and flexible enough to meet our needs while safe and bounded to run while remaining simple enough to feasibly implement.
  > 
  > [Scheme](https://en.wikipedia.org/wiki/Scheme_programming_language) is a turing-complete language with a (at least stated) fondness for minimalism. Unfortunately Scheme on its own is neither "safe" nor (necessarily) deterministic. Thankfully we can get the properties we want through:
  > 
  > - Making object capabilities a core part of the language. Specifically, [Jonathan Rees' "W7 security kernel"](http://mumble.net/~jar/pubs/secureos/secureos.html) demonstrates that a pure lexically scoped environment is itself an appropritate substrate for object capabilities.
  > - Restricting space and time precisely in a way that is deterministic and reproducible.
  > - Removing sources of external side effects.
* [Identity Hubs Capabilities Perspective](https://github.com/WebOfTrustInfo/rwot5-boston/blob/master/final-documents/identity-hubs-capabilities-perspective.md) by Adrian Gropper, Drummond Reed, Mark S. Miller – RWoT 5
  > Identity Hubs as currently proposed in the Decentralized Identity Foundation (DIF) are a subset of a general Decentralized Identifier (DID) based user-controlled agent, based on ACLs rather than an object-capabilities (ocap) architecture.  The current approach has both security and scalability issues. Transitioning the Hubs design to an ocap model can be achieved by introducing an UMA authorization server as the control endpoint. This avoids creating confused-deputy security issues and expands scale by enabling the hub to delegate access to resources not stored in the hub itself.
* [Linked Data Capabilities](https://github.com/WebOfTrustInfo/rwot5-boston/blob/master/final-documents/lds-ocap.md) By Christopher Lemmer Webber and Mark S. Miller
  > Linked Data Signatures enable a method of asserting the integrity of linked data documents that are passed throughout the web. The object capability model is a powerful system for ensuring the security of computing systems. In this paper, we explore layering an object capability model on top of Linked Data Signatures via chains of signed proclamations. fn:1 We call this system "Linked Data Capabilities", or "ld-ocap" for short.
