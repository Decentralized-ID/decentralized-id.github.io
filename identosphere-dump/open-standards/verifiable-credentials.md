---
published: false
---

# Verifiable Credentials

## Contents

- Varieties
  - JSON-LD 
  - JSON-LD ZKP BBS+
  - JSON-JWT
  - ZKP-CL - [IIA] Indy Aries AnnonCreds
  - JWP






## History

* [The original #VerifiableCredentials were PKI-based SIM cards and EMV cards.](https://twitter.com/Steve_Lockstep/status/1419935186188341249) @Steve_Lockstep
  > These bind key pairs to individuals, and to signed assertions (account numbers) to deliver provenance, fidelity and proof of possession. [https://constellationr.com/blog-news/not-too-much-identity-technology-and-not-too-little](https://constellationr.com/blog-news/not-too-much-identity-technology-and-not-too-little)
  > ![](https://i.imgur.com/ucAVxCX.png)

## DHS
* [FYI >> DHS W3C VC/DID Implementation Profile: Credential Data Model Representation Syntax & Proof Format](https://lists.w3.org/Archives/Public/public-credentials/2022Sep/0253.html) Anil John
  > We are walking this path step-by-step by documenting the results and lessons from the DHS sponsored multi-platform, multi-vendor interoperability plug-fests and other rigorous plug-fests with similar goals to develop a “DHS Implementation Profile of W3C Verifiable Credentials and W3C Decentralized Identifiers” to ensure the use of Security, Privacy and Interoperability implementation choices that are acceptable to the USG such that these capabilities can be deployed on and connect to USG networks and infrastructure.
  > … please [find attached the DHS Implementation Profile](https://lists.w3.org/Archives/Public/public-credentials/2022Sep/att-0253/DHS.W3C.VC-DID.Implemenation.Profile-20220929-SHARE.pdf) of W3C VCs and W3C DIDs normative guidance on:
  > - Credential Data Model Representation Syntax
  > - Credential Data Model Proof Format


## Ontology
* [Verifiable Claim Protocol](https://github.com/ontio/ontology-DID/blob/master/docs/en/claim_spec.md) Ontology

## Literature

### NGI
* [Crossword wins NGI Atlantic funds for Verifiable Credentials project](https://www.crosswordcybersecurity.com/post/next-generation-internet-grant-win) Crossword Cybersecurity
  > European Commission’s Next Generation Internet (NGI) initiative to lead a project to test the OpenID Foundation’s protocols for transferring verifiable credentials. Crossword’s partners in this project are Spruce Inc from the USA and Fraunhofer from Germany

## VC-EDU
* [Add Your VC-EDU Use Cases](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0296.html)  Kerri Lemoie (Friday, 30 July)
  > For Github users, submit your use cases as issues here: [https://github.com/w3c-ccg/vc-ed-use-cases/issues](https://github.com/w3c-ccg/vc-ed-use-cases/issues)
  > 
  > This template can help guide you: [https://github.com/w3c-ccg/vc-ed-use-cases/blob/main/.github/ISSUE_TEMPLATE/use-case-template.md](https://github.com/w3c-ccg/vc-ed-use-cases/blob/main/.github/ISSUE_TEMPLATE/use-case-template.md)
* [W3C Verifiable Credentials Education Task Force 2022 Planning](https://kayaelle.medium.com/w3c-verifiable-credentials-education-task-force-2022-planning-efc9b07cc2a3) Kerri Lemoie
  > We’ve been hard at work writing use cases, helping education standards organizations understand and align with VCs, and we’ve been heading towards a model recommendation doc for the community.

## Questions and Answers

* [Question About Signatures & Contexts](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0290.html)  Kerri Lemoie (Friday, 30 July)
  > Is a VC still considered to be valid if it contains fields that are not described in its context file(s)? Does it depend on the signature type?
  * [Re: Question About Signatures & Contexts](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0291.html) Manu Sporny
    > The short answers are "maybe" and "yes".
* [Any Good use case of PAM (Privileged account Management) using Vcs](https://lists.w3.org/Archives/Public/public-credentials/2021Nov/0028.html) Bob Wyman (Sunday, 7 November)
  > A common example of this is when someone uses a "Power of Attorney," to sign a contract. When they do, they typically sign documents with their own names and an annotation "on behalf of," "for," or "by power of attorney," they don't forge the signature of the one who granted the power of attorney.



## Varieties

* [Verifiable Credentials Specifications Relationship Diagram](https://github.com/manicprogrammer/vc-spec-rel/) "Good for anyone but especially useful when trying to jump in on the deep end. If you walk even this limited tree of specs you know a lot" - [@michaelruminer](https://twitter.com/michaelruminer/status/1328827452886540296)
* [Paper based Verifiable Credentials](https://www.youtube.com/watch?v%3DEXvWxFjHvdY) Mattr
  > Paper-based Verifiable Credentials allow us to have a low-tech solution for adopting VC's in situations where access to a phone cannot be guaranteed. This presentation looks at how this solution can be used to aid with the distribution of Vaccine Credentials.
* [The Flavors of Verifiable Credentials](https://www.lfph.io/2021/02/11/cci-verifiable-credentials-flavors-and-interoperability-paper/) Linux Foundation Public Health Blog [pdf]((https://www.lfph.io/wp-content/uploads/2021/02/Verifiable-Credentials-Flavors-Explained.pdf))
  > The differences between the different flavors of VCs for technically inclined readers. It elaborated on the differences between JSON and JSON-LD and articulated differences between the two different implementations of ZKP style credentials. The ‘Journey of a VC’ section articulated all steps where VCs are active and highlighted the differences in how different VC flavors ’behave’.
* [Why the Verifiable Credentials Community Should Converge on BBS+](https://www.evernym.com/blog/bbs-verifiable-credentials/)
  > BBS+ LD-Proofs use JSON-LD schemas, so credentials that use them can have a rich, hierarchical set of attributes. Instead of the heavy-handed mechanism for the encoding and canonicalization of attributes values that we’d imagined for Rich Schemas, they use RDF canonicalization and a hash function. Rather than expanding the credential definition, they discarded it, taking advantage of some properties of BBS+ keys which allow for deterministic expansion.
* [GS1 2021 VC Prototype Journey](https://iiw.idcommons.net/20P/_GS1_2021_VC_Prototype_Journey) by Paul Dietrich
  > There was some feedback that  BBS, PE, and DIDCommV2 are possible points of convergence.
  > 
  > Also comments that WACI Bloom may play a part in convergence


## VC for OAuth 2.0

* [VC Issuance based on OAuth 2.0](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0084.html)  Nikos Fotiou (Thursday, 14 April)

We design, implement, and evaluate a solution for achieving continuous authorization of HTTP requests exploiting Verifiable Credentials (VCs) and OAuth 2.0. Specifically, we develop a VC issuer that acts as an OAuth 2.0 authorization server, a VC verifier that transparently protects HTTP-based resources, and a VC wallet implemented as a browser extension capable of injecting the necessary authentication data in HTTP requests without needing user intervention.


### VC-HTTP-API

* [Supporting VC-JWT and BBS+ Presentation Exchange in the VC-HTTP-API](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0313.html)  Orie Steele (Saturday, 31 July)
  > [https://github.com/OR13/GNARLY](https://github.com/OR13/GNARLY)  (while we wait for a better name...)
  > 
  > This demo API and Spec has a number of improvements over the current
  > 
  > VC-HTTP-API, including tested support for VC-JWT, JsonWebSignature2020 and
  > 
  > BBS+ Selective Disclosure Presentation Exchange.
* [Updated VC-API diagram for Supply Chain flow](https://lists.w3.org/Archives/Public/public-credentials/2021Sep/0141.html)  Joe Andrieu (Tuesday, 28 September)
  > ![](https://i.imgur.com/mH5TBtU.png)
* [re: VC API: handling large documents client to server](https://lists.w3.org/Archives/Public/public-credentials/2022Feb/0035.html)  Manu Sporny (Thursday, 10 February)
  > Typical solutions to this problem require that you put the binary data outside of the VC, if at all possible. This works well for common static images such as logos. It is also possible to split the VC into two VCs... one with the machine-readable data from the issuer (with a digital signature) and one with the image data from any source (without a digital signature, since, if hashlinked, the signature will verify the validity of the image data). That latter approach can be more privacy preserving AND more complex than many might feel is necessary.
* [VC-API interoperability test suites ready for experimental integration](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0126.html)  Manu Sporny (Tuesday, 26 April)
  > * [The VC API test suite for basic issuer interop is here](https://w3c-ccg.github.io/vc-api-issuer-test-suite/)
  > * [The VC API test suite for basic verifier interop is here](https://w3c-ccg.github.io/vc-api-verifier-test-suite/)
  > * [The Data Integrity test suite for Ed25519Signature2020 interop is here](https://w3c-ccg.github.io/di-ed25519-test-suite/)
* [Cross-industry VC API test suite achieves first multi-vendor interop for issue/verify](https://lists.w3.org/Archives/Public/public-credentials/2022May/0041.html)  Manu Sporny (Wednesday, 18 May)
  > We are happy to announce today that we have our first demonstration of cross-vendor interoperability between Danube Tech and Digital Bazaar for the VC Issuer API and VC Verifier API. The test suites test the OAS definition files (which are used to generate the specification):
  > * [2.1 Verify Credential - Data Integrity](https://w3c-ccg.github.io/vc-api-verifier-test-suite/%23Verify%2520Credential%2520-%2520Data%2520Integrity)
  > * [2.1 Issue Credential - Data Integrity](https://w3c-ccg.github.io/vc-api-issuer-test-suite/%23Issue%2520Credential%2520-%2520Data%2520Integrity)

* [Diagrams for VC HTTP API work [was Re: [AGENDA] VC HTTP API Work Item - August 17th 2021]](https://lists.w3.org/Archives/Public/public-credentials/2021Aug/0231.html)  Joe Andrieu (Monday, 16 August)
  > ![](https://i.imgur.com/4hCNLVA.png)
* [Issuer API Cross Trust Boundary Scoping - VC-HAPI (f.k.a. VC-HTTP-API)](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0263.html)  Brian Richter (Saturday, 24 July)
  > I think I'm starting to understand how RAR fits into this picture. This decision can be made for us by punting the question to the authorization process entirely. With RAR we can force the user to authorize for the actual subject they are issuing the credential about. Is Alice authorized to issue VCs with claims about did:example:12345? To answer that question Alice asks for a token with the following RAR request
* [RAR Structures for VC HTTP API](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0208.html)  Justin Richer (Wednesday, 21 July)
  > It seemed like a good idea when I first invented it a decade ago: [](https://blue-button.github.io/blue-button-plus-pull/%23scopes)[https://blue-button.github.io/blue-button-plus-pull/#scopes](https://blue-button.github.io/blue-button-plus-pull/%23scopes) or when it got pulled into other efforts like [https://openid.net/specs/openid-heart-fhir-oauth2-1_0-2017-05-31.html](https://openid.net/specs/openid-heart-fhir-oauth2-1_0-2017-05-31.html)… and Orie even suggested the following set of parameterized scopes for this API:
  > 'create:credentials': Grants permission to create credentials\
  > 'derive:credentials': Grants permission to derive credentials\
  > 'create:presentations': Grants permission to create presentations\
  > 'verify:presentations': Grants permission to verify presentations\
  > 'exchange:presentations': Grants permission to exchange presentations\
  > So what’s the problem? I can say with full confidence after years of experience building and deploying systems to support parameterized scopes like this that they are fragile, awkward, and lead to insecure corner cases.
* [Bikeshed: Renaming the VC HTTP API](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0131.html)  Manu Sporny (Saturday, 17 July)
  > the fundamental issue is that stringing a bunch of consonants together ("HTTP") rarely leads to something easy to say in conversation.
* [Identity, Unlocked... Explained: Season 2, Ep. 2](https://auth0.com/blog/identity-unlocked-explained-season-2-ep-2/) Vittorio Bertocci with Filip Skokan
  > a conversation about a few three-letter extensions to OAuth (which, incidentally, would also fit well in a pirate incantation!): PAR, RAR, and JAR. Filip is a Senior Engineer II at Auth0, the author of a popular book on open source identification, and a contributor to both the [IETF](https://www.ietf.org/) and the [OpenID Foundation](https://openid.net/foundation/).
