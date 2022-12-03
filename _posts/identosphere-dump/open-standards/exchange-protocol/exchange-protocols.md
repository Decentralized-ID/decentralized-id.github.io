---
published: false
---

# Credential Exchange

* [IETF: Secure Credential Transfer](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0025.html)  Orie Steele (Monday, 4 April)

* [https://www.ietf.org/archive/id/draft-secure-credential-transfer-03.html](https://www.ietf.org/archive/id/draft-secure-credential-transfer-03.html)

This document describes a mechanism to transfer digital credentials securely between two devices. Secure credentials may represent a digital key to a hotel room, a digital key to a door lock in a house or a digital key to a car. Devices that share credentials may belong to the same or two different platforms (e.g. iOS and Android). Secure transfer may include one or more write and read operations. Credential transfer needs to be performed securely due to the sensitive nature of the information.

* [Figuring out Verifiable Credentials Exchange - combining Bloom, Aires Protocols, Presentation Exchange into a unified - Killer Whale Jello Salad](https://iiw.idcommons.net/22H/_Figuring_out_Verifiable_Credentials_Exchange_-_combining_Bloom,_Aires_Protocols,_Presentation_Exchange_into_a_unified_-_Killer_Whale_Jello_Salad) by Kaliya Young, Orie Steele, Drummond , Kyle et al [ [presentation](https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit%23slide%3Did.p)]
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


* [BBS+ Credential Exchange in Hyperledger Aries](https://iiw.idcommons.net/11E/_BBS%252B_Credential_Exchange_in_Hyperledger_Aries) [[presentation](https://iiw.animo.id)]

* [Credentials Exchange - figuring it out - (Jello Bowl Death Match?)](https://iiw.idcommons.net/12F/_Credentials_Exchange_-_figuring_it_out_-_(Jello_Bowl_Death_Match%253F)_%25E2%2580%2593) [[Slides](https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit%23slide%3Did.p)]
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

The Credential Handler API or CHAPI is currently a draft community group report developed by/under the Credentials Community Group at the W3C. At the heart of this model is a credential repository which is a Web application that can handle credential requests and credential storage on behalf of the user/holder.  The API Is designed to support the transmission of credentials between a web based issuer and a holder with a cloud wallet (credential repository) that is visible in the same browser but in a different tab.  It creates a “dumb pipe” between the two tabs in the holder’s browser and permits the transmition of the credential effectively from one tab to another.
* [chapi.io launches, includes VC playground](https://lists.w3.org/Archives/Public/public-credentials/2022Jun/0055.html) Manu Sporny CCG

TL;DR: chapi.io is a site that helps developers integrate Verifiable Credential issuance, holding, and presentation into their applications. It includes a playground that can issue arbitrary VCs to digital wallets (web and native). It also includes tutorials on how Web Developers can add CHAPI integration to their websites. All you need to try it out is a web browser.

* [TrustBloc - Duty Free Shop use case (CHAPI Save + WACI Share)](https://www.youtube.com/watch?v%3DaagFJBI1fBE)

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

* [https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0/#status-of-this-document](https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0/%23status-of-this-document)

WACI bound to JWT - signed. Could be JWE technically (would have to know the other parties DID and Keys - only optionally required here).

Fully supports credential manifest and presentation exchange.

Could be bound to DIDComm
* [Introducing: WACI (Wallet And Credential Interaction)](https://iiw.idcommons.net/4K/_Introducing:_WACI_(Wallet_And_Credential_Interaction)) by Jace Hensley

* [https://specs.bloom.co/wallet-and-credential-interactions/](https://specs.bloom.co/wallet-and-credential-interactions/)

* [https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0](https://specs.bloom.co/wallet-and-credential-interactions/versions/v0.1.0)

Orie linked this related github issue and discussion:[https://github.com/w3c-ccg/universal-wallet-interop-spec/issues/84](https://github.com/w3c-ccg/universal-wallet-interop-spec/issues/84)
Also related: [https://w3c-ccg.github.io/vp-request-spec/#format](https://w3c-ccg.github.io/vp-request-spec/%23format)

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

### OIDC-SOIP

Self-Issued OpenID Connect Provider or  OIDC-SOIP  was created to take advantage of the fact that there are several 100,000 implementations of OpenID Connect on todays web. This method of exchange verifiable credentials leverages that infrastructure with a few small changes to support OpenID enabled sites to be able to accept verifiable credentials. Holders have wallets or agents that they use to interact with a system. The protocols to do this are being worked on jointly by the OpenID Foundation and Decentralized Identity Foundation.

* [OIDC Credential Provider](https://medium.com/mattr-global/introducing-oidc-credential-provider-7845391a9881) Mattr Global. Dec 15, 2000
* [State of identity on the web](https://medium.com/mattr-global/the-state-of-identity-on-the-web-cffc392bc7ea) Mattr Global. March 14, 2021

Current MATTR spec for OpenID Credential Exchange: [OpenID Connect Credential Provider](https://mattrglobal.github.io/oidc-client-bound-assertions-spec/)

* [More Killer Whale Jello Salad…figuring out how credential exchange can harmonize.](https://iiw.idcommons.net/24B/_More_Killer_Whale_Jello_Salad...figuring_out_how_credential_exchange_can_harmonize.) by Kaliya Young et al.
  > - Because what we need is interoperable - issuance - issue-> holder || holder -> verifier some conversation about SIOP - has not been the focus of the discussion.
  > - Goal to create a bridge between
  > - the W3C CCG / DHS SVIP - VCI-HTTP-API (VHA) in combination with CHAPI protocol and the (VC Request) for issuing credentials.
  > - Aries protocols run on top of DIDComm
  > - If we agree on a credential format we can exchange across those universes - JSON-LD ZKP BBS+ then we need a protocol to do it - can go between.
  > - Orie proposed - that we rather then extend VHA - that the we take a streamlined path with DIDComm as envelop layer - present proof - presentation exchange as a payload including the DIF work presentation, Aries and hopefully alternative to expanding VHA - for holder interactions - since it doesn’t have a holder interactions leverage existing
  > - So can be tested with next SVIP - testing.
  > - Presentation Exchange and use of DIDComm and for sake of interop testing pave a narrow path - and expand in future interoperability efforts.
  > - Summary: DIDComm, Presentation request, presentation exchange, present proof format using JSON-LD ZKP with BBS+
* [OpenID Connect Presentation at IIW XXXII](https://self-issued.info/?p%3D2167)
- [OpenID Connect](https://openid.net/connect/)
- [Frequently Asked Questions](https://openid.net/connect/faq/)
- [Working Group Mailing List](https://lists.openid.net/mailman/listinfo/openid-specs-ab)
- [OpenID Certification Program](https://openid.net/certification/)
- [Certified OpenID Connect Implementations Featured for Developers](https://openid.net/developers/certified/)
* [OpenID Connect Credential Provider](https://medium.com/mattr-global/introducing-oidc-credential-provider-7845391a9881) Mattr
* [OIDC Credential Provider](https://mattrglobal.github.io/oidc-client-bound-assertions-spec/) is “an extension to OpenID Connect which enables the end-user to request credentials from an OpenID Provider and manage their own credentials in a digital wallet.”
* [CREATE AN OIDC CREDENTIAL ISSUER WITH MATTR AND ASP.NET CORE](https://damienbod.com/2021/05/03/create-an-oidc-credential-issuer-with-mattr-and-asp-net-core/)
  > This article shows how to create and issue verifiable credentials using [MATTR](https://mattr.global/) and an [ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/introduction-to-aspnet-core). The ASP.NET Core application allows an admin user to create an OIDC credential issuer using the MATTR service. The credentials are displayed in an ASP.NET Core Razor Page web UI as a QR code for the users of the application.
* [Use CodeB SSI as OpenID Connect Identity Provider for WordPress](https://blog.codeb.io/use-codeb-ssi-as-oidc-identity-provider-for-wordpress/) CodeB

The Self-Sovereign Identity System of CodeB does not only support W3C DID’s but comes also with an inbuilt OpenID Connect (OIDC) Identity Provider. [OpenID Connect meets distributed Self-Sovereign Identities.](https://www.codeb.io/openid-connect-meets-distributed-self-sovereign-identities/)
* [Spruce Developer Update #20](https://blog.spruceid.com/spruce-developer-update-20/)

We've set up a [release pipeline](https://github.com/spruceid/ens-oidc/) and had our first witnessed deployment for the ENS Community-Maintained OIDC IdP ([more info here](https://blog.spruceid.com/sign-in-with-ethereum-decentralizing-an-identity-provider-server/)
* [Use-cases: OIDC for Verifiable Credentials - How do you want to use Identity Provider you control?](https://iiw.idcommons.net/12G/_Use-cases:_OIDC_for_Verifiable_Credentials_-_How_do_you_want_to_use_Identity_Provider_you_control%253F) by Oliver Terbu, Torsten Lodderstedt, Kristina Yasuda, Adam Lemmon, Tobias Looker
* [Browser APIs to enable OpenID Session Management and Privacy](https://iiw.idcommons.net/13L/_Browser_APIs_to_enable_OpenID_Session_Management_and_Privacy) by Sam Goto

How does logout in OIDC happen?

- Classification problem - browsers do not know it is a logout now
- Easiest way
- Browser asks for a user consent
- Hard from a permission implementation perspective
- Tim: No issues with this idea
- If user logged into several OPs, user will not look to all the ones they log out from
- Option2
- Browser classifies signing-in event
- On log out does not prompt the user and IdP has no incentives to lie
- RPs get to determine if they want to log the user out or not
- Whether you can swap generic frame with fenced frame, frame can see it’s own cookies
- May not be able to pass any parameters that you need to pass; no link decoration for framed frame
- Subdomains also considered, but not well thought out
- Logout URL - other option to add, but more work for RP: Resource metadata. Specification - not much adoption. It just feels like a place where RP metadata could be declared which could be useful in this context of the RP defining its metadata (e.g. what IDP it uses
- [draft-jones-oauth-resource-metadata-01 - OAuth 2.0 Protected Resource Metadata (ietf.org)](https://tools.ietf.org/html/draft-jones-oauth-resource-metadata-01)
- On digression: [https://cloudidentity.com/blog/wp-content/uploads/2013/01/3252.image_5F00_04277494.png](https://cloudidentity.com/blog/wp-content/uploads/2013/01/3252.image_5F00_04277494.png)
- Messy real-life situation - sign in to AAD with OIDC and WS-fed; register something at sign-in. From a user, same account, does not matter which protocol is used
- What needs more to be discussed what log out means to the user
- User does not understand when they log out from office, they also log out from Azure
- Also a developer choice
- Relevant one, but not much browsers can do about
- If a bigger picture is browser wants to be in the middle, browser can do something in this area too.
- Ugly part of logout - mechanisms to allow the range of services
- IdP does not need to send back list of all RPs user is logging out from
- Idea not entirely off for IdP to tell a browser from there it wants to log user out from
- Browser have confident of the user intent
- Prompt the user for the intent - never a good idea
- Logout API that community can control a behaviour of
- You call it, browser logs it, and tell where the user left of
- Browser observes the login - passively. Heuristics - what if the browser has not seen it..
- some of this is already starting to show up in chrome canarie
- [https://chromium-review.googlesource.com/c/chromium/src/+/2837551](https://chromium-review.googlesource.com/c/chromium/src/%2B/2837551)
- If domain name ETLD of the issuer is the same as IdP, automatically logs out

* […]

- Looks like we can preserve session management if we figure out logout
- Next would be good to see pseudo code with concrete scenario and sequence diagrams
- Pseudo text: [https://github.com/WICG/WebID/blob/main/cookies.md#logout](https://github.com/WICG/WebID/blob/main/cookies.md%23logout)
- Prototype is being built
- AOB? At IIW?
- Understand what third party cookies actually mean - no cookies at all? Partition cookies going away. The way firefox is doing it?
* [The State of Identity on the Web](https://medium.com/mattr-global/the-state-of-identity-on-the-web-cffc392bc7ea) Mattr
  > This article discusses how the success of Open ID Connect shaped the state of identity on the web, how new web standards enable a new model, and describes a bridge between those worlds: [OIDC Credential provider](https://mattrglobal.github.io/oidc-client-bound-assertions-spec/).
  > This cycle perpetuates the dominance of a few major IdPs and likewise forces users to keep choosing from the same set of options or risk losing access to all of their online accounts. In addition, many of these IdPs have leveraged their role as central intermediaries to increase surveillance and user behavior tracking, not just across their proprietary services, but across a user’s entire web experience.
  > [...]
  > [OIDC Credential Provider](https://mattrglobal.github.io/oidc-client-bound-assertions-spec/) allows you to extend OIDC to allow IdPs to issue reusable VCs about the end-user instead of simple identity tokens with limited functionality. It allows end-users to request credentials from an OpenID Provider and manage their own credentials in a [digital wallet](https://learn.mattr.global/concepts/digital-wallets) under their control.
* [@kimdhamilton](https://twitter.com/kimdhamilton) · [May 25](https://twitter.com/kimdhamilton/status/1397241823190523904)

I've read every decentralized identity protocol so you don't have to. They all just read like "nothing to see here, just f- right off" Oh, except for OIDC Credential Provider. Well done to them!

* [How a combination of Federated identity and Verifiable Credentials can help with Customer onboarding](https://pranavkirtani.medium.com/how-a-combination-of-federated-identity-and-verifiable-credentials-can-help-with-customer-7e6518feb018) Pranav Kirtani

Before we dive into how Federated systems like OIDC and SAML along with Verifiable Credentials (VC) can help improve customer onboarding to your application, let us first understand what are the current methods being used for onboarding.
* [OIDC with SIOPv2 and DIF Presentation Exchange](https://vimeo.com/630104529) Sphereon

* [First Public Review Period for OpenID Connect SIOPV2 and OIDC4VP Specifications Started](https://openid.net/2021/12/17/first-public-review-period-for-openid-connect-siopv2-and-oidc4vp-specifications-started/) OpenID

- Implementer’s Drafts public review period: Friday, December 17, 2021 to Monday, January 31, 2022 (45 days)
- Implementer’s Drafts vote announcement: Tuesday, January 18, 2022
- Implementer’s Drafts voting period: Tuesday, February 1, 2022 to Tuesday, February 8, 2022 *

* [​​First Implementer’s Drafts of OpenID Connect SIOPV2 and OIDC4VP Specifications Approved](https://openid.net/2022/02/08/first-implementers-drafts-of-openid-connect-siopv2-and-oidc4vp-specifications-approved/) OpenID

* [Vote for First Implementer’s Drafts of OIDConnect SIOPV2 and OIDC4VP Specifications](https://openid.net/2022/01/18/notice-of-vote-for-first-implementers-drafts-of-openid-connect-siopv2-and-oidc4vp-specifications/) OpenID

The official voting period will be between Tuesday, February 1, 2022 and Tuesday, February 8, 2022, following the [45-day review](https://openid.net/2021/12/17/first-public-review-period-for-openid-connect-siopv2-and-oidc4vp-specifications-started/) of the specifications.
* [Differences between SAML, OAuth & OIDC (OpenID Connect)](https://www.ubisecure.com/education/differences-between-saml-oauth-openid-connect/)
  > SAML 2.0 - Security Assertion Markup Language
> 
> OAuth 2.0 - Web Authorization Protocol
> OpenID Connect 1.0 (OIDC) - Simple identity layer on top of OAuth 2.0


### Assorted
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

* [VC-HTTP-API discussion (FAQ, vs other APIs, etc)](https://iiw.idcommons.net/13E/_VC-HTTP-API_discussion_-FAQ,_vs_other_APIs,_etc-) by Dmitri Zagidulin

* [https://w3c-ccg.github.io/meetings/2021-04-22-vchttpapi/](https://w3c-ccg.github.io/meetings/2021-04-22-vchttpapi/)

* [W3C CCG weekly call about VC HTTP APIs](https://iiw.idcommons.net/1P/_9am_PT:_W3C_CCG_weekly_call_about_VC_HTTP_APIs) – W3C CCG

We discussed[https://github.com/w3c-ccg/vc-http-api](https://github.com/w3c-ccg/vc-http-api)[Address concerns with VC-HTTP-API #190](https://github.com/w3c-ccg/community/issues/190)

* [[PROPOSED WORK ITEM] Traceability API #191](https://github.com/w3c-ccg/community/issues/191)  
See also [https://w3c-ccg.github.io/meetings/](https://w3c-ccg.github.io/meetings/)

