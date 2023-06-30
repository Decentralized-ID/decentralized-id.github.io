---
date: 2020-11-10
title: Handshake
description: Handshake is public blockchain that will serve as a global list of top-level domain names.
excerpt: >
    Handshake is a UTXO-based blockchain protocol which manages the registration, renewal and transfer of DNS top-level domains (TLDs). Our naming protocol differs from its predecessors in that it has no concept of namespacing or subdomains at the consensus layer. Its purpose is not to replace DNS, but to replace the root zone file and the root servers.
layout: single
header:
  image: /images/handshake-header.webp
  teaser: /images/handshake_teaser.webp
categories: ["Decentralized Web"]
tags: ["Blockchain","DNS","Handshake"]
permalink: /decentralized-web/handshake/
redirect_from: /blockchain/handshake/
last_modified_at: 2020-11-10
toc: false
---

**[Website](https://handshake.org) • [WhitePaper](https://handshake.org/files/handshake.txt) • [Docs](https://handshake-org.github.io/) • [Twitter](https://twitter.com/hns) • [Github](https://github.com/handshake-org) • [Hacker News](https://news.ycombinator.com/item?id=17673922)**

* [The Case for Handshake - A Compelling Bid to Decentralize Domain Names](https://medium.com/amentum/the-case-for-handshake-9b0af0d989fe) by Steven McKie
  > Handshake is public blockchain that will serve as a global list of top-level domain names. By pointing your browser to resolve requests via the Handshake network instead of at your local DNS resolving server, you’ll essentially be looking up websites’ IP addresses on the Handshake blockchain, instead of those maintained on DNS resolvers that are centralized. 

* [Everything You Didn’t Know About the Handshake Naming System](https://hackernoon.com/everything-you-didnt-know-about-the-handshake-naming-system-how-this-blockchain-project-will-483464309f33)
  > Many fail to realize that DNS is already decentralized, with the exception of a single, critical component, of which trust is centralized: the root zone, or simply, a collection of top level domains (TLDs). And this trust anchor is kept by a small federation of authoritative bodies, where ICANN is currently the ultimate authority. 
  > 
  > Certificate Authorities in the DNS network constructed the way it is today are the trusted stewards for the operation of the Internet. These stewards, as explained in the project paper, are profit-maximizing entities. Meaning, ICANN has no altruistic incentive to act honestly, yet has every incentive to maintain its natural monopoly over the riches that come with governing a critical layer of the Internet. 

* [Handshake Whitepaper](https://namebase.io/handshake-whitepaper/)
  > The foundation for the internet's security has relied upon trusted Certificate Authorities (CAs) which attest that a user is connecting to the correct server or node.1 This has created a reliance upon a handful of trusted actors, many of whom are for-profit corporations or other actors who may not have long-term incentive towards stewardship of the internet. The net-effect is a "1-of-m multisig" whereby if any one of the trusted CAs fail, the entire security of the internet fails. This failure has occurred and will continue to occur with the trusted-CA design, with catastrophic risks as more and more infrastructure becomes networked.

* [Handshake, ENS and Decentralized Naming Services Explained](https://medium.com/tokendaily/handshake-ens-and-decentralized-naming-services-explained-2e69a1ca1313)
  > The DNS database is large but the distributed nature of the blockchain could store information on millions of devices globally. With the information being stored and with the right consensus mechanism, we can avoid the reason to trust back-end servers to resolve queries. From a security perspective, we could mitigate most attacks by resolving to the immutable blockchain.

### Repositories

* [handshake-org/hsd](https://github.com/handshake-org/hsd) - Handshake Daemon & Full Node
* [handshake-org/hs-client](https://github.com/handshake-org/hs-client) - REST, websocket, and RPC client for hsd
* [handshake-org/urkel](https://github.com/handshake-org/urkel) - Cryptographically provable database (i.e. an urkel tree)
* [handshake-org/goosig](https://github.com/handshake-org/goosig) - Anonymous RSA signatures
* [handshake-org/handshake-org.github.io](https://github.com/handshake-org/handshake-org.github.io) - Handshake developer documentation site
* [handshake-org/hnsd](https://github.com/handshake-org/hnsd) - Handshake SPV name resolver
* [handshake-org/hs-miner](https://github.com/handshake-org/hs-miner) - Mining infrastructure for handshake
* [handshake-org/hs-airdrop](https://github.com/handshake-org/hs-airdrop) - Decentralized airdrop to open source developers
* [handshake-org/hs-names](https://github.com/handshake-org/hs-names) - Pre-reserved Handshake Names
* [handshake-org/hs-tree-data](https://github.com/handshake-org/hs-tree-data)
* [handshake-org/hdns](https://github.com/handshake-org/hdns) - Handshake-capable DNS module for node.js
* [handshake-org/bcuckoo](https://github.com/handshake-org/bcuckoo) - Cuckoo Cycle in pure javascript
* [handshake-org/faucet-tool](https://github.com/handshake-org/faucet-tool) - A tool to generate mnemonic seeds, keys and addresses for the Handshake Faucet
* [handshake-org/hndshkBot](https://github.com/handshake-org/hndshkBot) - IRC Bot for developer faucet
* [handshake-org/libhns](https://github.com/handshake-org/libhns) -C library for resolving handshake names (fork of c-ares)
