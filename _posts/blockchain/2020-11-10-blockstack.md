---
date: 2020-11-10
title: Blockstack
description: Blockstack is an open-source and developer-friendly network for building decentralized apps and smart contracts.
excerpt: >
  Blockstack builds an alternate DNS and alternate public-key infrastructure. It's the first implementation of a decentralized DNS system on top of the Bitcoin blockchain It combines DNS functionality with public key infrastructure and is primarily meant to be used by new blockchain applications.
layout: single
header:
  image: /images/blockstack_header.webp
  teaser: /images/blockstack_teaser.webp
categories: ["Companies"]
tags: ["Blockstack","Bitcoin","DID","Blockchain"]
permalink: blockchain/blockstack/
toc: false
last_modified_at: 2020-11-10
---

**[Website](https://blockstack.org/) • [GitHub](https://github.com/blockstack) • [Forum](https://forum.blockstack.org/) • [Blog](https://blockstack.org/blog) • [Twitter](https://twitter.com/blockstack) • [Whitepaper](https://blockstack.org/whitepaper.pdf) • [Apps](https://app.co)**

## Blockchain

* [BitcoinWiki](https://en.bitcoinwiki.org/wiki/BlockStack)]
  > BlockStack is a new network for decentralized applications[1]. Blockstack aims to address the centralization at the application-layer of the internet. More specifically, Blockstack builds an alternate DNS and alternate public-key infrastructure. It's the first implementation of a decentralized DNS system on top of the Bitcoin blockchain It combines DNS functionality with public key infrastructure and is primarily meant to be used by new blockchain applications.
* [Awesome Blockstack](https://github.com/dantrevino/awesome-blockstack) -[gitlab](https://gitlab.com/dantrevino/awesome-blockstack)
* [Launch HN: Stacks (YC S14) – The first SEC-qualified crypto token offering](https://news.ycombinator.com/item?id=20413420) -news.ycombinator
* [Introducing Clarity, a language for predictable smart contracts](https://blog.blockstack.org/introducing-clarity-the-language-for-predictable-smart-contracts/)
* [Extending Existing Blockchains with Virtualchain](https://www.zurich.ibm.com/dccl/papers/nelson_dccl.pdf)
* [Breaking Down Blockstack — Whitepaper Review](https://tokeneconomy.co/breaking-down-blockstack-whitepaper-review-3c828788f3e9)
  * [Breaking Down Blockstack pt2 —  Stack Tokens](https://tokeneconomy.co/breaking-down-blockstack-pt-2-stack-tokens-7718578cfeae)

## Identity

* [Blockchain naming system (BNS)](https://docs.blockstack.org/technology/naming-system)
  > BNS is a network system that binds names to off-chain state without relying on any central points of control. The Stacks V1 blockchain implemented BNS through first-order name operations. In Stacks V2, BNS is instead implemented through a smart-contract loaded during the genesis block.Names in BNS have three properties:
  > - Names are globally unique. The protocol does not allow name collisions, and all well-behaved nodes resolve a given name to the same state.
  > - Names are human-meaningful. Each name is chosen by its creator.
  > - Names are strongly-owned. Only the name's owner can change the state it resolves to. Specifically, a name is owned by one or more ECDSA private keys.
* [Blockstack DID Method Specification](https://github.com/blockstack/stacks-blockchain/blob/stacks-1.0/docs/blockstack-did-spec.md)
  > Blockstack is a network for decentralized applications where users own their identities and data. Blockstack utilizes a public blockchain to implement a decentralized naming layer, which binds a user's human-readable username to their current public key and a pointer to their data storage buckets. The naming layer ensures that names are globally unique, that names can be arbitrary human-meaningful strings, and that names are owned and controlled by cryptographic key pairs such that only the owner of the private key can update the name's associated state.
* [Authentication](https://docs.blockstack.org/authentication/overview) - Blockstack Auth provides single sign on and authentication without third parties or remote servers.
  > A decentralized application and the Blockstack App communicate during the authentication flow by passing back and forth two tokens. The requesting application sends the Blockstack App an authRequest token. Once a user approves a sign-in, the Blockstack App responds to the application with an authResponse token. These tokens are JSON Web Tokens, and they are passed via URL query strings.
* [DID method at identity.foundation](https://forum.blockstack.org/t/did-method-at-identity-foundation/4287) (forum post about DID Method)
* [Bringing decentralized identity to traditional apps](https://larrysalibra.com/adding-blockstack-auth-to-discourse/)
  > We really liked the Discourse forum software and wanted to give users the option to sign in with their Blockstack IDs.
  >
  > Enabling Blockstack Authentication on a centralized app potentially enables a range of functionality:
  > - single sign on - users with a Blockstack ID don't have to register again or sign up for your app
  > - an instant profile system - users can bring their existing profile to your app
  > - client-side encryption - you can encrypt user data on your users' client devices before sending it to your server. This is great for user privacy and may offer legal and security advantages for your business. Both hackers and law enforcement aren't able to access user data that has been encrypted with keys generated from a Blockstack ID. Hopefully this means they leave you alone!
  