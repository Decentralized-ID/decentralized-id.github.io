---
title: "(DID) the Decentralized Identifier"
description: Decentralized identifiers (DIDs) are a new type of identifier that enables verifiable, decentralized digital identity. 
excerpt: >
  Decentralized identifiers (DIDs) are a new type of identifier that enables verifiable, decentralized digital identity. A DID identifies any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) that the controller of the DID decides that it identifies. In contrast to typical, federated identifiers, DIDs have been designed so that they may be decoupled from centralized registries, identity providers, and certificate authorities. Specifically, while other parties might be used to help enable the discovery of information related to a DID, the design enables the controller of a DID to prove control over it without requiring permission from any other party. DIDs are URIs that associate a DID subject with a DID document allowing trustable interactions associated with that subject.
categories: ["Web Standards"]
tags: ["51nodes","ABT Network","Aergo","Alastria","ArcBlock","Ardor","Baidu","BCGov","Besu","bif","BiiLabs","Binance","Bitcoin","Blockcore","Blocko","Blockstack","BOTLabs","bryk","BTCR","CAICT","Celo","Chainyard","Cloudchain","Commercio","Cosmos","Consensys","Consent","Corda","Credentials Community Group","cryptonics","DID","Digital Bazaar","Dock","Echo","Elastos","Element","ERC725","Ethereum","evan","Evernym","Fabric","Factom","Gatica","Github","GRGBanking","GrgChain","Halialabs","Hashgraph","Holochain","Hydra","Hyland Credentials","Hyperledger Foundation ","IBM","ICONLOOP","IIW","InfoWallet","ION","IOP","IOTA","IoTeX","IPFS","IPID","JLinc","Jnctn","Jolocom","KILT","Klaytn","lifeID","MediBloc","Metadium","Microsoft","MOAC","NEAR","Ocean Protocol","Ockam","OmniOne","Ontology","Panacea","Peer DID","ProximaX","Quorum","Raonsecure","RChain","Rebooting WoT","SecureKey","SelfKey","Sovrin Foundation","SpaceElephant","Sphereon","Swisscom ","teleinfo ","TMChain","Token.TM","TranSendX","Transmute","TRON","Twitter","UNS","uPort","Vaultie","Veres One","Vivvo","VP","W3C","Web","Weelink","Workday","XDI","YLZ ","Zilliqa"]
permalink: web-standards/w3c/wg/did/decentralized-identifier/
canonical_url: https://decentralized-id.com/web-standards/w3c/wg/did/decentralized-identifier/
redirect_from: 
  - web-standards/w3c/did-wg/decentralized-identifier/
  - specs-standards/decentralized-identifier-did/
  - web-standards/decentralized-identifier-did/
  - adoption/
last_modified_at: 2020-12-02
toc: false
---

{% include toc %}

<a href="https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf"><img src="https://i.imgur.com/7NRcJbq.png"/></a>

## Decentralized Identifier

* [Decentralized Identifiers (DIDs) v1.0](https://w3c.github.io/did-core/)
  >   Decentralized identifiers (DIDs) are a new type of identifier that enables verifiable, decentralized digital identity. A DID identifies any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) that the controller of the DID decides that it identifies. In contrast to typical, federated identifiers, DIDs have been designed so that they may be decoupled from centralized registries, identity providers, and certificate authorities. Specifically, while other parties might be used to help enable the discovery of information related to a DID, the design enables the controller of a DID to prove control over it without requiring permission from any other party. DIDs are URIs that associate a DID subject with a DID document allowing trustable interactions associated with that subject.
* [DID Whitepaper](https://github.com/WebOfTrustInfo/rwot2-id2020/blob/master/topics-and-advance-readings/DID-Whitepaper.md)
  > A DID architecture should focus on the set of components that Mr. Gupta refers to as "the minimum required for people to be able to do business (or other critical functions) together".
  >
  >**A Decentralized Identifier (DID) Registry and Discovery Service**
  >
  > This "minimum required" is defined by a union of the proposed requirements identified by the W3C Credential Community Group, the XDI.org Registry Working Group, and the Rebooting the Web of Trust group. It consists of three functions that can be addressed by a combination of blockchain and DHT technology:
  >
  > * A DID registration function
  > * A discovery function that enables looking up a registered DID in the blockchain
  > * A master key recovery function
* [A Universally Unique IDentifier (UUID) URN Namespace](https://www.ietf.org/rfc/rfc4122.txt) <-DID's modeled after
  * [All you need to know about sequential UUID generators](https://blog.2ndquadrant.com/sequential-uuid-generators/)
* [Understanding Decentralized IDs (DIDs)](https://medium.com/@adam_14796/understanding-decentralized-ids-dids-839798b91809)
* [DID Primer](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/draft-documents/did-primer.md) [[**ϟ**](https://github.com/WebOfTrustInfo/rwot7-fall2018/blob/master/topics-and-advance-readings/did-primer-extended.md)]
* [Decentralized IDentifers (DIDs)](https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf) 
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
* [DIDs in DPKI](https://github.com/WebOfTrustInfo/rwot7/blob/master/topics-and-advance-readings/dids-in-dpki.md)
* [What is a DID?](https://docs.google.com/document/d/1Ym85y_bDVN9xkRZ-oD-zlUUIeZjVGWNihfZBk2GQidk/edit)
* [The Path from an id (DID) to a Real-Life Something](https://hyperonomy.com/2019/01/04/the-path-from-a-id-did-to-a-real-life-something)

<a href="https://hyperonomy.files.wordpress.com/2019/01/path-id-did-real-life-somethings-v0.2-1.png"><img src="https://hyperonomy.files.wordpress.com/2019/01/path-id-did-real-life-somethings-v0.2-1.png?w=500"/></a>

[1A/ DID 101 – Decentralized Identifiers & how they are the key to interoperable self-sovereign ID](http://iiw.identitycommons.net/1A/_DID_101_%E2%80%93_Decentralized_Identifiers_%26_how_they_are_the_key_to_interoperable_self-sovereign_ID)


## [DID Method Registry](https://w3c-ccg.github.io/did-method-registry/#the-registry)

### [**`did:abt:`**](https://arcblock.github.io/abt-did-spec/)
###### For ABT Network, by ArcBlock

> ```
>     did:abt:z1muQ3xqHQK2uiACHyChikobsiY5kLqtShA
>       DID            DID string
>     schema
> ```
> One of our main goal is to protect users’ privacy. So people do not use the DID generated from their master key to talk to DAPPs, instead, the WALLET automatically generates an extended DID according to the user’s master DID and the DAPP’s DID and use this extended DID to communicate with the DAPP. 

### [**`did:btcr:`**](https://w3c-ccg.github.io/didm-btcr)
###### For Bitcoin, by Christopher Allen, Ryan Grant, Kim Hamilton Duffy

> The Bitcoin Reference DID method (did:btcr) supports DIDs on the public Bitcoin blockchain. The Bitcoin Reference method has minimal design goals: a DID trust anchor based on the Bitcoin blockchain, updates publicly visible and auditable via Bitcoin transactions, and optionally, additional DID Document information referenced in the transaction OP_RETURN data field. No other Personal Identifiable Information (PII) would be placed on the immutable blockchain.
> 
> A secondary intent of the BTCR method is to serve as a very conservative, very secure example and some best practices for creating a DID method. The use cases for BTCR are focused on anonymous and pseudo-anonymous identities, web-of-trust style webs of identity, and absolute mimimal personal information disclosure. Other DID methods will likely need to loosen these standards.
> 
> Some aspects of the BTCR method will not be practical if inappropriately scaled — for instance, there is a transaction cost to update keys and DDO object, potential UTXO inflation (i.e. one additional unspent output for every BTCR-based identity), and even if segwit isn’t used it could cause blockchain bloat. However, identities using the BTCR method can be a strong as Bitcoin itself -- currently securing billions of dollars of digital value.

### [**`did:stack:`**](https://github.com/blockstack/blockstack-core/blob/stacks-1.0/docs/blockstack-did-spec.md)
###### For Bitcoin, by Jude Nelson

> Blockstack's DID method is specified as part of its decentralized naming system. Each name in Blockstack has one or more corresponding DIDs, and each Blockstack DID corresponds to exactly one name -- even if the name was revoked by its owner, expired, or was re-registered to a different owner.
> 
> Blockstack is unique among decentralized identity systems in that it is not anchored to a specific blockchain or DLT implementation. The system is designed from the ground up to be portable, and has already been live-migrated from the Namecoin blockchain to the Bitcoin blockchain. The operational ethos of Blockstack is to leverage the must secure blockchain at all times -- that is, the one that is considered hardest to attack.
> 
> Blockstack's naming system and its DIDs transcend the underlying blockchain, and will continue to resolve to DID document objects (DDOs) even if the system migrates to a new blockchain in the future.

### [**`did:erc725:`**](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/topics-and-advance-readings/DID-Method-erc725.md)
###### For Ethereum, by Markus Sabadello, Fabian Vogelsteller, Peter Kolarov

> Decentralized Identifiers (DIDs, see [1]) are designed to be compatible with any distributed ledger or network (called the target system). In the Ethereum community, a pattern known as ERC725 (see [2]) utilizes smart contracts for standard key management functions. We propose a new DID method that allows ERC725 identities to be treated as valid DIDs. One advantage of this DID method over others appears to be the ability to use the full flexibility of Ethereum smart contracts for key management purposes.

### [**`did:example:`**](https://w3c.github.io/did-core/#a-simple-example)
###### DID Specification, by W3C Credentials Community Group

> A DID is a simple text string consisting of three parts, the:
> - URI scheme identifier (did)
> - Identifier for the DID method
> - DID method-specific identifier.
> 
> **EXAMPLE 1: A simple example of a decentralized identifier (DID)**

> ```
> did:example:123456789abcdefghi
> ```

> The example DID above resolves to a DID document. A DID document contains information associated with the DID, such as ways to cryptographically authenticate the DID controller, as well as services that can be used to interact with the DID subject.
>
> **EXAMPLE 2: Minimal self-managed DID document**
> ```
> {
>   "@context": "https://www.w3.org/ns/did/v1",
>   "id": "did:example:123456789abcdefghi",
>   "authentication": [{
>     
>     "id": "did:example:123456789abcdefghi#keys-1",
>     "type": "Ed25519VerificationKey2018",
>     "controller": "did:example:123456789abcdefghi",
>     "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
>   }],
>   "service": [{
>     
>     "id":"did:example:123456789abcdefghi#vcs",
>     "type": "VerifiableCredentialService",
>     "serviceEndpoint": "https://example.com/vc/"
>   }]
> }
> ```

### [**`did:ipid:`**](https://did-ipid.github.io/ipid-did-method/)
###### For IPFS, by TranSendX

> The Interplanetary Identifiers DID method (did:ipid:) supports DIDs on the public and private Interplanetary File System (IPFS) networks. IPFS is the distributed content addressable permanent web. More specifically, the IPID DID method utilizes the Interplanetary Linked Data (IPLD) suite of tools. The IPID DID method has minimal design goals: a DID trust anchor based on the IPFS and Libp2p protocol. In and of itself, this is not a blockchain solution. However, blockchains and other distributed ledger technologies could be utilized to anchor the artifacts of this DID methods for further enhanced security.

### [**`did:life:`**](https://lifeid.github.io/did-method-spec/)
###### For RChain, by lifeID Foundation

> lifeID is a decentralized, blockchain-based protocol that acts as an open identity provider. The protocol enables the creation and use of self-sovereign identities as well as the issuance of verifiable credentials to those identities. The blockchain-based components of the protocol include smart contracts for storage, revocation, and recovery of keys and credentials. These contracts may be run on any open, permissionless blockchain. The purpose of this protocol is to allow users to transact their identity in a way that minimizes data disclosure, is cryptographically secure, and enables censorship-resistant decentralized identity provisioning and recovery. The purpose of this specification is to describe how lifeID DIDs are created and the technical requirements to operate on the lifeID platform.

### [**`did:sov:`**](https://sovrin-foundation.github.io/sovrin/spec/did-method-spec-template.html)
###### For Sovrin, by Mike Lodder

> Sovrin is a public ledger designed specifically and only for privacy-preserving self-sovereign identity. The Sovrin Ledger is governed by the international non-profit Sovrin Foundation. As the only public ledger designed exclusively for self-sovereign identity, Sovrin is optimized for DIDs and DID Documents. DIDs are created, stored, and used with verifiable claims. This specification covers how these DIDs are managed. It also describes related features of Sovrin of particular interest to DID owners, guardians, and developers.

### [**`did:ethr:`**](https://github.com/decentralized-identity/ethr-did-resolver/blob/master/doc/did-method-spec.md)
###### For Ethereum, by uPort

> In the Ethereum community, a pattern known as ERC1056 (see [2]) utilizes a smart contract for a lightweight identity management system intended explicitly for off-chain usage.
> 
> The described DID method allows any Ethereum smart contract or key pair account to become a valid identity. An identity needs no registration. In the case that key management or additional attributes such as "service endpoints" are required, we deployed ERC1056 smart contracts on:

Mainnet • Ropsten • Rinkeby • Goerli • Kovan • RSK • Alastria • Telsius • ARTIS tau1 • ARTIS sigma1

> Since each Ethereum transaction must be funded, there is a growing trend of on-chain transactions that are authenticated via an externally created signature and not by the actual transaction originator. This allows for 3rd party funding services, or for receivers to pay without any fundamental changes to the underlying Ethereum architecture. These kinds of transactions have to be signed by an actual key pair and thus cannot be used to represent smart contract based Ethereum accounts. ERC1056 proposes a way of a smart contract or regular key pair delegating signing for various purposes to externally managed key pairs. This allows a smart contract to be represented, both on-chain as well as off-chain or in payment channels through temporary or permanent delegates.

* [decentralized-identity/ethr-did-resolver](https://github.com/decentralized-identity/ethr-did-resolver) - DID resolver for Ethereum Addresses with support for key management (and DID reference implementation)

### [**`did:v1:`**](https://w3c-ccg.github.io/did-method-v1/)
###### For Veres One, by Digital Bazaar

> There are two primary classes of DID-based identifiers in Veres One. The first type of identifier is called a cryptonym-based identifier. This identifier is a SHA-256 hash of a public key. Cryptonym-based identifiers are not required to be registered on the ledger and may be used as unregistered pseudonymous pairwise identifiers. These identifiers may also be registered on the ledger and MUST contain a authentication key with a public key fingerprint equal to the value of the cryptonym-based identifier.
> 
> **EXAMPLE 1: A valid Veres One Cryptonym-based Decentralized Identifier**

> ```
> did:v1:nym:4jWHwNdrG9-6jd9I7K1si3kTRneNwftZV9m6rkrAfWQ
> ```

> The second type of identifier on Veres One is a UUID-based identifier and may be used by entities that want to store metadata on the ledger. These sorts of identifiers are often used, but not limited to, storing and refering to Capabilities and Revocation lists.
> 
> **EXAMPLE 2: A valid Veres One UUID-based Decentralized Identifier**

> ```
> did:v1:uuid:804c6ac3-ce3b-46ce-b134-17175d5bee74
> ```

### [**`did:com:`**](https://github.com/commercionetwork/Commercio.network-DID-Method-Specification/)
###### For commercio.network, by Commercio Consortium

> Commercio.network is a cosmos based sovereign blockchain network, built on the base of cosmos sdk and tendermint state machine replication engine, adopting Proof of Stake as a consensus algorithm.
> 
> Commercio.network, aims to be known as "The Documents Blockchain" and is to become "the easiest way for companies to manage their business documents using the blockchain technology".
> 
> Commercio.newtork ultimate goal is not just to share documents, but to create a network of trusted organizations, on the base of a web of trust, build on the Decentralized Identifier and Verifiable Credentials standard pillars.
> 
> In this document we specify the DID Method for Commercio.network, in comformance to the requirements specified in the DID specification[4] currently published by the W3C Credentials Community Group. For more information about DIDs and DID method specifications, please see DID Primer[6] and DID Specification[4].

### [**`did:ont:`**](https://github.com/ontio/ontology-DID/blob/master/docs/en/DID-ONT-method.md)
###### For Ontology, by Ontology Foundation

> This specification defines how Ontology blockchain[1] stores DIDs and DID documents, and how to do CRUD operations on DID documents. More importantly, this specification confirms to the requirements specified in the DID specification[2] currently published by the W3C Credentials Community Group.
> 
> Ontology provides high-performance public blockchains that include a series of complete distributed ledgers and smart contract systems. Ontology blockchain framework supports public blockchain systems and is able to customize different public blockchains for different applications.

> ```
> ont-did   = "did:ont:" id-string 
> id-string = 1* idchar
> idchar    = 1-9 / A-H / J-N / P-Z / a-k / m-z 
> ```

### [**`did:vvo:`**](https://vivvo.github.io/vivvo-did-scheme/spec/did-method-spec-template.html)
###### For Vivvo, by Vivvo Application Studios

> Vivvo is a private ledger designed specifically and only for privacy-preserving self-sovereign identity. The Vivvo Ledger is governed by Vivvo Application Studios. As a private ledger designed exclusively for self-sovereign identity, Vivvo is optimized for DIDs and DID Documents. DIDs are created, stored, and used with verifiable claims. This specification covers how these DIDs are managed. It also describes related features of Vivvo of particular interest to DID owners, guardians, and developers.

> ```
> vivvo-did = "did:vvo:idstring" *(":" subnamespace)
> idstring = 21*22(char)
> subnamespace = ALPHA *(ALPHA / DIGIT / "_" / "-")
> char = "1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9" / "A" / "B" / "C"
>     / "D" / "E" / "F" / "G" / "H" / "J" / "K" / "L" / "M" / "N" / "P" / "Q"
>     / "R" / "S" / "T" / "U" / "V" / "W" / "X" / "Y" / "Z" / "a" / "b" / "c"
>     / "d" / "e" / "f" / "g" / "h" / "i" / "j" / "k" / "m" / "n" / "o" / "p"
>     / "q" / "r" / "s" / "t" / "u" / "v" / "w" / "x" / "y" / "z"
> ```

### [**`did:aergo:`**](https://github.com/aergoio/aergo-identity/blob/master/doc/did-method-spec.md)
###### For https://www.aergo.io/, by https://www.blocko.io/

> The described DID method allows any Aergo smart contract or key pair account to become a valid identity. An identity needs no registration. In the case that key management or additional attributes such as "service endpoints" are required, we deployed did registry smart contracts on:
> 
> Mainnet: `AmgUfj2ghDBRJsmpuSvBZq1Zp67kMc8QX72r1Eh7aS24ueADStPv`
> Testnet: `AmhPkt8JXujkN6TWEJbynaXqnQUh1AfUckJEyDvTYoA3PyXXf7as`
>
> Since each Aergo transaction must be funded, in order to update attributes, account balance must be greater than zero.

### [**`did:icon:`**](https://github.com/icon-project/icon-DID/blob/master/docs/ICON-DID-method.md)
###### For ICON, by ICONLOOP

> ICON[1,2,3] is a decentralized network that connects various independent communities to enable interoperability between them. ICON DID is a decentralized identifier devised to provide a way to uniquely identify a person, an organization, or a digital device across the communities connected to the ICON network. ICON DID method specification conforms to the DID and the DID Documents Spec[4]. This document describes how ICON blockchain manages the DIDs and the DID documents, and specifies a set of rules for how a DID is created, queried, updated, and revoked.

### [**`did:is:`**](https://github.com/block-core/blockcore-did-method)
###### For Blockcore, by Blockcore

> Decentralized identifiers (DIDs) are a new type of identifiers that enables verifiable, self-sovereign digital identity. Blockcore supports decentralized identities through the Blockcore Storage feature.
> 
> This specification describes how the Blockcore Identity framework aligns with the DID specification and how the Blockcore Universal Resolver works.
> 
> This specification conforms to the requirements specified in the DIDs specification currently published by the W3C Credentials Community Group.
> 
> The Blockcore Identity registry is a permissionless and borderless runtime for identities.

> ```
> did:is:PLBNc1Ph6whu1vbQGEuRywTTHCEnfDDuXh
> ```

### [**`did:iwt:`**](https://github.com/infowallet/did_method/blob/master/did_method.md)
###### For InfoWallet, by Raonsecure

> InfoWallet is a decentralized network system for Self-Sovereign identity and Verifiable Claims. It can replace a legacy centralized credential system that with trusted blockchain node. In the InfoWallet system, several types of certificates are issued. DID(Decentralized Identifiers) is used as the unique identifier of the certificate. Also DID allows to obtain public key information for secure exchange of information between users.

> ```
> iwt-did = "did:iwt:" id-string id-string = 1* idchar idchar = 1-9 / A-H / J-N / P-Z / a-k / m-z
> 
> Example did:iwt:4EFNaYeA9hDp6F55JAB38EFtNcYEbbM9nwKr
> ```

### [**`did:ockam:`**](https://github.com/ockam-network/did-method-spec/blob/master/README.md)
###### For Ockam, by Ockam

> A DID that uses this method MUST begin with the following prefix: did:ockam:. Per the DID specification, this prefix MUST be in lowercase. The format of remainder of the DID, after this prefix, is specified below in the section on Method Specific Identifiers.

> Ockam DIDs conform with the Generic DID Scheme described in the DID spec. The format of the ockam-specific-idstring is described below in ABNF:
> 
> ```
> ockam-did               = "did:ockam:" ockam-specific-idstring
> 
> ockam-specific-idstring = *(zone ":") idstring
> 
> zone                    = 1*zonechar
> zonechar                = %x61-7A / DIGIT ; 61-7A is a-z in US-ASCII
> 
> idstring                = 28*31(base58char)
> base58char              = "1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9" / "A" / "B" / "C"
>                           / "D" / "E" / "F" / "G" / "H" / "J" / "K" / "L" / "M" / "N" / "P" / "Q"
>                           / "R" / "S" / "T" / "U" / "V" / "W" / "X" / "Y" / "Z" / "a" / "b" / "c"
>                           / "d" / "e" / "f" / "g" / "h" / "i" / "j" / "k" / "m" / "n" / "o" / "p"
>                           / "q" / "r" / "s" / "t" / "u" / "v" / "w" / "x" / "y" / "z"
> ```

### [**`did:ala:`**](https://github.com/alastria/alastria-identity/wiki/Alastria-DID-Method-Specification-(Quorum-version))
###### For Alastria, by Alastria National Blockchain Ecosystem

> This document is divided into two parts:
> - The first one defines the Alastria DID Method Specification, describing the Alastria DID Scheme and the Alastria DID Document.
> - The second part describes the format for Alastria Credentials and Presentations in the current Alastria Red T, based on Quorum.
> - The third part describes the Credentials and Presentation Life Cycle and the Private Credential Multi Hashes (PSM Hashes) used to anchor Credential and Presentation actions ensuring privacy.
> 
> The objective of this document is to be aligned with the work on Decentralized IDs (DIDs) and Verifiable Credentials being carried out by the Verifiable Credentials Working Group. The specs are already on the CR (Candidate Recommendation) phase and they may still change. However, its maturity is enough to assume that the changes are going to be minor so it makes sense to align the Alastria DID Method Specification as much as possible to those specifications.

### [**`did:op:`**](https://github.com/oceanprotocol/OEPs/blob/master/7/v0.2/README.md)
###### For Ocean Protocol, by Ocean Protocol

> **Requirements are:**
> - The DID resolving capabilities MUST be exposed in the client libraries, enabling to resolve a DDO directly in a totally transparent way
> - ASSETS are DATA objects describing RESOURCES under control of a PUBLISHER
> - KEEPER stores on-chain only the essential information about ASSETS
> - PROVIDERS store the ASSET metadata off-chain
> - KEEPER doesn't store any ASSET metadata
> - OCEAN doesn't store ASSET contents (e.g. files)
> - An ASSET is modeled in OCEAN as on-chain information stored in the KEEPER and metadata stored in OCEANDB
> - ASSETS on-chain information only can be modified by OWNERS or DELEGATED USERS
> - ASSETS can be resolved using a Decentralized ID (DID) included on-chain and off-chain
> - A DID Document (DDO) should include the ASSET metadata
> - Any kind of object registered in Ocean SHOULD have a DID allowing one to uniquely identify that object in the system
> - ASSET DDO (and the metadata included as part of the DDO) is associated to the ASSET information stored on-chain using a common DID
> - A DID can be resolved to get access to a DDO
> - ASSET DDOs can be updated without updating the on-chain information
> - ASSET information stored in the KEEPER will include a checksum attribute
> - The ASSET on-chain checksum attribute SHOULD include a one-way HASH calculated using the DDO content
> - After the DDO resolving, the DDO HASH can be calculated off-chain to validate if the on-chain and off-chain information is aligned
> - A HASH not matching with the checksum on-chain means the DDO was modified without the on-chain update
> - The function to calculate the HASH MUST BE standard

### [**`did:jlinc:`**](https://did-spec.jlinc.org/)
###### For JLINC Protocol, by Victor Grey

> JLINC is a protocol for sharing data protected by an agreement on the terms under which the data is being shared.
> 
> This document specifies methods for creating and editing Decentralized IDs (DIDs) suitable for use with the JLINC protocol. It conforms to the requirements specified in the DID specification currently published by the W3C Credentials Community Group.

> ```
> jlinc-did = "did:jlinc:" id-string
> id-string = 1* idchar
> idchar    = ALPHA / DIGIT / "-" / "_"
> ```

### [**`did:ion:`**](https://github.com/decentralized-identity/ion-did-method)
###### For Bitcoin, by Various DIF contributors

> ION is a public, permissionless, Decentralized Identifier (DID) network that implements the blockchain-agnostic Sidetree protocol on top of Bitcoin (as a 'Layer 2' overlay) to support DIDs/DPKI (Decentralized Public Key Infrastructure) at scale.
> 
> IMPORTANT NOTE: The majority of ION's code is developed under the blockchain-agnostic Sidetree protocol's repo: [https://github.com/decentralized-identity/sidetree](https://github.com/decentralized-identity/sidetree), which this project uses internally with the code required to run the protocol on Bitcoin, as the ION network.
> 
> **Key Points:**
> - ION is public and permissionless - the system is decentralized, no company, organization, or group owns/controls the identifiers and DPKI entries in the system, and no one dictates who can participate.
> - ION doesn't introduce new tokens/coins - Bitcoin is the only unit of value relevant in the operation of the on-chain aspects of the ION network.
> - ION is not a sidechain or consensus system - the network nodes do not require any additional consensus mechanism.


### [**`did:jolo:`**](https://github.com/jolocom/jolo-did-method/blob/master/jolocom-did-method-specification.md)
###### For Ethereum, by Jolocom

> The Jolocom distributed identity system aims to provide a secure, robust and flexible implementation of the DID and Verifiable Claims specifications published by the W3C and the Decentralised Identity Foundation. It’s core technologies are the Ethereum blockchain and the Interplanetary File System (IPFS).
> 
> The Jolocom DID method uses IPFS as a decentralised CAS layer for DID Documents. A deployed smart contract provides a mapping from a DID to an IPFS hash address of the corrosponding DID Document. This enables DID Documents on IPFS to be effectively addressed via their DIDs.
> 
> Jolocom DIDs are identifiable by their did:jolo: method string and conform to the [Generic DID Scheme](https://w3c-ccg.github.io/did-spec/#the-generic-did-scheme).


### [**`did:bryk:`**](https://github.com/bryk-io/did-method/blob/master/README.md)
###### For bryk, by Marcos Allende, Sandra Murcia, Flavia Munhoso, Ruben Cessa

> The method specification provides all the technical considerations, guidelines and recommendations produced for the design and deployment of the DID method implementation. The document is organized in 3 main sections.
> 
> - DID Schema. Definitions and conventions used to generate valid identifier instances.
> - DID Document. Considerations on how to generate and use the DID document associated with a given identifier instance.
> - Agent Protocol. Technical specifications detailing how to perform basic network operations, and the risk mitigation mechanisms in place, for tasks such as:
>   - Publish a new identifier instance.
>   - Update an existing identifier instance.
>   - Resolve an existing identifier and retrieve the latest published version of its DID Document.

> **Schema**
> ```
> did                = "did:" method-name ":" method-specific-id
> method-name        = 1*method-char
> method-char        = %x61-7A / DIGIT
> method-specific-id = *idchar *( ":" *idchar )
> idchar             = ALPHA / DIGIT / "." / "-" / "_"
> did-url            = did *( ";" param ) path-abempty [ "?" query ]
>                      [ "#" fragment ]
> param              = param-name [ "=" param-value ]
> param-name         = 1*param-char
> param-value        = *param-char
> param-char         = ALPHA / DIGIT / "." / "-" / "_" / ":" /
>                      pct-encoded
> ```

> ```
> did:example:123456789abcdefghi
> ```

> Expanding on the previous definitions the bryk DID Method specification use the following format.
> ```
> did                = "did:bryk:" [tag ":"] specific-idstring
> tag                = 1*tagchar
> specific-idstring  = depends on the particular use case
> tagchar            = ALPHA / DIGIT / "." / "-"
> ```

### [**`did:peer:`**](https://identity.foundation/peer-did-method-spec/)
###### For Peer 2 Peer, by Daniel Hardman

> Most documentation about decentralized identifiers (DIDs) describes them as identifiers that are rooted in a public source of truth like a blockchain, a database, a distributed filesystem, or similar. This publicness lets arbitrary parties resolve the DIDs to an endpoint and keys. It is an important feature for many use cases.
> 
> However, the vast majority of relationships between people, organizations, and things have simpler requirements. When Alice(Corp|Device) and Bob want to interact, there are exactly and only 2 parties in the world who should care: Alice and Bob. Instead of arbitrary parties needing to resolve their DIDs, only Alice and Bob do. Peer DIDs are perfect in these cases. In many ways, peer DIDs are to public, blockchain-based DIDs what Ethereum Plasma or state channels are to on-chain smart contracts— or what Bitcoin's Lightning Network is to on-chain cryptopayments. They move the bulk of interactions off-chain, but offer options to connect back to a chain-based ecosystem as needed. Peer DIDs create the conditions for people, organizations and things to have full control of their end of the digital relationships they sustain.

### [**`did:selfkey:`**](https://github.com/SelfKeyFoundation/selfkey-identity/blob/develop/DIDMethodSpecs.md)
###### For Ethereum, by SelfKey

> The following document defines a DID method for the SelfKey Identity platform. Although this method provides support to the SelfKey ecosystem and its related applications, the underlying DID platform is fully decentralized, and it's designed to serve as a DID layer for other systems that might find it valuable.
> 
> The following specifications are subject to change in the future, yet they MUST comply with the latest version of the [generic DID specs](https://w3c-ccg.github.io/did-spec/) as specified by the W3C Credentials Community Group.
> 
> The functionality for this method is provided by the DIDLedger smart contract found in [this repository](https://github.com/SelfKeyFoundation/selfkey-identity).

### [**`did:meta:`**](https://github.com/METADIUM/meta-DID/blob/master/doc/DID-method-metadium.md)
###### For Metadium, by Metadium Foundation

> Metadium is the next-generation identity system powered by blockchain technology. Metadium Decentralized Identifiers is a distributed identifier designed to provide a way for a community connected to the Metadium Ecosystem to uniquely identify an individual, organization, or digital device. The role of a Metadium DID is to provide a service that supports user-authentication and personal information verification.
> 
> The Metadium DID method specification conforms to the requirements specified in the DID specification [1], currently published by the W3C Credentials Community Group. For more information about DIDs and DID method specifications, please see the DID Primer [2]

> ```
> meta-did = "did:meta:" + meta-specific-idstring
> meta-specific-idstring = meta-network + ":" + MIN
> meta-network = "mainnet" | "testnet"
> meta-address = 40*HEXDIG
> ```
> The MIN is case-insensitive, but it is recommended to use mixed-case checksum for address encoding (see [3]).

### [**`did:tys:`**](https://github.com/chainyard-tys/tys/blob/master/README.md)
###### For DID Specification, by Chainyard

> “Trust Your Supplier” aka “TYS” is actively in development at Chainyard, a leading Blockchain development firm located in RTP North Carolina. The network is undergoing beta testing and will go live in the next couple of months.
> 
> The TYS network is a cross industry source of supplier information and identity helping to simplify and accelerate the onboarding and lifecycle management process. TYS is a fit-for-purpose blockchain optimized for sharing supplier credentials in a supply chain environment. TYS DIDs may be used by Suppliers, Buyers, Verifiers, Banks and other organizations to establish identities for verifiable claims made by any party.
> 
> TYS is implemented on Hyperledger Fabric, a permissioned blockchain technology under the Linux Foundation’s Hyperledger Project. The “Smart Contract” Functions are written in “Golang” and all client APIs are provided as REST APIs written in “Javascript” running on “NodeJS.

### [**`did:git:`**](https://github.com/dhuseby/did-git-spec/blob/master/did-git-spec.md)
###### For DID Specification, by Internet Identity Workshop

> The Git revision control tool is designed to function in a decentralized peer-to-peer fashion to facilitate collaboration in the frequently-disconnected world. Git uses a directed acyclic graph (DAG) of commits that represent the changes to the folders and files in the repository. Because it uses blockchain-like hash-linking of commits, Git is effectively a blockchain and distributed ledger with the patch review and merge process functioning as the consensus mechanism. This makes it a great tool for tracking the provenance of data inside the repository. Git also records the author and other meta data such as digital signatures with each commit linking identity of committers to each commit. Git repos therefore contain all of the information needed to serve as the single source of truth for the provenance of the data it contains and the identities of the contributors that created it.

### [**`did:tangle:`**](https://github.com/TangleID/TangleID/blob/develop/did-method-spec.md)
###### For IOTA Tangle, by BiiLabs Co., Ltd.

> IOTA is a public distributed ledger that utilizes an invention called the Tangle at its core, address scalability issues and having no transaction fee, that encourages adoption of the technology in the industry. TangleID is intended to implement DIDs and DID Documents.
> 
> TangleID also optimizes MAM for key management and related features across the Tangle. Masked Authenticated Messaging (MAM) is a data communication protocol which adds functionality to broadcast and access data streams over the Tangle which adds integrity to these message streams. The owner of seed in MAM is able to create a channel structure like above to transfer the messages. TangleID stores and manages corresponding DID Documents on the MAM channels, and use the initial channel id as the DID’s idstring, each revision of the DID document is recorded on the message of the endpoint afterward.

### [**`did:emtrust:`**](https://github.com/Halialabs/did-spec/blob/gh-pages/readme.md)
###### For Hyperledger Fabric, by Halialabs Pte Ltd.

> The Emtrust DID method utilizes Hyperledger fabric as the DLT implementation, having an identity channel which is shared among the identity nodes with participating organizations. The DID document along with metadata of third party endorsements resides on ledger and the private information of users are kept on the mobile or persona devices which never leaves the device. The Interaction of DID and blockchain ledger happens via the API servers hosted by any participating organizations.

### [**`did:ttm:`**](https://github.com/TokenTM/TM-DID/blob/master/docs/en/DID_spec.md)
###### For TMChain, by Token.TM

> ```
> did:ttm:0xe32df42865e97135acfb65f3bae71bdc86f4d49150ad6a440b6f15878109880a
> ```

> <32 byte hexadecimal string> corresponds to keccak256 and the hash value of Ethereum address connected by random numbers generated in the DID contract.
> 
> DID is registered in the contract and controlled by a single Ethereum address, which is set by default to the address where the createDID method was originally called. Then, this address can transfer control to a different address, or update/delete the corresponding DID in the contract.


> The DID ledger is implemented as a simple layer of persistent identity registration on the Ethereum blockchain network. Meanwhile it can be extended to contain other data and functions. Scalability is achieved by using an identity contract as a controller for DID on the ledger. In particular, ERC725 combined with private key management contract, for example, ERC734 is expected to involve additional features with common conditions (such as defines service endpoint, private key rotation, delegation and licensing, etc.). At the meantime, it gives the permit of exploiting other standards, and even allows the owner of DID to transforms contract implementation to another without losing its identifier.


### [**`did:wlk:`**](https://weelink-team.github.io/weelink/DIDDesignEn)
###### For Weelink Network, by Weelink

> Weelink DID is a new blockchain-based authentication method that follows all the requirements of W3C. Based on Weelink Wallet, our method provides a series of APIs and services for a fast and secure authentication process.
> 
> The rapid development of Internet has provided unparalled convenience to the public, yet it is also inevitably bringing some potential problems. One of them is the leaking of private information that comes with traditional authentication systems. Taking advantage of blockchain’s decentralization and security characteristics, we thus propose our secure authentication method.

### [**`did:pistis:`**](https://github.com/uino95/ssi/blob/consensys/dashboard/server/pistis/pistis-did-resolver/README.md)
###### For Ethereum, by Andrea Taglia, Matteo Sinico
 
> This specification defines how Pistis deals with DID and DID Documents and how it interacts with the Ethereum blockchain. Also CRUD operations on DID documents are described. This specification confirms to the requirements specified in the DID specification[1] currently published by the W3C Credentials Community Group.
> 
> Pistis is a credential management system based on the Ethereum blockchain. It provides a set of novel smart contracts to handle efficient multi signature operations, delegates management, permissioned access to extensible services based upon the Decentralized IDentifier specification.

### [**`did:holo:`**](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/draft-documents/did:hc-method.md)
###### For Holochain, by Holo.Host

> ```
> holo-did = "did:holo:" holo-specific-idstring
> holo-specific-idstring = [ holo-network  ":" ] holo-address
> holo-network  = "mainnet" / "testnet"
> holo-address  = (Hex-encoded smart contract address)
> ```

> All transactions on Holochain are signed by a user's key. Therefore, by learning a holo DID, an observer/attacker is able to link the user's Holochain activities with potential DID-based applications such as DID Auth or Verifiable Credentials. Users should be aware that he/she can publish their own data associated with their public key on a specific Holochain network.

### [**`did:web:`**](https://github.com/w3c-ccg/did-method-web)
###### For Web, by Oliver Terbu, Mike Xu, Dmitri Zagidulin, Amy Guy

> The target system of the Web DID method is the web host that the domain name described by the DID resolves to when queried through the Domain Name System (DNS).

> The method specific identifier MUST match the common name used in the SSL/TLS certificate, and it MUST NOT include IP addresses or port numbers. Directories and subdirectories MAY optionally be included, delimited by colons rather than slashes.
>
> web-did = "did:web:" domain-name
> web-did = "did:web:" domain-name * (":" path)
>
> **EXAMPLE 2: Example Web Method DIDs**
> ```
> did:web:w3c-ccg.github.io
> 
> did:web:w3c-ccg.github.io:user:alice
> ```

### [**`did:io:`**](https://github.com/iotexproject/iotex-did/blob/master/README.md)
###### For IoTeX, by IoTeX Foundation

> Our DID design allows each manufacture or entity to have its own namespace, which stores and manages DIDs through a self-managed DID contract. A self-managed contract could have customized business logic to adapt the application's needs but has to implement the SelfManagedDID interface, defined as follows:

> ```
> interface SelfManagedDID {
>     function createDID(string id, bytes32 hash, string uri) public returns (string);
>     function deleteDID(string did) public;
>     function updateHash(string did, bytes32 hash) public;
>     function updateURI(string did, string uri) public;
>     function getHash(string did) public view returns (bytes32);
>     function getURI(string did) public view returns (string);
> }
> ```

### [**`did:vaultie:`**](https://github.com/vaultie/vaultie-did-method/blob/master/vaultie-did-method-specification.md)
###### For Ethereum, by Vaultie Inc.

> Vaultie DID method uses IPFS as a decentralised storage for DID Documents. An Ethereum transaction, that does not require any additional Smart Contracts, provides a mapping from a DID to an IPFS hash address of the corrosponding DID Document. This enables DID Documents on IPFS to be effectively addressed via their DIDs. While this method requires additional step in order to lookup DID Document, the method is much more cost effective than using Smart Contracts and Ethereum's expensive storage.

### [**`did:moac:`**](https://github.com/DavidRicardoWilde/moac-did/blob/master/did-moac-method.md)
###### For MOAC, by MOAC Blockchain Tech, Inc.

> The MOAC DID method uses MOAC blockchain as a decentralized storage layer for DID Documents. A deployed smart-contract provides a mapping from a DID to an MOAC blockchain hash address of the corrosponding DID Document. This enables DID Documents on MOAC blockchain to be effectively addressed via their DIDs.

### [**`did:omn:`**](https://github.com/OmniOneID/did_method/blob/master/did_method.md)
###### For OmniOne, by OmniOne

> OmniOne is a decentralized network system for Self-Sovereign identity and Verifiable Claims. It can replace a legacy centralized credential system that with trusted blockchain node. In the OmniOne system, several types of certificates are issued. DID(Decentralized Identifiers) is used as the unique identifier of the certificate. Also DID allows to obtain public key information for secure exchange of information between users.

### [**`did:work:`**](https://workday.github.io/work-did-method-spec/)
###### For Hyperledger Fabric, by Workday, Inc.

> Workday offers a decentralized Credentialing Platform with a Blockchain based trust layer. A key component of the platform is the WayTo by Workday mobile app which allows the user to store verifiable identity documents, encrypted using their own personal encryption key, which is managed in the Trusted Execution Environment (TEE) of their mobile device. The mobile app can hold official documents, training certifications, verified accomplishments and other credentials. The user can choose what to share, and with whom to share it with. Users of the Workday Credentialing Platform will have a DID and a corresponding DID Document on a permissioned ledger, which credential verifiers can use to validate users’ cryptographic signatures, included in their credentials.

### [**`did:vid:`**](https://github.com/vpayment/did-method-spec/blob/master/vid.md)
###### For VP, by VP Inc.

> The system aims to provide secure authentication and various payment services based on the DID and Verifiable Claims specificiatons published by the W3C and the Decentralised Identity Foundation. VP DID is a decentralized identifier devised to provide a way to uniquely identify a person, an organization. VP DID document contains information for providing various payment methods among network participants in a decentralized way. This specification defines how VP blockchain stores DIDs and DID documents, and how to do CRUD operations on DID documents.

> The namestring that shall identify this DID method is: vp. A DID that uses this method MUST begin with the following prefix: did:vp. Per the DID specification, this string MUST be in lowercase. The remainder of the DID, after the prefix, is specified below.
> ```
> did                 = "did:" method-name ":" method-specific-id
> method-name         = vid
> method-specific-id  = 40*HEXDIGIT
> ```

### [**`did:ccp:`**](https://did.baidu.com/did-spec/)
###### For Quorum, by Baidu, Inc.

> Application scenarios:
> 
> - Digital identity
> - Joint member key customer system
> - Financial KYC
> - Exchange
> - Smart City
> - IoT deviceless identity management
> 
> Program features:
> 
> Building a decentralized ID system based on blockchain and consortium chains will have almost equal control over the system and enhance cooperation intentions.
Blockchain asymmetric encryption technology combines public and private keys to ensure the authenticity and reliability of ID and certification.
Form a richer user portrait, with multiple tags (VIP authentication, privilege authentication, asset authentication...) and one ID.

> ```
> did:ccp:1FsbKR6UpV6GW8o8szccdxXkquzTg2VZLL
> ```

> Where `<method-specific-id>` = `base58(ripemd160(sha256(<Base DID Document>)))` (Refer to Bitcoin, use double hash).


### [**`did:jnctn:`**](https://github.com/jnctn/did-method-spec/)
###### For Jnctn Network, by Jnctn Limited

> The system provides secure credential management services based on the DID and Verifiable Claims specifications published by the W3C and the Decentralised Identity Foundation. JNCTN DID method enables an interoperability bridge between the worlds of centralized, federated, and decentralized identifiers with self soverign identity services. JNCTN DID document contains information for accessing JNCTN DID network methods, how JNCTN stores DIDs and DID documents, and how to do CRUD operations on JNCTN DID documents. This specification is intended to be conformant with the DID Specification at https://w3c-ccg.github.io/did-spec/.

> The namestring that shall identify this DID method is: jnctn. A DID that uses this method MUST begin with the following prefix: did:jnctn. Per the DID specification, this string MUST be in lowercase. The remainder of the DID, after the prefix, is specified below.
> ```
> did                 = "did:" method-name ":" method-specific-id
> method-name         = jnctn
> method-specific-id  = 36*HEXDIGIT
> 
> ```

### [**`did:evan:`**](https://github.com/evannetwork/evan.network-DID-method-specification/blob/master/evan_did_method_spec.md)
###### For evan.network, by evan GmbH

> evan.network is a blockchain for digitalization and automation of business transactions. The network members create digital twins for their machines and products and develop standards for cross-company transactions. The open technology allows integration into existing business models. evan.network guarantees 100% reliable and permanently secured information.
> 
> This document specifies the DID method for evan.network, including how an evan.network DID is assembled, several sample documents, details about CRUD operations on DID, as well as security and privacy considerations, as required by the W3C DID specification. For more information regarding DID, please refer to the W3C DID working draft.

> ```
> evan-did = "did:evan:" evan-specific-identifier
> evan-specific-identifier = [ evan-network ":" ] evan-identifier
> evan-network = "core" / "testcore"
> evan-identifier = evan-account / evan-asset
> evan-account = "0x"20*HEXDIG
> evan-asset = "0x"32*HEXDIG
> ```

### [**`did:elastos:`**](https://github.com/elastos/Elastos.DID.Method/blob/master/DID/Elastos-DID-Method-Specification_en.md)
###### For Elastos ID Sidechain, by Elastos Foundation

> DID is completely under the control of the DID subject, without reliance on any centralized registration body, commercial identity provider, or organization issuing certificates. The DID is described in the DID documents. Each DID document includes at least two items: encryption materials and verification methods. The encryption materials integrated with the verification methods provides a set of identify verification mechanisms (such as a public key, anonymous biological identification agreement, etc.), with other optional parts that can be used according to the needs of the application and of the user.

> There are two goals for the creation of this specification. The first is to define an internal Elastos system standard for the DID documents description format and a basic DID property set, allowing Elastos ecosystem apps to understand the basic digital identity information defined in the standard set, thereby achieving standardization of digital identities in the Elastos ecosystem. The secondary goal is to define a set of general operation methods that can be used for any dApp to reference to the Elastos DID service.

### [**`did:kilt:`**](https://github.com/KILTprotocol/kilt-did-driver/blob/master/DID%20Method%20Specification.md)
###### For KILT Blockchain, by BOTLabs GmbH

> KILT DIDs are stored on KILT Protocol's blockchain that is public and by definition decentralized. The KILT Blockchain runs in a proof-of-authority manner and will become permissionless, see `§ Status of this document` in this specification document.
> 
> KILT Blockchain nodes implement a DID module to create, store, query and manage DIDs in the form of on-chain DID items. A DID item is a mapping between the DID owner's public address and its public signature key `sign_key`, its public encryption key `box_key`, and an optional location for the associated DID Document `doc_ref`:
> ```
> owner => (sign_key, box_key, doc_ref)
> ```

### [**`did:elem:`**](https://github.com/decentralized-identity/element/blob/master/docs/did-method-spec/spec.md)
###### For Element DID, by Transmute

> Element is an implementation of the Sidetree protocol that uses the Ethereum blockchain as the ledger layer and IPFS as the Content-addressable storage layer

> A DID that uses this method MUST begin with the following prefix: did:elem. Per the DID specification, this string MUST be in lowercase.
> 
> An additional optional network specific identifier may be added as such
> 
> * `did:elem:ropsten:EiBOWH8368BI9NSaVZTmtxuqwpfN9NwAwy4Z95_VCl6A9g`
> * `did:elem:mainnet:EiBOWH8368BI9NSaVZTmtxuqwpfN9NwAwy4Z95_VCl6A9g`
> * `did:elem:EiBOWH8368BI9NSaVZTmtxuqwpfN9NwAwy4Z95_VCl6A9g`
> By default, if the network specific identifier is not present, then the default is ropsten. The default may change in the future once mainnet is supported.
> 
> The remainder of a DID after the prefix, called the did unique suffix, MUST be SHA256 hash of the encoded create payload (see below)

### [**`did:github:`**](https://docs.github-did.com/did-method-spec/)
###### For Github, by Transmute

> The `github` method is meant to make working with DIDs very simple at the cost of trusting Github.com for assisting in resolving DID Documents.
> 
> Many developers are familar with Github, and its 2 supported public key cryptosystems, GPG and SSH.
> 
> Linked Data Signatures are difficult to work with when operating a server or running a local node of some distributed system / blockchain is a requirement.
> 
> The objective of GitHub DID is to encourage contribution to the DID Spec and Linked Data Signatures, and allow rapid development of extensions to these without requiring the use of slow, or complicated more trustless infrastructure, such as blockchains or other distributed systems.

### [**`did:bid:`**](https://github.com/teleinfo-bif/bid/tree/master/doc/en)
###### For bif, by teleinfo caict

> BID provides distributed identifiers and blockchain-based digital identity services for people, enterprises, devices and digital objects. It aims to build a decentralized, data-secure, privacy-protected and flexible identifier system that addresses trusted connections among people, enterprises, devices and digital objects，enabling the vision of the Internet of Things and trust ingress with everything.
> 
> BID is built on decentralized identification protocols and equipped with characters like decentralization, self-management, privacy protection, security and ease of use. Each BID links to one BIF DID Description Object (DDO).

### [**`did:ptn:`**](https://github.com/palletone/palletone-DID/blob/master/docs/did-method/README.md)
###### For PalletOne, by PalletOne

> Description of each field in the Base DID Document example (★ required fields, others are optional fields):
> 
> * ★ `context` A single value or an array, specifying the syntax standard that the DID Document format complies with.
> * `controller` Single value or array, other owners of DID Document. You can specify other DIDs to manage the file, and the permissions of other DIDs will be set in the corresponding operations authentication, updation, deletion, and recovery later. The default is controlled by the DID in the DID Document corresponding to the Base DID Document.
> * ★ `publicKey` A single value or an array that controls the public key information corresponding to the private key of the DID Document.
>   * ★ `id` The ID of the public key, `#keys-<num>` expressed in a unified way, incremented `<num>` from the `1` beginning.
>   * ★ `type` The algorithm of public key generation is unified with the chain,
>   * `controller` The owner of the public key `controller` corresponds to the one in the previous level. The format is `<DID>#keys-<num>`. The default situation is controlled by the document DID. `<DID>` The value on the stage controller, a `#keys-<num>` is `<DID>` a corresponding public key `id`.
>   * `publicKeyHex` Hexadecimal information of the public key. When the above controller is the default, this field is **required**.
> * ★ `authentication` Specify `publicKey` which fields can be used for authentication.
> * `updation` Specify `publicKey` which fields can be used for DID Document **update** operations, such as updating information such as pubkey or service.
> * `deletion` Specify `publicKey` which fields can be used for DID Document **delete** operation.
> * `recovery` Specify `publicKey` which fields can be used for DID Document **recovery** operations.

### [**`did:echo:`**](https://github.com/echoprotocol/uni-resolver-driver-did-echo/blob/master/echo_did_specifications.md)
###### For Echo, by Echo Technological Solutions LLC

> We propose a new DID method that allows special objects in ECHO network to be treated as valid DIDs.

> Method Specific Identifier
> The method specific identifier is composed of network type and id of object at ECHO network.
> 
> Network type can be '0' for mainnet, '1' for testnet and '2' for devnet. Next goes triplet of numbers devided by points: id of object at ECHO network.
> 
> Note: if it's not one of this networks, value will be '255'.
> ```
> echo-did = "did:echo:" echo-specific-idstring
> echo-specific-idstring = [ echo-network  ":" ] echo-object-id
> echo-network  = "0" / "1" / "2" / "255"
> echo-object-id  = 1*DIGIT "." 1*DIGIT "." 1*DIGIT
> ```

### [**`did:trustbloc:`**](https://github.com/trustbloc/trustbloc-did-method/blob/master/docs/spec/trustbloc-did-method.md)
###### For Hyperledger Fabric, by SecureKey

> The did:trustbloc DID method allows groups of independent entities to share custody of a DID registry consisting of a Sidetree implementation over a permissioned ledger. For more information on Sidetree, please refer to the Sidetree protocol specification.
> 
> Independent stakeholders wishing to transact with one another using DIDs can come together to form a consortium to manage their shared custody of a ledger.
> 
> This spec defines a discovery service. The discovery service provided by the TrustBloc DID Method allows a client to verify that a consortium is endorsed by its constituent stakeholders, verify that the configuration files of each stakeholder (which includes a list of Sidetree endpoints) are signed by the respective stakeholders, and use the provided Sidetree endpoints to perform Sidetree DID operations.


### [**`did:san:`**](https://github.com/Baasze/DID-method-specification)
###### For SAN Cloudchain, by YLZ Inc.

> The system aims to provide secure authentication and various health services based on the SAN blockchain and DID & Verifiable Credential Specifications published by the W3C.

> The namestring that shall identify this DID method is: san
> ```
> did:san:<method-specific-id>
> 
> did:san:abcdefgh1234
> ```

### [**`did:gatc:`**](https://github.com/gatacaid/gataca-did-method)
###### For Ethereum, Hyperledger Fabric, Hyperledger Besu, Alastria, by https://gataca.io/

> Gataca’s platform is based on a mobile identity portfolio, a set of APIs, and controllers for multiple blockchain networks.
> 
> Gataca is agnostic to the blockchain network. We adapt our infrastructure to the third party’s preferred ledger. Gataca currently supports the public network Ethereum and private networks based on Hyperledger Fabric, Hyperledger Besu or Quorum. Other networks may be added as requested.
> 
> This document provides the DID method specs for how our DID schema is implemented on the Ethereum network.
> 
> The simple structure links an object to a DID with states and public keys. Users do not need privileges to read the information on the blockchain but do need them to write. Gataca is the unique user that can modify the smart contract.

### [**`did:factom:`**](https://github.com/factom-protocol/FIS/blob/master/FIS/DID.md)
###### For Factom, by Sphereon, Factomatic, Factom Inc

> This proposal contains the interoperability specifications for products creating, reading (resolving) updating and deactivating Decentralized Identifiers on top of the Factom Protocol. This specification is not about other products wanting to use DIDs for their specific purpose, like signing or voting. This document describes the low level data structures and rules for DIDs, DID documents, resolution and registration on Factom itself.
> 
> Decentralized Identifiers are a cross ledger solution to support self sovereign identities. The Factom Protocol is ideally suited to store DIDs. This specification is the first step in creating a single specification for maximum interoperability with regards to identities across products and solutions on top of the Factom Protocol.

### [**`did:signor:`**](https://github.com/cryptonicsconsulting/signor-did-contracts/blob/master/did-method-spec.md)
###### For Ethereum, Hedera Hashgraph, Quorum, Hyperledger Besu, by https://cryptonics.consulting/

> This method shall be identified with the name sginor. A Signor DID has the following format:

> ```
> did:signor:<network>:<20 byte hexadecimal string>
> ```

> ```
> did:signor:mainet:0x70997970C51812dc3A010C7d01b50e0d17dc79C8
> ```

> The <20 byte hexadecimal string> corresponds to an Ethereum address in the current implementation, but maybe abstracted to different identfiers when implemented on different networks.
> 
> The <network> string corresponds to human readable form of an distributed ledger capable of running Ethereum smart contracts, including the following:

**Ethereum mainet** • **ropsten** • **rinkeby** • **Kovan**

> DIDs are registered in the DID Registry on-chain, and have a controller and a subject, expressed in the form of Ethereum addresses. The DID controller may or may not be the subject itself. Multiple controllers can be implemented through proxy smart contracts.

### [**`did:hedera:`**](https://github.com/hashgraph/did-method/blob/master/did-method-specification.md)
###### For Hedera Hashgraph, by Hedera Hashgraph, Swisscom Blockchain AG

> This document defines a binding of the Decentralized Identifier architecture to Hedera Hashgraph - specifically how to use the Hedera File Service to record membership in 'business application networks' (appnets) and how to use the Hedera Consensus Service (HCS) for CRUD mechanisms on DID documents stored in such business application network. An business application network is a network of computers that store some set of business data (such as DID Documents) in a shared state, and rely on the Hedera mainnet for timestamping and ordering the transactions that cause that business application network state to change. An business application network could be exclusively dedicated to managing DID Documents and other identity artifacts in its state, or it could itself be multi-purpose. For instance, a Supply Chain could establish an business application network and, in addition to using HCS for tracking the location of shipments, use the DID method defined here to manage the identities of the associated companies, employees, and IoT devices. The HCS model is designed to off load from the Hedera mainnet node the burden of disk writes and long term storage and so allow those nodes to be optimized for high throughput ordering of transactions.

### [**`did:sirius:`**](https://gitlab.com/proximax-enterprise/siriusid/sirius-id-specs/-/blob/master/docs/did-method-spec.md)
###### For ProximaX Sirius Chain, by ProximaX Enterprise, Proximax Inc.

> ProximaX SiriusID is intended to implement `did:sirius` and its DID Document.

> A DID that uses this method MUST begin with the following prefix: did:sirius. Per the DID specification, this string MUST be in lowercase. The remainder of the DID, after the prefix, is specified below.

> The SiriusID DID schema is defined by the following:
> ```
> siriusid-did = "did:sirius:" idstring
> 
> idstring = base58(version,network-identifier,address)
> ```

### [**`did:dock:`**](https://github.com/docknetwork/dock-did-driver/blob/master/Dock%20DID%20method%20specification.md)
###### For Dock, by https://www.dock.io/

> Currently, three public key and signing algorithms are supported for authentication.

> - Schnorr signatures with Sr25519. The public key is 32 bytes and signature is 64 bytes in size. These are supported by Substrate and Polkadot.
> - EdDSA signatures with Ed25519 curve. The public key is 32 bytes and signature is 64 bytes in size.
> - ECDSA signatures with secp256k1 curve. Compressed public keys are used, hence the public key is 33 bytes in size. Signature is 65 bytes in size.

> Dock is currently running as a proof of authority network but will evolve into a proof of stake chain. DIDs can be created by anyone holding Dock tokens but the creator of the DID is not necessarily the owner of the DID and thus cannot manage (update, remove) them. DIDs are managed using their corresponding private keys and these keys are independent of keys controlling the Dock tokens spent while creating the DID.
> 
> The chain does not store the full DID document but only the DID, the corresponding keys and controllers and block number for the last update and this block number changes with each update to the DID. This is needed for replay protection. Dock's client SDK retrieves those details and constructs the full DID document.
> 
> Currently, Dock supports registering a new DID with only one public key on chain. The key can be rotated by providing a signed message from the current key. The DID can be removed by providing a signed message from the current key. In future, multiple keys for authentication and authorization and other relevant W3C compliant features will be supported.



### [**`did:twit:`**](https://did-twit.github.io/did-twit/)
###### For Twit, by https://github.com/did-twit/did-twit/blob/master/spec/index.md

> Twitter is a highly used and influential social media network that lacks decentralization and higher levels of trust (i.e. signed messages). The `did:twit` specification makes an attempt to increase trust in Twitter interactions.
> 
> The method is similar to [did:key](https://w3c-ccg.github.io/did-method-key) in the sense that it is uses a `did` to wrap a single public key.
> 
> The objective of Twitter DID, similar to that of the [GitHub DID Method](https://github.com/decentralized-identity/github-did),  is to encourage use of the [DID Spec](https://w3c-ccg.github.io/did-spec/), by lowering the barrier to entry for use of the technology, and promote higher trust interactions.

### [**`did:near:`**](https://github.com/ontology-tech/DID-spec-near/blob/master/NEAR/DID-Method-NEAR.md)
###### For NEAR, by Ontology Foundation

> NEAR uses readable account identifiers instead of a hash of a public key, and the accounts have some DID features, but not all. We have developed this specification to define a new DID method for hosting DIDs on the NEAR blockchain, also referred to as NEAR DID, and facilitate developers to work with related contracts.

> ```
> near-did   = "did:near:" near-specific-idstring
> near-specific-idstring = *( 1*idchar ".") 2*idchar
> idchar    = %x30-39 / %x61-7A / "-" / "_"
> ```

### [**`did:vaa:`**](https://github.com/caict-develop-zhangbo/vaa-method/blob/master/README.md)
###### For bif, by China Academy of Information and Communications Technology (CAICT)

> Blockchain Identifier Infrastructure (BIF) is a permissioned public blockchain aiming for creating a distributed trust management framework typical for internet ID service, and the BIF blockchain (http://bidspace.cn/) is governed by China Academy of Information and Communications Technology (CAICT). CAICT is also the official issuing agency with Issuing Agency Code (IAC)——"VAA", given by ISO/IEC 15459. The IAC indicates an authorized qualification of distributing identifiers with own allocation rules.
> 
> As the "VAA" means a self-defined rule for internet identifiers, these letters could be literal used as a DID method name conformant with W3C DID specification. The VAA method is created not only to define a random identifier generation rules, but ultimately to create smart contracts, which support different identifiers format.

### [**`did:bba:`**](https://github.com/blobaa/bba-did-method-specification/blob/master/docs/markdown/spec.md)
###### For Ardor, by Attila Aldemir

> The `bba` DID method aims to enable the Ardor blockchain to act as a DPKI within the SSI ecosystem. It runs on the independent IGNIS child chain and utilizes Ardors Account Properties feature to manage DIDs and corresponding DID controllers. The Account Properties feature provides the possibility to tag an account with a small amount of data (160 characters). A DID controller is always represented in form of an Ardor account and is by default separated from the public keys (if present) embedded in a DID document. Think of a master key controlling the DID operations create, update and deactivate. A DID controller always corresponds to exactly one Ardor account, whereas one Ardor account can control multiple DIDs.
> 
> DID and DID document handling is decoupled so that multiple DID document storages can be defined and integrated to store DID document templates (DID documents without a DID reference). In its current state, the `bba` DID method defines only one storage type (Ardor Cloud Storage).
> 
> In the following, `bba` DID method compliant account properties are called DID attestations. An account property is `bba` DID method compliant if it aligns to the data model described in the DID Attestation Data Fields section and is self-set. A self-set account property is a property in which sender and receiver accounts are identical.

### [**`did:morpheus:`**](https://developer.iop.global/w3c?id=personal-data)
###### For Hydra, by https://iop.global/

> Distributed ledger technologies (DLT, blockchain) are mostly used by cryptocurrencies, but their event ordering and decentralized consensus algorithms are useful for general purpose. Morpheus needs DLT for safe ordering DID updates and querying the historical state of a DID Document at any given point of time for signature validation. The main benefit of DLTs is that many parties with opposing interests run the infrastructure, therefore it is almost impossible to unilaterally control changes to the history and state of the ledger.
> 
> Morpheus currently uses the Hydra blockchain, a dPoS ledger built as an Ark bridgechain and customized with DID-related transactions. Morpheus has a ledger-agnostic design, thus could operate with other ledgers as well.

> ```
> morpheus-did = "did:morpheus:" morpheus-idstring
> morpheus-idstring = (multicipher-encoded asymmetric cryptographic keyId value)
> ``` 

### [**`did:etho:`**](https://github.com/ontology-tech/DID-method-specs/blob/master/did-etho/DID-Method-etho.md)
###### For Ethereum, by Ontology Foundation

> Decentralized identifiers (DIDs) are a new type of identifiers that enables verifiable, self-sovereign digital identity. This ETHO DID method specification describes a new DID method, that is, ETHO DID and defines how Ethereum blockchain stores ETHO DIDs and their corresponding DID documents, and how to do CRUD operations on ETHO DID documents.

> ```
> etho-did   = "did:etho:" etho-specific-idstring
> etho-specific-idstring = 40*40HEXDIG
> ```

### [**`did:bnb:`**](https://github.com/ontology-tech/DID-method-specs/blob/master/did-bnb/DID-Method-bnb.md)
###### For Binance Smart Chain, by Ontology Foundation

> Decentralized identifiers (DIDs) are a new type of identifiers that enables verifiable, self-sovereign digital identity. This Binance DID method specification describes a new DID method, that is, Binance DID and defines how Binance Smart Chain stores Binance DIDs and their corresponding DID documents, and how to do CRUD operations on Binance DID documents.

> ```
> bnb-did   = "did:bnb:" bnb-specific-idstring
> bnb-specific-idstring = 40*40HEXDIG
> ```

### [**`did:celo:`**](https://github.com/ontology-tech/DID-method-specs/blob/master/did-celo/DID-Method-celo.md)
###### For Celo, by Ontology Foundation

> Decentralized identifiers (DIDs) are a new type of identifiers that enables verifiable, self-sovereign digital identity. This Celo DID method specification describes a new DID method, that is, Celo DID and defines how Celo blockchain stores Celo DIDs and their corresponding DID documents, and how to do CRUD operations on Celo DID documents.

> ```
> celo-did   = "did:celo:" celo-specific-idstring
> celo-specific-idstring = 40*40HEXDIG
> ```

### [**`did:klay:`**](https://github.com/ontology-tech/DID-method-specs/blob/master/did-klay/DID-Method-klay.md)
###### For Klaytn, by Ontology Foundation

> Decentralized identifiers (DIDs) are a new type of identifiers that enables verifiable, self-sovereign digital identity. This Klaytn DID method specification describes a new DID method, that is, Klaytn DID and defines how Klaytn blockchain stores Klaytn DIDs and their corresponding DID documents, and how to do CRUD operations on Klaytn DID documents.

### [**`did:trx:`**](https://github.com/ontology-tech/DID-method-specs/blob/master/did-trx/DID-Method-trx.md)
###### For TRON, by Ontology Foundation

> Decentralized identifiers (DIDs) are a new type of identifiers that enables verifiable, self-sovereign digital identity. This TRON DID method specification describes a new DID method, that is, TRON DID and defines how TRON blockchain stores TRON DIDs and their corresponding DID documents, and how to do CRUD operations on TRON DID documents.

### [**`did:grg:`**](https://github.com/GrgChain/DID-method-specs/blob/master/README.md)
###### For GrgChain, by GRGBanking Blockchain Express Co. Ltd.

> ```
> 1. Did document
> {
> 	"@context": "https://w3id.org/did/v1",
> 	"id": "did:grg:0x584b244f03BCE0e1e9766a880d0713410B955Fb3",
> 	"version": 1,
> 	"created": "2020-08-25T15:05:02.364Z",
> 	"updated": "2020-08-25T15:05:02.364Z",
> 	"publicKey": [{
> 		"id": "did:grg:0x584b244f03BCE0e1e9766a880d0713410B955Fb3#keys-1",
> 		"type": "SM2",
> 		"publicKeyHex": "04712eb2f39204e9cf44728fe7e8191ad043091d0fc7d860be1339c565834b95862ed9956fe56caf9ddd46ae287d973f7d2ce974cdf474e56f1d204a65836f9882"
> 	}, {
> 		"id": "did:grg:0x584b244f03BCE0e1e9766a880d0713410B955Fb3#keys-2",
> 		"type": "SM2",
> 		"publicKeyHex": "048c89b67d48d9245ac20e600108b6dbb3a07f9275b0b0f0ad0b7457f8cb6aeb4c178c93f1d7fb7e0d7ee8b55261b28a4eba14158a6dd2d1b9a152fa9d2839c8bb"
> 	}],
> 	"authentication": ["did:grg:0x584b244f03BCE0e1e9766a880d0713410B955Fb3#keys-1"],
> 	"recovery": ["did:grg:0x584b244f03BCE0e1e9766a880d0713410B955Fb3#keys-2"],
> 	"service": [{
> 		"id": "",
> 		"type": "",
> 		"serviceEndpoint": ""
> 	}],
> 	"proof": {
> 		"type": "SM2",
> 		"creator": "did:grg:0x584b244f03BCE0e1e9766a880d0713410B955Fb3#keys-1",
> 		"signatureValue": "f12493e632f91e4f415732de62871fb3c3ffb943ce6e52682154837f0d8109bd65a183c8cf5b39d9c06e0a415ead1230b1d88db877fd6b0b2460acc503ead04b"
> 	}
> }
> 
> 2. Claim
> {
> 	"@context": "https://w3id.org/did/v1",
> 	"id": "XXX",
> 	"type": ["ProofClaim"],
> 	"issuer": "did:grg:0x802B718AF528214931E2642C2b113436C847a16b",
> 	"issuanceDate": "2020-02-27T15:55:42.956Z",
> 	"expirationDate": "2020-04-01T12:01:20Z",
> 	"credentialSubject": {
> 		"id": "did:ccp:ceNobbK6Me9F5zwyE3MKY88QZLw",
> 		"shortDescription": "实名认证声明",
> 		"longDescription": "该用户经过了我司的实名认证",
> 		"type": "RealNameAuthentication"
> 	},
> 	"revocation": {
> 		"id": "https://example.com/v1/claim/revocations",
> 		"type": "SimpleRevocationListV1"
> 	},
> 	"proof": {
> 		"creator": "did:grg:0x802B718AF528214931E2642C2b113436C847a16b",
> 		"type": "Secp256k1",
> 		"signatureValue": "0x49a714001405bc39c12764a44e678854e388dca1edcce1384054d1e62244751358996e7593a46ccb6b35a2bfa85cea1ae1f90e98e81e2943e9c655f14d9ebb7b1c"
> 	}
> }
> 
> 3. Did Info
>     {
>       did: "did:grg:0x584b244f03BCE0e1e9766a880d0713410B955Fb3",
>       mnemonic: "play smile scatter pigeon uncover among dismiss scatter fever rose wrestle rotate m/1 m/2",
>       mainPrivateKey: "82b28ff4626e3151f873c1af9b3a28a8723fd5a7a74092812c92435f88f6cf9c",
>       recoveryPrivateKey: "19863244cce676ccaf7507b49b2ae725d4603f8a7bbfe505978144129b56fa59"
>     },
> ```


### [**`did:schema:`**](https://github.com/51nodes/schema-registry-did-method/blob/master/README.md)
###### For Multiple storage networks, currently public IPFS and evan.network IPFS, by 51nodes GmbH

> The Schema Registry DID Method aims to provide unique and universal identification for schemas in multiple formats hosted on multiple storage mechanisms or networks.
> 
> This first version will focus on JSON Schema and XML Schema Definition/XSD schemas stored using the IPFS (InterPlanetary File System) protocol, but the DID method and concept is open for contributions and extensions regarding further schema formats and storage/network options.

### [**`did:key:`**](https://w3c-ccg.github.io/did-method-key/)
###### For Ledger independent DID method based on public/private key pairs, by Rick Astley (thank you for your inspiration), Manu Sporny, Dmitri Zagidulin, Dave Longley, Orie Steele

> While DLT-based DID Methods have great decentralization characteristics, and some of the more centralized DID Methods provide strong system control guarantees, the general approaches tend to be expensive to setup and operate. Some use cases requiring DIDs do not need the guarantees provided by these heavy-weight systems. For example, a DID that will only be used for a single, ephemeral interaction might not need to be registered, updated, or deactivated. It is for this class of use cases that the did:key method exists.

> The format for the did:key method conforms to the [DID-CORE] specification and is simple. It consists of the did:key prefix, followed by a Multibase [MULTIBASE] base58-btc encoded value that is a concatenation of the Multicodec [MULTICODEC] identifier for the public key type and the raw bytes associated with the public key format.

### [**`did:tyron:`**](https://www.tyronzil.com/)
###### For Zilliqa, by Julio Cabrapan Duarte

> Self-Sovereign Identity (SSI) allows people to manage their digital identities, proving who they are without a middleman, by anchoring DIDs on blockchain platforms as a shared root of trust. However, most blockchains still can't provide decentralized identity at scale. By implementing the Tyron SSI Protocol, tyronZIL aims to solve this issue and enable user-controlled digital identities.
> 
> The word Tyron derives from the Greek turannos that means sovereign, and Tyron's purpose is to give people sovereignty over their data.

### [**`did:corda:`**](https://htmlpreview.github.io/?https://github.com/persistentsystems/corda-did-method/blob/master/corda_did_method.html)
###### For Corda, by Nitesh Solanki,Moritz Platt,Pranav Kirtani

> To understand the environment in which the Corda DID method operates, the permissioned nature of a Corda network and the point-to-point approach to data replication must be taken into account. While parties in permissionless blockchains remain anonymous and can join and leave at will, any Corda network utilizes a standard PKIX infrastructure for linking public keys to identities [corda-whitepaper]. As such, individually deployed entities in the network – nodes – have a strong notion of identity. This concept is instrumental in network communication. Similarly, the data-replication model implemented in Corda is different to that of a conventional public blockchain, which makes all in-ledger data visible to all network participants. In Corda, data are distributed to a configurable subset of network members only.

> The Corda DID method operates in an environment where multiple nodes form a consortium in order to replicate decentralized identity data (cf. figure 1). These consortium nodes replicate decentralized identifier documents to form a network-wide and, ultimately, consistent view of the unity of decentralized identifiers, using the Corda DID method.

### [**`did:uns:`**](https://github.com/unik-name/did-method-spec/blob/main/did-uns/UNS-DID-Specification.md)
###### For https://docs.uns.network/, by https://www.spacelephant.org/

> The uns DID method provides support for DIDs on the uns.network blockchain. More specifically, it associates a DID to every address in the ledger. This method is very minimalistic in the sense that it produces DID Document (DDoc) with minimal information: a DID and its associated public key. Furthermore, once a uns-did is created, it cannot be updated.
> 
> The goal of this method is to work in tandem with other, more complex DID methods based on the same blockchain. Uns.network is dedicated to the management of Non Fungible Tokens (NFT). The first type of NFT that it supports is [@uniknames](https://docs.unikname.com/), human-readable identifiers. Just like any other tokens, @uniknames can be bought or exchanged, but they can also be linked to public properties the owner wishes to advertise, or used to connect to compliant websites in a private and secure fashion, among other things. The `unik` DID method associates a DID to these NFT tokens, using uns-did as controllers.
> 
> Identifiers are only the first use case for uns.network NFTs. Other use cases are likely to require their own DID method based on uns DIDs.

### [**`did:panacea:`**](https://github.com/medibloc/panacea-core/blob/master/docs/did.md)
###### For Panacea, by MediBloc

> Panacea is a public blockchain built by MediBloc to reinvent the healthcare experience. Panacea also supports DID operations. DIDs are created and stored in the Panacea, and they are used with verifiable credentials.

### [**`did:avvcyber:`**](https://github.com/Amrita-TIFAC-Cyber-Blockchain/DID-AVVCYBER/blob/main/did-avvcyber-v1.md)
###### For TIFAC-CORE in Cyber Security, Amrita Vishwa Vidyapeetham, by Ramaguru Radhakrishnan

> TIFAC-CORE in Cyber Security, Amrita School of Engineering, Amrita Vishwa Vidyapeetham Coimbatore is Center of Relevance and Excellence (CORE) in Cyber Security. The Center is working toward Cryptography, Visual Cryptography, Steganography, Cyber Forensics, Machine Learning and Blockchain Technology. There are multiple projects being worked across domains where we are using  DIDs. did:avvcyber: is a dedicated DID created for all our Blockchain Projects from 2022.
