---
published: false
---

# DIDs

* [The did:indy DID Method - Future Indy Ledgers](https://iiw.idcommons.net/4I/_The_did:indy_DID_Method_-_Future_Indy_Ledgers) by Stephen Curran

* [Presentation](https://docs.google.com/presentation/d/1c5K7E5CRx9ANuwmVBIyFVG5hJ4lH0EyW-wkmraLivBI/edit?usp%3Dsharing)

Goals of the did:indy DID Method Specification

- Namespaced DIDs useful across all Indy instances
- Indy network discovery
- Full DIDDoc support
- Namespaced identifiers for other Indy objects (schemas, etc.)
- Support for important resolution parameters
- E.g. version-id, version-time, resource
- Nice to have (but not likely to be there):
- Cross-ledger registration of networks for discovery
- Support for KERI identifiers on Indy networks

Getting involved with this work:

- [HackMD Document](https://hackmd.io/@icZC4epNSnqBbYE0hJYseA/S1eUS2BQw) with current spec
- Home of future spec: [indy-did-method](https://github.com/hyperledger/indy-did-method)
- [Meeting Wiki](https://wiki.hyperledger.org/display/indy/Indy%2BDID%2BMethod%2BSpecification) and schedule
- Hyperledger [indy-did-method](https://chat.hyperledger.org/channel/indy-did-method) chat channel
- Currently seeking developers to implement the required updates
- Python for indy-node, Rust for indy-sdk and indy-vdr

* [DID Method Onion Specification](http://htmlpreview.github.io/?https://raw.githubusercontent.com/BlockchainCommons/did-method-onion/main/index.html)
  > 🧅 part of the torgap technology family

> DIDs that target a distributed ledger face significant practical challenges in bootstrapping enough meaningful trusted data around identities to incentivize mass adoption. We propose using a new DID method that allows them to bootstrap trust using a Tor Hidden Service's existing reputation.

> we'd like to review more with our community how close we want to keep did:onion to did:web, and if we want to incorporate some elements of did:peer or KERI or to leverage services like Open Time Stamps.
* [Sidetree Spec V1.0.0](https://identity.foundation/sidetree/spec/) Working Group approved status

* [Elastos DID: What’s Ahead for 2021](https://news.elastos.org/elastos-did-whats-ahead-for-2021/)
  > DID 2.0’s primary objectives are to provide a superior developer and user experience, and to support more complex business models and use case scenarios enabling the expansion of DID’s implementation and adoption potential.
* [Discussion of NFT and music projects, NFT:DID for turning NFT's into identities, and critical updates en route to mainnet.](https://www.youtube.com/watch?v%3DJfvRLhz6OpY) Ceramic Community Call
  > you can go to [ceramicnetwork/nft-did-resolver](https://github.com/ceramicnetwork/nft-did-resolver) on github to see the prototype
  > so this is the minimal implementation that allows you to verify signatures of the most recent owner of the nft did as like being valid
* [did:did - DID Identity DID (DID) DID method](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0026.html)
  > Spruce announces did:did, a DID method based on Decentralized Identifiers (DIDs). We hope the community will find this useful to help increase adoption and interoperability of Decentralized Identity technology.

Specification: [https://did-did.spruceid.com/](https://did-did.spruceid.com/)

Source: [https://github.com/spruceid/did-did/](https://github.com/spruceid/did-did/)

Registration request: [https://github.com/w3c/did-spec-registries/pull/280](https://github.com/w3c/did-spec-registries/pull/280)
* [The EOSIO DID method specification](https://www.gimly.io/blog/the-eosio-did-method-specification)
  > We have been working with the [Decentralised Identity Foundation](https://identity.foundation) to shape this specification, and also want to thank the [W3C Credentials Community Group](https://www.w3.org/community/credentials/) for their support in the creation of the [Verifiable Condition](https://github.com/Gimly-Blockchain/verifiable-conditions) type, a necessary component to create the EOSIO DID document to represent EOSIO account permissions.
* [DID Identity UN-DID Method Specification](https://did-undid.github.io/did-undid/)
  > Clarification, a few week ago we shared about the [DID:DID](https://did-did.spruceid.com/) method. [April Fools Joke](https://en.wikipedia.org/wiki/April_Fools%2527_Day_RFC)!!! Here’s yet another DID method in the series.

did:un-did is a DID method that enables using any valid Decentralized Identifier (DID) as a did:un-did DID, but more importantly it un-does the did that did:did did method performs.
* [Don’t use DIDs, DIDs, nor DIDs: Change My Mind (a.k.a. Oh no he DIDn’t)](https://dwhuseby.medium.com/dont-use-dids-58759823378c) by Dave Huseby ([video](https://eu01web.zoom.us/rec/play/4_ZLV8uot0hFQgRZsoILvdnn879oGEmrXsPXsCcvf4GsDPjWLQAxKjrZFiF0AxQe_MYb1_oeQa9HsRY.8KTaTYyrhu2Q-kJ_?continueMode%3Dtrue))

Joe came and fervently disagreed with my assertions. Lots of people had reasonable counter arguments. My main arguments are 1. DID Documents don't have history when old keys are always relevant and 2. having 94 different DID methods that aren't compatible nor replaceable and don't function the same way is a HUGE problem.

* [WACI (Wallet And Credential Interaction)](https://identity.foundation/wallet-and-credential-interactions/)
### DID Methods

* [DID:Customer](https://medium.com/transmute-techtalk/did-customer-4ca8b7957112)
  > While we are committed to providing optionality to our customers, it’s equally important to communicate the selection criteria behind these options so that customers can consider the tradeoffs of underlying DID-methods alongside the problem set they’re solving for.

* [BrightID](https://www.brightid.org/) (a singular address that is linked to your friends’ ID in a “web of trust”) and [UBDI](https://app.ubdi.com/) lets you pull in data from a whole variety of sources and then make deals to get $ for your data.

* [3IDConnect](https://blog.ceramic.network/what-is-3id-connect/) Ceramic
 - along with the slightly problematic frame that users have “a DID” ([GitHub](https://github.com/3box/3id-connect))

* [Trinsic Basics: What Are SSI Standards?](https://trinsic.id/what-are-ssi-standards/)
  > There are two kinds of standards that Trinsic implements to enable interoperability and avoid vendor lock-in: data model standards and protocol standards.

* [Trusted P2P Messaging with DIDs, DIDComm and VCs](https://medium.com/uport/trusted-p2p-messaging-with-dids-didcomm-and-vcs-398f4c3f3cda) uPort
  > about their path towards trusted P2P messaging and announces the [DIDAgent Framework (DAF)](https://github.com/uport-project/daf)
  > 
  > when we speak about a DID, then we need to be more precise and also speak about the particular DID method of that DID which defines the CRUD operations on a target system such as Ethereum.

* [DogeCoin DID Method by Spruce Systems](https://github.com/spruceid/did-doge)
  > - Such Decentralization: Dogecoin is a public, permissionless blockchain favored by Shiba Inus worldwide, making it suitable for this purpose.
  > - Much Identity: Since shibes are unique in different and special ways, this specification provides the means to assign each one their very own ShibeID.
  > - Wow Blockchains: Dogecoin has proven again and again its resiliency in the face of adversity, proving that it is the ultimate host to such a primitive.
* [Decentralized Identity with the Tezos DID Method](https://sprucesystems.medium.com/decentralized-identity-with-the-tezos-did-method-d9cf6676dd64)

* [Spruce](https://www.spruceid.com/) and [TQ Tezos](https://tqtezos.com/) are jointly releasing the [draft specification](https://did-tezos.spruceid.com/) and [initial implementation](https://github.com/spruceid/did-tezos) of [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/) based on the Tezos blockchain.

* [godiddy.com - Universal DID Services](https://iiw.idcommons.net/2C/_godiddy.com_-_Universal_DID_Services) by Markus Sabadello

godiddy.com is a hosted platform that makes it easy for SSI developers and solution providers to work with DIDs.

Basic functions are creating, resolving, updating, and deactivating DIDs across multiple DID methods and networks. Advanced functions include key management, search, transfer of DIDs, lookup of historical DID document versions, notification of DID-related events, and more.

This platform can be accessed either via a web frontend, or an API.

Check out the [Documentation](https://docs.godiddy.com/) and the [API Reference](https://api.godiddy.com/).

SaaS, Wallet, DID

- Centralized service that shouldn’t be used to host security sensitive DIDs, it contradicts the principle of self-sovereignty. The service is meant for developers to try out the technology.
- Godiddy is a service that hosts the community components universal resolver and registrar + additional proprietary components so that it offers a comprehensive DID service for creating and managing DIDs across multiple methods.
- How robust is the service on bad network connections? Markus: There are github issues concerning TTL in the DID spec WG. Self-hosting is likely to be a better option than using the centralized service.
- Feature Grid with future ideas: [https://docs.godiddy.com/en/feature-grid](https://docs.godiddy.com/en/feature-grid)

- Key Management: When keys are created they are stored in the wallet and are returned to the client. This is not ideal from a security point of view. An improved API is planned that would allow clients to keep the private key on the client and use the service to create for example the DID Document -> this is also part of the next session.

* [Don’t use DIDs, DIDs, nor DIDs: Change My Mind (a.k.a. Oh no he DIDn’t)](https://iiw.idcommons.net/10A/_Don%2527t_use_DIDs,_DIDs,_nor_DIDs:_Change_My_Mind_(a.k.a._Oh_no_he_DIDn%2527t)) by Dave Huseby

This session was to talk about the topics I put in a recent article that created a huge fire in our community where I lay out the case for completely abandoning the W3C DID standards.

* [https://dwhuseby.medium.com/dont-use-dids-58759823378c](https://dwhuseby.medium.com/dont-use-dids-58759823378c)

Joe came and fervently disagreed with my assertions. Lots of people had reasonable counter arguments. My main arguments are 1. DID Documents don't have history when old keys are always relevant and 2. having 94 different DID methods that aren't compatible nor replaceable and don't function the same way is a HUGE problem.

There was no conclusion other than Sam Smith and I came to the conclusion that we have more in common than we thought.

* [Standard Interfaces for DID Create/Update/Deactivate](https://iiw.idcommons.net/3C/_Standard_Interfaces_for_DID_Create/Update/Deactivate) by Markus Sabadello

- There is an attempt to specify abstract interfaces if you want to Create/Update/Deactivate a did that could be implemented for all did methods.
- The idea of this specification is to provide a standard with the same assumptions as with resolution. It should be in an abstract level, meaning it should specify the inputs and outputs of creating/updating/deactivating a did but not how it should be implemented.
- There are many differences on how the operations of different did methods work, so it is still a question whether this standard will work for all did methods at the current state.
- Two greatest architectural questions that have come in the way:
- How should key management be handled: where are keys created, how are they handled etc?
- The concept of internal state or longer running jobs
- Regarding key management, in the current early draft there is a section which describes 3 possible way to handle key management:
- Internal secret mode: The service itself generates keys and either stores them or returns them to the client. The disadvantage is that the service has to be highly trusted. This mode could make sense if you run the service yourself.
- External secret mode: Key management is handled by some kind of externally hosted wallet that the service can call (e.g hardware wallet).
- Client-managed secret mode: The client that makes use of the registrar service would first create the keys and then call the different functions of the service. This would mean back and forth communication between server and client (e.g server sends sign request, client signs etc.).

* [...]

Links:

- [https://peacekeeper.github.io/did-registration/](https://peacekeeper.github.io/did-registration/)
- [https://dev.uniresolver.io/](https://dev.uniresolver.io/)
- [https://uniregistrar.io/](https://uniregistrar.io/)
- [https://w3c-ccg.github.io/did-resolution/](https://w3c-ccg.github.io/did-resolution/)
- [https://w3c.github.io/did-rubric/](https://w3c.github.io/did-rubric/)
- [https://github.com/decentralized-identity/universal-registrar](https://github.com/decentralized-identity/universal-registrar)
- [https://godiddy.com](https://godiddy.com/)

* [We evaluated 7 DID methods with the W3C DID Rubric! did:btcr, did:sov, did:ion, did:web, did:v1, did:peer, did:ethr](https://iiw.idcommons.net/13D/_We_evaluated_7_DID_methods_with_the_W3C_DID_Rubric!_did:btcr,_did:sov,_did:ion,_did:web,_did:key,_did:peer,_did:ethr) by Walid Fdhila, Markus Sabadello ([video](https://eu01web.zoom.us/rec/play/5wIkMptZK28kj6LFF5NlILMApA-2CwRMw1L7s4aO8wsgFDODJ-pGlbKPh6YA7BEADftL_Uw7sHx6YY2r.KWeBYTIH4BFQmLIv?continueMode%3Dtrue)

Join research project between SBA Research and Danube Tech, partially funded by FFG (Austria) and DHS (US).

did:btcr [https://w3c-ccg.github.io/didm-btcr](https://w3c-ccg.github.io/didm-btcr)

did:v1 [https://w3c-ccg.github.io/did-method-v1/](https://w3c-ccg.github.io/did-method-v1/)

did:ethr [https://github.com/ethr-did-resolver/](https://github.com/decentralized-identity/ethr-did-resolver/blob/master/doc/did-method-spec.md)

did:sov(did:indy) [Sovrin DID Method Specification](https://sovrin-foundation.github.io/sovrin/spec/did-method-spec-template.html)

did:web [https://github.com/w3c-ccg/did-method-web](https://github.com/w3c-ccg/did-method-web)

did:ion [https://github.com/decentralized-identity/ion-did-method](https://github.com/decentralized-identity/ion-did-method)

did:peer [https://identity.foundation/peer-did-method-spec/index.html](https://identity.foundation/peer-did-method-spec/index.html)

Selected criteria were rule making, operation, enforcement, security, controllability, portability, keying material, privacy.

Challenges and insights:

- For some DID method, evaluation requires more effort than just the specification. Each DID method uses different infrastructure. E.g. evaluating governance of Bitcoin blockchain is complex.
- Most DID methods focus on CRUD operations but don't think much about governance, privacy, security.
- Some DID methods are not very well documented.
- Discrepancies between specifications and actual implementations.
- It was difficult to compare methods since they are based on different technologies.
- Specifications change after or during the evaluation.
- DID Rubric has also changed/improved over time.
- Each DID method has pros and cons; there is no "winner"
- We had 6 evaluators, and in some cases we had different opinions.

Criteria for did Method Evaluation:

* [https://docs.google.com/document/d/1vAKtMrsrjO_tLQhah8tRoLaIS7HpOIE6xM38ZoBpgWU/](https://docs.google.com/document/d/1vAKtMrsrjO_tLQhah8tRoLaIS7HpOIE6xM38ZoBpgWU/)

DID Methods Evaluation Report - Draft

* [https://docs.google.com/document/d/1jP-76ul0FZ3H8dChqT2hMtlzvL6B3famQbseZQ0AGS8/](https://docs.google.com/document/d/1jP-76ul0FZ3H8dChqT2hMtlzvL6B3famQbseZQ0AGS8/)

* [Demystifying Decentralized Identifiers (DIDs)](https://academy.affinidi.com/demystifying-decentralized-identifiers-dids-2dc6fc3148fd) Affinidi

- Does not require a centralized registration authority
- Many DIDs use the distributed ledger technology or any other decentralized network, though it is not mandatory
- It is a permanent identifier because it does not depend on a single third-party or centralized registry for its existence.
- Can be cryptographically verified
- They connect a DID subject (the entity identified by the DID) with a DID document (a set of data that describes the DID subject) to enable the subject to have trustable interactions.
- They are interoperable and portable, provided they conform to the existing standards laid down by W3C
* [Peer DIDs — An Off-Ledger DID Implementation](https://academy.affinidi.com/peer-dids-an-off-ledger-did-implementation-5cb6ee6eb168) Affinidi

Peer DIDs offer many benefits such as,

- No transaction costs involved
- Easy to create and maintain
- Since these DIDs are independent of a central system such as a GDPR controller, they can be scaled as needed
- Offers the highest levels of privacy as only the parties involved can access the DIDs
- No uncertainties or external problems since these DIDs are not associated with any particular network
- No degradation of trust throughout the entire lifecycle.
- In tune with local-first software philosophies
- Reduces unnecessary correlation between a verifier and an issuer of a [verifiable credential](https://academy.affinidi.com/what-are-verifiable-credentials-79f1846a7b9).
* [UNISOT DID approved by W3C](https://unisot.com/unisot-did-approved-by-w3c/)

We are proud to have UNISOT ID (did:unisot) listed at the Decentralized Identity Foundation (DIF). As part of our commitment to open technologies and global interoperability we have presented our DID schema (did:unisot) to the Decentralized Identity Foundation (DIF) and supplied a driver for their Universal DID Resolver which can be accessed at: [https://resolver.identity.foundation/](https://resolver.identity.foundation/). With this anyone can resolve a UNISOT DID Document in a trusted and easy way.
* [Don’t Use DIDs: Political Solutions Never Solve Technological Problems](https://dwhuseby.medium.com/dont-use-dids-58759823378c) DW Husebey

A large set of impact investor, international donor, and government anti-poverty policy is based on the notion that for-profit companies can be induced to serve the poor with life changing services like banking or schooling but the limits of the for profit model are not always taken into account

* [SecureKey’s New Ledger-Agnostic did:orb](https://securekey.com/securekeys-new-ledger-agnostic-solution-orb-helps-solve-decentralized-identifier-challenges/)

did:orb that decouples DIDs from ledgers while maintaining trust and security. SecureKey is leveraging standard and open-source peer-to-peer protocols like ActivityPub, data structures like verifiable credentials content-addressed storage like IPFS, and distributed trust services like the Google Trillian project to build a peer-to-peer trust network.

* [Git as Authentic Data Creation Tool (a.k.a. what happened to did:git? a.k.a. independently verifiable, secure, developer sovereign, open source software supply chain)](https://iiw.idcommons.net/12A/_Git_as_Authentic_Data_Creation_Tool_(a.k.a._what_happened_to_did:git%253F_a.k.a._independently_verifiable,_secure,_developer_sovereign,_open_source_software_supply_chain)) by Dave Huseby

This session covered the evolution of thinking from the initiation of did:git at IIW April 2019 up until now. I recently chose to deprecate the did:git proposal in lieu of a new project to update Git to use provenance logs for identifier management in Git repos. I recently wrote an article describing the proposal:

* [https://dwhuseby.medium.com/universal-cryptographic-signing-protocol-for-git-42e7741b8773](https://dwhuseby.medium.com/universal-cryptographic-signing-protocol-for-git-42e7741b8773)

and the current proposal is here:

* [https://github.com/TrustFrame/git-cryptography-protocol](https://github.com/TrustFrame/git-cryptography-protocol)

This is an exciting project that will bring decentralized identifiers to software creation to give us end-to-end secure and verifiable software delivery.

* [Veres One (did:v1) Rubric Evaluation](https://iiw.idcommons.net/12B/_Veres_One_(did:v1)_Rubric_Evaluation) by Joe Andrieu

Veres One, DID Rubric Evaluation, DID methods, DIDs,

* [http://legreq.com/pres/v1.rubric.iiw.2021.04.21.pdf](http://legreq.com/pres/v1.rubric.iiw.2021.04.21.pdf)

What we learned #1

- Rubric still in infancy
- Some questions were just too academic
- Need structure-variable questions
- 1.3 Separation of Power
- 4.6 Consensus layers
- Enforcement (initial draft of real questions)

What we learned #2

- Design is itself a separable concern
- Distinct from governance
- May need separate evaluations for Implementations, esp wallets
- Adversaries: how does the method handle particular adversaries

What we learned #3

- Still a long learning curve
- Learning the Rubric
- Learning each Method
- Need better tools for community engagement
- Criteria discussion
- Custom rubric development
- Shared rubric evaluations

* [http://legreq.com/media/rubric.v1.2021.04.20.pdf](http://legreq.com/media/rubric.v1.2021.04.20.pdf)

- Questions/Comments:
- Looks like NIST (Common Criteria)
- Evaluating security of systems
- [https://en.wikipedia.org/wiki/Common_Criteria](https://en.wikipedia.org/wiki/Common_Criteria)
- [https://www.nist.gov/publications/common-criteria-launching-international-standards](https://www.nist.gov/publications/common-criteria-launching-international-standards)

* [...]

Notes from Chat:

* [http://legreq.com/pres/v1.rubric.iiw.2021.04.21.pdf](http://legreq.com/pres/v1.rubric.iiw.2021.04.21.pdf)

* [http://legreq.com/media/rubric.v1.2021.04.20.pdf](http://legreq.com/media/rubric.v1.2021.04.20.pdf)

* [DID Method Rubric v1.0](https://w3c.github.io/did-rubric/)

* [rwot9-prague/decentralized-did-rubric.md at master · WebOfTrustInfo/rwot9-prague](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/draft-documents/decentralized-did-rubric.md)

* [Common Criteria](https://en.wikipedia.org/wiki/Common_Criteria)

* [Introduction to Portable Contexts](https://www.youtube.com/watch?v%3DDVK5G9DIKf8)

* [The world between public and private DIDs - Or how to make use of SSI without the subjects](https://iiw.idcommons.net/21D/_The_world_between_public_and_private_DIDs_-_Or_how_to_make_use_of_SSI_without_the_subjects) by This Loepfe, cardossier CH

Slides: [iiw-between-public-and-private.pdf](https://cardossier.ch/wp-content/uploads/2021/05/iiw-between-public-and-private.pdf)

- It was very hard for me to explain the problem I’m searching a solution for and equally for the proposed solution ideas.
- We discussed a lot of more philosophical questions and if peer-dids are a good thing or not and if it is worth trying to minimize correlation when any involved party anyway stores the personal data of the related persons. I think we should make it as hard as possible to correlate data, even if we can not completely prevent it.
- We also discussed the potential complexity of such a solution and if it is worth it. The conclusion was to minimize the number of personas one should (be forced) to hold, such that it is still easy to maintain.
