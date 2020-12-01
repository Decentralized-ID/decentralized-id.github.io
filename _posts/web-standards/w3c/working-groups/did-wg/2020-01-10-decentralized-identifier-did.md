---
title: "(DID) the Decentralized Identifier"
description: Decentralized identifiers (DIDs) are a new type of identifier that enables verifiable, decentralized digital identity. 
excerpt: >
  Decentralized identifiers (DIDs) are a new type of identifier that enables verifiable, decentralized digital identity. A DID identifies any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) that the controller of the DID decides that it identifies. In contrast to typical, federated identifiers, DIDs have been designed so that they may be decoupled from centralized registries, identity providers, and certificate authorities. Specifically, while other parties might be used to help enable the discovery of information related to a DID, the design enables the controller of a DID to prove control over it without requiring permission from any other party. DIDs are URIs that associate a DID subject with a DID document allowing trustable interactions associated with that subject.
categories: ["Web Standards"]
tags: ["W3C","Credentials Community Group","DID","BTCR","Blockstack","ERC725","IPID","lifeID","Dominode","Ontology","Ockam","JLinc","ION","Jolocom","Veres One","XDI","uPort","Ethereum","Bitcoin","IBM", "Microsoft", "Digital Bazaar", "Consensys", "Evernym", "Hyland Credentials","BCGov","Ocean Protocol","Alastria","InfoWallet","ICON","Vivvo","Sovrin Foundation","Consent","Peer DID"]
permalink: web-standards/w3c/wg/did/decentralized-identifier/
canonical_url: https://decentralized-id.com/web-standards/w3c/wg/did/decentralized-identifier/
redirect_from: 
  - web-standards/w3c/did-wg/decentralized-identifier/
  - specs-standards/decentralized-identifier-did/
  - web-standards/decentralized-identifier-did/
  - adoption/
last_modified_at: 2020-11-23
---

<a href="https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf"><img src="https://i.imgur.com/7NRcJbq.png"/></a>

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

* [@ChristopherA on DID adoption](https://twitter.com/ChristopherA/status/989122017348784130)
   > "22/ Over a dozen companies and organizations, using multiple blockchains (Bitcoin, Ethereum, Hyperledger, etc.), have committed to deploying DIDs, including IBM, Microsoft, Digital Bazaar, Consensys, Evernym, Learning Machine, British Columbia, and more:" —[How blockchain could solve the internet privacy problem](https://www.computerworld.com/article/3267930/blockchain/how-blockchain-could-solve-the-internet-privacy-problem.html)

### [DID Method Registry](https://w3c-ccg.github.io/did-method-registry/#the-registry)
[Peer DID Method Spec](https://dhh1128.github.io/peer-did-method-spec/index.html)

* did:example:   - [DID Specification](https://w3c-ccg.github.io/did-spec/)
* did:btcr:      - [BTCR DID Method](https://w3c-ccg.github.io/didm-btcr/) 
  * The Bitcoin Reference DID method (did:btcr) supports DIDs on the public Bitcoin blockchain. The Bitcoin Reference method has minimal design goals: a DID trust anchor based on the Bitcoin blockchain, updates publicly visible and auditable via Bitcoin transactions, and optionally, additional DID Document information referenced in the transaction OP_RETURN data field. No other Personal Identifiable Information (PII) would be placed on the immutable blockchain.
  * [btcr tx conversion playground](https://weboftrustinfo.github.io/btcr-tx-playground.github.io/) 
* did:stack:     - [Blockstack DID Method](https://github.com/blockstack/blockstack-core/blob/master/docs/blockstack-did-spec.md) [[**ϟ**](https://forum.blockstack.org/t/did-method-at-identity-foundation/4287/9)] 
  - Blockstack is a network for decentralized applications where users own their identities and data. Blockstack utilizes a public blockchain to implement a decentralized naming layer, which binds a user's human-readable username to their current public key and a pointer to their data storage buckets.
* did:cnsnt:   - Consent 	
* did:erc725:  - [erc725 DID Method](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/topics-and-advance-readings/DID-Method-erc725.md)
* did:ipid:    - [IPID DID method](https://did-ipid.github.io/ipid-did-method/)
  - Implementation of the DID spec over IPFS (Interplanetary File System) 
* did:life:    - [lifeID DID Method](https://lifeid.github.io/did-method-spec/)
* did:sov: 	   - [Sovrin DID Method](https://sovrin-foundation.github.io/sovrin/spec/did-method-spec-template.html)
* did:uport: 	- uPort 	
* did:v1: 	   - [Veres One DID Method](https://w3c-ccg.github.io/did-method-v1/)
  * [**veres.one**](https://veres.one) — a permissionless public ledger designed specifically for the creation and management of decentralized identifiers (DIDs)
* did:dom:     - Dominode 	
* did:ont: 	   - [Ontology DID Method](https://github.com/ontio/ontology-DID/blob/master/docs/en/DID-ONT-method.md)
* did:vvo: 	   - [Vivvo DID Method](https://vivvo.github.io/vivvo-did-scheme/spec/did-method-spec-template.html)
* did:icon:    - [ICON DID Method](https://github.com/icon-project/icon-DID/blob/master/docs/ICON-DID-method.md)
* did:iwt: 	   - [InfoWallet DID Method](https://github.com/infowallet/did_method/blob/master/did_method.md)
* did:ockam:   - [Ockam DID Method](https://github.com/ockam-network/did-method-spec/blob/master/README.md)
  * [did:ockam:](https://medium.com/ockam/an-introduction-to-did-ockam-8626d5aecc53) [[**ϟ**](https://twitter.com/Ockam_io/status/1064589363269365763)]
* did:ala: 	   - [Alastria DID Method](https://github.com/alastria/alastria-identity/wiki/Alastria-DID-Method-Specification-(Quorum-version))
* did:op:      - [Ocean Protocol DID Method](https://github.com/oceanprotocol/OEPs/tree/master/7/v0.2)
* did:jlinc:   - [JLINC Protocol DID Method](https://did-spec.jlinc.org/)
* did:ion:     - [ION DID Method](https://github.com/decentralized-identity/ion-did-method)
* did:jolo:    - Jolocom 	
* did:ethr:    - [ETHR DID Method](https://github.com/uport-project/ethr-did-resolver/blob/develop/doc/did-method-spec.md)

