---
published: false
---

# KERI

* [KERI Q&A basic introduction](https://iiw.idcommons.net/3K/_KERI_Q%2526A_basic_introduction) by Henk van Cann

This the link to the 20 minute introductory presentation in pdf:

* [https://blockchainbird.org/downloads/KERI-QA-introduction.pdf](https://blockchainbird.org/downloads/KERI-QA-introduction.pdf)

It has lots of relevant links in it to start your journey in KERI.

What is KERI?

- Key Event Receipt Infrastructure
- Intends to repair the Internet
- KERI = CT with decentralized CA
- NOT a coin, token…

Why KERI? (and not something else)

- Strong autonomous identifiers
- Abiding to privacy (laws and good habits)
- Portability, delegation, rotatable keys
- Direct & Indirect method
- <there’s more>

With my notes:

* [https://blockchainbird.org/downloads/KERI-QA-introduction_notes.pdf](https://blockchainbird.org/downloads/KERI-QA-introduction_notes.pdf)

* [GLEIF and KERI (Global Legal Entity Identifier Foundation)](https://iiw.idcommons.net/1K/_GLEIF_and_KERI_(Global_Legal_Entity_Identifier_Foundation)) by Karla McKenna ([notes](https://docs.google.com/document/d/1oX7FonXfw8vofgLCHEghJwbxb4Xbf9dCkhHg50W___I/edit?usp%3Dsharing)) ([recording](https://eu01web.zoom.us/rec/play/xHLkyi5GSKHsU2frR8JX9oXXS5X_rxwTi9TcFpKtveYI3UZjOaVszW5X-Ie8_n6kJkrsAa7S0SW9zhBx.LM3S0YgffGYhm7uc?continueMode%3Dtrue)

* [LEI Digital Strategy](https://www.gleif.org/content/3-lei-solutions/6-gleifs-digital-strategy-for-the-lei/2021-02-09_lei-digital-strategy_v1.0-final.pdf)

* [Security Considerations of KERI. Why and how KERI provides secure portability](https://iiw.idcommons.net/2K/_Security_Considerations_of_KERI._Why_and_how_KERI_provides_secure_portability) by Samuel Smith

The Three KERI Security Sessions have the same set of Slides it just 3 hours to get through them.

* [https://github.com/SmithSamuelM/Papers/blob/master/presentations/KERI_Overview.web.pdf](https://github.com/SmithSamuelM/Papers/blob/master/presentations/KERI_Overview.web.pdf)

* [https://identity.foundation/keri/docs/Q-and-A-Security.html#part-two-security](https://identity.foundation/keri/docs/Q-and-A-Security.html%23part-two-security)

### *Q: What are the security risks of KERI with regard to the identity protocol?

Harm that can be done to the a controller: Unavailability, loss of control authority, externally forced duplicity

Harm that can be done to a validator: Inadvertent acceptance of verifiable - but forged or duplicitous events

Breaking the promise of global consistemcy by a controller is a provable liability. However, global consistency may only matter after members of that community need to interact, not before.

(SamMSmith)

### Q: How secure is the KERI infrastructure?

KERI changes the discussion about security. From a discussion about the security of infrastructure to a discussion about the security of your key management infrastructure. Most people when they think security, the think “oh, blockchain!”: permissioned or permissionless, how hard is it to get 51% attack, etc.Non of that matters for KERI. KERI is all about “are your private keys private?!” And if yes, that drastically slims down the security discussion to brute force attacks to public keys. And because the next public keys are in fact protected by a hash, you have to brute force the hash algorithm, that is post-quantum secure. So that is a very high level of infrastructural security.

So private key management and protection is the root of your security in KERI.

### *Q: You are arguing KERI affords greater security than a decentralized linear event system like Bitcoin?

…you would be fundamentally arguing that you can record a singular, immutable linear event history more securely than Bitcoin, and I see nothing in KERI that would indicate that.

Read the answer to [this](https://identity.foundation/keri/docs/Q-and-A-Security.html%23keri-is-basically-a-series-of-pay2publickeyhash-transactions) first.

If you read Szabo’s paper on threshold structures, you get security of the same type when ever you use a threshold structure, be it MFA, Multi-Sig, or Distributed consensus. They all are using a combination of multiple relatively weak attack surfaces that must be simulatenously compromised for a successful attack. So multiplying simulatneous weak surfaces = functional equivalent of a stronger attack surface. So when you look at KERI you see that the security is primarily due to cryptographic strength and the witnesses are not the primary source of security but merely secure one thing, that is the availability of the KEL for an identifier. Not the KEL itself. The KEL iteself is secured by signatures.

From a Validator perspective their security is due to duplicity detection. Successful attack against duplicity detection requires an eclipse attack. Ledgers such as bitcoin are also susceptible to eclipse attacks. So in an apples to apples (resistance to eclipse attack) a KERI watcher network of comparable reach (1000’s of watchers) would have comparable resistance to an eclipse attack.

### Q: Differences between blockchain-based security and KERI security

- Where KERI doesn’t need total ordering in its logs, blockchain do need that. What KERI needs is watchers that construct string of event in the relative order of reception of the KEL {TBW please explain or improve this: what is this, why is it important?}
- Another characteristic is that KERI identifiers are transferable and blockchain-based identifiers are not, they are bound to their ledger.

* [KERI and ADS Key State Provenance Logs Kumbaya (KEL and ADPL)](https://iiw.idcommons.net/24H/_KERI_and_ADS_Key_State_Provenance_Logs_Kumbaya_(KEL_and_ADPL)) by Samuel Smith, Dave Huseby

This was a meeting of the minds between myself and Sam Smith and Adrian Gropper that was hugely successful. We all decided to use the term "endorser" for what we all called "registrar"/"witness"/"notary". We also realized that the KERI proposal for encoding is good enough for authentic data provenance logs and we will be using the KERI encoding. Sam has modified the spec for KERI key event logs to include scripting capabilities needed in the authentic data economy for doing things like cross-chain atomic swaps for selling non-fungible authentic data (NFADs).

The result is that there is grand convergence on the encoding and file format for key event provenance logs that will be supported by both KERI networks and the broader authentic data economy.

* [KERI: Centralized registry with decentralized control (KEL & TEL ) + DEMO](https://iiw.idcommons.net/11K/_KERI:_Centralized_registry_with_decentralized_control_(KEL_%2526_TEL_)_%252B_DEMO) by Robert Mitwicki, Charles Cunningham, Phil Feairheller , Michał Pietrus

* [GLEIF vLEI with KERI](https://iiw.idcommons.net/20K/_GLEIF_vLEI_with_KERI)

The Global Legal Entity Identifier Foundation (GLEIF) proposes that the Legal Enitity Identifier (LEI) can be used to establish a chain of trust for organizational identity.

In this session, GLEIF shares plans and progress regarding its development program to create an ecosystem and credential governance framework, together with a technical supporting infrastructure, for a verifiable LEI (vLEI), a digitally verifiable credential containing the LEI.

Link to presentation available until April 2022:

* [https://td2ec2in3mv1euwest.teamdrive.net/bgvkygms/public/I39DS3Tn?k=MMiiLXItHvmxOtB0kFROQGXMTDFgjCngWTiQFed43Ak](https://td2ec2in3mv1euwest.teamdrive.net/bgvkygms/public/I39DS3Tn?k%3DMMiiLXItHvmxOtB0kFROQGXMTDFgjCngWTiQFed43Ak)

Agnostic to any network

- Development of the capabilities needed for GLEIF to issue and verify vLEIsfor vLEI Issuers does not need to operate on blockchain or distributed ledger technology.
- GLEIF can implement KERI (Key Event Receipt Infrastructure) to support fully decentralized portable secure key management operations on self-certifying identifiers.
- GLEIF is undertaking development of the capabilities based on KERI during 1Q to 3Q of 2021 and aim for initial live beta implementation with an SSI Network starting in 4Q.

Interoperability

- This would allow GLEIF to connect to any blockchain or distributed ledger technology SSI network without the need for custom implementation, cost and overhead of operation.
- KERI is Quantum Safe. It is resistant to attacks by both classical and quantum computers.

* [Supply chain – ACDC and KERI + DEMO](https://iiw.idcommons.net/14K/_Supply_chain_%25E2%2580%2593_ACDC_and_KERI_%252B_DEMO) by Robert Mitwicki ([video](https://eu01web.zoom.us/rec/play/GKGhv1QJ0BSoQZ9Dg-IKeyXKb0Nw0GZUry8qgvM58NS6YcZIz-u8xYMaeKn6-HpP6SMxNJvHebrvdw.NNWuKPuVGekv7zyU?continueMode%3Dtrue)

* [https://docs.google.com/presentation/d/1tF_OFGAKUz9RKCLTdwDYDu7hJuEbFz-LQ6PAih7HBK8/edit#slide=id.p](https://docs.google.com/presentation/d/1tF_OFGAKUz9RKCLTdwDYDu7hJuEbFz-LQ6PAih7HBK8/edit%23slide%3Did.p)

* [https://en.wikipedia.org/wiki/Spime](https://en.wikipedia.org/wiki/Spime)

* [https://wiki.trustoverip.org/display/HOME/ACDC+%28Authentic+Chained+Data+Container%29+Task+Force](https://wiki.trustoverip.org/display/HOME/ACDC%2B%2528Authentic%2BChained%2BData%2BContainer%2529%2BTask%2BForce)

* [https://hackmd.io/RX8ZAycxQhSpGZgBfRzqbg?view](https://hackmd.io/RX8ZAycxQhSpGZgBfRzqbg?view)

ACDC

Datum is, from its Latin origin, a singular form of “data”, and may refer to a single item of data.

* [git@github.com](mailto:git@github.com):THCLab/keri-python-ffi.git

* [https://trustedcomputinggroup.org/](https://trustedcomputinggroup.org/)

* [https://www.microcontrollertips.com/what-is-dice-architecture-faq/](https://www.microcontrollertips.com/what-is-dice-architecture-faq/)

* [KERI Composable Event Streaming Representation](https://iiw.idcommons.net/23K/_KERI_Composable_Event_Streaming_Representation) by Samuel Smith

* [KERI: For every DID, a microledger](https://medium.com/decentralized-identity/keri-for-every-did-a-microledger-f9457fa80d2d) Decentralized Identity Foundation
* [On KERI: a way not to reveal more personal info than you need to](https://blogs.harvard.edu/doc/2020/10/22/keri/) Doc Searls
* [How KERI tackles the problem of trust](https://jolocom.io/blog/how-keri-tackles-the-problem-of-trust/) by Jolocom
* [Tim talks with Sam Smith, creator of KERI](https://podcasts.apple.com/ca/podcast/definitely-identity-episode-14-with-sam-smith/id1496565155?i=1000494102345)
  > In this episode, we explore the Key Event Receipt Infrastructure (KERI)and how it relates to decentralized identity. We also touch topics in the white paper: trust domains, self-certifying identifiers, architectural implications, and more.
* [Thinking of DID? KERI On](https://humancolossus.foundation/blog/thinking-of-did-keri-on)
  > The current generation of DIDs has introduced an innovative approach to digital identifiers, which has triggered the SSI movement. However, the inclusion of the method space in the DID syntax has led to fragmentation and weak security properties of the identifier type. These known method-space issues give the community impetus to redress them. In light of these innovative developments, now is the time to embrace KERI as an improved interoperable and secure solution for digital identity.
