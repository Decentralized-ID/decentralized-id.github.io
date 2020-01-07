---
date: 2019-03-11
layout: single
title: SSI-DID Github Repositories
description: "A start at listing all DID-SSI related GitHub Repositories."
permalink: /code/github/
canonical_url: 'https://decentralized-id.com/identity-github/'
redirect_from: 
  - github/
  - github
  - identity-github
  - identity-github/
toc_sticky: false
categories: ["Code","Specs-Standards"]
tags: ["ID2020","Danube","W3C","XDI","OASIS","Digital Bazaar","Rebooting WoT","JSON-LD","
Credentials Community Group","RDF","Veres One","Learning Machine"]
last_modified_at: 2019-03-15
---

[![](https://i.imgur.com/rsGOVgt.png)](https://internetidentityworkshop.com/)

## /project-danube

* [projectdanube/indy-sdk-java](https://github.com/projectdanube/indy-sdk-java) - Java binding to the native Indy SDK
* [projectdanube/blockstack-cli-java](https://github.com/projectdanube/blockstack-cli-java) - Java client for Blockstore


### Danube - XDI

>[XDI.org](https://xdi.org) is a non-profit public trust organization whose purpose is to provide public infrastructure for digital identity, security, and privacy using the open standard XDI semantic data interchange protocol developed by the OASIS XDI Technical Committee.
* [projectdanube/xdi-tutorial](https://github.com/projectdanube/xdi-tutorial) - XDI Tutorial
* [projectdanube/XDINinja-swing](https://github.com/projectdanube/XDINinja-swing) - XDI-enabled standalone client application
* [projectdanube/xdi2-tools](https://github.com/projectdanube/xdi2-tools) - XDI2 maintenance and other tools
* [projectdanube/xdi2-connector-personal](https://github.com/projectdanube/xdi2-connector-personal) - A connector plugin for the XDI2 server that maps data from Personal.com to XDI
* [projectdanube/xdi2-docker](https://github.com/projectdanube/xdi2-docker) - Dockerfiles for XDI2
* [projectdanube/xdi2-connect-buttonbuilder](https://github.com/projectdanube/xdi2-connect-buttonbuilder) - "Button Builder" component for the XDI Connect protocol

### Danube - XDI libraries

* [projectdanube/xdi2](https://github.com/projectdanube/xdi2) - XDI2 general purpose library and server
* [projectdanube/xdi-js](https://github.com/projectdanube/xdi-js) - XDI client library for JavaScript
* [projectdanube/xdi2-connect-core](https://github.com/projectdanube/xdi2-connect-core) - Shared library for the XDI Connect protocol


### Danube - XDI - Various Integrations

* [projectdanube/xdi2-bdb](https://github.com/projectdanube/xdi2-bdb) - Support for using BDB as XDI2 backend storage
* [projectdanube/xdi2-mongodb](https://github.com/projectdanube/xdi2-mongodb) - Support for using MongoDB as XDI2 backend storage
* [projectdanube/xdi2-server-heroku](https://github.com/projectdanube/xdi2-server-heroku) - XDI2 Server deployed via Heroku
* [projectdanube/xdi2-redis](https://github.com/projectdanube/xdi2-redis) - Support for using Redis as XDI2 backend storage
* [projectdanube/xdi2-tor](https://github.com/projectdanube/xdi2-tor) - Integration of XDI and Tor
* [projectdanube/xdi2-ipfs](https://github.com/projectdanube/xdi2-ipfs) - Integration of XDI and IPFS
* [projectdanube/withsqlite](https://github.com/projectdanube/withsqlite) - A module for a python dict that back ends on an sqlite3 database. It's bit like shelve but with json and sqlite3.
  - Forked from jvasile/withsqlite

### Danube - XDI Configuration

* [projectdanube/xdi2-selfhosted](https://github.com/projectdanube/xdi2-selfhosted) - A configuration profile of the XDI2 server for self-hosting a single XDI graph.
* [projectdanube/xdi2-csp](https://github.com/projectdanube/xdi2-csp) - A configuration profile of the XDI2 server for hosting a dynamic number of XDI graphs.
* [projectdanube/xdi2-registry](https://github.com/projectdanube/xdi2-registry) - 
A configuration profile of the XDI2 server for hosting a registry of XDI names and XDI numbers.

### Danube - XDI Examples

* [projectdanube/xdi2-example-messaging](https://github.com/projectdanube/xdi2-example-messaging) - XDI2 Examples: Basic messaging functionality.
* [projectdanube/xdi2-example-advanced-server](https://github.com/projectdanube/xdi2-example-advanced-server) - XDI2 Examples: Setting up advanced XDI servers.
* [projectdanube/xdi2-example-core](https://github.com/projectdanube/xdi2-example-core) - XDI2 Examples: Simple uses of the core functionality.
* [projectdanube/xdi2-example-client](https://github.com/projectdanube/xdi2-example-client) - XDI2 Examples: Writing XDI client applications.
* [projectdanube/xdi2-example-secp256k1-server](https://github.com/projectdanube/xdi2-example-secp256k1-server) - Example XDI server using cid-2 cryptographic XDI numbers.
* [projectdanube/xdi2-example-ec25519-server](https://github.com/projectdanube/xdi2-example-ec25519-server) - Example XDI server using cid-1 cryptographic XDI numbers.
* [projectdanube/xdi2-connect-acmenews](https://github.com/projectdanube/xdi2-connect-acmenews) - +acmenews XDI2 demo
* [projectdanube/xdi2-connect-leshop](https://github.com/projectdanube/xdi2-connect-leshop) - +leshop XDI2 demo
* [projectdanube/xdi2-example-secp256k1-client](https://github.com/projectdanube/xdi2-example-secp256k1-client) - Example XDI client using cid-2 cryptographic XDI numbers.
* [projectdanube/xdi2-example-ec25519-client](https://github.com/projectdanube/xdi2-example-ec25519-client) - Example XDI client using cid-1 cryptographic XDI numbers.



### Danube - XDI Plugins

* [projectdanube/xdi2-crypto-secp256k1](https://github.com/projectdanube/xdi2-crypto-secp256k1) - This is an secp256k1 crypto plugin for the XDI2 client and server.
* [projectdanube/xdi2-crypto-ec25519](https://github.com/projectdanube/xdi2-crypto-ec25519) - This is an Ed25519 crypto plugin for the XDI2 client and server.
* [projectdanube/xdi2-connector-facebook](https://github.com/projectdanube/xdi2-connector-facebook) - A connector plugin for the XDI2 server that maps data from Facebook to XDI
* [projectdanube/xdi2-connector-meeco](https://github.com/projectdanube/xdi2-connector-meeco) - A connector plugin for Meeco
* [projectdanube/XDINinja-plugin](https://github.com/projectdanube/XDINinja-plugin) - A browser plugin that is like "Twitter for data"
* [projectdanube/xdi2-connector-cozy](https://github.com/projectdanube/xdi2-connector-cozy) - A connector plugin for CozyCloud
* [projectdanube/xdi2-filesys](https://github.com/projectdanube/xdi2-filesys) - Plugin for an XDI2 server to integrate with a local filesystem

### Danube - Aeternam

* [projectdanube/aeternam-xdi-sncf](https://github.com/projectdanube/aeternam-xdi-sncf) - Aeternam PNR Demo: SNCF
* [projectdanube/aeternam-xdi-db](https://github.com/projectdanube/aeternam-xdi-db) - Aeternam PNR Demo: Deutsche Bahn
* [projectdanube/aeternam-xdi-tests](https://github.com/projectdanube/aeternam-xdi-tests) - XDI experimentation for ÆTERNAM / ÆVATAR
* [projectdanube/aeternam-xdi-maria](https://github.com/projectdanube/aeternam-xdi-maria) - Aeternam PNR Demo: Maria
* [projectdanube/aeternam-xdi-webshop](https://github.com/projectdanube/aeternam-xdi-webshop) - Aeternam PNR Demo: Webshop
* [projectdanube/aeternam-xdi-oebb](https://github.com/projectdanube/aeternam-xdi-oebb) - Aeternam PNR Demo: ÖBB

### Danube - XDI Cloud

* [projectdanube/xdi2-cloudcards](https://github.com/projectdanube/xdi2-cloudcards) - XDI Cloud Card Viewer
* [projectdanube/xdi2-messenger](https://github.com/projectdanube/xdi2-messenger) - XDI Cloud Messenger
* [projectdanube/xdi2-manager](https://github.com/projectdanube/xdi2-manager) - XDI Cloud Manager
* [projectdanube/xdi2-pixel](https://github.com/projectdanube/xdi2-pixel) - Tool to translate a personal cloud policy language (Pixel) to XDI link contracts.

### Danube - XDI Server Deployed Via

* [projectdanube/xdi2-server-grizzly](https://github.com/projectdanube/xdi2-server-grizzly) - XDI2 Server deployed via Grizzly
* [projectdanube/xdi2-server-mina](https://github.com/projectdanube/xdi2-server-mina) - XDI2 Server deployed via Apache MINA
* [projectdanube/xdi2-server-netty](https://github.com/projectdanube/xdi2-server-netty) - XDI2 Server deployed via netty
* [projectdanube/xdi2-server-undertow](https://github.com/projectdanube/xdi2-server-undertow) - XDI2 Server deployed via Undertow
* [projectdanube/xdi2-server-vertx](https://github.com/projectdanube/xdi2-server-vertx) - XDI2 Server deployed via vert.x

### Danube Sevices
* [projectdanube/xdi2-connect-service](https://github.com/projectdanube/xdi2-connect-service) - This is a "Connect Service" component for the XDI Browser binding.
* [projectdanube/neustar-discovery-service](https://github.com/projectdanube/neustar-discovery-service) - Neustar XDI Discovery Service based on XRI Resolution
  - Forked from neustarpc/neustar-discovery-service
* [projectdanube/xdi2-connect-auth-service-war](https://github.com/projectdanube/xdi2-connect-auth-service-war) - "Authorization Service" for the XDI Connect protocol, packaged as .WAR file
* [projectdanube/xdi2-connect-service-war](https://github.com/projectdanube/xdi2-connect-service-war) - "Connect Service" for the XDI Connect protocol, packaged as .WAR file
* [projectdanube/xdi-grapheditor](https://github.com/projectdanube/xdi-grapheditor) - An XDI Graph Editor
  -Forked from neustar/xdi-grapheditor
* [projectdanube/xdi2-connect-auth-service](https://github.com/projectdanube/xdi2-connect-auth-service) - This is a "Connect Auth Service" component for the XDI Browser binding.


## OASIS XDI TC Technical Committee

* [OASIS-XDI-Technical-Committee/xdi-spec-docbook](https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook) - XDI Specifications (Docbook)
* [OASIS-XDI-Technical-Committee/xdi-developers-guide](https://github.com/OASIS-XDI-Technical-Committee/xdi-developers-guide) - XDI Developer's Guide
* [OASIS-XDI-Technical-Committee/xdi-spec-openoffice](https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-openoffice) - XDI Specifications (Open Office)
* [OASIS-XDI-Technical-Committee/xdi-spec-dita](https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-dita) - XDI Specifications (DITA)
* [OASIS-XDI-Technical-Committee/](https://github.com/OASIS-XDI-Technical-Committee/)
* [OASIS-XDI-Technical-Committee/](https://github.com/OASIS-XDI-Technical-Committee/)
* [OASIS-XDI-Technical-Committee/](https://github.com/OASIS-XDI-Technical-Committee/)



## Digital Bazaar

* [digitalbazaar/bedrock](https://github.com/digitalbazaar/bedrock) - Bedrock: A core foundation for rich Web applications.
* [digitalbazaar/forge](https://github.com/digitalbazaar/forge) - A native implementation of TLS in Javascript and tools to write crypto-based and network-heavy webapps 
* [digitalbazaar/veres-delta-docs](https://github.com/digitalbazaar/veres-delta-docs)
* [digitalbazaar/uuid-random](https://github.com/digitalbazaar/uuid-random)


### DB - Identity
* [digitalbazaar/bedrock-angular-identity-composer](https://github.com/digitalbazaar/bedrock-angular-identity-composer) - An bedrock-based AngularJS directive for composing an Identity from a set of credentials
* [digitalbazaar/bedrock-identity-http](https://github.com/digitalbazaar/bedrock-identity-http)
* [digitalbazaar/opencred-idp](https://github.com/digitalbazaar/opencred-idp) - Open Credentials Identity Provider and demo websites
* [digitalbazaar/bedrock-angular-identity](https://github.com/digitalbazaar/bedrock-angular-identity) - Bedrock AngularJS Identity Modules
* [digitalbazaar/bedrock-identity](https://github.com/digitalbazaar/bedrock-identity) - Bedrock identity
* [digitalbazaar/bedrock-idp](https://github.com/digitalbazaar/bedrock-idp) - Bedrock Identity Provider

### DB - Credentials
* [digitalbazaar/vc-data-model](https://github.com/digitalbazaar/vc-data-model) - Verifiable Claims Data Model and Representations specification
  - Forked from w3c/vc-data-model
* [digitalbazaar/vc-test-suite](https://github.com/digitalbazaar/vc-test-suite) - Verifiable Claims WG Test Suite
  - Forked from w3c/vc-test-suite
* [digitalbazaar/vc-js](https://github.com/digitalbazaar/vc-js) - Verifiable Claims JavaScript library
* [digitalbazaar/credentials-io](https://github.com/digitalbazaar/credentials-io) - Library for reading/writing credentials
* [digitalbazaar/bedrock-credentials-rest](https://github.com/digitalbazaar/bedrock-credentials-rest) - A RESTful API for credential storage
* [digitalbazaar/bedrock-credential-vocabs](https://github.com/digitalbazaar/) - Semantic web vocabularies for processing credentials.
* [digitalbazaar/bedrock-address-credential-issuer](https://github.com/digitalbazaar/bedrock-address-credential-issuer) - A module for issuing address credentials
* [digitalbazaar/opencred-verifier](https://github.com/digitalbazaar/opencred-verifier) - Open Credentials Verifier JavaScript API
* [digitalbazaar/opencred-idp](https://github.com/digitalbazaar/opencred-idp) - Open Credentials Identity Provider and demo websites
* [digitalbazaar/bedrock-credential-notifications](https://github.com/digitalbazaar/) - Notification issuing for credentials.
* [digitalbazaar/bedrock-credentials-mongodb](https://github.com/digitalbazaar/bedrock-credentials-mongodb) - Credential storage in mongodb
* [digitalbazaar/bedrock-credentials-context](https://github.com/digitalbazaar/bedrock-credentials-context)
* [digitalbazaar/bedrock-angular-card-displayer](https://github.com/digitalbazaar/bedrock-angular-card-displayer) - Bedrock displayer for card-based credentials
* [digitalbazaar/bedrock-credential-handler](https://github.com/digitalbazaar/bedrock-credential-handler) - Credential Handler for DID-based credentials
* [digitalbazaar/bedrock-web-vc-store](https://github.com/digitalbazaar/bedrock-web-vc-store) - A Javascript library for storing Verifiable Credentials for Bedrock web apps
* [digitalbazaar/web-vc-query-creator](https://github.com/digitalbazaar/web-vc-query-creator) - A Javascript library providing a simplified API for creating Verifiable Credentials queries for web apps.
* [digitalbazaar/bedrock-angular-identity-composer](https://github.com/digitalbazaar/bedrock-angular-identity-composer) - An bedrock-based AngularJS directive for composing an Identity from a set of credentials
* [digitalbazaar/bedrock-web-profile-composer](https://github.com/digitalbazaar/bedrock-web-profile-composer) - A Javascript library for fulfilling Verifiable Credentials queries for Bedrock web apps


### DB - DID
* [digitalbazaar/did-whisper](https://github.com/digitalbazaar/did-whisper) - DID whisper
* [digitalbazaar/did-whisper-server](https://github.com/digitalbazaar/did-whisper-server) - A simple DID Whisper server
* [digitalbazaar/bedrock-web-did-store](https://github.com/digitalbazaar/bedrock-web-did-store) - Enables storage and management of DIDs in a Web App
* [digitalbazaar/bedrock-authn-did](https://github.com/digitalbazaar/bedrock-authn-did)
* [digitalbazaar/did-ssh](https://github.com/digitalbazaar/did-ssh)
bedrock-angular-authn-did
* [digitalbazaar/did-cli](https://github.com/digitalbazaar/did-cli) - A client for managing Decentralized Identifiers
* [digitalbazaar/did-io](https://github.com/digitalbazaar/did-io) - Decentralized identifier management library for browser and node.js
* [digitalbazaar/bedrock-authn-did-jwt](https://github.com/digitalbazaar/bedrock-authn-did-jwt)
* [digitalbazaar/bedrock-did-client](https://github.com/digitalbazaar/bedrock-did-client)
* [digitalbazaar/bedrock-angular-authn-did-jwt](https://github.com/digitalbazaar/bedrock-angular-authn-did-jwt)
* [digitalbazaar/bedrock-credential-handler](https://github.com/digitalbazaar/bedrock-credential-handler) - Credential Handler for DID-based credentials


### DB - Linked Data

* [digitalbazaar/php-json-ld](https://github.com/digitalbazaar/php-json-ld) - PHP implementation of a JSON-LD Processor and API
* [digitalbazaar/pyld](https://github.com/digitalbazaar/pyld) - JSON-LD processor written in Python
* [digitalbazaar/jsonld.js](https://github.com/digitalbazaar/) - A JSON-LD Processor and API implementation in JavaScript
* [digitalbazaar/jsonld-signatures](https://github.com/digitalbazaar/jsonld-signatures) - An implementation of the Linked Data Signatures specification for JSON-LD. Works in the browser and node.js.
* [digitalbazaar/json-ld](https://github.com/digitalbazaar/json-ld) - A Context-based JSON Serialization for Linked Data
* [digitalbazaar/ocapld.js](https://github.com/digitalbazaar/ocapld.js) - Linked Data Capabilities reference implementation
* [digitalbazaar/cuckoo-ldp](https://github.com/digitalbazaar/cuckoo-ldp) - Cuckoo Cycle Based Linked Data Proofs
* [digitalbazaar/bedrock-ldn-receiver](https://github.com/digitalbazaar/bedrock-ldn-receiver) - Bedrock module for Linked Data Notification Receiver
* [digitalbazaar/bedrock-ldn-inbox](https://github.com/digitalbazaar/bedrock-ldn-inbox) - Bedrock module for Linked Data Notification Inboxes
* [digitalbazaar/bedrock-angular-ldn](https://github.com/digitalbazaar/bedrock-angular-ldn) - Bedrock AngularJS module for Linked Data Notification Sender+Consumer
* [digitalbazaar/flex-ledger](https://github.com/digitalbazaar/flex-ledger) - Forked from web-payments/flex-ledger
A decentralized Linked Data Ledger for the Web

## JSON-LD Public Repositories 


* [json-ld/json-ld.org](https://github.com/json-ld/json-ld.org) - JSON for Linked Data
* [json-ld/json-ld-patch](https://github.com/json-ld/json-ld-patch) - JSON-LD Patch
* [json-ld/minutes](https://github.com/json-ld/minutes) - Teleconference minutes - text and audio logs
* [json-ld/normalization](https://github.com/json-ld/normalization) - RDF Dataset Normalization
* [json-ld/tests](https://github.com/json-ld/tests) Archived - [READ-ONLY] Subtree split of the JSON-LD tests – obsolete, please see WG test suites
* [json-ld/scrawl.js](https://github.com/json-ld/scrawl.js)
Scribe tool used by the JSON-LD Community Group
* [json-ld/Charter](https://github.com/json-ld/Charter)
Charter for JSON-LD WG



## /WebOfTrustInfo

>The Web of Trust is a buzzword for a new model of decentralized self-sovereign identity. It’s a phrase that dates back almost twenty-five years, the classic definition derives from PGP.

\#RebootingWebOfTrust holds bi-annual design workshops where many of the ideas in SSI\DID were formed.

In advance of each workshop, all participants produce a one-or-two page topic paper on either:

* A specific problem that they wanted to solve with a web-of-trust solution, and why current solutions (PGP or CA-based PKI) can't address the problem?
*  A specific solution related to the web-of-trust that you'd like others to use or contribute to?

The workshop itself also produces technical whitepapers, this Repository holds a record of the progression of thought in SSI, since November, 2015.

* [One Page List of Rebooting WoT Literature](/literature/rebooting-web-of-trust/) 
* [WebOfTrustInfo/self-sovereign-identity](https://github.com/WebOfTrustInfo/self-sovereign-identity) - Articles and documents associated with designing and implementing identity technology using self-sovereign identity principles
* [WebOfTrustInfo/website](https://github.com/WebOfTrustInfo/website) - Website for http://www.WebOfTrust.info
* [WebOfTrustInfo/community-resilience](https://github.com/WebOfTrustInfo/community-resilience) - Rebooting Web of Trust Community Resilience Team
* [WebOfTrustInfo/satyrn](https://github.com/WebOfTrustInfo/satyrn) - A Markdown-based JavaScript Sandbox
* [WebOfTrustInfo/sss](https://github.com/WebOfTrustInfo/sss) - Library for the Shamir secret sharing scheme
  - Forked from dsprenkels/sss
* [WebOfTrustInfo/verifiable-news](https://github.com/WebOfTrustInfo/verifiable-news) - TBD: W3C Credentials Community Group repository for curbing "social bots" and mitigating the spread of online misinformation and "fake news".
* [WebOfTrustInfo/portable-reputation-toolkit](https://github.com/WebOfTrustInfo/portable-reputation-toolkit)

### RWoT Design Workshop

* [White Papers, Specifications & Proofs of Concept](https://github.com/WebOfTrustInfo/rwot1-sf/blob/master/topics-and-advance-readings/white-papers--specifications---and-proof-of-concept-code.md) 
  >Our goal for this initial #RebootingWebOfTrust design workshop is to:
  >
  > * Focus on the creation of the next generation of decentralized web-of-trust based identity systems.
  > * To generate 5 technical white papers on topics decided by the group that will have the greatest impact on the future"
  >
  > To this end, I thought it would be useful to define what is a white paper, and as some people desire to go beyond this, what is a specification and proof of concept code.
* [WebOfTrustInfo/rwot1-sf](https://github.com/WebOfTrustInfo/rwot1-sf) - RWOT1 in San Francisco, California (November 2015)
* [WebOfTrustInfo/rwot2-id2020](https://github.com/WebOfTrustInfo/rwot2-id2020) - RWOT2 for the ID2020 UN Summit (May 2016)
* [WebOfTrustInfo/rwot3-sf](https://github.com/WebOfTrustInfo/rwot3-sf) - RWOT3 in San Francisco, California (October 2016)
* [WebOfTrustInfo/rwot4-paris](https://github.com/WebOfTrustInfo/rwot4-paris) - RWOT4 in Paris, France (April 2017)
* [WebOfTrustInfo/rwot5-boston](https://github.com/WebOfTrustInfo/rwot5-boston) - RWOT5 in Boston, Massachusetts (October 2017)
* [WebOfTrustInfo/rwot6-santabarbara](https://github.com/WebOfTrustInfo/rwot6-santabarbara) - RWOT6 in Santa Barbara, California (March 2018)
* [WebOfTrustInfo/rwot7-toronto](https://github.com/WebOfTrustInfo/rwot7-toronto) - RWOT7 in Toronto, Canada (September 2018)
* [WebOfTrustInfo/rwot8-barcelona](https://github.com/WebOfTrustInfo/rwot8-barcelona) - RWOT8 in Barcelona, Spain (March 2019)

### RWot BTCR

* [WebOfTrustInfo/btcr-tx-playground.github.io](https://github.com/WebOfTrustInfo/btcr-tx-playground.github.io)
* [WebOfTrustInfo/btcr-did-tools-js](https://github.com/WebOfTrustInfo/btcr-did-tools-js)
* [WebOfTrustInfo/btcr-hackathon](https://github.com/WebOfTrustInfo/btcr-hackathon) - Virtual hackathon to create spec and code for Bitcoin-based Decentralized Identifiers (DIDs)

### RWoT Txref Conversion

* [WebOfTrustInfo/txref-conversion-java](https://github.com/WebOfTrustInfo/txref-conversion-java) - Java library for converting txids to txrefs and back
* [WebOfTrustInfo/txref-conversion-js](https://github.com/WebOfTrustInfo/txref-conversion-js) - Javascript library for converting txids to txrefs and back
* [WebOfTrustInfo/txref-conversion-python](https://github.com/WebOfTrustInfo/txref-conversion-python) - Python library to handle conversion between TxRef(bech32) <-> TxID

### RWoT Linked Data

* [WebOfTrustInfo/schemas](https://github.com/WebOfTrustInfo/) - Draft schemas for JSON-LD etc.
* [WebOfTrustInfo/ld-signatures-java](https://github.com/WebOfTrustInfo/ld-signatures-java) - Java implementation of Linked Data Signatures
* [WebOfTrustInfo/ld-signatures-python](https://github.com/WebOfTrustInfo/ld-signatures-python) - JSON-LD Signatures with JSON Web Signatures


## /w3c - World Wide Web Consortium

### /w3c/verifiable-claims  - VC Working Group

[Verifiable Claims WG - Mailing List](https://lists.w3.org/Archives/Public/public-vc-wg/) (and archives)

* [w3c/verifiable-claims](https://github.com/w3c/verifiable-claims) - W3C Verifiable Claims Working Group.
* [w3c/vc-data-model](https://github.com/w3c/vc-data-model) -Verifiable Claims Data Model and Representations specification.
* [w3c/vc-use-cases](https://github.com/w3c/vc-use-cases) - Verifiable Claims Use Cases.
* [w3c/vc-test-suite](https://github.com/w3c/vc-test-suite) - Verifiable Claims WG Test Suite.
* [w3c/vc-imp-guide](https://github.com/w3c/vc-imp-guide) - Verifiable Credentials Implementation Guidelines

### /w3c-ccg - Credentials Community Group

[Public mailing list for the Credentials Community Group](http://lists.w3.org/Archives/Public/public-credentials/) (and archives) - Anyone may read or write to this list.
  * [w3c-ccg/meetings](https://github.com/w3c-ccg/meetings) CCG Meeting Transcripts
* [w3c-ccg/community](https://github.com/w3c-ccg/community) - CCG Community Repo
* [w3c-ccg/announcements](https://github.com/w3c-ccg/announcements) - CCG Announcements
* [w3c-ccg/w3c-ccg-process](https://github.com/w3c-ccg/w3c-ccg-process)
* [w3c-ccg/registries-process](https://github.com/w3c-ccg/registries-process)

#### CCG - DID

* [w3c-ccg/did-primer](https://github.com/w3c-ccg/did-primer) - A Primer for Decentralized Identifiers
* [w3c-ccg/did-spec](https://github.com/w3c-ccg/did-spec) - Decentralized Identifier (DID) 1.0 Specification - Data Model and Syntax
* [w3c-ccg/did-resolution](https://github.com/w3c-ccg/did-resolution) Spec 1.0
* [w3c-ccg/did-use-cases](https://github.com/w3c-ccg/did-use-cases)
* [w3c-ccg/did-method-registry](https://github.com/w3c-ccg/did-method-registry) - a list of all known DID Methods and their current level of maturity.
  * [w3c-ccg/didm-btcr](https://github.com/w3c-ccg/didm-btcr) - WORK ITEM: BTCR DID Method Spec
  * [w3c-ccg/didm-veres-one](https://github.com/w3c-ccg/didm-veres-one) - Veres One Decentralized Identifier Method Specification
* [w3c-ccg/did-wg-proposal](https://github.com/w3c-ccg/did-wg-proposal) - Proposal to W3C membership for a DID Working Group.
  * [w3c-ccg/did-wg-charter](https://github.com/w3c-ccg/did-wg-charter) - EXPERIMENTAL charter for the W3C Decentralized Identifier Working Group 
* [w3c-ccg/did-hackathon-2018](https://github.com/w3c-ccg/did-hackathon-2018)
* [w3c-ccg/data-minimization](https://github.com/w3c-ccg/data-minimization) - Data Minimization, Selective Disclosure, and Progressive Trust
* [w3c-ccg/credential-handler-api](https://github.com/w3c-ccg/credential-handler-api)
* [w3c-ccg/amira](https://github.com/w3c-ccg/amira) - Amira Engagement Model.
* [w3c-ccg/functional-identity](https://github.com/w3c-ccg/functional-identity)

#### CCG - Verifiable Credentials

* [](https://github.com/w3c-ccg/vc-status-registry) - REGISTRY: The Verifiable Credentials Status Scheme Registry.
* [w3c-ccg/edu_occ_verifiable_credentials](https://github.com/w3c-ccg/edu_occ_verifiable_credentials) - WORK ITEM: Drafts and Ideas of Educational and Occupational Verifiable Credentials.
* [w3c-ccg/vc-examples](https://github.com/w3c-ccg/vc-examples) - WORK ITEM: Verifiable Credentials Examples

#### CCG -  Linked Data
* [w3c-ccg/ocap-ld](https://github.com/w3c-ccg/ocap-ld) - WORK ITEM: Linked Data Object Capabilities specification
* [w3c-ccg/ld-cryptosuite-registry](https://github.com/w3c-ccg/ld-cryptosuite-registry) - REGISTRY: Linked Data Keys Registry

### Digital Verification Community Group
> The mission of the W3C Digital Verification Community Group is to study, design, promote, and deploy systems that increase trust on the Web.

* [w3c-dvcg/w3c-dvcg.github.io](https://sea-region.github.com/w3c-dvcg/w3c-dvcg.github.io) - Landing site for W3C Digital Verification Community Group.
* [w3c-dvcg/multibase](https://sea-region.github.com/w3c-dvcg/multibase) - 
An IETF Internet Draft for the Multibase data format
* [w3c-dvcg/hashlink](https://sea-region.github.com/w3c-dvcg/hashlink) - An IETF Internet Draft for the Hashlink data format
* [w3c-dvcg/multihash](https://sea-region.github.com/w3c-dvcg/multihash) - An IETF Internet Draft for the Multihash data format
* [w3c-dvcg/security-vocab](https://sea-region.github.com/w3c-dvcg/security-vocab) - The Linked Data Security Vocabulary
* [w3c-dvcg/lds-rsa2018](https://sea-region.github.com/w3c-dvcg/lds-rsa2018) - 
Linked Data Signature Suite created in 2018
* [w3c-dvcg/http-signatures](https://sea-region.github.com/w3c-dvcg/http-signatures) - Signing HTTP Messages specification
* [w3c-dvcg/ld-proofs](https://sea-region.github.com/w3c-dvcg/ld-proofs) - 
Linked Data Proofs Specification
* [w3c-dvcg/ld-signatures](https://sea-region.github.com/w3c-dvcg/ld-signatures) - Linked Data Signatures enable digital signatures on Linked Data
* [w3c-dvcg/lds-ed25519-2018](https://sea-region.github.com/w3c-dvcg/lds-ed25519-2018) - Linked Data Signature Suite for Ed25519 2018
* [w3c-dvcg/lds-merkleproof2017](https://sea-region.github.com/w3c-dvcg/lds-merkleproof2017) - 2017 Signature suite for doing Merkle Proofs.
* [w3c-dvcg/lds-redaction2016](https://sea-region.github.com/w3c-dvcg/lds-redaction2016) - Linked Data Signature Suite created in 2016 for performing Redacted 
* [w3c-dvcg/http-signatures-audit](https://sea-region.github.com/w3c-dvcg/http-signatures-audit) - Security considerations for HTTP Signatures specification.
* [w3c-dvcg/lds-koblitz2016](https://sea-region.github.com/w3c-dvcg/lds-koblitz2016) - Linked Data Signature Suite for the Koblitz Elliptic Curve 2016
* [w3c-dvcg/lds-pseudonymous2016/](https://sea-region.github.com/w3c-dvcg/lds-pseudonymous2016/)
* [w3c-dvcg/lds-rsa2016/](https://sea-region.github.com/w3c-dvcg/lds-rsa2016/)

### /opencreds

* [opencreds/website](https://github.com/opencreds/website) - The Open Credentials Website
* [opencreds/minutes](https://github.com/opencreds/minutes) - 
Text and audio meeting minutes for W3C Credentials Community Group


## Spidchain

* [Spidchain.com](http://www.spidchain.com/) -Blockchain for Self Sovereign Identity

### Spid Bitcoin
* [SpidChain/spidchain-btcr](https://github.com/SpidChain/spidchain-btcr) - An implementation of the btcr standard for self sovereign distributed digital identity
* [SpidChain/electrumx](https://github.com/SpidChain/electrumx) Forked from kyuupichan/electrumx
  - Alternative implementation of spesmilo/electrum-server
* [SpidChain/btcr-spv](https://github.com/SpidChain/btcr-spv) - Poc of an SPV implementation of BTCR
* [SpidChain/satoshis-wheel-of-fortune](https://github.com/SpidChain/satoshis-wheel-of-fortune) - Pick a name from a list randomly in a provably honest way
* [SpidChain/txref-conversion-js](https://github.com/SpidChain/txref-conversion-js) - Forked from WebOfTrustInfo/txref-conversion-js
  - Javascript library for converting txids to txrefs and back


### Spid Ethereum
* [SpidChain/eth-lightwallet](https://github.com/SpidChain/eth-lightwallet) - Forked from ConsenSys/eth-lightwallet
  - Lightweight JS Wallet for Node and the browser
* [SpidChain/truffle](https://github.com/SpidChain/truffle) - Forked from trufflesuite/truffle
  - A development framework for Ethereum
* [SpidChain/VotingSystem](https://github.com/SpidChain/VotingSystem) - A dapp, library and smart contract to notarize votes on the ethereum blockchain
* [SpidChain/ethers-wallet](https://github.com/SpidChain/ethers-wallet) - Forked from ethers-io/ethers.js
  - Complete Ethereum wallet implementation and library in JavaScript.
* [SpidChain/nodejs-ethereum](https://github.com/SpidChain/nodejs-ethereum) - Forked from b9lab/nodejs-ethereum
Example of using NodeJs with Ethereum

### Spid Hackathon
* [SpidChain/chainpass](https://github.com/SpidChain/chainpass) - App for Trenitalia hackathon - 09 / 16 / 2017 - Rome
* [SpidChain/vipPrice](https://github.com/SpidChain/vipPrice) - #internationalhackathon #spidchain

### Democracy Earth

* [democracyearth/self](https://github.com/democracyearth/self) - Cryptgraphic peer authentication.
  >We keep the identity 100% in the hands of the user. We took the decentralization approach to create a login protocol and Cryptography (SHA-256 hash function) to ensure security and identity. We allow users to show the information that they want, when they want and to they want.
* [democracyearth/sovereign](https://github.com/democracyearth/sovereign) - earth_americas Blockchain democracy.
* [democracyearth/paper](https://github.com/democracyearth/paper) - On decentralized digital democracy.
* [democracyearth/community.](https://github.com/democracyearth/community.) - earth_americas Be an Ambassador or Student Ambassador anywhere in the world.
* [democracyearth/vote](https://github.com/democracyearth/vote) - Smart contracts for vote token.
* [democracyearth/dapp](https://github.com/democracyearth/dapp) - Liquid democracy smart contract implementation
* [democracyearth/blockchain](https://github.com/democracyearth/blockchain) - A block chain for democracy.
* [democracyearth/handbook](https://github.com/democracyearth/handbook) - Forked from loomio/loomio-coop-handbook
  - Handbook for Democracy Earth Foundation
* [democracyearth/press-kit](https://github.com/democracyearth/press-kit) - A set of resources about the Democracy Earth Foundation to share with journalists and media.
* [democracyearth/exodus](https://github.com/democracyearth/exodus) - Smart contracts enabling a Universal Basic Income for self-sovereign citizens earth_americas
* [democracyearth/party](https://github.com/democracyearth/party) -  horse Trojan political party.
* [democracyearth/balance-keeper](https://github.com/democracyearth/balance-keeper) - token balance keeper daemon.
* [democracyearth/dapp](https://github.com/democracyearth/dapp) - Liquid democracy smart contract implementation
* [democracyearth/DesignSystem](https://github.com/democracyearth/DesignSystem)
* [democracyearth/vzla-propone-cambio](https://github.com/democracyearth/vzla-propone-cambio) - venezuelaVenezuela sera libre
* [democracyearth/advocacy](https://github.com/democracyearth/advocacy) - Toolkit with static and live documents that will concentrate relevant information aimed at advocacy efforts for liquid democracy around the world.
* [democracyearth/protocol](https://github.com/democracyearth/protocol) - Forked from arikan/bitcoin-voting
  - bulb Cryptocurrency voting schema.
* [democracyearth/dips](https://github.com/democracyearth/dips) - Democracy Improvement Proposals
* [democracyearth/micropayment-voting](https://github.com/democracyearth/micropayment-voting) - eagle Vote as bitcoin micropayment.
* [democracyearth/concept](https://github.com/democracyearth/concept) - Forked from makingdevs/mecate-democra



## Ethereum
* [ERC: Lightweight Identity #1056](https://github.com/ethereum/EIPs/issues/1056) —This ERC describes a standard for creating and updating identities with a limited use of blockchain resources. An identity can have an unlimited number of delegates and attributes associated with it. Identity creation is as simple as creating a regular key pair ethereum account, which means that it's fee (no gas costs) and all ethereum accounts are valid identities. Furthermore this ERC is fully DID compliant.
* [ERC-1484: Digital Identity Aggregator #1495](https://github.com/ethereum/EIPs/issues/1495) —A protocol for aggregating digital identity information that's broadly interoperable with existing, proposed, and hypothetical future digital identity standards.
* [ERC725](https://github.com/ethereum/EIPs/issues/725) 
  * The following describes standard functions for a unique identifiable proxy account to be used by humans, groups, organisations, objects and machines
* [ERC735](https://github.com/ethereum/EIPs/issues/735) -  The following describes standard functions for adding, removing and holding of claims.
  - These claims can attested from third parties (issuers) or self attested.
* [EIP712](https://github.com/ethereum/EIPs/blob/f29527ab39357548b06b29e937a48f06ae099de7/EIPS/eip-712.md) - This is a standard for hashing and signing of typed structured data
* [ERC: Ethereum Claims Registry #780](https://github.com/ethereum/EIPs/issues/780)
* [EIP-1078](https://github.com/ethereum/EIPs/blob/ed621645c8f3bc5756492f327cda015f35d9f8da/EIPS/eip-1078.md) - 
This presents a method to replace the usual signup/login design pattern with a minimal ethereum native scheme, that doesn’t require passwords, backing up private keys nor typing seed phrases. 

### Assorted Ethereum Apps

[XLNT/meirl](https://github.com/XLNT/meirl) - Counterfactual and Upgradable Self-Sovereign Identity for Ethereum, using Gnosis Safe



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

## Cryptonomica

[![](https://i.imgur.com/moVyrrt.png)](https://cryptonomica.github.io)

* [Cryptonomica/cryptonomica](https://github.com/Cryptonomica/cryptonomica) - Cryptonomica keys server
* [Cryptonomica/cryptonomica.github.io](https://github.com/Cryptonomica/cryptonomica.github.io) - Cryptonomica frontend
* [Cryptonomica/arbitration-rules](https://github.com/Cryptonomica/arbitration-rules) - Cryptonomica Arbitration Rules
* [Cryptonomica/dappathon-tlv](https://github.com/Cryptonomica/dappathon-tlv)
* [Cryptonomica/Ethereum-IdentityVerification](https://github.com/Cryptonomica/Ethereum-IdentityVerification) - Indentity verification and KYC for Ethereum blockchain
* [Cryptonomica/ethnode.cryptonomica.net](https://github.com/Cryptonomica/ethnode.cryptonomica.net) - Ethereum node with API on nodejs and web3.js
* [Cryptonomica/Ethereum-IdentityProof](https://github.com/Cryptonomica/Ethereum-IdentityProof) - Smart contract for Ethereum's account owner verification using Cryptonomica.net
* [Cryptonomica/international-arbitration-law](https://github.com/Cryptonomica/international-arbitration-law) - Repository for collecting information about international arbitration law and practice



## Learning Machine

* [learningmachine/stage.blockcerts.github.io](https://github.com/learningmachine/stage.blockcerts.github.io) - Web site 
  - Forked from blockchain-certificates/blockchain-certificates.github.io
* [learningmachine/polymer-redux](https://github.com/learningmachine/polymer-redux) - An example use-case to showcase the state/view abstraction in Polymer 3, LitElement and Redux context
* [learningmachine/ajv](https://github.com/learningmachine/ajv) -The fastest JSON-Schema Validator. Supports draft-06
  - Forked from epoberezkin/ajv
* [learningmachine/Foundatio](https://github.com/learningmachine/Foundatio) - Pluggable foundation blocks for building distributed apps.
  - Forked from FoundatioFx/Foundatio

### Blockcerts

* [blockchain-certificates/blockcerts-verifier](https://github.com/blockchain-certificates/blockcerts-verifier) - A Blockcerts verifier and viewer
* [blockchain-certificates/cert-issuer](https://github.com/blockchain-certificates/cert-issuer) - Issues Blockcerts using either the Bitcoin or Ethereum blockchain
* [blockchain-certificates/cert-verifier](https://github.com/blockchain-certificates/cert-verifier) - Python library for verifying Blockcerts
* [blockchain-certificates/cert-schema](https://github.com/blockchain-certificates/cert-schema) - The schema for Blockcerts
  - Forked from IMSGlobal/cert-schema
* [blockchain-certificates/assets](https://github.com/blockchain-certificates/assets)
* [blockchain-certificates/cert-verifier-js](https://github.com/blockchain-certificates/cert-verifier-js) - Javascript library for verifying Blockcerts Certificates
* [blockchain-certificates/cert-tools](https://github.com/blockchain-certificates/cert-tools) -Command line tools for designing certificate templates and instantiating a certificate batch
* [blockchain-certificates/obi-baking](https://github.com/blockchain-certificates/obi-baking) - Example of baking a blockcert into an Open Badge
* [blockchain-certificates/cert-core](https://github.com/blockchain-certificates/cert-core)
* [blockchain-certificates/wallet-test-resources](https://github.com/blockchain-certificates/wallet-test-resources) - These are resources used to test implementations of the evolving blockcerts certificate standard and issuer conventions.
* [blockchain-certificates/pyld](https://github.com/blockchain-certificates/pyld) - JSON-LD processor written in Python
  - Forked from digitalbazaar/pyld
* [blockchain-certificates/archived-cert-store](https://github.com/blockchain-certificates/archived-cert-store) - Storage library and service for Blockchain Certificates
* [blockchain-certificates/openbadges-validator-core](https://github.com/blockchain-certificates/openbadges-validator-core) - Open Badges validation in python 
  - Forked from IMSGlobal/openbadges-validator-core
* [blockchain-certificates/PodSpecs](https://github.com/blockchain-certificates/PodSpecs) - A listing of CocoaPod .podspec files for all pods created in the Blockchain Certificates project.
* [blockchain-certificates/openbadges-bakery](https://github.com/blockchain-certificates/openbadges-bakery) - An OpenBadges image baking library that works with PNGs and SVGs
  - Forked from mozilla/openbadges-bakery

#### Blockcerts Json
* [blockchain-certificates/JSONLD](https://github.com/blockchain-certificates/JSONLD) - An iOS framework for processing JSON-LD files.
* [blockchain-certificates/JSONLDProcessor](https://github.com/blockchain-certificates/JSONLDProcessor) - An iOS framework for processing JSON-LD files.


#### Blockcerts Web

* [blockchain-certificates/cert-viewer](https://github.com/blockchain-certificates/cert-viewer) - A web app for viewing and validating Blockchain Certificates
* [blockchain-certificates/blockcerts-playground.github.io](https://github.com/blockchain-certificates/blockcerts-playground.github.io) - In-browser tool to experiment with Blockcerts
* [blockchain-certificates/blockchain-certificates.github.io](https://github.com/blockchain-certificates/blockchain-certificates.github.io) 
  - Forked from mmistakes/minimal-mistakes
* [blockchain-certificates/cert-web-component](https://github.com/blockchain-certificates/cert-web-component) - A web component for displaying blockchain certificates.

#### Blockcerts Mobile

* [blockchain-certificates/wallet-android](https://github.com/blockchain-certificates/wallet-android) - An Android app for Blockcerts
* [blockchain-certificates/BlockcertsFramework-iOS](https://github.com/blockchain-certificates/BlockcertsFramework-iOS) - An iOS wallet for viewing, validating, and sharing certs
* [blockchain-certificates/wallet-iOS](https://github.com/blockchain-certificates/wallet-iOS) - An iOS wallet for Blockcerts


## Sovrin Foundation

* [sovrin-foundation/sovrin.org](https://github.com/sovrin-foundation/sovrin.org) - the foundation web site
* [sovrin-foundation/sovrin](https://github.com/sovrin-foundation/sovrin)
* [sovrin-foundation/sovrin-sip](https://github.com/sovrin-foundation/sovrin-sip) - controlled techical docs/standards for Sovrin Foundation
* [sovrin-foundation/sov-docs-conf](https://github.com/sovrin-foundation/sov-docs-conf) - A repository containing the code that builds the Sovrin documentation website's shared repository sidebar
* [sovrin-foundation/ssi-protocol](https://github.com/sovrin-foundation/ssi-protocol) - Document the interactions and conventions that make self-sovereign identity interoperable.
* [sovrin-foundation/protocol](https://github.com/sovrin-foundation/protocol) 
* [sovrin-foundation/steward-tools](https://github.com/sovrin-foundation/steward-tools) - tools for Sovrin steward
* [sovrin-foundation/token-plugin](https://github.com/sovrin-foundation/token-plugin) - source code and tests for Sovrin Ledger plugins
* [sovrin-foundation/sovrin-test-automation](https://github.com/sovrin-foundation/sovrin-test-automation) - quality assurance automation for Sovrin repos.
* [sovrin-foundation/agent-sdk](https://github.com/sovrin-foundation/agent-sdk) - Reference Agent
* [sovrin-foundation/sovrin-connector-preview](https://github.com/sovrin-foundation/sovrin-connector-preview) - Forked from evernym/sovrin-connector-preview
* [sovrin-foundation/pipeline-test](https://github.com/sovrin-foundation/pipeline-test) - Test integrations, hooks and build pipelines.


### Sovrin - Indy
* [sovrin-foundation/indy-dev</a> - Forked from michaeldboyd/indy-dev](https://github.com/sovrin-foundation/indy-dev) - This is a quick way to setup a development environment to experiment with IndySDK
* [sovrin-foundation/libsovtoken](https://github.com/sovrin-foundation/libsovtoken) - This is a payment handler library to work with libindy. It may one day be merged into libindy.
* [sovrin-foundation/sovrin-indy-android-dependencies](https://github.com/sovrin-foundation/sovrin-indy-android-dependencies) - indy-android-dependencies
* [sovrin-foundation/connector-app](https://github.com/sovrin-foundation/connector-app) - Reference mobile edge agent for use with the Sovrin Network built from Hyperledger Indy.
* [sovrin-foundation/indy-android-dependencies](https://github.com/sovrin-foundation/indy-android-dependencies) - Dependencies required to build indy-sdk


## /decentralized-identity - DIF

* [decentralized-identity/decentralized-identity.github.io](https://github.com/decentralized-identity/decentralized-identity.github.io)  - Site for the open source, community-driven group of dev and organizations working toward an interoperable, decentralized identity ecosystem
* [decentralized-identity/org](https://github.com/decentralized-identity/org) - DIF docs, wiki, and organizational material
* [decentralized-identity/credential-manifest](https://github.com/decentralized-identity/credential-manifest) - Format that normalizes the definition of requirements for the issuance of a credential
* [decentralized-identity/universal-registrar](https://github.com/decentralized-identity/universal-registrar) - Specifications and implementation of a universal identifier registrar
* [decentralized-identity/attestations](https://github.com/decentralized-identity/attestations) - Attestation API implementations for various languages and platforms.

### DIF - DID
* [decentralized-identity/did-methods](https://github.com/decentralized-identity/did-methods) - DID Method specs, docs, and materials
* <a href="https://github.com/decentralized-identity/did-common-typescript" />/decentralized-identity/did-common-typescript
</a> - A common bundle of shared code and modules for working with DIDs, DID Documents, and other DID-related activities
* [decentralized-identity/did-security-csharp](https://github.com/decentralized-identity/did-security-csharp) - C# implementation of DID security and privacy controls
* [decentralized-identity/did-security-typescript](https://github.com/decentralized-identity/did-security-typescript) - Typescript implementation of DID security and privacy controls
* [decentralized-identity/did-common-java](https://github.com/decentralized-identity/did-common-java) - Shared DID Java library.
* [decentralized-identity/ua-web-extension](https://github.com/decentralized-identity/ua-web-extension) - Basic web extension version of a DID User Agent
* [decentralized-identity/did-recovery](https://github.com/decentralized-identity/did-recovery) - Various methods for DID recovery
* [decentralized-identity/web-polyfills](https://github.com/decentralized-identity/web-polyfills) - Polyfills for proposed or emerging DID-centric Web APIs
* [decentralized-identity/](https://github.com/decentralized-identity/)
* [decentralized-identity/http-did-auth-proxy](https://github.com/decentralized-identity/http-did-auth-proxy) - Forked from bcgov/http-did-auth-proxy
DID Auth HTTP proxy.

### DIF - DID-Auth
* [decentralized-identity/did-auth-jose](https://github.com/decentralized-identity/did-auth-jose) - JOSE-based implementation of DID Authenticated Encryption

### DIF - Sidetree
* [decentralized-identity/sidetree-ipfs](https://github.com/decentralized-identity/sidetree-ipfs) - IPFS module for storing and accessing Sidetree entity operation data via content addressable storage
* [decentralized-identity/sidetree-core](https://github.com/decentralized-identity/sidetree-core) - The blockchain-agnostic server implementation of the Sidetree protocol.
* [decentralized-identity/sidetree-bitcoin](https://github.com/decentralized-identity/sidetree-bitcoin) - Blockchain-specific code for the Sidetree-based DID Method implementation on Bitcoin
* [decentralized-identity/ion](https://github.com/decentralized-identity/ion) - DID Method implementation using the Sidetree protocol on top of Bitcoin

### DIF - Hub
* [decentralized-identity/hub-sdk-js-sample](https://github.com/decentralized-identity/hub-sdk-js-sample) - Sample app demonstrating use of the DIF Identity Hub JavaScript SDK.
* [decentralized-identity/hub-sdk-js](https://github.com/decentralized-identity/hub-sdk-js) - JavaScript SDK for interacting with Identity Hubs
* [decentralized-identity/hub-common-js](https://github.com/decentralized-identity/hub-common-js) - Common interfaces for working with Identity Hubs in JavaScript/TypeScript
* [decentralized-identity/hub-node-core](https://github.com/decentralized-identity/hub-node-core) - Node.js implementation of the Identity Hub interfaces, business logic, and replication protocol.
* [decentralized-identity/identity-hub](https://github.com/decentralized-identity/identity-hub) - Storage and compute nodes for decentralized identity data and interactions
* [decentralized-identity/hub-node-reference](https://github.com/decentralized-identity/hub-node-reference) - The official Identity Hub reference implementation bundle for Node.js

### DIF - Uniresolver

* [decentralized-identity/universal-resolver](https://github.com/decentralized-identity/universal-resolver) - Universal Resolver implementation and drivers.
* [decentralized-identity/universal-resolver-frontend](https://github.com/decentralized-identity/universal-resolver-frontend) - Frontend web UI for Universal Resolver
* [decentralized-identity/universal-resolver-python](https://github.com/decentralized-identity/universal-resolver-python)
* [decentralized-identity/universal-resolver-java](https://github.com/decentralized-identity/universal-resolver-java)

## Veres One

* [veres-one/veres-one](https://github.com/veres-one/veres-one) - A ledger for acquiring and managing decentralized identifiers
* [veres-one/did-veres-one](https://github.com/veres-one/did-veres-one) - A Decentralized Identifier utility library for Veres One
* [veres-one/veres-one-validator](https://github.com/veres-one/veres-one-validator) - A ledger validator that accepts either signatures or proof of work
* [veres-one/veres-one-context](https://github.com/veres-one/veres-one-context)
* [veres-one/veres-one-consensus-continuity-elector-selection](https://github.com/veres-one/veres-one-consensus-continuity-elector-selection)
* [veres-one/did-client-veres-one](https://github.com/veres-one/did-client-veres-one) - DID client APIs for Veres One
* [veres-one/docs.veres.one](https://github.com/veres-one/docs.veres.one) - Documentation for the Veres One Project
* [veres-one/status.testnet.veres.one](https://github.com/veres-one/status.testnet.veres.one) - Testnet status dashboard website
* [veres-one/veres-one-project](https://github.com/veres-one/veres-one-project)



## /hyperledger Indy
* [indy-plenum](https://github.com/hyperledger/indy-plenum) - Byzantine Fault Tolerant Protocol [[**wiki**](https://github.com/hyperledger/indy-plenum/wiki)]
    > "Byzantine fault tolerance is a sub-field of fault tolerance research inspired by the Byzantine Generals' Problem, which is a generalized version of the Two Generals' Problem." 
    * [Storage components](https://github.com/hyperledger/indy-plenum/blob/master/docs/storage.md) - As of now, RocksDB is used as a key-value database for all Storages.
* [indy-sdk](https://github.com/hyperledger/indy-sdk) - Everything needed to build applications that interact with an Indy distributed identity ledger.
  * [MAINTAINERS.md](https://github.com/hyperledger/indy-sdk/blob/master/MAINTAINERS.md)
* [indy-node](https://github.com/hyperledger/indy-node) - The server portion of a distributed ledger purpose-built for decentralized identity.
* [indy-anoncreds](https://github.com/hyperledger/indy-anoncreds) - Anonymous credentials protocol implementation in python
* [indy-agent](https://github.com/hyperledger/indy-agent) - reference agents and associated tools.
* [indy-test-automation](https://github.com/hyperledger/indy-test-automation) - Automation tools for testing of Indy Project components.
* [indy-post-install-automation](https://github.com/hyperledger/indy-post-install-automation)
* [indy-hipe](https://github.com/hyperledger/indy-hipe) - 
Hyperledger Indy Project Enhancements
  * https://indy.readthedocs.io/projects/hipe/en/latest/
* [indy-crypto](https://github.com/hyperledger/indy-crypto) - shared crypto library for Hyperledger Indy components. To be:
* [ursa](https://github.com/hyperledger/ursa) [[**ϟ**](https://www.hyperledger.org/blog/2018/12/04/welcome-hyperledger-ursa)][[**ϟ**](https://www.coindesk.com/hyperledger-launches-cryptography-toolbox-for-blockchain-developers)] 
  > "includes the Hyperledger Indy-Crypto code base that is the building block for anonymous credentials, the verifiable credentials protocol, in indy-sdk used by the Sovrin Network. [...]  We are hopeful the shared library will help other platforms better incorporate and use ZKP-based credentials and leverage Sovrin for their identity component." (From Nathan George on Sovrin Telegram) [[**wiki**](https://wiki.hyperledger.org/projects/ursa)]

### IDChain

* [ID-Chain/IEA-API](https://github.com/ID-Chain/IEA-API) - Institutional Edge Agent Generic API
* [ID-Chain/Common](https://github.com/ID-Chain/Common) - Common Repository for IdentityChain Project
* [ID-Chain/tlabshack](https://github.com/ID-Chain/tlabshack) - Repository to hold files for the tlabshack hackathon
* [ID-Chain/ID-Chain.github.io](https://github.com/ID-Chain/ID-Chain.github.io) - Documentation site for IdentityChain Project
* [ID-Chain/Cloud-Agent](https://github.com/ID-Chain/Cloud-Agent) - Indy Cloud Agent using Google Firebase Cloud Messaging
* [ID-Chain/Chamber-Of-Commerce](https://github.com/ID-Chain/Chamber-Of-Commerce) - Institutional Edge Agent Legacy Example (Verifier + Issuer)
* [ID-Chain/Government](https://github.com/ID-Chain/Government) - Institutional Edge Agent Legacy Example (Initial Issuer)
* [ID-Chain/IEA-Admin-UI](https://github.com/ID-Chain/IEA-Admin-UI) - Admin User Interface to manage the Institutional Edge Agent API
* [ID-Chain/Schema-Extensions](https://github.com/ID-Chain/Schema-Extensions) - High level Schema Extensions (Compiler & Checker)
* [ID-Chain/Mobile-Edge-Agent](https://github.com/ID-Chain/Mobile-Edge-Agent) - Mobile Edge Agent Application



### /IBM-Blockchain-Identity

[IBM-Blockchain-Identity/indy-tutorial-sandbox](https://github.com/IBM-Blockchain-Identity/indy-tutorial-sandbox) - Forked from brycecurtis/indy-tutorial-sandbox
A turnkey, Docker-based sandbox that enables quick and easy exploration of Hyperledger Indy concepts.

[IBM-Blockchain-Identityindy-ssivc-tutorial](https://github.com/IBM-Blockchain-Identity/indy-ssivc-tutorial) - A turnkey, Docker-based tutorial for help developers get acquainted with Self-Sovereign Identity and Verifiable Credentials.
 

## Verifiable Organizations Network

* [bcgov/BC-Policy-Framework-For-GitHub](https://github.com/bcgov/BC-Policy-Framework-For-GitHub) - Policy information for BC Government employees using GitHub
* [bcgov/design-system](https://github.com/bcgov/design-system) - British Columbia Government Design System for Digital Services

### BCGov - VON
* [bcgov/TheOrgBook](https://github.com/bcgov/TheOrgBook) - A public repository of verifiable claims about organizations. A key component of the Verifiable Organization Network.
* [bcgov/von](https://github.com/bcgov/von) - Verifiable Organizations Network
* [bcgov/von-connector](https://github.com/bcgov/von-connector) - Verifiable Organization Network Connector
* [bcgov/von-network](https://github.com/bcgov/von-network) - A portable development level Indy Node network.
* [bcgov/von-ledger-explorer](https://github.com/bcgov/von-ledger-explorer) - The VON Ledger Explorer
* [bcgov/dFlow](https://github.com/bcgov/dFlow) - A demonstration of the verifiable organization network showing a new restaurant gathering the permits necessary to open.

#### VON - Indy

* [bcgov/indy-catalyst](https://github.com/bcgov/indy-catalyst) - Hyperledger Indy Catalyst is a set of application level software components designed to accelerate the adoption of trustworthy entity to entity communications.
* [bcgov/indy-sdk-postgres-storage](https://github.com/bcgov/indy-sdk-postgres-storage) - PostgreSQL plug-in for use with the indy-sdk

#### VON - Agents


* [bcgov/von-personal-agent](https://github.com/bcgov/von-personal-agent) - A personal agent for the von network.
* [bcgov/VON-ESB-DRS-Agent](https://github.com/bcgov/VON-ESB-DRS-Agent) - Piloting the Dispute Resolution Suite with connections to the OrgBook
* [bcgov/von-agent-template](https://github.com/bcgov/von-agent-template) - Template for a von-x based agent
* [bcgov/von-bc-registries-agent](https://github.com/bcgov/von-bc-registries-agent)
* [bcgov/von_agent](https://github.com/bcgov/von_agent) Forked from PSPC-SPAC-buyandsell/von_agent - VON agents using indy-sdk


### BCGov - DID-Auth
* [bcgov/did-auth-extension](https://github.com/bcgov/did-auth-extension) - DID Auth browser extension.
* [bcgov/http-did-auth-proxy](https://github.com/bcgov/http-did-auth-proxy) - DID Auth HTTP proxy.
* [bcgov/did-auth-relying-party](https://github.com/bcgov/did-auth-relying-party) - DID Auth relying party.

### /PSPC-SPAC-buyandsell
**Public Services and Procurement Canada: buyandsell.gc.ca --- Services publics et Approvisionnement Canada : Achatsetventes.gc.ca**

* [PSPC-SPAC-buyandsell/von_tails](https://github.com/PSPC-SPAC-buyandsell/von_tails) - Tails file server for von_anchor issuer and holder-prover anchors
* [PSPC-SPAC-buyandsell/von_base](https://github.com/PSPC-SPAC-buyandsell/von_base)
* [PSPC-SPAC-buyandsell/von_anchor](https://github.com/PSPC-SPAC-buyandsell/von_anchor) - VON anchor classes for interaction with sovrin/indy ledger via indy-sdk
* [PSPC-SPAC-buyandsell/von-image](https://github.com/PSPC-SPAC-buyandsell/von-image) - Standard docker images for building VON components
* [PSPC-SPAC-buyandsell/von-x](https://github.com/PSPC-SPAC-buyandsell/von-x) - VON-X is a Python library enabling rapid deployment of Hyperledger Indy credential issuer, holder, and verifier services, particularly for integration with TheOrgBook.
* [PSPC-SPAC-buyandsell/didauth](https://github.com/PSPC-SPAC-buyandsell/didauth) - DID authentication by way of HTTP Signatures for Hyperledger Indy agents
* [PSPC-SPAC-buyandsell/von_agent](https://github.com/PSPC-SPAC-buyandsell/von_agent) - VON agents using indy-sdk
* [PSPC-SPAC-buyandsell/von_connector](https://github.com/PSPC-SPAC-buyandsell/von_connector) - service wrapper API per agent, via django application
* [PSPC-SPAC-buyandsell/ReferenceVonActuator](https://github.com/PSPC-SPAC-buyandsell/ReferenceVonActuator) - Java implementation of actuator of reference von_connector implementation
* [PSPC-SPAC-buyandsell/von_conx](https://github.com/PSPC-SPAC-buyandsell/von_conx) - Reference implementation (sample) for a VON Connector using tools of VON_X
* [PSPC-SPAC-buyandsell/demo-agent](https://github.com/PSPC-SPAC-buyandsell/demo-agent) - agent and api wrapper code base

## Selfkey Foundation

* [SelfKeyFoundation/selfkeyfoundation.github.io](https://github.com/SelfKeyFoundation/selfkeyfoundation.github.io)
* [SelfKeyFoundation/selfkey-developers](https://github.com/SelfKeyFoundation/selfkey-developers) - SelfKey Developer Site
* [SelfKeyFoundation/selfkey-developer-portal](https://github.com/SelfKeyFoundation/selfkey-developer-portal) - Developer Resources for SelfKey SDK's
* [SelfKeyFoundation/selfkey-platform](https://github.com/SelfKeyFoundation/selfkey-platform) - Temporarily hosted here until ready for public consumption.
* [SelfKeyFoundation/selfkey-download-portal](https://github.com/SelfKeyFoundation/selfkey-download-portal) - Download links and information for SelfKey software releases
* [SelfKeyFoundation/selfkey-net](https://github.com/SelfKeyFoundation/selfkey-net)
* [SelfKeyFoundation/Identity-Wallet](https://github.com/SelfKeyFoundation/Identity-Wallet) - Code for the SelfKey Identity Wallet
* [SelfKeyFoundation/selfkey-ui](https://github.com/SelfKeyFoundation/selfkey-ui)
* [SelfKeyFoundation/selfkey-simulation](https://github.com/SelfKeyFoundation/selfkey-simulation)
* [SelfKeyFoundation/selfkey-payments](https://github.com/SelfKeyFoundation/selfkey-payments)
* [SelfKeyFoundation/selfkey-lib](https://github.com/SelfKeyFoundation/selfkey-lib)
* [SelfKeyFoundation/selfkey-network-demo](https://github.com/SelfKeyFoundation/selfkey-network-demo)
* [SelfKeyFoundation/selfkey-extension](https://github.com/SelfKeyFoundation/selfkey-extension) - SelfKey Extension
* [SelfKeyFoundation/selfkey-service](https://github.com/SelfKeyFoundation/selfkey-service) - SelfKey Service
* [SelfKeyFoundation/selfkey-aspnetcore-demo](https://github.com/SelfKeyFoundation/selfkey-aspnetcore-demo)
* [SelfKeyFoundation/face-rec](https://github.com/SelfKeyFoundation/face-rec) - Selfkey Face Recognition API
* [SelfKeyFoundation/passport-selfkey](https://github.com/SelfKeyFoundation/passport-selfkey)
* [SelfKeyFoundation/selfkey-login](https://github.com/SelfKeyFoundation/selfkey-login) - Components for external "log-in with selfkey"
* [SelfKeyFoundation/matomo](https://github.com/SelfKeyFoundation/matomo) - SelfKey Foundation Matomo server
* [SelfKeyFoundation/Marketplaces](https://github.com/SelfKeyFoundation/Marketplaces) - Marketplace Applications
* [SelfKeyFoundation/identity-wallet-mobile](https://github.com/SelfKeyFoundation/identity-wallet-mobile) - The React Native mobile application for SelfKey.

### Selfkey DID

* [SelfKeyFoundation/selfkey-did](https://github.com/SelfKeyFoundation/selfkey-did) - Library for DID managemente and issuance and verification of verifiable credentials
* [SelfKeyFoundation/selfkey-claim-registry](https://github.com/SelfKeyFoundation/selfkey-claim-registry) - Public claim registry for Selfkey DIDs
* [SelfKeyFoundation/selfkey-did-resolver](https://github.com/SelfKeyFoundation/selfkey-did-resolver) - Library for resolving DIDs in SelfKey method space

### Selfkey SmartContracts
* [SelfKeyFoundation/selfkey-commerce](https://github.com/SelfKeyFoundation/selfkey-commerce) - Payment, Escrow and Affiliate Smart Contract Development
* [SelfKeyFoundation/selfkey-token](https://github.com/SelfKeyFoundation/selfkey-token) - Crowdsale Smart Contract
* [SelfKeyFoundation/selfkey-identity](https://github.com/SelfKeyFoundation/selfkey-identity) - Smart contracts supporting SelfKey identity platform
* [SelfKeyFoundation/selfkey-staking](https://github.com/SelfKeyFoundation/selfkey-staking) - Contracts that implement staking and marketplace deposit functionality for SelfKey
* [SelfKeyFoundation/identity-contracts](https://github.com/SelfKeyFoundation/identity-contracts) - Development on self-sovereign identity and verifiable claims
* [SelfKeyFoundation/selfkey-name-registry](https://github.com/SelfKeyFoundation/selfkey-name-registry) - Smart contract for registering names

### Selfkey Javascript
* [SelfKeyFoundation/keythereum](https://github.com/SelfKeyFoundation/keythereum) - Forked from ethereumjs/keythereum - Create, import and export Ethereum keys
* [SelfKeyFoundation/selfkey-js-client](https://github.com/SelfKeyFoundation/selfkey-js-client) - JavaScript Client Library for integrating Login with SelfKey
* [SelfKeyFoundation/selfkey-nodejs-demo](https://github.com/SelfKeyFoundation/selfkey-nodejs-demo) - Demo Site For Testing SelfKey Marketplace and LWS Integrations

### Selfkey Assorted

* [SelfKeyFoundation/trezor-wallet-provider](https://github.com/SelfKeyFoundation/trezor-wallet-provider) - Forked from HartgerV/trezor-wallet-provider - Trezor wallet provider for the Web3 ProviderEngine
* [SelfKeyFoundation/lws-app](https://github.com/SelfKeyFoundation/lws-app) - lws-app react app prototype
* [SelfKeyFoundation/airtable-proxy](https://github.com/SelfKeyFoundation/airtable-proxy) - A proxy service for airtable
* [SelfKeyFoundation/react-jsonschema-form-material-theme](https://github.com/SelfKeyFoundation/react-jsonschema-form-material-theme) - Widgets and templates using material-ui
* [react-jsonschema-form](https://github.com/SelfKeyFoundation/react-jsonschema-form) - Forked from rodrigopavezi/react-jsonschema-form
A React component for building Web forms from JSON Schema.



## Ockam Network

* [ockam-network/ockam](https://github.com/ockam-network/ockam) - Tools for building identity, trust and interoperability into connected devices.
* [ockam-network/did](https://github.com/ockam-network/did) - A golang package to work with Decentralized Identifiers (DIDs)
* [ockam-network/did-method-spec](https://github.com/ockam-network/did-method-spec) - Ockam DID Method Specification

## Ontology

* [ontio/ontology](https://github.com/ontio/ontology) - Official Go implementation of the Ontology protocol. https://dev-docs.ont.io/#/
* [ontio/documentation](https://github.com/ontio/documentation) - Ontology Documents https://ont.io
* [ontio/ontology-DID](https://github.com/ontio/ontology-DID) - Ontology decentralized identification protocol based on W3C DID specifications.
* [ontio/ontology-crypto](https://github.com/ontio/ontology-crypto) 
* [ontio/OWallet](https://github.com/ontio/OWallet) - a comprehensive Ontology desktop wallet
* [ontio/ontology-dapi](https://github.com/ontio/ontology-dapi) - A lightweight Javascript library for interacting with Ontology node and Ontology wallets
* [ontio/ontology-ddxf](https://github.com/ontio/ontology-ddxf) - Distributed data eXchange Framework,which allows to build data marketplaces . 

## TangleID

* [TangleID/TangleID/](https://github.com/TangleID/TangleID/) - Secure self-sovereign identity built on IOTA/Tangle
identity
* [TangleID/api-examples/](https://github.com/TangleID/api-examples/) - API examples for TangleID
* [TangleID/TangleID.github.io/](https://github.com/TangleID/TangleID.github.io/) - TangleID Landing Page
* [TangleID/tangleid-client/](https://github.com/TangleID/tangleid-client/) - TangleID Client/Mobile application
* [TangleID/demo-site/](https://github.com/TangleID/demo-site/) - A sample web illustrating how to issue claims to the participants with TangleID
* [TangleID/docs](https://github.com/TangleID/docs) - TangleID API Documentation
  - Forked from lord/slate
* [TangleID/sample-issuer/](https://github.com/TangleID/sample-issuer/) - TangleID Sample Issuer

## Simbol

AR\VR\Mixed

* [wearesimbol/simbol-design](https://github.com/wearesimbol/simbol-design)
* [wearesimbol/a-simbol](https://github.com/wearesimbol/a-simbol) - A-Frame component for Simbol
* [wearesimbol/simbol](https://github.com/wearesimbol/simbol) - Social and Communications platform WebXR sites with a self-sovereign identity
* [wearesimbol/simbol-server](https://github.com/wearesimbol/simbol-server) - Simple Web and WebSocket server, specially for sites that use Simbol
* [wearesimbol/simbol-demo](https://github.com/wearesimbol/simbol-demo) - Create a fullstack Simbol virtual world very easily



## Assorted

[bnelson777/id.ly](https://github.com/bnelson777/id.ly) - Cross-platform self-sovereign identity business card and messaging app


## /peacekeeper/blockchain-identity

>Projects/companies working on blockchain and identity

* [peacekeeper/blockchain-identity](https://github.com/peacekeeper/blockchain-identity) - The Original list of Blockchain Identity Initiatives. 

Maintained by, [Markus Sabadello (Peacekeeper)](https://medium.com/@markus.sabadello)

---

Cover Image Source:

[<img src="https://i.imgur.com/RhbNQXF.png"/>](https://github.myshopify.com/products/die-cut-github-stickers)<br/>
[https://github.myshopify.com/products/die-cut-github-stickers](https://github.myshopify.com/products/die-cut-github-stickers)

