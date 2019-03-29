---
title:  DID Related Web Standards
layout: single
---

## contents

* [XDI](#xdi)
  * [OASIS XDI TC Technical Committee on GitHub](#oasis-xdi-tech-committee-on-github)
* [W3C](#w3c)
  * [DID the Decentralized Identifier](#did-the-decentralized-identifier)
  * [Verifiable Claims](#verifiable-claims)
* [Decentralized Key Managment DKMS](#decentralized-key-management-agents)
* [DID Auth](#did-auth) 
* [Ethereum ERC-EIP](#ethereum-erc-eip)
  * [ERC725-735](#erc725-735)
* [Blockcerts](#blockcerts)
* [Schema](#schema)


## XDI

* [**XDI**](xdi.html) **>>**

The XNS Public Trust Organization was founded in July 2000, shortly after International Planetwork Conference. -[xdi.org - History](http://xdi.org/?page_id=13)
  > to promote the concept of individuals owning their own digital identity and data based on a nascent technology being produced by two Technical Committees at OASIS: XRI (Extensible Resource Identifier) and XDI (Extensible Data Interchange).
* [tutorial.xdi2.org](https://tutorial.xdi2.org)
  > XDI is a technology for modeling, storing, and manipulating data.
  >
  > It fits into a similar category of technologies as JSON, XML and RDF, but also has a number of properties that distinguishes it.
  >
  > XDI is a graph-based data model. This means that all data is expressed using nodes and arcs in a graph. At a minimum, a graph consists of a single node, called the common root node.

### OASIS XDI Tech Committee on Github
* <a href="https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook">/OASIS-XDI-Technical-Committee/xdi-spec-docbook</a> - XDI Specifications (Docbook)
* <a href="https://github.com/OASIS-XDI-Technical-Committee/xdi-developers-guide">/OASIS-XDI-Technical-Committee/xdi-developers-guide</a> - XDI Developer's Guide
* <a href="https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-openoffice">/OASIS-XDI-Technical-Committee/xdi-spec-openoffice</a> - XDI Specifications (Open Office)
* <a href="https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-dita">/OASIS-XDI-Technical-Committee/xdi-spec-dita</a> - XDI Specifications (DITA)


## W3C

![](https://imgur.com/Lz6RTysl.png)

* [World Wide Web Consortium(W3C)](https://www.w3.org/) [[**T**](https://twitter.com/w3c)] [[**G**](https://github.com/w3c)]
  >The [World Wide Web Consortium (W3C)](https://www.w3.org/Consortium/) is an international community where Member organizations, a full-time staff, and the public work together to develop Web standards. Led by Web inventor and Director Tim Berners-Lee and CEO Jeffrey Jaffe, W3C's mission is to lead the Web to its full potential.
* <a href="https://lists.w3.org/Archives/Public/public-vc-wg/" target="_blank">Verifiable Claims WG - Mailing List</a> (and archives)
* [Credentials Community Group](https://www.w3.org/community/credentials/)[[**B**](https://w3c-ccg.github.io/)]  
* <a href="http://lists.w3.org/Archives/Public/public-credentials/" target="_blank">Public mailing list for the Credentials Community Group</a> (and archives) - Anyone may read or write to this list.
* <a href="https://github.com/opencreds/website" target="_blank">/opencreds/website</a> 
  * [opencreds.org — Identity Credentials 1.0](https://opencreds.org/specs/source/identity-credentials/)
* <a href="https://sea-region.github.com/w3c-dvcg/w3c-dvcg.github.io" target="_blank">/w3c-dvcg/w3c-dvcg.github.io</a> - Landing site for W3C Digital Verification Community Group. [<a href="https://www.w3.org/community/digital-verification/">**W**</a>]
* [JSON-LD 1.0, W3C Recommendation](https://www.w3.org/TR/json-ld/)

![](https://imgur.com/6MLNgXal.png)\
<sup><a href="https://www.youtube.com/watch?v=RllH91rcFdE">The Story of Open SSI Standards - Drummond Reed/Evernym SSIMeetup.org</a>[<b><a href="https://www.slideshare.net/SSIMeetup/self-sovereign-identity-ssi-open-standards-with-drummond-reed">ϟ</a></b>]</sup>

### DID the Decentralized Identifier 

<a href="https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf"><img src="https://i.imgur.com/7NRcJbq.png"/></a>

* [DID Whitepaper](https://github.com/WebOfTrustInfo/rwot2-id2020/blob/master/topics-and-advance-readings/DID-Whitepaper.md)
  > A DID architecture should focus on the set of components that Mr. Gupta refers to as "the minimum required for people to be able to do business (or other critical functions) together".
  >
  >**A Decentralized Identifier (DID) Registry and Discovery Service**
  >
  > This "minimum required" is defined by a union of the proposed requirements identified by the W3C Credential Community Group, the XDI.org Registry Working Group, and the Rebooting the Web of Trust group. It consists of three functions that can be addressed by a combination of blockchain and DHT technology:
  >
  > * A DID registration function
  > * A discovery function that enables looking up a registered DID in the blockchain
  > * A master key recovery function
* [A Universally Unique IDentifier (UUID) URN Namespace](https://www.ietf.org/rfc/rfc4122.txt) <-DID's modeled after
  * [All you need to know about sequential UUID generators](https://blog.2ndquadrant.com/sequential-uuid-generators/)
* [w3c- Decentralized Identifiers (DIDs) v0.11](https://w3c-ccg.github.io/did-spec/)
  * Authors:
     * [Drummond Reed](https://equalsdrummond.name/) [[**T**](https://twitter.com/drummondreed)] ([Evernym](https://www.evernym.com/))  
     * [Manu Sporney](http://manu.sporny.org/)[[**T**](https://twitter.com/manusporny)]  ([Digital Bazaar](https://digitalbazaar.com))
     * Dave Longley ([Digital Bazaar](https://digitalbazaar.com))
     * [Christopher Allen](http://www.lifewithalacrity.com/) [[**info**](https://github.com/ChristopherA/info)] ([Blockstream](https://blockstream.com/))
     * Ryan Grant
     * [Markus Sabadello (Peacekeeper)](http://mydata2016.org/speaker/markus-sabadello/) [[**T**](https://twitter.com/peacekeeper)] [[**G**](https://github.com/peacekeeper)] [[**B**](https://medium.com/@markus.sabadello)] ([Danube Tech](https://github.com/projectdanube))
* [Understanding Decentralized IDs (DIDs)](https://medium.com/@adam_14796/understanding-decentralized-ids-dids-839798b91809)
* [DID Primer](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/draft-documents/did-primer.md) [[**ϟ**](https://github.com/WebOfTrustInfo/rwot7-fall2018/blob/master/topics-and-advance-readings/did-primer-extended.md)]
* [Decentralized IDentifers (DIDs)](https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf) 
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
* [DIDs in DPKI](https://github.com/WebOfTrustInfo/rwot7/blob/master/topics-and-advance-readings/dids-in-dpki.md)
* [What is a DID?](https://docs.google.com/document/d/1Ym85y_bDVN9xkRZ-oD-zlUUIeZjVGWNihfZBk2GQidk/edit)
* [The Path from an id (DID) to a Real-Life Something](https://hyperonomy.com/2019/01/04/the-path-from-a-id-did-to-a-real-life-something)

<a href="https://hyperonomy.files.wordpress.com/2019/01/path-id-did-real-life-somethings-v0.2-1.png"><img src="https://hyperonomy.files.wordpress.com/2019/01/path-id-did-real-life-somethings-v0.2-1.png?w=500"/></a>

### Verifiable Claims 

<a href="https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf"><img src="https://i.imgur.com/nsZ0X7r.png"/></a>


* [Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/) [[**D**](https://www.w3.org/2017/vc/charter.html)]
* [Verifiable Claims Data Model 1.0](https://w3c.github.io/vc-data-model/) [[**G**](https://github.com/w3c/vc-data-model)] [[**D**](https://w3c.github.io/vc-use-cases/)]
* [Verifiable Credentials 101 for SSI – Tyler Ruff – Webinar 11](http://ssimeetup.org/verifiable-credentials-101-ssi-tyler-ruff-webinar-11/)


## DID Auth 

![](https://imgur.com/XMaq5cil.png)


   * [DID Auth and the Little I-am-Me](https://medium.com/@markus.sabadello/did-auth-and-the-little-i-am-me-ec14d757ff09)
   * [Introduction to DID Auth](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/did-auth.md) [[**ϟ**](http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10/)]

<a href="http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10/"><img src="https://i.imgur.com/YNlk8RY.png"/></a>\
http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10


## Decentralized Key Management-Agents 

<img src="https://i.imgur.com/0SLcjUv.png"/>

* [Decentralized Key Management (DKMS): An Essential Missing Piece of the SSI Puzzle - Drummond Reed](https://www.slideshare.net/SSIMeetup/decentralized-key-management-dkms-an-essential-missing-piece-of-the-ssi-puzzle-drummond-reed)
* [Recommendations for Decentralized Key Management Systems](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/dkms-recommendations.md)
* [Agent to Agent Communication](https://drive.google.com/file/d/1PHAy8dMefZG9JNg87Zi33SfKkZvUvXvx/view): Daniel Hardman explains the goals of agent to agent communication


![](https://i.imgur.com/5qc1qrG.png)\
<sup><a href="http://ssimeetup.org/decentralized-key-management-dkms-essential-missing-piece-ssi-puzzle-drummond-reed-webinar-8/">DKMS - An Essential Missing Piece of the SSI Puzzle. Drummond Reed. SSIMeetup.org</a></sup>

* <a href="https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE2DjfY" target="_blank">Microsoft- Decentralized Identity — Own and Control Your Identity.</a>
![](https://i.imgur.com/ozOLCuW.png)

## Ethereum ERC-EIP

* [ERC: Lightweight Identity #1056](https://github.com/ethereum/EIPs/issues/1056) —This ERC describes a standard for creating and updating identities with a limited use of blockchain resources. An identity can have an unlimited number of delegates and attributes associated with it. Identity creation is as simple as creating a regular key pair ethereum account, which means that it's fee (no gas costs) and all ethereum accounts are valid identities. Furthermore this ERC is fully DID compliant.
* [ERC1056 ❤ ERC780 — an open identity and claims protocol for Ethereum](https://medium.com/uport/erc1056-erc780-an-open-identity-and-claims-protocol-for-ethereum-aef7207bc744)
* [EIP-780 Ethereum Claims Registry](https://github.com/ethereum/EIPs/issues/780)
* [EIP712](https://github.com/ethereum/EIPs/blob/f29527ab39357548b06b29e937a48f06ae099de7/EIPS/eip-712.md) - This is a standard for hashing and signing of typed structured data
* [ERC-1484 Digital Identity Aggregator](https://github.com/ethereum/EIPs/issues/1495) —A protocol for aggregating digital identity information that's broadly interoperable with existing, proposed, and hypothetical future digital identity standards.
* [EIP-1078](https://github.com/ethereum/EIPs/blob/ed621645c8f3bc5756492f327cda015f35d9f8da/EIPS/eip-1078.md) - 
This presents a method to replace the usual signup/login design pattern with a minimal ethereum native scheme, that doesn’t require passwords, backing up private keys nor typing seed phrases. 
* [ERC-1077 and ERC-1078: The magic of executable signed messages](https://ethereum-magicians.org/t/erc-1077-and-erc-1078-the-magic-of-executable-signed-messages-to-login-and-do-actions/351)
* [ERC-EIP on GitHub](eth-id-github.html#eip---erc) **>>**

### ERC725-735 

* [ERC725](https://github.com/ethereum/EIPs/issues/725) 
  * The following describes standard functions for a unique identifiable proxy account to be used by humans, groups, organisations, objects and machines
* [ERC735](https://github.com/ethereum/EIPs/issues/735) -  The following describes standard functions for adding, removing and holding of claims.
  - These claims can attested from third parties (issuers) or self attested.
* [Origin partners on ERC725](https://coinjournal.net/origin-protocol-partners-on-new-erc-725-alliance-to-promote-the-adoption-of-blockchain-based-identity-standard)
* [Managing Identity with a UI—ERC-725](https://medium.com/originprotocol/managing-identity-with-a-ui-for-erc-725-5c7422b38c09)
* [Ethereum ERC725 Blockchain Based, Self-Sovereign Identity Management](https://bitcoinexchangeguide.com/ethereum-erc725-blockchain-based-self-sovereign-identity-management/)
* [erc725alliance.org](https://erc725alliance.org)
* [ERC: Lightweight Identity #1056](https://github.com/ethereum/EIPs/issues/1056) —This ERC describes a standard for creating and updating identities with a limited use of blockchain resources. An identity can have an unlimited number of delegates and attributes associated with it. Identity creation is as simple as creating a regular key pair ethereum account, which means that it's fee (no gas costs) and all ethereum accounts are valid identities. Furthermore this ERC is fully DID compliant.



## Blockcerts 
* [Learning Machine](https://www.learningmachine.com/)
* [Academic Credentialing and the Blockchain](https://www.learningmachine.com/academic-credentialing-blockchain/)
* [Blockcerts](https://www.blockcerts.org), developed by learning machine is an open standard for issuing and verifying blockchain-based official records; The project offers  open-source libraries, tools, and mobile apps. MIT has [issued](https://www.insidehighered.com/news/2017/10/19/mit-introduces-digital-diplomas) digital certificates based on this standard.
  * [CXC (Carribean) Pilots E-Certificates on the Blockchain](https://www.cxc.org/cxc-pilots-e-certificates-on-the-blockchain/)
  * [A Decentralized Approach to Blockcerts Credential Revocation](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/blockcerts-revocation.md)


## Schema
* [Schema](https://schema.org) — a collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet. Schema.org vocabulary can be used with many different encodings, including RDFa, Microdata and JSON-LD. These vocabularies cover entities, relationships between entities and actions, and can easily be extended through a well-documented extension model. Over 10 million sites use Schema.org to markup their web pages and email messages. Many applications from Google, Microsoft, Pinterest, Yandex and others already use these vocabularies to power rich, extensible experiences."
