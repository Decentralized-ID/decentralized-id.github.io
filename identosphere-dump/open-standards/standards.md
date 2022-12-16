---
published: false
---

# Standards

* [DIDs are not enough - we need an Authoriziation standard too](https://medium.com/energy-web-insights/api-access-security-for-dapps-cfcfa928623c) Energy Web

If you are a developer and want to write a DApp [...] you probably are using API-Keys in your front-end. If this is the case, then you should consider the security risk the publication of the API-Key in your front end represents and ask yourself if it would make sense to switch to a user authentication scheme.


## In general
* [FYI: What makes a standard ‘world class’?](https://lists.w3.org/Archives/Public/public-credentials/2021Aug/0213.html) Michael Herman (Trusted Digital Web) (Saturday, 14 August)
  > - A world class standard should have well-defined objectives that respond to real needs in a timely manner.
  > - Its technical content should be complete and accurate.
  > - It should be easy to understand (or as easy as the subject matter allows!) and easy to implement.
  > - Its requirements should be expressed clearly and unambiguously.
  > - It should be validated.
  > - It should be well-maintained.
  > 
  > Reference: [A Guide To Writing World Class Standards](https://www.etsi.org/images/files/Brochures/AGuideToWritingWorldClassStandards.pdf)
* [Trust Frameworks? Standards Matter](https://medium.com/@trbouma/trust-frameworks-standards-matter-47c946992f44) Tim Bouma
  > He points at the NIST documents about it [Developing Trust Frameworks to Support Identity Federations](https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8149.pdf) published in 2018. He also points at the Canadian government’s definition of standards.
  > 
  > “a document that provides a set of agreed-upon rules, guidelines or characteristics for activities or their results. Standards establish accepted practices, technical requirements, and terminologies for diverse fields.”  He goes on to highlight a lot of the work being done in Canada and where it all sits relative to being a standard - “In closing, there are lots of trust frameworks being developed today. But to be truly trusted, a trust framework needs to either apply existing standards or become a standard itself.”
* [Open standards should be developed openly](https://blog.weareopen.coop/open-standards-should-be-developed-openly-1f0cf552308d) WeAreOpen
  > Open standards should be developed openly because not enough people work to ensure that equity is central to innovation and development. We believe that openness is an attitude, and one which bears fruit over time from which everyone can benefit.

* [Global Standards Mapping Initiative](https://www.continuumloop.com/global-standards-mapping-initiative/) ContinuumLoop

This past November, the GBBC released [The Global Standards Mapping Initiative 2.0](https://gbbcouncil.org/wp-content/uploads/2021/11/GBBC-GSMI-2.0-Report-1.pdf), updating the [standards published in 2020](https://gbbcouncil.org/wp-content/uploads/2020/10/GSMI-Legal-Regulatory-Report.pdf). The GBBC is a strong proponent of standardization and intends to serve as a baseline for establishing frameworks and standards that will allow for adoption and innovation.
* [Premature Standardization & Interoperability](https://www.continuumloop.com/premature-standardization-interoperability/) Continuum Loop

Here’s my premise – we don’t have standards nor interoperability – at least not as people really need. We have been through a process that is powerful and good – but what we have is what I call “premature standardization.” It’s a great start but nowhere near where things will be.

* [Trinsic Basics: What Are SSI Standards?](https://trinsic.id/what-are-ssi-standards/)
  > There are two kinds of standards that Trinsic implements to enable interoperability and avoid vendor lock-in: data model standards and protocol standards.

* [Manifesto: Rules for standards-makers](http://scripting.com/2017/05/09/rulesForStandardsmakers.html)
  > I've used all kinds of formats and protocols in a long career as a software developer, even created a few. My new manifesto summarizes what I've learned about what works and what doesn't.


* [Linked Data Security](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0134.html) ([slide deck](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/att-0134/2021-Linked-Data-Security.pdf)
  > The attached slide deck provides a basic overview (with examples) of Linked Data Security as well as the specifications in that orbit. The W3C CCG is  actively developing a number of these specifications.
* [Roadmap: Verifiable Trust Standards](https://lists.w3.org/Archives/Public/public-credentials/2021Mar/0014.html)
  > Green - General data format standards
  > Yellow - Vocabulary standards (I the mislabeled VC work)
  > Magenta - Protocol standards (I mislabeled DID Resolution)
  > Red - Low-level cryptographic primitives
  > Purple - General crypto packaging/protocol standards
  > Orange - Application layer standards

### Verifier Universal Interface
* [Verifier Universal Interface by Gataca España S.L.](https://essif-lab.eu/verifier-universal-interface-by-gataca-espana-s-l/)
  > This draft version can be found at [https://gataca-io.github.io/verifier-apis/](https://gataca-io.github.io/verifier-apis/) and has been built using ReSpec.
  > This draft version for VUI includes today 6 APIs:
  > 
  > - Presentation Exchange
  > - Consent Management
  > - Schema resolution
  > - Issuer resolution
  > - ID resolution
  > - Credential status resolution


### WebAuthn

* [W3C WebAuthn V2 Now a Standard](https://self-issued.info/?p%3D2160) Mike Jones
  > While remaining compatible with the original standard, this second version adds additional features, among them for user verification enhancements, manageability, enterprise features, and an Apple attestation format. ([Recommendation](https://www.w3.org/TR/2021/REC-webauthn-2-20210408/)) ([CTAP also approaching standardization](https://self-issued.info/?p%3D2155).
* [Web Authentication: An API for accessing Public Key Credentials Level 2](https://www.w3.org/TR/2021/PR-webauthn-2-20210225/). This specification defines an API enabling the creation and use of strong, attested, scoped, public key-based credentials by web applications, for the purpose of strongly authenticating users.
* [Second Version of W3C Web Authentication (WebAuthn) advances to Proposed Recommendation (PR)](https://self-issued.info/?p%3D2149)
  > The World Wide Web Consortium (W3C) has published this [Proposed Recommendation (PR)](https://www.w3.org/TR/2021/PR-webauthn-2-20210225/) Level 2 specification, bringing the second version of WebAuthn one step closer to becoming a completed standard. While remaining compatible with the original standard, this second version adds additional features, among them for user verification enhancements, manageability, enterprise features, and an Apple attestation format.
* [Near-Final Second W3C WebAuthn and FIDO2 CTAP Specifications](https://self-issued.info/?p=2143)
  > The [W3C WebAuthn](https://www.w3.org/blog/webauthn/) and [FIDO2](https://fidoalliance.org/fido2/) working groups have been busy this year preparing to finish second versions of the W3C Web Authentication (WebAuthn) and FIDO2 Client to Authenticator Protocol (CTAP) specifications

### KMIP

* [OASIS releases KMIP 2.1](https://www.oasis-open.org/2020/12/18/key-management-interoperability-protocol-specification-and-key-management-interoperability-protocol-profiles-oasis-standards-published/)
  > The Key Management Interoperability Protocol (KMIP) is a single, comprehensive protocol for communication between clients that request any of a wide range of encryption keys and servers that store and manage those keys. By replacing redundant, incompatible key management protocols, KMIP provides better data security while at the same time reducing expenditures on multiple products.

### OMG
* [OMG ISSUES RFI FOR DISPOSABLE SELF-SOVEREIGN IDENTITY STANDARD](https://www.omg.org/news/releases/pr2021/01-21-21.htm)
  > This RFI aims to gain a better understanding of the self-sovereign identity space. In particular, the Blockchain PSIG is exploring the potential for standards setting in the area of contextually constrained or ‘disposable’ self-sovereign identity arrangements, building on top of existing W3C standards for self-sovereign identity [DID] and verifiable credentials [VC]. The aim of this RFI is to determine whether new standards for this specific aspect of self-sovereign identity are necessary, desirable and timely, and are not already being developed elsewhere. (The RFI)
A [public presentation on the Disposable Self-sovereign Identity RFI](https://www.brighttalk.com/webcast/12231/461001) will be held on February 3, 2021 at 11:00 AM ET.
  > The Object Management Group® (OMG®) is an international, open membership, not-for-profit technology standards consortium, founded in 1989. OMG standards are driven by vendors, end-users, academic institutions and government agencies. OMG Task Forces develop enterprise integration standards for a wide range of technologies and an even wider range of industries.


## Agents

* [Agent Frameworks & Infrastructure (“Layer 2”)](https://identity.foundation/faq/#agent-frameworks-infrastructure-layer-2)

* [Mobile Agent Development FAQ](https://iiw.idcommons.net/1L/_Mobile_Agent_Development_FAQ) by Horacio Nunez
  > - What’s the best place to start creating your own mobile agent?
  > - How do you get updates once you ship your first version?
  > - Do I actually have to support a fork for every mobile agent I create?
  > - Do I need to use a Mediator?


## Schema.org 

* [Schema.org is ten!](http://blog.schema.org/2021/06/schemaorg-is-ten.html)

Schema.org was founded on the idea of making it easier and simpler for the ordinary, everyday sites that make up the web to use machine-readable data, and for that data to enable an ecosystem of applications used by millions of people. While it's hard to predict exactly what the next decade will bring, if we can all keep these founding concerns in mind as we improve, refine and curate our growing collection of schemas, we'll be doing our part to continue improving the web.

## Identiverse
* [Reflections from Identiverse: Identity Security Threats & Trends](https://www.secureauth.com/blog/reflections-from-identiverse-identity-security-threats-and-trends/) SecureAuth
  > talks like [“Simplify Your Least-Privilege Journey with Access Analysis”](https://identiverse.com/idv2021/session/SESCI5F77RW8COIGZ/) and [“Managing and governing workload identities”](https://identiverse.com/idv2021/session/SESTZ5WNB1OMKD9EV/) definitively provide greater insight. [...] UberEther showed in [“User Behavior Analytics: Marrying Identity and the SOC Like Peanut Butter and Jelly”](https://pheedloop.com/identiverse2021/virtual/?page%3Dsessions%26section%3DSESKWZML7NBJX42P3) how UBA (User Behavior Analytics) and UEBA (User Events Behavior Analysis) deliver additional value to help avoid threats in real-time and provide visibility to analysts.

## Oasis
* [Managed Open Projects: A New Way For Open Source and Open Standards To Collaborate](https://www.oasis-open.org/2021/09/08/managed-open-projects/)

I recently pointed out in a [TechCrunch contribution](https://techcrunch.com/2021/06/09/a-revival-at-the-intersection-of-open-source-and-open-standards/) that the open source and open standards communities need to find ways to team up if they are to continue driving innovation and  development of transformative technologies to push our society forward.

## JSON

* [JSON is Robot Barf](https://www.windley.com/archives/2021/09/json_is_robot_barf.shtml) Windley

JSON has its place. But I think we're overusing it in places where a good notation would serve us better.

## ISO 27001
* [WAYF certificeret efter ISO 27001](https://www.wayf.dk/en/node/317)

WAYF has now been certified according to the standard for information security ISO 27001. This is the result of the audit that DNV conducted at WAYF on 23 September 2021. Language Danish Read more about WAYF certified according to ISO 27001
* [What Is ISO 27001:2013? A Guide for Businesses](https://auth0.com/blog/what-is-iso-27001-2013-a-guide-for-businesses/)
  > ISO 27001 is also the cornerstone of a growing international consensus about data security best practices. Australia based its federal Digital Security Policy on ISO 27001. Likewise, ISO 27001 can provide guidance on how to meet the standards of other data privacy laws, such as the GDPR, which often direct companies to it as an example of universal best practices. So if you abide by ISO 27001’s recommendations, you’re on the right track for legal compliance, not to mention improved data security.

## OpenBadges

* [Open Recognition is for every type of learning](https://blog.weareopen.coop/open-recognition-is-for-every-type-of-learning-ffd137a6fe17) From cold hard credentialing to warm fuzzy recognition

we want to explain what we talk about when we talk about Open Recognition. It builds on this [previous post](https://blog.weareopen.coop/what-is-open-recognition-anyway-9f38ec1f8629), and aims to move from the abstract to practicalities.
* [Keep Badges Weird is about breaking boundaries: How the KBW community is convening systems](https://blog.weareopen.coop/keep-badges-weird-is-about-breaking-boundaries-42afb0415826) WeAreOpenCoop

KBW helps people understand the badge landscape. The community is there to provide solidarity for badge champions and newbies. We do not assume prior knowledge of Open Badges or Verifiable Credentials. We recognise and celebrate those who can share their experience. Anyone interested in badges or integrating [Open Recognition](https://blog.weareopen.coop/what-is-open-recognition-anyway-9f38ec1f8629) are welcome to join.
* [Keep Badges Weird…](https://blog.weareopen.coop/keep-badges-weird-e26a1b055ff5) at the Badge Summit
  > We have a new suite of badges to encourage participation, create value for others, and reflect on that experience. Participants will be able to both earn AND award badges, so they’ll have a chance to prove that they’ve understood the theory surrounding CoPs and badges as well as put those theories into practice.
* [Discover Open Badges 3.0!](https://app.participate.com/communities/keep-badges-weird/62003f3f-a7ba-4f6a-990a-64d6f893016d/announcements/0bc15852-0f91-48c8-a7ca-478b246b553c) Keep Badges Weird
  > 1. Check out the (accepted) [Open Badges 3.0 proposal](https://github.com/IMSGlobal/openbadges-specification/files/6977048/Proposal-Open-Badges-3.0-update-08-11-2021.pdf)​
  > 2. ​[Watch a video](https://www.youtube.com/watch?v%3DQDGPwR1F3FY%26t%3D1357s) from the ePIC conference giving an overview of what Open Badges 3.0 will enable (or view the [slide deck](https://docs.google.com/presentation/d/1NEJoQaI9b6KC1EFDDhR3MGybGVoa0R3bQh0xuKtUKkY)
  > 3. Discuss what this means for you, your organisation, or your community in [this thread](https://app.participate.com/discussions/open-badges-3-0/68917656-db8f-4932-88fd-153fdb54e285)​
* [Reflecting on the Evolving Badges and Credentials Ecosystem](https://blog.weareopen.coop/reflecting-on-the-evolving-badges-and-credentials-ecosystem-6efac4d673d3)
  > Recently, the WAO team took the opportunity to update the badge platforms page on Badge Wiki, a knowledgebase for the Open Badge community. As the ecosystem continues to evolve we’re seeing some early platforms fall by the wayside and new platforms emerge.
* [What is Open Recognition, anyway?](https://blog.weareopen.coop/what-is-open-recognition-anyway-9f38ec1f8629) Going beyond credentialing and the formal/informal divide
  > Badges as credentials includes approaches that are well understood and largely replace or augment existing certification practices. Badges for recognition, however, include approaches that remain somewhat confusing to many people.

## Blockcerts

* [Blockcerts V3 release](https://community.blockcerts.org/t/blockcerts-v3-release/3022)
  > The main change is the alignment with the [W3C Verifiable Credentials specification 3](https://www.w3.org/TR/vc-data-model/).
  > 
  > Regarding the standard itself metadata and display are entering the default standard. metadata comes in replacement of metadataJson and remains a stringified JSON that will allow consumers to register specific data which are too unique for issuances to be defined in the context.
  > 
  > display brings in [a little bit of novelty 2](https://github.com/blockchain-certificates/cert-schema/blob/master/cert_schema/3.0/displaySchema.json%23L6) images or pdfs, in addition to the more classic HTML.
* [Blockcerts v3 release, a Verifiable Credentials implementation](https://lists.w3.org/Archives/Public/public-credentials/2021Dec/0051.html)  Julien Fraichot (Monday, 13 December)
  > I am excited to share with you today the release of [Blockcerts](https://www.blockcerts.org/) V3. As you may already know the earlier versions of Blockcerts were architected by Kim H. Duffy through Learning Machine and leveraged the Open Badge standard.
  > 
  > We have followed through with the initial [ideas established at RWOT 9 in Prague in December 2019, to align Blockcerts with the Verifiable Credential specification](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/final-documents/BlockcertsV3.md).

### XSL SDI

* [XSL Labs: Your Data Belongs to You](https://www.xsl-labs.io/whitepaper/white_paper_en.pdf)

The SDI technology constitutes a very important example of decentralized counter-power to the web giants. The SDI maintains to keep the practicality of a unique identifier while guaranteeing the security of the data and the user's sovereignty over it

### CCI
* [Use Case Implementation Workstream](https://covidcreds.groups.io/g/usecaseCCI) [usecaseCCI@covidcreds.groups.io](mailto:usecaseCCI@covidcreds.groups.io)

This is the Use Case Implementation Workstream of the [COVID Credentials Initiative (CCI)](https://www.covidcreds.com/). This workstream identifies privacy-preserving verifiable credentials (VCs) that are most useful to the COVID-19 response and provides a forum and platform for those who are implementing COVID VCs to present their projects/solutions.

### VON\ION
* [@csuwildcat](https://twitter.com/csuwildcat) shares
  > As of Friday, we believe v1 of ION is functionally code complete, and the Sidetree Working Group at DIF (@DecentralizedID) should have a v1 spec candidate ready for the underlying protocol by Jan 21st. Public v1 launch of the ION network on Bitcoin mainnet is just weeks away.


## Oberon protocol

* [Better and more secure methods for API authentication](https://iiw.idcommons.net/1D/_Better_and_more_secure_methods_for_API_authentication) by Michael Lodder

Presentation slides: [https://docs.google.com/p>resentation/d/1UO25DzVmq25ya2S4_tV5UKTSP6NtBggln9vP1TEXSzE/edit](https://docs.google.com/presentation/d/1UO25DzVmq25ya2S4_tV5UKTSP6NtBggln9vP1TEXSzE/edit)

Goal of the Oberon protocol when building an API:

- Super effective: no separate session token to required for accessing the API; very fast to issue and verify tokens; 128 bytes required per message
- Privacy preserving
- No new crypto, uses BLS signature keys and Pointecheval saunders Construction

### Timestamping

* [Trusted Timestamping Part 3: Family of Standards](https://medium.com/finema/trusted-timestamping-part-3-family-of-standards-f0c89a5e97ab) Nunnaphat Songmanee Finema

Read more about timestamping and its concepts at [Trusted Timestamping Part 1: Scenarios](https://medium.com/finema/trusted-timestamping-part-1-scenarios-9bf4a7cc2364) and [Trusted Timestamping Part 2: Process and Safeguards](https://medium.com/finema/trusted-timestamping-part-2-process-and-safeguards-f75286a0c370).

Family of standards related to timestamping

## GAIN

- [Nat has a presentation](https://nat.sakimura.org/2021/09/14/announcing-gain/)
- There is a [linked in Group](https://www.linkedin.com/groups/12559000/)

### OASIS
* [Secure QR Code Authentication v1.0 from ESAT TC approved as a Committee Specification](https://www.oasis-open.org/2022/07/12/secure-qr-code-authentication-v1-0-from-esat-tc-approved-as-a-committee-specification/)

An alternative to passwords that includes QR Codes is described, and typical use cases are described. This document also provides an overview and context for using QR Codes for security purposes.

## JWP

* [JSON Web Proofs BoF at IETF 114 in Philadelphia](https://self-issued.info/?p%3D2286)
- [Chair Slides](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-json-web-proofs-chair-drafts-00) – [Karen O’Donoghue](https://twitter.com/kodonog) and [John Bradley](https://twitter.com/ve7jtb)
- [The need: Standards for selective disclosure and zero-knowledge proofs](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-the-need-standards-for-selective-disclosure-and-zero-knowledge-proofs-00) – [Mike Jones](https://twitter.com/selfissued)
- [What Would JOSE Do? Why re-form the JOSE working group to meet the need?](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-the-need-standards-for-selective-disclosure-and-zero-knowledge-proofs-00) – [Mike Jones](https://twitter.com/selfissued)
- [A Look Under the Covers: The JSON Web Proofs specifications](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-json-web-proofs-initial-drafts-00) – Jeremie Miller


### ONDC
* [ONDC: An Open Network for Ecommerce](https://www.windley.com/archives/2022/08/ondc_an_open_network_for_ecommerce.shtml) Phil Windley
* [Open Network for Digital Commerce](https://en.wikipedia.org/wiki/Open_Network_for_Digital_Commerce) is a non-profit established by the Indian government to develop open ecommerce. The goal is to end platform monopolies in ecommerce using an open protocol called [Beckn](https://developers.becknprotocol.io/). I'd never heard of Beckn before. From the reaction on the VRM mailing list, not many there had either.

## JWT



### BBS Creds
- [aries-rfcs/0646-bbs-credentials#drawbacks](https://github.com/hyperledger/aries-rfcs/tree/main/features/0646-bbs-credentials%23drawbacks)
- [Zero-Knowledge Proofs Do Not Solve the Privacy-Trust Problem of Attribute-Based Credentials: What if Alice Is Evil?](https://ieeexplore.ieee.org/document/9031545) IEEE


## C2PA
* [FYI: C2PA Releases Specification of World’s First Industry Standard for Content Provenance](https://lists.w3.org/Archives/Public/public-credentials/2022Jan/0207.html)  Leonard Rosenthol (Wednesday, 26 January)

Just wanted to update folks here that the C2PA has released version 1.0 of their specification at [https://c2pa.org/specifications/specifications/1.0/index.html](https://c2pa.org/specifications/specifications/1.0/index.html).  As previously mentioned, it includes native support for VC’s for use in identification of actors (be they human, organizations, etc.).  Thanks to everyone here for their input on our work and helping us to deliver.

