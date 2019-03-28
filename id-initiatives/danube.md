# Project Danube

Danube Tech must be the longest running firm working towards user-owned and controlled internet identity. 

* [Danube Tech](http://danubetech.com/) — digital identity and personal data, including personal agents, semantic graphs, and blockchain ([**xdi**](https://xdi2.org)) ([**navigator**](https://github.com/projectdanube/xdi2))


## Contents

* [Danube](#danube-)
* [Project Danube on Github](#project-danube-github-)
  * [Danube XDI](#xdi-)
  * [Danube XDI Libraries](#xdi-libraries-)
  * [Danube XDI - Various Integrations](#xdi---various-integrations-)
  * [Danube XDI Configurations](#xdi-configurations-)
  * [Danube XDI Examples](#xdi-examples-)
  * [Danube XDI Plugins](#xdi-plugins-)
  * [Danube Aeternam](#aeternam-)
  * [Danube XDI Cloud](#xdi-cloud-)
  * [Danube XDI Server Deployed Via](#xdi-server-deployed-via-)
  * [Danube Services](#services-)
* [**See also: XDI**](standards/xdi.html) >>

## Danube

* *member of Sovrin and Decentralized Identity foundations*

[Markus Sabadello (Peacekeeper)](http://mydata2016.org/speaker/markus-sabadello/) [[**T**](https://twitter.com/peacekeeper)] [[**G**](https://github.com/peacekeeper)] [[**B**](https://medium.com/@markus.sabadello)] has been working on XDI personal data stores since as early as 2010.

>This is an open-source project offering software for identity and personal data services on the Internet. The core of this project is an XDI-based Personal Data Store - a semantic database for your personal data, which always remains under your control. Applications on top of this database include the Federated Social Web, the selective sharing of personal data with organizations, and much more.
>[![](https://i.imgur.com/dpKldXI.png)](https://web.archive.org/web/20101103064516/http://projectdanube.org/)


* [A position paper on blockchain enabled identity and the road ahead](https://www.bundesblock.de/wp-content/uploads/2018/10/ssi-paper.pdf)—Identity Working Group of the German Blockchain Association [[**ϟ**](https://www.bundesblock.de/2018/10/23/position-paper-self-sovereign-identity/)]
  >In a SSI proof-of-concept during the first half of 2018, 3 banks, an insurance company, the Austrian Post, and an institution representing notaries has cooperated to implement a range of use cases based on DIDs, Verifiable Credentials, Sovrin, and the XDI protocol. The use cases included:
  > * digital ID onboarding for existing clients,
  > * SSO for new clients,
  > * sharing of KYC data between organizations,
  > * dynamic data verification (change-of-address),
  > * secure communication (e-mail with ID confirmation),
  > * change of identity service providers,
  > * personal ID verification in a peer-to-peer marketplace


## /project-danube Github [**^**](#contents)

* <a href="https://github.com/projectdanube/indy-sdk-java" target="_blank">/projectdanube/indy-sdk-java</a> - Java binding to the native Indy SDK
* <a href="https://github.com/projectdanube/blockstack-cli-java" target="_blank">/projectdanube/blockstack-cli-java</a> - Java client for Blockstore


### XDI [**^**](#contents)

>[XDI.org](https://xdi.org) is a non-profit public trust organization whose purpose is to provide public infrastructure for digital identity, security, and privacy using the open standard XDI semantic data interchange protocol developed by the OASIS XDI Technical Committee.
* <a href="https://github.com/projectdanube/xdi-tutorial" target="_blank">/projectdanube/xdi-tutorial</a> - XDI Tutorial
* <a href="https://github.com/projectdanube/XDINinja-swing" target="_blank">/projectdanube/XDINinja-swing</a> - XDI-enabled standalone client application
* <a href="https://github.com/projectdanube/xdi2-tools" target="_blank">/projectdanube/xdi2-tools</a> - XDI2 maintenance and other tools
* <a href="https://github.com/projectdanube/xdi2-connector-personal" target="_blank">/projectdanube/xdi2-connector-personal</a> - A connector plugin for the XDI2 server that maps data from Personal.com to XDI
* <a href="https://github.com/projectdanube/xdi2-docker" target="_blank">/projectdanube/xdi2-docker</a> - Dockerfiles for XDI2
* <a href="https://github.com/projectdanube/xdi2-connect-buttonbuilder" target="_blank">/projectdanube/xdi2-connect-buttonbuilder</a> - "Button Builder" component for the XDI Connect protocol

### XDI libraries [**^**](#contents)

* <a href="https://github.com/projectdanube/xdi2" target="_blank">/projectdanube/xdi2</a> - XDI2 general purpose library and server
* <a href="https://github.com/projectdanube/xdi-js" target="_blank">/projectdanube/xdi-js</a> - XDI client library for JavaScript
* <a href="https://github.com/projectdanube/xdi2-connect-core" target="_blank">/projectdanube/xdi2-connect-core</a> - Shared library for the XDI Connect protocol


### XDI - Various Integrations [**^**](#contents)

* <a href="https://github.com/projectdanube/xdi2-bdb" target="_blank">/projectdanube/xdi2-bdb</a> - Support for using BDB as XDI2 backend storage
* <a href="https://github.com/projectdanube/xdi2-mongodb" target="_blank">/projectdanube/xdi2-mongodb</a> - Support for using MongoDB as XDI2 backend storage
* <a href="https://github.com/projectdanube/xdi2-server-heroku" target="_blank">/projectdanube/xdi2-server-heroku</a> - XDI2 Server deployed via Heroku
* <a href="https://github.com/projectdanube/xdi2-redis" target="_blank">/projectdanube/xdi2-redis</a> - Support for using Redis as XDI2 backend storage
* <a href="https://github.com/projectdanube/xdi2-tor" target="_blank">/projectdanube/xdi2-tor</a> - Integration of XDI and Tor
* <a href="https://github.com/projectdanube/xdi2-ipfs" target="_blank">/projectdanube/xdi2-ipfs</a> - Integration of XDI and IPFS
* <a href="https://github.com/projectdanube/withsqlite" target="_blank">/projectdanube/withsqlite</a> - A module for a python dict that back ends on an sqlite3 database. It's bit like shelve but with json and sqlite3.
  - Forked from jvasile/withsqlite

### XDI Configuration [**^**](#contents)

* <a href="https://github.com/projectdanube/xdi2-selfhosted" target="_blank">/projectdanube/xdi2-selfhosted</a> - A configuration profile of the XDI2 server for self-hosting a single XDI graph.
* <a href="https://github.com/projectdanube/xdi2-csp" target="_blank">/projectdanube/xdi2-csp</a> - A configuration profile of the XDI2 server for hosting a dynamic number of XDI graphs.
* <a href="https://github.com/projectdanube/xdi2-registry" target="_blank">/projectdanube/xdi2-registry</a> - 
A configuration profile of the XDI2 server for hosting a registry of XDI names and XDI numbers.

### XDI Examples [**^**](#contents)

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



### XDI Plugins [**^**](#contents)

* <a href="https://github.com/projectdanube/xdi2-crypto-secp256k1" target="_blank">/projectdanube/xdi2-crypto-secp256k1</a> - This is an secp256k1 crypto plugin for the XDI2 client and server.
* <a href="https://github.com/projectdanube/xdi2-crypto-ec25519" target="_blank">/projectdanube/xdi2-crypto-ec25519</a> - This is an Ed25519 crypto plugin for the XDI2 client and server.
* <a href="https://github.com/projectdanube/xdi2-connector-facebook" target="_blank">/projectdanube/xdi2-connector-facebook</a> - A connector plugin for the XDI2 server that maps data from Facebook to XDI
* <a href="https://github.com/projectdanube/xdi2-connector-meeco" target="_blank">/projectdanube/xdi2-connector-meeco</a> - A connector plugin for Meeco
* <a href="https://github.com/projectdanube/XDINinja-plugin" target="_blank">/projectdanube/XDINinja-plugin</a> - A browser plugin that is like "Twitter for data"
* <a href="https://github.com/projectdanube/xdi2-connector-cozy" target="_blank">/projectdanube/xdi2-connector-cozy</a> - A connector plugin for CozyCloud
* <a href="https://github.com/projectdanube/xdi2-filesys" target="_blank">/projectdanube/xdi2-filesys</a> - Plugin for an XDI2 server to integrate with a local filesystem

### Aeternam [**^**](#contents)

* <a href="https://github.com/projectdanube/aeternam-xdi-sncf" target="_blank">/projectdanube/aeternam-xdi-sncf</a> - Aeternam PNR Demo: SNCF
* <a href="https://github.com/projectdanube/aeternam-xdi-db" target="_blank">/projectdanube/aeternam-xdi-db</a> - Aeternam PNR Demo: Deutsche Bahn
* <a href="https://github.com/projectdanube/aeternam-xdi-tests" target="_blank">/projectdanube/aeternam-xdi-tests</a> - XDI experimentation for ÆTERNAM / ÆVATAR
* <a href="https://github.com/projectdanube/aeternam-xdi-maria" target="_blank">/projectdanube/aeternam-xdi-maria</a> - Aeternam PNR Demo: Maria
* <a href="https://github.com/projectdanube/aeternam-xdi-webshop" target="_blank">/projectdanube/aeternam-xdi-webshop</a> - Aeternam PNR Demo: Webshop
* <a href="https://github.com/projectdanube/aeternam-xdi-oebb" target="_blank">/projectdanube/aeternam-xdi-oebb</a> - Aeternam PNR Demo: ÖBB

### XDI Cloud [**^**](#contents)

* <a href="https://github.com/projectdanube/xdi2-cloudcards" target="_blank">/projectdanube/xdi2-cloudcards</a> - XDI Cloud Card Viewer
* <a href="https://github.com/projectdanube/xdi2-messenger" target="_blank">/projectdanube/xdi2-messenger</a> - XDI Cloud Messenger
* <a href="https://github.com/projectdanube/xdi2-manager" target="_blank">/projectdanube/xdi2-manager</a> - XDI Cloud Manager
* <a href="https://github.com/projectdanube/xdi2-pixel" target="_blank">/projectdanube/xdi2-pixel</a> - Tool to translate a personal cloud policy language (Pixel) to XDI link contracts.

### XDI Server Deployed Via [**^**](#contents)

* <a href="https://github.com/projectdanube/xdi2-server-grizzly" target="_blank">/projectdanube/xdi2-server-grizzly</a> - XDI2 Server deployed via Grizzly
* <a href="https://github.com/projectdanube/xdi2-server-mina" target="_blank">/projectdanube/xdi2-server-mina</a> - XDI2 Server deployed via Apache MINA
* <a href="https://github.com/projectdanube/xdi2-server-netty" target="_blank">/projectdanube/xdi2-server-netty</a> - XDI2 Server deployed via netty
* <a href="https://github.com/projectdanube/xdi2-server-undertow" target="_blank">/projectdanube/xdi2-server-undertow</a> - XDI2 Server deployed via Undertow
* <a href="https://github.com/projectdanube/xdi2-server-vertx" target="_blank">/projectdanube/xdi2-server-vertx</a> - XDI2 Server deployed via vert.x

### Sevices [**^**](#contents)
* <a href="https://github.com/projectdanube/xdi2-connect-service" target="_blank">/projectdanube/xdi2-connect-service</a> - This is a "Connect Service" component for the XDI Browser binding.
* <a href="https://github.com/projectdanube/neustar-discovery-service" target="_blank">/projectdanube/neustar-discovery-service</a> - Neustar XDI Discovery Service based on XRI Resolution
  - Forked from neustarpc/neustar-discovery-service
* <a href="https://github.com/projectdanube/xdi2-connect-auth-service-war" target="_blank">/projectdanube/xdi2-connect-auth-service-war</a> - "Authorization Service" for the XDI Connect protocol, packaged as .WAR file
* <a href="https://github.com/projectdanube/xdi2-connect-service-war" target="_blank">/projectdanube/xdi2-connect-service-war</a> - "Connect Service" for the XDI Connect protocol, packaged as .WAR file
* <a href="https://github.com/projectdanube/xdi-grapheditor" target="_blank">/projectdanube/xdi-grapheditor</a> - An XDI Graph Editor
  -Forked from neustar/xdi-grapheditor
* <a href="https://github.com/projectdanube/xdi2-connect-auth-service" target="_blank">/projectdanube/xdi2-connect-auth-service</a> - This is a "Connect Auth Service" component for the XDI Browser binding.


