---
title       : "Ceramic - 3box"
description : "Ceramic is a decentralized data network that powers an ecosystem of interoperable Web3 applications and services."
excerpt : "Designed to be cross-platform and highly configurable, IDX is compatible with all blockchains, wallets, and a wide variety of user and application data storage options including Ceramic, Textile, OrbitDB, Filecoin, IPFS, and Secure Data Stores — so you can seamlessly integrate decentralized identity with the rest of your Web3 tech stack."
header:
  image: #/images/3box_header.webp
  teaser: #/images/3box-teaser.webp
layout: single
author_profile: false
permalink: /web-3/ethereum/3box-ceramic/
redirect_from: 
  - /blockchain/3box/
canonical_url: 'https://decentralized-id.com/web-3/ethereum/3box-ceramic/'
categories: ["Web 3"]
tags: ["Ethereum","Ceramic","DIF","Web3","3box","uPort","IPID","Web3Connect","ENS","oCap","Gitcoin","revocation","DAO"]
last_modified_at: 2023-06-25
toc: true
---

## Ceramic

**[GitHub](https://github.com/ceramicnetwork/ceramic) • [Ceramic Studio](https://github.com/ceramicstudio) • [Documentation](https://developers.ceramic.network/learn/welcome/) • [Forum](https://forum.ceramic.network/)**

> Ceramic is a decentralized data network that powers an ecosystem of interoperable Web3 applications and services. Ceramic's event streaming protocol is a highly-scalable decentralized data infrastructure used for building all kinds of interoperable Web3 services and protocols, such as decentralized databases. Ceramic-powered databases and services enable thousands of Web3 developers to build data-intensive applications and solve the world's most complex data challenges. By decentralizing application databases, Ceramic makes data composable and reusable across all applications.

* [Protocol Overview](https://developers.ceramic.network/protocol/overview/)
  > Ceramic is a decentralized event streaming protocol that enables developers to build decentralized databases, distributed compute pipelines, and authenticated data feeds, etc. Ceramic nodes can subscribe to subsets of streams forgoing the need of a global network state. This makes Ceramic an eventually consistent system (as opposed to strongly consistent like L1 blockchains), enabling web scale applications to be built reliably.
  > 
  > The protocol doesn't prescribe how to interpret events found within streams; this is left to the applications consuming the streams. One example of this type of application is ComposeDB.
* [Tutorial: Getting Started With ComposeDB on Ceramic](https://blog.ceramic.network/getting-started-with-composedb-on-ceramic-2/) 2023-06-13 Ceramic
  > ComposeDB on Ceramic is a decentralized, composable graph database that empowers developers to store and interact with their application data efficiently and swiftly. By integrating Ceramic infrastructure with an indexer, reusable data models, and GraphQL, ComposeDB paves the way for the creation of truly interoperable and composable Web3 applications.
* [GitCoin working with Ceramic on “GitCoin Passport”](https://blog.ceramic.network/a-higher-personhood-score-means-more-contribution-matching/) 2022-06-08 Ceramic
  > PoPP signs and issues “stamps” to the user’s Passport that publicly attest to the user’s claims. Behind the scenes, these are Verifiable Credentials (VCs) that are stored on the user’s Ceramic streams.
* [Headline Introduces Creator-Controlled, Subscription-Based Publishing](https://blog.ceramic.network/headline-rewrites-subscription-based-publishing-for-web3/) 2022-05-31 Ceramic
  > The publishing protocol uses Unlock’s NFT-based access system and Ceramic’s decentralized data protocol to give creators full control over their content, communities and monetization.
* [How Web3 apps are building composable trust](https://blog.ceramic.network/how-web3-apps-are-building-composable-trust/) 2022-05-19 Ceramic
  > Explore the unique paradigms behind Web3 reputation, prominent use cases, and example architectures to incorporate credentials into your application.
* [Key Revocation in Self-Certifying Protocols](https://blog.ceramic.network/key-revocation-in-self-certifying-protocols/) 2022-04-28 Ceramic
  > In Web3 protocols cryptographic keys are used for encryption and signature verification. Typically a key is split into a public and a private key and because private keys are hard to keep secure, it is considered good practice to change keys over time.
* [3Box Labs, core developers of Ceramic, has raised a $30,000,000 Series A co-led by Multicoin Capital and Union Square Ventures](https://blog.ceramic.network/30-million-series-a-multicoin-usv/) 2022-02-16 Ceramic
  > …Ceramic, a decentralized network for composable Web3 data. The network consists of three core components:
  > 
  > 1. Scalable, decentralized data infrastructure
  > 2. Open APIs for storing, modifying, and retrieving data
  > 3. Community-created marketplace of reusable data models
* [User-centric data on Web3](https://blog.ceramic.network/user-centric-data-on-web3/) 2022-02-08 Ceramic
  > What if there was a way to give users full sovereign control over their data while getting access to not just the data from your application but many other compatible ones? 
* [DAOhaus adds functionality for rich member profiles for DAOs](https://blog.ceramic.network/daohaus-adds-rich-dao-member-profiles/) 2022-02-04 Ceramic
  > Identity in web3, as is the case in most DAOs today, is typically address based. Users represent themselves as their wallet or account address, but long hex strings are not sufficient. While ENS names are great for Ethereum mainnet, they don’t currently work across all the networks DAOhaus supports. Users need a human-readable identity solution that works across networks and the many tools DAOs commonly use.
* [Building capability-based data security for Ceramic](https://blog.ceramic.network/capability-based-data-security-on-ceramic/) 2022-01-05 Ceramic
  > The 3Box Labs team recently published a new standard for creating capability containers for accessing decentralized data to the Chain Agnostic Standards Alliance. Capability containers are an approach for managing advanced data security and permissions, commonly referred to as “Object Capabilities” or “OCAPs.”
  > 
  > This new standard is currently in development for use on Ceramic. Once deployed in a future version of the protocol, it will allow Ceramic to be fully compatible with the new Sign-in with Ethereum (SIWE) specification as well as provide advanced data flow control features for resources stored on the Ceramic network.
* [code] [An authentication system built with Ceramic & self.id](https://github.com/dabit3/decentralized-identity-example) 2021-12-11 dabit3
  > This project implements a user authentication flow leveraging an Ethereum wallet for single sign on capabilities across all of Web3.
  > 
  > The technologies used are [DID (decentralized identifiers)](https://www.w3.org/TR/did-core/), [Ceramic](https://ceramic.network/), [3id-connect](https://github.com/ceramicstudio/3id-connect), and [Self.ID](https://developers.ceramic.network/tools/self-id/overview/)
* [Building the Social Graph Infrastructure for Web3.0](https://blog.ceramic.network/building-the-social-graph-infrastructure-for-web3-0/) 2021-11-03
  > Using Ceramic, CyberConnect is building a new decentralized social graph protocol. This critical piece of web3 infrastructure is blockchain-agnostic and openly accessible for developers to build decentralized social networks and other apps in the Metaverse.
* [The next architecture for building Web3 data apps](https://blog.ceramic.network/the-next-architecture-for-building-web3-data-applications/) 2021-10-04 Ceramic
  > We're replacing the popular IDX runtime with a more powerful set of tools for building applications on Ceramic including DID DataStore, DataModels, and Self.ID.
* [Geo Web is connecting digital content to the physical world with NFTs and Ceramic](https://blog.ceramic.network/geo-web-is-connecting-digital-content-to-the-physical-world-with-nfts-and-ceramic/) 2021-06-17 Ceramic
  > With DID:NFT, because the content that is anchored to a Geo Web parcel can actually be owned by the parcel itself, when someone buys the land they're also getting the infrastructure that's been built up on that land.
* [3IDConnect](https://blog.ceramic.network/what-is-3id-connect/) 2020-11-25 Ceramic [GitHub](https://github.com/3box/3id-connect)\
*along with the slightly problematic frame that users have “a DID”*
  > 3ID Connect is a hosted authentication system for browser-based Ceramic applications that allows users to onboard to applications, control their DID, and interact with Ceramic streams using their existing blockchain accounts.
* [Identity-centric interoperability with the Ceramic Protocol – Joel Thorstensson – Webinar 57](https://ssimeetup.org/identity-centric-interoperability-ceramic-protocol-joel-thorstensson-webinar-57/) 2020-05-05
  > Ceramic is a new permissionless protocol for creating and accessing unstoppable documents that serve as the foundation for a connected, interoperable web without silos. Joel Thorstensson is the founder and CTO of 3Box and the primary author of the ceramic protocol as well as several Ethereum standards for identity and will provide a conceptual and technical intro to Ceramic.\
  > [...]\
  > Ceramic uses DIDs (Decentralized Identifiers), IPLD (InterPlanetary Linked Data), signed messages, and blockchain anchoring to create a trusted and shared graph of verifiable documents. While flexible, these documents are especially well-suited for self-sovereign identity systems, user-centric data ecosystems, and open web services.
* [Introduction to the Ceramic Protocol](https://medium.com/ceramic/introduction-to-the-ceramic-protocol-8d56951ae3f) 2020-03-24 Ceramic
  > For self-sovereign identity and to enable user-managed access control, 3Box uses Ceramic’s 3ID DID method which allows users to control their identity, information, and services using all of their existing private wallet keys.  

## 3box
[3box.io](https://3box.io/) • [Blog](https://medium.com/3box) • [GitHub](https://github.com/3box) • [twitter](https://twitter.com/3boxdb) • [discord](https://discord.gg/Z3f3Cxy)

* [IDX] [A Devkit for Open Identity](https://medium.com/3box/idx-a-devkit-for-open-identity-48edc88e8e85) 2020-10-23 3box\
*This is interesting, but they are taking on a huge amount of work without an [IPR](https://en.wikipedia.org/wiki/Intellectual_property#Intellectual_property_rights) container/wrapper).*
  > Designed to be cross-platform and highly configurable, IDX is compatible with all blockchains, wallets, and a wide variety of user and application data storage options including Ceramic, Textile, OrbitDB, Filecoin, IPFS, and Secure Data Stores — so you can seamlessly integrate decentralized identity with the rest of your Web3 tech stack.
* [3Box messaging plugins get more social!](https://medium.com/3box/3box-messaging-plugins-get-more-social-354e2afe88cb) 2020-02-06 - Message Likes, Reactions, Replies, and Votes
* [3Box Hub now supports ENS](https://medium.com/3box/3box-hub-now-supports-ens-af4a8efbd36e) 2020-01-07 - View ENS names inside Hub using ENS SDK and The Graph
* [Building a Distributed AppStore with 3Box](https://medium.com/3box/building-a-distributed-appstore-with-3box-ef7345aab34e) 2019-12-27 - How to build an app with 3Box SDK and Plugins
* [3Box Edit Profile Plugin](https://medium.com/3box/3box-edit-profile-plugin-8502509a4ff4) 2019-12-04 - Drop-in component for React applications
* [Introducing, 3Box Wall](https://medium.com/3box/introducing-3box-wall-7c299f4e0a1d) 2019-11-07 - Ready, set, socialize...Decentralized comments on 3Box Profiles
* [3Box Hub Search](https://medium.com/3box/3box-hub-search-6ba9ec0e672) 2019-10-23 - Discover users on 3Box with their ETH address 
* [Introducing, 3Box Chatbox Plugin](https://medium.com/3box/introducing-3box-chatbox-plugin-698f4433b9a9) 2019-10-18 - Drop-in chatrooms for your decentralized app
* [How FOAM uses 3Box threads to create a location-based review system](https://medium.com/3box/how-foam-uses-3box-threads-to-create-a-location-based-review-system-15ca1024e73) 2019-09-17 3box
  > The FOAM protocol allows cartographers to add points of interest to the FOAM map by staking tokens, which you can easily purchase on Uniswap. These points of interest can represent anything from restaurants to businesses, public parks, and more. See more at: https://map.foam.space/.
* [3Box Followers: Your Open Social Graph](https://medium.com/3box/3box-followers-your-open-social-graph-1f5e42c50afd) 2019-09-12 3box - Discover and follow Ethereum users. Build trust together.
* [Smarter authentication on 3Box Hub](https://medium.com/3box/smarter-authentication-on-3box-hub-dad11389de2) 2019-08-08 3box
  > Web3Connect is an open-source, drop-in web3 provider that abstracts away all of the complexity associated with supporting multiple web3 providers in your application. Although this library is fairly new, we’re excited to see the community moving in this direction.
* [3Box Decentralized Comments API 💬](https://medium.com/3box/3box-decentralized-comments-api-7e495d2ddd24) 2019-03-26 3box 
  > [Open Threads](https://github.com/3box/3box-js#using-threads) allow any number of users to openly send and receive messages in sequence. Thread data is stored on the 3Box network with the users themselves instead of on your server or the blockchain.
* [Introducing, 3Box Collectibles Gallery](https://medium.com/3box/introducing-3box-collectibles-gallery-4414f2a50551) 2019-03-07 3box
  > Browse your entire collectibles gallery alongside the rest of your web3 profile and curate a few favorites for others to see. 
* [3Box Builders Series: How to Integrate with Profiles](https://medium.com/3box/3box-builders-series-how-to-integrate-with-profiles-34078af41c47) 2019-03-03 3box
  > The Builders Series is a collection of blog posts aimed at helping developers easily build better distributed apps using the 3Box suite of APIs. 
* [Launching, 3Box Email Verification Service](https://medium.com/3box/launching-3box-email-verification-service-fc729981ec32) 2019-03-02 3box
  > In addition to making onboarding more convenient and seamless, verified email addresses also respect user privacy. Emails are saved to a user’s private 3Box profile, giving the user full control of their contact information. Verified emails are only shared with applications that the user explicitly approves.
* [A More Human Web3 Activity Feed](https://medium.com/3box/a-more-human-web3-activity-feed-2d3b8f62afec) 2019-02-19 3box
  > The new and improved 3Box activity feed integrates a user’s activity from across various networks that make up web3 today, including public Ethereum networks and the 3Box data network, into a single coherent view.
* [Shareable Public Profiles](https://medium.com/3box/shareable-public-profiles-94387c0d641e) 2019-01-28
  > Now with the addition of shareable profiles, anyone can view your public profile by clicking your profile URL.
* [Announcing, 3Box Partnership with Ethstats](https://medium.com/3box/announcing-3box-partnership-with-ethstats-d9c65f582e50) 2019-01-24
  > We’re excited to announce that 3Box has partnered with Ethstats to deliver the first ethereum explorer with built-in social profiles functionality.
* [Announcing 3Box.js 1.1.0 — API Boost](https://medium.com/3box/https-medium-com-3box-announcing-3box-js-1-1-0-api-boost-1339c8fa4cb8) 2018-12-27 3Box
  > Together these features work to improve performance and stability by reducing the average log-in time for users, reducing API response times for getProfile, and allowing developers to be much more efficient in writing their public profile queries.
* [Announcing Ethereum Profiles 1.0.0 is Live](https://medium.com/3box/announcing-ethereum-profiles-1-0-0-is-live-f0316e15ce23) 2018-10-24 3box
  > Ethereum Profiles allows Ethereum users to collect and control their information on the distributed web using their existing Ethereum wallets.

