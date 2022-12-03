# Decentralized Identifier

* [W3C launches Decentralized Identifiers as a web standard](https://portswigger.net/daily-swig/w3c-launches-decentralized-identifiers-as-a-web-standard) in the Daily Swig: Cybersecurity news and views.

“I would summarize the overall impact of DIDs on cybersecurity as making digital signing and [encryption](https://portswigger.net/daily-swig/encryption) much more widely available than today’s conventional X.509-based public key infrastructure (PKI),” Drummond Reed, director of trust services at Avast
* [W3C overrules objections by Google, Mozilla to decentralized identifier spec](https://www.theregister.com/2022/07/01/w3c_overrules_objections/) Oh no, he DIDn't in the Register
  > The [DID specification](https://www.w3.org/TR/did-core/%23introduction) describes a way to deploy a globally unique identifier without a centralized authority (eg, Apple [for Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) as a verifying entity.
* [Link your domain to your Decentralized Identifier (DID) (preview)](https://docs.microsoft.com/en-us/azure/active-directory/verifiable-credentials/how-to-dnsbind)
  > We make a link between a domain and a DID by implementing an open standard written by the Decentralized Identity Foundation called [Well-Known DID configuration](https://identity.foundation/.well-known/resources/did-configuration/). The verifiable credentials service in Azure Active Directory (Azure AD) helps your organization make the link between the DID and domain by including the domain information that you provided in your DID, and generating the well-known config file:

* [What is a DID? Part 1](https://www.youtube.com/watch?v%3DOYYtxVEra1c) XSL Labs
* [Qu’est-ce qu’un DID? Partie 1](https://www.youtube.com/watch?v%3DVNLKufTDM4o) XSL Labs
* [Decentralized Identity: Why Are DIDs The Future of Digital Identity Management?](https://elastos.info/decentralized-identity-dids/)
  > Why would you have 75 logins when you could have 1?
* [A DIF & TOIP Joint Statement of Support for the Decentralized Identifiers (DIDS) V1.0 Specification Becoming A W3C Specification](https://trustoverip.org/blog/2021/10/29/a-dif-toip-joint-statement-of-support-for-the-decentralized-identifiers-dids-v1-0-specification-becoming-a-w3c-standard/).

DIDs are a critical part of a technical foundation for the products and activities of many of our members. Many of the implementations in the [DID Working Group’s implementation report](https://w3c.github.io/did-test-suite/%23report-by-methods) were developed by engineers and companies who collaborate openly at DIF on points of technical interoperability, and at ToIP on points of policy and governance.
* [Indicio’s support for the W3C DID Specification and its path to standardization](https://indicio.tech/indicios-support-for-the-w3c-did-specification-and-its-path-to-standardization/)
  > The position of Indicio is that the DID Specification is of signal importance to creating a better digital world. We recognize that, as with any specification, improvements can and will be made in the future; but we back its recommendations and its approval.
* [ENS names are Decentralized Identifiers (DIDs)](https://medium.com/uport/ens-names-are-decentralized-identifiers-dids-724f0c317e4b) uPort
  > - did:ens:mainnet:vitalik.eth
  > 
  > This has two purposes:
  > 1. to wrap existing ENS names as DIDs to facilitate interoperability of emerging technologies in the Decentralized Identity and Ethereum community,
  > 2. to define a canonical way to augment ENS names with DID capabilities (e.g., encryption) as mentioned above.
* [Community Resources - DID Primer](https://w3c-ccg.github.io/did-primer/) Credentials Community Group
  > At a superficial level, a decentralized identifier (DID) is simply a new type of globally unique identifier. But at a deeper level, DIDs are the core component of an entirely new layer of decentralized digital identity and public key infrastructure (PKI) for the Internet. This [decentralized public key infrastructure](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/dpki.pdf) (DPKI) could have as much impact on global cybersecurity and cyberprivacy as the development of the [SSL/TLS protocol](https://en.wikipedia.org/wiki/Transport_Layer_Security) for encrypted Web traffic (now the largest PKI in the world).
* [Cryptography Review of W3C VC Data Model and DID Standards and Implementation Recommendations](https://www.linkedin.com/posts/aniljohn_cryptography-review-of-w3c-vc-and-w3c-did-ugcPost-6892250585652162560-OQ3Y) SRI International
* [Adding DID ION to MATTR VII](https://medium.com/mattr-global/adding-did-ion-to-mattr-vii-d56bdb7a2fde)
  > Different types of DIDs can be registered and anchored using unique rules specific to the set of infrastructure where they’re stored. Since DIDs provide provenance for keys which are controlled by DID owners, the rules and systems that govern each kind of DID method have a significant impact on the trust and maintenance model for these identifiers.

## DID Core advances to recommendation

* [Objections overruled by W3C director approving the DIDCore specification as a W3C Recommendation](https://www.w3.org/2022/06/DIDRecommendationDecision.html) W3C

The DID core specification is approved to advance to W3C Recommendation.

In its next chartered period the Working Group should address and deliver proposed standard DID method(s) and demonstrate interoperable implementations.  The community and Member review of such proposed methods is the natural place to evaluate the questions raised by the objectors and other Member reviewers regarding decentralization, fitness for purpose, and sustainable resource utilization. -Ralph Swick, for Tim Berners-Lee

* [Decentralized Identifiers (DID) 1.0 specification approved as W3C Recommendation](https://blog.identity.foundation/w3cdidspec-2/) Identity Foundatoin

Announcing the [Decentralized Identifiers (DID) v1.0 specification](https://www.w3.org/TR/did-core/) as an open web standard signals that it is technically sound, mature, and ready for widespread adoption. Having an established v1.0 specification allows work to continue with renewed energy and focus, not only at the many groups meeting at DIF, but across the digital identity community.
* [Decentralized Identifiers: Implications for Your Data, Payments and Communications](https://newsletter.impervious.ai/decentralized-identifiers-implications-for-your-data-payments-and-communications-2/) Impervious
  > Through the DID Specification, service endpoints and DIDComm, Impervious has interlaced DIDs with Bitcoin Lightning, IPFS, WebRTC and resilient relays to introduce a new peer-to-peer internet standard with practical applications for mitigating censorship and surveillance risk.
* [Verification Patterns, Part 2](https://docs.centre.io/blog/verification-patterns-2) Verite

Part 2 of this 2-part series explains the [did:pkh](https://github.com/w3c-ccg/did-pkh/blob/main/did-pkh-method-draft.md)/[CACAO](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-74.md%23simple-summary) variation for Verite data models and flows, which provides an entry path for wallets that may not support sufficient functionality for emerging decentralized identity patterns

* [Cute Learning Thread](https://twitter.com/fennykyun/status/1564249472053514240) fennykyun

tldr :: DID is just an URI :: VC is a cryptographically verifiable credential using DID :: SSI is a self-sovereign and privacy-preserving identity :: Non-human (Machines, Bots, Goods, anything) also able to have DID, VC, and SSIs

* [Universal Resolver - resolve practically any DID](https://blog.identity.foundation/uni-resolver/) Identity Foundation

The Universal Resolver can now resolve 45 DID methods, and more are being added regularly. Visit [https://dev.uniresolver.io/](https://dev.uniresolver.io/) to see the full list of supported methods, and visit [this github page](https://github.com/decentralized-identity/universal-resolver/blob/main/docs/driver-development.md) to contribute a driver for a DID method.
* [Advancing digital identity through DID core specification](https://iohk.io/en/blog/posts/2022/09/08/advancing-digital-identity-through-did-core-specification/) IOHK

Good news to see Cardano jumping on the bandwagon, looks like they will join the fray and bring DID\VC to Atla Prism.

The recent DID core specification approval at the World Wide Web Consortium (W3C) provided clearer and stronger foundations for identity platforms building decentralized identifiers.

* [DIDs in DPKI](https://github.com/WebOfTrustInfo/rwot7/blob/master/topics-and-advance-readings/dids-in-dpki.md)
- [jolocom/ddoresolver-rs](https://github.com/jolocom/ddoresolver-rs) github
- [Rust implementation of the did:key method](https://crates.io/crates/did-key) creds to Tomislav Markovski.
* [Universal Resolver Driver Policy Discussion](https://iiw.idcommons.net/21P/_Universal_Resolver_Driver_Policy_Discussion) by Bernhard Fuchs, Markus Sabadello
  > The project has some guidelines for contributing new DID method drivers:[https://github.com/decentralized-identity/universal-resolver/blob/master/docs/driver-development.md](https://github.com/decentralized-identity/universal-resolver/blob/master/docs/driver-development.md)
- [DID test suite](https://github.com/w3c/did-test-suite) GitHub
  > DID test suite is not for runtime, but the Universal Resolver could do a few simple checks on a driver's responses. But there's also a philosophical question: Should the Universal Resolver be "allowed" to check and potentially transform driver responses, or should it just "pass through" everything that comes from a driver?
* [did:orb slides Troy Ronda (SecureKey)](https://lists.w3.org/Archives/Public/public-credentials/2021Mar/0017.html)
  > - Decouple witness ledgers from the critical path.
  > - Allow for Trust but Verify model.
  > - Leverage the Certificate Transparency model
  > - Witnesses observe VDR objects and promise to include in their ledgers.
  > - Provide a signed timestamp and a maximum merge delay.
  > - Enable monitoring to ensure witnesses follow their promises.
  > - Use trusted Witness (and origin) timings to resolve late publishing.
  > - Use origin to enable observers to know if they have the latest operations.


* [re: Defining load balanced, failover clusters for DID Document serviceEndpoints?](https://lists.w3.org/Archives/Public/public-credentials/2022Jan/0056.html)  (Monday, 10 January)

#didlang 0.3 includes support for round-robin, load-balanced DID Agent serviceEndpoint clusters. [Here's a demo](https://youtu.be/mf0aKLvJoCw)

* [W3C Decentralized Identifiers v1.0 is a W3C Proposed Recommendation](https://lists.w3.org/Archives/Public/public-credentials/2021Aug/0030.html)  Manu Sporny (Tuesday, 3 August)

* [W3C Decentralized Identifiers v1.0 is a W3C Proposed Recommendation](https://www.w3.org/blog/news/archives/9179):

* [The published version that will be voted on by W3C Members can be found here](https://www.w3.org/TR/2021/PR-did-core-20210803/):

This is the final step of the W3C global standardization process.

If you are a W3C Member, you can now vote to approve it as a global standard here:

* [DID 1.0 Comments / Meeting Minutes (was RE: Mozilla Formally Objects to DID Core)](https://lists.w3.org/Archives/Public/public-credentials/2021Sep/0135.html)  John, Anil (Monday, 27 September)

* [https://www.w3.org/2021/09/21-did10-minutes.html](https://www.w3.org/2021/09/21-did10-minutes.html) is fascinating reading!

* [...] I can speak to the work of the DHS SVIP Program and our approach and perspective across our two  work-streams that touch upon the two points.

1.  Governments “lobbying” for single DID method and Non-Interoperability

*   “tantek: concerned to hear that there are governments looking to adopt, with only single implementation methods and non interop, sounds like lobbying may have occurred, … advocating for single-implementation solutions that are centralized wolves in decentralized clothing”

*   “<cwilso> +1 to tantek's concern that governments are responding to lobbying attempts on non-interoperable methods”

* [Mozilla Formally Objects to DID Core](https://lists.w3.org/Archives/Public/public-credentials/2021Sep/0010.html)  Drummond Reed (Thursday, 1 September)

Now, here's the REAL irony. Mozilla and others are pointing to the URI spec and existing URI schemes as the precedent without recognizing that in [in section 9.11 of the DID spec](https://www.w3.org/TR/did-core/%23dids-as-enhanced-urns), we specifically compare the DID spec to the *URN spec*, [RFC 8141](https://datatracker.ietf.org/doc/html/rfc8141). In fact we deliberately patterned the [ABNF for DIDs](https://www.w3.org/TR/did-core/%23did-syntax)  after the ABNF for URNs—and patterned DID method names after URN namespaces. And we set up a registry for the exactly the same way RFC 8141 establishes a [registry of URN namespaces](https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml).

Now: guess how many URN namespaces have been registered with IANA?

- [SEVENTY*. Count em.](https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xhtml)

I don't see anyone complaining about interoperability of URN namespaces. Amd RFC 8141 was published over four years ago.

* [Some questions regarding DID verification relationships](https://lists.w3.org/Archives/Public/public-credentials/2021Dec/0009.html) Dmitri Zagidulin (Thursday, 2 December)

The motivation for verification relationships in the DID spec stems from the general security recommendation of "use separate keys for separate purposes".

You can see this at work in other specifications, such as JWKS (JSON Wek Key Set), specifically in the 'use' (Public Key Use) parameters, from [https://datatracker.ietf.org/doc/html/rfc7517#section-4.2](https://datatracker.ietf.org/doc/html/rfc7517%23section-4.2)

* [DID press release and UNECE white paper](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0087.html)  steve capell (Wednesday, 20 July)

great to see that press release at [https://www.w3.org/2022/07/pressrelease-did-rec.html.en](https://www.w3.org/2022/07/pressrelease-did-rec.html.en)

There's a testimonial from UNECE near the bottom.  I thought the community might be interested in the white paper from UNECE on VCs and DIDs for cross border trade - [https://unece.org/trade/uncefact/guidance-material](https://unece.org/trade/uncefact/guidance-material)

* [DID Press Release Testimonials](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0022.html)  Zundel, Brent (Friday, 8 July)

This message is to inform the DID WG and CCG that the W3C intends to write a press release.

To that end, we are seeking testimonials about Decentralized Identifiers.

For an example of the sort of thing we're looking for, please see: [https://www.w3.org/2019/03/pressrelease-webauthn-rec.html](https://www.w3.org/2019/03/pressrelease-webauthn-rec.html)

The testimonials may be submitted as a reply to this email.

DID Methods

* [Announcement: New DID Method Specification: did:object](https://lists.w3.org/Archives/Public/public-credentials/2021Dec/0067.html)  (Tuesday, 14 December)

The publication of [this DID Method specification](https://github.com/mwherman2000/TrustedDigitalWeb/blob/master/specifications/did-methods/did-object.md) realizes, in large part, a 4-year quest (or should I say personal mission) to create a platform to Tokenize Every Little Thing (ELT).

* [Re: CCG Community opinions needed to define CCG scope (specifically re: did methods as work items)](https://lists.w3.org/Archives/Public/public-credentials/2021Aug/0376.html)  Manu Sporny (Thursday, 26 August)

On 8/26/21 12:37 PM, Heather Vescent wrote:

> 1. What are the *pros* of including did methods as work items in the CCG?

Community vetting and approval of particular DID Methods.

Basically, broader and deeper review of DID Methods that we expect to be of

great use to the world. I expect there will be DID Methods that the community

wants to eventually propose as DID Methods for standardization (did:key and

did:web feel like two ones where we could get consensus on doing so).

* [DID methods as W3C standards - a happy compromise?](https://lists.w3.org/Archives/Public/public-credentials/2022Feb/0117.html)  steve capell (Tuesday, 22 February)

can't we pick just a small number of un-controversial methods to standardise?  even if it's just did:key and did:web to start with.

* [Cross border identity use case - which did methods?](https://lists.w3.org/Archives/Public/public-credentials/2022Mar/0016.html)  steve capell (Sunday, 6 March)

The broader generalisation of this question is : "for trust anchors like governments that issue VCs to their constituents, what rules should govern which did:methods they should accept as the *subject* identifier for the VCs they issue?"  Are those rules context specific?

I'm not sure of the answer - but it's why did:ion was on my list - as an allowed *subject* of a government issued vc - and as the issuer of trade documents.  should I take it off my list pending a bit more maturity (eg that azure service goes out of beta into full production)?  or is it safe enough for this use case?  if so what others would also be "safe enough"?

![https://www.notion.soimages/image2.png](https://www.notion.soimages/image2.png)

DID:TAG[re: Using Email as an Identifier](https://lists.w3.org/Archives/Public/public-credentials/2021Nov/0065.html)  Bob Wyman (Friday, 12 November)

My [did:tag](https://github.com/bobwyman/did_method_tag) proposal is, I believe, the only proposed DID Method that addresses the use of email addresses and email as a resolution method

There are quite a number of issues with using email addresses as identifiers, or parts of identifiers, and I'm hoping that discussion and development of the did:tag method will illuminate those issues and potentially find solutions for them.

DID:WEB

* [re: some thought after using did:web](https://lists.w3.org/Archives/Public/public-credentials/2022Jan/0031.html)  Orie Steele (Wednesday, 5 January)

We have had the same issue... per the did core spec, there are really 2 main key types, in our crypto libraries for the key pair classes themselves, we do our best to support both and handle translation for you:

* [https://github.com/transmute-industries/verifiable-data/blob/main/packages/ed25519-key-pair/src/Ed25519KeyPair.ts#L78](https://github.com/transmute-industries/verifiable-data/blob/main/packages/ed25519-key-pair/src/Ed25519KeyPair.ts%23L78)

* [https://github.com/transmute-industries/verifiable-data/blob/main/packages/ed25519-key-pair/src/types/Ed25519VerificationKey2018.ts](https://github.com/transmute-industries/verifiable-data/blob/main/packages/ed25519-key-pair/src/types/Ed25519VerificationKey2018.ts)

* [https://github.com/transmute-industries/verifiable-data/blob/main/packages/ed25519-key-pair/src/types/Ed25519VerificationKey2020.ts](https://github.com/transmute-industries/verifiable-data/blob/main/packages/ed25519-key-pair/src/types/Ed25519VerificationKey2020.ts)

* [https://github.com/transmute-industries/verifiable-data/blob/main/packages/ed25519-key-pair/src/types/JsonWebKey2020.ts](https://github.com/transmute-industries/verifiable-data/blob/main/packages/ed25519-key-pair/src/types/JsonWebKey2020.ts)

* [DID Web, OpenSSL and Certificate Authorities](https://lists.w3.org/Archives/Public/public-credentials/2022Feb/0078.html)  Orie Steele (Thursday, 17 February)

We then generate a DID Web DID Document from the public keys for the 3 children, and encode the ca chain from them back to the root using `x5c`.

We then issue a JWT from the private key for 1 of them.

We then verify the JWT signature using the public key.

We then check the x5c using open seel to confirm the certificate chain.

My questions are:

1. Is it possible to use JOSE to automate this further?

2. Is there a better way of accomplishing this?

3. Should the CA chain be pushed into the JWT?

DID:JWK

* [did:jwk is reborn!](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0066.html)  Orie Steele (Friday, 8 April)

* [https://github.com/w3c/did-spec-registries/pull/432](https://github.com/w3c/did-spec-registries/pull/432)

DID:KEY

* [did-key-creator published](https://lists.w3.org/Archives/Public/public-credentials/2022Jun/0061.html)  Brent Shambaugh (Tuesday, 28 June)

I published a did:key creator at

* [https://www.npmjs.com/package/did-key-creator](https://www.npmjs.com/package/did-key-creator)

This has been tested to create did:keys from the P-256,P-384, and P-521 curves specified in [https://github.com/w3c-ccg/did-method-key](https://github.com/w3c-ccg/did-method-key) and [https://w3c-ccg.github.io/did-method-key/](https://w3c-ccg.github.io/did-method-key/) .

* [did:key DID Document generation algorithm feedback](https://lists.w3.org/Archives/Public/public-credentials/2022Jun/0016.html)  Manu Sporny (Tuesday, 14 June)

The DID Document generation algorithm for did:key is being refined to the

point that we can finish off a first pass of a did:key test suite.

* [...] [https://github.com/w3c-ccg/did-method-key/pull/51](https://github.com/w3c-ccg/did-method-key/pull/51)

