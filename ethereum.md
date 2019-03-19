---
title       : "Ethereum Identity Specs and Apps"
description : "A Collection of Ethereum-based Decentralized Identity Specs, Literature, (d)Apps, and GitHub Repositories."
image       : "https://infominer.id/DIDecentralized/images/ethereum.png"
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
* [uPort GitHub Repos](#uport-github-repos-)
  * [uPort DID](#uport-did-)
  * [uPort Identification](#uport-identification-)
  * [uPort Mobile](#uport-mobile-)
  * [uPort Lambda](#uport-lambda-)
  * [uPort React](#uport-react-)
  * [uPort Assorted](#uport-assorted-)
* [Jolocom](#jolocom-)
  * [Jolocom Github Repos](#jolocom-github-repos-)
* [Spidchain](#spidchain-)
  * [Spid-Eth Repos](#spid-eth-repos-)
* [Cryptonomica](#cryptonomica-)
  * [Cryptonomica Github Repos](#cryptonomica-github-repos-)
* [Assorted Ethereum Apps](#assorted-ethereum-apps-)


## ERC-EIP [**^**](#contents)

* [ERC: Lightweight Identity #1056](https://github.com/ethereum/EIPs/issues/1056) —This ERC describes a standard for creating and updating identities with a limited use of blockchain resources. An identity can have an unlimited number of delegates and attributes associated with it. Identity creation is as simple as creating a regular key pair ethereum account, which means that it's fee (no gas costs) and all ethereum accounts are valid identities. Furthermore this ERC is fully DID compliant.
* [ERC1056 ❤ ERC780 — an open identity and claims protocol for Ethereum](https://medium.com/uport/erc1056-erc780-an-open-identity-and-claims-protocol-for-ethereum-aef7207bc744)
* [EIP-780 Ethereum Claims Registry](https://github.com/ethereum/EIPs/issues/780)
* [EIP712](https://github.com/ethereum/EIPs/blob/f29527ab39357548b06b29e937a48f06ae099de7/EIPS/eip-712.md) - This is a standard for hashing and signing of typed structured data
* [ERC-1484 Digital Identity Aggregator](https://github.com/ethereum/EIPs/issues/1495) —A protocol for aggregating digital identity information that's broadly interoperable with existing, proposed, and hypothetical future digital identity standards.
* [EIP-1078](https://github.com/ethereum/EIPs/blob/ed621645c8f3bc5756492f327cda015f35d9f8da/EIPS/eip-1078.md) - 
This presents a method to replace the usual signup/login design pattern with a minimal ethereum native scheme, that doesn’t require passwords, backing up private keys nor typing seed phrases. 
* [ERC-1077 and ERC-1078: The magic of executable signed messages](https://ethereum-magicians.org/t/erc-1077-and-erc-1078-the-magic-of-executable-signed-messages-to-login-and-do-actions/351)

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



## uPort [**^**](#contents)

![](https://i.imgur.com/sPAP2g3.png)

* [uPort](https://www.uport.me/) [[**G**](https://github.com/uport-project/)] [[**T**](https://twitter.com/uport_me)]
   * [Ethereum studio ConsenSys launches digital IDs and assets secured on Ubuntu phones](http://www.ibtimes.co.uk/ethereum-studio-consensys-launches-internet-people-digital-ids-assets-secured-unbuntu-phones-1542620)
   * [Year in Review. What's to come in 2018](https://medium.com/uport/uport-year-in-review-whats-to-come-in-2018-15ccb9214439)
* [Different Approaches to Ethereum Identity Standards](https://medium.com/uport/different-approaches-to-ethereum-identity-standards-a09488347c87)
  ![](https://i.imgur.com/ASI0PaB.png)

## uPort Github Repos [**^**](#contents)

* <a href="https://github.com/uport-project/developers" target="_blank">/uport-project/developers</a> - Developer portal for documentation and application management
* <a href="https://github.com/uport-project/specs" target="_blank">/uport-project/specs</a> - uPort Protocol Specs
* <a href="https://github.com/uport-project/uport-connect" target="_blank">/uport-project/uport-connect</a> - Main uPort library for front end developers
* <a href="https://github.com/uport-project/eth-typed-data" target="_blank">/uport-project/eth-typed-data</a> - A javascript library for working with typed structured data as defined by EIP712
* <a href="https://github.com/uport-project/uport-transports" target="_blank">/uport-project/uport-transports</a> - Set up communication channels between your app and a uPort client to handle requests and responses.
* <a href="https://github.com/uport-project/webcard" target="_blank">/uport-project/webcard</a> - Transaction Sharing
* <a href="https://github.com/uport-project/demo" target="_blank">/uport-project/demo</a> - uPort Demo dApp
* <a href="https://github.com/uport-project/uport-lite" target="_blank">/uport-project/uport-lite</a> - Lightweight uport registry lookup
* <a href="https://github.com/uport-project/eslint-config-uport" target="_blank">/uport-project/eslint-config-uport</a> - Shareable eslint config for uport libraries
* <a href="https://github.com/uport-project/uPort-live" target="_blank">/uport-project/uPort-live</a> - Forked from Siunami/uPort-live
* <a href="https://github.com/uport-project/uport-wordpress-plugin" target="_blank">/uport-project/uport-wordpress-plugin</a> - A Passwordless Login for uPort and Wordpress
* <a href="https://github.com/uport-project/community-projects" target="_blank">/uport-project/community-projects</a> - A list of community hackathon projects and other experiments.
* <a href="https://github.com/uport-project/udoor" target="_blank">/uport-project/udoor</a> - uPort Door Management
* <a href="https://github.com/uport-project/uport-bounties" target="_blank">/uport-project/uport-bounties</a>- A Library of uPort Bounties
* <a href="https://github.com/dconroy/CityKey" target="_blank">/dconroy/CityKey</a> - Adding uPort support to Chicago CityKey, adding all the benefits of Self Sovereign Identity to municipal services. http://citykeychained.com

### uPort DID [**^**](#contents)

* <a href="https://github.com/uport-project/ethr-did-resolver" target="_blank">/uport-project/ethr-did-resolver</a> - DID resolver for Ethereum Addresses with support for key management
* <a href="https://github.com/uport-project/secp256k1-did-resolver" target="_blank">/uport-project/secp256k1-did-resolver</a> - Resolve DID documents for secp256k1 public keys
* <a href="https://github.com/uport-project/uport-did-driver" target="_blank">/uport-project/uport-did-driver</a> - Driver for the uPort DID method
* <a href="https://github.com/uport-project/eth-did-resolver" target="_blank">/uport-project/eth-did-resolver</a> - DID resolver for Ethereum Addresses
* <a href="https://github.com/uport-project/ethr-did" target="_blank">/uport-project/ethr-did</a> - Create ethr DIDs
* <a href="https://github.com/uport-project/ethr-did-registry" target="_blank">/uport-project/ethr-did-registry</a> - Backing for an experimental DID method
* <a href="https://github.com/uport-project/did-resolver" target="_blank">/uport-project/did-resolver</a> - Generic did-resolver
* <a href="https://github.com/uport-project/https-did-resolver" target="_blank">/uport-project/https-did-resolver</a> - DID resolver for HTTPS domains
* <a href="https://github.com/uport-project/nacl-did" target="_blank">/uport-project/nacl-did</a> - Light weight DID method, complete with Identity Creation tools, encryption and JWT signing
* <a href="https://github.com/uport-project/did-jwt" target="_blank">/uport-project/did-jwt</a> - Create and verify uPort and DID compliant JWT's in Javascript
* <a href="https://github.com/uport-project/uport-did-resolver" target="_blank">/uport-project/uport-did-resolver</a> - DID resolver for uPort identities


### uPort Identification [**^**](#contents)
* <a href="https://github.com/uport-project/openid" target="_blank">/uport-project/openid</a> - uPort openid
* <a href="https://github.com/uport-project/kmnid" target="_blank">/uport-project/kmnid</a> - A kotlin implementation of MNID
* <a href="https://github.com/uport-project/uport-registry" target="_blank">/uport-project/uport-registry</a> - Core uPort registry contract for linking attributes to uPort identities.
* <a href="https://github.com/uport-project/uport-chrome-extension" target="_blank">/uport-project/uport-chrome-extension</a> - An experiment to test decentralized identity in a Browser Extension environment.
* <a href="https://github.com/uport-project/infrastructure" target="_blank">/uport-project/infrastructure</a> - Support services for Self-Sovereign Identity
* <a href="https://github.com/uport-project/mnid" target="_blank">/uport-project/mnid</a> - Multi Network Identifier - spec and reference implementation



### uPort Mobile [**^**](#contents)

* <a href="https://github.com/uport-project/uport-android-sdk" target="_blank">/uport-project/uport-android-sdk</a> - Collections of tools and helper libraries for android to issue and use identities on the uPort platform
* <a href="https://github.com/uport-project/uport-android-signer" target="_blank">/uport-project/uport-android-signer</a> - android ETH signer library to be used by uport app and sdk
* <a href="https://github.com/uport-project/uport-android" target="_blank">/uport-project/uport-android</a> - uPort app for android - under construction
* <a href="https://github.com/uport-project/uport-ios-demo" target="_blank">/uport-project/uport-ios-demo</a> - Demo iPhone app using uPort SDK
* <a href="https://github.com/uport-project/uport-mobile-issues" target="_blank">/uport-project/uport-mobile-issues</a> - This repository is a place for developers to report and track status of issues reported while using the uPort mobile app
* <a href="https://github.com/uport-project/uport-mobile" target="_blank">/uport-project/uport-mobile</a> - uPort mobile app
* <a href="https://github.com/uport-project/uport-ios-sdk" target="_blank">/uport-project/uport-ios-sdk</a> - uPort iOS SDK in Swift
* <a href="https://github.com/uport-project/uport-ios-core-eth" target="_blank">/uport-project/uport-ios-core-eth</a> - iOS Ethereum Toolkit for uPort SDK
* <a href="https://github.com/uport-project/uport-ios-openssl" target="_blank">/uport-project/uport-ios-openssl</a> - iOS OpenSSL Framework for uPort SDK
* <a href="https://github.com/uport-project/UPTEthereumSigner" target="_blank">/uport-project/UPTEthereumSigner</a> - Ethereum signer library for iOS



### uPort Lambda [**^**](#contents)

* <a href="https://github.com/uport-project/lambda-chasqui" target="_blank">/uport-project/lambda-chasqui</a> - running_man Messenger service running_man
* <a href="https://github.com/uport-project/lambda-agora" target="_blank">/uport-project/lambda-agora</a> - An open public space where an assembly of applications can share details and be discovered (pre-alpha)
* <a href="https://github.com/uport-project/lambda-champagne" target="_blank">/uport-project/lambda-champagne</a>
* <a href="https://github.com/uport-project/lambda-niscani" target="_blank">/uport-project/lambda-niscani</a>
* <a href="https://github.com/uport-project/lambda-sensui" target="_blank">/uport-project/lambda-sensui</a> - uPort tx funding service
* <a href="https://github.com/uport-project/" target="_blank">/uport-project/lambda-caleuche</a> - Caleuche. Event Hub Service
* <a href="https://github.com/uport-project/lambda-idgraph" target="_blank">/uport-project/lambda-idgraph</a>
* <a href="https://github.com/uport-project/lambda-olorun" target="_blank">/uport-project/lambda-olorun</a> - uPort private network support
* <a href="https://github.com/uport-project/lambda-fatima" target="_blank">/uport-project/lambda-fatima</a> - uPort badge event attestor
* <a href="https://github.com/uport-project/lambda-pututu" target="_blank">/uport-project/lambda-pututu</a> - Push notification service
* <a href="https://github.com/uport-project/lambda-nisaba" target="_blank">/uport-project/lambda-nisaba</a> - Lambda functions for anti-sybill
* <a href="https://github.com/uport-project/lambda-unnu" target="_blank">/uport-project/lambda-unnu</a> - Creator of Identities

### uPort React [**^**](#contents)

* <a href="https://github.com/uport-project/react-native-uport-signer" target="_blank">/uport-project/react-native-uport-signer</a> 
* <a href="https://github.com/uport-project/react-native-signer-demo" target="_blank">/uport-project/react-native-signer-demo</a> 
* <a href="https://github.com/uport-project/uport-react-native-demo" target="_blank">/uport-project/uport-react-native-demo</a>
* <a href="https://github.com/uport-project/react-native-uport-connect" target="_blank">/uport-project/react-native-uport-connect</a> - Library for integrating uPort into your React Native app
* <a href="https://github.com/uport-project/react-uport-box" target="_blank">/uport-project/react-uport-box</a> - Truffle and React/Redux boilerplate with uPort Connect
* <a href="https://github.com/uport-project/react-native-passcode-android" target="_blank">/uport-project/react-native-passcode-android</a> - Forked from aldigjo/react-native-passcode-android

### uPort Assorted [**^**](#contents)
* <a href="https://github.com/uport-project/champagne-dapp" target="_blank">/uport-project/champagne-dapp</a> - Champagne Project dApp
* <a href="https://github.com/uport-project/tweetnacl-k" target="_blank">/uport-project/tweetnacl-k</a> - kotlin implementation of tweetnacl
* <a href="https://github.com/uport-project/sample-data-generator" target="_blank">/uport-project/sample-data-generator</a>
* <a href="https://github.com/uport-project/bck-wallet" target="_blank">/uport-project/bck-wallet</a>
* <a href="https://github.com/uport-project/UPTEthereumSigner-Example" target="_blank">/uport-project/UPTEthereumSigner-Example</a> - Example app and unit tests for the UPTEthereumSigner repo
* <a href="https://github.com/uport-project/lastblock" target="_blank">/uport-project/lastblock</a> - Daemon that alerts when a new block is mined
* <a href="https://github.com/uport-project/service-tests" target="_blank">/uport-project/service-tests</a> - Test servers from the outside
* <a href="https://github.com/uport-project/paper" target="_blank">/uport-project/paper</a>
* <a href="https://github.com/uport-project/swift-rlp" target="_blank">/uport-project/swift-rlp</a> - Recursive Length Prefix in Swift - CocoaPod
* <a href="https://github.com/uport-project/SwiftKeccak" target="_blank">/uport-project/SwiftKeccak</a> - Ethereum compatible Keccak hash for Swift
* <a href="https://github.com/uport-project/ed2curve-js" target="_blank">/uport-project/ed2curve-js</a> - Convert Ed25519 signing keys into Curve25519 Diffie-Hellman keys



## Jolocom [**^**](#contents)

![](https://i.imgur.com/BNmq1U9.png)

* [Jolocom](http://jolocom.com/) 
   * a "SmartWallet" for everyone to own their personal digital identity, using [Social Linked Data](https://github.com/solid/solid-spec), WebID, and verifiable claims standards via Ethereum smart contracts. 
   * [A universal identity layer we can only build together](https://stories.jolocom.com/a-universal-identity-layer-we-can-only-build-together-e297ed5ae4ed)

## Jolocom Github Repos [**^**](#contents)

* <a href="https://github.com/jolocom/docs" target="_blank">/jolocom/docs</a> - Documentation
* <a href="https://github.com/jolocom/smartwallet-app" target="_blank">/jolocom/smartwallet-app</a> - A decentralized self sovereign identity solution developed by Jolocom.
* <a href="https://github.com/jolocom/jolocom-lib" target="_blank">/jolocom/jolocom-lib</a> - Library for interacting with the identity solution provided by Jolocom.
* <a href="https://github.com/jolocom/jolocom-did-driver" target="_blank">/jolocom/jolocom-did-driver</a> - Universal Resolver DID Driver for the did:jolo identity space
* <a href="https://github.com/jolocom/generic-backend" target="_blank">/jolocom/generic-backend</a> - A generic backend implementation that makes use of the Jolocom Library for authentication, and for issuing credentials.
* <a href="https://github.com/jolocom/demo-sso" target="_blank">/jolocom/demo-sso</a> - A simple example web application integrating the Jolocom library for authentication.
* <a href="https://github.com/jolocom/demo-sso-mobile" target="_blank">/jolocom/demo-sso-mobile</a> - An example mobile application in React Native that showcases the interaction flows between the Smartwallet and another mobile app.
* <a href="https://github.com/jolocom/cred-types-jolocom-demo" target="_blank">/jolocom/cred-types-jolocom-demo</a> - Collection of metadata definitions for the demo Jolocom credential types.
* <a href="https://github.com/jolocom/react-native-build-config" target="_blank">/jolocom/react-native-build-config</a> - Expose native build config to JS (android only for now)
* <a href="https://github.com/jolocom/credTypes-jolocom-core" target="_blank">/jolocom/credTypes-jolocom-core</a> - Collection of metadata definitions for the core Jolocom credential types.
* <a href="https://github.com/jolocom/fueling-service" target="_blank">/jolocom/fueling-service</a> - Simple express service that can wire ether to requester.
* <a href="https://github.com/jolocom/registry-contract" target="_blank">/jolocom/registry-contract</a> - A basic smart contract on top of the Ethereum network that registers mappings between DID and IPFS DDO hashes.
* <a href="https://github.com/jolocom/smartwallet-webid-proxy" target="_blank">/jolocom/smartwallet-webid-proxy</a> - WebID proxy service

## Spidchain [**^**](#contents)

![](https://i.imgur.com/azuC8lh.png)

* [Spidchain](http://www.spidchain.com/) [[**wp**](https://drive.google.com/file/d/0B89WE3IIHmy1Z0ZSSWVmVEtaaG8/view)]
   * "offers a platform for self-sovereign identity, including desktop and mobile apps for end-users. It uses Decentralized Identifiers (DIDs) - backed by optionally Bitcoin or Ethereum - to implement a marketplace for verifiable claims. The Spidchain applications allow individuals to create, recover, and revoke DIDs, to authenticate, to sign and verify files and claims, and more."

### Spid-Eth Repos [**^**](#contents)
* <a href="https://github.com/SpidChain/eth-lightwallet" target="_blank">/SpidChain/eth-lightwallet</a> - Forked from ConsenSys/eth-lightwallet
  - Lightweight JS Wallet for Node and the browser
* <a href="https://github.com/SpidChain/truffle" target="_blank">/SpidChain/truffle</a> - Forked from trufflesuite/truffle
  - A development framework for Ethereum
* <a href="https://github.com/SpidChain/VotingSystem" target="_blank">/SpidChain/VotingSystem</a> - A dapp, library and smart contract to notarize votes on the ethereum blockchain
* <a href="https://github.com/SpidChain/ethers-wallet" target="_blank">/SpidChain/ethers-wallet</a> - Forked from ethers-io/ethers.js
  - Complete Ethereum wallet implementation and library in JavaScript.
* <a href="https://github.com/SpidChain/nodejs-ethereum" target="_blank">/SpidChain/nodejs-ethereum</a> - Forked from b9lab/nodejs-ethereum
Example of using NodeJs with Ethereum

## Cryptonomica [**^**](#contents)

[![](https://i.imgur.com/moVyrrt.png)](https://cryptonomica.github.io)

 * [Cryptonomica.net](https://cryptonomica.net) is an identity verification service based on [OpenPGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) and [Ethereum](https://www.ethereum.org) with legal framework and online dispute resolution for electronic contracts from London-based [court of arbitration](https://cryptonomica.net/#!/arbitration) 

### Cryptonomica Github Repos [**^**](#contents)
* <a href="https://github.com/Cryptonomica/cryptonomica" target="_blank">/Cryptonomica/cryptonomica</a> - Cryptonomica keys server
* <a href="https://github.com/Cryptonomica/cryptonomica.github.io" target="_blank">/Cryptonomica/cryptonomica.github.io</a> - Cryptonomica frontend
* <a href="https://github.com/Cryptonomica/arbitration-rules" target="_blank">/Cryptonomica/arbitration-rules</a> - Cryptonomica Arbitration Rules
* <a href="https://github.com/Cryptonomica/dappathon-tlv" target="_blank">/Cryptonomica/dappathon-tlv</a>
* <a href="https://github.com/Cryptonomica/Ethereum-IdentityVerification" target="_blank">/Cryptonomica/Ethereum-IdentityVerification</a> - Indentity verification and KYC for Ethereum blockchain
* <a href="https://github.com/Cryptonomica/ethnode.cryptonomica.net" target="_blank">/Cryptonomica/ethnode.cryptonomica.net</a> - Ethereum node with API on nodejs and web3.js
* <a href="https://github.com/Cryptonomica/Ethereum-IdentityProof" target="_blank">/Cryptonomica/Ethereum-IdentityProof</a> - Smart contract for Ethereum's account owner verification using Cryptonomica.net
* <a href="https://github.com/Cryptonomica/international-arbitration-law" target="_blank">/Cryptonomica/international-arbitration-law</a> - Repository for collecting information about international arbitration law and practice

### Assorted Ethereum Apps [**^**](#contents)

* [Deloitte SmartID](http://www.deloitte.co.uk/smartid/) [[**G**](https://github.com/SmartIdentity/smartId-contracts)]
   * "Smart Identity uses the Ethereum blockchain to represent an identity using a smart contract, attributes can be added by the identity owner and are stored in hash form"
* [Nuggets](http://www.nuggets.life/) [[**wp**](https://nuggets.life/images/Nuggets-White-Paper.pdf)]
   * "is a blockchain platform giving users a single biometric tool for login, payment and identity verification. It stores an individual's information in a "personal cloud" in "zero-knowledge blockchain storage".
* [poa.network](https://poa.network/)[**[D](https://medium.com/poa-network/poa-network-how-honey-badger-bft-consensus-works-4b16c0f1ff94)**]
 POA Network is an Ethereum-based platform that offers an open-source framework for smart contracts. POA Network is a sidechain to Ethereum utilizing [Proof of Authority](https://blockonomi.com/proof-of-authority/)
 as its consensus mechanism. 
