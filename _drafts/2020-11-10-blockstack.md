---
title: "Stacks: A Bitcoin Layer for Smart Contracts"
description: Stacks is a blockchain anchored by Bitcoin that enables apps, smart contracts, and digital assets.
excerpt: >
  the Stacks Bitcoin layer unlocks smart contracts and decentralized applications that use Bitcoin as their asset and perform the final settlement of transactions on the Bitcoin blockchain. Stacks allows BTC to be a productive asset without compromising its security and durability and enabling a wide range of applications like decentralized Bitcoin lending and Bitcoin-backed stablecoins.
layout: single
header:
  image: /images/blockstack_header.webp
  teaser: /images/blockstack_teaser.webp
categories: ["Web 3"]
tags: ["Blockstack","Bitcoin","Blockchain","DPKI"]
permalink: blockchain/blockstack/
toc: true
last_modified_at: 2023-06-10
---

## Main

[Website](https://www.stacks.co/) • [Foundation](https://www.stacks.org) • [GitHub](https://github.com/blockstack) • [Forum](https://forum.stacks.org/) • [Docs](https://docs.stacks.co/) • [Blog](https://www.stacks.co/blog) • [Twitter](https://twitter.com/Stacks) • [Apps](https://stacks.co) • [Discord](https://discord.gg/5DJaBrf)

* [Stacks: A Bitcoin Layer for Smart Contracts](https://gaia.blockstack.org/hub/1AxyPunHHAHiEffXWESKfbvmBpGQv138Fp/stacks.pdf)
  > With its Nakamoto release, the Stacks Bitcoin layer unlocks smart contracts and decentralized applications that use Bitcoin as their asset and perform the final settlement of transactions on the Bitcoin blockchain. Stacks allows BTC to be a productive asset without compromising its security and durability and enabling a wide range of applications like decentralized Bitcoin lending and Bitcoin-backed stablecoins. These applications through the Stacks layer allow people to use Bitcoin as money and the Bitcoin blockchain as the settlement of identity or application data, reducing the need for users to explore alternate, less secure L1 blockchains and crypto assets than BTC
* [Awesome Blockstack](https://github.com/friedger/awesome-stacks-chain) 2023-05-18
  > Stacks is a blockchain anchored by Bitcoin that enables apps, smart contracts, and digital assets. Stacks is a layer-1 blockchain that connects to Bitcoin and implements smart contracts and decentralized applications through the Clarity language. Through the Proof of Transfer (PoX) consensus mechanism, the state of the Stacks blockchain is anchored against the Bitcoin blockchain, thus providing the security and finality of Bitcoin to Stacks. Stacks brings the programmability of other blockchain technologies to Bitcoin, without the need to modify the core consensus mechanism of Bitcoin itself.
* [Launch HN: Stacks (YC S14) – The first SEC-qualified crypto token offering](https://news.ycombinator.com/item?id=20413420) 2019-07-11 news.ycombinator
  > Our regulatory approach is also very different from typical “ICOs” you may have seen. For distributing Stacks to the general public, we decided to work with US regulators. We wanted to open up the US market to our offering instead of blocking US investors. Yesterday, we received qualification from the SEC. The SEC has never qualified any token offering until now.
* [BitcoinWiki](http://en.bitcoinwiki.org/wiki/BlockStack)] 2019-02-22
  > BlockStack is a new network for decentralized applications[1]. Blockstack aims to address the centralization at the application-layer of the internet. More specifically, Blockstack builds an alternate DNS and alternate public-key infrastructure. It's the first implementation of a decentralized DNS system on top of the Bitcoin blockchain It combines DNS functionality with public key infrastructure and is primarily meant to be used by new blockchain applications.

## Decentralized ID

* [GreenPass Integrates Blockstack: Fighting Coronavirus While Protecting Your Privacy](https://blog.blockstack.org/greenpass-integrates-blockstack) 2020-08-18 Jenny Mith
  > GreenPass is a mobile app that aims to mitigate the impact of COVID-19 by helping users track and manage health data in a secure and private way. By utilizing decentralized identity (DID), verifiable credentials (VC), and distributed storage, GreenPass is able to preserve user privacy, which is critical given the sensitivity of the health related data being shared.
* [Presentation] [Blockstack and Verifiable Credentials](https://p2p.paris/gen/attADzQJ92rNIv6B3-Blockstack_and_Verifiable_Credentials_-_Paris_P2P_Festival_.pdf) 2020-01-10 Paris P2P Festival
  > • Keep auth and smart contracts on-chain
  > • Keep encrypted data off-chain
  > • Wrap everything in an easy JavaScript API
* [Blockstack DID Method Specification](https://github.com/blockstack/stacks-blockchain/blob/stacks-1.0/docs/blockstack-did-spec.md) 2019-07-19 Blockstack
  > Blockstack is a network for decentralized applications where users own their identities and data. Blockstack utilizes a public blockchain to implement a decentralized naming layer, which binds a user's human-readable username to their current public key and a pointer to their data storage buckets. The naming layer ensures that names are globally unique, that names can be arbitrary human-meaningful strings, and that names are owned and controlled by cryptographic key pairs such that only the owner of the private key can update the name's associated state.

## Web3 ID

* [Documentation] [Authentication](https://docs.blockstack.org/authentication/overview) - Blockstack Auth provides single sign on and authentication without third parties or remote servers.
  > A decentralized application and the Blockstack App communicate during the authentication flow by passing back and forth two tokens. The requesting application sends the Blockstack App an authRequest token. Once a user approves a sign-in, the Blockstack App responds to the application with an authResponse token. These tokens are JSON Web Tokens, and they are passed via URL query strings.
* [Documentation] [Blockchain naming system (BNS)](https://docs.blockstack.org/technology/naming-system)
  > BNS is a network system that binds names to off-chain state without relying on any central points of control. The Stacks V1 blockchain implemented BNS through first-order name operations. In Stacks V2, BNS is instead implemented through a smart-contract loaded during the genesis block.Names in BNS have three properties:
  > - Names are globally unique. The protocol does not allow name collisions, and all well-behaved nodes resolve a given name to the same state.
  > - Names are human-meaningful. Each name is chosen by its creator.
  > - Names are strongly-owned. Only the name's owner can change the state it resolves to. Specifically, a name is owned by one or more ECDSA private keys.
* [Blockstack Auth] [Bringing decentralized identity to traditional apps](https://larrysalibra.com/adding-blockstack-auth-to-discourse/) 2018-09-14
  > We really liked the Discourse forum software and wanted to give users the option to sign in with their Blockstack IDs.
  >
  > Enabling Blockstack Authentication on a centralized app potentially enables a range of functionality:
  > - single sign on - users with a Blockstack ID don't have to register again or sign up for your app
  > - an instant profile system - users can bring their existing profile to your app
  > - client-side encryption - you can encrypt user data on your users' client devices before sending it to your server. This is great for user privacy and may offer legal and security advantages for your business. Both hackers and law enforcement aren't able to access user data that has been encrypted with keys generated from a Blockstack ID. Hopefully this means they leave you alone!
* [Archived] [Blockstack: Design and Implementation of a Global Naming System with Blockchains](http://web.archive.org/web/20160909124003/https://blockstack.org/blockstack.pdf) 2016-06-22 Muneeb Ali, Jude Nelson, Ryan Shea
  > Blockchains like Bitcoin and Namecoin and their respective P2P networks have seen significant adoption in the past few years and show promise as naming systems with no trusted parties. Users can register human meaningful names and securely associate data with them, and only the owner of the particular private keys that registered them can write or update the name-value pair. In theory, many decentralized systems can be built using these blockchain networks, such as new, decentralized versions of DNS and PKI. As the technology is relatively new and evolving rapidly, however, little production data or experience is available to guide design tradeoffs.
  > 
  > In this paper, we describe our experiences operating a large deployment of a decentralized PKI service built on top of the Namecoin blockchain. We present various challenges pertaining to network reliability, throughput, and security that we needed to overcome while registering and updating over 33,000 entries and 200,000 transactions on the Namecoin blockchain. Further, we discuss how our experience informed the design of a new blockchain-based naming and storage system called Blockstack. We detail why we switched from the Namecoin network to the Bitcoin network for the new system, and present operational lessons from this migration.
  
