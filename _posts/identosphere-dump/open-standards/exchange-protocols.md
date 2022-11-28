---
published: false
---

# Credential Exchange


* [Figuring out Verifiable Credentials Exchange - combining Bloom, Aires Protocols, Presentation Exchange into a unified - Killer Whale Jello Salad](https://iiw.idcommons.net/22H/_Figuring_out_Verifiable_Credentials_Exchange_-_combining_Bloom,_Aires_Protocols,_Presentation_Exchange_into_a_unified_-_Killer_Whale_Jello_Salad) by Kaliya Young, Orie Steele, Drummond , Kyle et al


- [https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit#slide=id.p](https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit%23slide%3Did.p)

ReCap & Summary

- Because what we need is interoperable - issuance - issue-> holder || holder -> verifier some conversation about SIOP - has not been the focus of the discussion.
- Goal to create a bridge between
- the W3C CCG / DHS SVIP - VCI-HTTP-API (VHA) in combination with CHAPI protocol and the (VC Request) for issuing credentials.
- Aries protocols run on top of DIDComm
- If we agree on a credential format we can exchange across those universes - JSON-LD ZKP BBS+ then we need a protocol to do it - can go between.
- Orie proposed - that we rather then extend VHA - that the we take a streamlined path with DIDComm as envelop layer - present proof - presentation exchange as a payload including the DIF work presentation, Aries and hopefully alternative to expanding VHA - for holder interactions - since it doesn’t have a holder interactions leverage existing
- So can be tested with next SVIP - testing.
- Presentation Exchange and use of DIDComm and for sake of interop testing pave a narrow path - and expand in future interoperability efforts.
- Summary: DIDComm, Presentation request, presentation exchange, present proof format using JSON-LD ZKP with BBS+
- Potentially quickly spinning up a working group at DIF - Decision was to nest within the Credentials and Claims group at DIF

Result:

* [https://identity.foundation/arewewaciyet/](https://identity.foundation/arewewaciyet/)


* [BBS+ Credential Exchange in Hyperledger Aries](https://iiw.idcommons.net/11E/_BBS%252B_Credential_Exchange_in_Hyperledger_Aries)

* [https://iiw.animo.id](https://iiw.animo.id)

* [Credentials Exchange - figuring it out - (Jello Bowl Death Match?)](https://iiw.idcommons.net/12F/_Credentials_Exchange_-_figuring_it_out_-_(Jello_Bowl_Death_Match%253F)_%25E2%2580%2593)

DIDComm, Verifiable Credential Exchange, Aries Protocol, Bloom Protocol, Presentation Exchange ([Slides](https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit%23slide%3Did.p)

The ultimate goal is to get to a clear exchange protocols.

Also to have a paper similar to this one that outlines the choice landscape that is and points to a convergence point - [https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf)

Good Health Pass is literally right now trying to figure this out and will “pick” solutions it needs to get implementations working in the next 30-90 days and point the whole industry in one direction.

We started out with this framework of understanding

Contextualizing VC Exchange in Layers

Verifiable Credentials (VC or VCs) is one of the key standardized components of decentralized identity. [The VCs Data Model](https://www.w3.org/TR/vc-data-model/), defined at the W3C, is a universal data format that lets any entity express anything about another entity.  It provides a common mechanism for the interoperable implementation of digital credentials that are cryptographically secure, tamper-evident, privacy-respecting, and machine-verifiable.

There clarity emerging on standards that are interoperable with one another for the VC format.

There is less clarity on the Exchange mechanisms.

One way that has been proposed to look at the exchange options available is to see them in different layers.

* [...]

* [Aries RFC 0453 - credential issuance protocol using DIDComm V1 data formats](https://github.com/hyperledger/aries-rfcs/tree/master/features/0453-issue-credential-v2)

* [Aries RFC 0454 - Present Proof protocol V2 using DIDCommV1 data formats](https://github.com/hyperledger/aries-rfcs/tree/master/features/0454-present-proof-v2)

DIDComm v2

Work Item within DIF right now - envelope format with some other opinions we may or may want. Daniel Hardman gave vision - of parts that are done - leaving behind parts not done.

- DIDCom V2 Envelops JWEs (a standard that exists)
- Aries RFCs for payloads that go in JWE envelopes.
- Send envelopes over HTTP as a starting point

* [...]

CHAPI

The Credential Handler API or CHAPI is currently a draft community group report developed by/under the Credentials Community Group at the W3C. At the heart of this model is a credential repository which is a Web application that can handle credential requests and credential storage on behalf of the user/holder.  The API Is designed to support the transmission of credentials between a web based issuer and a holder with a cloud wallet (credential repository) that is visible in the same browser but in a different tab.  It creates a “dumb pipe” between the two tabs in the holder’s browser and permits the transmition of the credential effectively from one tab to another.

* [...]

VC-HTTP-API  (VHA)

The VC HTTP is a RESTful API specification (conforming with the [OpenAPI](https://swagger.io/specification/) [3.0 Specification](https://swagger.io/specification/) for constructing and verifying objects which conform to the Verifiable Credential Data Model specification.

A bit more about the OpenAPI 3.0 specification itself:

The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. When properly defined, a consumer can understand and interact with the remote service with a minimal amount of implementation logic.

This API is versioned in conformance with the [Semantic Versioning 2.0 specification](https://semver.org/) to prevent breaking changes between minor versions, and to allow for reliable testing and integration of implementations of this API within enterprise environments. This API provides a standard set of interfaces by which interoperability may be tested and verified by various parties who leverage Verifiable Credentials (VCs).

This slide, from a slide deck presentation by Manu Sporny to the W3C Credentials Community Group on 20 April 2021, explains the relationship of the VC-HTTP-API to CHAPI:

* [...]

WACI

There are interactions between a wallet and relying party that require passing information between the two. WACI provides a standard for these interactions.

* [https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0/#status-of-this-document](https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0/%23status-of-this-document)

WACI bound to JWT - signed. Could be JWE technically (would have to know the other parties DID and Keys - only optionally required here).

Fully supports credential manifest and presentation exchange.

Could be bound to DIDComm

Message Format

Presentation Exchange defined in DIF

Presentation Exchange is a protocol to support the interaction between holders and verifiers. It supports them being able to express what combination of credential the verifier wants or needs.

Credential Manifest as defined in DIF

Asking for a presentation

And asking proof to enable issuing a credential.

Indy Proof Request

Aries Exchange Protocol

Define the messages that go back and forth between

Issuer and holder (4 messages)

Holder and Verifier (3 messages)

Different formats (types of credentials) are different attachments in those messages.

DIDComm v1, there is AIP v1 and AIP v2 :)

Where does it go?

OIDC-SOIP

Self-Issued OpenID Connect Provider or  OIDC-SOIP  was created to take advantage of the fact that there are several 100,000 implementations of OpenID Connect on todays web. This method of exchange verifiable credentials leverages that infrastructure with a few small changes to support OpenID enabled sites to be able to accept verifiable credentials. Holders have wallets or agents that they use to interact with a system. The protocols to do this are being worked on jointly by the OpenID Foundation and Decentralized Identity Foundation.

Recommended Medium articles about OpenID, VCs, DIDs, and decentralized identity by Nader Helmy at MATTR:

1. Dec 15, 2000: [https://medium.com/mattr-global/introducing-oidc-credential-provider-7845391a9881](https://medium.com/mattr-global/introducing-oidc-credential-provider-7845391a9881)
2. March 14, 2021: [https://medium.com/mattr-global/the-state-of-identity-on-the-web-cffc392bc7ea](https://medium.com/mattr-global/the-state-of-identity-on-the-web-cffc392bc7ea)

Current MATTR spec for OpenID Credential Exchange: [https://mattrglobal.github.io/oidc-client-bound-assertions-spec/](https://mattrglobal.github.io/oidc-client-bound-assertions-spec/)

Raise up to the connect working group

More on the presentation side of things.

OpenID_Credential.

RP wallet holder.

Self-Issued OpenID Connect Provider

EXTENSION for OPs to Issue Verifiable Credentials.

Stand up your own openID Connect provider to stand up a wallet.

If you are doing a custodial system.

Google can be your OP and your wallet.

Progressive web application - where it is the OP itself. That web-app is able to be your wallet.

Original version of SIOP getting ID Token for a DID.

Future - heading…

Allow OIDC to support issuance of

Allow OIDC to support presentation of VCs.

Aggregated Claim Usage - determine how VC flow to hold from OP to RP.

OpenID Foundation has been pulling things apart.

Separate spec called portable identifiers - could apply to SSI. (JWK thumbprints).

Chat about Aries. During issuance there is an implied assumption already authenticated - some sort of authentication

Way DHS Demo works - DID Auth request - VC presentation exchange.

DIDSIOP is a dead term - multiple extensions in openiD foundation - some will be relevent.

Issuance and authentication are two steps in some places and in other places they are one step.

Looking for a solution for I am a holder A - holder B - present credentials to drummond. Go to his website - start a flow from QR code - to initiate presentation flow. Not helpful to bring in concept of credential issuers.

Presentations of Credentials.

I don’t have an authenticated session - want to get to a presentation of a VC.

There really are entirely different protocols - how do you get it into your wallet. How do you authenticate to the issuer to assure rightful subject/holder - multiple ways to do that.

Entirely different protocols for issuance and presentation - can be different.

Are they trying to reach the same place.

Yes they are trying to do both.

Mutual Authentication - breaks with many of the protocols. It is a key feature of SSI.

Drummond - need separate issuance and verification.

Having a way to bind protocols into a single session - single Aires connection.

Sep

Daniel - learned something in ories comment - verifier work flow. Credential exchange is used - always issuance - never means proving.

We could collapse complexity out of Aires - aries of messages instead of API calls - should be described as message exchanges (thumbs up from Orie).

Brent - good conversation.

ORIE

We are on a whale watching expedition - largest great white shark - try and complete with largest killer whale. Trying to capture the presentation exchange

OpenIDConnect - is all of the largest IdP

Gravity Well - connected largest industry players - regardless of openID

Hunting helpless little seals.

Outside of OpenID Connect the next biggest “animal” is Aries protocols.

What if we had one or two things that are eating all of the seals. Is there another one?

Kyle - deployment architectures is what has made this so hard.

Presentation in offline - DIDComm only.

Reasonable assumption one online one not - DIDComm with OIDC.

Server to server - look in completely different scenario.

Quite like the idea of combining different things.

DIDComm as authentication mechanism - pre-issuance - from an OIDC issuer.

How do we combine things together to decide when they fit in different deployment.

FIDO?

W3C Data Model - do they care?

Competing things:

mDL ISO 18013-5

MRTD -

Bloom Spec + Aries RFC - tried to describe without any baggage.

Simplified - message based - description of steps challenging getting proofs back.

Minor upgrade from Aries.

Implemented with

Other key thoughts: OpenID only usable by institutions.

Individuals asking individuals for proof - no implementations individuals have software in their control proof over

Combining things.

Things that limit aries

* [More Killer Whale Jello Salad…figuring out how credential exchange can harmonize.](https://iiw.idcommons.net/24B/_More_Killer_Whale_Jello_Salad...figuring_out_how_credential_exchange_can_harmonize.) by Kaliya Young et al.

ReCap & Summary

- Because what we need is interoperable - issuance - issue-> holder || holder -> verifier some conversation about SIOP - has not been the focus of the discussion.
- Goal to create a bridge between
- the W3C CCG / DHS SVIP - VCI-HTTP-API (VHA) in combination with CHAPI protocol and the (VC Request) for issuing credentials.
- Aries protocols run on top of DIDComm
- If we agree on a credential format we can exchange across those universes - JSON-LD ZKP BBS+ then we need a protocol to do it - can go between.
- Orie proposed - that we rather then extend VHA - that the we take a streamlined path with DIDComm as envelop layer - present proof - presentation exchange as a payload including the DIF work presentation, Aries and hopefully alternative to expanding VHA - for holder interactions - since it doesn’t have a holder interactions leverage existing
- So can be tested with next SVIP - testing.
- Presentation Exchange and use of DIDComm and for sake of interop testing pave a narrow path - and expand in future interoperability efforts.
- Summary: DIDComm, Presentation request, presentation exchange, present proof format using JSON-LD ZKP with BBS+
- Potentially quickly spinning up a working group at DIF - Decision was to nest within the Credentials and Claims group at DIF

Agenda Creation

Things on the Path:

- Scope/Goals:
- Specification good and complete
- 
- BBS+ enabled attestation that transit across issuer, holder, verifier using the rails (paved path) that are envisioned here.
- Maximal adoption as soon as possible,
- Proceed forward in a way - that doesn’t require us to abandon some aspect of what we are doing - start with simpler form to get to bigger. Path can be made wider in future.
- System architecture diagram that articulates how it all fits together - next step.
- Do not re-invent things that already exist.
- Test Suite - Test conformance vs. a Specification <- end goal interoperable implementation
- A matrix Testing N-N testing - plugfest.
- Be nice pick fast resolving DID methods for testing
- Implementation Guide - maybe by: Documentation Corps in DIF
- Test are about SHOWING the protocols work - not that the DID resolution works
- Define the Rails:
- Government issues the credential using software of their choice - did anchored in some did utility - citizen able to use a wallet of their choice - that they hold it in - business using a different software (and different ledger for their public did) all able to do this making their own choices. The reason they can is because of those rails - claim we can do this to a great extent - what we can not do right now across the linked-data signature Aries Ecosystem. Show how we can do what you just described across ecosystems. (Mediation is important - how do we do mediation on these rails).
- System creating presentation is - web wallet, backend system or mobile app.
- We need to handle working with registered web wallets - and also be able to formulate a payload for mobile (QR code) both of these paths need to be speced out to cover both communities.
- We need as many Verifiers as possible (to devalue information on the dark web - with
- Only HTTP Transports
- Verifier - Holder - Issuer

Verifier - is a web accessible verifier.

Holder - app/mobile wallet, Browser wallet ,  backend service wallet (supply chain)

Issuer - is a web accessible verifier.

Things to Paint out of Interoperability Picture / Path Narrowing:

- Non-HTTP Transports (however, let's leave room for non-HTTP transports for future iterations)
- Don’t do negotiation in presentation exchange
- Request -> Presentation -> Fail -> Error
- Lots of way to specify requirements inside presentation exchange - features we decide we are not going to use.
- Credential formats will comply with the W3C VC Data Model
- Support for VC-JWT and LD Proof with example of BBS+ (BLS12381 G2) and ES256
- No revocation (not ready enough yet) [revocation list 2020 does exist]
- Holder refresh is out of scope [there is some work going on on this]
- Issuer/verifier mobile app

Targets for path widening later

- Revocation
- Holder Refresh
- Credential Issuance

What work will go where?

- Work within DIF
- [Credentials and Claims](https://github.com/decentralized-identity/org/blob/master/Org%2520documents/WG%2520documents/DIF_CC_WG_charter_v1.pdf) working group (explicitly mentions something like "unifying existing formats and protocols" in its charter) <- fast time
- Or new WG, draft charter by Balazs: [https://docs.google.com/document/d/18L2-t4_2yrO_xZkwPjMCRcKIDiRGCziNs2X4k093pvo/](https://docs.google.com/document/d/18L2-t4_2yrO_xZkwPjMCRcKIDiRGCziNs2X4k093pvo/)
- DIF - presentation exchange?

Timeline:

- When is the next Claims and Credentials Group? (who are the chairs? - Martin, Wayne, Daniel McGrogan ) Bi-Weekly -
- Work Items within DIF WG can have their own dedicated Calls.
- Join DIF: [https://identity.foundation/join/](https://identity.foundation/join/)
- Stewardship - , Orie, Brent, Snorre, Stephen? Troy
- DIDComm Expert - Sam, Stephen
- Presentation Exchange Expert -
- Register for the first meeting:(26th April, Monday 1pm ET) [https://forms.gle/SqkymupnYc9tDARm9](https://forms.gle/SqkymupnYc9tDARm9)

When do we want it done?

Good Health Pass has tremendous pressure!

When do we need what by?

Feedback into this group from Good Health Pass.

May 1: GHP Drafting Groups First Drafts Due -
           June 1 GHP Interoperability Blueprint Recommendations Spec complete

- 30 day vision
- 90 day vision <- would be ideal to have something that can be tested against for this timeframe.
- 180 day vision

July 1 Test Complete

August 1 - 10+ Implementations / Vendors passing VP Exchange Interop Tests.

October 1 - Cross Wallet Interop Exchange Tests.

Share with DIF Interoperability Working Group

Success Criteria:

- Interop Testing Outcome
- Artifacts Produced
- Test Artifacts to TEST <- effort time and energy

Milestones:

Daniel Hardman wrote this before IIW in the DIF slack and many people +1 it.

this was ideated by Daniel before the last meeting, Balazs just copied it here for safekeeping.

* [Daniel Hardman](https://app.slack.com/team/U01UWQTJMCZ)  [18 hours ago](https://difdn.slack.com/archives/CRMKSUE8M/p1619112488145600?thread_ts%3D1619048996.142500%26cid%3DCRMKSUE8M)

I see this as being a layered spec:

Layer 1 = plaintext JSON payloads, presented in sequence, with possible error conditions. Understanding the spec at this level requires nothing except knowledge of JSON and the general problem domain of VCs. No DIDComm, no HL anything, no dependencies anywhere.

Layer 2 = Security. How to wrap layer 1 such that two parties can exchange the payloads and achieve the trust they need in the process. Here, I see a forked path: use TLS (in which case security is really simple, but is transport dependent), or use DIDComm (in which case you use the JWE wrapper that DIDComm is standardizing, based on keys in a DID doc -- more complex but more flexible). The key thing about Layer 2 is that once it's stripped away (e.g., by an adapter), the payloads exchanged at layer 1 are identical and interoperable.

Layer 3: routing. This is for delivering payloads via intermediaries. It is not needed by HTTP that's direct point-to-point. If you add this layer, you introduce more DIDComm-isms but gain extra flexibility as well.

If you like this framing, then I see a spec where layer 1 is presented very quickly and easily; it should be ultra simple and easy to understand by anyone who knows JSON. No mention of any dependencies anywhere.

This would be followed by an explanation of why additional layers could be added, and then a presentation of a 2-forked road, where one is pure HTTP (TLS for security, no routing), and one is DIDComm (DID docs for security, transport-independent routing). Both use the same layer 1.

Having presented the two forks at a high level, I would then imagine a page of text describing how the HTTP fork would work (HTTP status codes, adaptation for web sockets vs. web hooks, etc).

Then I would imagine a page describing how the DIDComm fork would work -- but instead of hyperlinking to DIDComm auxiliary material, it would be a page or two of copy-pasted material that would allow DIDComm compatibility without consuming any other docs.

The upshot would be a single doc that:

A) describes a simple exchange of messages that lets credential-based proof be requested and presented

B) Structures the messages in a way that's compatible with DIDComm, without requiring anybody outside the DIDComm circle to know that.

C) Explains how the protocol could run over a web service.

D) Explains how the protocol could run over DIDComm -- but in a simplified, self-contained doc rather than with dependencies.

E) Explains the tradeoffs of the pure HTTP vs. DIDComm approaches.

* [VC-HTTP-API discussion (FAQ, vs other APIs, etc)](https://iiw.idcommons.net/13E/_VC-HTTP-API_discussion_-FAQ,_vs_other_APIs,_etc-) by Dmitri Zagidulin

* [https://w3c-ccg.github.io/meetings/2021-04-22-vchttpapi/](https://w3c-ccg.github.io/meetings/2021-04-22-vchttpapi/)

* [W3C CCG weekly call about VC HTTP APIs](https://iiw.idcommons.net/1P/_9am_PT:_W3C_CCG_weekly_call_about_VC_HTTP_APIs) – W3C CCG

We discussed[https://github.com/w3c-ccg/vc-http-api](https://github.com/w3c-ccg/vc-http-api)[Address concerns with VC-HTTP-API #190](https://github.com/w3c-ccg/community/issues/190)

* [[PROPOSED WORK ITEM] Traceability API #191](https://github.com/w3c-ccg/community/issues/191)  
See also [https://w3c-ccg.github.io/meetings/](https://w3c-ccg.github.io/meetings/)
