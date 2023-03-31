---
date: 2019-03-26
title: Ethereum Decentralized-Identity Github Repositories
description: Github Repositories for projects related to Ethereum Based Decentralized Identity.
excerpt: A listing of Github Repositories for projects related to Ethereum Based Decentralized Identity.
layout: single
header: 
  image: /images/ehtereum-github-header.webp
  caption: "[EIP #1056 - Ethereum Lightweight Identity](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1056.md)"
  teaser: /images/eth-git-thumb.webp
permalink: /blockchain/ethereum/repositories/
redirect_from: /ethereum/id-github/
canonical_url: 'https://decentralized-id.com/blockchain/ethereum/repositories/'
categories: ["Code"]
tags: ["Ethereum","Jolocom","uPort","Consensys","Universal Resolver"]
last_modified_at: 2019-07-11

---

A listing of any Github Repositories for Ethereum Based Decentralized Identity specifications and applications.


## EIP - ERC

* [ethereum/EIPs/issues/1056](https://github.com/ethereum/EIPs/issues/1056) - ERC: Lightweight Identity
  - This ERC describes a standard for creating and updating identities with a limited use of blockchain resources. An identity can have an unlimited number of delegates and attributes associated with it. Identity creation is as simple as creating a regular key pair ethereum account, which means that it's fee (no gas costs) and all ethereum accounts are valid identities. Furthermore this ERC is fully DID compliant.
* [ethereum/EIPs/issues/780](https://github.com/ethereum/EIPs/issues/780) - EIP-780 Ethereum Claims Registry
* [ethereum/EIPs / eip-712.md](https://github.com/ethereum/EIPs/blob/f29527ab39357548b06b29e937a48f06ae099de7/EIPS/eip-712.md) - EIP712
  - This is a standard for hashing and signing of typed structured data
* [ethereum/EIPs/issues/1495](https://github.com/ethereum/EIPs/issues/1495) - ERC-1484 Digital Identity Aggregator
  - A protocol for aggregating digital identity information that's broadly interoperable with existing, proposed, and hypothetical future digital identity standards.
* [ethereum/EIPs / eip-1078.md](https://github.com/ethereum/EIPs/blob/ed621645c8f3bc5756492f327cda015f35d9f8da/EIPS/eip-1078.md) - EIP-1078
  - This presents a method to replace the usual signup/login design pattern with a minimal ethereum native scheme, that doesn’t require passwords, backing up private keys nor typing seed phrases. 


## Jolocom

* [jolocom/docs](https://github.com/jolocom/docs) - Documentation
* [jolocom/smartwallet-app](https://github.com/jolocom/smartwallet-app) - A decentralized self sovereign identity solution developed by Jolocom.
* [jolocom/jolocom-lib](https://github.com/jolocom/jolocom-lib) - Library for interacting with the identity solution provided by Jolocom.
* [jolocom/jolocom-did-driver](https://github.com/jolocom/jolocom-did-driver) - Universal Resolver DID Driver for the did:jolo identity space
* [jolocom/generic-backend](https://github.com/jolocom/generic-backend) - A generic backend implementation that makes use of the Jolocom Library for authentication, and for issuing credentials.
* [jolocom/demo-sso](https://github.com/jolocom/demo-sso) - A simple example web application integrating the Jolocom library for authentication.
* [jolocom/demo-sso-mobile](https://github.com/jolocom/demo-sso-mobile) - An example mobile application in React Native that showcases the interaction flows between the Smartwallet and another mobile app.
* [jolocom/cred-types-jolocom-demo](https://github.com/jolocom/cred-types-jolocom-demo) - Collection of metadata definitions for the demo Jolocom credential types.
* [jolocom/react-native-build-config](https://github.com/jolocom/react-native-build-config) - Expose native build config to JS (android only for now)
* [jolocom/credTypes-jolocom-core](https://github.com/jolocom/credTypes-jolocom-core) - Collection of metadata definitions for the core Jolocom credential types.
* [jolocom/fueling-service](https://github.com/jolocom/fueling-service) - Simple express service that can wire ether to requester.
* [jolocom/registry-contract](https://github.com/jolocom/registry-contract) - A basic smart contract on top of the Ethereum network that registers mappings between DID and IPFS DDO hashes.
* [jolocom/smartwallet-webid-proxy](https://github.com/jolocom/smartwallet-webid-proxy) - WebID proxy service

## uPort

* [uport-project/developers](https://github.com/uport-project/developers) - Developer portal for documentation and application management
* [uport-project/specs](https://github.com/uport-project/specs) - uPort Protocol Specs
* [uport-project/uport-connect](https://github.com/uport-project/uport-connect) - Main uPort library for front end developers
* [uport-project/eth-typed-data](https://github.com/uport-project/eth-typed-data) - A javascript library for working with typed structured data as defined by EIP712
* [uport-project/uport-transports](https://github.com/uport-project/uport-transports) - Set up communication channels between your app and a uPort client to handle requests and responses.
* [uport-project/webcard](https://github.com/uport-project/webcard) - Transaction Sharing
* [uport-project/demo](https://github.com/uport-project/demo) - uPort Demo dApp
* [uport-project/uport-lite](https://github.com/uport-project/uport-lite) - Lightweight uport registry lookup
* [uport-project/eslint-config-uport](https://github.com/uport-project/eslint-config-uport) - Shareable eslint config for uport libraries
* [uport-project/uPort-live](https://github.com/uport-project/uPort-live) - Forked from Siunami/uPort-live
* [uport-project/uport-wordpress-plugin](https://github.com/uport-project/uport-wordpress-plugin) - A Passwordless Login for uPort and Wordpress
* [uport-project/community-projects](https://github.com/uport-project/community-projects) - A list of community hackathon projects and other experiments.
* [uport-project/udoor](https://github.com/uport-project/udoor) - uPort Door Management
* [uport-project/uport-bounties](https://github.com/uport-project/uport-bounties)- A Library of uPort Bounties
* [dconroy/CityKey](https://github.com/dconroy/CityKey) - Adding uPort support to Chicago CityKey, adding all the benefits of Self Sovereign Identity to municipal services. http://citykeychained.com

### uPort DID

* [uport-project/ethr-did-resolver](https://github.com/uport-project/ethr-did-resolver) - DID resolver for Ethereum Addresses with support for key management
* [uport-project/secp256k1-did-resolver](https://github.com/uport-project/secp256k1-did-resolver) - Resolve DID documents for secp256k1 public keys
* [uport-project/uport-did-driver](https://github.com/uport-project/uport-did-driver) - Driver for the uPort DID method
* [uport-project/eth-did-resolver](https://github.com/uport-project/eth-did-resolver) - DID resolver for Ethereum Addresses
* [uport-project/ethr-did](https://github.com/uport-project/ethr-did) - Create ethr DIDs
* [uport-project/ethr-did-registry](https://github.com/uport-project/ethr-did-registry) - Backing for an experimental DID method
* [uport-project/did-resolver](https://github.com/uport-project/did-resolver) - Generic did-resolver
* [uport-project/https-did-resolver](https://github.com/uport-project/https-did-resolver) - DID resolver for HTTPS domains
* [uport-project/nacl-did](https://github.com/uport-project/nacl-did) - Light weight DID method, complete with Identity Creation tools, encryption and JWT signing
* [uport-project/did-jwt](https://github.com/uport-project/did-jwt) - Create and verify uPort and DID compliant JWT's in Javascript
* [uport-project/uport-did-resolver](https://github.com/uport-project/uport-did-resolver) - DID resolver for uPort identities


### uPort Identification
* [uport-project/openid](https://github.com/uport-project/openid) - uPort openid
* [uport-project/kmnid](https://github.com/uport-project/kmnid) - A kotlin implementation of MNID
* [uport-project/uport-registry](https://github.com/uport-project/uport-registry) - Core uPort registry contract for linking attributes to uPort identities.
* [uport-project/uport-chrome-extension](https://github.com/uport-project/uport-chrome-extension) - An experiment to test decentralized identity in a Browser Extension environment.
* [uport-project/infrastructure](https://github.com/uport-project/infrastructure) - Support services for Self-Sovereign Identity
* [uport-project/mnid](https://github.com/uport-project/mnid) - Multi Network Identifier - spec and reference implementation



### uPort Mobile

* [uport-project/uport-android-sdk](https://github.com/uport-project/uport-android-sdk) - Collections of tools and helper libraries for android to issue and use identities on the uPort platform
* [uport-project/uport-android-signer](https://github.com/uport-project/uport-android-signer) - android ETH signer library to be used by uport app and sdk
* [uport-project/uport-android](https://github.com/uport-project/uport-android) - uPort app for android - under construction
* [uport-project/uport-ios-demo](https://github.com/uport-project/uport-ios-demo) - Demo iPhone app using uPort SDK
* [uport-project/uport-mobile-issues](https://github.com/uport-project/uport-mobile-issues) - This repository is a place for developers to report and track status of issues reported while using the uPort mobile app
* [uport-project/uport-mobile](https://github.com/uport-project/uport-mobile) - uPort mobile app
* [uport-project/uport-ios-sdk](https://github.com/uport-project/uport-ios-sdk) - uPort iOS SDK in Swift
* [uport-project/uport-ios-core-eth](https://github.com/uport-project/uport-ios-core-eth) - iOS Ethereum Toolkit for uPort SDK
* [uport-project/uport-ios-openssl](https://github.com/uport-project/uport-ios-openssl) - iOS OpenSSL Framework for uPort SDK
* [uport-project/UPTEthereumSigner](https://github.com/uport-project/UPTEthereumSigner) - Ethereum signer library for iOS



### uPort Lambda

* [uport-project/lambda-chasqui](https://github.com/uport-project/lambda-chasqui) - running_man Messenger service running_man
* [uport-project/lambda-agora](https://github.com/uport-project/lambda-agora) - An open public space where an assembly of applications can share details and be discovered (pre-alpha)
* [uport-project/lambda-champagne](https://github.com/uport-project/lambda-champagne)
* [uport-project/lambda-niscani](https://github.com/uport-project/lambda-niscani)
* [uport-project/lambda-sensui](https://github.com/uport-project/lambda-sensui) - uPort tx funding service
* [uport-project/lambda-caleuche](https://github.com/uport-project/) - Caleuche. Event Hub Service
* [uport-project/lambda-idgraph](https://github.com/uport-project/lambda-idgraph)
* [uport-project/lambda-olorun](https://github.com/uport-project/lambda-olorun) - uPort private network support
* [uport-project/lambda-fatima](https://github.com/uport-project/lambda-fatima) - uPort badge event attestor
* [uport-project/lambda-pututu](https://github.com/uport-project/lambda-pututu) - Push notification service
* [uport-project/lambda-nisaba](https://github.com/uport-project/lambda-nisaba) - Lambda functions for anti-sybill
* [uport-project/lambda-unnu](https://github.com/uport-project/lambda-unnu) - Creator of Identities

### uPort React

* [uport-project/react-native-uport-signer](https://github.com/uport-project/react-native-uport-signer) 
* [uport-project/react-native-signer-demo](https://github.com/uport-project/react-native-signer-demo) 
* [uport-project/uport-react-native-demo](https://github.com/uport-project/uport-react-native-demo)
* [uport-project/react-native-uport-connect](https://github.com/uport-project/react-native-uport-connect) - Library for integrating uPort into your React Native app
* [uport-project/react-uport-box](https://github.com/uport-project/react-uport-box) - Truffle and React/Redux boilerplate with uPort Connect
* [uport-project/react-native-passcode-android](https://github.com/uport-project/react-native-passcode-android) - Forked from aldigjo/react-native-passcode-android

### uPort Assorted
* [uport-project/champagne-dapp](https://github.com/uport-project/champagne-dapp) - Champagne Project dApp
* [uport-project/tweetnacl-k](https://github.com/uport-project/tweetnacl-k) - kotlin implementation of tweetnacl
* [uport-project/sample-data-generator](https://github.com/uport-project/sample-data-generator)
* [uport-project/bck-wallet](https://github.com/uport-project/bck-wallet)
* [uport-project/UPTEthereumSigner-Example](https://github.com/uport-project/UPTEthereumSigner-Example) - Example app and unit tests for the UPTEthereumSigner repo
* [uport-project/lastblock](https://github.com/uport-project/lastblock) - Daemon that alerts when a new block is mined
* [uport-project/service-tests](https://github.com/uport-project/service-tests) - Test servers from the outside
* [uport-project/paper](https://github.com/uport-project/paper)
* [uport-project/swift-rlp](https://github.com/uport-project/swift-rlp) - Recursive Length Prefix in Swift - CocoaPod
* [uport-project/SwiftKeccak](https://github.com/uport-project/SwiftKeccak) - Ethereum compatible Keccak hash for Swift
* [uport-project/ed2curve-js](https://github.com/uport-project/ed2curve-js) - Convert Ed25519 signing keys into Curve25519 Diffie-Hellman keys



## Spidchain
* [SpidChain/eth-lightwallet](https://github.com/SpidChain/eth-lightwallet) - Forked from ConsenSys/eth-lightwallet
  - Lightweight JS Wallet for Node and the browser
* [SpidChain/truffle](https://github.com/SpidChain/truffle) - Forked from trufflesuite/truffle
  - A development framework for Ethereum
* [SpidChain/VotingSystem](https://github.com/SpidChain/VotingSystem) - A dapp, library and smart contract to notarize votes on the ethereum blockchain
* [SpidChain/ethers-wallet](https://github.com/SpidChain/ethers-wallet) - Forked from ethers-io/ethers.js
  - Complete Ethereum wallet implementation and library in JavaScript.
* [SpidChain/nodejs-ethereum](https://github.com/SpidChain/nodejs-ethereum) - Forked from b9lab/nodejs-ethereum
Example of using NodeJs with Ethereum


## Cryptonomica
* [Cryptonomica/cryptonomica](https://github.com/Cryptonomica/cryptonomica) - Cryptonomica keys server
* [Cryptonomica/cryptonomica.github.io](https://github.com/Cryptonomica/cryptonomica.github.io) - Cryptonomica frontend
* [Cryptonomica/arbitration-rules](https://github.com/Cryptonomica/arbitration-rules) - Cryptonomica Arbitration Rules
* [Cryptonomica/dappathon-tlv](https://github.com/Cryptonomica/dappathon-tlv)
* [Cryptonomica/Ethereum-IdentityVerification](https://github.com/Cryptonomica/Ethereum-IdentityVerification) - Indentity verification and KYC for Ethereum blockchain
* [Cryptonomica/ethnode.cryptonomica.net](https://github.com/Cryptonomica/ethnode.cryptonomica.net) - Ethereum node with API on nodejs and web3.js
* [Cryptonomica/Ethereum-IdentityProof](https://github.com/Cryptonomica/Ethereum-IdentityProof) - Smart contract for Ethereum's account owner verification using Cryptonomica.net
* [Cryptonomica/international-arbitration-law](https://github.com/Cryptonomica/international-arbitration-law) - Repository for collecting information about international arbitration law and practice
