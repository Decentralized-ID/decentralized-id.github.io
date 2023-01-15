---
published: false
---

# Crypto 


* [FYI: Cryptography Review and Recommendations for W3C VC and W3C DID Implementations by SRI International](https://lists.w3.org/Archives/Public/public-credentials/2022Jan/0209.html)  John, Anil (Wednesday, 26 January)

This type of independent review is critically important for U.S. Government entities who are deploying capabilities based on these standards to ensure that the technologies conform to relevant U.S. Federal government standards and requirements, including the Federal Information Security Management Act (FISMA) and National Institute of Technology (NIST) standards for use of cryptography.

Please find attached (and online at the link below) the results of this independent review and the associated cryptography implementation recommendations.

* [SRI-Cryptography Review and Recommendations  for W3C VCDM and W3C DID Standards.docx](https://docs.google.com/document/d/1EdCBSACtlBv2DxNZM67qi9F15Iv5uWOW/)

* [Blog on SSI and Cryptographically Enforceable Policies](https://lists.w3.org/Archives/Public/public-credentials/2022Feb/0032.html)  (Tuesday, 8 February)

I've posted a new SSI blog entitled: "[Protecting Sensitive Parts of Credentials with Cryptographically Enforceable Policies](https://blockchain.tno.nl/blog/protecting-sensitive-parts-of-credentials-with-cryptographically-enforceable-policies/)".

It has a proposal that enables credential issuers to encrypt sensitive parts of credentials in such a way that can only be decrypted by parties tha satisfy the issuer's policy (that was used to encrypt these parts). The blog motivates the need, introduces a high-level architecture, explains how it would work, and discusses some issues that need to be looked into.

* [Use of cryptography with W3C VCs and DIDs released](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0109.html)  Manu Sporny (Thursday, 21 April)

Cryptography Review of W3C Verifiable Credentials Data Model (VCDM) and Decentralized Identifiers (DIDs) Standards and Cryptography Implementation Recommendations by David Balenson & Nick Genise

* [http://www.csl.sri.com/papers/vcdm-did-crypto-recs/](http://www.csl.sri.com/papers/vcdm-did-crypto-recs/)

It's largely a view from the US NIST cybersecurity standards, which are used through most of the world, but not everywhere. In any case, it's a valuable perspective that I hope the VC2WG and DIDWG takes into the next stage of the work.

* [Universal signature verifier](https://lists.w3.org/Archives/Public/public-credentials/2022May/0005.html)  Marcus Sabadello (Wednesday, 4 May)

We (Danube Tech) have a "Universal Verifier" here: [https://univerifier.io/](https://univerifier.io/)

But I don't claim that it actually supports all the credential formats  and signature suites in existence...

Especially considering that at the last Internet Identity Workshop a lot of different formats were identified:

* [https://docs.google.com/document/d/1aNHvPhFv85HHlG8Ry2etrw15KdY830oAL804rMFY9bY](https://docs.google.com/document/d/1aNHvPhFv85HHlG8Ry2etrw15KdY830oAL804rMFY9bY/)

* [Updating SafeCurves for 2022...](https://lists.w3.org/Archives/Public/public-credentials/2022May/0048.html)  Manu Sporny (Tuesday, 24 May)

* [Guidance for Choosing an Elliptic Curve Signature Algorithm in 2022](https://soatok.blog/2022/05/19/guidance-for-choosing-an-elliptic-curve-signature-algorithm-in-2022/)

It suggests updates to the [SafeCurves website](https://safecurves.cr.yp.to/)

* [Cross-vendor interop for Data Integrity and Ed25519Signature2020 achieved](https://lists.w3.org/Archives/Public/public-credentials/2022May/0034.html)  Manu Sporny (Tuesday, 17 May)

We are happy to announce today that we have our first demonstration of cross-vendor interoperability between Danube Tech and Digital Bazaar for verification regarding the Data Integrity and Ed25519Signature2020 work items:

* [https://w3c-ccg.github.io/di-ed25519-test-suite/#Data%20Integrity%20(verifier](https://w3c-ccg.github.io/di-ed25519-test-suite/#Data%20Integrity%20(verifier)

* [https://w3c-ccg.github.io/di-ed25519-test-suite/#Ed25519Signature2020%20(verifier](https://w3c-ccg.github.io/di-ed25519-test-suite/#Ed25519Signature2020%20(verifier)

* [Streamlining Data Integrity Cryptosuites](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0115.html)  Manu Sporny (Sunday, 31 July)

* [2022-VCWG-Data-Integrity-Streamlining.pdf](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/att-0115/2022-VCWG-Data-Integrity-Streamlining.pdf)

![https://www.notion.soimages/image5.png](https://www.notion.soimages/image5.png)

* [Publication request for Data Integrity CGFRs](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0107.html)  Manu Sporny (Tuesday, 26 July)

This is a publication request for four Data Integrity Community Group

Final Reports. Namely:

* [Data Integrity](https://w3c.github.io/cg-reports/credentials/CG-FINAL-data-integrity-20220722/)

* [Data Integrity JSON Web Signature Cryptosuite 2020](https://w3c.github.io/cg-reports/credentials/CG-FINAL-lds-jws2020-20220721/)

* [Data Integrity ECDSA Cryptosuite 2019](https://w3c.github.io/cg-reports/credentials/CG-FINAL-di-ecdsa-2019-20220724/)

* [Data Integrity EdDSA Cryptosuite 2020](https://w3c.github.io/cg-reports/credentials/CG-FINAL-di-eddsa-2020-20220724/)



* [ZK for Authentication With Nolan and Locke from NuID](https://www.zeroknowledge.fm/154) - ZeroKnowledge Podcast.
  > Universally Composable Direct Anonymous Attestation by Jan Camenisch , Manu Drijvers , and Anja LehmannPractical UC-Secure Delegatable Credentials with Attributes and Their Application to Blockchain by Jan Camenisch , Manu Drijvers , and Anja LehmannPrivacy-Preserving User-Auditable Pseudonym Systems by Jan Camenisch & Anja Lehmann IBM Research – Zurich

## Jose-Cose

* [Two new COSE- and JOSE-related Internet Drafts with Tobias Looker](https://self-issued.info/?p=2260) Mike Jones
  > This week, [Tobias Looker](https://twitter.com/tplooker) and I submitted two individual Internet Drafts for consideration by the [COSE working group](https://datatracker.ietf.org/wg/cose/about/).
* [XMSS: Generating usable test vectors for JOSE and COSE](https://lists.w3.org/Archives/Public/public-credentials/2022Apr/0007.html)  Orie Steele (Sunday, 3 April)

We've been working on generating test vectors for: [https://datatracker.ietf.org/doc/html/rfc8391](https://datatracker.ietf.org/doc/html/rfc8391) $1$2

That we could use to register the `kty` and `alg` for XMSS such that it could be used by JOSE and COSE.

## Quantum


* [Future-proofing VCs via multiple signatures](https://lists.w3.org/Archives/Public/public-credentials/2022Jan/0043.html)  Manu Sporny (Thursday, 6 January)

What this means is that it is now possible to not have to depend on one signature format, and instead use multiple to meet different needs. The VC above supports NIST-approved cryptography today, while enabling the advanced use of BBS+ (if an organization would like to use it /before/ it is standardized at IETF), and also enabling protection if a quantum computer were to break both Ed25519 and BBS+... all on the same VC in a fairly compact format.

* [re: New Work Item Incubating for IETF: JSON Encoding for Post Quantum Signatures](https://lists.w3.org/Archives/Public/public-credentials/2022Feb/0008.html)  Orie Steele (Tuesday, 1 February)

I look forward to continuing to work on JSON encoding for post quantum signature schemes.

In particular, support for JWS and JWK as building blocks for higher order cryptographic systems, such as DIDs and VCs.

If you are interested in contributing, please feel free to open issues here: [](https://github.com/mesur-io/post-quantum-signatures)[https://github.com/mesur-io/post-quantum-signatures](https://github.com/mesur-io/post-quantum-signatures)

* [Post Quantum and Related](https://lists.w3.org/Archives/Public/public-credentials/2022Jul/0010.html) Mike Prorock (Wednesday, 6 July)

* [NIST Announcement here](https://csrc.nist.gov/News/2022/pqc-candidates-to-be-standardized-and-round-4)

* [And a pretty good game plan from CISA with some timing implications here](https://www.cisa.gov/uscert/ncas/current-activity/2022/07/05/prepare-new-cryptographic-standard-protect-against-future-quantum)

The TLDR is to assume that we need hard answers as a community, and at the standards level, on crypto agility by 2024, as well as support for the key algorithms as listed above.

* [[CEIP] Draft paper on Cryptographically Enforceable Issuer Policies](https://lists.w3.org/Archives/Public/public-credentials/2021May/0170.html)  Joosten, H.J.M. (Rieks) May 30

my colleague Sterre and I drafted [a paper that we provisionally called Cryptographically Enforceable Issuer Policies](https://docs.google.com/document/d/1c8kIUqB2BBzM3usfD0_s5wu_z6K2KndzJ4uK_oZcPOs/edit?usp=sharing), which describes our current thinking on this topic.

The paper isn’t finished. We need more text in the ‘discussions’ section, and hope that by making the draft available we’ll get the discussions that we (or you?) can describe in there. Also, we might have missed stuff that you as a reader need for a proper understanding of what this is all about, and to start pondering for what (other) purposes all this might be used. Or why this proposal is a very bad idea that we should not spend any more time on.


