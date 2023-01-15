---
published: false
---

# Credential Exchange

* [IETF: Secure Credential Transfer](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0025.html)  Orie Steele (Monday, 4 April)

* [https://www.ietf.org/archive/id/draft-secure-credential-transfer-03.html](https://www.ietf.org/archive/id/draft-secure-credential-transfer-03.html)

This document describes a mechanism to transfer digital credentials securely between two devices. Secure credentials may represent a digital key to a hotel room, a digital key to a door lock in a house or a digital key to a car. Devices that share credentials may belong to the same or two different platforms (e.g. iOS and Android). Secure transfer may include one or more write and read operations. Credential transfer needs to be performed securely due to the sensitive nature of the information.

* [Figuring out Verifiable Credentials Exchange - combining Bloom, Aires Protocols, Presentation Exchange into a unified - Killer Whale Jello Salad](https://iiw.idcommons.net/22H/_Figuring_out_Verifiable_Credentials_Exchange_-_combining_Bloom,_Aires_Protocols,_Presentation_Exchange_into_a_unified_-_Killer_Whale_Jello_Salad) by Kaliya Young, Orie Steele, Drummond , Kyle et al [ [presentation](https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit#slide=id.p)]
  > - Because what we need is interoperable - issuance - issue-> holder || holder -> verifier some conversation about SIOP - has not been the focus of the discussion.
  > - Goal to create a bridge between
  > - the W3C CCG / DHS SVIP - VCI-HTTP-API (VHA) in combination with CHAPI protocol and the (VC Request) for issuing credentials.
  > - Aries protocols run on top of DIDComm
  > - If we agree on a credential format we can exchange across those universes - JSON-LD ZKP BBS+ then we need a protocol to do it - can go between.
  > - Orie proposed - that we rather then extend VHA - that the we take a streamlined path with DIDComm as envelop layer - present proof - presentation exchange as a payload including the DIF work presentation, Aries and hopefully alternative to expanding VHA - for holder interactions - since it doesn’t have a holder interactions leverage existing
  > - So can be tested with next SVIP - testing.
  > - Presentation Exchange and use of DIDComm and for sake of interop testing pave a narrow path - and expand in future interoperability efforts.
  > - Summary: DIDComm, Presentation request, presentation exchange, present proof format using JSON-LD ZKP with BBS+
  > - Potentially quickly spinning up a working group at DIF - Decision was to nest within the Credentials and Claims group at DIF
  > Result: [https://identity.foundation/arewewaciyet/](https://identity.foundation/arewewaciyet/)


* [BBS+ Credential Exchange in Hyperledger Aries](https://iiw.idcommons.net/11E/_BBS+_Credential_Exchange_in_Hyperledger_Aries) [[presentation](https://iiw.animo.id)]

* [Credentials Exchange - figuring it out - (Jello Bowl Death Match?)](https://iiw.idcommons.net/12F/_Credentials_Exchange_-_figuring_it_out_-_(Jello_Bowl_Death_Match%3F)_%E2%80%93) [[Slides](https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit#slide=id.p)]
  DIDComm, Verifiable Credential Exchange, Aries Protocol, Bloom Protocol, Presentation Exchange 

The ultimate goal is to get to a clear exchange protocols.

Also to have a paper similar to this one that outlines the choice landscape that is and points to a convergence point - [https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf)

Good Health Pass is literally right now trying to figure this out and will “pick” solutions it needs to get implementations working in the next 30-90 days and point the whole industry in one direction.

We started out with this framework of understanding

Contextualizing VC Exchange in Layers

Verifiable Credentials (VC or VCs) is one of the key standardized components of decentralized identity. [The VCs Data Model](https://www.w3.org/TR/vc-data-model/), defined at the W3C, is a universal data format that lets any entity express anything about another entity.  It provides a common mechanism for the interoperable implementation of digital credentials that are cryptographically secure, tamper-evident, privacy-respecting, and machine-verifiable.

There clarity emerging on standards that are interoperable with one another for the VC format.

There is less clarity on the Exchange mechanisms.

One way that has been proposed to look at the exchange options available is to see them in different layers.

### CHAPI

* [chapi.io launches, includes VC playground](https://lists.w3.org/Archives/Public/public-credentials/2022Jun/0055.html) Manu Sporny CCG

TL;DR: chapi.io is a site that helps developers integrate Verifiable Credential issuance, holding, and presentation into their applications. It includes a playground that can issue arbitrary VCs to digital wallets (web and native). It also includes tutorials on how Web Developers can add CHAPI integration to their websites. All you need to try it out is a web browser.

The Credential Handler API or CHAPI is currently a draft community group report developed by/under the Credentials Community Group at the W3C. At the heart of this model is a credential repository which is a Web application that can handle credential requests and credential storage on behalf of the user/holder.  The API Is designed to support the transmission of credentials between a web based issuer and a holder with a cloud wallet (credential repository) that is visible in the same browser but in a different tab.  It creates a “dumb pipe” between the two tabs in the holder’s browser and permits the transmition of the credential effectively from one tab to another.
* [chapi.io launches, includes VC playground](https://lists.w3.org/Archives/Public/public-credentials/2022Jun/0055.html) Manu Sporny CCG

TL;DR: chapi.io is a site that helps developers integrate Verifiable Credential issuance, holding, and presentation into their applications. It includes a playground that can issue arbitrary VCs to digital wallets (web and native). It also includes tutorials on how Web Developers can add CHAPI integration to their websites. All you need to try it out is a web browser.

* [TrustBloc - Duty Free Shop use case (CHAPI Save + WACI Share)](https://www.youtube.com/watch?v=aagFJBI1fBE)

This video demonstrates the TrustBloc platform to Issue a W3C Verifiable Credential through CHAPI and Share the Verifiable Credential/Presentation through WACI.


CHAPI

* [VC-API Diagram for today. Focus on CHAPI](https://lists.w3.org/Archives/Public/public-credentials/2021Nov/0007.html)  Joe Andrieu (Tuesday, 2 November)

![https://www.notion.soimages/image7.png](https://www.notion.soimages/image7.png)

* [chapi.io launches, includes VC playground](https://lists.w3.org/Archives/Public/public-credentials/2022Jun/0055.html)  Manu Sporny (Monday, 27 June)

TL;DR: chapi.io is a site that helps developers integrate Verifiable Credential issuance, holding, and presentation into their applications. It includes a playground that can issue arbitrary VCs to digital wallets (web and native). It also includes tutorials on how Web Developers can add CHAPI integration to their websites. All you need to try it out is a web browser.

* [chapi.io playground upgrades - credential selector, resident card](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0111.html)  Manu Sporny (Wednesday, 27 July)

The credential selector is an icon-based selector for all the credentials that the chapi.io playground currently supports issuing. You can now click on an image of the credential you'd like to issue.

* [...]

We have added a permanent resident card from the fictitious Government of Utopia to the list of credentials that can be issued. This credential uses the Citizenship Vocabulary[...]

* [You can try both of these new features out in the playground](https://playground.chapi.io/issuer)

* [Jobs For The Future VC added to chapi.io playground](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0031.html)  Manu Sporny (Wednesday, 13 July)

TL;DR: In an attempt to support the current Jobs for the Future Plugfest, an Open Badge v3.0 example for an Academic Achievement has been added to the chapi.io playground. You can now see what a JFF badge issuance and transfer to a Holder wallet looks like in CHAPI (on mobile and web, on any device that can run a web browser). Images of the flow are attached.

### VC-HTTP-API  (VHA)

The VC HTTP is a RESTful API specification (conforming with the [OpenAPI](https://swagger.io/specification/) [3.0 Specification](https://swagger.io/specification/) for constructing and verifying objects which conform to the Verifiable Credential Data Model specification.

A bit more about the OpenAPI 3.0 specification itself:

The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. When properly defined, a consumer can understand and interact with the remote service with a minimal amount of implementation logic.

This API is versioned in conformance with the [Semantic Versioning 2.0 specification](https://semver.org/) to prevent breaking changes between minor versions, and to allow for reliable testing and integration of implementations of this API within enterprise environments. This API provides a standard set of interfaces by which interoperability may be tested and verified by various parties who leverage Verifiable Credentials (VCs).

This slide, from a slide deck presentation by Manu Sporny to the W3C Credentials Community Group on 20 April 2021, explains the relationship of the VC-HTTP-API to CHAPI:

### WACI

There are interactions between a wallet and relying party that require passing information between the two. WACI provides a standard for these interactions.

* [https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0/#status-of-this-document](https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0/#status-of-this-document)

WACI bound to JWT - signed. Could be JWE technically (would have to know the other parties DID and Keys - only optionally required here).

Fully supports credential manifest and presentation exchange.

Could be bound to DIDComm
* [Introducing: WACI (Wallet And Credential Interaction)](https://iiw.idcommons.net/4K/_Introducing:_WACI_(Wallet_And_Credential_Interaction)) by Jace Hensley

* [https://specs.bloom.co/wallet-and-credential-interactions/](https://specs.bloom.co/wallet-and-credential-interactions/)

* [https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0](https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0)

Orie linked this related github issue and discussion:[https://github.com/w3c-ccg/universal-wallet-interop-spec/issues/84](https://github.com/w3c-ccg/universal-wallet-interop-spec/issues/84)
Also related: [https://w3c-ccg.github.io/vp-request-spec/#format](https://w3c-ccg.github.io/vp-request-spec/#format)

Use cases support mobile wallets, backend services and web apps.
Supports chaining of requests…. Relies on credential manifest and presentation exchange

W3C CCG work seems focussed on the “vc-http-api” and “vp-request-spec” as the solutions to this problem…
We reviewed IoT / Web / API considerations for presentation exchange.
We notes the following hypothetically viable non interoperable solutions to this problem:
1. DIDComm v1 (IIW ticket flows?)
2. vp-request-spec + CHAPI

3. vc-http-api + …. ? / w3c ccg traceability API.

4. OIDF vp-token spec?
* [WACI (Wallet And Credential Interaction)](https://identity.foundation/wallet-and-credential-interactions/)

### Message Format

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


### Assorted
- Work within DIF
- [Credentials and Claims](https://github.com/decentralized-identity/org/blob/master/Org%20documents/WG%20documents/DIF_CC_WG_charter_v1.pdf) working group (explicitly mentions something like "unifying existing formats and protocols" in its charter) <- fast time
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

* [VC-HTTP-API discussion (FAQ, vs other APIs, etc)](https://iiw.idcommons.net/13E/_VC-HTTP-API_discussion_-FAQ,_vs_other_APIs,_etc-) by Dmitri Zagidulin

* [https://w3c-ccg.github.io/meetings/2021-04-22-vchttpapi/](https://w3c-ccg.github.io/meetings/2021-04-22-vchttpapi/)

* [W3C CCG weekly call about VC HTTP APIs](https://iiw.idcommons.net/1P/_9am_PT:_W3C_CCG_weekly_call_about_VC_HTTP_APIs) – W3C CCG

We discussed[https://github.com/w3c-ccg/vc-http-api](https://github.com/w3c-ccg/vc-http-api)[Address concerns with VC-HTTP-API #190](https://github.com/w3c-ccg/community/issues/190)

* [[PROPOSED WORK ITEM] Traceability API #191](https://github.com/w3c-ccg/community/issues/191)  
See also [https://w3c-ccg.github.io/meetings/](https://w3c-ccg.github.io/meetings/)

