---
published: false
---

# Verifiable Credentials
## Contents

- Explainer
- Comparisons with/ other Tech
- Varieties
  - JSON-LD 
  - JSON-LD ZKP BBS+
  - JSON-JWT
  - ZKP-CL - [IIA] Indy Aries AnnonCreds
  - JWP

## Explainer
* [Article three - An introductory dive into VCs (verifiable credentials)](https://hackernoon.com/understanding-the-verifiable-credentials-vcs-it1535e9) HackerNoon
  > Verifiable Credentials heavily utilize Decentralized Identifiers to identify people, organizations, and things and to achieve a number of security and privacy-protecting guarantees. They are issued and cryptographically signed documents, intended to be understood by computers rather than people.

## Comparisons with/ other Tech
* [Compare and Contrast: OpenBadges vs Verifiable Credentials](https://academy.affinidi.com/compare-and-contrast-openbadges-vs-verifiable-credentials-d504c054d5db) Affinidi 
  > As we move towards a world of digital identity, many ways of sharing and verifying Personally Identifiable Information are emerging. Two such modes that we’ll talk about today are Open Badges and Verifiable Credentials.
* [Non-Fungible Tokens (NFTs) vs Verifiable Credentials (VCs)](https://academy.affinidi.com/non-fungible-tokens-nfts-vs-verifiable-credentials-vcs-cd0ebb13f1fb) Affinidi
  > A common thread that connects both NFTs and VCs is that they leverage the potential benefits of the digital world to give users more security, flexibility, and freedom to monetize.


Prerequisites

- [Understanding the Decentralized identifiers](https://hackernoon.com/decentralized-identifiers-dids-a-deeper-dive-04383442?ref%3Dhackernoon.com)
- [[Optional] - DID for DeFi, definitivel](https://hackernoon.com/decentralized-identifiers-for-defi-definitively-25j33qa?ref%3Dhackernoon.com)y
* [How to Create New Verifiable Credentials with Customizable Schemas](https://www.youtube.com/watch?v%3D3JR6_tQYhgk)

* [OWI Digital Forum Recap: The Rise & Adoption of Verifiable Credentials](https://trinsic.id/owi-digital-forum-recap-the-rise-adoption-of-verifiable-credentials/)

Trinsic CEO Riley Hughes sat down with [One World Identity](https://oneworldidentity.com/) (OWI) CEO Travis Jarae to have a one-on-one conversation about [“The Rise & Adoption of Verifiable Credentials”](https://oneworldidentity.com/session/trinsic/). Below is a short summary

* [25+ Proof of Concepts (PoCs) for Verifiable Credentials](https://academy.affinidi.com/25-proof-of-concept-poc-for-verifiable-credentials-edf684b592f2) Affinidi

Today, we proudly present another 25+ Proof of Concepts for VC implementation. These use cases are a compilation of the [submissions](https://affinidipocathon.devpost.com/) (in no particular order) made by the participants of the Affindi PoCathon 2021.
* [Biometrics come to verifiable credentials with Applied Recognition and Sovrin Foundation](https://www.biometricupdate.com/202105/philsys-surpasses-10m-biometric-enrollments-online-milestone)
* [Verifiable Credentials Aren’t Credentials. And They’re Not Verifiable In the Way You Might Think](https://credentialmaster.com/verifiable-credentials-arent-credentials-theyre-containers/) Timothy Ruff

When you hear the term “VC” or “Verifiable Credential”, think “authenticatable data container” and you’ll be closer to the truth, plus you’ll be more effective in explaining VCs to the next person. [...]

VCs can carry any sort of data payload, and that isn’t just a good thing, it’s a great one. [Part two](https://medium.com/@rufftimo/like-shipping-containers-verifiable-credentials-will-economically-transform-the-world-fece2b9da14a) of my container series covers how such fluid data portability could economically affect cyberspace to a degree comparable to how shipping containers affected global trade.

* [Verifiable credentials are key to the future of online privacy](https://www.helpnetsecurity.com/2021/07/26/verifiable-credentials/) HelpNetSecurity

- All the data is decentralized, meaning there’s no need for a database of student records that could be jeopardized. Alice’s data lives with her.
- The employer doesn’t need to keep a copy of Alice’s transcript to verify her education.
- The college doesn’t play intermediary and doesn’t have access to the list of organizations Alice shares her data with. Other parties have no way of correlating this data as each exchange is private and unique.
- If desired, Alice could pick and choose what she wants to share. She could prove her degree without sharing her date of graduation or GPA, for example.

* [Azure AD Verifiable Credentials architecture overview (preview)](https://docs.microsoft.com/en-us/azure/active-directory/verifiable-credentials/introduction-to-verifiable-credentials-architecture)

This architectural overview introduces the capabilities and components of the Azure Active Directory Verifiable Credentials service. For more detailed information on issuance and validation, see

- [Plan your issuance solution](https://docs.microsoft.com/en-us/azure/active-directory/verifiable-credentials/plan-issuance-solution)
- [Plan your verification solution](https://docs.microsoft.com/en-us/azure/active-directory/verifiable-credentials/plan-verification-solution)

* [@Steve_Lockstep](https://twitter.com/Steve_Lockstep)

The original #VerifiableCredentials were PKI-based SIM cards and EMV cards. These bind key pairs to individuals, and to signed assertions (account numbers) to deliver provenance, fidelity and proof of possession. [https://constellationr.com/blog-news/not-too-much-identity-technology-and-not-too-little](https://constellationr.com/blog-news/not-too-much-identity-technology-and-not-too-little)

* [The value of verifiable credentials in the evolving digital identity landscape](https://verified.me/blog/the-value-of-verifiable-credentials-in-the-evolving-digital-identity-landscape/) Verified Me

In my recent podcast with [Brad Carr](https://www.iif.com/Staff-and-Authors/uid/46/BradCarr) of the [Institute of International Finance](https://www.iif.com/Publications/ID/4304/FRT-Episode-87-Digital-Identity-with-SecureKey-CEO-Greg-Wolfond), we discussed how digital identity and verified credentials can support a digital-first world, something that’s extremely relevant amid the current pandemic.

* [Better digital living with blockchain-backed verifiable credentials](https://thepaypers.com/expert-opinion/better-digital-living-with-blockchain-backed-verifiable-credentials--1250869) The Paypers

The NHS can now provide you with a digital verifiable credential to prove your vaccination status, securely stored in the NHS app and easily accessible, generating a QR code to prove to airlines and employers that you are fit to fly or work. But this is just the first step in the development of an enabling technology that can bring benefits to many areas of modern life.

* [On Climate Crisis and Self-Sovereign Verifiable Career Credentials](https://www.velocitynetwork.foundation/on-climate-crisis-and-self-sovereign-verifiable-career-credentials/) Velocity Network

This rich verifiable self-sovereign career identity will be the ‘great transformer’ of the global labor market. It will change the way people navigate their careers and livelihoods, and how employers make talent decisions.

* [Transforming Scottish Education on the Blockchain](https://digitalscot.net/education-blockchain/) DigitalScot

A pertinent example of how this can be applied in the corporate world is this example of the [Scottish Social Services Council uses them](https://www.badges.sssc.uk.com/getting-started/what-you-need-to-know-about-open-badges/) to underpin workforce learning. The BCS describes this as the [future of professional development](https://www.bcs.org/content-hub/digital-badging-the-future-of-professional-development/), with many organizations like [Siemens](https://new.siemens.com/uk/en/company/education/teachers/siemens-digital-badges.html) using them this way.

* [Bloom Attestation Service migrating to Verifiable Credentials](https://bloom.co/blog/migration-from-attestation-service-to-verified-credentials/) Bloom

To transition fully to the W3C VC standard, Bloom decided to deprecate the proprietary attestation format and adopt the new open VC standard. The transition will fulfill the vision of giving Bloom users complete, secure control of their private data, while allowing interoperability with the rest of the VC ecosystem.

* [How Does a Verifier Know the Credential is Yours?](https://www.evernym.com/blog/how-does-a-verifier-know-the-credential-is-yours/) Evernym

A link secret is a large random number, wrapped in a way that allows the holder to prove that they know the secret.
* [Introduction to Verifiable Credentials](https://www.ubisecure.com/identity-management/verifiable-credentials/) Ubisecure

The Verifiable Credentials specification is quite new, and many pieces that are required to create interoperable solutions are still incomplete or missing at time of writing. However, there is significant momentum around verifiable credentials (VCs). This is partly attributed to VCs being part of the solution for blockchain-based decentralised identity.

* [8 Reasons to use Verifiable Credentials](https://academy.affinidi.com/8-reasons-to-use-verifiable-credentials-300833276b52) Affinidi

VCs are interoperable across many systems and can be used in almost every possible scenario. Here is a list of [use-cases](https://academy.affinidi.com/25-proof-of-concept-poc-for-verifiable-credentials-edf684b592f2) where VCs can be used and PoCs developed based on them.

* [Verifiable Credentials Guide for Developer: Call for Participation](https://hyperonomy.com/2021/09/06/verifiable-credentials-guide-for-developer-call-for-participation/)

Want to contribute to the World Wide Web Consortium (W3C) Developers Guide for Verifiable Credentials?

* [What are Verifiable Credentials in 3 Minutes](https://www.youtube.com/watch?v%3Ds5h7OgmnrxE) Affinidi (video)

* [EIC Speaker Spotlight: Kay Chopard on Driving Digital Trust](https://www.kuppingercole.com/blog/beskers/eic-speaker-spotlight-kay-chopard-driving-digital-trust)

We really hope that a diverse audience will be attracted to the Kantara workshop. The reason I say that is - we're very focused, obviously in the work we do around identity, around assurance programs, around really developing what we recommend the part of standards that are used internationally. And then also taking that the next step and making sure that those standards are implemented in the identity products that are available in the field.
* [Comparing VCs to ZCAP-LD](https://kyledenhartog.com/comparing-VCs-with-zcaps/) Kyle Den Hartog

^^ technically important and relevant.

Why make the investment then to put the time and effort into ZCAPs when we’ve already got VCs? Simply put because security is hard and trying to push square pegs into round holes often times leads to bugs which are elevated to mission critical authentication/authorization bypass vulnerabilities. By designing around a fit for purpose data model with a well defined problem being solved it allows for us to be much more precise about where we believe extensibility is important versus where normative statements should be made to simplify the processing of the data models. By extension this leads to a simpler security model and likely a much more robust design with fewer vulnerabilities.
* [Issue Azure AD Verifiable Credentials from an application](https://docs.microsoft.com/en-us/azure/active-directory/verifiable-credentials/verifiable-credentials-configure-issuer) Microsoft

learn how to:

- Set up Azure Blob Storage for storing your Azure AD Verifiable Credentials configuration files.
- Create and upload your Verifiable Credentials configuration files.
- Create the verified credential expert card in Azure.
- Gather credentials and environment details to set up the sample application.
- Download the sample application code to your local computer.
- Update the sample application with your verified credential expert card and environment details.
- Run the sample application and issue your first verified credential expert card.
- Verify your verified credential expert card.

* [Issuing a verifiable credential in 7 easy steps](https://medium.com/@AnimoSolutions/issuing-a-verifiable-credential-in-7-easy-steps-a7fa18d41c6d) Amino

First we’re going to create a holder Agent, this will be the Agent that receives the membership credential. During their life, the holder will collect many different verifiable credentials. Memberships, ID-cards, even purchasing records.
* [W3C Verifiable Credentials Education Task Force 2022 Planning](https://kayaelle.medium.com/w3c-verifiable-credentials-education-task-force-2022-planning-efc9b07cc2a3) Kerri Lemoie

We’ve been hard at work writing use cases, helping education standards organizations understand and align with VCs, and we’ve been heading towards a model recommendation doc for the community.

* [The World of Anonymous Credentials](https://blog.dock.io/anonymous-credentials/) Dock

A credential is called a verifiable credential when its authenticity can be cryptographically checked by anyone because the credential contains a cryptographic signature by the issuer, and the issuer's public key is well known.

* [WHY THRIVACY?: Think about it. What did you leave behind when you bought the last round of drinks.](https://www.thrivacy.io/why-thrivacy)

Your Thrivacy wallet allows you to request all your important, personal information that can be used to identify who you are to be created into what we call verified credentials. Then those same verified credentials or VCs can be downloaded and stored in your own personal wallet that is kept inside your cell phone.

* [Why Are Governments Choosing Hyperledger?](https://northernblock.io/governments-are-choosing-aries-indy-ursa/) Northern Block

- Open Data Standards (W3C’s DID & VC Standards)
- Open Tech Standards (Hyperledger Aries, Indy, Ursa)
- Achieving W3C-Compliance on Aries and Indy
* [25 Use Cases for Verifiable Credentials](https://drive.google.com/file/d/1BrFjh6-TVkJ4Rfllh5fUTjh6hkYtPbR_/view) LTO Network and Sphereon

* [Verifiable Credentials For Travel & Hospitality](https://www.youtube.com/watch?v%3DXxd56y2mhFQ) Evernym

In this webinar, Evernym's Jamie Smith and Andrew Tobin discuss how verifiable credentials and digital wallets can reduce fraud, automate workflows, and transform customer experiences across the travel and hospitality industries.

* [Issuing credentials directly to the MATTR mobile wallet](https://medium.com/mattr-global/issuing-credentials-directly-to-the-mattr-mobile-wallet-8e8cab931e2e) Mattr

If you’re already using a secure mechanism to authenticate your users, then setting up OIDC capability isn’t necessary. As we’ve explored, sending credentials using secure DID messaging directly or via a QR code or deep-link is safe, convenient and allows users to obtain their credentials directly.

* [Verifiable Credential Notarization and Third-Party Notary Services Providers: User Scenarios](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0109.html) Michael Herman 7/15
* [The VC Lifecycle](https://credentialmaster.com/the-vc-lifecycle/) Credential Master

In 1956 the switch to consistent shipping containers began, and it changed the physical world [profoundly](https://www.economist.com/finance-and-economics/2013/05/18/the-humble-hero); the switch to consistent, authenticatable digital data containers [will do the same for cyberspace](https://rufftimo.medium.com/like-shipping-containers-verifiable-credentials-will-economically-transform-the-world-fece2b9da14a).

* [Example Design of an Authorization System with Verifiable Credentials and the Tradeoffs](https://kyledenhartog.com/example-authz-with-VCs/) Kyle Den Hartog

The primary focus of this blog post is to highlight the different problems that are likely to occur when going down the path of building an authorization system with verifiable credentials. I’ll be sure to keep things at a higher level so that anyone can understand these tradeoffs, but take you through the details that would be thought through by an architect designing the system.

* [The Power of Verifiable Credentials](https://credentialmaster.com/the-power-of-vcs/) Credential Master

For the first time ever, data from one ecosystem can be instantly authenticated in any other, online or off, without a direct connection to the source.

* [Compare and Contrast — IRMA vs Verifiable Credentials](https://academy.affinidi.com/compare-and-contrast-irma-vs-verifiable-credentials-58e4b30d85f1)
## Azure AD
* [Issuing your own DIDs & VCs with Azure AD](https://www.xtseminars.co.uk/post/issuing-your-own-dids-vcs-with-azure-ad)
- [Re: VCs - zCaps / OCap a Discussion](https://lists.w3.org/Archives/Public/public-credentials/2020Dec/0027.html) Dave Longley 12/5
  > TL; DR: My current view is that the main confusion here may be over the difference between VCs and LD Proofs, not VCs and ZCAPs. VCs are not a generalized container for attaching a cryptographic proof to a document. That's what LD proofs (or JOSE style proofs) are for. VCs *use* LD proofs (or JOSE style proofs) to attach an assertion proof to a document that specifically models statements made by an issuer about some subject, which is therefore inherently about the identity of that subject.

* [What are Verifiable Credentials?](https://medium.com/affinidi/what-are-verifiable-credentials-79f1846a7b9)
  > At the most basic level, verifiable credentials, or VC in short, are tamper-proof credentials that can be verified cryptographically.

* [Why the Verifiable Credentials Community Should Converge on BBS+](https://www.evernym.com/blog/bbs-verifiable-credentials/)
  > BBS+ LD-Proofs use JSON-LD schemas, so credentials that use them can have a rich, hierarchical set of attributes. Instead of the heavy-handed mechanism for the encoding and canonicalization of attributes values that we’d imagined for Rich Schemas, they use RDF canonicalization and a hash function. Rather than expanding the credential definition, they discarded it, taking advantage of some properties of BBS+ keys which allow for deterministic expansion.

* [Verifiable Credentials: Mapping to a Generic Policy Terminology](https://trbouma.medium.com/verifiable-credentials-mapping-to-a-generic-policy-terminology-bce84a039bb)
  > Why is this useful? When writing policy, you need a succinct model which is clear enough for subsequent interpretation. To do this, you need conceptual buckets to drop things into. Yes, this model is likely to change, but it’s my best and latest crack at it to synthesize the complex world of digital credentials with an abstraction that might be useful to help us align existing solutions while adopting exciting new capabilities.

* [What BBS+ Means For Verifiable Credentials](https://www.youtube.com/watch?v%3DdXlRIrrb9f4) Evernym
  > In a recent Evernym blog post, [we discussed why BBS+ LD-Proofs](https://www.evernym.com/blog/bbs-verifiable-credentials/) are the privacy-preserving VC format that everyone should implement. In this webinar….

- A brief history of verifiable credential formats, and how a lack of convergence makes scale and interoperability an ongoing challenge
- How BBS+ Signatures are the breakthrough that combine the best of the JSON-LD and ZKP formats, while still allowing for selective disclosure and non-trackability
- The path forward: What remains to be done to fully converge on the BBS+ format
* [Is the verifiable credential trust triangle incomplete?](https://iiw.idcommons.net/3M/_Is_the_verifiable_credential_trust_triangle_incomplete%253F) by Riley Hughes

Fundamental problem:

- Why should a verifier trust a credential?

VC marketplace project at DIF is talking about a reputation system for issuers, using VCs

We need to agree on:

- Machine-readable document (governance framework)
- URI for a governance framework that we need to agree on

Sterre’s organization (TNO) is developing a software implementation called a “credential catalogue” which is like the yellow pages for verifiable credentials

- With yellow pages, who publishes it, and will everyone trust it? That brings us full-circle to the first issue

Drummond shared work at the Good Health Pass is tackling this

- Trust registries
- Rules engines
- Governance frameworks

Original question is: how does the verifier know who to trust? Then how do they know which governance framework to trust? Then who governs that list? And how do you trust that? It always comes full-circle

* [Verifiable Credentials for Authentic Data in the Supply Chain](https://iiw.idcommons.net/10G/_Verifiable_Credentials_for_Authentic_Data_in_the_Supply_Chain) by Gena Morgan, Kevin Dean

Using DiDs and VCs for verifiable product data in supply chains, leveraging the largest supply chain standard system in the world,

2.5 million users companies, over 6 billion product scans per day

Product data and attestations from a number of various authoritative sources

Leverage DIDs/VCs for distributed data sharing, verification

## 

* [Managing VCs at scale & the VC Stack](https://iiw.idcommons.net/index.php?title%3D12L/_Managing_VCs_at_Scale_%2526_the_VC_Stack%26action%3Dedit%26redlink%3D1) by Timothy Ruff & Alan Davies

* [https://twitter.com/rufftimo/status/1301314001251438593](https://twitter.com/rufftimo/status/1301314001251438593)

How does VC Functional Stack compare to [#ToIP](https://) Stack?

1. ToIP Layers 2 & 3 compare to Functional Layer 2

2. ToIP Layer 4 compares to Functional Layers 3 & 4 (horizontal layer for VC Management, vertical layer for Applications)

3. Functional stack doesn't require #blockchain

4. Functional Stack doesn't detail steps for trust or verification; ToIP Stack doesn't separate management or storage

5. Functional Stack clarifies functions, roles, and potential business models; ToIP stack clarifies trust & security They are complementary, not contradictory.

* [Trust Assurance in SSI / Verifiable Credential Ecosystems](https://iiw.idcommons.net/14F/_Trust_Assurance_in_SSI_/_Verifiable_Credential_Ecosystems) by Scott Perry

The meeting started with a presentation of an updated representation of a trust assurance model being promoted by the Trust over IP Foundation’s Governance Stack Working Group.

Given the audience of 8-10 people, we polled the reasons for attending a topic on Trust Assurance and discussed a few gnarly challenges in the space:

1. An owner of a background check company conveyed challenges with complying with a myriad of governance authority frameworks audited by a myriad of qualified/unqualified auditors looking at a myriad of evidence to render a judgement
2. The addition of privacy controls (notice and consent) to augment existing marketplace controls due to the specific need in SSI networks: [https://kantarainitiative.org/confluence/display/WA/Privacy+as+Expected%3A+UI+Signalling+a+Consent+Gateway+For+Human+Consent](https://kantarainitiative.org/confluence/display/WA/Privacy%2Bas%2BExpected%253A%2BUI%2BSignalling%2Ba%2BConsent%2BGateway%2BFor%2BHuman%2BConsent)
3. A discussion of the China Civil Code: [https://www.dlapiper.com/en/uk/insights/publications/2020/06/new-chinese-civil-code-introduces-greater-protection-of-privacy-rights-and-personal-information/](https://www.dlapiper.com/en/uk/insights/publications/2020/06/new-chinese-civil-code-introduces-greater-protection-of-privacy-rights-and-personal-information/)
4. A need for a civilian clearance credential.

It was a lively conversation for those who attended.

* [Figuring out Verifiable Credentials Exchange - combining Bloom, Aires Protocols, Presentation Exchange into a unified - Killer Whale Jello Salad](https://iiw.idcommons.net/22H/_Figuring_out_Verifiable_Credentials_Exchange_-_combining_Bloom,_Aires_Protocols,_Presentation_Exchange_into_a_unified_-_Killer_Whale_Jello_Salad) by Kaliya Young, Orie Steele, Drummond , Kyle et al

Credentials Exchange - figuring it out

Killer Whale Jello Salad

* [DIF Hosted WG charter Draft](https://docs.google.com/document/d/18L2-t4_2yrO_xZkwPjMCRcKIDiRGCziNs2X4k093pvo/edit%23heading%3Dh.xgh5sqxr7f2y)

Slides to complement this document - [https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit#slide=id.p](https://docs.google.com/presentation/d/1t4o6AXclqR7SqhGCbIJKVtYxh4fm_5mGT11MBx9K95c/edit%23slide%3Did.p)

Link to the document that the work and documentation is done in:

* [https://docs.google.com/document/d/1_b5MxzUPWzYxXxWt7Tw6-MySqh77ZvYHBnUgEBCFH7Q/edit#heading=h.dmkfjagb2ier](https://docs.google.com/document/d/1_b5MxzUPWzYxXxWt7Tw6-MySqh77ZvYHBnUgEBCFH7Q/edit%23heading%3Dh.dmkfjagb2ier)

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

* [IIW verifiable credentials - Decentralized VC integration with Eventbrite and Qiqo chat. This session will review the implementation process, lessons learned, and community discussion on related use cases.](https://iiw.idcommons.net/11A/_IIW_verifiable_credentials_-_Decentralized_VC_integration_with_Eventbrite_and_Qiqo_chat._This_session_will_review_the_implementation_process,_lessons_learned,_and_community_discussion_on_related_use_cases.) by Mike Vesey, Karl Kneis

* [Group Credentials/Multi-Issuer Credentials](https://iiw.idcommons.net/11B/_Group_Credentials/Multi-Issuer_Credentials) by Benji Kok

Current ssi solutions are geared to allow the issuance of a specific verifiable credential by a single issuer. There are use cases that would benefit from enabling the aggregation of multiple credentials into a single credential so that the holder can’t delete sub credentials of the aggregated credential. Is it possible to implement such an aggregation while allowing the holder to present only certain sub credentials of the aggregated credential as required?

An example use case is the issuance of credit history credentials. If each creditor issues separate credentials, the holder can delete the “bad” credentials and only present the “good” credentials. By enabling all creditors to contribute separately to a single credit history credential, the holder must either delete/present the whole credential.

* [GS1 2021 VC Prototype Journey](https://iiw.idcommons.net/20P/_GS1_2021_VC_Prototype_Journey) by Paul Dietrich

A overview of the GS1 Prototype effort for Q1-2 2021.

There was some feedback that  BBS, PE, and DIDCommV2 are possible points of convergence.

Also comments that WACI Bloom may play a part in convergence

* [Verifiable Credentials for Assets <30 min](https://iiw.idcommons.net/21E/_Verifiable_Credentials_for_Assets_30_min) by Mahmoud Alkhraishi

General Framework on how to think of VCs for Assets including leveraging GS1 and other vocabularies in the traceability vocab.

Requirements and Opportunities that block adoption of VCs in Supply chains
Current Status of work and Steps Forward

* [https://pmandic-my.sharepoint.com/:p:/g/personal/mahmoud_mavennet_com/EawHRlN0VqpPhiXxZfTnWdMBZxvZuIuA7_kAlEJDWEtthg?e=NVGUnK](https://pmandic-my.sharepoint.com/:p:/g/personal/mahmoud_mavennet_com/EawHRlN0VqpPhiXxZfTnWdMBZxvZuIuA7_kAlEJDWEtthg?e%3DNVGUnK)

* [Traceability Vocabulary v0.0](https://w3c-ccg.github.io/traceability-vocab/)

* [VC HTTP API (0.0.2-unstable)](https://w3c-ccg.github.io/vc-http-api)

* [Status List 2021](https://w3c-ccg.github.io/vc-status-list-2021/)

* [Credential-based login to a Pico-based application](https://iiw.idcommons.net/11P/_Credential-based_login_to_a_Pico-based_application) by Bruce Conrad

Verifiable credentials, authentication, picos, pico-based application

The slides are at [https://bruceatbyu.com/s/HRDDSiiw32](https://bruceatbyu.com/s/HRDDSiiw32)

* [SNARK-based anonymous credentials](https://iiw.idcommons.net/14B/_SNARK-based_anonymous_credentials) by Johannes Sedlmeir, Matthias Babel

An implementation of anonymous credentials using generic ZKPs, in our case, SNARKs. This gives a lot of flexibility as it replaces developing new, optimized “island” cryptography through generic tools and an “engineering” approach; however, at the cost of significant performance challenges compared to CL/BBS+.

So far, there has not been a cryptographic review on the code.

The major limitation is performance; while prover time is currently ~1s on a Macbook with 12 cores, the CPU and memory requirements are likely too high for general purpose smartphones and IoT devices. STARKs could help, but the larger proof size may be inhibiting.

The implementation covers private holder binding (potentially even using secure hardware for the binding key), private delegation (from the perspective of the holder), revocation, and range proofs for expiration.

A new feature that we implemented and that is probably difficult to achieve without generic ZKPs comprise, e.g., the “Leather Trousers” proof that can be used to demonstrate that an x and y coordinate are inside or outside a polygon defined by the verifier. It is also very easy to add further features that output a computation on the attributes, such as multiplying or adding different attributes.

The presentation slides and also the code will be made public by the end of July at [https://github.com/MatthiasBabel/heimdall](https://github.com/MatthiasBabel/heimdall).
The implementation is based on SNARKs, using the libraries [https://github.com/iden3/circom](https://github.com/iden3/circom) and [https://github.com/iden3/snarkjs](https://github.com/iden3/snarkjs).

* [Could an NFT be a VC?](https://iiw.idcommons.net/20I/_Could_an_NFT_be_a_VC%253F) by Grace Rachmany

Case discussed: A group of villages in Africa using a cryptocurrency platform for alternative currencies. Different organizations issue the coins under different circumstances. When you accept a currency, you want to know who is the issuer. The Red Cross might be more or less trusted than the local leader or agricultural cooperative as the issuer of a currency that is supposedly equivalent to a shilling.

What types of tech could be used for this?

- Multiple currencies on the blockchains
- Certifications in the form of some kind of NFT issued by the issuer.
- Limited supply tokens or NFTs that are “expired” when you use them
- Open Credential Publisher framework was suggested
- VCs are generally authorizations associated with a person, so maybe a person could have the VC and show their credit rating in some way while they are making a transaction
- Similarly maybe the VC belongs to the organization that is issuing the coin, proving its reputation over time.

* [Self Attested vs Chain of Custody - assurance levels in data provenance in VCs](https://iiw.idcommons.net/23G/_Self_Attested_vs_Chain_of_Custody_-_assurance_levels_in_data_provenance_in_VCs) by Stew Whitman & Alka Lachhwani

Identity Binding, Credential Binding, when they go high, we go low?

What levels of identity enrolment and binding of credential to identity are required for “good” SSI

Is (Using US centric NIST 800.63) IAL 1 sufficient, can self-attestation of identity and of a claim (e.g I am vaccinated) work.

There are two important factors in establishing “truth” or the trustworthiness of the information. Attributional and Reputational. You need to have both to have trust.

Digital needs higher level of attestation because it is easier to forge and easier to propagate that forgery.

If the risk level is low lower levels of reputation may be acceptable.

Definition of Trust - Sufficient information to leap into the unknown

A certificate must meet 4-criteria of definition
        Who issued it/ Who was it issued to/Has it been changed / Has it been revoked

So long as these attributes are clear the verifier can interrogate and make a decision based on the Attribution and Reputation of the issuer.

Concept of what is preferred by the verifier.

For the verifier it is based on risk, it is never going to be based on perfect information.

But it is most important to make sure that you are binding the credential to the correct identity

So what is the requirement for onboarding or enrolling an identity?

* [VCs Policy Committeee (California) – Participate in passing legislation to create a California Trust Framework!](https://iiw.idcommons.net/21B/_(California)_Verifiable_Credentials_Policy_Committeee_-_Come_learn_about_how_participate_in_passing_legislation_to_crete_a_California_Trust_Framework!) by Kaliya Young, Ally Medina

Link Slides: [https://docs.google.com/presentation/d/1VyxmWan3qbxynxhKvw1CHhWZINiPRF9gjeqSCSDh1MY/edit?usp=sharing](https://docs.google.com/presentation/d/1VyxmWan3qbxynxhKvw1CHhWZINiPRF9gjeqSCSDh1MY/edit?usp%3Dsharing)

TLDR:

We discussed how the Blockchain Advocacy Coalition’s sponsorship of [AB 2004](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id%3D201920200AB2004) pushed verifiable credentials into mainstream political discourse and how companies can help us shape public policy and government pilot programs of Verifiable Credential technology.

We are planning on working with legislators to introduce a bill that creates a California Trust Framework and lays the groundwork for use of the technology in the public and private sector.

Our coalition is funded by the companies who participate in it. If you are interested in being part of shaping legislation in California the will build the market for your tools and services please be in touch.  Remember what happens in California shapes what happens nationally and has a global impact.

Ally Medina - head of the Blockchain Advocacy Coalition - ally@blockadvocacy.org

Kaliya Young Chair of the Verifiable Credentials Policy Committee - Kaliya@identitywoman.net

* [What are Verifiable Credentials](https://academy.affinidi.com/what-are-verifiable-credentials-79f1846a7b9)

* Release the v1 of the [verifiable credentials specifications relationship diagram](https://github.com/manicprogrammer/vc-spec-rel/)

* [h/t @michaelruminer](https://twitter.com/michaelruminer/status/1328827452886540296) “Good for anyone but especially useful when trying to jump in on the deep end. If you walk even this limited tree of specs you know a lot.”

* [Paper based Verifiable Credentials](https://www.youtube.com/watch?v%3DEXvWxFjHvdY) Mattr

Paper-based Verifiable Credentials allow us to have a low-tech solution for adopting VC's in situations where access to a phone cannot be guaranteed. This presentation looks at how this solution can be used to aid with the distribution of Vaccine Credentials.
* [How W3C Verifiable Credentials (VC) Work: Part 1 – VC Issuance](https://blockster.global/self-sovereign-identity/)

When an issuer creates a verifiable credential, it contains following information –

- Who has issued – DID of the Issuer
- To whom it is issued – User Identifier
- Attributes of the credential – Details of the credential being Issued
- When it is Issued – Date of issuance
- Credential proof with Issuer signature that makes it tamper evident
- Revocation details

* [The Role of Witness Organizations in Verifiable Credentials](https://medium.com/@m.ruminer/on-the-role-of-witness-organizations-in-self-sovereign-identity-or-vcs-aren-t-just-p2p-e2cbafce6928)

Verifiable credentials aren’t just P2P.

* [...] The basis is that not every source of a verifiable credential has an interest in issuing verifiable credentials and that it is not only logical but beneficial to the ecosystem of trust that witness organizations will issue on behalf of these sources.
* [ERC-721 Non-Fungible Token Standard on Ethereum vs. VCs on Hyperledger Indy](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0059.html) Michael Herman
  > When are Hyperledger Indy/Sovrin VCs better than Ethereum smart contracts for NFEs/NFTs (non-fungible entities/tokens)?
  > 
  > It seems obvious but I don't have a detailed/worked out answer.  One project I'm associated with wants to use the [ERC-721 Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) on Ethereum but I believe VCs are a better route to take. Part of the desire to stay on Ethereum is there is quite a vibrant NFT community on Ethereum and lots of different EC-721 tokens.
* [The Flavors of Verifiable Credentials](https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf)

is complete and published on the [Linux Foundation Public Health Blog](https://www.lfph.io/2021/02/11/cci-verifiable-credentials-flavors-and-interoperability-paper/).

> The differences between the different flavors of VCs for technically inclined readers. It elaborated on the differences between JSON and JSON-LD and articulated differences between the two different implementations of ZKP style credentials. The ‘Journey of a VC’ section articulated all steps where VCs are active and highlighted the differences in how different VC flavors ’behave’.

### Azure AD Verifiable Credentials

* [Announcing Azure AD Verifiable Credentials](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/announcing-azure-ad-verifiable-credentials/ba-p/1994711) MS ID Blog
  > We started on a [journey with the open standards community](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/decentralized-digital-identities-and-blockchain-the-future-as-we/ba-p/1994714) to empower everyone to own and control their own identity. I’m thrilled to share that we’ve achieved a major milestone in making this vision real. Today we’re announcing that the public preview for Azure AD verifiable credentials is now available: organizations can empower users to control credentials that manage access to their information.

* [Azure AD Verifiable Credentials Entering Public Preview](https://www.kuppingercole.com/blog/bailey/azure-ad-verifiable-credentials-entering-public-preview) Kuppinger Cole
  > Microsoft announced on April 5, 2020 that its Azure AD Verifiable Credentials is now in public preview. This solution enables organizations to design and issue verifiable credentials to their users, be it enterprises issuing employment credentials to their employees, universities enrolling students or issuing diplomas, governments issuing passports, ID cards, and countless other uses.

* [Azure Active Directory VCs - preview introduction](https://daniel-krzyczkowski.github.io/Azure-AD-Verifiable-Credentials-Intro/) Daniel Krzyczkowski
  > Once I discovered that documentation is available, I decided to create a small proof of concept. I have configured Verifiable Credentials accordingly to [details in the documentation](https://docs.microsoft.com/en-us/azure/active-directory/verifiable-credentials/enable-your-tenant-verifiable-credentials) I have an existing Azure AD B2C tenant so it was much easier because users have to sign in first before they can be issued a verifiable credential.

* [Verifiable Credentials go mainstream at Identiverse 2022](https://www.biometricupdate.com/202206/verifiable-credentials-go-mainstream-at-identiverse-2022) Biometric Update

Verifiable Credentials was a breakthrough topic and it’s clearly on the path to mainstream adoption. Main sessions by Microsoft and Avast showcased their application of VCs in the IAM landscape, showing VCs aren’t the future anymore–they are the present.

VCs need Threat Modeling

* [Thread started by Pamela Dingle](https://twitter.com/pamelarosiedee/status/1537233243086327812?s%3D20%26t%3DWWt14_H4AXgtn09xb5-yew)

Another pre-read recommendation for @identiverse: the @openid for Verifiable Credentials Whitepaper.  It is a great high level explanation of decentralized benefits and use cases, both @kristinayasuda & @tlodderstedt contributed! OpenID for Verifiable Credentials

* [Firstyear Replying to @Erstejahre @pamelarosiedee and 4 others](https://twitter.com/Erstejahre/status/1537615778106658816)

It also seems to lack any sections about threat modelling and possible risks, making it hard to trust since risks are not directly and clearly addressed.

* [Torsten Lodderstedt Replying to @Erstejahre @pamelarosiedee and 3 others](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)

I agree. We thread model while we are designing the protocol, we also need to add it to the spec. Please note: we build on existing work. There is an extensive thread model for OAuth and countermeasures that we built on ([datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics). Feel free to contribute.
