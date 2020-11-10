---
date: 2019-03-04
layout: single
title: "Decentralized Identity. Pre-history + resources for further exploration."
description: "As computers began to proliferate, concern grew over our lack of control over our personal information. Naturally arising through this concern, is to consider ways an individual might have ownership over their personal idenitifier that relates with our personal data."
excerpt: "These pages are loosely categorized by year and era. The date ranges, are somewhat arbitrary and not perfectly adhered to, and the headings are not perfect descriptors of those date ranges. Rather those are some major themes occuring within that time period."
permalink: /history/
cannonical_url: https://decentralized-id.com/history/
categories: ["History"]
tags: ["IETF","DPKI","PGP"]
last_modified_at: 2020-01-05
sidebar: 
  nav: didnav
classes: wide
---

**Ultimately, the idea is to put this all into some data-structure, and funnel this information into the identity-commons historical repository:**

[*Here is a community timeline that was created at IIW in 2011 & renewed at IIW 28 in 2019*](https://github.com/Identitywoman/identity-commons/blob/master/ID-History.md)

## Category Index

This history behind decentralized identity is loosely categorized by year and era. 

* [User Centric Identity - 2000-2009](/history/2000-2009/)
* [Personal Data Ecosystem - 2010-2014](/history/2010-2014)
* [Blockchain Identity - 2015-2019](/history/2015-2019/)

## Pre-History

* [Sovereignty in Historical Context for Self-Sovereign Identity](https://ssimeetup.org/sovereignty-historical-context-self-sovereign-identity-natalie-smolenski-webinar-18/) • [video](https://www.youtube.com/watch?v=eVDE_svZJD0)
  > This presentation reflects the first installment of a wider project examining the origins and potential of self-sovereign identity. While the term "self-sovereign identity" has become commonplace within digital identity circles and in the media, what it means in theory and in...
* [A short history of PKI](https://www.telekom.hu/static-tr/sw/file/PKI_tortenete_en.pdf)
  > The history of the research-development activity of PKI dates back to the renewal of postal and telegraph services at the end of the last century. The modernization was initiated by G·bor Baross, Minister of Commerce. In 1891 PKI was founded by a decree issued by the minister and was the second Post Office Research Station to open in Europe with the task of testing materials used in telegraph and telephone networks to introduce advanced equipment and provide high level services. Its staff included dr. Gyˆrgy BÈkÈsy, a physicist who worked for twenty years for the institute to earn undying merits in acoustics and ultimately to deserve the Nobel prize. In appreciation of its past the Institute, now the development centre of Magyar Telekom, Hungaryís leading telecommunications company, uses the abbreviation of its original name.
  > 
  > The Institute in 1891 was operating in the Main Office Building of the Hungarian Royal Post Office in P·rizsi Street, then in 1903 moved to the building of a telephone exchange in Nagymező utca. The Institute in 1912 moved in the building in Zombori utca where it operated for 88 years. Network planning activities from 1994 to 2000 were however carried out at a different place, in the former building of the Postal Network Planning Directorate, in RÛna utca.
* [Some Experience with File Transfer](https://tools.ietf.org/html/rfc269) - ??
* ["VERY DISTANT" HOST INTERFACE](https://tools.ietf.org/html/rfc263) - ??
* [IAB Recommended Policy on Distributing Internet Identifier Assignment](https://tools.ietf.org/html/rfc1174) and IAB Recommended Policy Change to Internet "Connected" Status
* [Oral History of Elizabeth (Jake) Feinler](https://web.archive.org/web/20110811175249/http://archive.computerhistory.org/resources/access/text/Oral_History/102702199.05.01.acc.pdf)
* [Establishing Identity Without Certification Authorities (1996)](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.31.7263) - Carl M. Ellison - CyberCash, Inc

### Losing Control Over our Personal Information

![](/images/chaum-security-without-identification-big-brother.png)

* [Security without Identification Transactions Systems to Make Big Brother Obsolete](https://www.cs.ru.nl/~jhh/pub/secsem/chaum1985bigbrother.pdf) - David Chaum, 1985. 
  > The large-scale automated transaction systems of the near future can be designed to protect the privacy and maintain the security of both individuals and organizations. Computerization is robbing individuals of the ability to monitor and control the ways information about them is used. As organizations in both the private and the public sectors routinely exchange such information, individuals have no way of knowing if the information is inaccurate, obsolete, or otherwise inappropriate. The foundation is being laid for a dossier society, in which computers could be used to infer individuals’ life-styles, habits, whereabouts, and associations from data collected in ordinary consumer transactions. Uncertainty about whether data will remain secure against abuse by those maintaining or tapping it can have a “chilling effect,” causing people to alter their observable activities. As computerization becomes mclre pervasive, the potential for these problems will grow dramatically.
  > 
  > [...]
  >
  > The solution is based on an individual’s ability to take a specially coded credential issued under one pseudonym and to transform it into a similarly coded form of the same credential that can be shown under the individual’s other pseudonyms. -[*Security without Identification*](https://www.chaum.com/publications/Security_Wthout_Identification.html)


#### Roger Clarke - Dataveillance

* [Information Technology and Dataveillance](http://www.rogerclarke.com/DV/CACM88.html)
  > The concept of 'dataveillance' is introduced, and defined as the systematic monitoring of people's actions or communications through the application of information technology. Dataveillance's origins are traced, and an explanation provided as to why it is becoming the dominant means of monitoring individuals and populations. The paper identifies, classifies and describes the various dataveillance techniques. It then examines the benefits, and especially the dangers, arising from dataveillance. It considers the intrinsic and extrinsic controls that act to keep the application of dataveillance under control, and suggests some appropriate policy measures.

### PGP - Web of Trust

[![](https://i.imgur.com/sMV9PE4.png)](https://www.philzimmermann.com/EN/essays/WhyIWrotePGP.html)

* Phil [Zimmerman creates PGP](https://www.philzimmermann.com/EN/essays/WhyIWrotePGP.html), 1991. 
  * First time strong encryption widely available to general public. 
  * PGP’s web-of-trust provide early foundation for SSI. However, PGP is known as difficult to use and failed to reach wide adoption for personal communication\identification.
* [Why I wrote PGP](https://www.philzimmermann.com/EN/essays/WhyIWrotePGP.html)
* [PGP -Web of Trust -linux.com](https://www.linux.com/learn/pgp-web-trust-core-concepts-behind-trusted-communication)
* [PGP Web of Trust: Core Concepts Behind Trusted Communication - Lin...](https://www.linux.com/learn/pgp-web-trust-core-concepts-behind-trusted-communication)
  > Public Key Cryptography infrastructure (PKI) has two main implementations. One is done using certificates and certificate authorities (CAs), and is described in the X.509 standard. It is best suited for structured organizational hierarchies with an implicitly trusted authorit...
* [The PGP Paradigm](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/topics-and-advance-readings/PGP-Paradigm.pdf). by Jon Callas and Philip Zimmermann
  > This chapter describes the mechanisms that PGP® software uses for its public key infrastructure. Much has written about PGP and practical public key cryptography. Much of this is to our opinion only mostly accurate. It is our goal in this chapter to describe the PGP models, as well as their implementation, standardization, and use. We also will put this in its historic and political context.

## resources

* [Identity Blog](http://www.identityblog.com)
* [History](http://wiki.idcommons.net/History) - wiki.idcommons.net
* [Identity Commons-History](http://wiki.idcommons.net/History) -wiki.idcommons.net
* [Identity Woman](https://identitywoman.net/)
* [IIW - Past Workshops](https://internetidentityworkshop.com/past-workshops/)
* [windley.com/tags/identity](http://www.windley.com/tags/identity.shtml)
* [Path to Self Sovereign Identity](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)
* [Web of Trust Info](https://github.com/WebOfTrustInfo/) - github
  > Shared repositories for #RebootingWebOfTrust Design Workshops - Web of Trust Info
* [The Evolution of Internet Identity](https://www.slideshare.net/prabathsiriwardena/the-evolution-of-internet-identity)
* [A Brief History of Digital Identity](https://medium.com/humanizing-the-singularity/a-brief-history-of-digital-identity-9d6a773bf9f5)
  > Many histories of digital identity start at the advent of the Internet, but the construction of name spaces is much older.
  >
  > Identity in our social systems is less concerned with encapsulating the human and more about the act of naming. As Silicon Valley’s Jared Dunn says in a moment of sad wisdom, “a name is just a sound that somebody makes when they need you.” The purpose of these names (or numbers) is to prove the uniqueness of a particular individual, to ensure accountability, and to establish some trust between individuals and institutions, to provide points of reference for the framework of laws and other social contracts that run our society.
* [Identity Management OSS Map](http://web.archive.org/web/20110207095948/docs.safehaus.org/display/HAUS/Id+OSS+Map) - web.archive.org
* [Vendor List](http://identityaccessmanagement.blogspot.com/2005/05/vendor-list.html) - identityaccessmanagement.blogspot.com
  > Updated: November 12 2006 I am trying to come up with the list of vendors and associated products in the Identity and Access Management ar...
* [Rebooting digital identity: how the social web is transforming citizen behaviours and expectations](https://www.slideshare.net/solutist/rebooting-digital-identity-how-the-social-web-is-transforming-citizen-behaviours-and-expectations) -  Slideshare - 2012
* [A Step Back in Time: The History and Evolution of Digital Identity](https://www.iotevolutionworld.com/iot/articles/410328-step-back-time-history-evolution-digital-identity.htm)
  > As Identity 3.0 continues to evolve, fascinating implementations and use cases are on the rise with the most talked-about frontier of the technological landscape: the Internet of Things (IoT).
* [Identity Trust Charter](http://wiki.idcommons.org/Identity_Trust_Charter)
  > To advocate and facilitate open (not closed) internet policy notices and terms that enable people to control personal information. Enabling a rich ecosystem of granualr controls to set personal information free from its current privacy prison.
  > 
  > Both Consent and Notice are primary tools online used to legally control and administer the flow of personal sharing and disclosure of information online. At this time this policy infrastructure is a relic of the industrial age, broken by surveillance capitalists, and not usable for privacy rights in context with identity management. 
  * [Influential Works](http://wiki.idcommons.org/Identity_Trust_Charter#Influential_Works_.26_Events)
    > Some Papers, Presentations & Hackathons: international privacy 

<iframe src="//www.slideshare.net/slideshow/embed_code/key/ujYqOXNEaaogEq" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> 
<strong> <a href="//www.slideshare.net/prabathsiriwardena/the-evolution-of-internet-identity">The Evolution of Internet Identity</a> </strong> from <strong> <a href="https://www.slideshare.net/prabathsiriwardena">Prabath Siriwardena</a> </strong> 

### open-standards

* [The Story of Open SSI Standards - Drummond Reed/Evernym - Webinar 1](https://ssimeetup.org/story-open-ssi-standards-drummond-reed-evernym-webinar-1/) • [video](https://www.youtube.com/watch?v=RllH91rcFdE) • [Self Sovereign Identity (SSI) Open standards with Drummond Reed](https://www.slideshare.net/SSIMeetup/self-sovereign-identity-ssi-open-standards-with-drummond-reed)
  > Drummond Reed, Chief Trust Officer at Evernym and Sovrin Foundation Trustee, features in our first Webinar "The Story of SSI Open Standards" by giving us the background on the foundation of Self Sovereign Identity.
* <a href="https://iiw.idcommons.net/Identity_Standards:_The_Soap_Opera_(catch_up_on_previous_episodes_%2B_review_major_plot_points">Identity_Standards: The_Soap Opera* - catch_up_on_previous episodes</a>

![](https://i.imgur.com/XtZQg0j.png)

![](https://i.imgur.com/FBe3S0w.png)

![](https://i.imgur.com/5R51G4Y.png)

![](https://i.imgur.com/xmWkc4l.png)
