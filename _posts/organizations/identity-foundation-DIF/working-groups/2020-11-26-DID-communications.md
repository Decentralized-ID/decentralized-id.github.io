---
date: 2020-11-26
title: DID Communications WG - DIF 
description: contribute to specs that embody a method for secure, private and authenticated message-based communication, where trust is rooted in DIDs and used over a wide variety of transports.
excerpt: >
  Produce one or more high-quality specs that embody a method (“DIDComm”) for secure, private and (where applicable) authenticated message-based communication, where trust is rooted in DIDs and depends on the messages themselves, not on the external properties of the transport(s) used. The method must be usable over many means of transport, including those that are asynchronous and simplex, and ones that do not necessarily use the internet. It must support routing and relay through untrusted intermediaries, not just point-to-point delivery. In addition to the communication and protocols described above, the protocols for exchanging DIDs/keys to bootstrap such communication are within scope. These protocols can be the foundation of higher-level protocols such as credential exchange and higher-level authentication protocols.
permalink: organizations/decentralized-identity-foundation/wg/did-comm/
canonical_url: https://decentralized-id.com/organizations/decentralized-identity-foundation/wg/did-comm/
redirect_from: 
categories: ["Web Standards"]
tags: ["DIDComm WG","DIDComm","DIF","Aries","DID","W3C"]
header:
  image: /images/DIDComm-header.webp
  teaser: /images/DIDComm-teaser.webp
last_modified_at: 2020-11-26
---

[Webpage](https://identity.foundation/working-groups/did-comm.html) - [GitHub](https://github.com/decentralized-identity/didcomm-messaging/)

> Join this group to contribute to specs that embody a method for secure, private and authenticated message-based communication, where trust is rooted in DIDs and used over a wide variety of transports.

* [Mailing list](https://dif.groups.io/g/didcomm-wg) - The more foundational communication protocols have been known by several names during their history, including Agent to Agent Communication and more recently DID Communications (DIDComm for short). On top of this foundation are other protocols, including credential exchange, basic user messaging, etc
* [DIDcomm WG Charter](https://github.com/decentralized-identity/org/blob/master/Org%20documents/WG%20documents/DIF_DIDcomm_WG_Charter_v1.pdf)
  > Produce one or more high-quality specs that embody a method (“DIDComm”) for secure, private and (where applicable) authenticated message-based communication, where trust is rooted in DIDs and depends on the messages themselves, not on the external properties of the transport(s) used. The method must be usable over many means of transport, including those that are asynchronous and simplex, and ones that do not necessarily use the internet. It must support routing and relay through untrusted intermediaries, not just point-to-point delivery. In addition to the communication and protocols described above, the protocols for exchanging DIDs/keys to bootstrap such communication are within scope. These protocols can be the foundation of higher-level protocols such as credential exchange and higher-level authentication protocols.
* [DIDcomm WG Operating Addendum](https://github.com/decentralized-identity/org/blob/master/Org%20documents/WG%20documents/DIF_DIDcomm_WG_Operating_Addendum_v1.pdf)
  > We are designing communications protocols specifically for use with the decentralized identifier specification at W3C (​https://www.w3.org/TR/did-core/​).  The DID Core specification and the surrounding family of DID specifications (e.g ​https://w3c-ccg.github.io/did-resolution/​) represent the format for entity identification in our DIDComm efforts.
* [DIF starts DIDComm Working Group](https://medium.com/decentralized-identity/dif-starts-didcomm-working-group-9c114d9308dc)
  > Over the past few months, the DIF and Hyperledger Aries community have come together and agreed to work on a common work item aimed at developing secure communication based on Decentralized Identifiers (DIDs) — hence the name DIDComm, which is short for DID Communication. Significant prior work in developing a messaging-based communication protocol using DIDs has been incubating in the HyperLedger (HL) Aries community, with the progress of this effort evident in the resulting [Aries RFCs](https://github.com/hyperledger/aries-rfcs). To address the requirements of a broader and more heterogeneous community we selected DIF as the place to pursue the next phase of work associated with this effort. Presenting the progress of DIDcomm to other relevant working groups will drive the interoperability between the various decentralized identity vendors and hence enabling a range of decentralized identity-related use cases.

## Specs & Projects

* [decentralized-identity/DIDComm-js](https://github.com/decentralized-identity/DIDComm-js)
  > DIDComm JS LibA shared effort with the HL Aries project to create a standardized means of authenticated general message passing between DID controllers. More information will be added soon.

### DIDComm Messaging

* [decentralized-identity/didcomm-messaging](https://github.com/decentralized-identity/didcomm-messaging)
  > DIDComm Messaging is a powerful way for people, institutions, and IoT things to interact via machine-readable messages, using features of decentralized identifiers (DIDs) as the basis of security and privacy. It works over any transport: HTTP, BlueTooth, SMTP, raw sockets, and sneakernet, for example.
  > 
  > This repo is where we develops specs and reference code to explain DIDComm Messaging. Some of the work incubated here is likely to be standardized at IETF or in other places.
  * [Spec](https://identity.foundation/didcomm-messaging/spec/) - [Markdown](https://github.com/decentralized-identity/didcomm-messaging/blob/master/spec.md)
    > DIDComm enables higher-order protocols that inherit its security, privacy, decentralization, and transport independence. Examples include exchanging verifiable credentials, creating and maintaining relationships, buying and selling, scheduling events, negotiating contracts, voting, presenting tickets for travel, applying to employers or schools or banks, arranging healthcare, and playing games. Like web services atop HTTP, the possibilities are endless; unlike web services atop HTTP, many parties can participate without being clients of a central server, and they can use a mixture of connectivity models and technologies.
* [Implementers Guide](https://identity.foundation/didcomm-messaging/guide/) - This guide contains concepts, explanations, and important considerations for those building DIDComm capable systems.
  > Routing is the process of managing the delivery of messages from sender to recipient, possibly adapting the packaging and transfer to intermediate nodes. A route is a map or plan that specifies enough to achieve delivery in at least one direction; it may omit uninteresting details.
  > 
  > A sender emits a message hoping that a recipient eventually receives it. As a message moves toward the recipient, we say it is moving destward; the opposite direction is sourceward. Note that sender and recipient flip if a request-like message is followed by a response-like message in the opposite direction; the context that defines a sender is a single message, not a paired interaction. (DIDComm supports request-response but does not require it.)
