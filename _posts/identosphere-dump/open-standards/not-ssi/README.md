# Non SSI Identity Standards

## Contents

- OpenID
- FIDO
- OAuth
- SCIM
- SAML
- KMIP
- Secure QR Code

## OpenID


* [Registration - OpenID Foundation Virtual Workshop](https://openid.net/2021/03/01/registration-open-for-openid-foundation-virtual-workshop-april-29-2021/) April 29, 2021

updates on all active OpenID Foundation Working Groups as well the OpenID Certification Program
OpenID Specs Up for Review

* [Public Review Period for Second Proposed RISC Profile Implementer’s Draft](https://openid.net/2022/07/05/public-review-period-for-second-proposed-risc-profile-implementers-draft/)

This specification defines event types and their contents based on the [SSE Framework](https://openid.net/specs/openid-risc-profile-specification-1_0-02.html%23SSE-FRAMEWORK) that are required to implement Risk Incident Sharing and Coordination.

## FIDO

* [2021 FIDO Developer Challenge: Outcomes and Winners](https://fidoalliance.org/2021-fido-developer-challenge-outcomes-and-winners/)

1. Gold Winner – [Lockdrop](https://lockdrop.com/)
2. Silver Winner – [Shaxware](https://www.shaxware.com/)
3. Bronze Winner – SoundAuth ([Trillbit](https://www.trillbit.com/)

This year’s FIDO Developer Challenge reached a successful conclusion, with a ceremonial event during [Authenticate 2021](https://authenticatecon.com/event/authenticate-2021-conference/) of the ceremony is available now, and we’re pleased to share more detailed stories of the three finalists as well as the rest of the teams that made it to the final stage.
* [Integrating FIDO with Verifiable Credentials (8.30 am start)](https://iiw.idcommons.net/10E/_Integrating_FIDO_with_Verifiable_Credentials_(8.30_am_start)) by David Chadwick

* [The Use of FIDO2 and Verifiable Credentials (David Chadwick)](https://youtube.com/watch?v%3Dl3taGxBdrRU)

W3C Web Authentication (FIDO2) provides a mechanism for strong authentication whilst W3C Verifiable Credentials provide a mechanism for strong identification and authorisation. Together they make an unbeatable pair for identity management.

Prof. David Chadwick presented work on sharing W3C Verifiable Crendentials via FIDO2 key setup with issuers of credentials.  In a nutshell, the holder and issuer use the WebAuthN protocol to strongly authenticate before the issuer protects the credentials with its signature.  Upon providing credentials to a relying party, the issuer (acting in an IDP capacity, so they must be online) will verify the identity of the holder via FIDO2 WebAuthN so that the credentials (or selected claims in the credentials for selective disclosure) can be shared with the relying party.  Ephemeral keys are created to bind the holder with such credentials shared to the relying party/verifier.  The relying party/verifier can use X.509 certs to confirm that the issuer is valid by checking the signature on the derived credential from the holder.
* [Fido Passkey](https://www.pingidentity.com/en/resources/blog/post/how-fido-passkeys-accelerate-passwordless-future.html)
* * [What is FIDO? Infographic](https://www.scmagazine.com/resource/identity-and-access/what-is-fido)

- [How passkeys pave the way for passwordless authentication](https://www.scmagazine.com/resource/identity-and-access/how-passkeys-pave-the-way-for-passwordless-authentication)
* [FIDO: Everything You Need to Know About Fast Identity Online](https://www.pingidentity.com/en/company/blog/posts/2021/fast-identity-online-fido.html)
* [Use Fido2 Passwords Authentication with Azure AD](https://damienbod.com/2022/01/17/use-fido2-passwordless-authentication-with-azure-ad/) Damion Bod

This article shows how to implement FIDO2 passwordless authentication with Azure AD for users in an Azure tenant.
* [Charting an Accelerated Path Forward for Passwordless Authentication Adoption](https://fidoalliance.org/charting-an-accelerated-path-forward-for-passwordless-authentication-adoption/) FIDO

* [The paper introduces](https://media.fidoalliance.org/wp-content/uploads/2022/03/How-FIDO-Addresses-a-Full-Range-of-Use-CasesFINAL.pdf) multi-device FIDO credentials, also informally referred to by the industry as “passkeys,” which enable users to have their FIDO login credentials readily available across all of the user’s devices.
* [FIDO passkeys are an existential threat to fintech startups](https://werd.io/2022/fido-passkeys-are-an-existential-threat-to-fintech-startups)

by definition, screen scraping requires storing a user’s financial system passwords in clear text. Nonetheless, you can bet that every system that integrates with payroll systems, and almost every system that integrates with banks (at a minimum), uses the technique. The US has badly needed [open banking style standards](https://standards.openbanking.org.uk/api-specifications/) for years.
* [FIDO Alliance Supports Biden Administration EO on Cybersecurity](https://fidoalliance.org/fido-alliance-supports-biden-administration-eo-on-cybersecurity/)

There have been a number of high profile attacks against critical American infrastructure in recent months, including the Solarwinds supply chain attack that exposed much of the government to potential risk. Top of mind in recent days is the ransomware attack against Colonial Pipeline, which significantly impacted the flow of refined oil across America. These attacks expose the vulnerability of critical infrastructure in the United States, and the Biden Administration is issuing federal directives that will minimize or eliminate risk.


## OAuth

## SCIM

## SAML

## KMIP

## Secure QR Code

## RDF


## RDF

* [Technical Report on the Universal RDF Dataset Normalization Algorithm](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/att-0032/Mirabolic_Graph_Iso_Report_2020_10_19.pdf) - [Bill Bradley](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0032.html)
  > The goal of this technical report is to review the Universal RDF Dataset Normalization Algorithm (URDNA2015) for correctness and to provide satisfactory evidence that possible issues with URDNA2015 have been considered and dismissed. We do not lay out the algorithm in its considerable technical detail here, but refer the reader to the proposed technical specification 1 [Longley], a set of proofs by Rachel Arnold and Dave Longely [Arnold], and a reference implementation in Python [DigitalBazaar]

* [Importing Verifiable Data as Labeled Property Graphs](https://lists.w3.org/Archives/Public/public-credentials/2022Jun/0022.html)  Orie Steele (Wednesday, 15 June)

I think what happens is that a first blank node is created for the proof, and since that node has `@container` `@graph`, instead of being able to trace the relationships directly from credential to proof to verification method...

Each proof is being treated as a disjoint subgraph, and the relationship is not being preserved during import… [...]

I suspect this is solvable with a more complicated graph config: [https://neo4j.com/labs/neosemantics/4.0/config/](https://neo4j.com/labs/neosemantics/4.0/config/)

But I wonder if we might correct this behavior in VC Data Model 2.0, such that RDF representations don't have this odd behavior when imported as labeled property graphs. [...]

answer on the github issue for the standard, I raised it here: [](https://github.com/w3c/vc-data-model/issues/881)[https://github.com/w3c/vc-data-model/issues/881](https://github.com/w3c/vc-data-model/issues/881)

* [Proposed W3C Charter: RDF Dataset Canonicalization and Hash Working Group](https://lists.w3.org/Archives/Public/public-credentials/2022May/0033.html)  Manu Sporny (Tuesday, 17 May)

The goal of this group is to standardize the way many of us digitally sign Verifiable Credentials. This working group has been about decade in the making (some would say two decades) and is important for achieving things like BBS+ selective disclosure as well as standardizing the way we format Verifiable Credentials before they are digitally signed.

The [announcement](https://lists.w3.org/Archives/Public/public-new-work/2022May/0005.html) is here

The [proposed charter](https://www.w3.org/2022/05/04-proposed-rch-wg-charter/) is here

* [URDNA2015 Implementation Question](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0017.html)  Daniel Petranek (Thursday, 7 July)

I've instrumented the rdf-canonicalize library so I can inspect the order of execution, and it appears that what differs between my implementation and the Javascript one is the order of the permutations. The spec doesn't say how the permutations should be ordered, and my intuition is that the order does indeed matter - though I'm happy to be corrected if I'm wrong.

So, here is my question(s):

- Does the order of the permutations matter?
- If so, what order should they be in?

