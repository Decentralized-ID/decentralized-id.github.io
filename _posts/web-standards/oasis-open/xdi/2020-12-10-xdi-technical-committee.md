---
date: 2020-12-01
title: XDI Technical Committee
description: XDI is a format and protocol for semantic data interchange -- a way different systems, applications, and databases can describe, map, exchange, link, synchronize, and protect data using a shared semantic graph model.
excerpt: > 
   The purpose of the OASIS XDI TC is to define a generalized, extensible, location-, application-, and transport-independent service for sharing, linking, and synchronizing data over the Internet and other data networks using XML documents and XRIs (Extensible Resource Identifiers), a URI-compatible abstract identifier scheme defined by the OASIS XRI Technical Committee. With XDI, data from any data source can be identified, described, linked, and synchronized into an active, machine-readable "dataweb" just as content from any content source can be identified and linked into the human-readable Web today.
category: ["Web Standards"]
tags: ["OASIS","XRIm","XDI","RDF","Dataweb"]
permalink: web-standards/oasis-open/xdi/xri-tc/
canonical_url: https://decentralized-id.com/web-standards/oasis-open/xdi/xri-tc/
last_modified_at: 2020-12-01
header: 
  image: /images/xdi-tc-header.webp
  teaser: /images/xdi-teaser.webp
toc: false
---

**[GitHub](https://github.com/OASIS-XDI-Technical-Committee/) • [OASIS XRI Data Interchange (XDI) TC](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=xdi)**

> The Technical Committee was closed by OASIS TC Administration on 05 October 2020 and is no longer active. Archives of its work remain publicly accessible and are linked from this page. OASIS appreciates the efforts of all those who participated in this TC.

* [OASIS Members Form XRI Data Interchange (XDI) Technical Committee](http://xml.coverpages.org/ni2004-01-21-b.html)
> A particular purpose of XDI is to allow the controls needed to mediate access and usage of shared data to be expressed as XDI links. These data sharing controls can govern authority, authentication, authorization, access control, usage control, transmission, synchronization, and rights management. The integration of such controls into a common, generalized data-oriented service can provide a new platform for trusted data sharing networks and applications."
* [OASIS TC Call For Participation: OASIS XDI TC](https://lists.oasis-open.org/archives/tc-announce/200401/msg00002.html) - Wed, *21 Jan 2004*
> The purpose of the OASIS XDI TC is to define a generalized, extensible, location-, application-, and transport-independent service for sharing, linking, and synchronizing data over the Internet and other data networks using XML documents and XRIs (Extensible Resource Identifiers), a URI-compatible abstract identifier scheme defined by the OASIS XRI Technical Committee. With XDI, data from any data source can be identified, described, linked, and synchronized into an active, machine-readable "dataweb" just as content from any content source can be identified and linked into the human-readable Web today.
* [OASIS XRI Data Interchange (XDI) TC - Charter](https://www.oasis-open.org/committees/xdi/charter.php)
> As a data sharing service, XDI is intended to be very simple and generalized, so it can be bound to any transport protocol offering basic primitives like HTTP or SMTP. Similarly, the XDI graph model is intended to be very simple and generalized, so it can carry data directly (serialized in XML, JSON, or other formats) or reference it externally (much as XML or HTML documents can carry content directly or reference it externally). Such a "lingua franca" for data interchange can solve many problems related to mapping and sharing of data and metadata across domains, directories, schemas, ontologies, applications, and languages (both human and machine).
>
> Though the potential uses of XDI are very broad, the scope of the OASIS XDI TC work is limited to defining the specifications required for it to interoperate successfully. This includes:
> 
> - Defining the XDI graph model for describing and linking XRI-identified resources and data.
> - Defining concrete serialization formats for this graph model.
> - Defining rules for XRI addressing of XDI documents and the graphs they contain independent of serialization format.
> - Defining an abstract XDI API consisting of logical operations on the XDI graph.
> - Defining bindings of this abstract API to concrete transport protocols such as HTTP, SMTP, SIP, and XMPP, and to invocation protocols such as SOAP, REST, and RMI.
> - Defining the semantics of XDI dictionaries — self-describing ontologies for use in XDI data sharing.
> - Defining the semantics of XDI link contracts — XDI documents used to govern the terms of XDI data sharing relationships.
> - Defining the semantics of other types of XDI graphs that fulfill general interoperability requirements of XDI infrastructure, e.g., context discovery, versioning, queries, etc.
> - Maintaining additional versions of these specifications as they evolve over time.
* [OASIS XRI Data Interchange (XDI) TC - FAQ](https://www.oasis-open.org/committees/xdi/faq.php)
> 1. **_What is XDI?_**\
> Specifically, XDI consists of three parts:
> - The **XDI Meta-Schema-a** very simple XML schema that uses XRIs (Extensible Resource Identifiers) developed by the OASIS XRI TC to describe and link data that may be in many other native formats, including other XML schemas.
> - **XDI Service**: a WSDL-defined protocol for exchanging data and metadata using XDI documents, together with bindings to different transport protocols (HTTP, SOAP, SMTP/MIME, etc.)
> - The **XDI Service Dictionary**: a set of pre-defined XDI resources for describing other XDI resources and controlling XDI data interchange using XDI link contracts (see below).
> 2. **_Is XDI a Web service?_**\
> XDI over SOAP is a Web service. However XDI can also be bound to HTTP for use in "RESTful" architectures, as well as to other transport protocols like SMTP/MIME. So strictly speaking XDI is a generalized service based on XML document exchange that can be implemented as a Web service.
> 3. **_What are the primary problems XDI is intended to solve?_**\
> The general problem XDI is designed to address is interoperable, automated data interchange across distributed applications and trust domains. There are many specific examples of this problem:
> - Exchange, linking, and lifetime synchronization of electronic business cards, public keys, and other common identity attributes across distributed directories (commonly known as dynamic address books).*
> - Internet calendar sharing.*
> - Trusted search (searches that need to cross multiple private websites).*
> - Auto-configuration and intelligent data synchronization across multiple user devices (desktop, laptop, PDA, land phone, cell phone, etc.)
> - Automated website registration, form-fill, and e-commerce transactions.
        Cross-domain security and privacy management.
> 4. **What is the Dataweb?**\
> The inspiration for XDI was the application of the architectural principles of the Web and XML to the problem of distributed data sharing. The result is called the Dataweb, as summarized in the table below:
> 
> | Principle | World Wide Web | Dataweb |
> |---|---|---|
> | 100% addressable resources | URIs |  XRIs |
> | Common representation and linking language | HTML | XDI Meta-Schema & XDI Service Dictionary | 
> | Common interchange protocol | HTTP | XDI/HTTP, XDI/SOAP |
> | Logical organization and navigation of resources | Website | Dataweb site |
> 
> In essence, the XDI meta-schema and protocol is to sharing and linking machine-readable data what HTML and HTTP are to sharing and linking human-readable content. In particular, Dataweb links are can define and control two-ways data sharing "pipes" between dataweb sites that can actively synchronize shared data when it changes, as illustrated below.
> 5. **Why is existing URI syntax not sufficient for cross-domain data sharing?**
> 
> While URIs in general, and HTTP URIs (commonly called URLs) in particular, have been spectacularly successful for building the Web, they are missing several features that are vital for cross-domain data sharing:
> 
> - HTTP URIs do not provide absolute addressability of data instances down to any level of containment or nesting-they work only to the page or page fragment level. While XPath provides additional addressing features for XML documents, it operates only relative to XML document roots and is not integrated with HTTP URI syntax.
> - HTTP URIs do not provide support for persistent addresses (the Dataweb equivalent of global foreign keys in databases). Other persistent URI schemes have been created, most notably the URN scheme, however they are not integrated with HTTP URI syntax and have not gained widespread adoption.
> - HTTP URIs do not provide addressability of resources across contexts, i.e., the ability to share identifiers across multiple websites in order to identify the same logical resource in multiple domains or physical locations. This is extremely useful for cross-domain data sharing.
* [The Dataweb: An Introduction to XDI](https://www.oasis-open.org/committees/download.php/6434/wd-xdi-intro-white-paper-2004-04-12.pdf) - A White Paper for the OASIS XDI Technical Committee v2, *April 12, 2004* 
> XDI (XRI Data Interchange) is a new service for generalized distributed data sharing and mediation usingXRIs (Extensible Resource Identifiers), a URI-compatible abstract identifier scheme developed by the OASIS XRI Technical Committee. The goal of XDI is to enable data from any data source to be identified, exchanged, linked, and synchronized into a machine-readable dataweb using XML documents just as content from any content source can linked into the human-readable Web using HTML documents today. Because the controls needed to mediate access and usage of shared data can be built right into every XDI link, the emergence of a global Dataweb has the potential to do for trusted data interchange what the Web did for open content exchange.
>
> This white paper presents several examples of classic cross-domain data sharing problems, explains how the Dataweb model can provide a generalized solution, and describes the key objectives of the newlyformed OASIS XDI Technical Committee ([http://www.oasis-open.org/committees/xdi](http://www.oasis-open.org/committees/xdi)). 
* [The Cover Pages topic on Data Sharing, Mediation, and Synchronization](http://xml.coverpages.org/dataSharing.html) Robin Cover's overview of the context in which XDI is being developed.
> sample references are being collected for a broad range of topics relating to Web architecture, including notions of resource/object identity, resource identification schemes, persistence, namespaces, naming authorities, registration authorities, name resolution, network protocols, content negotiation, bindings, resource description, metadata, addressing and linking, automated data synchronization, access control, trust management, etc.

## [OASIS XDI TC Technical Committee Wiki](https://wiki.oasis-open.org/xdi/)

> - [The XDI Graph Model](https://wiki.oasis-open.org/xdi/XdiGraphModel) - contains links to introductory materials explaining XDI and the XDI graph model
> - [XDI Design Goals](https://wiki.oasis-open.org/xdi/XdiDesignGoals) - The ten major design goals for the XDI graph model and semantic data interchange protocol
> - [XDI ABNF](https://wiki.oasis-open.org/xdi/XdiAbnf) - formal ABNF rules defining the XDI graph model
> - [XDI Serialization Formats](https://wiki.oasis-open.org/xdi/SerializationFormats) - the JSON serialization formats (and 2 text display formats) for XDI
> - [XDI Messages](https://wiki.oasis-open.org/xdi/XdiMessagePatterns) - the basic patterns for XDI messaging
> - [XDI Dictionaries](https://wiki.oasis-open.org/xdi/XdiDictionaryPatterns) - the basic patterns for XDI dictionary definitions
> - [XDI Signatures](https://wiki.oasis-open.org/xdi/XdiSignature) - the pattern for digitally signing or encrypting an XDI graph, including an XDI message
> - [XDI Link Contracts](https://wiki.oasis-open.org/xdi/LinkContractPattern) - how XDI does portable semantic authorization
> - [XDI Policy Expression](https://wiki.oasis-open.org/xdi/XdiPolicyExpression) - how XDI does semantic policy expression
> - [XDI Discovery](https://wiki.oasis-open.org/xdi/XdiDiscovery) - how XDI does P2P discovery of XDI endpoint URIs
> - [Glossary](https://wiki.oasis-open.org/xdi/Glossary) - terminology used throughout the XDI 1.0 specifications
> - [XDI Symbol Table](https://wiki.oasis-open.org/xdi/XdiSymbolTable) - summary of the symbols used in XDI syntax
> - [XdiDollarDictionary](https://wiki.oasis-open.org/xdi/XdiDollarDictionary) - a list of all proposed entries for the XDI $ dictionary
Informative Pages
> - [Informative](https://wiki.oasis-open.org/xdi/CategoryInformative) (NOT part of XDI 1.0 specs)

## [XDI 1.0 Specs List](https://wiki.oasis-open.org/xdi/XdiOneSpecs) - a list of the proposed XDI 1.0 specifications

[**OASIS-XDI-Technical-Committee/xdi-spec-docbook/xdi**](https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook/tree/master/xdi)

* [XDI Core V1.0](https://docs.oasis-open.org/xdi/xdi-core/v1.0/xdi-core-v1.0.html) Editors: Joseph Boyle; Markus Sabadello; Drummond Reed
  > The foundational spec on which all other specs depend. It defines the ABNF for the normative graph model, serialization formats, and addressing syntax.
* [XDI Messaging V1.0](https://raw.githubusercontent.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook/master/xdi/xdi-messaging-1.0/xdi-messaging-1.0-wd05.xml) Editors: Joseph Boyle; Markus Sabadello; Drummond Reed
* [XDI Bindings V1.0](https://raw.githubusercontent.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook/master/xdi/xdi-bindings-1.0/xdi-bindings-1.0-wd05.xml) Editors: Markus Sabadello; Drummond Reed; Joseph Boyle;
  > Defines the concrete binding of XDI messaging to specific transport protocols, beginning with the http/https protocol.
* [XDI Link Contracts V1.0](https://raw.githubusercontent.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook/master/xdi/xdi-link-contracts-1.0/xdi-link-contracts-1.0-wd03.xml) Editors: Dan Blum • Drummond Reed • Markus Sabadello 
  > Defines the standard structure and vocabulary of XDI authorization statements, including XDI link contracts and policy expressions, so they are portable across all XDI endpoints.
* [XDI Cryptography V1.0](https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook/blob/master/xdi/xdi-cryptography-1.0/xdi-cryptography-1.0-wd02.xml) Editors: Markus Sabadello
  > Defines the semantics of using digital signatures and encryption with XDI graphs and XDI messages.
* [XDI Discovery V1.0](https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook/blob/master/xdi/xdi-discovery-1.0/xdi-discovery-1.0-wd01.xml) Editors: Joseph Boyle • Les Chasen • Markus Sabadello • Drummond Reed
  > Defines P2P discovery of XDI endpoint URI(s) given an XDI address (or a discoverable identifier that can be transformed into an XDI address).
* [XDI Security Mechanisms V1.0](https://htmlpreview.github.io/?https://raw.githubusercontent.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook/master/xdi/xdi-security-mechanisms-1.0/xdi-security-mechanisms-1.0-wd01.html) Editors: Joseph Boyle • Peter Davis • Dan Blum
  > Describes the mechanisms for implementing security in XDI, including transport-level security, message-level security, encryption, token formats, etc.
* [XDI Privacy Mechanisms V1.0](https://github.com/OASIS-XDI-Technical-Committee/xdi-spec-docbook/blob/master/xdi/xdi-privacy-mechanisms-1.0/xdi-privacy-mechanisms-1.0-wd01.xml) Editors: Dan Blum • Peter Davis • Drummond Reed
  > This working draft describes an environment for writing and publishing an OASIS specification using DocBook XML. It is an internal OASIS support document and not the basis of an OASIS specification in and of itself.

