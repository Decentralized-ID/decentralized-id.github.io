---
title       : "Ethereum Identity Specs and Apps"
description : "A Collection of Ethereum-based Decentralized Identity Specs, Literature, (d)Apps, and GitHub Repositories."
image       : "https://infominer.id/DIDecentralized/images/ethereum.png"
layout: single
---

# Ethereum Identity 
**Specifications, Literature, (d)Apps, and GitHub Repositories**

  ![](https://i.imgur.com/XWeGM72.png)
* [Decentralized Digital Identity on Ethereum](https://www.slideshare.net/FabriceCroiseaux/ethcc-2018-decentralized-digital-identity-on-ethereum) -SlideShare
* [DEVCON1: Digital Identity](https://www.youtube.com/watch?v=QpaTOvAhLR4) — video from DEVCON1
* [Proof-of-Individuality](http://proofofindividuality.online/) — how to prove a person only has one account
   * [Anti-Sybil Protocol using virtual pseudonym parties](https://medium.com/@unlisted/anti-sybil-protocol-using-virtual-pseudonym-parties-10276fcf3b20)

## Contents
* [ERC-EIP](#erc-eip-)
* [ERC725-735](#erc725-735-)
* [uPort](#uport-)
* [Jolocom](#jolocom-)
* [Spidchain](#spidchain-)
* [Cryptonomica](#cryptonomica-)
* [Assorted Ethereum Apps](#assorted-ethereum-apps-)

### Directory
* [Eth Github Repositories](eth-id-github.md) **>>**
  * [EIP - ERC](eth-id-github.md#eip---erc-) **>>**
  * [Jolocom](eth-id-github.md#jolocom-) **>>**
  * [uPort](eth-id-github.md#uport-) **>>**
    * [uPort DID](eth-id-github.md#uport-did-) **>>**
    * [uPort Identification](eth-id-github.md#uport-identification-) **>>**
    * [uPort Mobile](eth-id-github.md#uport-mobile-) **>>**
    * [uPort Lambda](eth-id-github.md#uport-lambda-) **>>**
    * [uPort React](eth-id-github.md#uport-react-) **>>**
    * [uPort Assorted](eth-id-github.md#uport-assorted-) **>>**
  * [Spid-Eth](eth-id-github.md#spidchain-) **>>**
  * [Cryptonomica](eth-id-github.md#cryptonomica-) **>>**

## ERC-EIP

* [ERC: Lightweight Identity #1056](https://github.com/ethereum/EIPs/issues/1056) —This ERC describes a standard for creating and updating identities with a limited use of blockchain resources. An identity can have an unlimited number of delegates and attributes associated with it. Identity creation is as simple as creating a regular key pair ethereum account, which means that it's fee (no gas costs) and all ethereum accounts are valid identities. Furthermore this ERC is fully DID compliant.
* [ERC1056 ❤ ERC780 — an open identity and claims protocol for Ethereum](https://medium.com/uport/erc1056-erc780-an-open-identity-and-claims-protocol-for-ethereum-aef7207bc744)
* [EIP-780 Ethereum Claims Registry](https://github.com/ethereum/EIPs/issues/780)
* [EIP712](https://github.com/ethereum/EIPs/blob/f29527ab39357548b06b29e937a48f06ae099de7/EIPS/eip-712.md) - This is a standard for hashing and signing of typed structured data
* [ERC-1484 Digital Identity Aggregator](https://github.com/ethereum/EIPs/issues/1495) —A protocol for aggregating digital identity information that's broadly interoperable with existing, proposed, and hypothetical future digital identity standards.
* [EIP-1078](https://github.com/ethereum/EIPs/blob/ed621645c8f3bc5756492f327cda015f35d9f8da/EIPS/eip-1078.md) - 
This presents a method to replace the usual signup/login design pattern with a minimal ethereum native scheme, that doesn’t require passwords, backing up private keys nor typing seed phrases. 
* [ERC-1077 and ERC-1078: The magic of executable signed messages](https://ethereum-magicians.org/t/erc-1077-and-erc-1078-the-magic-of-executable-signed-messages-to-login-and-do-actions/351)
* [ERC-EIP on GitHub](eth-id-github.html#eip---erc-) **>>**

### ERC725-735 [**^**](#contents-)

* [ERC725](https://github.com/ethereum/EIPs/issues/725) 
  * The following describes standard functions for a unique identifiable proxy account to be used by humans, groups, organisations, objects and machines
* [ERC735](https://github.com/ethereum/EIPs/issues/735) -  The following describes standard functions for adding, removing and holding of claims.
  - These claims can attested from third parties (issuers) or self attested.
* [Origin partners on ERC725](https://coinjournal.net/origin-protocol-partners-on-new-erc-725-alliance-to-promote-the-adoption-of-blockchain-based-identity-standard)
* [Managing Identity with a UI—ERC-725](https://medium.com/originprotocol/managing-identity-with-a-ui-for-erc-725-5c7422b38c09)
* [Ethereum ERC725 Blockchain Based, Self-Sovereign Identity Management](https://bitcoinexchangeguide.com/ethereum-erc725-blockchain-based-self-sovereign-identity-management/)
* [erc725alliance.org](https://erc725alliance.org)
* [ERC: Lightweight Identity #1056](https://github.com/ethereum/EIPs/issues/1056) —This ERC describes a standard for creating and updating identities with a limited use of blockchain resources. An identity can have an unlimited number of delegates and attributes associated with it. Identity creation is as simple as creating a regular key pair ethereum account, which means that it's fee (no gas costs) and all ethereum accounts are valid identities. Furthermore this ERC is fully DID compliant.



## uPort

![](https://i.imgur.com/sPAP2g3.png)

* [uPort](https://www.uport.me/) [[**G**](https://github.com/uport-project/)] [[**T**](https://twitter.com/uport_me)]
   * [Ethereum studio ConsenSys launches digital IDs and assets secured on Ubuntu phones](http://www.ibtimes.co.uk/ethereum-studio-consensys-launches-internet-people-digital-ids-assets-secured-unbuntu-phones-1542620)
   * [Year in Review. What's to come in 2018](https://medium.com/uport/uport-year-in-review-whats-to-come-in-2018-15ccb9214439)
* [Different Approaches to Ethereum Identity Standards](https://medium.com/uport/different-approaches-to-ethereum-identity-standards-a09488347c87)
  ![](https://i.imgur.com/ASI0PaB.png)

* [uPort GitHub Repos](eth-id-github.html#uport-)
  * [uPort DID](eth-id-github.html#uport-did-)
  * [uPort Identification](eth-id-github.html#uport-identification-)
  * [uPort Mobile](eth-id-github.html#uport-mobile-)
  * [uPort Lambda](eth-id-github.html#uport-lambda-)
  * [uPort React](eth-id-github.html#uport-react-)
  * [uPort Assorted](eth-id-github.html#uport-assorted-)



## Jolocom

![](https://i.imgur.com/BNmq1U9.png)

* [Jolocom](http://jolocom.com/) 
   * a "SmartWallet" for everyone to own their personal digital identity, using [Social Linked Data](https://github.com/solid/solid-spec), WebID, and verifiable claims standards via Ethereum smart contracts. 
   * [A universal identity layer we can only build together](https://stories.jolocom.com/a-universal-identity-layer-we-can-only-build-together-e297ed5ae4ed)
* [Jolocom Github Repos](eth-id-github.html#jolocom-)

## Spidchain

![](https://i.imgur.com/azuC8lh.png)

* [Spidchain](http://www.spidchain.com/) [[**wp**](https://drive.google.com/file/d/0B89WE3IIHmy1Z0ZSSWVmVEtaaG8/view)]
   * "offers a platform for self-sovereign identity, including desktop and mobile apps for end-users. It uses Decentralized Identifiers (DIDs) - backed by optionally Bitcoin or Ethereum - to implement a marketplace for verifiable claims. The Spidchain applications allow individuals to create, recover, and revoke DIDs, to authenticate, to sign and verify files and claims, and more."
* [Spid-Eth GitHub Repos](eth-id-github.html#spid-eth-repos-)

## Cryptonomica

[![](https://i.imgur.com/moVyrrt.png)](https://cryptonomica.github.io)

 * [Cryptonomica.net](https://cryptonomica.net) is an identity verification service based on [OpenPGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) and [Ethereum](https://www.ethereum.org) with legal framework and online dispute resolution for electronic contracts from London-based [court of arbitration](https://cryptonomica.net/#!/arbitration) 
  * [Cryptonomica Github Repos](eth-id-github.html#cryptonomica-)
  

### Assorted Ethereum Apps

* [Deloitte SmartID](http://www.deloitte.co.uk/smartid/) [[**G**](https://github.com/SmartIdentity/smartId-contracts)]
   * "Smart Identity uses the Ethereum blockchain to represent an identity using a smart contract, attributes can be added by the identity owner and are stored in hash form"
* [Nuggets](http://www.nuggets.life/) [[**wp**](https://nuggets.life/images/Nuggets-White-Paper.pdf)]
   * "is a blockchain platform giving users a single biometric tool for login, payment and identity verification. It stores an individual's information in a "personal cloud" in "zero-knowledge blockchain storage".
* [poa.network](https://poa.network/)[**[D](https://medium.com/poa-network/poa-network-how-honey-badger-bft-consensus-works-4b16c0f1ff94)**]
 POA Network is an Ethereum-based platform that offers an open-source framework for smart contracts. POA Network is a sidechain to Ethereum utilizing [Proof of Authority](https://blockonomi.com/proof-of-authority/)
 as its consensus mechanism. 
