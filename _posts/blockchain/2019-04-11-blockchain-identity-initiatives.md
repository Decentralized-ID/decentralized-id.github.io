---
title: Assorted Blockchain Identity Initiatives
layout: single
classes: wide
permalink: /blockchain/
categories: ["Blockchain"]
tags: ["Blockpass","Ontology","Blockstack","Handshake","Democracy Earth"]
---


## Blockpass

<img src="https://imgur.com/mMZ4E2rl.png" />

* [Blockpass](https://www.blockpass.org/) [[**T**](https://twitter.com/BlockpassOrg)] [[**wp**](https://www.blockpass.org/downloads/BlockpassWhitepaper.v1.3.3.pdf)]
  * [Edinburgh Identity Lab](https://identity-lab.blockpass.org/) [[**ϟ**](https://www.newsbtc.com/2018/09/28/worlds-first-blockchain-identity-lab-launched-today-in-edinburgh/)]

## Ontology


* [ONTology](https://ont.io/) [[**G**](https://github.com/ontio/ontology-DID)]— "a "Distributed Trust Network" which combines a cross-chain identity system, peer-to-peer data transmission, data authorization mechanisms, distributed data storage, attestation, and various industry-specific modules. It also includes an Ontology Crypto Package (OCP) and an Ontology Marketplace (OM)."

## Blockstack

![](https://i.imgur.com/ZZx8lfR.png)

* [Blockstack](https://blockstack.org/) • [[**G**](https://github.com/blockstack)]ithub • [[**F**](https://forum.blockstack.org/)]orum • [[**B**](https://blockstack.org/blog)]log • [[**T**](https://twitter.com/blockstack)]witter • [[**W**](https://blockstack.org/whitepaper.pdf)]hitepaper • [[**bitcoinwiki**](https://en.bitcoinwiki.org/wiki/BlockStack)]
* a network of computers that collectively maintain a global registry of domain names, public keys, and cryptographic hashes. With this registry, Blockstack serves as a decentralized domain name system (DNS) and a decentralized public key infrastructure (PKI).
* [/dantrevino/awesome-blockstack](https://github.com/dantrevino/awesome-blockstack) [[**ϟ**](https://gitlab.com/dantrevino/awesome-blockstack)]
* [Onename](https://onename.com/) — "a product built on Blockstack that allows people to register identities"
* [App Mining](https://app.co/mining)
* [Launch HN: Stacks (YC S14) – The first SEC-qualified crypto token offering](https://news.ycombinator.com/item?id=20413420) -news.ycombinator
* [Introducing Clarity, a language for predictable smart contracts](https://blog.blockstack.org/introducing-clarity-the-language-for-predictable-smart-contracts/)
* [Extending Existing Blockchains with Virtualchain](https://www.zurich.ibm.com/dccl/papers/nelson_dccl.pdf)
* [Breaking Down Blockstack — Whitepaper Review](https://tokeneconomy.co/breaking-down-blockstack-whitepaper-review-3c828788f3e9)
* [Breaking Down Blockstack —  Stack Tokens](https://tokeneconomy.co/breaking-down-blockstack-pt-2-stack-tokens-7718578cfeae)
* [app.co/blockstack](https://app.co/blockstack)
* [docs.blockstack.org/core/naming/did.html](https://docs.blockstack.org/core/naming/did.html)
  >BNS nodes are compliant with the emerging Decentralized Identity Foundation protocol specification for decentralized identifiers (DIDs).
  >
  >Each name in BNS has an associated DID. The DID format for BNS is:
  >
  > `did:stack:v0:{address}-{index}`
* [Blockstack DID Spec](https://github.com/blockstack/blockstack-core/blob/master/docs/blockstack-did-spec.md)[[**ϟ**](https://forum.blockstack.org/t/did-method-at-identity-foundation/4287)]
* [Bringing decentralized identity to traditional apps](https://www.larrysalibra.com/blog/adding-blockstack-auth-to-discourse/)
  >TL;DR: In this technical post for developers, I walk through how we added Blockstack ID support to the Discourse forum software.

## Handshake
<img src="https://i.imgur.com/lhHnC8w.png"/>

* [Handshake](https://handshake.org) 
* [WhitePaper](https://handshake.org/files/handshake.txt)
* [Docs](https://handshake-org.github.io/)
* [twitter.com/HNS](https://twitter.com/hns)
* [github.com/handshake-org](https://github.com/handshake-org)

Handshake is a UTXO-based blockchain protocol which manages the registration, renewal and transfer of DNS top-level domains (TLDs). Our naming protocol differs from its predecessors in that it has no concept of namespacing or subdomains at the consensus layer. Its purpose is not to replace DNS, but to replace the root zone file and the root servers.

>Handshake is public blockchain that will serve as a global list of top-level domain names. By pointing your browser to resolve requests via the Handshake network instead of at your local DNS resolving server, you’ll essentially be looking up websites’ IP addresses on the Handshake blockchain, instead of those maintained on DNS resolvers that are centralized. - [The Case for Handshake](https://medium.com/amentum/the-case-for-handshake-9b0af0d989fe) A Compelling Bid to Decentralize Domain Names
Steven McKie

>Many fail to realize that DNS is already decentralized, with the exception of a single, critical component, of which trust is centralized: the root zone, or simply, a collection of top level domains (TLDs). And this trust anchor is kept by a small federation of authoritative bodies, where ICANN is currently the ultimate authority. - [Everything You Didn’t Know About the Handshake Naming System](https://hackernoon.com/everything-you-didnt-know-about-the-handshake-naming-system-how-this-blockchain-project-will-483464309f33)

>Certificate Authorities in the DNS network constructed the way it is today are the trusted stewards for the operation of the Internet. These stewards, as explained in the project paper, are profit-maximizing entities. Meaning, ICANN has no altruistic incentive to act honestly, yet has every incentive to maintain its natural monopoly over the riches that come with governing a critical layer of the Internet. And even if CAs intend to be good stewards, the premise of the decentralization movement posits that we should not ever need to rely on any single authority, especially one that acts as the gatekeeper to the highway of all human knowledge  - [Everything You Didn’t Know About the Handshake Naming System](https://hackernoon.com/everything-you-didnt-know-about-the-handshake-naming-system-how-this-blockchain-project-will-483464309f33)

* [Handshake: An experimental peer-to-peer root DNS (handshake.org)](https://news.ycombinator.com/item?id=17676312) -news.ycombinator.com
  >This seems like a neat idea but the economics are that of a for profit business, and I think we learned that handing domains to a for profit (NetworkSolutions) was a bad idea.
  >
  >7% going to contributors and 7% going to financial backers is a pretty big incentive. [0]
  >
  >I’d rather see this set up as a non profit foundation or a community driven trust and run in an OSS way for the financial elements. As it is, I don’t think we should create a decentralized network with such significant financial incentives.
  >
  >[0] https://handshake.org/how-it-works 
* [Handshake Whitepaper](https://namebase.io/handshake-whitepaper/)
  > This is a formatted and annotated version of the original Handshake whitepaper hosted by Namebase, a Handshake registrar and exchange. Last updated November 29, 2018.
  >
  >If you have questions about the whitepaper, message the Telegram group or email whitepaper@namebase.io and we will add a relevant annotation to the whitepaper.

### [handshake-org](https://github.com/handshake-org) - github

* [@handshake-org](https://github.com/handshake-org)
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
  * [handshake-org/blog](https://github.com/handshake-org/blog) - the Handshake project's blog
  * [handshake-org/faucet-tool](https://github.com/handshake-org/faucet-tool) - A tool to generate mnemonic seeds, keys and addresses for the Handshake Faucet
  * [handshake-org/hndshkBot](https://github.com/handshake-org/hndshkBot) - IRC Bot for developer faucet
  * [handshake-org/libhns](https://github.com/handshake-org/libhns) -C library for resolving handshake names (fork of c-ares)

## Democracy Earth

![](https://i.imgur.com/KxbXb1t.png)

* [Democracy Earth Foundation](http://democracy.earth/) [[**G**](https://github.com/DemocracyEarth/)][[**B**](https://words.democracy.earth/)][[**T**](https://twitter.com/DemocracyEarth)][[**C**](http://chat.democracy.earth/)] - Crypto Governance
   * [Sovereign](http://sovereign.software/)[[**G**](https://github.com/DemocracyEarth/sovereign)], a blockchain direct democracy tool using "vote" tokens to grant democratic participation rights to every human. A proof-of-individuality (POI) process based on peer-to-peer validation establishes that a self-sovereign identity is uniquely tied to a single person. Cooperation is happening with other decentralized identity initiatives such as Blockstack and uPort.
* [The Social Smart Contract](https://github.com/DemocracyEarth/paper#The_Social_Smart_Contract)[[**ϟ**](https://www.dropbox.com/s/sifogl4zimwkkei/Democracy%20Earth%20-%20Social%20Smart%20Contract%20-%20Paper%20v0.2.pdf?dl=0)] An Initial Rights Offering from Democracy Earth Foundation.
* [December App-Mining Results](https://words.democracy.earth/decembers-app-mining-results-are-live-7bd2b4f2390)
* [Yellow Jackets on the Sovereign Platform](https://words.democracy.earth/yellow-jackets-on-the-sovereign-platform-bdebe6d62ae1)
* [Meet the Dad Who Registered His Daughter’s Birth on the Blockchain](https://www.coindesk.com/meet-the-dad-who-registered-his-daughters-birth-on-the-blockchain) [[**ϟ**](https://www.coindesk.com/humans-on-the-blockchain-why-crypto-is-the-best-defense-against-ai-overlords)]
* Token: [Sale](https://token.democracy.earth/) • [Economics](https://www.dropbox.com/s/8q35dvht2hkfvqa/Democracy%20Earth%20-%20Token%20Economics.pdf?dl=0) • [testnet](https://votest.democracy.earth/)
>we worked with councils, senates, non profits, student centers, political parties, corporations.. but implementing real digital governance at scale really took off with crypto networks. our partnership with @blockstack is our biggest milestone of 2018. -[Santi](https://twitter.com/santisiri/status/1076259390154592256)

