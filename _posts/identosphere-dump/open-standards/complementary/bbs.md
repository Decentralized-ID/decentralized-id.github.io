# BBS

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
- [Anonymous Credential Part 3: BBS+ Signature](https://medium.com/finema/anonymous-credential-part-3-bbs-signature-26797721ca74)
  > Compared to the CL signature, the BBS+ signature has much shorter keys and signatures for a comparable level of security. As a result, the BBS+ signature enables fast implementation for anonymous credentials. It can be used in combination with signature proof of knowledge to hide some of credential attributes/messages in a zero-knowledge fashion.

The BBS+ signature will also soon be available in [Finema](https://finema.co/)’s Identity Wallet! We are excited to see how this technology will make an impact to the society in the coming years.
* [Implement Compound Proof BBS+ Verifiable Credentials Using ASP.NET Core and MATTR](https://damienbod.com/2021/12/13/implement-compound-proof-bbs-verifiable-credentials-using-asp-net-core-and-mattr/) Damien Bod
  > The ZKP BBS+ verifiable credentials are issued and stored on a digital wallet using a Self-Issued Identity Provider (SIOP) and OpenID Connect. A compound proof presentation template is created to verify the user data in a single verify.
  > Code: [https://github.com/swiss-ssi-group/MattrAspNetCoreCompoundProofBBS](https://github.com/swiss-ssi-group/MattrAspNetCoreCompoundProofBBS)
* [The Perfect Signature Style is the Enemy of the One that Works Today](https://indicio.tech/the-perfect-signature-style-is-the-enemy-of-the-one-that-works-today/) Indicio
  > BBS+ signature styles are not going to be ready for deployment anytime soon. This is precisely why you should build today and in a way that allows you to add them later.
- [Beyond JWS: BBS as a new algorithm with advanced capabilities utilizing JWP](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-beyond-jws-bbs-00) – [Tobias Looker](https://twitter.com/tplooker)
* [SelfSovereignIdentity_memes](https://twitter.com/SSI_by_memes/status/1578045600833994755)

Currently, everyone waiting for [#AIP2](https://twitter.com/hashtag/AIP2), which enables [#BBS](https://twitter.com/hashtag/BBS)+ [#Signature](https://twitter.com/hashtag/Signature) in #SSI. Companies already implemented in their products, such as [@trinsic_id](https://twitter.com/trinsic_id) and [@mattrglobal](https://twitter.com/mattrglobal). But ZKP [#predicates](https://twitter.com/hashtag/predicates) are not supported by BBS+, so no ZKP age verification possible. Back to [#AnonCreds](https://twitter.com/hashtag/AnonCreds)?
- [aries-rfcs/0646-bbs-credentials#drawbacks](https://github.com/hyperledger/aries-rfcs/tree/main/features/0646-bbs-credentials%23drawbacks)
