---
title: Linked Data and the Semantic Web
tags: ["Linked Data", "JSON-LD","RDF","W3C","Veres One"]
categories: ["Web Standards"]
permalink: /web-standards/linked-data/
redirect_from: /specs-standards/linked-data/
last_modified_at: 2020-01-09
---


> In 2001, Tim Berners-Lee, inventor of the World Wide Web, published an article in Scientific American. Berners-Lee, along with two other researchers, Ora Lassila and James Hendler, wanted to give the world a preview of the revolutionary new changes they saw coming to the web. Since its introduction only a decade before, the web had fast become the world’s best means for sharing documents with other people. Now, the authors promised, the web would evolve to encompass not just documents but every kind of data one could imagine.  - [Whatever Happened to the Semantic Web?](https://twobithistory.org/2018/05/27/semantic-web.html)

## Getting Started

[linkeddata.org](http://linkeddata.org/)
  > "Linked Data is about using the Web to connect related data that wasn't previously linked, or using the Web to lower the barriers to linking data currently linked using other methods. More specifically, Wikipedia defines Linked Data as "a term used to describe a recommended best practice for exposing, sharing, and connecting pieces of data, information, and knowledge on the Semantic Web using URIs and RDF."

* [semantalytics/awesome-semantic-web](https://github.com/semantalytics/awesome-semantic-web) - A curated list of various semantic web and linked data resources.
* [Awesome Linked Data](https://github.com/nandana/awesome-linkeddata) - A list of tools for publishing and consuming Linked Data.
* [Linked Open Data](https://datahub.io/collections/linked-open-data) - An overview of the Linked Open Data datasets.
* [Publishing and consuming Linked Data embedded in HTML](https://www.w3.org/2001/sw/interest/ldh/)
* [Linked Data for Enterprises](https://kerfors.blogspot.com/)
* [linkeddata/dokieli](https://github.com/linkeddata/dokieli) • [wiki](https://github.com/linkeddata/dokieli/wiki) - Examples in the Wild << Pretty Awesome List
  > dokieli is a decentralised article authoring, annotation, and social notification tool which works from Web browsers. It is built with the following principles in mind: freedom of expression, decentralisation, interoperability, and accessibility.
* [solid/understanding-linked-data](https://github.com/solid/understanding-linked-data) - A slide deck introduction to Linked Data aimed at developers.
* [RDF AND JSON-LD UseCases](https://www.w3.org/2013/dwbp/wiki/RDF_AND_JSON-LD_UseCases)


[Introducing Linked Data And The Semantic Web](http://www.linkeddatatools.com/semantic-web-basics)
  > What is Linked Data and the Semantic Web and what is all the hype about? Principally, the Semantic Web is a Web 3.0 web technology - a way of linking data between systems or entities that allows for rich, self-describing interrelations of data available across the globe on the web.

## Linked Data

* [Designing a Linked Data developer experience](https://ruben.verborgh.org/blog/2018/12/28/designing-a-linked-data-developer-experience/)
  > Making decentralized Web app development fun
  > 
  > While the Semantic Web community was fighting its own internal battles, we failed to gain traction with the people who build apps that are actually used: front-end developers. Ironically, Semantic Web enthusiasts have failed to...
* [Linked Data Capabilities](https://github.com/WebOfTrustInfo/rwot5-boston/blob/master/final-documents/lds-ocap.md) By Christopher Lemmer Webber and Mark S. Miller
  > Linked Data Signatures enable a method of asserting the integrity of linked data documents that are passed throughout the web. The object capability model is a powerful system for ensuring the security of computing systems. In this paper, we explore layering an object capability model on top of Linked Data Signatures via chains of signed proclamations. fn:1 We call this system "Linked Data Capabilities", or "ld-ocap" for short.
* [Identity as Linked Data on Immutable Ledgers](https://github.com/WebOfTrustInfo/rwot3-sf/blob/master/topics-and-advance-readings/identity-as-linked-data-on-immutable-ledgers.md)
  > Content creators on the Web are getting a raw deal. They get a fraction of a cent for an ad played on YouTube, and nothing on Facebook, for filling these sites with traffic-driving content. It’s hard to make a living when you’re a creative. Licensing is hard; the user experience is bad, so lawyers and middlemen extract the most value. In the music industry, more money flows into the pockets of distributors than creatives. Consumers are often happy to pay for their content. Instead, they're forced to sit through ads.
* [Blockchain Extensions for Linked Data Signatures](https://github.com/WebOfTrustInfo/rwot3-sf/blob/master/topics-and-advance-readings/blockchain-extensions-for-linked-data-signatures.md) by Manu Sporny, Harlan Wood, Noah Thorp, Wayne Vaughn, Christopher Allen, Jason Bukowski, and Dave Longley
  > The term Linked Data is used to describe a recommended best practice for exposing, sharing, and connecting information on the Web using standards, such as URLs, to identify things and their properties. When information is presented as Linked Data, other related information can be easily discovered and new information can be easily linked to it. Linked Data is extensible in a decentralized way, greatly reducing barriers to large scale integration.
  > 
  > With the increase in usage of Linked Data for a variety of applications, there is a need to be able to verify the authenticity and integrity of Linked Data documents. The Linked Data Signatures specification added authentication and integrity protection to linked data documents through the use of public/private key cryptography without sacrificing Linked Data features such as extensibility and composability.
* [Resource Integrity Proofs](https://github.com/WebOfTrustInfo/rwot7-toronto/blob/master/final-documents/resource-integrity-proofs.md) by Ganesh Annan and Kim Hamilton Duffy
  > Cryptographic linking provides discoverability, integrity, and scheme agility
  > Contributors: Manu Sporny, Dave Longley, David Lehn, and Bohdan Andriyiv
  > 
  > Currently, the Web provides a simple yet powerful mechanism for the dissemination of information via links. Unfortunately, there is no generalized mechanism that enables verifying that a fetched resource has been delivered without unexpected manipulation. Would it be possible to create an extensible and multipurpose cryptographic link that provides discoverability, integrity, and scheme agility?
  > 
  > Cryptographic linking solutions today have yet to provide a generalized mechanism for creating tamper-evident links. The Subresource Integrity standard limits this guarantee to script and link resources loaded on Web pages via the use of HTML attributes. IPFS provides a verification mechanism that is constrained to hash-based, content-addressable links, with no ability to complete content negotiation. RFC6920 proposes another mechanism that cannot be applied to existing links: it recommends the use of named information hashes and a resolution method that creates a content addressable URL [1]. Resource Integrity Proofs incorporates ideas from these standards and solutions to provide a new data format for cryptographic links that is fit for the open world.
* [Recent happenings with Linked Data Capabilities](https://github.com/WebOfTrustInfo/rwot6-santabarbara/blob/master/topics-and-advance-readings/ld-ocap-recent-happenings.md)
  > Veres One's architecture has been adjusted to take full advantage of Linked Data Capabilities as its primary mechanism for granting authority to perform operations on the ledger as well as on DID Documents. permission to update key materials can be conditionally handed out to an entity (or entities) and later revoked if deemed appropriate using Linked Data Capabilities' design.
  > 
  > As for ledger updates, Accelerators also make use of Linked Data Capabilities. To prevent spamming the ledger, the costs of an update must somehow be accounted for. The traditional way to do this on a blockchain is to use proof of work, and this is also an option in Veres One, but for those use cases where expending time and energy on proof of work is less desirable users can use an "accelerator".
  > 
  > An accelerator is an entity that has been granted a capability to perform updates on the ledger more quickly. Accelerators may likewise take advantage of Linked Data Capabilities' support for delegation, with or without caveats.
* [LD Signature Format Alignment](https://nbviewer.jupyter.org/github/WebOfTrustInfo/rebooting-the-web-of-trust-spring2017/blob/master/final-documents/ld-signatures.pdf)
  > The goal of the "LD Signature Format Alignment" Working Group at Rebooting the Web of Trust IV was to investigate the feasibility and impact of the proposed 2017 RSA Signature Suite spec, which brings JSON-LD signatures into alignment with the JOSE JSON Web Signature (JWS) standards.The 2017 RSA Signature Suite is based on RFC 7797, the JSON Web Signature (JWS) Unencoded Payload Option specifcation. This approach avoids past concerns about JWT raised in the LD signature adopters, including:•Increased space consumption associated withbase-64 encoding.•Difculty of nesting or chaining signatures, leading to data duplication.•Use of a format that is not a JSON object, preventing ability to rely exclusively on a JSON document-based storage engine (whilepreserving the signature)

## GitHub Repos

* [WebOfTrustInfo/ld-signatures-java](https://github.com/WebOfTrustInfo/ld-signatures-java) - Java implementation of Linked Data Signatures
* [WebOfTrustInfo/ld-signatures-python](https://github.com/WebOfTrustInfo/ld-signatures-python)

### W3C-CCG
* [Authorization Capabilities for Linked Data v0.3](https://w3c-ccg.github.io/zcap-ld/) - An object capability framework for linked data systems
  > Authorization Capabilities for Linked Data (ZCAP-LD for short) provides a secure way for linked data systems to grant and express authority utilizing the object capability model. Capabilities are represented as linked data objects which are signed with Linked Data Signatures. ZCAP-LD supports delegating authority to other entities on the network by chaining together capability documents. "Caveats" may be attached to capability documents which may be used to restrict the scope of their use, for example to restrict the actions which may be used or providing a mechanism by which the capability may be later revoked.
* [w3c-ccg/ld-cryptosuite-registry](https://github.com/w3c-ccg/ld-cryptosuite-registry) -  REGISTRY: Linked Data Keys Registry (managed by W3C Credentials Community Group) - w3c-ccg/ld-cryptosuite-registry

### DB - Linked Data

* [digitalbazaar/ocapld.js](https://github.com/digitalbazaar/ocapld.js) - Linked Data Capabilities reference implementation
* [digitalbazaar/cuckoo-ldp](https://github.com/digitalbazaar/cuckoo-ldp) - Cuckoo Cycle Based Linked Data Proofs
* [digitalbazaar/bedrock-ldn-receiver](https://github.com/digitalbazaar/bedrock-ldn-receiver) - Bedrock module for Linked Data Notification Receiver
* [digitalbazaar/bedrock-ldn-inbox](https://github.com/digitalbazaar/bedrock-ldn-inbox) - Bedrock module for Linked Data Notification Inboxes
* [digitalbazaar/bedrock-angular-ldn](https://github.com/digitalbazaar/bedrock-angular-ldn) - Bedrock AngularJS module for Linked Data Notification Sender+Consumer
* [digitalbazaar/flex-ledger](https://github.com/digitalbazaar/flex-ledger) - Forked from web-payments/flex-ledger
A decentralized Linked Data Ledger for the Web


## RDF
[Comparison of RDFJS libraries](https://www.w3.org/community/rdfjs/wiki/Comparison_of_RDFJS_libraries)
[Design Issues - LinkedData](https://www.w3.org/DesignIssues/LinkedData.html) -w3.org
  > The Semantic Web isn't just about putting data on the web. It is about making links, so that a person or machine can explore the web of data.  With linked data, when you have some of it, you can find other, related, data.
  > 
  > Like the web of hypertext, the web of data is constructed with documents on the web. However,  unlike the web of hypertext,  where links are relationships anchors in hypertext documents written in HTML, for data they links  between arbitrary things described by RDF,.  The URIs identify any kind of object or  concept.   But for HTML or RDF, the same expectations apply to make the web grow:
  > 
  > - Use URIs as names for things
  > - Use HTTP URIs so that people can look up those names.
  > - When someone looks up a URI, provide useful information, using the standards (RDF*, SPARQL)
  > - Include links to other URIs. so that they can discover more things.
[RDF.js: The new RDF and Linked Data JavaScript library](https://www.w3.org/community/rdfjs/2018/04/23/rdf-js-the-new-rdf-and-linked-data-javascript-library/)
  > A diverse web requires decentralized data storage and maintenance. According to MIT’s Tim Berners-Lee, “it is about making links, so that a person or machine can explore the web of data. With Linked Data, when you have some of it, you can find other, related, data”.
  >
  > Zazuko’s CTO Thomas Bergwinkl adds that “Linked Data is built on top of the web stack and the programming language of the web is JavaScript. It is crucial for Web Developers to have access to well-designed JavaScript libraries to work with RDF and Linked Data”.
  >
  > The RDFJS W3C Community Group did a tremendous job in defining a standard to represent Linked Data in JavaScript. Several individuals and groups started to implement the RDFJS specification.
