---
date: 2020-12-01
title: XRI Technical Committee
description: Defining a syntax for abstract structured identifiers to share semantics across different URI schemes, domains, and applications (XRI); plus defining a simple XML format for uniform metadata discovery for all URIs (XRD)
excerpt: > 
    The purpose of this TC is to define a syntax for abstract structured identifiers -- identifiers that can be used within other URI schemes (such as http: and https: URIs) to share semantics across any number of domains and applications. The TC is also defining a simple XML descriptor format and HTTP(S) protocol for uniform resource metadata discovery.
category: ["Web Standards"]
tags: ["OASIS","XRI","XDI","Dataweb"]
last_modified_at: 2020-12-01
permalink: web-standards/oasis-open/xdi/xdi-tc/
canonical_url: https://decentralized-id.com/web-standards/oasis-open/xdi/xdi-tc/
toc: false
header: 
  image: /images/xri-tc-header.webp
  teaser: /images/xdi-teaser.webp

---

**[OASIS Extensible Resource Identifier (XRI) TC](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=xri)**

* [An Introduction to XRIs](https://docs.oasis-open.org/xri/xri/V2.0/xri-intro-V2.0.pdf)
  > - XRIs provide a uniform syntax and resolution protocol for both persistent and reassignable abstract identifiers. 
  > - XRIs provide a uniform syntax for delegating abstract identifiers between authorities at any level or context.
  > - XRIs provide a uniform syntax (called “cross-references”) for sharing abstract identifiers across all contexts.
  > - XRIs provide both a generic and a trusted protocol for resolving a single abstract identifier into any number of concrete identifiers.
  > - XRIs provide a simple, standard means of discovering URIs that may be associated with a resource, including those needed for additional metadata discovery.
  > - XRIs provide a standard means of protecting privacy by revealing the least possible information in an identifier and allowing an authority to control further access.
  > - XRIs provide a standard means of extension without sacrificing interoperability.   
* [XDI FAQ](https://www.oasis-open.org/committees/xdi/faq.php)
  > **_What features do XRIs have that URIs don't?_**
  > - **XRIs are "location-independent"** - the content of an XRI is decoupled from the network location of any data or services associated with the XRI. This means, among other things, that accessing a resource associated with an XRI isn't limited to a particular network location or protocol. (Most URI schemes in wide use today use identifiers that imply a close association to a network location or protocol.)
  > - **XRIs can assert persistence of all or parts of an identifier**. XRIs allow two types of separators (persistent and reassignable) between segments of an XRI, so the XRI can suggest that certain parts of the identifier are intended to be long-lived "primary keys" (a concept borrowed from database technology) and others are subject to change. Most URI schemes, on the other hand, are all-or-nothing. With URNs, for example, the entire identifier is persistent. With HTTP URIs, the entire identifier is potentially transient. The XRI scheme allows both characteristics to be combined in one federated identifier.
  > - **XRIs provide the ability to "contain" other URIs or XRIs in the form of cross-references**. Conceptually this is similar to using quote marks in English to talk about someone else's text. Cross references allow a well-defined URI or XRI to identify not only a concept or resource, but also to identify that concept or resource relative to another concept or resource. For example, a URI could identify a book, and an XRI could then identify a particular library's copies of the book by using that URI in a cross-reference appended to the library's XRI. So if " urn:isbn:0-131-10362-8" represents The C Programming Language by Kernighan and Ritchie, and "xri:@SeattlePublicLibrary" represents the Seattle Public Library, then "xri:@SeattlePublicLibrary/(urn:isbn:0-131-10362-8) " represents The C Programming Language in the context of the Seattle Public Library.
  > - **XRIs also support self-references**, a special form of cross-reference that indicates that an XRI is not intended to be resolved on the network but is intended solely as a unique identifier. For example, "xri:(@SeattlePublicLibrary/(urn:isbn:0-131-10362-8))" is a self-reference because it is entirely enclosed by parentheses, and as such represents the identifier itself.
  > - **XRIs allow unlimited delegation of namespaces**. While many URI schemes rely on DNS delegation, XRIs also have the ability to use abstract (non-DNS) names or identifiers that can contain a wider set of characters and strings. The XRI specification includes several global context symbols for this purpose (e.g., the "@" in "xri:@example/foo" represents a standard global namespace for organizations). In addition, a cross-reference can also serve as a namespace root, thus creating a private or community-based identifier space whose management is entirely community defined (for example, "xri:(http://www.example.com)/foo").
  > - **XRIs are fully internationalized**. XRI syntax builds on the W3C IRI (Internationalized Resource Identifier) specifications that adapt URIs to the Unicode character set.
* [Extensible Resource Identifier (XRI) Syntax V2.0](http://www.oasis-open.org/committees/download.php/5109/xri-syntax-resolution-1.0-cd.pdf) - Committee Specification, 14 November 2005 
  > Extensible Resource Identifiers (XRIs) provide a standard means of abstractly identifying a resource independent of any particular concrete representation of that resource—or, in the case of a completely abstract resource, of any representation at all.
  >
  > As shown in Figure 1, XRIs build on the foundation established by URIs (Uniform Resource Identifiers) and IRIs (Internationalized Resource Identifiers) as defined by [URI] and [IRI], respectively.\
  > ![](https://i.imgur.com/mq9znfO.png)\
  > The IRI specification created a new identifier by extending the unreserved character set to include characters beyond those allowed in generic URIs. It also defined rules for transforming this identifier into a syntactically legal URI. Similarly, this specification creates a new identifier, an XRI, that extends the syntactic elements (but not the character set) allowed in IRIs. To accommodate applications that expect IRIs or URIs, this specification also defines rules for transforming an XRI reference into a valid IRI or URI reference. 
* [Extensible Resource Identifier (XRI) Metadata V2.0](https://www.oasis-open.org/committees/download.php/11854/xri-metadata-V2.0-cd-01.pdf)
  > [XRISyntax] establishes five global context symbol (GCS) characters that may be used to begin an XRI authority segment for the purpose of expressing the abstract global context of an identifier. One of these GCS characters, "$", is reserved for identifiers for which the authority is a standards specification.
  > 
  > A second key XRI feature, cross-references (see section 2.2.2 of [XRISyntax]), allows XRIs to be embedded within other XRIs in order to share identifiers across contexts. This syntactic feature allows XRIs in the $ namespace to be used as metadata to describe an XRI itself. For example, the following XRI includes a cross-reference with version metadata.
  > ```
  > xri://@example*resource*($v/3)
  >                         \----/ cross-reference with XRI metadata
  > ```
  > The purpose of this specification is to define a set of XRIs in the $ namespace that function as identifier metadata—attributes that may be used describe an identifier itself, as opposed to attributes of the resource it identifies. This specification defines four such types of identifier metadata:
  > - Language metadata that specifies the human language in which an identifier is intended to be interpreted.
  > - Date/time metadata that specifies the point in time an identifier was established.
  > - Version metadata that specifies the identifier’s position in a sequence of identifiers for the same logical resource.
  > - Annotation metadata that allows XRI producers to add annotations to XRIs or XRI segments.
  > The definition of each metadata type also specifies comparison rules, significance in resolution, and any other special processing rules specific to that type. 
* [Extensible Resource Identifier (XRI) Resolution Version 2.0](https://docs.oasis-open.org/xri/xri-resolution/2.0/specs/cs01/xri-resolution-V2.0-cs-01.pdf)
  > Extensible Resource Identifier (XRI) provides a uniform syntax for abstract structured identifiers as defined in [XRISyntax]. Because XRIs may be used across a wide variety of communities and applications (as Web addresses, database keys, filenames, object IDs, XML IDs, tags, etc.), no single resolution mechanism may prove appropriate for all XRIs. However, in the interest of promoting interoperability, this specification defines a simple generic resource description format called XRDS (Extensible Resource Descriptor Sequence), a standard protocol for requesting XRDS documents using HTTP(S) URIs, and standard protocol for resolving XRIs using XRDS documents and HTTP(S) URIs. Both generic and trusted versions of the XRI resolution protocol are defined (the latter using HTTPS [RFC2818] and/or signed SAML assertions [SAML]). In addition, an HTTP(S) proxy resolution service is specified both to provide network-based resolution services and for backwards compatibility with existing HTTP(S) infrastructure. 
  > 
  > | Resolution Component | DNS Architecture | XRI Architecture |
  > | --- | --- | --- |
  > | Identifier | domain name |  XRI (authority + path + query) | 
  > | Resource record format | text (resource record) |  XML (XRDS document) |
  > | Attribute identifier | string | anyURI |
  > | Network endpoint identifier | IP address | URI | 
  > | Synonyms | CNAME | LocalID, EquivID, CanonicalID, CanonicalEquivID | 
  > | Primary resolution protocol | UDP | HTTP(S) | 
  > | Trusted resolution options | DNSSEC | HTTPS and/or SAML | 
  > | Resolution client | resolver | resolver | 
  > | Resolution server | authoritative nameserver | authority server | 
  > | Recursing resolution | recursing nameserver | recursing authority server or proxy resolver | 

## i-names

* [inames](https://web.archive.org/web/20150801134550/http://inames.net/)
  > URLs are for connecting web pages. Now get the address for connecting people and businesses in rich, long-lasting digital relationships: i-names.
* [http://dev.inames.net/wiki/Main_Page](https://web.archive.org/web/20111001110114/http://dev.inames.net/wiki/Main_Page)
  > The goal of this wiki is to be a portal for everything XRI and i-names developers need to know to integrate i-names and XRI infrastructure into their identity-enabled sites, services, and applications. Please let us know via the About Us page if you don't find what you are looking for, or just add a request directly to the wiki.
* [I Names](https://en.wikipedia.org/wiki/I-name)
  > I-names are one form of an XRI — an OASIS open standard for digital identifiers designed for sharing resources and data across domains and applications.[1] I-names are human readable XRIs intended to be as easy as possible for people to remember and use. For example, a personal i-name could be =Mary or =Mary.Jones. An organizational i-name could be @Acme or @Acme.Corporation.
