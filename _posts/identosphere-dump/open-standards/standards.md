---
published: false
---

# Standards

* [Decentralised Identity: What’s at Stake?](https://inatba.org/wp-content/uploads/2020/11/2020-11-INATBA-Decentralised-Identity-001.pdf) A Position Paper by the INATBA Identity Working Group
  > INATBA has a specific Standards Committee to liaison with relevant standardisation committees and bodies. Some relevant standardisation committee and bodies include:
- [ISO/TC 307 “Blockchain and distributed ledger technologies”](https://www.iso.org/committee/6266604.html)
- [CEN/CENELEC JTC 19 “Blockchain and Distributed Ledger Technologies”](https://standards.iteh.ai/catalog/tc/cen/d96ab6b7-aac8-49e9-9ac5-b391bbd2abdc/cen-clc-jtc-19)
- [Decentralised Identifiers (DIDs)](https://w3c.github.io/did-core/)
- [DID Resolution](https://w3c-ccg.github.io/did-resolution/)
- [Verifiable Credentials (VCs)](https://www.w3.org/TR/vc-data-model/)
- “[Issuer](https://github.com/w3c-ccg/vc-issuer-http-api)” and “[Verifier](https://github.com/w3c-ccg/vc-verifier-http-api)” API, [​Linked Data Vocabulary](https://digitalbazaar.github.io/citizenship-vocab/)
- [Credential Handler API](https://w3c-ccg.github.io/credential-handler-api/)
- [DID SIOP](https://identity.foundation/did-siop/)
- [DID Comm](https://github.com/decentralized-identity/didcomm-messaging)
- [Trust over IP Foundation](https://trustoverip.org/)
- [Hygiene for a computing pandemic: separation of VCs and ocaps/zcaps](https://lists.w3.org/Archives/Public/public-credentials/2020Dec/0028.html)
    - You *could* implement zcap-ld on top of VCs…
    - However, you're actually squishing together what should be a separation of concerns in a way that will become *unhygienic*. Like a lack of proper biological hygiene, the result is sickness in our computing systems.
    - The observation of "these things seem so similar though!" is true, but you can already make that claim even if you're just looking at the linked data proofs layer. VCs and zcap-ld diverge from there for two very separate purposes: what is said, and what is done.

* [distributed ID learning path](https://translate.google.com/translate?sl=auto&tl=en&u=https://kristinayasuda.com/posts/decentralized-identity-catch-up-path/) Christina Yasuda based on [VC-Spec](https://github.com/decentralized-identity/vc-spec-map) Map by Michael Ruminer
first describes pre-requisite knowledge, including JSON, JSON-LD, JWT, JWS, JWK, JWA, and sometimes CBOR. She then goes on to break down knowledge areas beginning with the basics: DID-Core, DID-Resolution, DID-Spec, DID Use-Cases. Next, she covers Verifiable Credentials with VC-Data Model, VC Use-Cases, and VC-Implementors Guide, and also Transport, Credential Presentation, and Other Data Formats.
[CCG Highlights](https://lists.w3.org/Archives/Public/public-credentials/)

* [Linked Data Security](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0134.html) (
[slide deck](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/att-0134/2021-Linked-Data-Security.pdf)

The attached slide deck provides a basic overview (with examples) of Linked Data Security as well as the specifications in that orbit. The W3C CCG is  actively developing a number of these specifications.

* [Roadmap: Verifiable Trust Standards](https://lists.w3.org/Archives/Public/public-credentials/2021Mar/0014.html)

Green - General data format standards

Yellow - Vocabulary standards (I the mislabeled VC work)

Magenta - Protocol standards (I mislabeled DID Resolution)

Red - Low-level cryptographic primitives

Purple - General crypto packaging/protocol standards

Orange - Application layer standards

* [did:orb slides Troy Ronda (SecureKey)](https://lists.w3.org/Archives/Public/public-credentials/2021Mar/0017.html)

The slides for today’s did:orb presentation can be found here

Motivation – Enable monitorable ledgers

- Decouple witness ledgers from the critical path.
- Allow for Trust but Verify model.
- Leverage the Certificate Transparency model
- Witnesses observe VDR objects and promise to include in their ledgers.
- Provide a signed timestamp and a maximum merge delay.
- Enable monitoring to ensure witnesses follow their promises.
- Use trusted Witness (and origin) timings to resolve late publishing.
- Use origin to enable observers to know if they have the latest operations.

* [Technical Report on the Universal RDF Dataset Normalization Algorithm](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/att-0032/Mirabolic_Graph_Iso_Report_2020_10_19.pdf) - [Bill Bradley](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0032.html)
  > The goal of this technical report is to review the Universal RDF Dataset Normalization Algorithm (URDNA2015) for correctness and to provide satisfactory evidence that possible issues with URDNA2015 have been considered and dismissed. We do not lay out the algorithm in its considerable technical detail here, but refer the reader to the proposed technical specification 1 [Longley], a set of proofs by Rachel Arnold and Dave Longely [Arnold], and a reference implementation in Python [DigitalBazaar].
* [The 7 Laws of Identity Standards](https://openid.net/2021/04/10/the-7-laws-of-identity-standards/) OpenID

1. A identity standard’s adoption is driven by its value of the reliability, repeatability and security of its implementations.
2. A standard’s value can be measured by the number of instances of certified technical conformance extant in the market.
3. Certified technical conformance is necessary but insufficient for global adoption.
4. Adoption at scale requires widespread awareness, ongoing technical improvement and a open and authoritative reference source.
5. When Libraries/Directories/ Registries act as authoritative sources they amplify awareness, extend adoption and promote certification.
6. Certified technical conformance importantly complements legal compliance and together optimize interoperability.
7. Interoperability enhances security, contains costs and drives profitability.

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
* [Trust Frameworks? Standards Matter](https://medium.com/@trbouma/trust-frameworks-standards-matter-47c946992f44) Tim Bouma
  > He points at the NIST documents about it [Developing Trust Frameworks to Support Identity Federations](https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8149.pdf) published in 2018. He also points at the Canadian government’s definition of standards.
  > 
  > “a document that provides a set of agreed-upon rules, guidelines or characteristics for activities or their results. Standards establish accepted practices, technical requirements, and terminologies for diverse fields.”  He goes on to highlight a lot of the work being done in Canada and where it all sits relative to being a standard - “In closing, there are lots of trust frameworks being developed today. But to be truly trusted, a trust framework needs to either apply existing standards or become a standard itself.”

* [Mike Jones shares](https://self-issued.info/?p=2136) that CBOR (Concise Binary Object Representation)  is officially a [specification at IETF](https://www.rfc-editor.org/rfc/rfc8943) - woohoo! and it is a key part of [ISO’s mDL standard](https://www.iso.org/committee/45144.html) (date fields must use it).
  > The Concise Binary Object Representation (CBOR), as specified in RFC 7049, is a data format whose design goals include the possibility of extremely small code size, fairly small message size, and extensibility without the need for version negotiation.
* [W3C WebAuthn V2 Now a Standard](https://self-issued.info/?p%3D2160) Mike Jones
  > While remaining compatible with the original standard, this second version adds additional features, among them for user verification enhancements, manageability, enterprise features, and an Apple attestation format. ([Recommendation](https://www.w3.org/TR/2021/REC-webauthn-2-20210408/)) ([CTAP also approaching standardization](https://self-issued.info/?p%3D2155).
* [Federated Identity, InCommon, and Enabling Federated Access to Research Services](https://njedge.net/blog/federated-identity-incommon-and-enabling-federated-access-to-research-services/)
  > The panel will review the concepts of federated identities, authentication, and the role attributes play in managing access to services. They’ll further describe how the InCommon Federation and eduGAIN enable academic collaboration across local, regional, national, and international scales, discuss technical alternatives for participation in InCommon, and delve a bit into how research communities and research cyberinfrastructures manage federated access to their services.
* [An overview of blockchain technical standards](https://www.weforum.org/whitepapers/global-standards-mapping-initiative-an-overview-of-blockchain-technical-standards)

This October report is the most comprehensive review of global standards around blockchain tech that we’ve seen. Here’s a list of standards bodies included in a chart towards the end:

- [IEEE](https://standards.ieee.org/) (IoT; Cryptocurrency exchange & payment; tokens; energy; digital assets)
- [ISO](https://www.iso.org/standards.html) (Security; identity)
- [W3C](https://www.w3.org/standards/) (Identity)
- [IRTF](https://irtf.org/) (Identity; digital assets)
- [IEC](https://www.iec.ch/) (IoT)
- [IETF](https://www.ietf.org/standards/) (Cryptocurrency payment)
- [ITU-T](https://www.itu.int/en/ITU-T/publications/Pages/default.aspx) (Security; IoT; identity; DLT requirements)
- [BSI](https://www.bsigroup.com/en-GB/standards/) (DLT requirements)
- [CEN](https://www.cen.eu/Pages/default.aspx); [CENELEC](https://www.cenelec.eu/) (Security)
- [Standards Australia](https://www.standards.org.au/) (Security; DLT taxonomy)
- [WIPO](http://www.wipo.int/) (Blockchain for intellectual property)
- [ETSI](https://www.etsi.org/standards) (Permissioned ledgers)
- [SAC](http://www.sac.gov.cn/sacen/) (DLT requirements)
- [BRIBA](https://www.beltandroadblockchain.org/) (DLT requirements)
- [CESI](http://www.cc.cesi.cn/english.aspx) (Tokens; security)
- [DCSA](https://dcsa.org/) (Interoperability)
- [International Chamber of Commerce](https://iccwbo.org/) (Interoperability)
- [EEA](https://entethalliance.org/) (Interoperability; tokens)
- [Hyperledger](https://www.hyperledger.org/) (Interoperability; tokens)
- [IWA](https://interwork.org/) (Tokens; analytics)
- [JWG](https://intervasp.org/) (Tokens)
- [National Blockchain and Distributed Accounting Technology Standardization Technical Committee](https://tech.sina.com.cn/it/2018-05-10/doc-ihaichqz3607998.shtml) (DLT requirements\terminology)
- [CDC](https://digitalchamber.org/initiatives/) (Digital assets)
- [MOBI](https://dlt.mobi/) (Vehicle identity; usage-based insurance; electric vehicle grid integration; connected mobility and data marketplace; supply chain and finance; securitization and smart contracts)
- [GDF](https://www.gdfi.io/) (DLT requirements)
- [BIG](https://blockchainindustrygroup.org/) (DLT requirements)
- [BIA](https://bialliance.io/) (Interoperability)
- [BiTA](https://www.bita.studio/) (Interoperability; DLT requirements)

* [OpenID Connect Credential Provider](https://medium.com/mattr-global/introducing-oidc-credential-provider-7845391a9881) Mattr
* [OIDC Credential Provider](https://mattrglobal.github.io/oidc-client-bound-assertions-spec/) is “an extension to OpenID Connect which enables the end-user to request credentials from an OpenID Provider and manage their own credentials in a digital wallet.”

* [OASIS releases KMIP 2.1](https://www.oasis-open.org/2020/12/18/key-management-interoperability-protocol-specification-and-key-management-interoperability-protocol-profiles-oasis-standards-published/)
  > The Key Management Interoperability Protocol (KMIP) is a single, comprehensive protocol for communication between clients that request any of a wide range of encryption keys and servers that store and manage those keys. By replacing redundant, incompatible key management protocols, KMIP provides better data security while at the same time reducing expenditures on multiple products.

* [OMG ISSUES RFI FOR DISPOSABLE SELF-SOVEREIGN IDENTITY STANDARD](https://www.omg.org/news/releases/pr2021/01-21-21.htm)
  > This RFI aims to gain a better understanding of the self-sovereign identity space. In particular, the Blockchain PSIG is exploring the potential for standards setting in the area of contextually constrained or ‘disposable’ self-sovereign identity arrangements, building on top of existing W3C standards for self-sovereign identity [DID] and verifiable credentials [VC]. The aim of this RFI is to determine whether new standards for this specific aspect of self-sovereign identity are necessary, desirable and timely, and are not already being developed elsewhere. (The RFI)

A [public presentation on the Disposable Self-sovereign Identity RFI](https://www.brighttalk.com/webcast/12231/461001) will be held on February 3, 2021 at 11:00 AM ET.
  > The Object Management Group® (OMG®) is an international, open membership, not-for-profit technology standards consortium, founded in 1989. OMG standards are driven by vendors, end-users, academic institutions and government agencies. OMG Task Forces develop enterprise integration standards for a wide range of technologies and an even wider range of industries.
* [Web Authentication: An API for accessing Public Key Credentials Level 2](https://www.w3.org/TR/2021/PR-webauthn-2-20210225/). This specification defines an API enabling the creation and use of strong, attested, scoped, public key-based credentials by web applications, for the purpose of strongly authenticating users.
* [Second Version of W3C Web Authentication (WebAuthn) advances to Proposed Recommendation (PR)](https://self-issued.info/?p%3D2149)
  > The World Wide Web Consortium (W3C) has published this [Proposed Recommendation (PR)](https://www.w3.org/TR/2021/PR-webauthn-2-20210225/) Level 2 specification, bringing the second version of WebAuthn one step closer to becoming a completed standard. While remaining compatible with the original standard, this second version adds additional features, among them for user verification enhancements, manageability, enterprise features, and an Apple attestation format.
## Identity not SSI

* [Near-Final Second W3C WebAuthn and FIDO2 CTAP Specifications](https://self-issued.info/?p=2143)

The [W3C WebAuthn](https://www.w3.org/blog/webauthn/) and [FIDO2](https://fidoalliance.org/fido2/) working groups have been busy this year preparing to finish second versions of the W3C Web Authentication (WebAuthn) and FIDO2 Client to Authenticator Protocol (CTAP) specifications
* [Announcing Schema Markup Validator: validator.schema.org (beta)](http://blog.schema.org/2021/05/announcing-schema-markup-validator.html)

SDTT is a tool from Google which began life as the [Rich Snippets Testing Tool](https://developers.google.com/search/blog/2010/09/rich-snippets-testing-tool-improvements) back in 2010. Last year Google [announced plans](https://developers.google.com/search/blog/2020/07/rich-results-test-out-of-beta) to migrate from SDTT to successor tooling, the [Rich Results Test](https://search.google.com/test/rich-results), alongside plans to "deprecate the Structured Data Testing Tool". The newer Google tooling is focused on helping publishers who are targeting specific schema.org-powered [searc](https://developers.google.com/search/docs/guides/search-gallery)[h features](https://www.blogger.com/) offered by Google, and for these purposes is a huge improvement as it contextualizes many warnings and errors to a specific target application.

* [JSON-LD Playground](https://json-ld.org/playground/)

Play around with JSON-LD markup by typing out some JSON below and seeing what gets generated from it at the bottom of the page. Pick any of the examples below to get started.

NOTE: The playground uses [jsonld.js](https://github.com/digitalbazaar/jsonld.js) which [conforms](https://github.com/digitalbazaar/jsonld.js%23conformance) to JSON-LD 1.1 [syntax](https://www.w3.org/TR/json-ld11/) ([errata](https://w3c.github.io/json-ld-syntax/errata/)), [API](https://www.w3.org/TR/json-ld11-api/) ([errata](https://w3c.github.io/json-ld-api/errata/)), and [framing](https://www.w3.org/TR/json-ld11-framing/) ([errata](https://w3c.github.io/json-ld-framing/errata/)). Also see the classic [JSON-LD 1.0 playground](https://json-ld.org/playground/1.0/) and the [RDF Distiller](http://rdf.greggkellogg.net/distiller).
## Standards
* [Do I Need a Verifiable Credential?](https://community.rsa.com/t5/rsa-labs-blog/do-i-need-a-verifiable-credential/ba-p/610241)
* [What is a DID? Part 1](https://www.youtube.com/watch?v%3DOYYtxVEra1c) XSL Labs
* [Qu’est-ce qu’un DID? Partie 1](https://www.youtube.com/watch?v%3DVNLKufTDM4o) XSL Labs
* [Verifiable Claim Protocol](https://github.com/ontio/ontology-DID/blob/master/docs/en/claim_spec.md) Ontology

This isn’t new, but it’s new to us, and thought our readers might appreciate it, in case you have also wondered about the nuts and bolts behind OntID

* [Open Badges as Verifiable Credentials](https://kayaelle.medium.com/in-the-w3c-vc-edu-call-on-june7-2021-we-discussed-open-badges-asserted-as-w3c-verifiable-90391cb9a7b7)

In the [W3C VC-EDU](https://w3c-ccg.github.io/vc-ed/) call on June 7, 2021 we discussed [Open Badges](https://openbadges.org/) asserted as [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model/) (VCs). This call began the public discussion of Open Badges as Native VCs (potentially as Open Badges 3.0) to inform the IMS Open Badges Working Group. Why are we discussing this? Why does it matter? How will it work?

* [ToIP Primer](https://trustoverip.org/wp-content/uploads/sites/98/2020/05/toip_050520_primer.pdf)

A history of procedural trust, leading to an overview of the TOIP stack.

* [ToIP Stack Diagram Preview](http://elanica.com/sandbox/)

Interactive

* [Decentralized Identity FAQ](https://identity.foundation/faq/%23agent-frameworks-infrastructure-layer-2)

DIF

* [Bloom donates WACI](https://medium.com/decentralized-identity/bloom-donates-waci-790f902ac9bd)

At its core, WACI can be thought of as a handshake using classic, industry-standard [JWT](https://datatracker.ietf.org/doc/html/rfc7519)s: the “Relying Party” signs a token given to the end-user’s wallet, and the wallet signs over a “challenge” contained within it, proving ownership of a DID.

* [The Verifiable Economy: Fully Decentralized Object (FDO) Example: Bob’s UDID Document](https://hyperonomy.com/2021/06/15/the-verifiable-economy-fully-decentralized-object-fdo-example-bobs-udid-document/)

Strongly-typed Code to Generate Bob’s UDID Document
* [Security Event Tokens, Subject Identifiers, and SSE/CAEP/RISC Java implementation](https://domsch.com/IIW32/IIW32-openid-sse-model.pdf) Matt Domsch, VP & Engineering Fellow
  > • Security Event Tokens – RFC 8417
  > • Subject Identifiers – Internet Draft RFC
  > • Shared Signals & Events – OpenID Foundation WG
  > • Includes RISC, CAEP, and Oauth event profiles

* [Schema.org is ten!](http://blog.schema.org/2021/06/schemaorg-is-ten.html)

Schema.org was founded on the idea of making it easier and simpler for the ordinary, everyday sites that make up the web to use machine-readable data, and for that data to enable an ecosystem of applications used by millions of people. While it's hard to predict exactly what the next decade will bring, if we can all keep these founding concerns in mind as we improve, refine and curate our growing collection of schemas, we'll be doing our part to continue improving the web.
* [DIF Grant #1: JWS Test Suite](https://blog.identity.foundation/dif-grant-1-jws-test-suite/)

DIF announces its first community microgrant, sponsored by Microsoft and rewarding the timely creation of a comprehensive test suite for detached-JWS signatures on Verifiable Credentials

* [How a combination of Federated identity and Verifiable Credentials can help with Customer onboarding](https://pranavkirtani.medium.com/how-a-combination-of-federated-identity-and-verifiable-credentials-can-help-with-customer-7e6518feb018) Pranav Kirtani

Before we dive into how Federated systems like OIDC and SAML along with Verifiable Credentials (VC) can help improve customer onboarding to your application, let us first understand what are the current methods being used for onboarding.
* [Reflections from Identiverse: Identity Security Threats & Trends](https://www.secureauth.com/blog/reflections-from-identiverse-identity-security-threats-and-trends/) SecureAuth

talks like [“Simplify Your Least-Privilege Journey with Access Analysis”](https://identiverse.com/idv2021/session/SESCI5F77RW8COIGZ/) and [“Managing and governing workload identities”](https://identiverse.com/idv2021/session/SESTZ5WNB1OMKD9EV/) definitively provide greater insight. [...] UberEther showed in [“User Behavior Analytics: Marrying Identity and the SOC Like Peanut Butter and Jelly”](https://pheedloop.com/identiverse2021/virtual/?page%3Dsessions%26section%3DSESKWZML7NBJX42P3) how UBA (User Behavior Analytics) and UEBA (User Events Behavior Analysis) deliver additional value to help avoid threats in real-time and provide visibility to analysts.

* [Kaliya Young on Identikit with Michelle Dennedy](https://identitywoman.net/podcast-identikit-with-michelle-dennedy/)

our latest series examining the evolution of digital identity, and how self-sovereign identity, specifically, can advance a consent-based economy.


* [DIF Grant #1: JWS Test Suite](https://medium.com/decentralized-identity/dif-grant-1-jws-test-suite-a26cc4a95540)

The Claims and Credentials Working Group will be overseeing a new work item open to all DIF members that creates and harden a JWS test suite, with this grant funding a lead editor to drive the work and keep it to a pre-determined timeline, paid upon stable and complete release.

* [Shared Signals: An Open Standard for Webhooks](https://openid.net/2021/08/24/shared-signals-an-open-standard-for-webhooks/) OpenID

The OpenID Foundation formed the “[Shared Signals and Events](https://openid.net/wg/sse/)” (SSE) Working Group as a combination of the previous OpenID RISC working group and an informal industry group that was focused on standardizing [Google’s CAEP proposal](https://cloud.google.com/blog/products/identity-security/re-thinking-federated-identity-with-the-continuous-access-evaluation-protocol). These represented two distinct applications of the same underlying mechanism of managing asynchronous streams of events. Therefore the [SSE Framework](https://openid.net/specs/openid-sse-framework-1_0-01.html) is now proposed to be a standard for managing such streams of events for any application, not just CAEP and RISC. In effect, it is a standard for generalized Webhooks.
* [OpenID Connect Client-Initiated Backchannel Authentication (CIBA) Core is now a Final Specification](https://openid.net/2021/09/01/openid-connect-client-initiated-backchannel-authentication-ciba-core-is-now-a-final-specification/)

The OpenID Foundation membership has approved the following [MODRNA](https://openid.net/wg/mobile/) specification as an OpenID Final Specification:
* [Managed Open Projects: A New Way For Open Source and Open Standards To Collaborate](https://www.oasis-open.org/2021/09/08/managed-open-projects/)

I recently pointed out in a [TechCrunch contribution](https://techcrunch.com/2021/06/09/a-revival-at-the-intersection-of-open-source-and-open-standards/) that the open source and open standards communities need to find ways to team up if they are to continue driving innovation and  development of transformative technologies to push our society forward.
* [OpenID Connect Presentation at 2021 European Identity and Cloud (EIC) Conference](https://self-issued.info/?p%3D2187)

I gave the following presentation on the [OpenID Connect Working Group](https://openid.net/wg/connect/) during the [September 13, 2021 OpenID Workshop](https://openid.net/oidf-workshop-at-eic-2021-monday-september-13-2021/) at the [2021 European Identity and Cloud (EIC) conference](https://www.kuppingercole.com/events/eic2021/). As I noted during the talk, this is an exciting time for OpenID Connect; there’s more happening now than at any time since the original OpenID Connect specs were created!

- OpenID Connect Working Group [(PowerPoint)](http://self-issued.info/presentations/OpenID_Connect_Working_Group_13-Sep-21.pptx) [(PDF)](http://self-issued.info/presentations/OpenID_Connect_Working_Group_13-Sep-21.pdf)

* [Hyperledger Aries Graduates To Active Status](https://www.hyperledger.org/blog/2021/02/26/hyperledger-aries-graduates-to-active-status-joins-indy-as-production-ready-hyperledger-projects-for-decentralized-identity)

The TSC commended the Aries project during the meeting for the project’s highly diverse contributors. Achieving a high number of organizations contributing to a project at Hyperledger is often a challenge. Congratulations are due to those participating in and supporting the Aries Project.

* [JSON is Robot Barf](https://www.windley.com/archives/2021/09/json_is_robot_barf.shtml) Windley

JSON has its place. But I think we're overusing it in places where a good notation would serve us better.

* DIDComm: [ECDH-1PU Implementation](https://blog.identity.foundation/ecdh-1pu-implementation/) Identity Foundation

In short, ECDH-1PU is a key derivation process that allows for sender authenticity and enables a “[Perfect Forward Secrecy](https://www.wired.com/2016/11/what-is-perfect-forward-secrecy/%23:~:text%3DPerfect%2520forward%2520secrecy%2520means%2520that,of%2520the%2520user%27s%2520sensitive%2520data.)” mechanism, in addition to significant performance gains over JWS message nested in a JWE envelope, as used by existign ECDH-ES aproaches.

* [Q&A: The Potential of Decentralized ID in Travel](https://www.webintravel.com/qa-the-potential-of-decentralized-digital-id-in-travel/) WebInTravel

Since February he has also been the informal chair of the [Hospitality and Travel Special Interest Group](https://www.notion.so/dif/HOSPITALITY-TRAVEL-SIG-242105321e1747f8bce776bf634a55b3), a subset within the Decentralized Identity Foundation, an organization creating technical specifications and reference implementations for decentralized identity and working with industries for commercial applications of such technologies.

### OpenID trying to make play in the “trusted identities” online space

* [Global Assured Identity Network White Paper](https://openid.net/2021/09/20/global-assured-identity-network-white-paper/)
* [OIDC with SIOPv2 and DIF Presentation Exchange](https://vimeo.com/630104529) Sphereon

* [Sign in with Ethereum](https://login.xyz/) is being developed by Spruce

Already used throughout web3, this is an effort to standardize the method with best practices and to make it easier for web2 services to adopt it.

* [Decentralized Identity: Why Are DIDs The Future of Digital Identity Management?](https://elastos.info/decentralized-identity-dids/)

Why would you have 75 logins when you could have 1?

* [WAYF certificeret efter ISO 27001](https://www.wayf.dk/en/node/317)

WAYF has now been certified according to the standard for information security ISO 27001. This is the result of the audit that DNV conducted at WAYF on 23 September 2021. Language Danish Read more about WAYF certified according to ISO 27001

* [TrustBloc - Duty Free Shop use case (CHAPI Save + WACI Share)](https://www.youtube.com/watch?v%3DaagFJBI1fBE)

This video demonstrates the TrustBloc platform to Issue a W3C Verifiable Credential through CHAPI and Share the Verifiable Credential/Presentation through WACI.

* [How Yoma Uses Trinsic to Help African Youth Build Digital CVs](https://trinsic.id/customer-story-yoma/)

Verifiable credentials is a beautiful set of technology that allows people and organizations to get the data in a verifiable form that still respects agency.”

Lohan Spies, Technical Lead, Yoma

* [Gimly ID: SSI with OpenID authentication](https://www.loom.com/share/d49e005bb32349d7950022e83d55b944)

About Dick Hardt’s new thing

Gimly ID is leading self-sovereign identity innovation, with the implementation of SSI with self-issued openID provider (SIOPv2) and full support for openID connect and DIF presentation exchange.

* [Explore Affinidi Schema Manager](https://ui.schema.affinidi.com/schemas/)

* [Proof-of-possession (pop) AMR method added to OpenID Enhanced Authentication Profile spec](https://self-issued.info/?p%3D2198) Mike Jones

I’ve defined an Authentication Method Reference (AMR) value called “pop” to indicate that Proof-of-possession of a key was performed. Unlike the existing “hwk” (hardware key) and “swk” (software key) methods [...] Among other use cases, this AMR method is applicable whenever a [WebAuthn](https://www.w3.org/TR/2021/REC-webauthn-2-20210408/) or [FIDO](https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html) authenticator are used.

- [https://openid.net/specs/openid-connect-eap-acr-values-1_0-01.html](https://openid.net/specs/openid-connect-eap-acr-values-1_0-01.html)
- [https://openid.net/specs/openid-connect-eap-acr-values-1_0.html](https://openid.net/specs/openid-connect-eap-acr-values-1_0.html)

* [OpenID Connect Presentation at IIW XXXIII](https://self-issued.info/?p%3D2196) Mike Jones

- Introduction to OpenID Connect [(PowerPoint)](https://self-issued.info/presentations/OpenID_Connect_Introduction_12-Oct-21.pptx) [(PDF)](https://self-issued.info/presentations/OpenID_Connect_Introduction_12-Oct-21.pdf)

The session was well attended. There was a good discussion about the use of passwordless authentication with OpenID Connect.
* [SSI with OpenID authentication](https://www.loom.com/share/d49e005bb32349d7950022e83d55b944) Gimly ID

* [DIDs are not enough - we need an Authoriziation standard too](https://medium.com/energy-web-insights/api-access-security-for-dapps-cfcfa928623c) Energy Web

If you are a developer and want to write a DApp [...] you probably are using API-Keys in your front-end. If this is the case, then you should consider the security risk the publication of the API-Key in your front end represents and ask yourself if it would make sense to switch to a user authentication scheme.

* [A DIF & TOIP Joint Statement of Support for the Decentralized Identifiers (DIDS) V1.0 Specification Becoming A W3C Specification](https://trustoverip.org/blog/2021/10/29/a-dif-toip-joint-statement-of-support-for-the-decentralized-identifiers-dids-v1-0-specification-becoming-a-w3c-standard/).

DIDs are a critical part of a technical foundation for the products and activities of many of our members. Many of the implementations in the [DID Working Group’s implementation report](https://w3c.github.io/did-test-suite/%23report-by-methods) were developed by engineers and companies who collaborate openly at DIF on points of technical interoperability, and at ToIP on points of policy and governance.

* [Keep Badges Weird…](https://blog.weareopen.coop/keep-badges-weird-e26a1b055ff5) at the Badge Summit

We have a new suite of badges to encourage participation, create value for others, and reflect on that experience. Participants will be able to both earn AND award badges, so they’ll have a chance to prove that they’ve understood the theory surrounding CoPs and badges as well as put those theories into practice.
* [Mission Accomplished: Universal Resolver Calls coming to an end](https://blog.identity.foundation/universal-resolver-calls-wrapup/) Identity Foundation

Considering that the group has accomplished these goals, there is currently no more need for dedicated calls. Work on the Universal Resolver work item will continue on Github (under the [Universal Resolver](https://github.com/decentralized-identity/universal-resolver) and [Identifiers &Discovery](https://github.com/decentralized-identity/identifiers-discovery/) and on DIF Slack in the Identifiers & Discovery Working Group channel, #wg-id.

* [First Official Me2B Alliance Recommendation](https://me2ba.org/first-official-me2b-alliance-recommendation/)

In a sense, this recommendation is a kind of abbreviation of the key things that our specifications test for. And you’ll be able to see that soon as the Me2B Safe Website Specification for Respectful Technology is currently in the membership review stage of the approval process.

* [The Pathway to Becoming a Hyperledger Maintainer](https://www.hyperledger.org/blog/2021/11/03/the-pathway-to-becoming-a-hyperledger-maintainer)

In this blogpost I’m going to share what it’s like to be a maintainer for the Hyperledger Aries project. You’ll learn how you can start contributing and maybe even set yourself on a path to becoming a maintainer.

* [Indicio’s support for the W3C DID Specification and its path to standardization](https://indicio.tech/indicios-support-for-the-w3c-did-specification-and-its-path-to-standardization/)

The position of Indicio is that the DID Specification is of signal importance to creating a better digital world. We recognize that, as with any specification, improvements can and will be made in the future; but we back its recommendations and its approval.

* [Discover Open Badges 3.0!](https://app.participate.com/communities/keep-badges-weird/62003f3f-a7ba-4f6a-990a-64d6f893016d/announcements/0bc15852-0f91-48c8-a7ca-478b246b553c) Keep Badges Weird

1. Check out the (accepted) [Open Badges 3.0 proposal](https://github.com/IMSGlobal/openbadges-specification/files/6977048/Proposal-Open-Badges-3.0-update-08-11-2021.pdf)​
2. ​[Watch a video](https://www.youtube.com/watch?v%3DQDGPwR1F3FY%26t%3D1357s) from the ePIC conference giving an overview of what Open Badges 3.0 will enable (or view the [slide deck](https://docs.google.com/presentation/d/1NEJoQaI9b6KC1EFDDhR3MGybGVoa0R3bQh0xuKtUKkY)
3. Discuss what this means for you, your organisation, or your community in [this thread](https://app.participate.com/discussions/open-badges-3-0/68917656-db8f-4932-88fd-153fdb54e285)​

* [Link your domain to your Decentralized Identifier (DID) (preview)](https://docs.microsoft.com/en-us/azure/active-directory/verifiable-credentials/how-to-dnsbind)

We make a link between a domain and a DID by implementing an open standard written by the Decentralized Identity Foundation called [Well-Known DID configuration](https://identity.foundation/.well-known/resources/did-configuration/). The verifiable credentials service in Azure Active Directory (Azure AD) helps your organization make the link between the DID and domain by including the domain information that you provided in your DID, and generating the well-known config file:

* [Reflecting on the Evolving Badges and Credentials Ecosystem](https://blog.weareopen.coop/reflecting-on-the-evolving-badges-and-credentials-ecosystem-6efac4d673d3)

Recently, the WAO team took the opportunity to update the badge platforms page on Badge Wiki, a knowledgebase for the Open Badge community. As the ecosystem continues to evolve we’re seeing some early platforms fall by the wayside and new platforms emerge.

* [The Perfect Signature Style is the Enemy of the One that Works Today](https://indicio.tech/the-perfect-signature-style-is-the-enemy-of-the-one-that-works-today/) Indicio

BBS+ signature styles are not going to be ready for deployment anytime soon. This is precisely why you should build today and in a way that allows you to add them later.

* [DIDComm Mythconceptions](https://www.youtube.com/watch?v%3DrwvQdRyMeY4) Daniel Hardman

DIDComm is a peer-to-peer communication technology for SSI (self-sovereign identity) with security and privacy properties rooted in DIDs (decentralized identifiers). Its core value proposition is often misunderstood or oversimplified. This webinar provides a proper mental model.
* [First Public Review Period for OpenID Connect SIOPV2 and OIDC4VP Specifications Started](https://openid.net/2021/12/17/first-public-review-period-for-openid-connect-siopv2-and-oidc4vp-specifications-started/) OpenID

- Implementer’s Drafts public review period: Friday, December 17, 2021 to Monday, January 31, 2022 (45 days)
- Implementer’s Drafts vote announcement: Tuesday, January 18, 2022
- Implementer’s Drafts voting period: Tuesday, February 1, 2022 to Tuesday, February 8, 2022 *

* [Report from EBSI4Austria. In 2018, all European member states…](https://medium.com/@markus.sabadello/report-from-ebsi4austria-b79c0ed8ab8d) Markus Sabadello

EBSI4Austria is a CEF funded project with two main objectives. First, EBSI4Austria aims to set up, operate and maintain the Austrian’s EBSI node. Second, we pilot the diploma use case on the Austrian level supported by two Universities and data providers as well as verifiers.

* [Blockcerts V3 release](https://community.blockcerts.org/t/blockcerts-v3-release/3022)

The main change is the alignment with the [W3C Verifiable Credentials specification 3](https://www.w3.org/TR/vc-data-model/).

Regarding the standard itself metadata and display are entering the default standard. metadata comes in replacement of metadataJson and remains a stringified JSON that will allow consumers to register specific data which are too unique for issuances to be defined in the context.

display brings in [a little bit of novelty 2](https://github.com/blockchain-certificates/cert-schema/blob/master/cert_schema/3.0/displaySchema.json%23L6) images or pdfs, in addition to the more classic HTML.

* [DIDComm Messaging through libp2p](https://medium.com/uport/didcomm-messaging-through-libp2p-cffe0f06a062) Oliver Terbu

We outlined the next generation decentralized messaging solution built on top of [DIDComm Messaging](https://identity.foundation/didcomm-messaging/spec/), [DIDs](https://www.w3.org/TR/did-core/) and [VCs](https://www.w3.org/TR/vc-data-model/) and a [libp2p](https://libp2p.io/) overlay network. We presented how Alice and Bob establish a connection, exchange messages and demonstrated what connection types are supported.
* [Self-Sovereign Identity (SSI) and Verifiable Credentials (VC) in Ocean Protocol](https://port.oceanprotocol.com/t/proposal-walt-id-bringing-self-sovereign-identity-ssi-and-verifiable-credentials-vc-to-ocean-protocol-proof-of-concept/976)

What already exists, more recently: [fine-grained permissions 1](https://blog.oceanprotocol.com/fine-grained-permissions-now-supported-in-ocean-protocol-4fe434af24b9):

1. Marketplace-level fine-grained permissions for browsing, publishing, etc within a marketplace frontend
2. Asset-level fine-grained permissions on consuming the asset itself

* [ENS names are Decentralized Identifiers (DIDs)](https://medium.com/uport/ens-names-are-decentralized-identifiers-dids-724f0c317e4b) uPort

- did:ens:mainnet:vitalik.eth

This has two purposes:

1. to wrap existing ENS names as DIDs to facilitate interoperability of emerging technologies in the Decentralized Identity and Ethereum community,
2. to define a canonical way to augment ENS names with DID capabilities (e.g., encryption) as mentioned above.

* [Community Resources - DID Primer](https://w3c-ccg.github.io/did-primer/) Credentials Community Group

At a superficial level, a decentralized identifier (DID) is simply a new type of globally unique identifier. But at a deeper level, DIDs are the core component of an entirely new layer of decentralized digital identity and public key infrastructure (PKI) for the Internet. This [decentralized public key infrastructure](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/dpki.pdf) (DPKI) could have as much impact on global cybersecurity and cyberprivacy as the development of the [SSL/TLS protocol](https://en.wikipedia.org/wiki/Transport_Layer_Security) for encrypted Web traffic (now the largest PKI in the world).

* [​​First Implementer’s Drafts of OpenID Connect SIOPV2 and OIDC4VP Specifications Approved](https://openid.net/2022/02/08/first-implementers-drafts-of-openid-connect-siopv2-and-oidc4vp-specifications-approved/) OpenID

- [Self-Issued OpenID Provider v2](https://openid.net/specs/openid-connect-self-issued-v2-1_0-07.html)
- [OpenID Connect for Verifiable Presentations](https://openid.net/specs/openid-connect-4-verifiable-presentations-1_0-08.html)

* [Indicio Wins British Columbia Code With Us Challenge to Upgrade Hyperledger Indy](https://indicio.tech/indicio-wins-british-columbia-code-with-us-challenge-to-upgrade-hyperledger-indy/)

Most of Hyperledger Indy’s development occurred prior to the completion of the standard DID Specification by the W3C and, as a result, identifiers written to one network are currently not resolvable on other networks. A new did:indy DID Method will fix that and make it easier for decentralized identity products and services to interoperate across different Indy networks.

* [Cryptography Review of W3C VC Data Model and DID Standards and Implementation Recommendations](https://www.linkedin.com/posts/aniljohn_cryptography-review-of-w3c-vc-and-w3c-did-ugcPost-6892250585652162560-OQ3Y) SRI International

* [Vote for First Implementer’s Drafts of OIDConnect SIOPV2 and OIDC4VP Specifications](https://openid.net/2022/01/18/notice-of-vote-for-first-implementers-drafts-of-openid-connect-siopv2-and-oidc4vp-specifications/) OpenID

The official voting period will be between Tuesday, February 1, 2022 and Tuesday, February 8, 2022, following the [45-day review](https://openid.net/2021/12/17/first-public-review-period-for-openid-connect-siopv2-and-oidc4vp-specifications-started/) of the specifications.


* [NFTs, Verifiable Credentials, and Picos](https://www.windley.com/archives/2021/10/nfts_verifiable_credentials_and_picos.shtml) Phil Windley

Summary: The hype over NFTs and collectibles is blinding us to their true usefulness as trustworthy persistent data objects. How do they sit in the landscape with verifiable credentials and picos? Listening to this Reality 2.0 podcast about NFTs with Doc Searls, Katherine Druckman, and their guest Greg Bledsoe got me thinking about NFTs.

* [Nat describes GAIN](https://nat.sakimura.org/2021/09/14/announcing-gain/) as an overlay network on top of the Internet with all its participants identity proofed. One key benefit of the approach proposed in the white paper is that the standards required to enable this network already exist: OpenID Connect and eKYC/IDA.

- [Nat has a presentation](https://nat.sakimura.org/2021/09/14/announcing-gain/)
- There is a [linked in Group](https://www.linkedin.com/groups/12559000/)

* [Adding DID ION to MATTR VII](https://medium.com/mattr-global/adding-did-ion-to-mattr-vii-d56bdb7a2fde)

Different types of DIDs can be registered and anchored using unique rules specific to the set of infrastructure where they’re stored. Since DIDs provide provenance for keys which are controlled by DID owners, the rules and systems that govern each kind of DID method have a significant impact on the trust and maintenance model for these identifiers.

- [OpenID Connect Client-Initiated Backchannel Authentication Flow – Core 1.0](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html)

A Final Specification provides intellectual property protections to implementers of the specification and is not subject to further revision.
* [VC Spec Enhancement Proposal](https://github.com/SmithSamuelM/Papers/blob/master/whitepapers/VC_Enhancement_Strategy.md) Sam Smith

the VC standard appears to be an adoption vector for Linked Data, not the other way around. My overriding interest is that the concept of a VC as a securely attributable statement is a very powerful and attractive one and therefore should be widely adopted. We should therefore be picking the best technologies that best support broad VC adoption, not the other way around.

* [Hyperledger SSI Ecosystem](https://dev.to/jakubkoci/hyperledger-ssi-ecosystem-4j2p) Jakubkoci

There are three projects under the Hyperledger umbrella related to digital identity. Hyperledger Indy, Aries, and Ursa. [...] describe their purpose and how they’re related to each other.

* [Open standards should be developed openly](https://blog.weareopen.coop/open-standards-should-be-developed-openly-1f0cf552308d)

Open standards should be developed openly because not enough people work to ensure that equity is central to innovation and development. We believe that openness is an attitude, and one which bears fruit over time from which everyone can benefit.

* [Use Case Implementation Workstream](https://covidcreds.groups.io/g/usecaseCCI) [usecaseCCI@covidcreds.groups.io](mailto:usecaseCCI@covidcreds.groups.io)

This is the Use Case Implementation Workstream of the [COVID Credentials Initiative (CCI)](https://www.covidcreds.com/). This workstream identifies privacy-preserving verifiable credentials (VCs) that are most useful to the COVID-19 response and provides a forum and platform for those who are implementing COVID VCs to present their projects/solutions.

* [@kimdhamilton](https://twitter.com/kimdhamilton) · [May 25](https://twitter.com/kimdhamilton/status/1397241823190523904)

I've read every decentralized identity protocol so you don't have to. They all just read like "nothing to see here, just f- right off" Oh, except for OIDC Credential Provider. Well done to them!

* [Hygiene for a computing pandemic](https://fossandcrafts.org/episodes/20-hygiene-for-a-computing-pandemic.html)

This episode of FOSS and Crafts features Christopher Lemmer Webber discussing the object capability security approach. Its a generalization not specific to VCs, continuing from the conversation on the CCG mailinglist, [Hygiene for a computing pandemic: separation of VCs and ocaps/zcaps](https://lists.w3.org/Archives/Public/public-credentials/2020Dec/0028.html), we shared last month.

The podcast *show-notes include an epic list of references* supporting the discussion.

* [@csuwildcat](https://twitter.com/csuwildcat) shares
  > As of Friday, we believe v1 of ION is functionally code complete, and the Sidetree Working Group at DIF (@DecentralizedID) should have a v1 spec candidate ready for the underlying protocol by Jan 21st. Public v1 launch of the ION network on Bitcoin mainnet is just weeks away.
* [CCG Call about ZCaps and OCaps](https://w3c-ccg.github.io/meetings/2021-01-13/audio.ogg) ([minutes](https://w3c-ccg.github.io/meetings/2021-01-13/))

This week’s CCG teleconference had a great discussion about object capabilities

> Alan Karp:  I've been doing capabilities since I reinvented them in 1996 and I want to make sure we get it right, because when newbies start to use them there are plenty of mistakes that can be made
> 
> [...]
> A capability or an OCAP is an unforgeable, transferable, permission to use the thing it designates ... it combines designation with authorization

* [What Is ISO 27018:2019? Everything Executives Need to Know](https://auth0.com/blog/what-is-iso-27018-2019-everything-executives-need-to-know/)
  > ISO 27018 is part of the ISO 27000 family of standards, which define best practices for information security management. ISO 27018 adds new guidelines, enhancements, and security controls to the ISO/IEC 27001 and ISO/IEC 27002 standards, which help cloud service providers better manage the data security risks unique to PII in cloud computing.
* [Differences between SAML, OAuth & OIDC (OpenID Connect)](https://www.ubisecure.com/education/differences-between-saml-oauth-openid-connect/)
  > SAML 2.0 - Security Assertion Markup Language
> 
> OAuth 2.0 - Web Authorization Protocol
> OpenID Connect 1.0 (OIDC) - Simple identity layer on top of OAuth 2.0
* [What's New in Passwordless Standards, 2021 edition!](https://techcommunity.microsoft.com/t5/identity-standards-blog/what-s-new-in-passwordless-standards-2021-edition/ba-p/2124136) (Microsoft)
  > The Web Authentication API (WebAuthn) Level 2 specification is currently a Candidate Recommendation at the W3C. "Level 2" essentially means major version number 2.
> 
> The version 2.1 of the[Client to Authenticator Protocol (CTAP)](https://fidoalliance.org/specs/fido-v2.1-rd-20201208/fido-client-to-authenticator-protocol-v2.1-rd-20201208.html) specification is a Release Draft at the FIDO Alliance. This means the spec is in a public review period before final publication.
> We think you might want to hear about what we think is especially fun about WebAuthn L2 and CTAP 2.1.

* [What Is ISO 27001:2013? A Guide for Businesses](https://auth0.com/blog/what-is-iso-27001-2013-a-guide-for-businesses/)
  > ISO 27001 is also the cornerstone of a growing international consensus about data security best practices. Australia based its federal Digital Security Policy on ISO 27001. Likewise, ISO 27001 can provide guidance on how to meet the standards of other data privacy laws, such as the GDPR, which often direct companies to it as an example of universal best practices. So if you abide by ISO 27001’s recommendations, you’re on the right track for legal compliance, not to mention improved data security.

### Data Privacy Vocab

* [OPN-R (Open Public Notice - Rights) - starting Notice & Control Language - for people to use rights and govern identity (govinterop) with @ Kantara, ToiP and W3C Data Privacy Vocabulary using international vocab - from ISO/IEC 29100 Legal Framework Vocabulary](https://iiw.idcommons.net/22F/_OPN-R_-_Open_Public_Notice_-_Rights_-_starting_Notice_and_Control_Language) by Mark Lizar

The language consists of

- International standard vocabulary for security and privacy frameworks provides roles and actors to govern the transfer of personal data.
- The active state notice and consent receipt - is a format for generating consent records from notice/policy - which provides people with information to use rights. .
- W3C Data Privacy Control Vocabulary and ISO/IEC 29100, Legal Framework Vocabulary

This language can be used to auto generate receipts to process rights and negotiate terms ..  At Kantara we are working to use the standards to auto read the notices/polices to provide a conformance / trust assessment for people so they can see risk independently of the service provider

We discussed these projects and have some links

For more info

Goto Kantara ANCR WG [https://kantarainitiative.org/confluence/pages/viewpage.action?pageId=140804260](https://kantarainitiative.org/confluence/pages/viewpage.action?pageId%3D140804260)

W3C DPV CG - [https://dpvcg.github.io/dpv/](https://dpvcg.github.io/dpv/)

ToiP -  ISWG - Notice & Consent Task force for a Privacy Controller Credential

* [https://wiki.trustoverip.org/pages/resumedraft.action?draftId=72226&draftShareId=8b665919-3b23-4a4d-be90-26947c7ae82c&](https://wiki.trustoverip.org/pages/resumedraft.action?draftId%3D72226%26draftShareId%3D8b665919-3b23-4a4d-be90-26947c7ae82c%26)

ToiP Privacy Risk -

Data Privacy Impact Assessments

- Breaking down -
- 

Kantara - ANCR -

Showing off the work and topics

- Privacy as Expected - a gateway to online consent
- 2 Factor Consent (2FC)

* [https://kantarainitiative.org/confluence/collector/pages.action?key=WA&src=sidebar-pages](https://kantarainitiative.org/confluence/collector/pages.action?key%3DWA%26src%3Dsidebar-pages)

W3C Data Privacy Vocabulary Control

* [https://dpvcg.github.io/dpv/#Representative](https://dpvcg.github.io/dpv/%23Representative)

* [Mobile Agent Development FAQ](https://iiw.idcommons.net/1L/_Mobile_Agent_Development_FAQ) by Horacio Nunez

This session had the objective to gather (and discuss) a set of recurrent questions people experience when trying to build their first mobile agents.

This was the end result of the session:

FAQ

What’s the best place to start creating your own mobile agent?

How do you get updates once you ship your first version?

Do I actually have to support a fork for every mobile agent I create?

Do I need to use a Mediator?

* [Better and more secure methods for API authentication](https://iiw.idcommons.net/1D/_Better_and_more_secure_methods_for_API_authentication) by Michael Lodder

Presentation slides: [https://docs.google.com/presentation/d/1UO25DzVmq25ya2S4_tV5UKTSP6NtBggln9vP1TEXSzE/edit](https://docs.google.com/presentation/d/1UO25DzVmq25ya2S4_tV5UKTSP6NtBggln9vP1TEXSzE/edit)

Goal of the Oberon protocol when building an API:

- Super effective: no separate session token to required for accessing the API; very fast to issue and verify tokens; 128 bytes required per message
- Privacy preserving
- No new crypto, uses BLS signature keys and Pointecheval saunders Construction

* [Trusted Timestamping Part 3: Family of Standards](https://medium.com/finema/trusted-timestamping-part-3-family-of-standards-f0c89a5e97ab) Nunnaphat Songmanee Finema

Read more about timestamping and its concepts at [Trusted Timestamping Part 1: Scenarios](https://medium.com/finema/trusted-timestamping-part-1-scenarios-9bf4a7cc2364) and [Trusted Timestamping Part 2: Process and Safeguards](https://medium.com/finema/trusted-timestamping-part-2-process-and-safeguards-f75286a0c370).

Family of standards related to timestamping


* [Global Standards Mapping Initiative](https://www.continuumloop.com/global-standards-mapping-initiative/) ContinuumLoop

This past November, the GBBC released [The Global Standards Mapping Initiative 2.0](https://gbbcouncil.org/wp-content/uploads/2021/11/GBBC-GSMI-2.0-Report-1.pdf), updating the [standards published in 2020](https://gbbcouncil.org/wp-content/uploads/2020/10/GSMI-Legal-Regulatory-Report.pdf). The GBBC is a strong proponent of standardization and intends to serve as a baseline for establishing frameworks and standards that will allow for adoption and innovation.

* [Verifiable Presentation Personas: Certifiers, Consolidators, & Submitters](https://medium.com/@Transmute/verifiable-presentation-personas-certifiers-consolidators-submitters-b38a281eb92f) Transmute

The arrow for “Issue Credentials” is exactly the same as “Send Presentation,” leading us to believe these activities are similar, but how are they similar? We can’t adequately answer these questions by looking at the above picture and the specification doesn’t provide a ton of help either…

WG Meeting of the week

* [OpenID for Verifiable Credentials](https://openid.net/2022/05/12/openid-for-verifiable-credentials-whitepaper/) OpenID ([Whitepaper](https://openid.net/wordpress-content/uploads/2022/05/OIDF-Whitepaper_OpenID-for-Verifiable-Credentials_FINAL_2022-05-12.pdf)

to inform and educate the readers about the work on the OpenID for Verifiable Credentials (OpenID4VC) specifications family. It addresses use-cases referred to as Self-Sovereign Identity, Decentralized Identity, or User-Centric Identity.

* [Indicio completes Hyperledger Indy DID Method—A Milestone in the Evolution of DID Interop](https://indicio.tech/indicio-completes-hyperledger-indy-did-method-a-milestone-in-the-evolution-of-decentralized-identity-network-interoperability/)

The Indy DID Method paves the way for Hyperledger Indy credentials to scale globally by allowing Indy networks to seamlessly interoperate and create a “network-of-networks” effect.

* [What is Open Recognition, anyway?](https://blog.weareopen.coop/what-is-open-recognition-anyway-9f38ec1f8629) Going beyond credentialing and the formal/informal divide

Badges as credentials includes approaches that are well understood and largely replace or augment existing certification practices. Badges for recognition, however, include approaches that remain somewhat confusing to many people.

BlueSky

* [dSocialCommons Hosts Twitter Spaces | Interoperable Formats](https://twitter.com/dsocialcommons/status/1519724178256982017)

Bluesky Community Voices #6: Interoperable Formats [https://twitter.com/i/spaces/1vAxRkVrMPzKl](https://twitter.com/i/spaces/1vAxRkVrMPzKl) Moderator [@kimdhamilton](https://twitter.com/kimdhamilton) Speakers [@kevinmarks](https://twitter.com/kevinmarks) [@mfosterio](https://twitter.com/mfosterio) [@JoeAndrieu](https://twitter.com/JoeAndrieu) [@harlantwood](https://twitter.com/harlantwood)

* [Working in Public](https://blueskyweb.xyz/blog/5-4-2022-working-in-public) BlueSky

Today we’re releasing [ADX, the “Authenticated Data Experiment”](https://github.com/bluesky-social/adx). Our company's name, “bluesky,” describes the open-ended nature of this project, and the freedom we were given to start from first principles. As we get more concrete, we’ll give more specific names to what we’re building, starting with ADX.
* [FLOSS WEEKLY 685: DIDS AND DIDCOMM](https://twit.tv/shows/floss-weekly/episodes/685) Featuring Sam Curren

Sam Curren unpacks for Doc Searls and Dan Lynch why DIDs and DIDcomm are the best approach to identity—and to making people first-class citizens on the Internet. Curren also discusses the origin story of picos and the advantages of nomadic living and hacking.

## DID Core advances to recommendation

* [Objections overruled by W3C director approving the DIDCore specification as a W3C Recommendation](https://www.w3.org/2022/06/DIDRecommendationDecision.html) W3C

The DID core specification is approved to advance to W3C Recommendation.

In its next chartered period the Working Group should address and deliver proposed standard DID method(s) and demonstrate interoperable implementations.  The community and Member review of such proposed methods is the natural place to evaluate the questions raised by the objectors and other Member reviewers regarding decentralization, fitness for purpose, and sustainable resource utilization. -Ralph Swick, for Tim Berners-Lee

* [Decentralized Identifiers (DID) 1.0 specification approved as W3C Recommendation](https://blog.identity.foundation/w3cdidspec-2/) Identity Foundatoin

Announcing the [Decentralized Identifiers (DID) v1.0 specification](https://www.w3.org/TR/did-core/) as an open web standard signals that it is technically sound, mature, and ready for widespread adoption. Having an established v1.0 specification allows work to continue with renewed energy and focus, not only at the many groups meeting at DIF, but across the digital identity community.

Harrison Tang, CEO of Spokeo, [is the new co-chair of the CCG](https://twitter.com/TheCEODad/status/1544884282316845057)

W3C CCG (World Wide Web Consortium’s Credentials Community Group) aims to explore the creation, storage, presentation, verification, and user control of credentials (i.e. a set of claims made about someone, or a person record).

* [Steering Committee approved the DIDComm Messaging Spec (DIDComm v2)](https://twitter.com/IndicioID/status/1545208982863691777) @IndicioID

* [DIDComm Messaging](https://identity.foundation/didcomm-messaging/spec/)

DIDComm Messaging enables higher-order protocols that inherit its security, privacy, decentralization, and transport independence. Examples include exchanging verifiable credentials, creating and maintaining relationships, buying and selling, scheduling events, negotiating contracts, voting, presenting tickets for travel, applying to employers or schools or banks, arranging healthcare, and playing games.

* [Our Approach to Resources on-ledger](https://blog.cheqd.io/our-approach-to-resources-on-ledger-25bf5690c975): Using the capabilities of the DID Core specification for standards-compliant resource lookup

Decentralised Identifiers (DIDs): are often stored on ledgers (e.g., [cheqd](https://github.com/cheqd/node-docs/blob/adr-008-resources-updates/architecture/adr-list/adr-002-cheqd-did-method.md), [Hyperledger Indy](https://hyperledger.github.io/indy-did-method/), distributed storage (e.g., [IPFS](https://ipfs.io/) in [Sidetree](https://identity.foundation/sidetree/spec/)), or non-ledger distributed systems (e.g., [KERI](https://keri.one/)). Yet, DIDs can be stored on traditional centralised-storage endpoints (e.g., [did:web](https://w3c-ccg.github.io/did-method-web/), [did:git](https://github-did.com/)).

Neighboring Standards

* [Secure QR Code Authentication v1.0 from ESAT TC approved as a Committee Specification](https://www.oasis-open.org/2022/07/12/secure-qr-code-authentication-v1-0-from-esat-tc-approved-as-a-committee-specification/)

An alternative to passwords that includes QR Codes is described, and typical use cases are described. This document also provides an overview and context for using QR Codes for security purposes.

* [The Most Inventive Thing I've Done](https://www.windley.com/archives/2022/07/the_most_inventive_thing_ive_done.shtml) Phil Windley

every pico is serverless and cloud-native, presenting an API that can be fully customized by developers. Because they're persistent, picos support databaseless programming with intuitive data isolation. As an actor-model programming system, different picos can operate concurrently without the need for locks, making them a natural choice for easily building decentralized systems.
W3C Press Release - [Decentralized Identifiers (DIDs) v1.0 becomes a W3C Recommendation](https://www.w3.org/2022/07/pressrelease-did-rec) worth reading to see who contributed comments (and notice who didn’t)

For individuals in particular, DIDs can put them back in control of their personal data and consent, and also enable more respectful bi-directional trust relationships where forgery is prevented, privacy is honored, and usability is enhanced.

* [W3C launches Decentralized Identifiers as a web standard](https://portswigger.net/daily-swig/w3c-launches-decentralized-identifiers-as-a-web-standard) in the Daily Swig: Cybersecurity news and views.

“I would summarize the overall impact of DIDs on cybersecurity as making digital signing and [encryption](https://portswigger.net/daily-swig/encryption) much more widely available than today’s conventional X.509-based public key infrastructure (PKI),” Drummond Reed, director of trust services at Avast

* [W3C overrules objections by Google, Mozilla to decentralized identifier spec](https://www.theregister.com/2022/07/01/w3c_overrules_objections/) Oh no, he DIDn't in the Register

The [DID specification](https://www.w3.org/TR/did-core/%23introduction) describes a way to deploy a globally unique identifier without a centralized authority (eg, Apple [for Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) as a verifying entity.

* [DIF Monthly #28](https://blog.identity.foundation/dif-monthly-28/)

Table of contents: 1. [Foundation News](https://blog.identity.foundation/dif-monthly-28/%23foundation); 2. [Group Updates](https://blog.identity.foundation/dif-monthly-28/%23groups); 3. [Member Updates](https://blog.identity.foundation/dif-monthly-28/%23members); 4. [Digital Identity Community](https://blog.identity.foundation/dif-monthly-28/%23Community); .5. [Funding](https://blog.identity.foundation/dif-monthly-28/%23funding); 6. [Events](https://blog.identity.foundation/dif-monthly-28/%23community); 7. [Hackathons](https://blog.identity.foundation/dif-monthly-28/%23hackathons); 8. [Jobs](https://blog.identity.foundation/dif-monthly-28/%23jobs); 9. [Metrics](https://blog.identity.foundation/dif-monthly-28/%23metrics); 10. [Get involved! Join DIF](https://blog.identity.foundation/dif-monthly-28/%23join)

* [Verification Patterns, Part 1](https://docs.centre.io/blog/verification-patterns-1) Verite

Since verification is off-chain (and generally fast/inexpensive, depending on the provider), and since this avoids on-chain storage of potentially correlatable data, this is often the preferred solution.

* [Verification Patterns, Part 2](https://docs.centre.io/blog/verification-patterns-2) Verite

Part 2 of this 2-part series explains the [did:pkh](https://github.com/w3c-ccg/did-pkh/blob/main/did-pkh-method-draft.md)/[CACAO](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-74.md%23simple-summary) variation for Verite data models and flows, which provides an entry path for wallets that may not support sufficient functionality for emerging decentralized identity patterns

* [DIDComm v2 reaches approved spec status!](https://blog.identity.foundation/didcomm-v2/) DIF Blog

DIDComm defines how messages are composed into application-level protocols and workflows.

* [Advanced DIDComm Messaging](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/advanced-didcomm-messaging.md) By: Karim Stekelenburg (Animo Solutions) -- karim@animo.id Date: 18-07-2022 Version: 0.1

in order for DIDComm to provide a potential replacement for commonly used chat protocols like WhatsApp (Extensible Messaging and Presence Protocol (XMPP)), Telegram (MTProto), or Signal (Signal Protocol), it needs to support modern chat features we use everyday

* [Decentralized Identifiers: Implications for Your Data, Payments and Communications](https://newsletter.impervious.ai/decentralized-identifiers-implications-for-your-data-payments-and-communications-2/) Impervious

Through the DID Specification, service endpoints and DIDComm, Impervious has interlaced DIDs with Bitcoin Lightning, IPFS, WebRTC and resilient relays to introduce a new peer-to-peer internet standard with practical applications for mitigating censorship and surveillance risk.

* [[SCITT] Endor: A SCITT PoC for W3C Verifiable Credentials](https://mailarchive.ietf.org/arch/msg/scitt/WSyUQuYimFowl6plzi_TIJzjBpM/)

I made this today: [https://github.com/OR13/endor](https://github.com/OR13/endor) [...]

nice thing about endorsing W3C Verifiable Credentials is that they are

already an abstraction that applies to "non software supply chain" use

Cases [...] we model [cyber physical supply chain flows](https://w3id.org/traceability)

^^^ [inspired by](https://twitter.com/OR13b/status/1553488644224204800) : [IETF 114: Plenary](https://www.ietf.org/live/ietf114-plenary/) (video)

* [GLEIF vLEI Verifiable Credentials containing trusted organization identity and roles](https://rapidlei.com/vlei/)

vLEI will provide a cryptographically secure chain of trust that will replace manual processes needed to access and confirm an entity’s identity across all industries.

* [Verifiable Health Data: Demonstrating Verifiable Credentials using Cardea](https://www.youtube.com/watch?v%3DruhnyMTqNog)

members from across the community come together to test interoperability between systems, networks, agents and more.


* [JSON Web Proofs BoF at IETF 114 in Philadelphia](https://self-issued.info/?p%3D2286)

- [Chair Slides](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-json-web-proofs-chair-drafts-00) – [Karen O’Donoghue](https://twitter.com/kodonog) and [John Bradley](https://twitter.com/ve7jtb)
- [The need: Standards for selective disclosure and zero-knowledge proofs](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-the-need-standards-for-selective-disclosure-and-zero-knowledge-proofs-00) – [Mike Jones](https://twitter.com/selfissued)
- [What Would JOSE Do? Why re-form the JOSE working group to meet the need?](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-the-need-standards-for-selective-disclosure-and-zero-knowledge-proofs-00) – [Mike Jones](https://twitter.com/selfissued)
- [The selective disclosure industry landscape, including Verifiable Credentials and ISO Mobile Driver Licenses (mDL)](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-why-selective-disclosure-00) – [Kristina Yasuda](https://twitter.com/kristinayasuda)
- [A Look Under the Covers: The JSON Web Proofs specifications](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-json-web-proofs-initial-drafts-00) – Jeremie Miller
- [Beyond JWS: BBS as a new algorithm with advanced capabilities utilizing JWP](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-beyond-jws-bbs-00) – [Tobias Looker](https://twitter.com/tplooker)

* [Aries Agent Test Harness Enhancement Project](https://www.idlab.org/en/aries-agent-test-harness-enhancement-project/) IDLab

At this stage of the AATH Enhancement Project, two factors helped define its broad content:

- The gap between AIP 2.0 constituent RFCs and the current implementation of the AATH tests
- Requirements from Interac with respect to AIP 2.0


* [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/)

- The components that constitute a [verifiable credential](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-credentials)
- The components that constitute a [verifiable presentation](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-presentations)
- An ecosystem where [verifiable credentials](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-credentials) and [verifiable presentations](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-presentations) are expected to be useful
- The use cases and requirements that informed this specification.

* [Volleyball, Identiverse, and Open Identity Standards](https://www.linkedin.com/pulse/volleyball-identiverse-open-identity-standards-alex-simons/?trackingId%3DiAokBqe0Qdqrwj5LfAEf3w%253D%253D) Alex Simons

* [Crossword wins NGI Atlantic funds for Verifiable Credentials project](https://www.crosswordcybersecurity.com/post/next-generation-internet-grant-win) Crossword Cybersecurity

European Commission’s Next Generation Internet (NGI) initiative to lead a project to test the OpenID Foundation’s protocols for transferring verifiable credentials. Crossword’s partners in this project are Spruce Inc from the USA and Fraunhofer from Germany

* [DIDComm & DIDComm Messaging](https://medium.com/datev-techblog/didcomm-didcomm-messaging-3e10fbf12bb8) Tim Vorgs, DATEV eG

* [Trinsic Builds Open Source Trust Registry Sponsored by eSSIF-Lab](https://trinsic.id/trinsic-builds-open-source-trust-registry-sponsored-by-essif-lab/) Trinsic

Driven by our motivation to make SSI more adoptable, we built the world’s first turn-key, open source trust registry solution. This work was sponsored by the [European Self-Sovereign Identity Framework Lab](https://essif-lab.eu/), which is an EU consortium that provides funding for projects that build SSI open source tools. Any ecosystem provider can use the trust registry implementation to enable governance in their verifiable data ecosystem.


* [Investing in Verifiable Credentials, Technical Interoperability and Open Source](https://www.hyperledger.org/blog/2022/08/23/investing-in-verifiable-credentials-technical-interoperability-and-open-source) Hyperledger

As our approach evolves, we also remain keen to support open source solutions that interoperate with other national and international efforts. There is no dominant design yet, no one network or technology, so we must remain nimble and flexible in our exploration. We also need to coexist with existing identity solutions that millions of British Columbians already rely upon.

* [Managing Trust and Reputation via Trust Registries](https://www.continuumloop.com/managing-trust-and-reputation-via-trust-registries/) Continuum Loop

The concept behind a Trust Registry is that a Wallet needs to know which decentralized identifiers (DIDs) to “trust” as a source of truth. At many levels, this “trust” translates to “authority” – knowing that somebody, centralized or decentralized, is responsible for maintaining a list of trusted DIDs.

* [Dock DIDs Now Support Multiple Key Pairs](https://blog.dock.io/dids-multikey-support/) Dock

- Keys can be given different capabilities using Verification Relationships
- We support 4 Verification Relationships: Authentication, Assertion, Key Agreement, and Capability Invocation.
- DIDs can now be controlled by other DIDs
- DIDs can now have service endpoints
- Dock now supports off-chain DID Documents

* [ONDC: An Open Network for Ecommerce](https://www.windley.com/archives/2022/08/ondc_an_open_network_for_ecommerce.shtml) Phil Windley

* [Open Network for Digital Commerce](https://en.wikipedia.org/wiki/Open_Network_for_Digital_Commerce) is a non-profit established by the Indian government to develop open ecommerce. The goal is to end platform monopolies in ecommerce using an open protocol called [Beckn](https://developers.becknprotocol.io/). I'd never heard of Beckn before. From the reaction on the VRM mailing list, not many there had either.
* [Cute Learning Thread](https://twitter.com/fennykyun/status/1564249472053514240) fennykyun

tldr :: DID is just an URI :: VC is a cryptographically verifiable credential using DID :: SSI is a self-sovereign and privacy-preserving identity :: Non-human (Machines, Bots, Goods, anything) also able to have DID, VC, and SSIs

* [Blockchain and Self-Sovereign Identity Empowered Cyber Threat Information Sharing Platform](https://www.youtube.com/watch?v%3DlzS49R52PwA) Siddhi

looks interesting and different - uses DIDComm

Presented in 7th IEEE International Conference on Smart Computing(IEEE SmartComp 2021)

* [BCGov improves sustainability reporting with digital trust technology](https://trustoverip.org/blog/2022/08/29/toip-steering-committee-member-the-government-of-british-columbia-improves-sustainability-reporting-with-digital-trust-technology/) ToIP

Digital credentials can be checked in real time, expediting access to trustworthy information. These trusted, verifiable digital credentials are the core digital trust technologies being piloted and the trust ecosystem in which they operate are defined in ToIP architecture, governance, and related documents.

* [Universal Resolver - resolve practically any DID](https://blog.identity.foundation/uni-resolver/) Identity Foundation

The Universal Resolver can now resolve 45 DID methods, and more are being added regularly. Visit [https://dev.uniresolver.io/](https://dev.uniresolver.io/) to see the full list of supported methods, and visit [this github page](https://github.com/decentralized-identity/universal-resolver/blob/main/docs/driver-development.md) to contribute a driver for a DID method.

Mobile Document Request API

* [Apple, with support from Google, just announced the Mobile Document Request API](https://github.com/WICG/proposals/issues/67) Web Incubator CG

The API is concerning because it lists "Define the native communication between the User Agent and the application holding the mdoc." as out of scope. That is, digital wallet selection is out of scope. Also out of scope is "issuing" and "provisioning". The specification focuses on delivery from a digital wallet to a website.

## Aries \ Indy \ AnonCreds the dialogue continues

* [Learnings from Aries, Indy and Various Verifiable Credential Implementations](https://northernblock.io/learnings-from-aries-indy-and-various-verifiable-credential-implementations/) Northern Block

Standards such as OIDC and mDL are all now in dialogue with W3C, AnonCreds, Aries, etc. Mobile is a predominant technology, just like the way laptops were once upon a time. To reduce consumer friction and drive adoption, convergence of all these different technologies is required inside a mobile environment

* [Hyperledger Aries is the Present and the Future of Internet-Scale Trusted Verifiable Credential Ecosystems](https://indicio.tech/hyperledger-aries-is-the-present-and-the-future-of-internet-scale-trusted-verifiable-credential-ecosystems/) Indicio

While no technology runs perfectly on every device, a signal strength of Aries, AnonCreds, and Indy is that they work on the vast majority of current devices and systems, including $35 smart phones and low powered IOT/embedded devices. They represent the most inclusive way into this technology, which is an important factor in their popularity.

* [AnonCreds Indy-Pendence](https://blog.cheqd.io/anoncreds-indy-pendence-4946367469d4) Cheqd

Part 1: Decoupling the reliance on Hyperledger Indy and creating more extensible AnonCreds Objects with cheqd.

## Standards Work

* [Premature Standardization & Interoperability](https://www.continuumloop.com/premature-standardization-interoperability/) Continuum Loop

Here’s my premise – we don’t have standards nor interoperability – at least not as people really need. We have been through a process that is powerful and good – but what we have is what I call “premature standardization.” It’s a great start but nowhere near where things will be.

* [Notes from W3C TPAC on major deployments of Verifiable Credentials](https://twitter.com/philarcher1/status/1570082512122294273) Manu Sporny via Phil Archer

- Steel, Oil Agriculture Shipment into US Customs ($2.3T in good/year)
- European Digital Wallet (€163M funding, 450M people)
- Digital Education Credentials in Uganda, Nigeria, Kenya (323M people)
- Digital Age Verfication (152k retail stores, 200M people)
- Content Authenticity Initative (30M Adobe customers)
- Digital Permanent Resident Cards (14M people)

* [IDnow joins Accelerate@IATA to shape the future of seamless air travel](https://www.idnow.io/pr/idnow-joins-accelerateiata/) IDnow

The goal of IATA One ID is to set industry standards that further streamline the passenger journey with digitalization of admissibility and a contactless process through secure biometric enabled identification.

Cardano showing interest in our work

* [Advancing digital identity through DID core specification](https://iohk.io/en/blog/posts/2022/09/08/advancing-digital-identity-through-did-core-specification/) IOHK

Good news to see Cardano jumping on the bandwagon, looks like they will join the fray and bring DID\VC to Atla Prism.

The recent DID core specification approval at the World Wide Web Consortium (W3C) provided clearer and stronger foundations for identity platforms building decentralized identifiers.

* [Timo Glastra @TimoGlastra](https://twitter.com/TimoGlastra/status/1572976791136137216) via Twitter

Just got my first DIDComm protocol published on the [https://didcomm.org](https://t.co/GvWIyysx1k) website.

* [Circle and Industry Leaders Have Built the First Decentralized Identity Proof-of-Concept for Crypto Finance using Verite Credentials](https://www.circle.com/en/pressroom/circle-and-industry-leaders-have-built-the-first-decentralized-identity-proof-of-concept-for-crypto-finance-using-verite-credentials) Circle

Circle joined other crypto and blockchain companies in February 2022 to introduce Verite as a open-source framework for decentralized identity credential issuance, custody and verification. Verite is designed to help make it safer, easier and more efficient to do business across the transformative worlds of DeFi and Web3 commerce.

* [TBD Partners with Circle!](https://developer.tbd.website/blog/tbd-circle-partnership/) TBD

TBD and [Circle](https://www.circle.com/en/?_gl%3D1*14yjcwp*_up*MQ..%26gclid%3DCjwKCAjwm8WZBhBUEiwA178UnPZbgZJJxhwK7ivE5Yx9FGW8PQ31-hc1O-njcLOmzcN2nzLz110FihoCgV4QAvD_BwE) are collaborating on a set of open standards and open source technologies aimed at enabling global-scale, mainstream adoption of digital currency in payments and financial applications. The first step of which will support cross-border remittances and self-custody wallets that can hold stablecoins.

* [Identos builds Verifiable Credentials into updated federated digital ID API](https://www.biometricupdate.com/202209/identos-builds-verifiable-credentials-into-updated-federated-digital-id-api) Biometric Update

The new FPX Junction cloud software suite is designed for fine-grained API authorization and user-centric digital identity management. The digital wallet and user-managed access 2.0 authorization server work together to enable single-sign on federation. An optional user interface SDK for the digital wallet provides native mobile and web support.

* [Open Workplace Recognition using Verifiable Credentials](https://blog.weareopen.coop/open-workplace-recognition-using-verifiable-credentials-fc0134fad7ec) WeAreOpenCoop

Yesterday, [the draft](https://w3c-ccg.github.io/vc-ed-use-cases/) Verifiable Credentials for Education, Employment, and Achievement Use Cases report was published [...] The next version of the Open Badges specification (v3.0) will be compatible with Verifiable Credentials (VCs).

* [Identity Manager – Self Sovereign Identity made Simple](https://tanglelabs.io/identity-manager-self-sovereign-identity-made-simple/) TangleLabs

By producing an accessible, open-source wrapper library, Tangle Labs provides any business or development team the opportunity to easily explore SSI and to test and prototype solutions that can bring added value to your business.

* [Introduction to Decentralized Identity](https://wiki.iota.org/identity.rs/decentralized_identity) IOTA Wiki

* [Podcast] [Privacy-preserving measures and SD-JWT with Daniel Fett](https://identityunlocked.auth0.com/public/49/Identity%252C-Unlocked.--bed7fada/3bbcbab8) IdentityUnlocked Auth0

The discussion gets very concrete when Daniel describes selective disclosure JWT, or SD-JWT, a new IETF specification he is coauthoring that offers a simple and easy-to-adopt approach to produce JWTs capable of supporting selective disclosure. Here at Identity, Unlocked, we are huge fans of this new specification, and we hope this episode will help you get started!

* [SelfSovereignIdentity_memes](https://twitter.com/SSI_by_memes/status/1578045600833994755)

Currently, everyone waiting for [#AIP2](https://twitter.com/hashtag/AIP2), which enables [#BBS](https://twitter.com/hashtag/BBS)+ [#Signature](https://twitter.com/hashtag/Signature) in #SSI. Companies already implemented in their products, such as [@trinsic_id](https://twitter.com/trinsic_id) and [@mattrglobal](https://twitter.com/mattrglobal). But ZKP [#predicates](https://twitter.com/hashtag/predicates) are not supported by BBS+, so no ZKP age verification possible. Back to [#AnonCreds](https://twitter.com/hashtag/AnonCreds)?

* [](https://twitter.com/SSI_by_memes/status/1578045600833994755)

Related resources:

- [aries-rfcs/0646-bbs-credentials#drawbacks](https://github.com/hyperledger/aries-rfcs/tree/main/features/0646-bbs-credentials%23drawbacks)
- [Zero-Knowledge Proofs Do Not Solve the Privacy-Trust Problem of Attribute-Based Credentials: What if Alice Is Evil?](https://ieeexplore.ieee.org/document/9031545) IEEE

* [Primer] [Data Privacy Vocabulary (DPV)](https://w3c.github.io/dpv/primer/%23core-taxonomy) w3c

Call for Comments/Feedbacks for DPV v1.0 release

Please provide your comments by 15-OCT-2022 via [GitHub](https://github.com/w3c/dpv/issues/50) or [public-dpvcg@w3.org](https://lists.w3.org/Archives/Public/public-dpvcg/) (mailing list).

* [FYI >> DHS W3C VC/DID Implementation Profile: Credential Data Model Representation Syntax & Proof Format](https://lists.w3.org/Archives/Public/public-credentials/2022Sep/0253.html) Anil John

We are walking this path step-by-step by documenting the results and lessons from the DHS sponsored multi-platform, multi-vendor interoperability plug-fests and other rigorous plug-fests with similar goals to develop a “DHS Implementation Profile of W3C Verifiable Credentials and W3C Decentralized Identifiers” to ensure the use of Security, Privacy and Interoperability implementation choices that are acceptable to the USG such that these capabilities can be deployed on and connect to USG networks and infrastructure.

…

please [find attached the DHS Implementation Profile](https://lists.w3.org/Archives/Public/public-credentials/2022Sep/att-0253/DHS.W3C.VC-DID.Implemenation.Profile-20220929-SHARE.pdf) of W3C VCs and W3C DIDs normative guidance on:

·         Credential Data Model Representation Syntax

·         Credential Data Model Proof Format

* [Using OpenID4VC for Credential Exchange; Technometria - Issue #62](http://news.windley.com/issues/using-openid4vc-for-credential-exchange-technometria-issue-62-1374264?via%3Dtwitter-card%26client%3DDesktopWeb%26element%3Dissue-card)

Extending OAuth and OIDC to support the issuance and presentation of verifiable credentials provides for richer interactions than merely supporting authentication. All the use cases we’ve identified for verifiable credentials are available in OpenID4VC as well.

* [Trinsic Basics: What Are SSI Standards?](https://trinsic.id/what-are-ssi-standards/)
  > There are two kinds of standards that Trinsic implements to enable interoperability and avoid vendor lock-in: data model standards and protocol standards.

* [Trusted P2P Messaging with DIDs, DIDComm and VCs](https://medium.com/uport/trusted-p2p-messaging-with-dids-didcomm-and-vcs-398f4c3f3cda) uPort
  > about their path towards trusted P2P messaging and announces the [DIDAgent Framework (DAF)](https://github.com/uport-project/daf)
  > 
  > when we speak about a DID, then we need to be more precise and also speak about the particular DID method of that DID which defines the CRUD operations on a target system such as Ethereum.
