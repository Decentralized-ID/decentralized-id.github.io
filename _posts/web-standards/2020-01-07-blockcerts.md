---
date: 2020-01-07
title: Blockcerts
description: "Open Standard for Blockchain Certificates"
excerpt: >
  Blockcerts is an open standard for building apps that issue and verify blockchain-based official records. These may include certificates for civic records, academic credentials, professional licenses, workforce development, and more.

  Blockcerts consists of open-source libraries, tools, and mobile apps enabling a decentralized, standards-based, recipient-centric ecosystem, enabling trustless verification through blockchain technologies.
header:
  image: /images/blockcerts-header.webp
permalink: /web-standards/blockcerts/
redirect_from: 
  - /blockchain/bitcoin/blockcerts/
  - /specs-standards/blockcerts/
categories: ["Web Standards"]
tags: ["Bitcoin","Learning Machine","BTCR","Blockchain"]
last_modified_at:  2020-01-07
---

## Learning Machine

[The Digital Identity Problem Space](https://www.learningmachine.com/digital-identity/)
  > A framework for organizing the categories of digital identity and an analysis of where disruptive innovation is most likely to succeed.
* [Learning Machine](https://www.learningmachine.com/)
* [Natalie Smolenski - Author, Speaker](https://www.nataliesmolenski.com/)
  > Natalie Smolenski is an anthropologist leading business development for blockchain technology firm Learning Machine. She writes and speaks about identity, tech, and government.

## Blockcerts

* [Blockcerts](https://www.blockcerts.org/)  - [Forum](http://community.blockcerts.org/) - [Github](https://github.com/blockchain-certificates) - [Twitter](https://twitter.com/blockcerts)
    > open standard for issuing and verifying blockchain-based official records; The project offers  open-source libraries, tools, and mobile apps. MIT has [issued](https://www.insidehighered.com/news/2017/10/19/mit-introduces-digital-diplomas) digital certificates based on this standard.
  
* [Introduction](https://www.blockcerts.org/guide/)
  > Blockcerts is an open standard for building apps that issue and verify blockchain-based official records. These may include certificates for civic records, academic credentials, professional licenses, workforce development, and more.
  > 
  > Blockcerts consists of open-source libraries, tools, and mobile apps enabling a decentralized, standards-based, recipient-centric ecosystem, enabling trustless verification through blockchain technologies.
  > 
  > Blockcerts uses and encourages consolidation on open standards. Blockcerts is committed to self-sovereign identity of all participants, and enabling recipient control of their claims through easy-to-use tools such as the certificate wallet (mobile app). Blockcerts is also committed to availability of credentials, without single points of failure.

![]({{ site.baseurl }}/images/blockcerts.webp)

* [Academic Credentialing and the Blockchain](https://www.learningmachine.com/academic-credentialing-blockchain/)
* [Blockcerts — An Open Infrastructure for Academic Credentials on the Blockchain](https://medium.com/mit-media-lab/blockcerts-an-open-infrastructure-for-academic-credentials-on-the-blockchain-899a6b880b2f)
* [Top 10 Reasons to Use Blockcerts](https://medium.com/learning-machine-blog/top-10-reasons-to-use-blockcerts-ec7d29f2712c)
  > The open standard for issuing blockchain-based records is your easiest bet for creating records that remain verifiable for a lifetime.
* [A Decentralized Approach to Blockcerts Credential Revocation](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/blockcerts-revocation.md)
  > The initial release of the Blockcerts standard and reference implementation described only one revocation mechanism, the issuer-hosted revocation list approach also used by Open Badges. This has known limitations, including: centralization, single point of failure, and inability for a recipient to revoke. Other approaches to revocation were considered, but none were technically or economically feasible at the time given the project goals, including Bitcoin blockchain anchoring, low overhead, and minimal cost.

### Open Badges
* [Badges and Blockcerts](https://www.learningmachine.com/badges-and-blockcerts/)
  > In education and workforce development, it’s important to understand the differences between digital credential formats and how to combine them for greatest impact.
  > ...
  > 2011 saw the birth of Open Badges, which digitally and visually convey the achievement of a specific skill. Similar to the Scouts movement, which uses a small fabric symbol to represent specific achievements, digital badges were designed to convey a singular achievement through a digital image and a hosted set of data. Initially spearheaded by the Mozilla Foundation, the Open Badges standard is now maintained by the IMS Global Learning Consortium, ensuring interoperability between platforms.
  > ...
  > In response to the desire for high-stakes credentials in a digital format, the development of Blockcerts began in 2015 as part of a project by the MIT Media Lab.
* [Open Badges are Verifable Credentials](https://nbviewer.jupyter.org/github/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/open-badges-are-verifiable-credentials.pdf)
  > The Blockcerts Open Badges Draft Extension introduced a verifcation method based on those used by Verifable Credentials for the specifc use case of blockchain-anchored credentials. This paper expands that work and proposes a new option that can reside alongside existing Open Badges verifcation methods.
* [OPEN BADGES ON THE BLOCKCHAIN](https://draftin.com/documents/1138961?token=hQ5q0mCHizZum8-pkDFYUZr4YFYOWMN01BPT-5uX00hAaGxYOAlgAlhyenat76hjNpTCs-CMWPI38KWn_omp0Oc)
  > This document gives an overview of the status, interesting companies and people regarding Verifiable Open Badges on the Blockchain. 

![]({{ site.baseurl }}/images/blockcerts.webp)

## Literature

* [Healthcare and Digital Credentials: Technical, Legal, and Regulatory Considerations](http://www.fsmb.org/siteassets/digital-credentials/digital-credentials-report-june-2019.pdf)
* [Security analysis of a blockchain-based protocol forthe certification of academic credentials](https://arxiv.org/pdf/1910.04622.pdf) by Marco Baldi, Franco Chiaraluce, Migelan Kodra and Luca Spalazzi
  > Abstract—We consider a blockchain-based protocol forthe certification of academic credentials named Blockcerts,which is currently used worldwide for validating digitalcertificates of competence compliant with the Open Badgesstandard. We study the certification steps that are per-formed by the Blockcerts protocol to validate a certificate,and find that they are vulnerable to a certain typeof impersonation attacks. More in detail, authenticationof the issuing institution is performed by retrieving anunauthenticated issuer profile online, and comparing somedata reported there with those included in the issuedcertificate. We show that, by fabricating a fake issuerprofile and generating a suitably altered certificate, anattacker is able to impersonate a legitimate issuer andcan produce certificates that cannot be distinguished fromoriginals by the Blockcerts validation procedure. We alsopropose some possible countermeasures against an attackof this type, which require the use of a classic public keyinfrastructure or a decentralized identity system integratedwith the Blockcerts protocol.

<center><iframe src="//www.slideshare.net/slideshow/embed_code/key/rVC25i8FzeTPiw" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> </center>

[Blockcerts: The Open Standard for Blockchain Credentials](https://www.slideshare.net/SSIMeetup/blockcerts-the-open-standard-for-blockchain-credentials) - [SSI-Meetup – Webinar 39](https://ssimeetup.org/blockcerts-open-standard-blockchain-credentials-daniel-paramo-anthony-ronning-webinar-39/)

## Adoption

* [MIT Launches Blockcerts Certification Using Bitcoin](https://news.bitcoin.com/mit-blockcerts-certification-bitcoin/) (10/2016)
  > The MIT Media Lab project has already deployed a few instances of blockchain-based digital certificate verification. In October of 2015, the group issued certificates to Media Lab alumni who attended the Lab’s 30th anniversary. The organization Learning Machine also issued HR certificates to employees. MIT’s Global Entrepreneurship Bootcamp workshop in Seoul, South Korea in March 2016 published digital verification using the system. Lastly, Laboratorio para la Ciudad issued digital certificates to workshop participants in Mexico City in September 2015.
* [education.gov.mt - Blockcerts Public Key Registry](https://education.gov.mt/en/Blockcerts/Pages/Blockcerts-Public-Key-Registry.aspx)
* [MIT Introduces Digital Diplomas](https://www.insidehighered.com/news/2017/10/19/mit-introduces-digital-diplomas)
* [CXC (Carribean) Pilots E-Certificates on the Blockchain](https://www.cxc.org/cxc-pilots-e-certificates-on-the-blockchain/)

### Cowcerts

{% include video id="3UvDv7OXsFs" provider="youtube" %}

* [Verifiable credentials using blockchain](https://www.cowstamp.com/) ([twitter](https://twitter.com/cowcerts)) ([gitlab](https://gitlab.com/cowcerts/))
  > Create, issue and receive verifiable credentials registered using blockchain technologies in a user-friendly fashion 
* [Cowcerts for Education](https://cowcerts.readthedocs.io/en/develop/edu/index.html) - Cowcerts for Education provides a data model for digital certificates to prove that someone has completed their education successfully.
  > * provides extensions to the following base standards:
  >   * [Open Badges](https://openbadgespec.org/) standard
  >   * [Blockcerts](https://blockcerts.org/) standard
* [cowcerts/schemas/](https://gitlab.com/cowcerts/schemas)
  > Specifications, JSON Schemas and JSON Linked Data definitions for Cowcerts certificates [https://cowcerts.dev](https://cowcerts.dev)

## GitHub Repositories

* [blockchain-certificates/blockchain-certificates.github.io](https://github.com/blockchain-certificates/blockchain-certificates.github.io) - Web site. 
* [learningmachine/stage.blockcerts.github.io](https://github.com/learningmachine/stage.blockcerts.github.io)
* [blockchain-certificates/blockcerts-playground.github.io](https://github.com/blockchain-certificates/blockcerts-playground.github.io) - In-browser tool to experiment with Blockcerts. 

---

* [learningmachine/Foundatio](https://github.com/learningmachine/Foundatio) Pluggable foundation blocks for building distributed apps.
* [blockchain-certificates/pyld](https://github.com/blockchain-certificates/pyld) - JSON-LD processor written in Python. 
* [learningmachine/polymer-redux](https://github.com/learningmachine/polymer-redux)
  > An example use-case to showcase the state/view abstraction in Polymer 3, LitElement and Redux context
* [blockchain-certificates/assets](https://github.com/blockchain-certificates/assets)
* [blockchain-certificates/archived-cert-store](https://github.com/blockchain-certificates/archived-cert-store)
  > Storage library and service for Blockchain Certificates
* [blockchain-certificates/PodSpecs](https://github.com/blockchain-certificates/PodSpecs)
  > A listing of CocoaPod .podspec files for all pods created in the Blockchain Certificates project.

### Issuing

* [blockchain-certificates/cert-schema](https://github.com/blockchain-certificates/cert-schema)
  > The schema for Blockcerts. 
* [blockchain-certificates/cert-issuer](https://github.com/blockchain-certificates/cert-issuer) - Issues Blockcerts using either the Bitcoin or Ethereum blockchain
* [blockchain-certificates/cert-tools](https://github.com/blockchain-certificates/cert-tools)
  > Command line tools for designing certificate templates and instantiating a certificate batch
* [blockchain-certificates/obi-baking](https://github.com/blockchain-certificates/obi-baking) 
  > Example of baking a blockcert into an Open Badge. 
* [blockchain-certificates/cert-core](https://github.com/blockchain-certificates/cert-core)
* [blockchain-certificates/wallet-test-resources](https://github.com/blockchain-certificates/wallet-test-resources)
  > These are resources used to test implementations of the evolving blockcerts certificate standard and issuer conventions.

### Validation

* [learningmachine/ajv](https://github.com/learningmachine/ajv)
  > The fastest JSON-Schema Validator. Supports draft-06
* [blockchain-certificates/openbadges-validator-core](https://github.com/blockchain-certificates/openbadges-validator-core) - Open Badges validation in python. 


### Verification

* [blockchain-certificates/blockcerts-verifier](https://github.com/blockchain-certificates/blockcerts-verifier) - A Blockcerts verifier and viewer. 
* [blockchain-certificates/cert-verifier](https://github.com/blockchain-certificates/cert-verifier)
Python library for verifying Blockcerts. 
* [blockchain-certificates/cert-verifier-js](https://github.com/blockchain-certificates/cert-verifier-js) - Javascript library for verifying Blockcerts Certificates

### Web

* [blockchain-certificates/cert-web-component](https://github.com/blockchain-certificates/cert-web-component) - A web component for displaying blockchain certificates.
* [blockchain-certificates/cert-viewer](https://github.com/blockchain-certificates/cert-viewer) - A web app for viewing and validating Blockchain Certificates

### Mobile

* [blockchain-certificates/wallet-android](https://github.com/blockchain-certificates/wallet-android) - An Android app for Blockcerts. 
* [blockchain-certificates/BlockcertsFramework-iOS](https://github.com/blockchain-certificates/BlockcertsFramework-iOS) - An iOS wallet for viewing, validating, and sharing certs
* [blockchain-certificates/wallet-iOS](https://github.com/blockchain-certificates/wallet-iOS) - An iOS wallet for Blockcerts. 
