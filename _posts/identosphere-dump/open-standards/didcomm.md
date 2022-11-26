---
published: false
---

# DIDComm

* [DID Comm has its own site](https://didcomm.org/)
  > DIDComm lets people and software use [DIDs](https://www.w3.org/TR/did-core/) to communicate securely and privately over many channels: the web, email, mobile push notifications, QR codes, Bluetooth, message queues, sneakernet, and more.
* [Why the Internet Needs DIDComm](https://iiw.idcommons.net/2D/_Why_the_Internet_Needs_DIDComm) by Sam Curren

* [https://docs.google.com/presentation/d/16HTPyZV_-BtM6EifQpxjivRHKYUeVtOAReUD1eGUA9M/edit?usp=sharing](https://docs.google.com/presentation/d/16HTPyZV_-BtM6EifQpxjivRHKYUeVtOAReUD1eGUA9M/edit?usp%3Dsharing)

- Enables Verifiable Communication
- Intelligence at the edge (like email)
- Protocol Based (like email)
- Supports HTTP(s) (like APIs) and others as a transport
- Bluetooth enables Edge to Edge transport
- Mobile / Offline Friendly (like email)
- Supports rotating from one DID to another
- Security independent of transport
- Protocol development becomes easier and more robust (unlike email)

- [https://identity.foundation/](https://identity.foundation/)
- [#wg-didcomm on DIF Slack](https://difdn.slack.com)
- [https://identity.foundation/didcomm-messaging/docs/spec/](https://identity.foundation/didcomm-messaging/docs/spec/)
- [https://github.com/decentralized-identity/didcomm-messaging](https://github.com/decentralized-identity/didcomm-messaging)
- WG Calls Mondays at noon US/Pacific ([Agenda](https://github.com/decentralized-identity/didcomm)

* [Decentralized Semantics 101](https://iiw.idcommons.net/2E/_Decentralized_Semantics_101) by Paul Knowles

The form of the session was a presentation (intended for those new to the subject), followed by Q/A and discussion

Presentation: [Decentralized Semantics 101](https://drive.google.com/file/d/1Og1LVND8RrHbZ8mBobBehRzN46YI4SXt/view?usp%3Dsharing)

A digital network must contain authenticable data entry and immutable data

capture elements in order to maintain balance and integrity.

Within the context of a decentralized network, these fundamentals enable a self-regulating system where ...

(1) data inputs can be trusted as having come from an assured source under the control of a governing entity; and

(2) semantic items ensure that the meaning and use of inputted data remains unaltered for all interacting actors.

Vocabulary:

- Form - taken from paper forms used filled in by subjects and service provider reps (e.g., clinician). A Form is a composite/aggregate packaging of claims/attributes from one or more Verifiable Credentials (VCs) for presentation (e.g., to a verifier) or for data exchange.

* [DIDComm v2: Implementation and integration](https://iiw.idcommons.net/11D/_DIDComm_V2:_Implementation_and_integration_%2527technical%2527_-_did:key_and_did:keri_resolvers,_seamless_and_partial_integrations-)

* [Didcomm-rs.pdf](https://drive.google.com/file/d/1dn5f2SqnCeQocOy5quJD9gpMPipKRmdC/view?usp%3Dsharing)

- DIDComm v2 spec: [https://identity.foundation/didcomm-messaging/spec](https://identity.foundation/didcomm-messaging/spec)
- didcomm-rs: [https://github.com/decentralized-identity/didcomm-rs](https://github.com/decentralized-identity/didcomm-rs)
• ddoresolver-rs: [https://github.com/jolocom/ddoresolver-rs](https://github.com/jolocom/ddoresolver-rs)
• keriox: [https://github.com/decentralized-identity/keriox](https://github.com/decentralized-identity/keriox) creds to Charles Cunningham, Edyta Pawlak and other contributors.
- did-key: [https://crates.io/crates/did-key](https://crates.io/crates/did-key) creds to Tomislav Markovski.
- DIF F2F demo session: [https://www.youtube.com/watch?v=SaNvIorKQ9I](https://www.youtube.com/watch?v%3DSaNvIorKQ9I)

* [DIDComm and the Self-Sovereign Internet](https://iiw.idcommons.net/21A/_DIDComm_and_the_Self-Sovereign_Internet) by Phil Windley

* [https://docs.google.com/presentation/d/1h0qi2qyGwM30DHpRAXW_Y0bBneo9xMEFZh1rIAeRa-E/edit?usp=sharing](https://docs.google.com/presentation/d/1h0qi2qyGwM30DHpRAXW_Y0bBneo9xMEFZh1rIAeRa-E/edit?usp%3Dsharing)

Summary: DIDComm is the messaging protocol that provides utility for DID-based relationships. DIDComm is more than just a way to exchange credentials, it's a protocol layer capable of supporting specialized application protocols for specific workflows. Because of its general nature and inherent support for self-sovereign relationships, DIDComm provides a basis for a self-sovereign internet much more private, enabling, and flexible than the one we've built using Web 2.0 technologies.

DID-based relationships are the foundation of self-sovereign identity (SSI). The exchange of DIDs to form a connection with another party gives both parties a relationship that is self-certifying and mutually authenticated. Further, the connection forms a secure messaging channel called DID Communication or DIDComm. DIDComm messaging is more important than most understand, providing a secure, interoperable, and flexible general messaging overlay for the entire internet.

* [DIDComm and the Self-Sovereign Internet - Phillip J. Windley, Ph.D., Brigham Young University](https://www.windley.com/archives/2020/11/didcomm_and_the_self-sovereign_internet.shtml)

DIDComm is a protocol layer capable of supporting specialized application protocols for specific workflows. Because of its general nature and inherent support for self-sovereign relationships, DIDComm provides a basis for a self-sovereign internet much more private, enabling, and flexible than the one we've built using Web 2.0 technologies. This talk introduces DIDComm, discusses its protocological nature, and presents use cases in the Internet of Things. Demonstrations of DIDComm protocol interactions will be shown on the Pico platform, which implements the Aries Cloud Agent (ACA) specification.


* [Why we need DIDComm](https://identitywoman.net/why-we-need-didcomm/) IdentityWoman

This is the text of an email I got today from a company that I had a contract with last year [...] I was reminded quite strongly why we need DIDComm as a protocol to enable the secure transport of all sorts of things not just signed VCs but intermediate uses
* [Two new COSE- and JOSE-related Internet Drafts with Tobias Looker](https://self-issued.info/?p%3D2260) Mike Jones

This week, [Tobias Looker](https://twitter.com/tplooker) and I submitted two individual Internet Drafts for consideration by the [COSE working group](https://datatracker.ietf.org/wg/cose/about/).

* [The Missing Network Layer Model](https://findy-network.github.io/blog/2022/03/05/the-missing-network-layer-model/) Findy

Epic Post

You might think that I have lost my mind. We have just reported that our Indy SDK based DID agency is [AIP 1.0](https://github.com/hyperledger/aries-rfcs/blob/main/concepts/0302-aries-interop-profile/README.md) compatible, and everything is wonderful. What’s going on?
