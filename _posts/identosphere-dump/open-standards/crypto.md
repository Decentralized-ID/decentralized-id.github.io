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

* [https://w3c-ccg.github.io/di-ed25519-test-suite/#Data%20Integrity%20(verifier](https://w3c-ccg.github.io/di-ed25519-test-suite/%23Data%2520Integrity%2520(verifier)

* [https://w3c-ccg.github.io/di-ed25519-test-suite/#Ed25519Signature2020%20(verifier](https://w3c-ccg.github.io/di-ed25519-test-suite/%23Ed25519Signature2020%2520(verifier)

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


* [Lightweight Credentials for Offers with UCAN](https://blog.fission.codes/lightweight-credentials-ucan/)

these are the types of use cases that we think can be created and enabled across the web as an open, interoperable standard. And some of it crosses into the work we're doing as [part of the Decentralized Identity Foundation](https://blog.fission.codes/fission-demo-day-may-2021/), too.

* [ZK for Authentication With Nolan and Locke from NuID](https://www.zeroknowledge.fm/154) - ZeroKnowledge Podcast.
  > Universally Composable Direct Anonymous Attestation by Jan Camenisch , Manu Drijvers , and Anja LehmannPractical UC-Secure Delegatable Credentials with Attributes and Their Application to Blockchain by Jan Camenisch , Manu Drijvers , and Anja LehmannPrivacy-Preserving User-Auditable Pseudonym Systems by Jan Camenisch & Anja Lehmann IBM Research – Zurich
* [What’s next for BBS+ LD-Proofs?](https://iiw.idcommons.net/13B/_What%2527s_next_for_BBS%252B_LD-Proofs%253F) by Brent Zundel

* [BBS+ Signatures 2020](https://w3c-ccg.github.io/ldp-bbs2020/)

- What’s next for BBS+ LD-Proofs?
- Implementation in Aries ([https://iiw.animo.id/](https://iiw.animo.id/), Used in SVIP Plugfest
- Implementation of BBS+ in Ursa, Core of higher level implementations
- Features
- Selective Disclosure
- Signature blinding
- Blinded messages (private holder binding)
- BBS+ LD Proofs uses this BBS+ scheme, MATTR provided spec
- Combine privacy features with semantic world
- Draft spec: [https://github.com/w3c-ccg/ldp-bbs2020/](https://github.com/w3c-ccg/ldp-bbs2020/)
- What needs to be refined?
- Private holder binding ([https://github.com/w3c-ccg/ldp-bbs2020/issues/37](https://github.com/w3c-ccg/ldp-bbs2020/issues/37)
- Do not bind to link secret, bind to keypair. Make keypair per credential
- How to participate?
- Read the draft BBS+ LD-Proofs spec
- Hardware security binding?
- Not possible with BLS yet?
- Is post-quantum secure?
- No. Pairing-based signatures are not post-quantum secure

Next steps:

- PRs for Issues 10 and 37 plus editorial pass to wrap up ldp-bbs2020
- Brent will do PR for 37 [https://github.com/w3c-ccg/ldp-bbs2020/issues/37](https://github.com/w3c-ccg/ldp-bbs2020/issues/37),
- Timo will do PR for 10 [https://github.com/w3c-ccg/ldp-bbs2020/issues/10](https://github.com/w3c-ccg/ldp-bbs2020/issues/10).
- Invite everyone to suggest editorial changes
- Create WG at DIF for Crypto - first work item BBS+
- Tobias will work with Rouven to get that started, [https://github.com/decentralized-identity/org/blob/master/working-group-lifecycle.md](https://github.com/decentralized-identity/org/blob/master/working-group-lifecycle.md)
- Brent and Tobias will work together to draft a charter

Future steps:

- Possible working group, or addition to DIF C&C WG for work on ldp-bbs2021
* [Tobias Looker on BBS+ use cases, DIF Interop WG 25Nov2020](https://www.youtube.com/watch?v=slkbFW6imUk) Tobias Looker, MATTR, Interoperability Working group at DIF:

- Replay attack protection
- Domain-specific identifiers and proofs
- New partial-disclosure topographies

* [Deciphering BBS+ Signatures](https://academy.affinidi.com/deciphering-bbs-signatures-e853bbf437bf) Affinidi

This digital signature was created by Dan Boneh, Xavier Boyen, and Hovav Shacham using the strong Diffie-Hellman encryption technique, and hence the name BBS (after their respective surnames). The original signature was modified later to include proof of knowledge, and hence the name BBS+
* [IIW32: BBS+ and Beyond](https://medium.com/mattr-global/iiw32-bbs-and-beyond-1a41634c15b0) Nader Helmy, Mattr

One common theme this year was the continued development and adoption of BBS+ signatures, a type of multi-message cryptographic digital signature that enables selective disclosure of verifiable credentials.

This development is possible due to the fact that BBS+ signatures is a ledger-independent approach to selective disclosure, effectively no custom logic or bespoke infrastructure is needed for these digital signatures to be created, used and understood.
* [The Power of a Secret](https://trbouma.medium.com/the-power-of-a-secret-c9fa6a404ea3)
  > What had been discovered by Whitfield Diffie and Martin Hellman (and also Jame Ellis), is changing the world as we know it. It’s been only 43 years. Yes, that seems like an ice-age ago, but in the grand scheme of history, it is only a wink.
* [credential definitions, credential manifests, BBS+, etc](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0010.html) Daniel Hardman
  > When Tobias first described Mattr's approach to BBS+ signatures, one of my takeaways was that this changed the Indy mechanism of cred defs in two wonderful ways:
> 1. It eliminated the need for lots of keys (only one key, Y, needs to be declared as a credential signing key, instead of a set of keys, Y[0]..Y[n])
> 2. It made it possible to store a cred def somewhere other than a ledger
> I was very happy about this.
> However, I have since heard several smart people summarize the breakthrough as: "We don't need credential definitions at all. You just use the assertionMethod key in your DID doc to sign credentials, and that's all you need." I believe this is oversimplifying in a way that loses something important, so I wanted to open a conversation

## Jose-Cose

* [Two new COSE- and JOSE-related Internet Drafts with Tobias Looker](https://self-issued.info/?p%3D2260) Mike Jones
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
