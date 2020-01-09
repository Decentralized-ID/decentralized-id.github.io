---
title: Secure Scuttlebutt
description: Secure Scuttlebutt is a database protocol for unforgeable append-only message feeds.
excerpt: >
  Secure Scuttlebutt is a database protocol for unforgeable append-only message feeds.

  "Unforgeable" means that only the owner of a feed can update that feed, as enforced by digital signing (see Security properties). This property makes Secure Scuttlebutt useful for peer-to-peer applications. Secure Scuttlebutt also makes it easy to encrypt messages.
permalink: /decentralized-web/scuttlebot/
categories: ["Decentralized Web"]
tags: ["Scuttlebot", "P2P"]
header: 
  image: /images/scuttlebutt-header.png
  caption: "[In the Mesh: Scuttlebutt, A Decentralized Social Platform](https://www.inthemesh.com/archive/secure-scuttlebutt-facebook-alternative/)"
last_modified_at: 2020-01-09
---

## Secure Scuttlebutt

* [Scuttlebutt social network](https://scuttlebutt.nz) - a decentralised platform

* [Secure Scuttlebutt](https://scuttlebot.io/more/protocols/secure-scuttlebutt.html)  is a database protocol for unforgeable append-only message feeds.
  > "Unforgeable" means that only the owner of a feed can update that feed, as enforced by digital signing (see Security properties). This property makes Secure Scuttlebutt useful for peer-to-peer applications. Secure Scuttlebutt also makes it easy to encrypt messages.
  > 
  > Scuttlebot forms a global cryptographic social network with its peers. Each user is identified by a public key, and publishes a log of signed messages, which other users follow socially.
  > 
  > Scuttlebot searches the P2P mesh for new messages and files from followed users and from FoaFs (friend of a friend's). The messages and files are stored locally, indefinitely, for applications to read.
  > 
  > **Identity**
  > Users are identified by confirmations and signals in the social graph. This is known as a Web-of-Trust. There is no global registry of usernames. Instead, users name themselves, and share petnames for each other.
  > 
  > Discovery occurs by examining the social graph, or by out-of-band sharing. Applications can analyze the follow-graph, and look for "flag" messages, to determine who is trust-worthy in the network.
* [Scuttlebot](https://scuttlebot.io/) - a peer-to-peer log store
  > Scuttlebot is an open source peer-to-peer log store used as a database, identity provider, and messaging system. It features global replication, file-syncronization, and end-to-end encryption.
* [ssbc.github.io/docs/](https://ssbc.github.io/docs/) - Get started with Scuttlebot and the Secure Scuttlebutt protocol
  > Scuttlebot implemented by [ssb-server](http://ssbc.github.io/ssb-server/): a p2p log store
  > Secure Scuttlebutt implemented by [ssb-db](http://ssbc.github.io/ssb-db/): a global database protocol
  > [Patchwork](http://ssbc.github.io/patchwork/): a social messaging app built on ssb-server and ssb-db
* [Secure-scuttlebutt vs scuttlebutt vs scuttlebot vs sbot?](https://www.scuttlebutt.nz/faq/basics/ssb-vs-scuttlebutt-vs-scuttlebot-vs-sbot) -  Explanation of terms, repos and project history
  > - scuttlebutt: a gossip protocol that synchronises messages via a vector clock of per-node timestamps or sequences. Dominic got this name from an amazon paper "Efficient Reconciliation and Flow Control for Anti-Entropy Protocols". This is the original scuttlebutt module which should now be known as "insecure scuttlebutt". This repo is generally no longer used by the ssb community.
  > - ssb-db: this is the database part of ssb. Previously this term referred to the protocol/database as a whole.
  > - ssb-server: this repo adds networking behaviour to the database (secure-scuttlebutt).
  > - sbot: short for scuttlebot, previously the CLI command name to control ssb-server. Now also named ssb-server.
* [Manyverse](https://www.manyver.se) -  Mobile App
  > Manyverse is a social network mobile app with features you would expect: posts, threads, likes, profiles, etc. But it's not running in the cloud owned by a company, instead, your friends' posts and all your social data live entirely in your phone. This way, even when you're offline, you can scroll, read anything, and even write posts and like content! When your phone is back online, it syncs the latest updates directly with your friends' phones, through a shared local Wi-Fi or on the internet.

## Literature

* [A collection of news articles and blogs about Scuttlebutt](https://scuttlebutt.nz/docs/media/)
* [Design Challenge: Avoid Centralization and Singletons](https://scuttlebot.io/more/articles/design-challenge-avoid-centralization-and-singletons.html)
    > The danger of centralization is obvious: it creates a single point of failure that can easily be attacked, or act as an attacker. And, it creates a monoculture of information, as the central point starts to control what information is trusted, or ranked highly.
* [Design Challenge: Sybil Attacks](https://scuttlebot.io/more/articles/design-challenge-sybil-attack.html)
    > If it is possible for an anyone to connect to a computer system then it may be possible to interfere with the operation of that system, and defenses against interference must be designed in.
* [*Efficient Reconciliation and Flow Control for Anti-Entropy Protocols*](https://www.cs.cornell.edu/home/rvr/papers/flowgossip.pdf)
  > The paper shows that anti-entropy protocols can process only a limited rate of updates, and proposes and evaluates a new state reconciliation mechanism as well as a flow control scheme for anti-entropy protocols.
* [Announcing: SSB Rooms](https://www.manyver.se/blog/announcing-ssb-rooms) - [news.ycombinator.com](https://news.ycombinator.com/item?id=20828356)
  > Today I'm launching something I've been working on since May to help improve the Secure Scuttlebutt (SSB) ecosystem with a new type of server: SSB Rooms. As an alternative or complement to pub servers, rooms are servers intended as meeting places where peers come to discover others and establish network connections with each other.
* [Scuttlebutt - P2PFR](https://wiki.p2pfr.com/p2p/scuttlebutt)
  > Scuttlebutt est un logiciel libre, développé pour assurer des fonctions utiles à un réseau social (type Facebook, Mastodon, Diaspora…). Nous n'en parlerions pas autrement, la communication entre chaque participant(e) au réseau se fait en pair-à-pair. rec
* [Counter-Anti-Disintermediation](http://wiki.p2pfoundation.net/Counter-Anti-Disintermediation)
* [The Nomad Who’s Exploding the Internet Into Pieces](https://www.theatlantic.com/technology/archive/2017/05/meet-the-counterantidisintermediationists/527553/) - Could decentralizing online life make it more compatible with human life?
* [Scuttlebutt: an "off-grid" P2P social network that runs without servers and can fall back to sneakernet](https://boingboing.net/2017/04/07/bug-in-tech-for-antipreppers.html)
* [Efficient Reconciliation and Flow Control for Anti-Entropy Protocols]
  >The paper shows that anti-entropy protocols can process only a limited rate of updates, and proposes and evaluates a new state reconciliation mechanism as well as a flow control scheme for anti-entropy protocols. 
* [Designing a Secret Handshake: Authenticated Key Exchange as a Capability System](https://dominictarr.github.io/secret-handshake-paper/shs.pdf)
  > Capability Based Security is a conceptual framework for designing decentralized access control systems, yet there is no widely implemented protocol for establishing secure two-way communication that also forms a capability system. We examine the ways various key exchange protocols arn’t capability systems, and then present a secure key exchange protocol designed with capability systems in mind. In this protocol, the server’s public key forms an access capability. Using a preauthentication step, we authenticate the client before the server, but still accomplish mutual authentication within 4 passes. All long term keys are kept secret from any unauthenticated actors.

## Podcasts

* [‎Show Zero Knowledge, Ep Episode 81: P2P Messaging & Scuttlebutt with Dominic Tarr](https://podcasts.apple.com/us/podcast/zero-knowledge/id1326503043?i=1000441290356) - Jun 12, 2019
  > In this week’s episode, we meet with Dominic Tarr, a protocol designer and security auditor at Least Authority who works on Scuttlebutt - a decentralized secure gossip platform. We discuss P2P messaging and the challenges of sending messages within a p2p network in a truly decentralised manner.
  > * [Dynamo: Amazon’s Highly Available Key-value Store Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall and Werner Vogels](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
  > * [The Nomad Who’s Exploding the Internet Into Pieces](https://www.theatlantic.com/technology/archive/2017/05/meet-the-counterantidisintermediationists/527553/)
* [Libre Lounge - Episode 14: Secure Scuttlebutt with Joey Hess](https://librelounge.org/episodes/episode-14-secure-scuttlebutt-with-joey-hess.html)
  > Libre Lounge comes to you with an interview from Libre Planet with Joey Hess discussing the Secure Scuttbutt project, a secure social network. The interview goes into detail about the protocol, differences between SSB and ActivityPub, and how Secure Scuttlebutt is a bit like Git.
* [Epicenter - Secure Scuttlebutt – The “Localized” but Distributed Social Network](https://epicenter.tv/episode/290/) Dominic Tarr
  > We’re joined by Dominic Tarr, a sailor, and the Founder of Secure Scuttlebutt. This curiously named project has a fascinating approach to creating a truly distributed social network. One might even say that Secure Scuttlebutt is “localized” as it gracefully degrades to Sneakernet, something few blockchain projects can claim. In actuality, the SSB protocol isn’t a blockchain in the traditional sense – each user’s feed acts as a sort of localized chain of posts, signed by their public key, and possibly encrypted for a friend’s key to decrypt. When users meet, the system syncs their local databases using a gossip protocol and replicates the data. Encrypted data is transported from peer, to peer, to peer (or friends of friends) until it reaches its intended recipient. User may also optionally rely on public servers to sync data over the internet.
* [The Third Web #11 - Scuttlebutt & Cypherspace](https://soundcloud.com/arthurfalls/the-third-web-11-scuttlebutt-cypherspace)
  > The first application has been a multi-client decentralized social media platform that is an absolute joy to use, and I encourage everyone to download my favourite desktop client, Patchwork, or Manyverse for Android. As an autonomous software system, like Bitcoin, Scuttlebutt rewards the provisioning of resources to support the network, only rather than a point system and money myth, Scuttlebutt offers something far more valuable, conversation. This mostly covers the origin of the protocol but I will definitely conduct more interviews with Dom and others close to the project, which is today one of the most impressive, and well used decentralized applications in existence.


## Secure Scuttlebutt Consortium - GitHub Repos

* [Secure Scuttlebutt Consortium](https://github.com/ssbc) - A distributed and secure peer to peer social network
- [somebodyshould](https://github.com/ssbc/somebodyshould) - A repo of suggestions / issues / bugs / ideas / feedback for ssb
- [.github](https://github.com/ssbc/.github)
Settings for the SSBC GitHub organization.
- [scuttlebot.io](https://github.com/ssbc/scuttlebot.io) - Source repo for [https://scuttlebot.io](https://scuttlebot.io/)

Nearly all of these repositories have seen activity within the past year!

### Info

- [docs](https://github.com/ssbc/docs)
  > Scuttlebot implemented by ssb-server: a p2p log store
  > Secure Scuttlebutt implemented by ssb-db: a global database protocol
  > Patchwork: a social messaging app built on ssb-server and ssb-db
- [handbook.scuttlebutt.nz](https://github.com/ssbc/handbook.scuttlebutt.nz)
  > ssb handbook: A guide to the Secure Scuttlebutt key concepts and influences (see also, new website: [ssbc/scuttlebutt.nz](https://gitlab.com/ssbc/scuttlebutt.nz/))
- [modules.scuttlebutt.nz](https://github.com/ssbc/modules.scuttlebutt.nz) - Documentation for the Scuttlebutt module ecosystem
  > This is an aggregation of commonly used scuttlebutt modules grouped for your convenience into several sections.
- [ssb-spec-drafts](https://github.com/ssbc/ssb-spec-drafts) - protocol specifications for Secure Scuttlebutt
  > SSB-Drafts are working documents of the Secure Scuttlebutt community. Note that other groups may also distribute working documents as SSB-Drafts.
  > 
  > SSB-Drafts are draft documents valid for a maximum of six months and may be updated, replaced, or obsoleted by other documents at any time. It is inappropriate to use SSB-Drafts as reference material or to cite them other than as "work in progress."
  > 
  > This wording aligns with the IRTF's document track for Internet-Drafts.
- [scuttlebutt-protocol-guide](https://github.com/ssbc/scuttlebutt-protocol-guide) - Protocol documentation for Secure Scuttlebutt
* [scuttlebutt-guide]https://github.com/ssbc/scuttlebutt-guide
  > Looking to learn how to build in Scuttlebutt? There's currently no canonical resource, but here's a map of the known archipelago!

### Server

- [ssb-server](https://github.com/ssbc/ssb-server)
The gossip and replication server for Secure Scuttlebutt - a distributed social network
- [ssb-minimal-pub-server](https://github.com/ssbc/ssb-minimal-pub-server) - A minimal version of ssb-server aimed at pubs
- [multiserver](https://github.com/ssbc/multiserver)
A single interface that can work with multiple protocols, and multiple transforms of those protocols (eg, security layer)
- [ssb-config](https://github.com/ssbc/ssb-config)
standard configuration for ssb

### Client
- [react-native-ssb-client-keys](https://github.com/ssbc/react-native-ssb-client-keys)
- [ssb-client](https://github.com/ssbc/ssb-client) -  client library to scuttlebot
- [ssb-hello-ws](https://github.com/ssbc/ssb-hello-ws) - simplest example to get a ssb-client working over websockets
- [chocolatey-packages](https://github.com/ssbc/chocolatey-packages) - Chocolatey packages for SSB clients
- [scoop-bucket](https://github.com/ssbc/scoop-bucket) - A bucket for scoop package manager with app manifests for SSB clients.

### Patchwork
- [patchwork](https://github.com/ssbc/patchwork) - A decentralized messaging and sharing app built on top of Secure Scuttlebutt (SSB).
- [patchbay](https://github.com/ssbc/patchbay) - An alternative Secure Scuttlebutt client interface that is fully compatible with Patchwork
- [patchlite](https://github.com/ssbc/patchlite) - [WIP] A browser lite client for the Scuttlebutt network
- [patchgit](https://github.com/ssbc/patchgit) - Add git-ssb related functionality to patchcore related apps
- [patchbay-book](https://github.com/ssbc/patchbay-book) - The patchbay part of scuttle-book, a book rating system
- [patchcore](https://github.com/ssbc/patchcore) - A shared library of depject modules to build Secure Scuttlebutt social network apps
- [patchbay-gatherings](https://github.com/ssbc/patchbay-gatherings)
- [ssb-markdown](https://github.com/ssbc/ssb-markdown)
  > patchwork's markdown parser
- [patchbay-scry](https://github.com/ssbc/patchbay-scry)
- [patchwork-threads](https://github.com/ssbc/patchwork-threads) - library of patchwork's thread data-structures
- [patchwork-icons](https://github.com/ssbc/patchwork-icons)
- [patchbay-thread](https://github.com/ssbc/patchbay-thread)
- [patch-drafts](https://github.com/ssbc/patch-drafts)

### Schema

- [ssb-gathering-schema](https://github.com/ssbc/ssb-gathering-schema)
- [ssb-invite-schema](https://github.com/ssbc/ssb-invite-schema) - schema for scuttle-invite message types
- [ssb-audio-schema](https://github.com/ssbc/ssb-audio-schema)
- [ssb-thread-schema](https://github.com/ssbc/ssb-thread-schema)
- [ssb-schema-definitions](https://github.com/ssbc/ssb-schema-definitions) - Standardised schema definitions for ssb message types using is-my-json-valid
- [ssb-contact-schema](https://github.com/ssbc/ssb-contact-schema)
- [ssb-schema-validation](https://github.com/ssbc/ssb-schema-validation)
  > Build a set of validators using JSON schema with multiple schema versions

### Crypto

- [ssb-keys](https://github.com/ssbc/ssb-keys) - keyfile operations for ssb
- [ssb-caps](https://github.com/ssbc/ssb-caps) - The default "Caps" keys for accessing the SSB protocol using secret handshake
- [box2-spec](https://github.com/ssbc/box2-spec)
  > This is a spec for encrypting messages to groups of people. Initially it will support communication for large groups which share a public key (secret key cryptography / symmetric keys), but it has also been designed to support forward-secure secret-key cryptography (a little like Signal's double-ratchet).
- [ssb-ephemeral-keys](https://github.com/ssbc/ssb-ephemeral-keys) - Methods for encrypting messages with ephemeral keys over Secure Scuttlebutt
- [secret-stack](https://github.com/ssbc/secret-stack) - connect peers to each other using secret-handshakes
- [ssb-secret-blob](https://github.com/ssbc/ssb-secret-blob) - encrypted blobs over ssb protocol
- [private-box2](https://github.com/ssbc/private-box2) - new message encryption for ssb

### MuxRPC
- [muxrpc](https://github.com/ssbc/muxrpc) - lightweight multiplexed rpc
- [muxrpc-validation](https://github.com/ssbc/muxrpc-validation)- Forked from [pfrazee/muxrpc-validation](https://github.com/pfrazee/muxrpc-validation)
Validation library for muxrpc apis
- [ssb-plugins](https://github.com/ssbc/ssb-plugins)
  > ssb-plugins is a plugin that provides additional plugin related functionality to a secret-stack instance.
  > 
  > Without ssb-plugins, plugins can only be loaded explicitly by an ssb-server with the .use() method.
  > 
  > Generally speaking, this plugin provides the abilility for plugins to be loaded and run as a separate process, with communication over muxrpc.
- [muxrpcli](https://github.com/ssbc/muxrpcli) - command-line interface to muxrpc servers
  > muxrpc aims to provide remote access to any reasonable node.js api remotely. this means it supports both streaming and async operations. pull-streams are used.
  > 
  > It may seem at first that it would be logically cleaner to separate this into two concerns, multiplexing and request-response. Indeed, we did just that in multilevel combining mux-demux and rpc-stream however, I realized that multiplexing depends on adding framing to incoming messages, and so does rpc. If rpc is implemented as another layer on top of multiplexing, then the rpc messages end up with a second layer of framing too. By implementing one protocol that supports both streams and rpc, we were able to have both features with only a single layer of framing.

### Plugins

- [ssb-search](https://github.com/ssbc/ssb-search)
fulltext search as scuttlebot plugin
- [ssb-links](https://github.com/ssbc/ssb-links)
ssb-plugin that indexes all the links!
- [ssb-backlinks](https://github.com/ssbc/ssb-backlinks)
scuttlebot plugin for indexing all link mentions of messages
- [ssb-identities](https://github.com/ssbc/ssb-identities)
manage multiple identities as sbot plugin
- [ssb-serve-blobs](https://github.com/ssbc/ssb-serve-blobs)
  > Sbot plugin to serve blobs from a local http server
- [ssb-threads](https://github.com/ssbc/ssb-threads)
  > Scuttlebot plugin for fetching messages as threads
announce a public address for yourself
- [ssb-about](https://github.com/ssbc/ssb-about)
scuttlebot plugin for getting reduced 'about' state
- [ssb-social-index](https://github.com/ssbc/ssb-social-index)
scuttlebutt plugin for getting reduced state based on the author's social graph
- [gitbook-plugin-ssb](https://github.com/ssbc/gitbook-plugin-ssb)
GitBook plugin for Secure Scuttlebutt markdown formatting
- [ssb-private](https://github.com/ssbc/ssb-private)
scuttlebot plugin for indexed private messages


### Invites

- [ssb-peer-invites](https://github.com/ssbc/ssb-peer-invites)
  > A new ssb invite system to create invites without having a pub
- [ssb-invite](https://github.com/ssbc/ssb-invite) - "followbot" style invite codes for ssb
- [scuttle-invite-db](https://github.com/ssbc/scuttle-invite-db) - fluemview-reduce of invites and replies for scuttle invite
- [scuttle-invite](https://github.com/ssbc/scuttle-invite) - polymorphic invite and reply logic for secure scuttlebutt
- [ssb-invite-schema](https://github.com/ssbc/ssb-invite-schema) - schema for scuttle-invite message types

### Testing
- [scuttle-testbot](https://github.com/ssbc/scuttle-testbot)
- [compatibility](https://github.com/ssbc/compatibility)
tool to run tests of your dependencies, to check they are compatible
- [ssb-integration-tests](https://github.com/ssbc/ssb-integration-tests)
integration-tests for sbot
- [ssb-testing-guide](https://github.com/ssbc/ssb-testing-guide)
  > This is the start of a collection of patterns we've found useful for doing testing in the Scuttlebutt ecosystem

### Assorted

- [ssb-bin](https://github.com/ssbc/ssb-bin) - ssb cli commands
- [ssb-first-aid-kit](https://github.com/ssbc/ssb-first-aid-kit) - A user-friendly app for diagnosing and fixing problems with your Scuttlebutt installation
- [ssb-msgs](https://github.com/ssbc/ssb-msgs) - message-processing for ssb
- [ssb-validate](https://github.com/ssbc/ssb-validate) - better ssb validator
- [scuttle-shell](https://github.com/ssbc/scuttle-shell) - A system tray app for running Secure Scuttlebutt and providing sbot features to your local system
- [ssb-local](https://github.com/ssbc/ssb-local)
- [ssb-suggest](https://github.com/ssbc/ssb-suggest)
- [layered-graph](https://github.com/ssbc/layered-graph)
- [ssb-db](https://github.com/ssbc/ssb-db)
A database of unforgeable append-only feeds, optimized for efficient replication for peer to peer protocols
- [ssb-backup-tool](https://github.com/ssbc/ssb-backup-tool) - A backup tool for the Scuttleverse
- [ssb-ebt](https://github.com/ssbc/ssb-ebt)
  > secure scuttlebutt replication with epidemic-broadcast-trees
- [ssb-blob-files](https://github.com/ssbc/ssb-blob-files)
  > Channel a bunch of files from a dom event into the blob store. Get some tweaks and checks made along the way.
- [ssb-ooo](https://github.com/ssbc/ssb-ooo) - retrive ssb messages Out Of Order
- [multiblob](https://github.com/ssbc/multiblob) - A content-addressable-store that supports multiple hashing algorithms, and pull-streams
- [ssb-ahoy](https://github.com/ssbc/ssb-ahoy) - An onboarding mini-app - gets you all set up, and caught up on the gossip before you set out on your adventure
- [react-native-ssb-shims](https://github.com/ssbc/react-native-ssb-shims) - Node.js-related shims necessary for the SSB ecosystem to run on React Native apps
- [ssb-mentions](https://github.com/ssbc/ssb-mentions) - extract the mentions in a ssb message, just using the markdown.
- [ssb-replicate](https://github.com/ssbc/ssb-replicate) - ssb legacy replication, previously built into ssb-server
- [ssbc-sitegen](https://github.com/ssbc/ssbc-sitegen) - Tool to generate the GH pages for ssbc repos
- [ssb-friend-pub](https://github.com/ssbc/ssb-friend-pub)
- [ssb-unread](https://github.com/ssbc/ssb-unread)
- [ssb-blobs](https://github.com/ssbc/ssb-blobs) - blob gossiping ssb-subprotocol
- [ssb-lists](https://github.com/ssbc/ssb-lists)
  > This implements block/follow lists. (the main use-case was block lists) but a system that could both block and follow was not more complicated.
- [ssb-tangle](https://github.com/ssbc/ssb-tangle)
- [ssb-friends](https://github.com/ssbc/ssb-friends)
the logic around who to replicate or not
- [two.camp.scuttlebutt.nz](https://github.com/ssbc/two.camp.scuttlebutt.nz)
- [ssb-ref](https://github.com/ssbc/ssb-ref)
check if a string is a valid ssb-reference
- [ssb-gossip](https://github.com/ssbc/ssb-gossip)
Schedule connections randomly with a peerlist constructed from config, multicast UDP announcements, feed announcements, and API-calls
- [ssb-contact-msg](https://github.com/ssbc/ssb-contact-msg)
- [ssb-ws](https://github.com/ssbc/ssb-ws) - ssb-ws & http server for ssb
- [multiserver-scopes](https://github.com/ssbc/multiserver-scopes)
- [ssb-tunnel](https://github.com/ssbc/ssb-tunnel)
create a p2p link tunneled through a pub server
- [bench-ssb](https://github.com/ssbc/bench-ssb)
benchmarks for all the parts of ssb
- [chloride](https://github.com/ssbc/chloride)- Forked from [dominictarr/chloride](https://github.com/dominictarr/chloride)
- [ssb-query](https://github.com/ssbc/ssb-query)
- [ssb-device-address](https://github.com/ssbc/ssb-device-address)
- [village-tracker](https://github.com/ssbc/village-tracker)
village-tracker community volunteer coordination project
- [ssb-master](https://github.com/ssbc/ssb-master)
- [noto-color-emoji](https://github.com/ssbc/noto-color-emoji)
- [open-dyslexic](https://github.com/ssbc/open-dyslexic)- Forked from [antijingoist/open-dyslexic](https://github.com/antijingoist/open-dyslexic) - What I intend to be an opensource font for dyslexics and for high readability
- [ssbc-owners](https://github.com/ssbc/ssbc-owners) - set org owners as npm owners
- [scuttle-thread](https://github.com/ssbc/scuttle-thread)
- [ssb-incoming-guard](https://github.com/ssbc/ssb-incoming-guard)
- [ssb-graphviz](https://github.com/ssbc/ssb-graphviz) - visualize your ssb network graph
- [scuttlebutt-mars-workshop](https://github.com/ssbc/scuttlebutt-mars-workshop)
- [scuttle-tag](https://github.com/ssbc/scuttle-tag)- Forked from [wittjosiah/scuttle-tag](https://github.com/wittjosiah/scuttle-tag)
- [scuttle-poll](https://github.com/ssbc/scuttle-poll)
* [gathering](https://github.com/search?q=topic%3Agathering+org%3Assbc&type=Repositories)
- [scuttle-inject](https://github.com/ssbc/scuttle-inject)
- [scuttle-gathering](https://github.com/ssbc/scuttle-gathering)
- [scuttle-blog](https://github.com/ssbc/scuttle-blog)
- [scuttle-blob](https://github.com/ssbc/scuttle-blob)
- [pull-next-query](https://github.com/ssbc/pull-next-query)
- [paulcbetts-spellchecker-prebuilt](https://github.com/ssbc/paulcbetts-spellchecker-prebuilt)- Forked from [anaisbetts/node-spellchecker](https://github.com/anaisbetts/node-spellchecker)
- Forked from @paulcbetts/spellchecker to add automated prebuilds
- [opencollective_page](https://github.com/ssbc/opencollective_page)
- [nicedate](https://github.com/ssbc/nicedate)
nicely formatted dates since 7d ago
- [marked](https://github.com/ssbc/marked)- Forked from [clehner/marked](https://github.com/clehner/marked)
A markdown parser and compiler. This fork adds SSB-specific features, such as mentions and emojis.
- [keyboard-layout-prebuilt](https://github.com/ssbc/keyboard-layout-prebuilt)- Forked from [atom/keyboard-layout](https://github.com/atom/keyboard-layout)
Fork of keyboard-layout that adds automated prebuilds
- [grants-process](https://github.com/ssbc/grants-process)
grants-process
- [forked-systray/systrayhelper](https://github.com/ssbc/forked-systray/systrayhelper) - Forked from [zaaack/systray-portable](https://github.com/zaaack/systray-portable)  - A portable version of go systray, using stdin/stdout to communicate with other language
- [emoji-server](https://github.com/ssbc/emoji-server)
emoji middleware/server
- [ssb-viewer](https://github.com/ssbc/ssb-viewer)
- [ssb-sort](https://github.com/ssbc/ssb-sort)
- [ssb-names](https://github.com/ssbc/ssb-names)
- [packet-stream](https://github.com/ssbc/packet-stream)
- [ssb-webexthost](https://github.com/ssbc/ssb-webexthost)
- [ssb-typescript](https://github.com/ssbc/ssb-typescript) - Contains type definitions for common SSB concepts
- [multiserver-address](https://github.com/ssbc/multiserver-address)
- [level-sublevel](https://github.com/ssbc/level-sublevel)- Forked from [dominictarr/level-sublevel](https://github.com/dominictarr/level-sublevel) - no longer maintained, sorry!
- [packet-stream-codec](https://github.com/ssbc/packet-stream-codec)


