# OpenID Connect


* [Public Review Period for Proposed Final OpenID Connect Logout](https://openid.net/2022/07/05/public-review-period-for-proposed-final-openid-connect-logout-specifications/)

Unless issues are identified during the review that the working group believes must be addressed by revising the drafts, this review period will be followed by a seven-day voting period during which OpenID Foundation members will vote on whether to approve these drafts as OpenID Final Specifications.


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
* [OpenID Connect Presentation at IIW XXXII](https://self-issued.info/?p=2167)
- [OpenID Connect](https://openid.net/connect/)
- [Frequently Asked Questions](https://openid.net/connect/faq/)
- [Working Group Mailing List](https://lists.openid.net/mailman/listinfo/openid-specs-ab)
- [OpenID Certification Program](https://openid.net/certification/)
- [Certified OpenID Connect Implementations Featured for Developers](https://openid.net/developers/certified/)
* [Use CodeB SSI as OpenID Connect Identity Provider for WordPress](https://blog.codeb.io/use-codeb-ssi-as-oidc-identity-provider-for-wordpress/) CodeB

The Self-Sovereign Identity System of CodeB does not only support W3C DID’s but comes also with an inbuilt OpenID Connect (OIDC) Identity Provider. [OpenID Connect meets distributed Self-Sovereign Identities.](https://www.codeb.io/openid-connect-meets-distributed-self-sovereign-identities/)
* [Spruce Developer Update #20](https://blog.spruceid.com/spruce-developer-update-20/)

We've set up a [release pipeline](https://github.com/spruceid/ens-oidc/) and had our first witnessed deployment for the ENS Community-Maintained OIDC IdP ([more info here](https://blog.spruceid.com/sign-in-with-ethereum-decentralizing-an-identity-provider-server/)
* [Use-cases: OIDC for Verifiable Credentials - How do you want to use Identity Provider you control?](https://iiw.idcommons.net/12G/_Use-cases:_OIDC_for_Verifiable_Credentials_-_How_do_you_want_to_use_Identity_Provider_you_control%3F) by Oliver Terbu, Torsten Lodderstedt, Kristina Yasuda, Adam Lemmon, Tobias Looker
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
- [https://chromium-review.googlesource.com/c/chromium/src/+/2837551](https://chromium-review.googlesource.com/c/chromium/src/+/2837551)
- If domain name ETLD of the issuer is the same as IdP, automatically logs out

* […]

- Looks like we can preserve session management if we figure out logout
- Next would be good to see pseudo code with concrete scenario and sequence diagrams
- Pseudo text: [https://github.com/WICG/WebID/blob/main/cookies.md#logout](https://github.com/WICG/WebID/blob/main/cookies.md#logout)
- Prototype is being built
- AOB? At IIW?
- Understand what third party cookies actually mean - no cookies at all? Partition cookies going away. The way firefox is doing it?
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

* [OpenID Presentations at December 2021 OpenID Virtual Workshop](https://self-issued.info/?p=2214)

- OpenID Connect Working Group [(PowerPoint)](http://self-issued.info/presentations/OpenID_Connect_Working_Group_9-Dec-21.pptx) [(PDF)](http://self-issued.info/presentations/OpenID_Connect_Working_Group_9-Dec-21.pdf)
- OpenID Enhanced Authentication Profile (EAP) Working Group [(PowerPoint)](http://self-issued.info/presentations/OpenID_EAP_Working_Group_9-Dec-21.pptx) [(PDF)](http://self-issued.info/presentations/OpenID_EAP_Working_Group_9-Dec-21.pdf)

use of IETF Token Binding specifications with OpenID Connect and integration with FIDO relying parties and/or other strong authentication technologies.”

* [DIF and OIDF cooperation](https://medium.com/decentralized-identity/dif-oidf-9753b9bd0093) 
  > to work together on areas of mutual interest, allowing working groups to align and coordinate through dual-members. The first major collaboration, which has already been underway for weeks, is a process for revising the Self-Issued OpenID Connect (SIOP) chapter of the OpenID Connect (OIDC) specification.
* [OpenID Connect Client-Initiated Backchannel Authentication (CIBA) Core is now a Final Specification](https://openid.net/2021/09/01/openid-connect-client-initiated-backchannel-authentication-ciba-core-is-now-a-final-specification/)

The OpenID Foundation membership has approved the following [MODRNA](https://openid.net/wg/mobile/) specification as an OpenID Final Specification:
* [OpenID Connect Presentation at 2021 European Identity and Cloud (EIC) Conference](https://self-issued.info/?p=2187)

I gave the following presentation on the [OpenID Connect Working Group](https://openid.net/wg/connect/) during the [September 13, 2021 OpenID Workshop](https://openid.net/oidf-workshop-at-eic-2021-monday-september-13-2021/) at the [2021 European Identity and Cloud (EIC) conference](https://www.kuppingercole.com/events/eic2021/). As I noted during the talk, this is an exciting time for OpenID Connect; there’s more happening now than at any time since the original OpenID Connect specs were created!

- OpenID Connect Working Group [(PowerPoint)](http://self-issued.info/presentations/OpenID_Connect_Working_Group_13-Sep-21.pptx) [(PDF)](http://self-issued.info/presentations/OpenID_Connect_Working_Group_13-Sep-21.pdf)


* [OIDC with SIOPv2 and DIF Presentation Exchange](https://vimeo.com/630104529) Sphereon

* [OpenID Connect Presentation at IIW XXXIII](https://self-issued.info/?p=2196) Mike Jones

- Introduction to OpenID Connect [(PowerPoint)](https://self-issued.info/presentations/OpenID_Connect_Introduction_12-Oct-21.pptx) [(PDF)](https://self-issued.info/presentations/OpenID_Connect_Introduction_12-Oct-21.pdf)

The session was well attended. There was a good discussion about the use of passwordless authentication with OpenID Connect.


* [​​First Implementer’s Drafts of OpenID Connect SIOPV2 and OIDC4VP Specifications Approved](https://openid.net/2022/02/08/first-implementers-drafts-of-openid-connect-siopv2-and-oidc4vp-specifications-approved/) OpenID

- [Self-Issued OpenID Provider v2](https://openid.net/specs/openid-connect-self-issued-v2-1_0-07.html)
- [OpenID Connect for Verifiable Presentations](https://openid.net/specs/openid-connect-4-verifiable-presentations-1_0-08.html)
* [Nat describes GAIN](https://nat.sakimura.org/2021/09/14/announcing-gain/) as an overlay network on top of the Internet with all its participants identity proofed. One key benefit of the approach proposed in the white paper is that the standards required to enable this network already exist: OpenID Connect and eKYC/IDA.
- [OpenID Connect Client-Initiated Backchannel Authentication Flow – Core 1.0](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html)

A Final Specification provides intellectual property protections to implementers of the specification and is not subject to further revision.
* [Intro to OpenID Connect at IIW XXXI](https://self-issued.info/presentations/OpenID_Connect_Introduction_20-Oct-20.pdf).
It is a great overview of the key design principles of OpenID and how we got to now with the protocol 
* [Identity, Unlocked... SIOP with Kristina Yasuda](https://auth0.com/blog/identity-unlocked-explained-season-2-ep-5/)
  > As a discovery mechanism to invoke a Self-Issued OP, the discussion on the podcast covered the usage of a custom schema 'openid://'. Alternative mechanisms to address the limitations of custom schemas are being actively explored in the WG.

The conversation meanders through deeper details, from how the current [SIOP specification draft](https://bitbucket.org/openid/connect/src/master/openid-connect-self-issued-v2-1_0.md) under the OpenID Foundation picks up the mission from a [former attempt under DIF](https://identity.foundation/did-siop/) to encoding approaches for verifiable presentations (embedding in JWTs, [LD proofs](https://w3c-ccg.github.io/ld-proofs/), how to represent attributes
* [The Era of Self-Sovereign Identity](https://www.chakray.com/era-self-sovereign-identity/) Chakaray

VC-AuthN OIDC uses the OpenID connect standards to easily integrate with the supported systems and also provides a way to authenticate using the verifiable credentials, giving the control back to the user. This is similar to the traditional OpenID connect, the only difference is in the token information. Rather than using the user’s information to construct the token, this uses claims in the verifiable credentials presented by the user.
* [Let’s talk about digital identity with Oscar Santolalla, Nat Sakimura and Petteri Stenius](https://www.ubisecure.com/podcast/openid-connect/)

the history of OpenID Connect and how it became so prevalent, with special guests [Nat Sakimura](https://www.linkedin.com/in/natsakimura/), Chairman at the OpenID Foundation, and [Petteri Stenius](https://www.linkedin.com/in/petteri-stenius-6a637/), Principal Scientist at Ubisecure. [...]

“New technology seldomly completely replaces the older technologies. They will form additional layers, and slowly start replacing it.”
* [101 Session: OpenID Connect](https://iiw.idcommons.net/1B/_101_Session:_OpenID_Connect) by Mike Jones

Described at: [https://openid.net/connect/](https://openid.net/connect/)
* [OpenID Connect Claims Aggregation](https://iiw.idcommons.net/5B/_OpenID_Connect_Claims_Aggregation) by Nat Sakimura, Edmund Jay, Kristina Yasuda
[2021-04-21_OpenID Connect Claims Aggregation](https://docs.google.com/presentation/d/1w-rmwZoLiFWczJ4chXuxhY0OsgHQmlIimS2TNlce4UU/edit?usp=sharing)

* [OpenID Connect 4 Identity Assurance](https://iiw.idcommons.net/10J/_OpenID_Connect_4_Identity_Assurance) by Torsten Lodderstedt
  > [https://www.slideshare.net/TorstenLodderstedt/openid-connect-4-identity-assurance-at-iiw-32](https://www.slideshare.net/TorstenLodderstedt/openid-connect-4-identity-assurance-at-iiw-32)
  > 
  > Jacob Dilles proposed to allow RPs to use handles for pre-configured eKYC requests. I filled an issue for discussion by the WG ([https://bitbucket.org/openid/ekyc-ida/issues/1245/pre-configured-claims-ekyc-requests](https://bitbucket.org/openid/ekyc-ida/issues/1245/pre-configured-claims-ekyc-requests).

* [OpenID Connect: Session Management vs Privacy](https://iiw.idcommons.net/11M/_OpenID_Connect:_Session_Management_vs_Privacy) by David Waite

To recap:

- Front-channel logout is simple
- …but brittle and doesn’t give good security guarantees
- Back-channel logout is robust
- …but difficult to implement/support, can still miss signals
- Session Management is useful for some apps
- …but is broken in many browsers

On their own independent schedules, all browsers have either broken or have plans to break state sharing via cross-site iframes to limit user tracking - arguably making the Session Management approach unusable.

* [The OpenID Connect Logout specifications are now Final Specifications](https://self-issued.info/?p=2298)

The OpenID Connect Logout specifications are now Final Specifications

Thanks to all who helped us reach this important milestone! This was originally [announced on the OpenID blog](https://openid.net/2022/09/12/the-openid-connect-logout-specifications-are-now-final-specifications/).

* [OpenID Connect for W3C Verifiable Credential Objects](https://iiw.idcommons.net/2F/_OpenID_Connect_for_W3C_Verifiable_Credential_Objects) by Oliver Terbu, Torsten Lodderstedt, Kristina Yasuda, Adam Lemmon, Tobias Looker

Slides: [https://www.slideshare.net/TorstenLodderstedt/openid-connect-for-w3c-verifiable-credential-objects](https://www.slideshare.net/TorstenLodderstedt/openid-connect-for-w3c-verifiable-credential-objects)

- Have been incubated in OpenID Foundation and DIF’s joint Self-Issued OpenID Provider WG - contact Kristina ([kristina.yasuda@microsoft.com](mailto:kristina.yasuda@microsoft.com) for participation details)
* [First Public Review Period for OpenID Connect SIOPV2 and OIDC4VP Specifications Started](https://openid.net/2021/12/17/first-public-review-period-for-openid-connect-siopv2-and-oidc4vp-specifications-started/) OpenID

- Implementer’s Drafts public review period: Friday, December 17, 2021 to Monday, January 31, 2022 (45 days)
- Implementer’s Drafts vote announcement: Tuesday, January 18, 2022
- Implementer’s Drafts voting period: Tuesday, February 1, 2022 to Tuesday, February 8, 2022 *

* [Differences between SAML, OAuth & OIDC (OpenID Connect)](https://www.ubisecure.com/education/differences-between-saml-oauth-openid-connect/)
  > SAML 2.0 - Security Assertion Markup Language
> 
> OAuth 2.0 - Web Authorization Protocol
> OpenID Connect 1.0 (OIDC) - Simple identity layer on top of OAuth 2.0

* OpenID: [Public Review Period for Proposed Final OpenID Connect Client-Initiated Backchannel Authentication (CIBA) Core Specification](https://openid.net/2021/06/07/public-review-period-for-proposed-final-openid-connect-client-initiated-backchannel-authentication-ciba-core-specification/)
* [Distributed Open Identity: Self-Sovereign OpenID: A Status Report](https://identiverse.gallery.video/detail/videos/standards/video/6184823227001/distributed-open-identity:-self-sovereign-openid:-a-status-report?autoStart=true)
  > follow up of the Identiverse 2019 session “SSO: Self-sovereign OpenID Connect – a ToDo list”. (Decentralized Identity, Mobile, Verified Claims & Credentials, Standards, Preeti Rastogi, Nat Sakimura)
* [Personal Digital Transformation and Holistic Digital Identity](https://www.youtube.com/watch?v=9DExNTY3QAk) OpenID Japan ← His last public talk

from the OpenID Summit Tokyo 2020 Keynote […] about Claims, Identity, Self-ness, Who-ness, and OpenID Connect and Decentralized Identity.

* [SIOP Use-cases - IIW Spring 2021](https://docs.google.com/presentation/d/1a0C4HvVYwwwDqSw3tgPNhy9Iqyufy9oZdnMgl7rQ9Vc/edit#slide=id.p)

- Continuity of a service
- Offline Authentication
- Speed, reduced latency
- Choice, Portability
- Privacy
* [DID chooser for SIOP](https://iiw.idcommons.net/20A/_DID_chooser_for_SIOP) by tom jones & friends

* [https://docs.google.com/presentation/d/1OaMecHecTUexv1skJZoYzJoHKYH8H03REFpFstLRjPg/edit?ts=607b7e5d#slide=id.gd2c45a9dcd_7_21](https://docs.google.com/presentation/d/1OaMecHecTUexv1skJZoYzJoHKYH8H03REFpFstLRjPg/edit?ts=607b7e5d#slide=id.gd2c45a9dcd_7_21)

Goal is to allow folks to pick their DID they want to use for a website.
“Subject choosing which DID to present”.

Use case:
A user goes to an RP, and decides to register for return visits.
RP can’t offer folks the Nascar Problem (too many IDP logos on the login screen).

Select a Wallet vs Select a Wallet and Identifier.

What happens when SIOP arrives?
We will need a DID chooser.

Some wallets will hold credentials for multiple identifiers, some will hold only 1.

An RP offers users multiple options for registration (Google, Facebook, Yahoo…. And coming soon… Personal)

RP should disclose their ID and why they are asking the user for what data.

Options we consider:

- [https://w3c-ccg.github.io/credential-handler-api/](https://w3c-ccg.github.io/credential-handler-api/)
- [https://w3c-ccg.github.io/vp-request-spec/#format](https://w3c-ccg.github.io/vp-request-spec/#format)
- [https://specs.bloom.co/wallet-and-credential-interactions/](https://specs.bloom.co/wallet-and-credential-interactions/)
- [https://github.com/w3c-ccg/universal-wallet-interop-spec/issues/84](https://github.com/w3c-ccg/universal-wallet-interop-spec/issues/84)
* [Using OpenID4VC for Credential Exchange; Technometria - Issue #62](http://news.windley.com/issues/using-openid4vc-for-credential-exchange-technometria-issue-62-1374264?via=twitter-card&client=DesktopWeb&element=issue-card)

Extending OAuth and OIDC to support the issuance and presentation of verifiable credentials provides for richer interactions than merely supporting authentication. All the use cases we’ve identified for verifiable credentials are available in OpenID4VC as well.

