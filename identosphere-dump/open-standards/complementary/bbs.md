# BBS

* [What’s next for BBS+ LD-Proofs?](https://iiw.idcommons.net/13B/_What%27s_next_for_BBS+_LD-Proofs%3F) by Brent Zundel

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

* [The Power of a Secret](https://trbouma.medium.com/the-power-of-a-secret-c9fa6a404ea3)
  > What had been discovered by Whitfield Diffie and Martin Hellman (and also Jame Ellis), is changing the world as we know it. It’s been only 43 years. Yes, that seems like an ice-age ago, but in the grand scheme of history, it is only a wink.


- [Beyond JWS: BBS as a new algorithm with advanced capabilities utilizing JWP](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-beyond-jws-bbs-00) – [Tobias Looker](https://twitter.com/tplooker)
* [SelfSovereignIdentity_memes](https://twitter.com/SSI_by_memes/status/1578045600833994755)

Currently, everyone waiting for [#AIP2](https://twitter.com/hashtag/AIP2), which enables [#BBS](https://twitter.com/hashtag/BBS)+ [#Signature](https://twitter.com/hashtag/Signature) in #SSI. Companies already implemented in their products, such as [@trinsic_id](https://twitter.com/trinsic_id) and [@mattrglobal](https://twitter.com/mattrglobal). But ZKP [#predicates](https://twitter.com/hashtag/predicates) are not supported by BBS+, so no ZKP age verification possible. Back to [#AnonCreds](https://twitter.com/hashtag/AnonCreds)?
- [Anonymous Credential Part 3: BBS+ Signature](https://medium.com/finema/anonymous-credential-part-3-bbs-signature-26797721ca74)
  > Compared to the CL signature, the BBS+ signature has much shorter keys and signatures for a comparable level of security. As a result, the BBS+ signature enables fast implementation for anonymous credentials. It can be used in combination with signature proof of knowledge to hide some of credential attributes/messages in a zero-knowledge fashion.

The BBS+ signature will also soon be available in [Finema](https://finema.co/)’s Identity Wallet! We are excited to see how this technology will make an impact to the society in the coming years.

- [aries-rfcs/0646-bbs-credentials#drawbacks](https://github.com/hyperledger/aries-rfcs/tree/main/features/0646-bbs-credentials#drawbacks)
* [What BBS+ Means For Verifiable Credentials](https://www.youtube.com/watch?v=dXlRIrrb9f4) Evernym
  > In a recent Evernym blog post, [we discussed why BBS+ LD-Proofs](https://www.evernym.com/blog/bbs-verifiable-credentials/) are the privacy-preserving VC format that everyone should implement. In this webinar….
  > - A brief history of verifiable credential formats, and how a lack of convergence makes scale and interoperability an ongoing challenge
  > - How BBS+ Signatures are the breakthrough that combine the best of the JSON-LD and ZKP formats, while still allowing for selective disclosure and non-trackability
  > - The path forward: What remains to be done to fully converge on the BBS+ format

* [BBS+ Credential Exchange in Hyperledger Aries](https://iiw.idcommons.net/11E/_BBS+_Credential_Exchange_in_Hyperledger_Aries) [[presentation](https://iiw.animo.id)]
* [Advanced DIDComm Messaging](https://github.com/WebOfTrustInfo/rwot11-the-hague/blob/master/advance-readings/advanced-didcomm-messaging.md) By: Karim Stekelenburg (Animo Solutions) -- karim@animo.id Date: 18-07-2022 Version: 0.1
  > in order for DIDComm to provide a potential replacement for commonly used chat protocols like WhatsApp (Extensible Messaging and Presence Protocol (XMPP)), Telegram (MTProto), or Signal (Signal Protocol), it needs to support modern chat features we use everyday
* [BBS+ Signatures 2020](https://w3c-ccg.github.io/ldp-bbs2020/)

- What’s next for BBS+ LD-Proofs?
- Implementation in Aries ([https://iiw.animo.id/](https://iiw.animo.id/), Used in SVIP Plugfest
