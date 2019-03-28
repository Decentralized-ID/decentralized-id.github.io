---
title: XDI
layout: single
---

* [tutorial.xdi2.org](https://tutorial.xdi2.org)
  > XDI is a technology for modeling, storing, and manipulating data.
  >
  > It fits into a similar category of technologies as JSON, XML and RDF, but also has a number of properties that distinguishes it.
  >
  > XDI is a graph-based data model. This means that all data is expressed using nodes and arcs in a graph. At a minimum, a graph consists of a single node, called the common root node.

## Contents

* [Intro](#intro)
* [RWoT Papers](#rwot-papers-)
* [Project Danube](#project-danube-)
* [Github Repos](#github-repos-)
  * [OASIS XDI TC Technical Committee](#oasis-xdi-tc-technical-committee-)
  * [Danube Github](#danube-github-)
    * [XDI - Various Integrations](#xdi---various-integrations-)
    * [XDI Configurations](#xdi-configurations-)
    * [XDI Examples](#xdi-examples-)
    * [XDI Plugins](#xdi-plugins-)
    * [Aeternam](#aeternam-)
    * [XDI Cloud](#xdi-cloud-)
    * [XDI Server Deployed Via](#xdi-server-deployed-via-)
    * [Services](#services-)

## Intro

The XNS Public Trust Organization was founded in July 2000, shortly after International Planetwork Conference. -[xdi.org - History](http://xdi.org/?page_id=13)
  > to promote the concept of individuals owning their own digital identity and data based on a nascent technology being produced by two Technical Committees at OASIS: XRI (Extensible Resource Identifier) and XDI (Extensible Data Interchange).
* [xdi.org](http://xdi.org/) is a non-profit public trust organization whose purpose is to provide public infrastructure for digital identity, security, and privacy using the open standard XDI semantic data interchange protocol developed by the OASIS XDI Technical Committee.


## RWoT Papers

* [Cool hack with XDI graphs, blockstore, link contracts, and cryptographic identifiers](https://github.com/WebOfTrustInfo/rwot1-sf/blob/master/topics-and-advance-readings/cool-hack-xdi-blockstore-bip32.md) 
  - Markus Sabadello *[@Peacekeeper](https://twitter.com/Peacekeeper) \<markus@projectdanube.org\>*
* [XDI Link Contracts: An Overview](https://github.com/WebOfTrustInfo/rwot1-sf/blob/master/topics-and-advance-readings/xdi-link-contracts.md) 
  - Drummond Reed *[@DrummondReed](https://twitter.com/DrummondReed) \<drummond@respect.network\>*
* [XDI Graphs in IPFS](/topics-and-advance-readings/XDI-Graphs-in-IPFS.md) 
  - Markus Sabadello
* [XDI Verifiable Claims and Link Contracts](https://github.com/WebOfTrustInfo/rwot4-paris/tree/master/topics-and-advance-readings/xdi-verifiable-claims-link-contracts.md) by Markus Sabadello
* [First XDI Link Contract between "btcr" DID and "sov" DID](https://github.com/WebOfTrustInfo/rwot5-boston/tree/master/topics-and-advance-readings/first-xdi-link-contract-between-btcr-did-and-sov-did.md) by Markus Sabadello
* [DID Whitepaper](https://github.com/WebOfTrustInfo/rwot2-id2020/blob/master/topics-and-advance-readings/DID-Whitepaper.md)
  > In April 2015 the XDI.org trustees formed the XDI Registry Working Group (XRWG) to transition XDI registry infrastructure from a centralized model to a new decentralized blockchain-based model.
  > 
  > The charter of the XRWG includes the following principles:
  >
  > * Maximum interoperability.   
  > * Minimum viable centralization. 
  > * Critical infrastructure. The XDI Registry must provide for a high level of reliability, stability, scalability, security, sustainability and other requirements typical of critical internet infrastructure.
  > * Sovereign identity. The XDI Registry should enable any XDI authority (person or organization) to fully administer its own registry and/or its own entry in an xdi.org-specified registry, without the need to rely on any particular external administrative authority.
  > * Neutrality. The XDI Registry should be available to all members of the public and should not discriminate against any party that wishes to use it for any lawful purpose.
  >
  > [...]
  >
  > A DID architecture should focus on the set of components that Mr. Gupta refers to as "the minimum required for people to be able to do business (or other critical functions) together".
  >
  >**A Decentralized Identifier (DID) Registry and Discovery Service**
  >
  > This "minimum required" is defined by a union of the proposed requirements identified by the W3C Credential Community Group, the XDI.org Registry Working Group, and the Rebooting the Web of Trust group. It consists of three functions that can be addressed by a combination of blockchain and DHT technology:
  >
  > * A DID registration function
  > * A discovery function - enables looking up a registered DID in the blockchain
  > * A master key recovery function



## Project Danube

Markus Sabadello began working on Project Danube [around 2010](https://web.archive.org/web/20101221105543/http://projectdanube.org/)

>This is an open-source project offering software for identity and personal data services on the Internet. The core of this project is an XDI-based Personal Data Store - a semantic database for your personal data, which always remains under your control. Applications on top of this database include the Federated Social Web, the selective sharing of personal data with organizations, and much more.

## Github Repos

## OASIS XDI TC Technical Committee

* <a href="https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook">/OASIS-XDI-Technical-Committee/xdi-spec-docbook</a> - XDI Specifications (Docbook)
* <a href="https://github.com/OASIS-XDI-Technical-Committee/xdi-developers-guide">/OASIS-XDI-Technical-Committee/xdi-developers-guide</a> - XDI Developer's Guide
* <a href="https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-openoffice">/OASIS-XDI-Technical-Committee/xdi-spec-openoffice</a> - XDI Specifications (Open Office)
* <a href="https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-dita">/OASIS-XDI-Technical-Committee/xdi-spec-dita</a> - XDI Specifications (DITA)
* <a href="https://github.com/OASIS-XDI-Technical-Committee/">/OASIS-XDI-Technical-Committee/</a>
* <a href="https://github.com/OASIS-XDI-Technical-Committee/">/OASIS-XDI-Technical-Committee/</a>
* <a href="https://github.com/OASIS-XDI-Technical-Committee/">/OASIS-XDI-Technical-Committee/</a>

## Danube Github
* <a href="https://github.com/projectdanube/xdi2" target="_blank">/projectdanube/xdi2</a> - XDI2 general purpose library and server
* <a href="https://github.com/projectdanube/xdi-js" target="_blank">/projectdanube/xdi-js</a> - XDI client library for JavaScript
* <a href="https://github.com/projectdanube/xdi2-connect-core" target="_blank">/projectdanube/xdi2-connect-core</a> - Shared library for the XDI Connect protocol
* <a href="https://github.com/projectdanube/indy-sdk-java" target="_blank">/projectdanube/indy-sdk-java</a> - Java binding to the native Indy SDK
* <a href="https://github.com/projectdanube/xdi-tutorial" target="_blank">/projectdanube/xdi-tutorial</a> - XDI Tutorial
* <a href="https://github.com/projectdanube/XDINinja-swing" target="_blank">/projectdanube/XDINinja-swing</a> - XDI-enabled standalone client application
* <a href="https://github.com/projectdanube/xdi2-tools" target="_blank">/projectdanube/xdi2-tools</a> - XDI2 maintenance and other tools
* <a href="https://github.com/projectdanube/xdi2-docker" target="_blank">/projectdanube/xdi2-docker</a> - Dockerfiles for XDI2
* <a href="https://github.com/projectdanube/xdi2-connect-buttonbuilder" target="_blank">/projectdanube/xdi2-connect-buttonbuilder</a> - "Button Builder" component for the XDI Connect protocol

### XDI - Various Integrations [**^**](#contents-)

* <a href="https://github.com/projectdanube/xdi2-bdb" target="_blank">/projectdanube/xdi2-bdb</a> - Support for using BDB as XDI2 backend storage
* <a href="https://github.com/projectdanube/xdi2-mongodb" target="_blank">/projectdanube/xdi2-mongodb</a> - Support for using MongoDB as XDI2 backend storage
* <a href="https://github.com/projectdanube/xdi2-server-heroku" target="_blank">/projectdanube/xdi2-server-heroku</a> - XDI2 Server deployed via Heroku
* <a href="https://github.com/projectdanube/xdi2-redis" target="_blank">/projectdanube/xdi2-redis</a> - Support for using Redis as XDI2 backend storage
* <a href="https://github.com/projectdanube/xdi2-tor" target="_blank">/projectdanube/xdi2-tor</a> - Integration of XDI and Tor
* <a href="https://github.com/projectdanube/xdi2-ipfs" target="_blank">/projectdanube/xdi2-ipfs</a> - Integration of XDI and IPFS
* <a href="https://github.com/projectdanube/withsqlite" target="_blank">/projectdanube/withsqlite</a> - A module for a python dict that back ends on an sqlite3 database. It's bit like shelve but with json and sqlite3.
  - Forked from jvasile/withsqlite
* <a href="https://github.com/projectdanube/blockstack-cli-java" target="_blank">/projectdanube/blockstack-cli-java</a> - Java client for Blockstore

### XDI Configuration

* <a href="https://github.com/projectdanube/xdi2-selfhosted" target="_blank">/projectdanube/xdi2-selfhosted</a> - A configuration profile of the XDI2 server for self-hosting a single XDI graph.
* <a href="https://github.com/projectdanube/xdi2-csp" target="_blank">/projectdanube/xdi2-csp</a> - A configuration profile of the XDI2 server for hosting a dynamic number of XDI graphs.
* <a href="https://github.com/projectdanube/xdi2-registry" target="_blank">/projectdanube/xdi2-registry</a> - 
A configuration profile of the XDI2 server for hosting a registry of XDI names and XDI numbers.

### XDI Examples

* <a href="https://github.com/projectdanube/xdi2-example-messaging" target="_blank">/projectdanube/xdi2-example-messaging</a> - XDI2 Examples: Basic messaging functionality.
* <a href="https://github.com/projectdanube/xdi2-example-advanced-server" target="_blank">/projectdanube/xdi2-example-advanced-server</a> - XDI2 Examples: Setting up advanced XDI servers.
* <a href="https://github.com/projectdanube/xdi2-example-core" target="_blank">/projectdanube/xdi2-example-core</a> - XDI2 Examples: Simple uses of the core functionality.
* <a href="https://github.com/projectdanube/xdi2-example-client" target="_blank">/projectdanube/xdi2-example-client</a> - XDI2 Examples: Writing XDI client applications.
* <a href="https://github.com/projectdanube/xdi2-example-secp256k1-server" target="_blank">/projectdanube/xdi2-example-secp256k1-server</a> - Example XDI server using cid-2 cryptographic XDI numbers.
* <a href="https://github.com/projectdanube/xdi2-example-ec25519-server" target="_blank">/projectdanube/xdi2-example-ec25519-server</a> - Example XDI server using cid-1 cryptographic XDI numbers.
* <a href="https://github.com/projectdanube/xdi2-connect-acmenews" target="_blank">/projectdanube/xdi2-connect-acmenews</a> - +acmenews XDI2 demo
* <a href="https://github.com/projectdanube/xdi2-connect-leshop" target="_blank">/projectdanube/xdi2-connect-leshop</a> - +leshop XDI2 demo
* <a href="https://github.com/projectdanube/xdi2-example-secp256k1-client" target="_blank">/projectdanube/xdi2-example-secp256k1-client</a> - Example XDI client using cid-2 cryptographic XDI numbers.
* <a href="https://github.com/projectdanube/xdi2-example-ec25519-client" target="_blank">/projectdanube/xdi2-example-ec25519-client</a> - Example XDI client using cid-1 cryptographic XDI numbers.

### XDI Plugins

* <a href="https://github.com/projectdanube/xdi2-crypto-secp256k1" target="_blank">/projectdanube/xdi2-crypto-secp256k1</a> - This is an secp256k1 crypto plugin for the XDI2 client and server.
* <a href="https://github.com/projectdanube/xdi2-crypto-ec25519" target="_blank">/projectdanube/xdi2-crypto-ec25519</a> - This is an Ed25519 crypto plugin for the XDI2 client and server.
* <a href="https://github.com/projectdanube/xdi2-connector-facebook" target="_blank">/projectdanube/xdi2-connector-facebook</a> - A connector plugin for the XDI2 server that maps data from Facebook to XDI
* <a href="https://github.com/projectdanube/xdi2-connector-meeco" target="_blank">/projectdanube/xdi2-connector-meeco</a> - A connector plugin for Meeco
* <a href="https://github.com/projectdanube/XDINinja-plugin" target="_blank">/projectdanube/XDINinja-plugin</a> - A browser plugin that is like "Twitter for data"
* <a href="https://github.com/projectdanube/xdi2-connector-cozy" target="_blank">/projectdanube/xdi2-connector-cozy</a> - A connector plugin for CozyCloud
* <a href="https://github.com/projectdanube/xdi2-filesys" target="_blank">/projectdanube/xdi2-filesys</a> - Plugin for an XDI2 server to integrate with a local filesystem
* <a href="https://github.com/projectdanube/xdi2-connector-personal" target="_blank">/projectdanube/xdi2-connector-personal</a> - A connector plugin for the XDI2 server that maps data from Personal.com to XDI

### Aeternam

* <a href="https://github.com/projectdanube/aeternam-xdi-sncf" target="_blank">/projectdanube/aeternam-xdi-sncf</a> - Aeternam PNR Demo: SNCF
* <a href="https://github.com/projectdanube/aeternam-xdi-db" target="_blank">/projectdanube/aeternam-xdi-db</a> - Aeternam PNR Demo: Deutsche Bahn
* <a href="https://github.com/projectdanube/aeternam-xdi-tests" target="_blank">/projectdanube/aeternam-xdi-tests</a> - XDI experimentation for ÆTERNAM / ÆVATAR
* <a href="https://github.com/projectdanube/aeternam-xdi-maria" target="_blank">/projectdanube/aeternam-xdi-maria</a> - Aeternam PNR Demo: Maria
* <a href="https://github.com/projectdanube/aeternam-xdi-webshop" target="_blank">/projectdanube/aeternam-xdi-webshop</a> - Aeternam PNR Demo: Webshop
* <a href="https://github.com/projectdanube/aeternam-xdi-oebb" target="_blank">/projectdanube/aeternam-xdi-oebb</a> - Aeternam PNR Demo: ÖBB

### XDI Cloud

* <a href="https://github.com/projectdanube/xdi2-cloudcards" target="_blank">/projectdanube/xdi2-cloudcards</a> - XDI Cloud Card Viewer
* <a href="https://github.com/projectdanube/xdi2-messenger" target="_blank">/projectdanube/xdi2-messenger</a> - XDI Cloud Messenger
* <a href="https://github.com/projectdanube/xdi2-manager" target="_blank">/projectdanube/xdi2-manager</a> - XDI Cloud Manager
* <a href="https://github.com/projectdanube/xdi2-pixel" target="_blank">/projectdanube/xdi2-pixel</a> - Tool to translate a personal cloud policy language (Pixel) to XDI link contracts.

### XDI Server Deployed Via

* <a href="https://github.com/projectdanube/xdi2-server-grizzly" target="_blank">/projectdanube/xdi2-server-grizzly</a> - XDI2 Server deployed via Grizzly
* <a href="https://github.com/projectdanube/xdi2-server-mina" target="_blank">/projectdanube/xdi2-server-mina</a> - XDI2 Server deployed via Apache MINA
* <a href="https://github.com/projectdanube/xdi2-server-netty" target="_blank">/projectdanube/xdi2-server-netty</a> - XDI2 Server deployed via netty
* <a href="https://github.com/projectdanube/xdi2-server-undertow" target="_blank">/projectdanube/xdi2-server-undertow</a> - XDI2 Server deployed via Undertow
* <a href="https://github.com/projectdanube/xdi2-server-vertx" target="_blank">/projectdanube/xdi2-server-vertx</a> - XDI2 Server deployed via vert.x

### Sevices
* <a href="https://github.com/projectdanube/xdi2-connect-service" target="_blank">/projectdanube/xdi2-connect-service</a> - This is a "Connect Service" component for the XDI Browser binding.
* <a href="https://github.com/projectdanube/neustar-discovery-service" target="_blank">/projectdanube/neustar-discovery-service</a> - Neustar XDI Discovery Service based on XRI Resolution
  - Forked from neustarpc/neustar-discovery-service
* <a href="https://github.com/projectdanube/xdi2-connect-auth-service-war" target="_blank">/projectdanube/xdi2-connect-auth-service-war</a> - "Authorization Service" for the XDI Connect protocol, packaged as .WAR file
* <a href="https://github.com/projectdanube/xdi2-connect-service-war" target="_blank">/projectdanube/xdi2-connect-service-war</a> - "Connect Service" for the XDI Connect protocol, packaged as .WAR file
* <a href="https://github.com/projectdanube/xdi-grapheditor" target="_blank">/projectdanube/xdi-grapheditor</a> - An XDI Graph Editor
  -Forked from neustar/xdi-grapheditor
* <a href="https://github.com/projectdanube/xdi2-connect-auth-service" target="_blank">/projectdanube/xdi2-connect-auth-service</a> - This is a "Connect Auth Service" component for the XDI Browser binding.




