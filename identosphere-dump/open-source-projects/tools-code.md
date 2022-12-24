---
published: false
---

[our library for Verifiable Credential eXchange](http://github.com/evernym/sdk) 
## Code

Code: [https://github.com/swiss-ssi-group/MattrGlobalAspNetCore](https://github.com/swiss-ssi-group/MattrGlobalAspNetCore)

## Schema

* [Announcing Schema Markup Validator: validator.schema.org (beta)](http://blog.schema.org/2021/05/announcing-schema-markup-validator.html)

SDTT is a tool from Google which began life as the [Rich Snippets Testing Tool](https://developers.google.com/search/blog/2010/09/rich-snippets-testing-tool-improvements) back in 2010. Last year Google [announced plans](https://developers.google.com/search/blog/2020/07/rich-results-test-out-of-beta) to migrate from SDTT to successor tooling, the [Rich Results Test](https://search.google.com/test/rich-results), alongside plans to "deprecate the Structured Data Testing Tool". The newer Google tooling is focused on helping publishers who are targeting specific schema.org-powered [search features](https://developers.google.com/search/docs/guides/search-gallery) offered by Google, and for these purposes is a huge improvement as it contextualizes many warnings and errors to a specific target application.

## Semantics
* [The Importance of Data Inputs and Semantics for SSI with Paul Knowles [Podcast]](https://northernblock.io/semantics-for-ssi-with-paul-knowles/)
  > The platform was an incredibly federated platform when I built it because I didn’t know that SSI existed. So as soon as I found that ecosystem, I tore up the rulebook and said, “This isn’t going to work; I have to rebuild it.”

## QR

* [Gordian QR Tool Supports Vaccine Records, 2FAs, Cryptoseeds, and More](https://www.blockchaincommons.com/projects/Releasing-QRTool/) Blockchain Commons
  > Some possible architectural issues arise from using QR codes for confidential data, such as the fact that you’re actually transmitting the data (not a proof of the data), that the QRs tend to contain all of the data (not just a selection), and that there’s no way to rescind a QR or expire it. Those issues will have to be dealt with at a foundational level as we figure out what can safely be encoded as a QR — and more importantly how to offer restricted proofs rather than complete information.

## Mobile Agent Dev
* [App Framework for Mobile Agent Dev - “No more forking”](https://iiw.idcommons.net/22A/_App_Framework_for_Mobile_Agent_Dev_-_%2522No_more_forking%2522) by Horacio Nunez

This session had the objective to present a solution to the problem of forking when developing new mobile agents. With the current starting kits available in the community it is very easy to start a path where it is almost impossible to retrofit updates to the kit back into our custom agent.

The solution consists in using a framework-first approach and ensuring that custom code can reside exclusively outside of the framework, thus ensuring updates can be executed more easily.

The following link can be used as the public url for the project:

* [https://www.notion.so/App-Framework-for-Mobile-Agent-Development-No-more-forking-52ebe4e5635d400eb225b0ed537404d8](https://www.notion.so/App-Framework-for-Mobile-Agent-Development-No-more-forking-52ebe4e5635d400eb225b0ed537404d8)


### Caribou - Research \ Advisory
Digital Caribou shares their thoughts on [Digital Transformation and inclusion](https://medium.com/caribou-digital/transformation-in-a-digital-age-9068338fd778) - very good thinking for all of us working on digital identity.

> We believe that the emphasis on transformation as both process and effects is particularly important, especially as although digitization and digitalization are well underway, accelerated by the response to COVID-19 (remote working, payments, etc.), these are not inevitable processes. They are the results of human decisions. Similarly, the effects of these are not inevitable, either.
* [The human impact of identity exclusion in financial service](https://medium.com/caribou-digital/the-human-impact-of-identity-exclusion-in-financial-services-ce1e0d769389) Caribou Digital
  > we spoke to a range of participants who are or who have felt excluded from financial systems for different reasons and we’ll be sharing these stories over the next few months. This research is the foundation for Women in Identity to build an Identity Code of Conduct — a set of guiding principles and a framework for inclusive ID-product development.
* [Digital Identity for Development — and protection](https://medium.com/caribou-digital/digital-identity-for-development-and-protection-d92716f24bb6) Caribou Digital
  > the deployment of digital identification systems needs to get smarter about understanding the political interests and risks that shape the contexts in which identification systems are used — our [ID Ecosystem Mapping tool](https://medium.com/caribou-digital/kenyas-identification-ecosystem-7cbc2ee27) supports risk assessment arising from the deployment of digital identification systems.

## General Dev
* [Technical Debt](https://www.continuumloop.com/technical-debt/)
  > - Technical Debt – Seth covers it well but missed a major cause of technical debt. That being the shortcuts that are taken to meet deadlines and requirements – with the hope/fantasy that we’ll go back and do them right later (hint: we never do).
  > - Project Debt
  > - Why saying NO to those simple things may be the best thing. For some hints on how to do that see [Say No With Grace](https://www.continuumloop.com/say-no-with-grace/).
* [The Journey of an SSI Developer](https://academy.affinidi.com/the-journey-of-an-ssi-developer-6ef4f642779c) Affinidi
* [Clear is better than clever](https://dave.cheney.net/2019/07/09/clear-is-better-than-clever) Cheney.net

“why would I read your code?” To be clear, when I say I, I don’t mean me, I mean you. And when I say your code I also mean you, but in the third person. So really what I’m asking is, “why would you read another person’s code?”
* [Contributing to Complex Projects](https://mitchellh.com/writing/contributing-to-complex-projects) Mitchell H

Inspiration - for folks engaging with new code

As a frequent open source maintainer and contributor, I’m often asked: where do you start? How do you approach a new project with the goal of making meaningful changes? How can you possibly understand the internals of a complex project?


### Civic

* [Introducing New Tools for Creators to Build Trusted Communities](https://www.civic.com/blog/introducing-new-tools-for-creators-to-build-trusted-communities/) CIVIC

Our goal is to make the process of building trust easier and more effective for creators. With that in mind, we’re sharing an overview of our plan to address the pain points of creators and marketplaces in the NFT space using identity tools.

## Entrustient
* [No Code Solution Using Self-Sovereign Identity on Redundant Blockchains](https://www.pressrelease.cc/2021/12/02/entrustient-launches-the-first-no-code-solution-for-trusted-decentralized-digital-identity-using-self-sovereign-identity-on-redundant-blockchains/) Entrustient

Our goal was to put the power back into the hands of users who do not have any coding knowledge or experience, to accelerate the time to configure and launch an entire Trusted Decentralized Digital Identity peer-to-peer ecosystem



### Sphereon
* [PRESENTATION EXCHANGE WITH SIOP V2](https://sphereon.com/solution/dif-presentation-exchange-with-siop-v2/)

Sphereon has developed a Typescript/Javascript Library  that implements the functionality described in the [DIF Presentation Exchange](https://identity.foundation/presentation-exchange/) specification.

### bloom

* [Introducing SSI SDK](https://bloom.co/blog/introducing-ssi-sdk/) Bloom

- @bloomprotocol/vc
- @bloomprotocol/ecdsa-secp256k1-signature-2019
- @bloomprotocol/ecdsa-secp256k1-verification-key-2019
- @bloomprotocol/elem-did-legacy-non-anchored
- @bloomprotocol/waci-core
- @bloomprotocol/waci-jose
- @bloomprocotol/waci-kit-react
- @bloomprotocol/presentation-exchange
- @bloomprotocol/credential-manifest

### Ringaile
* [How to write verifiable credentials in golang](https://ringaile.medium.com/how-to-write-verifiable-credentials-in-golang-7447234d5c16)
Note: the code is written following the 
[Verifiable Credentials Data Model 1.0](https://www.w3.org/TR/vc-data-model/)
You can find full code here: 
[https://github.com/ringaile/ver-cred](https://github.com/ringaile/ver-cred)

### EPS
* [EPS for SSI (Self-Sovereign Identity)](https://kokumai.medium.com/eps-for-ssi-self-sovereign-identity-8c742e2b1d02)
  > In my earlier post, I failed to refer specifically to the people working for Self-Sovereign Identity and the likes of blockchain that support the distributed/decentralised storage of secrets. [...] you might all be interested to hear that the key function of Expanded Password System is to convert images to high-entropy codes that work as very long passwords and also as the seeds of symmetric/asymmetric cryptographic keys.

### Dillo-DID Plugin Dillo Browser

* [Dillo plugin for DID URLs](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0038.html) Charles E. Lehner
  > I would like to announce dillo-did, a plugin for the Dillo web browser implementing support for DIDs. This plugin enables navigating to DID URLs in Dillo and viewing the resolved/dereferenced DID documents and resources like web pages. The implementation of the DID functionality used is from ssi/DIDKit.


### Godidy
* [@mfosterio · Apr 29](https://twitter.com/mfosterio/status/1520130657468440576) Twitter

I created a DID at [http://GoDiddy.com](https://t.co/QhwQhqUz0k) did:key:z6MkfxFPD3vwny367HZVQoqUnKatH4RTHEitcbEdvxst3nZm#z6MkfxFPD3vwny367HZVQoqUnKatH4RTHEitcbEdvxst3nZm DIDs are important in Self Sovereign Identity. You can learn about DIDs 

### ownyourdata
* [Semantic Overlay Architecture](https://www.ownyourdata.eu/en/semantic-overlay-architecture/) Own Your Data

We have documented the [functionality of SOyA](https://ownyourdata.github.io/soya/) in a W3C-conforming Specifiation and the full source code is available under the MIT License [on Github](https://github.com/OwnYourData/soya/). Examples and an introduction how to use SOyA is [available in a dedicated Tutorial](https://github.com/OwnYourData/soya/blob/main/tutorial/README.md)


### T-Systems
* [Self Sovereign Identity (SSI) at T-Systems MMS: Interview mit Mujtaba Idrees, T-Systems MMS](https://www.youtube.com/watch?v%3DA311QHASy5Y) 7min video on YouTube

► Dr. Ivan Gudymenko, Subject Matter Lead SSI and Confidential Computing, T-Systems MMS

►Mujtaba Idrees, Advanced Software Engineer, T-Systems MMS

► [Credentials as a Service Providing Self Sovereign Identity as a Cloud Service Using Trusted Execution Environments](https://ieeexplore.ieee.org/document/9610297)

### KidOYO
* [Engineer your world this summer: K-University student + teacher opportunities are live!](https://kidoyo.com/join) KidOYO

Whether a beginning learner, or interested in advanced concepts like Game Development, Hardware Prototyping, or Competitive Coding, you will find tools, lessons and mentors


### Aztec

* [Introducing Noir: The Universal Language of Zero-Knowledge](https://medium.com/aztec-protocol/introducing-noir-the-universal-language-of-zero-knowledge-ff43f38d86d9) Aztec Network

Noir is a Rust-based domain specific language (DSL) for creating and verifying zero-knowledge proofs. It’s the easiest way to write zk applications that are compatible with any proving system.


## Danube Tech

* [projectdanube/indy-sdk-java](https://github.com/projectdanube/indy-sdk-java) - Java binding to the native Indy SDK
* [projectdanube/blockstack-cli-java](https://github.com/projectdanube/blockstack-cli-java) - Java client for Blockstore

### XDI

>[XDI.org](https://xdi.org) is a non-profit public trust organization whose purpose is to provide public infrastructure for digital identity, security, and privacy using the open standard XDI semantic data interchange protocol developed by the OASIS XDI Technical Committee.
* [projectdanube/xdi-tutorial](https://github.com/projectdanube/xdi-tutorial) - XDI Tutorial
* [projectdanube/XDINinja-swing](https://github.com/projectdanube/XDINinja-swing) - XDI-enabled standalone client application
* [projectdanube/xdi2-tools](https://github.com/projectdanube/xdi2-tools) - XDI2 maintenance and other tools
* [projectdanube/xdi2-connector-personal](https://github.com/projectdanube/xdi2-connector-personal) - A connector plugin for the XDI2 server that maps data from Personal.com to XDI
* [projectdanube/xdi2-docker](https://github.com/projectdanube/xdi2-docker) - Dockerfiles for XDI2
* [projectdanube/xdi2-connect-buttonbuilder](https://github.com/projectdanube/xdi2-connect-buttonbuilder) - "Button Builder" component for the XDI Connect protocol

#### Libraries

* [projectdanube/xdi2](https://github.com/projectdanube/xdi2) - XDI2 general purpose library and server
* [projectdanube/xdi-js](https://github.com/projectdanube/xdi-js) - XDI client library for JavaScript
* [projectdanube/xdi2-connect-core](https://github.com/projectdanube/xdi2-connect-core) - Shared library for the XDI Connect protocol

#### Integrations

* [projectdanube/xdi2-bdb](https://github.com/projectdanube/xdi2-bdb) - Support for using BDB as XDI2 backend storage
* [projectdanube/xdi2-mongodb](https://github.com/projectdanube/xdi2-mongodb) - Support for using MongoDB as XDI2 backend storage
* [projectdanube/xdi2-server-heroku](https://github.com/projectdanube/xdi2-server-heroku) - XDI2 Server deployed via Heroku
* [projectdanube/xdi2-redis](https://github.com/projectdanube/xdi2-redis) - Support for using Redis as XDI2 backend storage
* [projectdanube/xdi2-tor](https://github.com/projectdanube/xdi2-tor) - Integration of XDI and Tor
* [projectdanube/xdi2-ipfs](https://github.com/projectdanube/xdi2-ipfs) - Integration of XDI and IPFS
* [projectdanube/withsqlite](https://github.com/projectdanube/withsqlite) - A module for a python dict that back ends on an sqlite3 database. It's bit like shelve but with json and sqlite3.
  - Forked from jvasile/withsqlite

#### Configuration

* [projectdanube/xdi2-selfhosted](https://github.com/projectdanube/xdi2-selfhosted) - A configuration profile of the XDI2 server for self-hosting a single XDI graph.
* [projectdanube/xdi2-csp](https://github.com/projectdanube/xdi2-csp) - A configuration profile of the XDI2 server for hosting a dynamic number of XDI graphs.
* [projectdanube/xdi2-registry](https://github.com/projectdanube/xdi2-registry) - 
A configuration profile of the XDI2 server for hosting a registry of XDI names and XDI numbers.

#### Examples

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

#### Plugins

* [projectdanube/xdi2-crypto-secp256k1](https://github.com/projectdanube/xdi2-crypto-secp256k1) - This is an secp256k1 crypto plugin for the XDI2 client and server.
* [projectdanube/xdi2-crypto-ec25519](https://github.com/projectdanube/xdi2-crypto-ec25519) - This is an Ed25519 crypto plugin for the XDI2 client and server.
* [projectdanube/xdi2-connector-facebook](https://github.com/projectdanube/xdi2-connector-facebook) - A connector plugin for the XDI2 server that maps data from Facebook to XDI
* [projectdanube/xdi2-connector-meeco](https://github.com/projectdanube/xdi2-connector-meeco) - A connector plugin for Meeco
* [projectdanube/XDINinja-plugin](https://github.com/projectdanube/XDINinja-plugin) - A browser plugin that is like "Twitter for data"
* [projectdanube/xdi2-connector-cozy](https://github.com/projectdanube/xdi2-connector-cozy) - A connector plugin for CozyCloud
* [projectdanube/xdi2-filesys](https://github.com/projectdanube/xdi2-filesys) - Plugin for an XDI2 server to integrate with a local filesystem

#### Aeternam

* [projectdanube/aeternam-xdi-sncf](https://github.com/projectdanube/aeternam-xdi-sncf) - Aeternam PNR Demo: SNCF
* [projectdanube/aeternam-xdi-db](https://github.com/projectdanube/aeternam-xdi-db) - Aeternam PNR Demo: Deutsche Bahn
* [projectdanube/aeternam-xdi-tests](https://github.com/projectdanube/aeternam-xdi-tests) - XDI experimentation for ÆTERNAM / ÆVATAR
* [projectdanube/aeternam-xdi-maria](https://github.com/projectdanube/aeternam-xdi-maria) - Aeternam PNR Demo: Maria
* [projectdanube/aeternam-xdi-webshop](https://github.com/projectdanube/aeternam-xdi-webshop) - Aeternam PNR Demo: Webshop
* [projectdanube/aeternam-xdi-oebb](https://github.com/projectdanube/aeternam-xdi-oebb) - Aeternam PNR Demo: ÖBB

#### XDI Cloud

* [projectdanube/xdi2-cloudcards](https://github.com/projectdanube/xdi2-cloudcards) - XDI Cloud Card Viewer
* [projectdanube/xdi2-messenger](https://github.com/projectdanube/xdi2-messenger) - XDI Cloud Messenger
* [projectdanube/xdi2-manager](https://github.com/projectdanube/xdi2-manager) - XDI Cloud Manager
* [projectdanube/xdi2-pixel](https://github.com/projectdanube/xdi2-pixel) - Tool to translate a personal cloud policy language (Pixel) to XDI link contracts.

#### XDI Server Deployed Via

* [projectdanube/xdi2-server-grizzly](https://github.com/projectdanube/xdi2-server-grizzly) - XDI2 Server deployed via Grizzly
* [projectdanube/xdi2-server-mina](https://github.com/projectdanube/xdi2-server-mina) - XDI2 Server deployed via Apache MINA
* [projectdanube/xdi2-server-netty](https://github.com/projectdanube/xdi2-server-netty) - XDI2 Server deployed via netty
* [projectdanube/xdi2-server-undertow](https://github.com/projectdanube/xdi2-server-undertow) - XDI2 Server deployed via Undertow
* [projectdanube/xdi2-server-vertx](https://github.com/projectdanube/xdi2-server-vertx) - XDI2 Server deployed via vert.x

#### Sevices
* [projectdanube/xdi2-connect-service](https://github.com/projectdanube/xdi2-connect-service) - This is a "Connect Service" component for the XDI Browser binding.
* [projectdanube/neustar-discovery-service](https://github.com/projectdanube/neustar-discovery-service) - Neustar XDI Discovery Service based on XRI Resolution
  - Forked from neustarpc/neustar-discovery-service
* [projectdanube/xdi2-connect-auth-service-war](https://github.com/projectdanube/xdi2-connect-auth-service-war) - "Authorization Service" for the XDI Connect protocol, packaged as .WAR file
* [projectdanube/xdi2-connect-service-war](https://github.com/projectdanube/xdi2-connect-service-war) - "Connect Service" for the XDI Connect protocol, packaged as .WAR file
* [projectdanube/xdi-grapheditor](https://github.com/projectdanube/xdi-grapheditor) - An XDI Graph Editor
  -Forked from neustar/xdi-grapheditor
* [projectdanube/xdi2-connect-auth-service](https://github.com/projectdanube/xdi2-connect-auth-service) - This is a "Connect Auth Service" component for the XDI Browser binding.
