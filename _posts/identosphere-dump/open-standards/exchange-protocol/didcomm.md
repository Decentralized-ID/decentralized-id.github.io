---
published: false
---


* [announcement: DIDComm user group](https://lists.w3.org/Archives/Public/public-credentials/2022Jan/0168.html)  Hardman, Daniel (Thursday, 20 January)

Now that the [DIDComm v2 spec](https://identity.foundation/didcomm-messaging/spec/) is nearing completion, and there are [robust libraries in multiple programming languages](https://github.com/decentralized-identity/didcomm-messaging%23implementations), we are starting a user group to share learnings as we put DIDComm into production. We will organize community resources, produce a handbook, foster application-level protocol creation, maintain the [didcomm.org website](https://didcomm.org) and [repo](https://github.com/decentralized-identity/didcomm.org), and recommend best practices.

* [slides for DIDComm discussion on Tuesday's CCG call](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0032.html)  Daniel Hardman (Tuesday, 5 April)

application/pdf attachment: [DIDComm_v2_Primer.pdf](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/att-0032/DIDComm_v2_Primer.pdf)


# DIDComm

* [DIDComm has its own site](https://didcomm.org/)
  > DIDComm lets people and software use [DIDs](https://www.w3.org/TR/did-core/) to communicate securely and privately over many channels: the web, email, mobile push notifications, QR codes, Bluetooth, message queues, sneakernet, and more.
- [DIDComm](https://identity.foundation/working-groups/did-comm.html) Identity Foundation
- [#wg-didcomm on DIF Slack](https://difdn.slack.com)
- [decentralized-identity/didcomm-messaging](https://github.com/decentralized-identity/didcomm-messaging) GitHub
- WG Calls Mondays at noon US/Pacific ([Agenda](https://github.com/decentralized-identity/didcomm)

## Specifications

- [DIDComm Messaging v2.x Editor’s Draft](https://identity.foundation/didcomm-messaging/docs/spec/) Identity Foundation
- [DIDComm v2 spec](https://identity.foundation/didcomm-messaging/spec)


## Explainer
* [Why the Internet Needs DIDComm](https://iiw.idcommons.net/2D/_Why_the_Internet_Needs_DIDComm) by Sam Curren [presentation](https://docs.google.com/presentation/d/16HTPyZV_-BtM6EifQpxjivRHKYUeVtOAReUD1eGUA9M/edit?usp%3Dsharing)
  > - Enables Verifiable Communication
  > - Intelligence at the edge (like email)
  > - Protocol Based (like email)
  > - Supports HTTP(s) (like APIs) and others as a transport
  > - Bluetooth enables Edge to Edge transport
  > - Mobile / Offline Friendly (like email)
  > - Supports rotating from one DID to another
  > - Security independent of transport
  > - Protocol development becomes easier and more robust (unlike email)
* [Decentralized Semantics 101](https://iiw.idcommons.net/2E/_Decentralized_Semantics_101) by Paul Knowles [Presentation](https://drive.google.com/file/d/1Og1LVND8RrHbZ8mBobBehRzN46YI4SXt/view?usp%3Dsharing)
  > A digital network must contain authenticable data entry and immutable data
  > 
  > capture elements in order to maintain balance and integrity.
  > 
  > Within the context of a decentralized network, these fundamentals enable a self-regulating system where ...
  > 
  > (1) data inputs can be trusted as having come from an assured source under the control of a governing entity; and
  > 
  > (2) semantic items ensure that the meaning and use of inputted data remains unaltered for all interacting actors.
* [DIDComm and the Self-Sovereign Internet](https://iiw.idcommons.net/21A/_DIDComm_and_the_Self-Sovereign_Internet) by Phil Windley [presentation](https://docs.google.com/presentation/d/1h0qi2qyGwM30DHpRAXW_Y0bBneo9xMEFZh1rIAeRa-E/edit?usp%3Dsharing)
  > DID-based relationships are the foundation of self-sovereign identity (SSI). The exchange of DIDs to form a connection with another party gives both parties a relationship that is self-certifying and mutually authenticated. Further, the connection forms a secure messaging channel called DID Communication or DIDComm. DIDComm messaging is more important than most understand, providing a secure, interoperable, and flexible general messaging overlay for the entire internet.
* [DIDComm and the Self-Sovereign Internet - Phillip J. Windley, Ph.D., Brigham Young University](https://www.windley.com/archives/2020/11/didcomm_and_the_self-sovereign_internet.shtml)
  > DIDComm is a protocol layer capable of supporting specialized application protocols for specific workflows. Because of its general nature and inherent support for self-sovereign relationships, DIDComm provides a basis for a self-sovereign internet much more private, enabling, and flexible than the one we've built using Web 2.0 technologies. This talk introduces DIDComm, discusses its protocological nature, and presents use cases in the Internet of Things. Demonstrations of DIDComm protocol interactions will be shown on the Pico platform, which implements the Aries Cloud Agent (ACA) specification.
* [Why we need DIDComm](https://identitywoman.net/why-we-need-didcomm/) IdentityWoman
  > This is the text of an email I got today from a company that I had a contract with last year [...] I was reminded quite strongly why we need DIDComm as a protocol to enable the secure transport of all sorts of things not just signed VCs but intermediate uses


## Development
* [DIDComm v2: Implementation and integration](https://iiw.idcommons.net/11D/_DIDComm_V2:_Implementation_and_integration_%2527technical%2527_-_did:key_and_did:keri_resolvers,_seamless_and_partial_integrations-)
* [didcomm-rs implementation](https://drive.google.com/file/d/1dn5f2SqnCeQocOy5quJD9gpMPipKRmdC/view?usp%3Dsharing) presentation
- [decentralized-identity/didcomm-rs](https://github.com/decentralized-identity/didcomm-rs) github

* [Trusted P2P Messaging with DIDs, DIDComm and VCs](https://medium.com/uport/trusted-p2p-messaging-with-dids-didcomm-and-vcs-398f4c3f3cda) uPort
  > about their path towards trusted P2P messaging and announces the [DIDAgent Framework (DAF)](https://github.com/uport-project/daf)
  > 
  > when we speak about a DID, then we need to be more precise and also speak about the particular DID method of that DID which defines the CRUD operations on a target system such as Ethereum.
* [DIDComm Mythconceptions](https://www.youtube.com/watch?v%3DrwvQdRyMeY4) Daniel Hardman
  > DIDComm is a peer-to-peer communication technology for SSI (self-sovereign identity) with security and privacy properties rooted in DIDs (decentralized identifiers). Its core value proposition is often misunderstood or oversimplified. This webinar provides a proper mental model.
* [FLOSS WEEKLY 685: DIDS AND DIDCOMM](https://twit.tv/shows/floss-weekly/episodes/685) Featuring Sam Curren
  > Sam Curren unpacks for Doc Searls and Dan Lynch why DIDs and DIDcomm are the best approach to identity—and to making people first-class citizens on the Internet. Curren also discusses the origin story of picos and the advantages of nomadic living and hacking.
* [Steering Committee approved the DIDComm Messaging Spec (DIDComm v2)](https://twitter.com/IndicioID/status/1545208982863691777) @IndicioID
* [DIDComm Messaging](https://identity.foundation/didcomm-messaging/spec/)
  > DIDComm Messaging enables higher-order protocols that inherit its security, privacy, decentralization, and transport independence. Examples include exchanging verifiable credentials, creating and maintaining relationships, buying and selling, scheduling events, negotiating contracts, voting, presenting tickets for travel, applying to employers or schools or banks, arranging healthcare, and playing games.
* [DIDComm v2 reaches approved spec status!](https://blog.identity.foundation/didcomm-v2/) DIF Blog
  > DIDComm defines how messages are composed into application-level protocols and workflows.
* [Advanced DIDComm Messaging](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/advanced-didcomm-messaging.md) By: Karim Stekelenburg (Animo Solutions) -- karim@animo.id Date: 18-07-2022 Version: 0.1
  > in order for DIDComm to provide a potential replacement for commonly used chat protocols like WhatsApp (Extensible Messaging and Presence Protocol (XMPP)), Telegram (MTProto), or Signal (Signal Protocol), it needs to support modern chat features we use everyday
* [DIDComm & DIDComm Messaging](https://medium.com/datev-techblog/didcomm-didcomm-messaging-3e10fbf12bb8) Tim Vorgs, DATEV eG

* [Blockchain and Self-Sovereign Identity Empowered Cyber Threat Information Sharing Platform](https://www.youtube.com/watch?v%3DlzS49R52PwA) Siddhi
  > looks interesting and different - uses DIDComm
  > 
  > Presented in 7th IEEE International Conference on Smart Computing(IEEE SmartComp 2021)
* [Timo Glastra @TimoGlastra](https://twitter.com/TimoGlastra/status/1572976791136137216) via Twitter
  > Just got my first DIDComm protocol published on the [https://didcomm.org](https://t.co/GvWIyysx1k) website.

* DIDComm: [ECDH-1PU Implementation](https://blog.identity.foundation/ecdh-1pu-implementation/) Identity Foundation

In short, ECDH-1PU is a key derivation process that allows for sender authenticity and enables a “[Perfect Forward Secrecy](https://www.wired.com/2016/11/what-is-perfect-forward-secrecy/%23:~:text%3DPerfect%2520forward%2520secrecy%2520means%2520that,of%2520the%2520user%27s%2520sensitive%2520data.)” mechanism, in addition to significant performance gains over JWS message nested in a JWE envelope, as used by existign ECDH-ES aproaches.

- We at Jolocom strongly believe that DIDComm is a crucial infrastructure element for the broader and future-proof SSI stack, and [current work on DIDComm v2 includes Jolocom’s implementation of the specification](http://github.com/jolocom/didcomm-rs) with authcrypt (authenticated encrypted) and most of the low level of the protocol.
* [trustbloc/hub-router](https://github.com/trustbloc/hub-router) DIDComm mediator and router with mailbox features.
  > The TrustBloc hub-router is a working implementation of the Mediator Coordination and the Pickup protocols built using Hyperledger Aries Framework - Go.
* [DIDComm Messaging through libp2p](https://medium.com/uport/didcomm-messaging-through-libp2p-cffe0f06a062) uPort
  > Peers would still use their peer ID for [libp2p](https://libp2p.io/) routing and authentication. Alice and Bob would exchange their [DID](https://www.w3.org/TR/did-core/) out of band and will be able to find their counterparty’s peer ID via their [DIDs](https://www.w3.org/TR/did-core/).
* [DIDComm Messaging through libp2p](https://medium.com/uport/didcomm-messaging-through-libp2p-cffe0f06a062) Oliver Terbu
  > We outlined the next generation decentralized messaging solution built on top of [DIDComm Messaging](https://identity.foundation/didcomm-messaging/spec/), [DIDs](https://www.w3.org/TR/did-core/) and [VCs](https://www.w3.org/TR/vc-data-model/) and a [libp2p](https://libp2p.io/) overlay network. We presented how Alice and Bob establish a connection, exchange messages and demonstrated what connection types are supported.
* [DIF F2FJan21 - DIDComm Demo Session with Ivan Temchenko, Tobias Looker, and Oliver Terbu](https://www.youtube.com/watch?v=SaNvIorKQ9I&feature=youtu.be)

During the live demo he showed the message lifecycle in various setups using the new, [open source didcomm-rs library](http://github.com/jolocom/didcomm-rs) on GitHub


* [Aries RFC 0453 - credential issuance protocol using DIDComm V1 data formats](https://github.com/hyperledger/aries-rfcs/tree/master/features/0453-issue-credential-v2)

* [Aries RFC 0454 - Present Proof protocol V2 using DIDCommV1 data formats](https://github.com/hyperledger/aries-rfcs/tree/master/features/0454-present-proof-v2)

### DIDComm v2

Work Item within DIF right now - envelope format with some other opinions we may or may want. Daniel Hardman gave vision - of parts that are done - leaving behind parts not done.

- DIDCom V2 Envelops JWEs (a standard that exists)
- Aries RFCs for payloads that go in JWE envelopes.
- Send envelopes over HTTP as a starting point

