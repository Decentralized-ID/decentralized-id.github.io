---
published: false
---

# Verifiable Credentials


* [DIF Grant #1: JWS Test Suite](https://blog.identity.foundation/dif-grant-1-jws-test-suite/)

DIF announces its first community microgrant, sponsored by Microsoft and rewarding the timely creation of a comprehensive test suite for detached-JWS signatures on Verifiable Credentials

* [Open Workplace Recognition using Verifiable Credentials](https://blog.weareopen.coop/open-workplace-recognition-using-verifiable-credentials-fc0134fad7ec) WeAreOpenCoop

Yesterday, [the draft](https://w3c-ccg.github.io/vc-ed-use-cases/) Verifiable Credentials for Education, Employment, and Achievement Use Cases report was published [...] The next version of the Open Badges specification (v3.0) will be compatible with Verifiable Credentials (VCs).
* [FYI >> DHS W3C VC/DID Implementation Profile: Credential Data Model Representation Syntax & Proof Format](https://lists.w3.org/Archives/Public/public-credentials/2022Sep/0253.html) Anil John
  > We are walking this path step-by-step by documenting the results and lessons from the DHS sponsored multi-platform, multi-vendor interoperability plug-fests and other rigorous plug-fests with similar goals to develop a “DHS Implementation Profile of W3C Verifiable Credentials and W3C Decentralized Identifiers” to ensure the use of Security, Privacy and Interoperability implementation choices that are acceptable to the USG such that these capabilities can be deployed on and connect to USG networks and infrastructure.
  > … please [find attached the DHS Implementation Profile](https://lists.w3.org/Archives/Public/public-credentials/2022Sep/att-0253/DHS.W3C.VC-DID.Implemenation.Profile-20220929-SHARE.pdf) of W3C VCs and W3C DIDs normative guidance on:
  > - Credential Data Model Representation Syntax
  > - Credential Data Model Proof Format

* [Notes from W3C TPAC on major deployments of Verifiable Credentials](https://twitter.com/philarcher1/status/1570082512122294273) Manu Sporny via Phil Archer

- Steel, Oil Agriculture Shipment into US Customs ($2.3T in good/year)
- European Digital Wallet (€163M funding, 450M people)
- Digital Education Credentials in Uganda, Nigeria, Kenya (323M people)
- Digital Age Verfication (152k retail stores, 200M people)
- Content Authenticity Initative (30M Adobe customers)
- Digital Permanent Resident Cards (14M people)
* [Do I Need a Verifiable Credential?](https://community.rsa.com/t5/rsa-labs-blog/do-i-need-a-verifiable-credential/ba-p/610241)
* [Verifiable Claim Protocol](https://github.com/ontio/ontology-DID/blob/master/docs/en/claim_spec.md) Ontology
* [Open Badges as Verifiable Credentials](https://kayaelle.medium.com/in-the-w3c-vc-edu-call-on-june7-2021-we-discussed-open-badges-asserted-as-w3c-verifiable-90391cb9a7b7)
  > In the [W3C VC-EDU](https://w3c-ccg.github.io/vc-ed/) call on June 7, 2021 we discussed [Open Badges](https://openbadges.org/) asserted as [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model/) (VCs). This call began the public discussion of Open Badges as Native VCs (potentially as Open Badges 3.0) to inform the IMS Open Badges Working Group. Why are we discussing this? Why does it matter? How will it work?
* [How a combination of Federated identity and Verifiable Credentials can help with Customer onboarding](https://pranavkirtani.medium.com/how-a-combination-of-federated-identity-and-verifiable-credentials-can-help-with-customer-7e6518feb018) Pranav Kirtani
  > Before we dive into how Federated systems like OIDC and SAML along with Verifiable Credentials (VC) can help improve customer onboarding to your application, let us first understand what are the current methods being used for onboarding.
* [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/)

- The components that constitute a [verifiable credential](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-credentials)
- The components that constitute a [verifiable presentation](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-presentations)
- An ecosystem where [verifiable credentials](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-credentials) and [verifiable presentations](https://www.w3.org/TR/2022/WD-vc-data-model-2.0-20220811/%23dfn-verifiable-presentations) are expected to be useful
- The use cases and requirements that informed this specification.
* [Crossword wins NGI Atlantic funds for Verifiable Credentials project](https://www.crosswordcybersecurity.com/post/next-generation-internet-grant-win) Crossword Cybersecurity

European Commission’s Next Generation Internet (NGI) initiative to lead a project to test the OpenID Foundation’s protocols for transferring verifiable credentials. Crossword’s partners in this project are Spruce Inc from the USA and Fraunhofer from Germany
* [Binding credentials to publicly accessible repositories](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0297.html)  Leonard Rosenthol (Friday, 30 July)

These VC’s (etc.) will be embedded into the assets (e.g., video, images, documents, etc.) in a tamper-evident manner, so that in addition to the individual VC’s “proof”, any attempt to change the CreativeWork relationships, etc. can also be detected. [..] we have no protection against a malicious actor simply copying the VC from one asset and dropping it into another (and then signing the new setup), because there is nothing that binds the credential to the asset in our case.

* [Re: Binding credentials to publicly accessible repositories](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0301.html) Joe Andrieu

This seems more of a feature of the architecture than a threat, as long as you understand that the signing of the anti-tamper mechanism is, by its nature, an attestation about the affinity of that VC to the rest of the PDF, made by that signing authority (and by neither the VC issuer nor the Holder, unless the tamper signature can be independently demonstrated to be either the issuer or holder).

* [Add Your VC-EDU Use Cases](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0296.html)  Kerri Lemoie (Friday, 30 July)

For Github users, submit your use cases as issues here: [https://github.com/w3c-ccg/vc-ed-use-cases/issues](https://github.com/w3c-ccg/vc-ed-use-cases/issues)

This template can help guide you: [https://github.com/w3c-ccg/vc-ed-use-cases/blob/main/.github/ISSUE_TEMPLATE/use-case-template.md](https://github.com/w3c-ccg/vc-ed-use-cases/blob/main/.github/ISSUE_TEMPLATE/use-case-template.md)

* [Question About Signatures & Contexts](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0290.html)  Kerri Lemoie (Friday, 30 July)

Is a VC still considered to be valid if it contains fields that are not described in its context file(s)? Does it depend on the signature type?

* [Re: Question About Signatures & Contexts](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0291.html) Manu Sporny

The short answers are "maybe" and "yes".

* [What are VCs similar to?](https://lists.w3.org/Archives/Public/public-credentials/2021Aug/0338.html) Michael Herman (Trusted Digital Web) (Monday, 23 August)

The chip in your e-passport is the analogy I’ve been most successful with

An issuer gives it to you.

You carry it around and show to whom you choose

The verifier can check its integrity without contacting the issuer

“A VC is like the chip in your passport - bit for any document type”

So far the best analogy I’ve found.  Policy makers say “ah, I see”…

Video [Using Paper-based Structured Credentials to Humanize Verifiable Credentials [Rough Cut]](https://www.youtube.com/watch?v%3DkM30pd3w8qE%26list%3DPLU-rWqHm5p45dzXF2LJZjuNVJrOUR6DaD%26index%3D2) Michael Herman (Trusted Digital Web) (Friday, 19 November)

User Scenario: ABC Grocery wants to use the Trusted Digital Web to issue a Purchase Order for 10 cabbages from David's Cabbages.

* [Any Good use case of PAM (Privileged account Management) using Vcs](https://lists.w3.org/Archives/Public/public-credentials/2021Nov/0028.html) Bob Wyman (Sunday, 7 November)

A common example of this is when someone uses a "Power of Attorney," to sign a contract. When they do, they typically sign documents with their own names and an annotation "on behalf of," "for," or "by power of attorney," they don't forge the signature of the one who granted the power of attorney.

One should delegate rights, not credentials.

* [Proposal: Anchored Resources and Hashlinks for VCs](https://lists.w3.org/Archives/Public/public-credentials/2021Nov/0009.html) Dmitri Zagidulin (Wednesday, 3 November)

Note that this is different than binding multiple credentials together in a Verifiable Presentation (and having the presenter sign the VP). In the VP case, the binding just means "this presenter is authenticating the handing over of these unrelated credentials". Whereas in the linked VC case, the credentials are aware of each other, and the peer or hierarchical relationship is built into the VC itself.

* [re: Wrapping a VC envelope around the results of a GraphQL query?](https://lists.w3.org/Archives/Public/public-credentials/2021Dec/0093.html) Michael Herman (Trusted Digital Web) (Friday, 17 December)

Apparently so… [Evaluating the Current State of Application Programming Interfaces for Verifiable Credentials](https://www.researchgate.net/publication/356195214_Evaluating_the_Current_State_of_Application_Programming_Interfaces_for_Verifiable_Credentials)

* [Blockcerts v3 release, a Verifiable Credentials implementation](https://lists.w3.org/Archives/Public/public-credentials/2021Dec/0051.html)  Julien Fraichot (Monday, 13 December)

I am excited to share with you today the release of [Blockcerts](https://www.blockcerts.org/) V3. As you may already know the earlier versions of Blockcerts were architected by Kim H. Duffy through Learning Machine and leveraged the Open Badge standard.

We have followed through with the initial [ideas established at RWOT 9 in Prague in December 2019, to align Blockcerts with the Verifiable Credential specification](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/final-documents/BlockcertsV3.md).

* [Proposal Work Item | Credential Chaining](https://lists.w3.org/Archives/Public/public-credentials/2022Jan/0235.html)  Robin Klemens (Thursday, 27 January)

* to provide an overview of all existing flavors of credential chaining (What current and new techniques exist or are being researched?)

* to gather the reasons and requirements for credential chaining

* to come up with best practices and create a sort of decision tree that helps map the requirements of the use case with the implementation of credential chaining

* to provide working code with concrete implementations on different chaining variants

* to integrate credential chaining into future versions of the Verifiable Credentials Data Model

* [DIF VC-JWTs look like Linked Data Proof Verifiable Credentials](https://lists.w3.org/Archives/Public/public-credentials/2022Feb/0138.html)  Orie Steele (Thursday, 24 February)

As far as I know, no other VC-JWT implementation supports this format, aka "JwtProof2020".

* [Here is a link to an issue with an example](https://github.com/centrehq/verite/issues/373%23issuecomment-1049888568)

If you have a few minutes, I would love some review of what the DIF implementation is doing, and how we can either push it all the way into the LD Proof camp, or all the way into the VC-JWT camp.

* [re: Recommendations for Storing VC-JWT](https://lists.w3.org/Archives/Public/public-credentials/2022Feb/0076.html)  David Chadwick (Thursday, 17 February)

as you know we spent quite some time on the text in the VC Data Model v1.1 to differentiate between a credential and a verifiable credential, and to highlight that regardless of the proof format (JWT, LD-Proof etc) the credential is always the same once the proof has been removed.

Therefore the obvious way to me to store any type of VC in a wallet is to store the credential as JSON, along with the proofed VC,  then the same wallet will be able to receive any type of proofed VC and store the embedded credential in the same way. I have also been highlighting this model in the DIF PE group, so that the same Presentation Definition can be used by any wallet to select any type of credential, regardless of the proof type.

* [re: cloud-based wallet](https://lists.w3.org/Archives/Public/public-credentials/2022Mar/0285.html)  Orie Steele (Saturday, 26 March)

If the VCs in the cloud are a commitment to a DID instead of a hardware bound key... then their presentation from hardware bound keys achieves the same effect, but if the device is lost, the holder just registers new device bound keys, and no need to re-issue the VCs (but a DID Update operation is required).

* [usage of credentialSubject WITHOUT id?](https://lists.w3.org/Archives/Public/public-credentials/2022Mar/0017.html)  Niels Klomp (Sunday, 6 March)

Indeed the use case is for so called [bearer credentials](https://www.w3.org/TR/vc-data-model/%23bearer-credentials). The example of a concert ticket mentioned in there is a good one, although the actual bachelor degree example nr 33 is questionable since a degree is not subject independent.  That seems to come more from the fact that the degree is used throughout the spec as an example.

* [Verifiable Web Form](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0115.html)  Shigeya Suzuki (Saturday, 23 April)

This document proposes Verifiable Web Forms -- a new way to provide Verifiable Credentials [VC-DATA-MODEL] to Web Browser via Clipboard. By using Verifiable Web Forms, users can provide third-party verified data with standard user interfaces without typing. The data is also verifiable on the server-side too.

* [Your Insights, Assumptions, & Questions About VC Governance & Registries Needed](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0107.html)  Kerri Lemoie (Wednesday, 20 April)

I’ve created a Miro board as a place to start gathering questions and assumptions:

* [https://miro.com/app/board/uXjVO8bG_9s=/](https://miro.com/app/board/uXjVO8bG_9s%3D/)

* [VC Extensions Registry updates](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0096.html)  Manu Sporny (Saturday, 16 April)

I've made a pass at updating the registry to be more helpful to people and organizations that are not involved in the week-to-week with VCWG or CCG. The update, which adds proof methods, links to specs, implementations, and test suites can be found here:

* [https://pr-preview.s3.amazonaws.com/w3c-ccg/vc-extension-registry/pull/12.html#proof-methods](https://pr-preview.s3.amazonaws.com/w3c-ccg/vc-extension-registry/pull/12.html%23proof-methods)

The pull request[4] involves a few things that are worth noting

* [VC Issuance based on OAuth 2.0](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0084.html)  Nikos Fotiou (Thursday, 14 April)

We design, implement, and evaluate a solution for achieving continuous authorization of HTTP requests exploiting Verifiable Credentials (VCs) and OAuth 2.0. Specifically, we develop a VC issuer that acts as an OAuth 2.0 authorization server, a VC verifier that transparently protects HTTP-based resources, and a VC wallet implemented as a browser extension capable of injecting the necessary authentication data in HTTP requests without needing user intervention.
* [VC Spec Enhancement Proposal](https://github.com/SmithSamuelM/Papers/blob/master/whitepapers/VC_Enhancement_Strategy.md) Sam Smith

the VC standard appears to be an adoption vector for Linked Data, not the other way around. My overriding interest is that the concept of a VC as a securely attributable statement is a very powerful and attractive one and therefore should be widely adopted. We should therefore be picking the best technologies that best support broad VC adoption, not the other way around.


* [Verifiable Credentials Data Model v1.1 is an official W3C standard!](https://lists.w3.org/Archives/Public/public-credentials/2022Mar/0005.html)  Manu Sporny (Thursday, 3 March)

Verifiable Credentials Data Model v1.1 [https://www.w3.org/TR/2022/REC-vc-data-model-20220303/](https://www.w3.org/TR/2022/REC-vc-data-model-20220303/)

This was largely a maintenance release of the specification. The list of (minor) revisions since the v1.0 release can be found here:

* [VC Evidence Discussion](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0050.html)  Kerri Lemoie (Thursday, 7 April)

This evidence could be a test score, a link to an image, video, and/or web page, etc. that demonstrates competency or participation. These specs are working towards aligning with VCs and it was originally thought that this type of evidence would be included as part of the credentialSubject if it existed.

This would look [something like this](https://json.link/21SpTf0rC4):

But since VCs already have an evidence property that allows for an array of evidence, it seems to make sense to use that property instead of using a separate property like the one demonstrated above.

* [Rendering Verifiable Credentials @ RWoT11](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0054.html)  Manu Sporny (Sunday, 17 July)

This draft Rebooting the Web of Trust 11 paper explores ways in which the Verifiable Credentials data model could be extended to support visual, audio, and physical renderings for Verifiable Credentials.

* [https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/rendering-verifiable-credentials.md)

VC-API

* [Supporting VC-JWT and BBS+ Presentation Exchange in the VC-HTTP-API](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0313.html)  Orie Steele (Saturday, 31 July)

* [https://github.com/OR13/GNARLY](https://github.com/OR13/GNARLY)  (while we wait for a better name...)

This demo API and Spec has a number of improvements over the current

VC-HTTP-API, including tested support for VC-JWT, JsonWebSignature2020 and

BBS+ Selective Disclosure Presentation Exchange.

* [Updated VC-API diagram for Supply Chain flow](https://lists.w3.org/Archives/Public/public-credentials/2021Sep/0141.html)  Joe Andrieu (Tuesday, 28 September)

![https://www.notion.soimages/image4.png](https://www.notion.soimages/image4.png)

* [re: VC API: handling large documents client to server](https://lists.w3.org/Archives/Public/public-credentials/2022Feb/0035.html)  Manu Sporny (Thursday, 10 February)

Typical solutions to this problem require that you put the binary data outside of the VC, if at all possible. This works well for common static images such as logos. It is also possible to split the VC into two VCs... one with the machine-readable data from the issuer (with a digital signature) and one with the image data from any source (without a digital signature, since, if hashlinked, the signature will verify the validity of the image data). That latter approach can be more privacy preserving AND more complex than many might feel is necessary.

* [VC-API interoperability test suites ready for experimental integration](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0126.html)  Manu Sporny (Tuesday, 26 April)

* [The VC API test suite for basic issuer interop is here](https://w3c-ccg.github.io/vc-api-issuer-test-suite/)

* [The VC API test suite for basic verifier interop is here](https://w3c-ccg.github.io/vc-api-verifier-test-suite/)

* [The Data Integrity test suite for Ed25519Signature2020 interop is here](https://w3c-ccg.github.io/di-ed25519-test-suite/)

* [Cross-industry VC API test suite achieves first multi-vendor interop for issue/verify](https://lists.w3.org/Archives/Public/public-credentials/2022May/0041.html)  Manu Sporny (Wednesday, 18 May)

We are happy to announce today that we have our first demonstration of cross-vendor interoperability between Danube Tech and Digital Bazaar for the VC Issuer API and VC Verifier API. The test suites test the OAS definition files (which are used to generate the specification):

* [https://w3c-ccg.github.io/vc-api-verifier-test-suite/#Verify%20Credential%20-%20Data%20Integrity](https://w3c-ccg.github.io/vc-api-verifier-test-suite/%23Verify%2520Credential%2520-%2520Data%2520Integrity)

* [https://w3c-ccg.github.io/vc-api-issuer-test-suite/#Issue%20Credential%20-%20Data%20Integrity](https://w3c-ccg.github.io/vc-api-issuer-test-suite/%23Issue%2520Credential%2520-%2520Data%2520Integrity)

* [Diagrams for VC HTTP API work [was Re: [AGENDA] VC HTTP API Work Item - August 17th 2021]](https://lists.w3.org/Archives/Public/public-credentials/2021Aug/0231.html)  Joe Andrieu (Monday, 16 August)

1. There are sequence and communications diagrams for both issuance and verification, plus a class diagram.

![https://www.notion.soimages/image3.png](https://www.notion.soimages/image3.png)

* [VC-HTTP-API new sequence diagram](https://lists.w3.org/Archives/Public/public-credentials/2021Sep/0109.html)  Joe Andrieu (Tuesday, 21 September)

![https://www.notion.soimages/image6.png](https://www.notion.soimages/image6.png)

* [Issuer API Cross Trust Boundary Scoping - VC-HAPI (f.k.a. VC-HTTP-API)](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0263.html)  Brian Richter (Saturday, 24 July)

I think I'm starting to understand how RAR fits into this picture. This decision can be made for us by punting the question to the authorization process entirely. With RAR we can force the user to authorize for the actual subject they are issuing the credential about. Is Alice authorized to issue VCs with claims about did:example:12345? To answer that question Alice asks for a token with the following RAR request

* [RAR Structures for VC HTTP API](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0208.html)  Justin Richer (Wednesday, 21 July)

It seemed like a good idea when I first invented it a decade ago: [](https://blue-button.github.io/blue-button-plus-pull/%23scopes)[https://blue-button.github.io/blue-button-plus-pull/#scopes](https://blue-button.github.io/blue-button-plus-pull/%23scopes) or when it got pulled into other efforts like [](https://openid.net/specs/openid-heart-fhir-oauth2-1_0-2017-05-31.html)[https://openid.net/specs/openid-heart-fhir-oauth2-1_0-2017-05-31.html](https://openid.net/specs/openid-heart-fhir-oauth2-1_0-2017-05-31.html)… and Orie even suggested the following set of parameterized scopes for this API:

'create:credentials': Grants permission to create credentials

'derive:credentials': Grants permission to derive credentials

'create:presentations': Grants permission to create presentations

'verify:presentations': Grants permission to verify presentations

'exchange:presentations': Grants permission to exchange presentations

So what’s the problem? I can say with full confidence after years of experience building and deploying systems to support parameterized scopes like this that they are fragile, awkward, and lead to insecure corner cases.

* [Proposals addressing discoverability issues with vc-http-api](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0192.html)  Orie Steele (Tuesday, 20 July)

See: [https://github.com/w3c-ccg/vc-http-api/issues/218](https://github.com/w3c-ccg/vc-http-api/issues/218)

Proposal 1: The APIs that use OAS3.0 MUST define securitySchemes per the OAS 3.0 spec. (@OR13 proposal addresses 4)

Proposal 2: The APIs that use OAS3.0 MUST define the use of the Link Header for suite and issuer id discovery (@TallTed 's proposal addressing 1/2/3)

Proposal 3: The APIs that use OAS3.0 MUST define the use of a .well-known JSON resource for conveying supported issuer ids and suites. (@OR13 's. proposal addressing 1/2/3)

* [Bikeshed: Renaming the VC HTTP API](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0131.html)  Manu Sporny (Saturday, 17 July)

the fundamental issue is that stringing a bunch of consonants together ("HTTP") rarely leads to something easy to say in conversation.


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

* [What are Verifiable Credentials](https://academy.affinidi.com/what-are-verifiable-credentials-79f1846a7b9)
* [How W3C Verifiable Credentials (VC) Work: Part 1 – Issuance](https://blockster.global/self-sovereign-identity/)
  > When an issuer creates a verifiable credential, it contains following information –
  > 
  > - Who has issued – DID of the Issuer
  > - To whom it is issued – User Identifier
  > - Attributes of the credential – Details of the credential being Issued
  > - When it is Issued – Date of issuance
  > - Credential proof with Issuer signature that makes it tamper evident
  > - Revocation details
* [The Role of Witness Organizations in Verifiable Credentials](https://medium.com/@m.ruminer/on-the-role-of-witness-organizations-in-self-sovereign-identity-or-vcs-aren-t-just-p2p-e2cbafce6928)
  >  The basis is that not every source of a verifiable credential has an interest in issuing verifiable credentials and that it is not only logical but beneficial to the ecosystem of trust that witness organizations will issue on behalf of these sources.
* [An introductory dive into VCs (verifiable credentials)](https://hackernoon.com/understanding-the-verifiable-credentials-vcs-it1535e9) HackerNoon
  > Verifiable Credentials heavily utilize Decentralized Identifiers to identify people, organizations, and things and to achieve a number of security and privacy-protecting guarantees. They are issued and cryptographically signed documents, intended to be understood by computers rather than people.
* [How Does a Verifier Know the Credential is Yours?](https://www.evernym.com/blog/how-does-a-verifier-know-the-credential-is-yours/) Evernym
  > A link secret is a large random number, wrapped in a way that allows the holder to prove that they know the secret.
* [Introduction to Verifiable Credentials](https://www.ubisecure.com/identity-management/verifiable-credentials/) Ubisecure
  > The Verifiable Credentials specification is quite new, and many pieces that are required to create interoperable solutions are still incomplete or missing at time of writing. However, there is significant momentum around verifiable credentials (VCs). This is partly attributed to VCs being part of the solution for blockchain-based decentralised identity.
* [8 Reasons to use Verifiable Credentials](https://academy.affinidi.com/8-reasons-to-use-verifiable-credentials-300833276b52) Affinidi
  > VCs are interoperable across many systems and can be used in almost every possible scenario.
* [What are Verifiable Credentials in 3 Minutes](https://www.youtube.com/watch?v%3Ds5h7OgmnrxE) Affinidi (video)
* [The VC Lifecycle](https://credentialmaster.com/the-vc-lifecycle/) Credential Master
  > In 1956 the switch to consistent shipping containers began, and it changed the physical world [profoundly](https://www.economist.com/finance-and-economics/2013/05/18/the-humble-hero); the switch to consistent, authenticatable digital data containers [will do the same for cyberspace](https://rufftimo.medium.com/like-shipping-containers-verifiable-credentials-will-economically-transform-the-world-fece2b9da14a).
* [Verifiable Credentials Aren’t Credentials. And They’re Not Verifiable In the Way You Might Think](https://credentialmaster.com/verifiable-credentials-arent-credentials-theyre-containers/) Timothy Ruff
  > think “authenticatable data container” [...]
  > 
  > VCs can carry any sort of data payload, and that isn’t just a good thing, it’s a great one. [Part two](https://medium.com/@rufftimo/like-shipping-containers-verifiable-credentials-will-economically-transform-the-world-fece2b9da14a) of my container series covers how such fluid data portability could economically affect cyberspace to a degree comparable to how shipping containers affected global trade.
* [Verifiable credentials are key to the future of online privacy](https://www.helpnetsecurity.com/2021/07/26/verifiable-credentials/) HelpNetSecurity
  > - All the data is decentralized, meaning there’s no need for a database of student records that could be jeopardized. Alice’s data lives with her.
  > - The employer doesn’t need to keep a copy of Alice’s transcript to verify her education.
  > - The college doesn’t play intermediary and doesn’t have access to the list of organizations Alice shares her data with. Other parties have no way of correlating this data as each exchange is private and unique.
  > - If desired, Alice could pick and choose what she wants to share. She could prove her degree without sharing her date of graduation or GPA, for example.
* [What are Verifiable Credentials?](https://medium.com/affinidi/what-are-verifiable-credentials-79f1846a7b9)
  > At the most basic level, verifiable credentials, or VC in short, are tamper-proof credentials that can be verified cryptographically.
* [Self Attested vs Chain of Custody - assurance levels in data provenance in VCs](https://iiw.idcommons.net/23G/_Self_Attested_vs_Chain_of_Custody_-_assurance_levels_in_data_provenance_in_VCs) by Stew Whitman & Alka Lachhwani
  > There are two important factors in establishing “truth” or the trustworthiness of the information. Attributional and Reputational. You need to have both to have trust.
  > 
  > Digital needs higher level of attestation because it is easier to forge and easier to propagate that forgery.

## Comparisons with/ other Tech
* [Compare and Contrast: OpenBadges vs Verifiable Credentials](https://academy.affinidi.com/compare-and-contrast-openbadges-vs-verifiable-credentials-d504c054d5db) Affinidi 
  > As we move towards a world of digital identity, many ways of sharing and verifying Personally Identifiable Information are emerging. Two such modes that we’ll talk about today are Open Badges and Verifiable Credentials.
* [Non-Fungible Tokens (NFTs) vs Verifiable Credentials (VCs)](https://academy.affinidi.com/non-fungible-tokens-nfts-vs-verifiable-credentials-vcs-cd0ebb13f1fb) Affinidi
  > A common thread that connects both NFTs and VCs is that they leverage the potential benefits of the digital world to give users more security, flexibility, and freedom to monetize.
* [ERC-721 Non-Fungible Token Standard on Ethereum vs. VCs on Hyperledger Indy](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0059.html) Michael Herman
  > When are Hyperledger Indy/Sovrin VCs better than Ethereum smart contracts for NFEs/NFTs (non-fungible entities/tokens)?
  > 
  > It seems obvious but I don't have a detailed/worked out answer.  One project I'm associated with wants to use the [ERC-721 Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) on Ethereum but I believe VCs are a better route to take. Part of the desire to stay on Ethereum is there is quite a vibrant NFT community on Ethereum and lots of different EC-721 tokens.
* [Comparing VCs to ZCAP-LD](https://kyledenhartog.com/comparing-VCs-with-zcaps/) Kyle Den Hartog
  > Why make the investment then to put the time and effort into ZCAPs when we’ve already got VCs? Simply put because security is hard and trying to push square pegs into round holes often times leads to bugs which are elevated to mission critical authentication/authorization bypass vulnerabilities. By designing around a fit for purpose data model with a well defined problem being solved it allows for us to be much more precise about where we believe extensibility is important versus where normative statements should be made to simplify the processing of the data models. By extension this leads to a simpler security model and likely a much more robust design with fewer vulnerabilities.
* [Compare and Contrast — IRMA vs Verifiable Credentials](https://academy.affinidi.com/compare-and-contrast-irma-vs-verifiable-credentials-58e4b30d85f1)
- [Re: VCs - zCaps / OCap a Discussion](https://lists.w3.org/Archives/Public/public-credentials/2020Dec/0027.html) Dave Longley 12/5
  > TL; DR: My current view is that the main confusion here may be over the difference between VCs and LD Proofs, not VCs and ZCAPs. VCs are not a generalized container for attaching a cryptographic proof to a document. That's what LD proofs (or JOSE style proofs) are for. VCs *use* LD proofs (or JOSE style proofs) to attach an assertion proof to a document that specifically models statements made by an issuer about some subject, which is therefore inherently about the identity of that subject.
* [Could an NFT be a VC?](https://iiw.idcommons.net/20I/_Could_an_NFT_be_a_VC%253F) by Grace Rachmany
  > Case discussed: A group of villages in Africa using a cryptocurrency platform for alternative currencies. Different organizations issue the coins under different circumstances. When you accept a currency, you want to know who is the issuer. The Red Cross might be more or less trusted than the local leader or agricultural cooperative as the issuer of a currency that is supposedly equivalent to a shilling.
  > 
  > What types of tech could be used for this?
  > 
  > - Multiple currencies on the blockchains
  > - Certifications in the form of some kind of NFT issued by the issuer.
  > - Limited supply tokens or NFTs that are “expired” when you use them
  > - Open Credential Publisher framework was suggested
  > - VCs are generally authorizations associated with a person, so maybe a person could have the VC and show their credit rating in some way while they are making a transaction
  > - Similarly maybe the VC belongs to the organization that is issuing the coin, proving its reputation over time.
* [How does VC Functional Stack compare to #ToIP Stack?](https://twitter.com/rufftimo/status/1301314001251438593) @rufftimo
  > 1. ToIP Layers 2 & 3 compare to Functional Layer 2
  > 2. ToIP Layer 4 compares to Functional Layers 3 & 4 (horizontal layer for VC Management, vertical layer for Applications)
  > 3. Functional stack doesn't require #blockchain
  > 4. Functional Stack doesn't detail steps for trust or verification; ToIP Stack doesn't separate management or storage
  > 5. Functional Stack clarifies functions, roles, and potential business models; ToIP stack clarifies trust & security They are complementary, not contradictory.
  > ![](https://i.imgur.com/8zakrMQ.png)

## HowTo
* [Example Design of an Authorization System with Verifiable Credentials and the Tradeoffs](https://kyledenhartog.com/example-authz-with-VCs/) Kyle Den Hartog
  > The primary focus of this blog post is to highlight the different problems that are likely to occur when going down the path of building an authorization system with verifiable credentials. I’ll be sure to keep things at a higher level so that anyone can understand these tradeoffs, but take you through the details that would be thought through by an architect designing the system.
* [Managing VCs at scale & the VC Stack](https://iiw.idcommons.net/index.php?title%3D12L/_Managing_VCs_at_Scale_%2526_the_VC_Stack%26action%3Dedit%26redlink%3D1) by Timothy Ruff & Alan Davies


## Organization
* [W3C Verifiable Credentials Education Task Force 2022 Planning](https://kayaelle.medium.com/w3c-verifiable-credentials-education-task-force-2022-planning-efc9b07cc2a3) Kerri Lemoie

We’ve been hard at work writing use cases, helping education standards organizations understand and align with VCs, and we’ve been heading towards a model recommendation doc for the community.

## History

* [The original #VerifiableCredentials were PKI-based SIM cards and EMV cards.](https://twitter.com/Steve_Lockstep/status/1419935186188341249) @Steve_Lockstep
  > These bind key pairs to individuals, and to signed assertions (account numbers) to deliver provenance, fidelity and proof of possession. [https://constellationr.com/blog-news/not-too-much-identity-technology-and-not-too-little](https://constellationr.com/blog-news/not-too-much-identity-technology-and-not-too-little)
  > ![](https://i.imgur.com/ucAVxCX.png)

## Use

* [Better digital living with blockchain-backed verifiable credentials](https://thepaypers.com/expert-opinion/better-digital-living-with-blockchain-backed-verifiable-credentials--1250869) The Paypers
  > The NHS can now provide you with a digital verifiable credential to prove your vaccination status, securely stored in the NHS app and easily accessible, generating a QR code to prove to airlines and employers that you are fit to fly or work. But this is just the first step in the development of an enabling technology that can bring benefits to many areas of modern life.
* [On Climate Crisis and Self-Sovereign Verifiable Career Credentials](https://www.velocitynetwork.foundation/on-climate-crisis-and-self-sovereign-verifiable-career-credentials/) Velocity Network
  > This rich verifiable self-sovereign career identity will be the ‘great transformer’ of the global labor market. It will change the way people navigate their careers and livelihoods, and how employers make talent decisions.
* [The World of Anonymous Credentials](https://blog.dock.io/anonymous-credentials/) Dock
  > A credential is called a verifiable credential when its authenticity can be cryptographically checked by anyone because the credential contains a cryptographic signature by the issuer, and the issuer's public key is well known.
* [WHY THRIVACY?: Think about it. What did you leave behind when you bought the last round of drinks.](https://www.thrivacy.io/why-thrivacy)
  > Your Thrivacy wallet allows you to request all your important, personal information that can be used to identify who you are to be created into what we call verified credentials. Then those same verified credentials or VCs can be downloaded and stored in your own personal wallet that is kept inside your cell phone.
* [25 Use Cases for Verifiable Credentials](https://drive.google.com/file/d/1BrFjh6-TVkJ4Rfllh5fUTjh6hkYtPbR_/view) LTO Network and Sphereon
* [Verifiable Credentials For Travel & Hospitality](https://www.youtube.com/watch?v%3DXxd56y2mhFQ) Evernym
  > verifiable credentials and digital wallets can reduce fraud, automate workflows, and transform customer experiences across the travel and hospitality industries.
* [The Power of Verifiable Credentials](https://credentialmaster.com/the-power-of-vcs/) Credential Master
  For the first time ever, data from one ecosystem can be instantly authenticated in any other, online or off, without a direct connection to the source.
* [Verifiable Credential Notarization and Third-Party Notary Services Providers: User Scenarios](https://lists.w3.org/Archives/Public/public-credentials/2021Jul/0109.html) Michael Herman 7/15
* [Verifiable Credentials for Authentic Data in the Supply Chain](https://iiw.idcommons.net/10G/_Verifiable_Credentials_for_Authentic_Data_in_the_Supply_Chain) by Gena Morgan, Kevin Dean
  > Using DiDs and VCs for verifiable product data in supply chains, leveraging the largest supply chain standard system in the world,
  > 
  > 2.5 million users companies, over 6 billion product scans per day
  > 
  > Product data and attestations from a number of various authoritative sources
  > 
  > Leverage DIDs/VCs for distributed data sharing, verification
* [IIW verifiable credentials - Decentralized VC integration with Eventbrite and Qiqo chat. This session will review the implementation process, lessons learned, and community discussion on related use cases.](https://iiw.idcommons.net/11A/_IIW_verifiable_credentials_-_Decentralized_VC_integration_with_Eventbrite_and_Qiqo_chat._This_session_will_review_the_implementation_process,_lessons_learned,_and_community_discussion_on_related_use_cases.) by Mike Vesey, Karl Kneis
* [Verifiable Credentials for Assets <30 min](https://iiw.idcommons.net/21E/_Verifiable_Credentials_for_Assets_30_min) by Mahmoud Alkhraishi
  > General Framework on how to think of VCs for Assets including leveraging GS1 and other vocabularies in the traceability vocab.
  > 
  > Requirements and Opportunities that block adoption of VCs in Supply chains
  > * [Traceability Vocabulary v0.0](https://w3c-ccg.github.io/traceability-vocab/)
  > * [VC HTTP API (0.0.2-unstable)](https://w3c-ccg.github.io/vc-http-api)
  > * [Status List 2021](https://w3c-ccg.github.io/vc-status-list-2021/)
* [Credential-based login to a Pico-based application](https://iiw.idcommons.net/11P/_Credential-based_login_to_a_Pico-based_application) by Bruce Conrad
  > Verifiable credentials, authentication, picos, pico-based application
  > 
  > The slides are at [https://bruceatbyu.com/s/HRDDSiiw32](https://bruceatbyu.com/s/HRDDSiiw32)

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
* [What BBS+ Means For Verifiable Credentials](https://www.youtube.com/watch?v%3DdXlRIrrb9f4) Evernym
  > In a recent Evernym blog post, [we discussed why BBS+ LD-Proofs](https://www.evernym.com/blog/bbs-verifiable-credentials/) are the privacy-preserving VC format that everyone should implement. In this webinar….
  > - A brief history of verifiable credential formats, and how a lack of convergence makes scale and interoperability an ongoing challenge
  > - How BBS+ Signatures are the breakthrough that combine the best of the JSON-LD and ZKP formats, while still allowing for selective disclosure and non-trackability
  > - The path forward: What remains to be done to fully converge on the BBS+ format

## Critique

Thread: VCs need Threat Modeling

* [Thread started by Pamela Dingle](https://twitter.com/pamelarosiedee/status/1537233243086327812?s%3D20%26t%3DWWt14_H4AXgtn09xb5-yew)
  > Another pre-read recommendation for @identiverse: the @openid for Verifiable Credentials Whitepaper.  It is a great high level explanation of decentralized benefits and use cases, both @kristinayasuda & @tlodderstedt contributed! OpenID for Verifiable Credentials
    * [Firstyear Replying to @Erstejahre @pamelarosiedee and 4 others](https://twitter.com/Erstejahre/status/1537615778106658816)
      > It also seems to lack any sections about threat modelling and possible risks, making it hard to trust since risks are not directly and clearly addressed.
    * [Torsten Lodderstedt Replying to @Erstejahre @pamelarosiedee and 3 others](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)
      > I agree. We [threat] model while we are designing the protocol, we also need to add it to the spec. Please note: we build on existing work. There is an extensive thread model for OAuth and countermeasures that we built on ([datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics). Feel free to contribute.
