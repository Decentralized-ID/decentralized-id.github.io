---
published: false
---

# Crypto 
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
