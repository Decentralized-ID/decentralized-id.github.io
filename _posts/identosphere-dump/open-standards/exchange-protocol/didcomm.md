---
published: false
---

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

## Real World
- [DIF F2F demo session](https://www.youtube.com/watch?v%3DSaNvIorKQ9I)



* [The Missing Network Layer Model](https://findy-network.github.io/blog/2022/03/05/the-missing-network-layer-model/) Findy

Epic Post

You might think that I have lost my mind. We have just reported that our Indy SDK based DID agency is [AIP 1.0](https://github.com/hyperledger/aries-rfcs/blob/main/concepts/0302-aries-interop-profile/README.md) compatible, and everything is wonderful. What’s going on?
