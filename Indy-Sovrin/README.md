# Awesome Hyperledger Indy Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) 
<a href="https://infominer.id"><img src="https://infominer.id/images/infominer.png" align="right" width="150" height="140"></a>
**Protocol, Governance, Education, Ecosystem** 

This page contains a growing collection of educational resources related to Evernym, the Sovrin Foundation, and Hyperledger Indy. It was born from [/awesome-decentralized-id](../README.md) and contains some of the same material, but is quite exhaustive. As a result, I decided to split this list off to focus on learning about Hyperedger Indy, the Sovrin Foundation, adn Evernym. Its an index for training, developers, students, end users, investors, and enterprise to more easily navigate the digital identity landscape enabled by Hyperledger Indy.
 
Since the information is all inter-related, there is some overlapp. Skipping back and forth may be required, depending on your particular interests. 

**[Pull Requests](https://github.com/infominer33/awesome-decentralized-id/blob/master/contributing.md) and\or [Contributions](#brought-to-you-by-the-crypto-librarysuper-source) Welcome**


![](https://i.imgur.com/KFmYHQ6.png)

## Contents

* [Introduction](#introduction-)
  * [Link Shorthand](#link-shorthand-)
* [Self Sovereign Identity—SSI](#self-sovereign-identity-)
* [Evernym](#evernym-)
* [The Sovrin Foundation](#the-sovrin-foundation-)
  * [Sovrin Stewards](#sovrin-stewards-)
  * [Selected Articles Windley.com](#selected-articles-windleycom-)
* [Hyperledger Indy](#hyperledger-indy-)
  * [Additional Indy Related](#additional-indy-related-)
  * [Wallets](#wallets-)
  * [Zero Knowledge Proof in Indy](#zero-knowledge-proofs-in-indy-)
* [W3C and DID Related Standards](#w3c-and-did-related-standards--)
  * [DID the Decentralized Identifier](#did-the-decentralized-identifier--)
  * [DID Auth](#did-auth-) 
  * [Verifiable Claims](#verifiable-claims-)
  * [Decentralized Key Management (Agents)](#decentralized-key-management-agents-)
* [GDPR](#eu-general-data-protection-regulation-act--)
* [Research Papers](#research-papers--)
* [Reports](#reports--)
* [Videos](#video--)
* [Podcasts](#podcasts--)
* [Sources](#sources--)

## Introduction [**^**](#Contents)

Internet Identity Workshop is where the quest for concious, user-centric, identity began. Rebooting Web-of-Trust Workshops sprung from the IIW, focused on creating standards for DPKI. Among the United Nations 'Sustainable Development Goals' is for all the world to have access to a digital identity by 2030. Around 2016, the SDGs, blockchain, and the GDPR converged bringing much energy to the decentralized identity ecosystem. 

**Additional history and related information may be found at [/awesome-decentralized-id](../README.md#Contents)**.

## Link Shorthand [**^**](#Contents)
[[**T**](#Link-Shorthand)]witter • [[**G**](#Link-Shorthand)]ithub • [[**B**](#Link-Shorthand)]log • [[**wp**](#Link-Shorthand)] whitepaper • [[**D**](#Link-Shorthand)]ocumentation • [[**F**](#Link-Shorthand)]orums • [[**C**](#Link-Shorthand)]hat • [[**tele**](Link-Shorthand)]gram • [[**web**](Link-Shorthand)]site
• [[**ϟ**](#Link-Shorthand)] related resource • [[**>**](#Link-Shorthand)] related section • [[**>>**]()] related section on awesome-decentralized-id • [[**^**](#Link-Shorthand)] back to the contents. 

![](https://imgur.com/3zz62kpl.png)




### The Sovrin Foundation [**^**](#Contents)

![](https://www.evernym.com/wp-content/uploads/2017/04/logo-large.png)

* [[**F**](https://forum.sovrin.org/)]orum • [[**C**](https://chat.sovrin.org/)]hat • [[**T**](https://twitter.com/SovrinID)]witter • [[**G**](https://github.com/sovrin-foundation/sovrin)]ithub • [[**tele**](https://t.me/sovrin_foundation)]gram • [[**web**](https://sovrin.org/)]site
* [Founded](http://www.windley.com/archives/2016/09/announcing_the_sovrin_foundation.shtml) in [September](https://www.prnewswire.com/news-releases/sovrin-foundation-launches-first-dedicated-self-sovereign-identity-network-300336702.html) 2016, The [Sovrin](https://sovrin.org/)
 Foundation is creating a public instance of the Sovrin\Indy codebase; initially developed by [Evernym](#Evernym)
* [Sovrin Library](https://sovrin.org/library/)
* [Getting Started with Sovrin](https://sovrin.org/library/getting-started-with-sovrin/)
* [Sovrin: A Protocol and Token for Self-Sovereign Identity and Decentralized Trust](https://sovrin.org/wp-content/uploads/Sovrin-Protocol-and-Token-White-Paper.pdf)
* [Sovrin Network: What Goes on the Ledger?](https://sovrin.org/wp-content/uploads/2018/10/What-Goes-On-The-Ledger.pdf)
* [Sovrin Governance Framework](https://sovrin.org/library/sovrin-governance-framework/)
* [How Sovrin Works: A Technical Guide from the Sovrin Foundation](https://sovrin.org/wp-content/uploads/2018/03/How-Sovrin-Works.pdf) [[**ϟ**](https://sovrin.org/wp-content/uploads/AnonCred-RWC.pdf)]
* [Sovrin Test Network Trust Anchor Registration](https://s3.us-east-2.amazonaws.com/evernym-cs/sovrin-STNnetwork/www/trust-anchor.html)[[**F**](https://forum.sovrin.org/t/testing-on-the-sovrin-test-network-stn/643/17)]
* [Sovrin Main Net Outage, December 2018](https://forum.sovrin.org/t/sovrin-main-net-outage-december-2018/1010)
  > The Sovrin Main Network experienced an outage lasting from Saturday 2018-12-08 until Tuesday 2018-12-11. This was our first significant outage of the network. This post describes the incident, how it was addressed, and what we are doing to prevent future incidents and improve our responses.
  * [Sovrin Status Twitter](https://twitter.com/sovrin_status)


#### Sovrin Stewards [**^**](#Contents)

The Sovrin ledger is operated by Stewards, trusted organizations within the ecosystem who have agreed to abide by the requirements in the [Sovrin Trust Framework](https://sovrin.org/library/sovrin-governance-framework/) and are responsible for operation the nodes that maintain the Sovrin distributed ledger.

Stewards also, as a group, accept or reject any changes to the ledger-specific portions of the Sovrin open source code by virtue of that role. They thus provide a counterbalance to the Sovrin architects who maintain the Indy code base.

[Aalto University](http://www.aalto.fi/en/) 
• [Absa Group Limited](https://www.absa.africa/absaafrica/) 
• [Amihan Global Strategies](https://amihan.net/) 
• [ARTiFACTS](https://artifacts.ai/) 
• [Attinad Software](http://attinadsoftware.com/) 
• [ATB Financial](http://www.atb.com/Pages/default.aspx) 
• [Best Innovation Group](http://www.big-fintech.com/) 
• [BakerHostetler](https://www.bakerlaw.com/) 
• [Cisco](https://www.cisco.com/) 
• [Certisign](http://www.certisign.com.br/) 
• [Crypto Valley Association](https://cryptovalley.swiss/) 
• [CULedger](http://culedger.com/) 
• [Danube Tech](https://danubetech.com/) 
• [Datum](https://datum.org/) 
• [Desert Financial Credit Union](https://www.desertschools.org/business) 
• [Digicert](https://www.digicert.com/) 
• [Digital Bazaar](https://digitalbazaar.com/) 
• [estatus AG](https://www.esatus.com/) 
• [Evernym](https://www.evernym.com/) 
• [European Business Process Institute](https://ebpi.nl/en/home/) 
• [Finicity](https://www.finicity.com/) 
• [First Education Credit Union](https://www.firstedfcu.com/) 
• [Global Consent](http://www.consent.global/) 
• [IBM](https://www.ibm.com/blogs/blockchain/2018/08/ibm-blockchain-trusted-identity-sovrin-steward-closed-beta-offering/) 
• [InfoCert](https://infocert.digital/) 
• [iRespond](https://irespond.org/) 
• [KYC Chain](https://kyc-chain.com/) 
• [lab10 collective](https://lab10.coop/en/) 
• [OAS Staff Federal Credit Union](https://www.oasfcu.org/en/default.asp) 
• [Perkins Cole](https://www.perkinscoie.com/) 
• [ProSapien](https://www.prosapien.com/) 
• [Qiy Foundation](https://www.qiyfoundation.org/) 
• [Royal Credit Union](https://www.rcu.org/) 
• [SICPA](https://www.sicpa.com/) 
• [SITA](https://www.sita.aero/) 
• [Spark New Zealand](http://www.sparknz.co.nz/) 
• [Swisscom Blockchain](https://blockchain.swisscom.com/)
• [T-Labs](https://laboratories.telekom.com/) 
• [The City of Osmio](https://osmio.ch/) 
• [TNO](https://www.tno.nl/en/) 
• [Truu](https://www.truu.id/) 
• [TwinPeek](https://twinpeek.net/) 
• [Tykn](https://tykn.tech/) 
• [Veridium](https://veridiumid.com/)

#### Selected articles Windley.com [[**^**](#Contents)]

* [windley.com/tags/sovrin](http://www.windley.com/tags/sovrin)
* [An Internet for Identity](http://www.windley.com/archives/2016/08/an_internet_for_identity.shtml)
* [A Universal Trust Framework](http://www.windley.com/archives/2017/01/a_universal_trust_framework.shtml)
* [Building Your Business on Sovrin: Domain-Specific Trust Frameworks](http://www.windley.com/archives/2018/03/building_your_business_on_sovrin_domain-specific_trust_frameworks.shtml)
* [The Sovrin Foundation](http://www.windley.com/archives/2018/07/the_sovrin_foundation.shtml)
* [Decentralization in Sovrin](http://www.windley.com/archives/2018/10/decentralization_in_sovrin.shtml)
* [Self-Sovereign Identity and the Legitimacy of Permissioned Ledgers](http://www.windley.com/archives/2016/09/self-sovereign_identity_and_the_legitimacy_of_permissioned_ledgers.shtml)
* [The Sovrin Ecosystem](http://www.windley.com/archives/2018/11/the_sovrin_ecosystem.shtml) (Disambiguating between Evernym, Sovrin, and Indy)



### Hyperledger Indy [**^**](#Contents)

![](https://www.osiztechnologies.com/asset/oimages/hyperledger_indy/hyperledger_indy_02.png)

![](https://imgur.com/2LWlrgvl.png)\
<sup><a href="https://www.edx.org/course/blockchain-for-business-an-introduction-to-hyperledger-technologies">Linux Foundation -Blockchain for Business -INDY</a></sup>

* [Hyperledger Indy - *Distributed Ledger and Utility Library*](https://www.hyperledger.org/projects/hyperledger-indy) [[**T**](https://twitter.com/Hyperledger)] [[**C**](https://chat.hyperledger.org)]
* [Indy Documentation Index - wiki.hyperledger.org](https://wiki.hyperledger.org/projects/indy/documentation)
  * [indy.readthedocs.io](https://indy.readthedocs.io/) (under construction)
  * [Indy Docs Framwork](https://github.com/hyperledger/indy-hipe/tree/master/text/0025-indy-docs-framework)
* [Introduction to Hyperledger Indy](https://github.com/hyperledger/education/blob/master/LFS171x/docs/introduction-to-hyperledger-indy.md) (awesome resource from hyperledger github)
* [Hyperledger Indy — the Future of Decentralized Identity](https://www.axiomtech.io/blog-feed/hyperledger-indy-decentralized-identity)
* [Hyperledger Welcomes Project Indy](https://www.hyperledger.org/blog/2017/05/02/hyperledger-welcomes-project-indy) - ANN
* [The Rise of Self-Sovereign Identity - Hyperledger Indy](https://wso2.com/blog/research/the-rise-of-self-sovereign-identity-hyperledger-indy)
* [Ernesto.net - What goes on the Ledger](https://www.ernesto.net/ernesto-net-5-minute-course-on-indy-and-what-goes-on-the-blockchain-ledger/)
* [Ernesto.net - Hyperledger Indy Architecture](https://www.ernesto.net/hyperledger-indy-architecture/)
* [github.com/IBM-Blockchain-Identity](https://github.com/IBM-Blockchain-Identity) (Docker based tutorial sandbox env)
* The Linux Foundation's [Blockchain for Business](https://www.edx.org/professional-certificate/linuxfoundationx-blockchain-for-business) course may be freely audited and has a section about Indy.
* [Blockchain development made easy: Getting started with Hyperledger Indy](https://jaxenter.com/hyperledger-indy-interview-hardman-148796.html) - Interview with Daniel Hardman[[**G**](https://github.com/dhh1128)][[**L**](https://www.linkedin.com/in/danielhardman/)][[**T**](https://twitter.com/dhh1128)], Hyperledger Indy maintainer

<img src="https://i.imgur.com/a0dpDtr.png"/>


#### Additional Indy Related [**^**](#Contents) 
* [Hyperledger Identity Working Group-paper](https://docs.google.com/document/d/1ExFNRx-yYoS8FnDIUX1_0UBMha9TvQkfts2kVnDc4KE/edit#heading=h.7noli5fp1i70)
* [HyperledgerIndyWGCall_2018-12-06](https://drive.google.com/file/d/1166XpTM8WgZVMN2ca53CRCJapZlAeUhM/view) Discussion of VON and Plenum Docs (w info-graphics)
* [A Framework for Designing Cryptographic Key Management Systems](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-130.pdf) 
* [An Accumulator Based on Bilinear Maps and Efficient Revocation for Anonymous Credentials](https://eprint.iacr.org/2008/539.pdf)
* [An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation](https://www.iacr.org/archive/eurocrypt2001/20450093.pdf)
* [sovrin-foundation/connector-app](https://github.com/sovrin-foundation/connector-app) - Reference mobile edge agent for use with the Sovrin Network built from Hyperledger Indy.
* [Building binaries of LibIndy for Android](https://github.com/hyperledger/indy-sdk/blob/master/doc/android-build.md)
* [HIPE 0014-ssi-notation](https://github.com/hyperledger/indy-hipe/tree/master/text/0014-ssi-notation)
* [Set up Indy Pool in Local Linux Environment Using Docker](https://medium.com/@smaldeniya/setup-hyperledger-indy-pool-in-local-linux-environment-using-docker-304d13eb86dc)
* [Learn how to set up a DEV Environment with Vagrant on Hyperledger Indy!](https://github.com/hyperledger/indy-node/blob/master/environment/vagrant/sandbox/DevelopmentEnvironment/Virtualbox/Vagrantfile)
* [Semantics Working Group Shared Docs](https://drive.google.com/drive/u/0/folders/1zkXr--0DG7I1k62vaFuotEzIaTIUH0ou?ogsrc=32)
  * [Verifiable Credentials, Schema and Overlays- Overview Decks](https://drive.google.com/drive/u/0/folders/1UxLLugRQKuV8Mdvv_X9Y6ty4szSi5ZNU?ogsrc=32)
* [Indy August Update](https://wiki.hyperledger.org/groups/tsc/project-updates/indy-2018-aug) - Most recent report from the Hyperledger Indy team.


#### Wallets [**^**](#Contents)

* [How to build a Self Sovereign Identity Wallet](https://www.devteam.space/blog/how-to-build-a-self-sovereign-identity-wallet/)
* https://github.com/streetcred-id/indy-sdk-storage

#### Zero Knowledge Proofs in Indy [**^**](#Contents)
<a href="https://www.slideshare.net/eralcnoslen/privacypreserving-authentication-another-reason-to-care-about-zeroknowledge-proofs"><img src="https://i.imgur.com/LAUkkbN.png"/><br/><sup>Privacy Preserving Authentication—Another reason to care about ZKP</sup></a>

* [The Sovrin Network and Zero Knowledge Proof](https://sovrin.org/the-sovrin-network-and-zero-knowledge-proofs/) - high level walk through
* [AnonCreds: Anonymous credentials protocol implementation in python](https://github.com/hyperledger/indy-anoncreds) [[**ϟ**](https://github.com/hyperledger/indy-anoncreds/blob/master/docs/anoncred-usecase1.pdf)]
  * [Relationship Diagram](https://github.com/hyperledger/indy-node/blob/master/docs/relationship-diagram.png)
* [Zero-Knowledge Proofs: Privacy-Preserving Digital Identity with Clare Nelson](https://www.slideshare.net/SSIMeetup/zeroknowledge-proofs-privacypreserving-digital-identity-with-clare-nelson)
* [Anonymous Credentials: Claims and Proofs in a Developer-friendly Format](https://docs.google.com/document/d/1XEfaOinOTIU9RgtP-GlXQAbOoW8z-oR5aWJDoQdftZ4/edit#heading=h.vor6nerodxkn) - Mike Lodder


>Our zero-knowledge proofs are part of the [Idemix protocol](http://domino.research.ibm.com/library/cyberdig.nsf/papers/EEB54FF3B91C1D648525759B004FBBB1/%24File/rz3730_revised.pdf), where they are used to prove the possession of [Camenisch-Lysyanskaya credentials](https://eprint.iacr.org/2001/019.pdf). We also use zero-knowledge proofs in the revocation protocol, which is based on [cryptographic accumulators](https://eprint.iacr.org/2008/539.pdf). —*[What Zero Knowledge Poof Algorithm is used in Sovrin?](https://forum.sovrin.org/t/what-zero-knowledge-proof-algorithm-is-used-in-sovrin/71/2)*

>Identity Mixer is not directly (re)implemented by Sovrin, but its cryptographic foundations are very similar, and Sovrin’s implementation includes most of its extended features (predicates, multi-credential, revocation, advanced issuance…). One of the researchers who helped to create Identity Mixer is on Sovrin’s Technical Governance Board and has offered insight to keep the implementations aligned on goals and methods. 
>—*[How is IDEMix Implemented?](https://forum.sovrin.org/t/how-idemex-is-implemented-in-sovrin-indy/)*

* [IBM Identity Mixer](https://www.zurich.ibm.com/identity_mixer/) [[**B**](https://idemix.wordpress.com/)]
  * [idemix in Hyperledger Fabric](https://hyperledger-fabric.readthedocs.io/en/release-1.3/idemix.html)
* [ABC4Trust—Attribute-based Credentials for Trust](https://abc4trust.eu/)
* [Concepts and Features of Privacy-Preserving Attribute-Based Credentials](https://github.com/p2abcengine/p2abcengine/wiki/Concepts-and-features)
* [Concepts and Languages for Privacy-Preserving Attribute-Based Authentication](http://dl.ifip.org/db/conf/idman/idman2013/CamenischDLNPP13.pdf)
* [Zero-Knowledge Proofs Starter Pack](https://ethresear.ch/t/zero-knowledge-proofs-starter-pack/4519) (Not ID related)


![](https://imgur.com/6MLNgXal.png)\
<sup><a href="https://www.youtube.com/watch?v=RllH91rcFdE">The Story of Open SSI Standards - Drummond Reed/Evernym SSIMeetup.org</a>[<b><a href="https://www.slideshare.net/SSIMeetup/self-sovereign-identity-ssi-open-standards-with-drummond-reed">ϟ</a></b>]</sup>



### W3C and DID Related Standards [**^**](#Contents) [**>>**](../README.md#w3c-and-did-related-standards)

* [World Wide Web Consortium(W3C)](https://www.w3.org/) [[**T**](https://twitter.com/w3c)] [[**G**](https://github.com/w3c)]
* [Credentials Community Group](https://www.w3.org/community/credentials/)[[**B**](https://w3c-ccg.github.io/)]  
* [JSON-LD 1.0, W3C Recommendation](https://www.w3.org/TR/json-ld/)

#### DID the Decentralized Identifier [**^**](#Contents) [**>>**](../README.md#did-the-decentralized-identifier)

<a href="https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf"><img src="https://i.imgur.com/7NRcJbq.png"/></a>

* [w3c- Decentralized Identifiers (DIDs) v0.11](https://w3c-ccg.github.io/did-spec/)
  * Authors:
     * [Drummond Reed](https://equalsdrummond.name/) [[**T**](https://twitter.com/drummondreed)] ([Evernym](https://www.evernym.com/))  
     * [Manu Sporney](http://manu.sporny.org/)[[**T**](https://twitter.com/manusporny)]  ([Digital Bazaar](https://digitalbazaar.com))
     * Dave Longley ([Digital Bazaar](https://digitalbazaar.com))
     * [Christopher Allen](http://www.lifewithalacrity.com/) [[**info**](https://github.com/ChristopherA/info)] ([Blockstream](https://blockstream.com/))
     * Ryan Grant
     * [Markus Sabadello (Peacekeeper)](http://mydata2016.org/speaker/markus-sabadello/) [[**T**](https://twitter.com/peacekeeper)][[**G**](https://github.com/peacekeeper)][[**B**](https://medium.com/@markus.sabadello)] ([Danube Tech](https://github.com/projectdanube))
* [DID Primer](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/draft-documents/did-primer.md) [[**ϟ**](https://github.com/WebOfTrustInfo/rwot7-fall2018/blob/master/topics-and-advance-readings/did-primer-extended.md)]
* [Decentralized IDentifers (DIDs)](https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf) 
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
* [Peer DID Method Spec](https://github.com/dhh1128/peer-did-method-spec)


#### DID Auth [**^**](#Contents) 

![](https://imgur.com/XMaq5cil.png)\
<sup><a href="https://www.youtube.com/watch?v=RllH91rcFdE">The Story of Open SSI Standards - Drummond Reed/Evernym SSIMeetup.org</a>[<b><a href="https://www.slideshare.net/SSIMeetup/self-sovereign-identity-ssi-open-standards-with-drummond-reed">ϟ</a></b>]</sup>

   * [DID Auth and the Little I-am-Me](https://medium.com/@markus.sabadello/did-auth-and-the-little-i-am-me-ec14d757ff09)
   * [Introduction to DID Auth](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/did-auth.md) [[**ϟ**](http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10/)]

<sup><a href="http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10/"><img src="https://i.imgur.com/YNlk8RY.png"/></a>\
http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10</sup>

#### Verifiable Claims [**^**](#Contents) 

<a href="https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf"><img src="https://i.imgur.com/nsZ0X7r.png"/></a>


* [Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/) [[**D**](https://www.w3.org/2017/vc/charter.html)]
* [Verifiable Claims Data Model 1.0](https://w3c.github.io/vc-data-model/) [[**G**](https://github.com/w3c/vc-data-model)] [[**D**](https://w3c.github.io/vc-use-cases/)]
* [Verifiable Credentials 101 for SSI – Tyler Ruff – Webinar 11](https://http://ssimeetup.org/verifiable-credentials-101-ssi-tyler-ruff-webinar-11/)



#### Decentralized Key Management-Agents [**^**](#Contents) 

<img src="https://i.imgur.com/0SLcjUv.png"/>

* [Decentralized Key Management (DKMS): An Essential Missing Piece of the SSI Puzzle - Drummond Reed](https://www.slideshare.net/SSIMeetup/decentralized-key-management-dkms-an-essential-missing-piece-of-the-ssi-puzzle-drummond-reed)
* [Recommendations for Decentralized Key Management Systems](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/dkms-recommendations.md)
* [Agent to Agent Communication](https://drive.google.com/file/d/1PHAy8dMefZG9JNg87Zi33SfKkZvUvXvx/view): Daniel Hardman explains the goals of agent to agent communication



### EU General Data Protection Regulation Act [**^**](#Contents) 

* [Digital Identity Management in the Context of GDPR & Sovrin —Why Data Privacy Matters & How to Protect It](https://blog.tykn.tech/digital-identity-management-in-the-context-of-gdpr-sovrin-43028247378b)
* [Implementing Privacy by Design in Hyperledger Indy](https://www.infoq.com/news/2018/09/Hyperledger-Indy-Privacy)
* [Self-Sovereign Privacy By Design](https://github.com/sovrin-foundation/protocol/blob/master/self_sovereign_privacy_by_design_v1.md)
* [Privacy by Design The 7 Foundational Principles](https://www.ipc.on.ca/wp-content/uploads/Resources/7foundationalprinciples.pdf) 
* [When GDPR Becomes Real, and Blockchain is no longer fairydust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/gdpr.md)
* [Is Self-Sovereign Identity the ultimate GDPR compliance tool? [1\3]](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-9d8110752f89) [[**2**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-40db94c1c437)] [[**3**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-7296a3b07769)]
* [Privacy by Design in Hyperledger Indy](https://www.hyperledger.org/blog/2018/09/12/privacy-by-design-in-hyperledger-indy)

### Research Papers [**^**](#Contents
* [A Conceptual Analysis on Sovrin](https://www.researchgate.net/publication/323144927_A_Conceptual_Analysis_on_Sovrin)
* [Evernym Research Collection *2016 Archive*](https://web.archive.org/web/20170206161655/http://www.evernym.com/our-research/)
* [Matching Identity Management Solutions to Self Sovereign Identity Solutions](https://www.slideshare.net/TommyKoens/matching-identity-management-solutions-to-selfsovereign-identity-principles)
* [A First Look at Identity Management Schemes on the Blockchain](https://arxiv.org/pdf/1801.03294.pdf)


### Reports [**^**](#Contents)
* [A Comprehensive Evaluation of the Identity Management Utility Sovrin](https://dutchblockchaincoalition.org/uploads/pdf/Blockchain-Sovrin-rapport.pdf)
* [White Paper: Canada’s Digital ID Future - A Federated Approach](https://www.cba.ca/embracing-digital-id-in-canada)
* [IDENTITY MATTERS](https://cboxxtest.files.wordpress.com/2017/09/cboxxidentitymatters04.pdf)
* [A position paper on blockchain enabled identity and the road ahead—Identity Working Group of the German Blockchain Association](https://www.bundesblock.de/wp-content/uploads/2018/10/ssi-paper.pdf)


### Video [**^**](#Contents) 
* [Meet the Sovrin Foundation](https://vimeo.com/299487829)
* [Hyperledger Indy Explainer Video](https://www.youtube.com/watch?v=MnO2L6WoqD0)
* [Phil Windley on the Sovrin Network](https://www.youtube.com/watch?v=IxQUL2ztFi8)
* [Self-Sovereign Identity with Hyperledger Indy\Sovrin- Calvin Cheng - FOSSASIA 2018](https://www.youtube.com/watch?v=hfyIZu3_fw8)
* [Hyperledger Indy introduction with Indy Agents Demo](https://www.youtube.com/watch?v=llwfb5Ut5sg)
* [Hyperledger Indy Demo Screencast](https://www.youtube.com/watch?v=9WZxlrGMA3s&t=93s)
* [Architectural Overview of Indy Wallets](https://www.youtube.com/watch?v=Km4IoUdb3Lc)
* [Indy Demo by IBM](https://www.youtube.com/watch?v=cz-6BldajiA)
* [Behind the Cloud Episode 6: Blockchain and Self-Sovereign Identity in the Enterprise](https://www.youtube.com/watch?v=wSdm2-18Z2g)
* [Evernym's contributions to Hyperledger Indy](https://www.youtube.com/playlist?list=PLRp0viTDxBWGLdZk0aamtahB9cpJGV7ZF)
* [Introduction to Indy Plenum Architecture](https://www.youtube.com/watch?v=WZin717AT_A)
* [Hyperledger Indy Working Group Calls](https://drive.google.com/drive/u/0/folders/1AwHWN95KmSEi5fijraID0tFFMzYHoMwt?ogsrc=32)
* [Sovrin: Public, Permissioned and Still Decentralized - Nathan George](https://www.youtube.com/watch?v=lVHJiUrHv2A&app=desktop)
* [Hyperledger Global Forum - Video](https://www.youtube.com/playlist?list=PL0MZ85B_96CGkWnEvdPy5sB4VRcH2XWuP)


### Podcasts [**^**](#Contents) 
* [MyData Podcast](https://mydata.org/podcast/)

### Sources [**^**](#Contents) 
* [Evernym](https://www.evernym.com/)
* [Sovrin Foundation](https://sovrin.org/)
* [wiki.hyperledger.org—Indy](https://wiki.hyperledger.org/display/indy)
* [indy.readthedocs.io](https://indy.readthedocs.io)
* [SSI Meetup](http://ssimeetup.org/) [[**V**](https://www.youtube.com/channel/UCSqSTlKdbbCM1muGOhDa3Og)][[**SS**](https://www.slideshare.net/SSIMeetup/presentations/)] 
* [windley.com/tags/sovrin](http://www.windley.com/tags/sovrin)
* [/WebOfTrustInfo](https://github.com/WebOfTrustInfo/)
* [/peacekeeper/blockchain-identity](https://github.com/peacekeeper/blockchain-identity)
* [/awesome-decentralized-id](/README.md)

---

### Contact Me for Research Based Content—[infominer.id](https://infominer.id)
<a href="https://infominer.id"><img src="https://infominer.id/images/infominer.png" align="right" width="150" height="140"></a>

Check out the [Crypto SuperSource Discord Server](https://discord.gg/ahTuPMY), if you'd like to chat or discover our other crypto-resources.

**Tips Welcome**

BTC— 1GvkjHtiy9LUjVkStnEAXxjhcoS56aCokY

![](https://imgur.com/yXLLm9Bl.png) 

DOGE— DSzMxfABB8EwKiumzV7YHhS7HTvWAyM7QF

![](https://i.imgur.com/0zBLoUP.png) 
