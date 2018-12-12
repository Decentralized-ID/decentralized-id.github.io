# Awesome Sovrin, Hyperledger Indy and DID Resources.
**Protocol, Governance, and Immediately Surrounding Ecosystem** 

Much of the material in this document came from [/awesome-decentralized-id](../README.md).\
However, this one contains attitional material about Evernym, Sovrin, and Hyperledger Indy.

For anyone who wants to think just about indy\sovrin-related things without all the noise.
Since its all related, some jumping back and might be required, but I think its good to have this page "just for Indy" and not so much about other DID solutions.

Pull Requests Welcome.

##### Link Shorthand:
[[**T**](#Link-Shorthand)]witter [[**G**](#Link-Shorthand)]ithub [[**B**](#Link-Shorthand)]log [[**wp**](#Link-Shorthand)] whitepaper [[**D**](#Link-Shorthand)]ocumentation [[**F**](#Link-Shorthand)]orums [[**C**](#Link-Shorthand)]hat [[**ϟ**](#Link-Shorthand)] related resource [[**^**](#Link-Shorthand)] back to the contents [[**>**](#Link-Shorthand)] related section.


### Contents
* [Self Sovereign Identity—SSI](#Self-Sovereign-Identity)
* [GDPR](#EU-General-Data-Protection-Regulation-Act)
* [World Wide Web Consortium—W3C](#World-Wide-Web-Consortium)
  * [DID the Decentralized Identifier](#DID-the-Decentralized-Identifier) 
* [Evernym](#Evernym)
* [The Sovrin Foundation](#The-Sovrin-Foundation)
  * [Sovrin Stewards](#Sovrin-Stewards)
  * [Selected Articles Windley.com](#Selected-Articles-Windley.com)
* [Hyperledger Indy](#Hyperledger-Indy)
  * [Additional Indy Related](#Additional-Indy-Related)
    * [Idemix](#IDEMix)
* [Video](#Video)
* [RWoT Whitepapers](#Selected-Rebooting-Web-of-Trust-Whitepapers)
  * [RWoT Use Cases](#RWoT-Use-Cases) -infographic workflow
* [Evernym\Sovrin\Indy Adoption](#Evernym\Sovrin\Indy-Adoption)
* [DID Adoption](#DID-Adoption)
  * [The Decentralized Identity Foundation (DIF)](#Decentralized-Identity-Foundation)
* [Reports](#Reports)
* [Sources](#Sources)

![](http://imgur.com/3zz62kpl.png)

### Self Sovereign Identity[**^**](#Contents)

Internet Identity Workshop is where the quest for concious, user-centric, identity began. Rebooting Web-of-Trust Workshops sprung from the IIW, focused on creating standards for decentralized identifiers, along with decentralized key managment\PKI. The United Nations 'Sustainable Development Goals' among which is for all the world to have access to a digital identity by 2020. The UN SDGs, blockchain, and the GDPR converged bringing much energy into the identity ecosystem. Additional history and background information may be found at [awesome-decentralized-id](/README.md#History). 

[Christopher Allen](http://www.lifewithalacrity.com/)[[**T**](https://twitter.com/ChristopherA)][[**G**](https://github.com/ChristopherA)] details the overarching history of internet idenitity standards in his seminal work: 
   * **[The Path to Self-Soverereign Identity](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)**[[**ϟ**](https://www.coindesk.com/path-self-sovereign-identity/amp/)].

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">0/ “Self-Sovereign Identity: A Progress Report”…</p>&mdash; Christopher Allen (@ChristopherA) <a href="https://twitter.com/ChristopherA/status/989120215702261761?ref_src=twsrc%5Etfw">April 25, 2018</a></blockquote>

* [Inevitable Rise of Self-Sovereign Identity](https://sovrin.org/wp-content/uploads/2018/03/The-Inevitable-Rise-of-Self-Sovereign-Identity.pdf)
* [Self Sovereign Identity Principles](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md)
* [7 Myths of Self Sovereign Identity](https://medium.com/evernym/7-myths-of-self-sovereign-identity-67aea7416b1)
* [SSI Meetup](http://ssimeetup.org/)


### EU General Data Protection Regulation Act[**^**](#Contents)

* [Digital Identity Management in the Context of GDPR & Sovrin —Why Data Privacy Matters & How to Protect It](https://blog.tykn.tech/digital-identity-management-in-the-context-of-gdpr-sovrin-43028247378b)
* [Self-Sovereign Privacy By Design](https://github.com/sovrin-foundation/protocol/blob/master/self_sovereign_privacy_by_design_v1.md)
* [Privacy by Design The 7 Foundational Principles](https://www.ipc.on.ca/wp-content/uploads/Resources/7foundationalprinciples.pdf) 
* [When GDPR Becomes Real, and Blockchain is no longer fairydust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/gdpr.md)

### World Wide Web Consortium[**^**](#Contents)

![](http://imgur.com/Lz6RTysl.png)

* [World Wide Web Consortium(W3C)](https://www.w3.org/) [[**T**](https://twitter.com/w3c)] [[**G**](https://github.com/w3c)]
* [Credentials Community Group](https://www.w3.org/community/credentials/)[[**B**](https://w3c-ccg.github.io/)]  
* [Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/) [[**D**](https://www.w3.org/2017/vc/charter.html)]
* [Verifiable Claims Data Model 1.0](https://w3c.github.io/vc-data-model/) [[**G**](https://github.com/w3c/vc-data-model)] [[**Use Cases**](https://w3c.github.io/vc-use-cases/)]
* [JSON-LD 1.0, W3C Recommendation](https://www.w3.org/TR/json-ld/)


### DID the Decentralized Identifier[**^**](#Contents) 

* [w3c- Decentralized Identifiers (DIDs) v0.11](https://w3c-ccg.github.io/did-spec/)
  * Authors:
     * Drummond Reed (Evernym)
     * Manu Sporny (Digital Bazaar)
     * Dave Longley (Digital Bazaar)
     * Christopher Allen (Blockstream)
     * Ryan Grant
     * Markus Sabadello (Danube Tech)
* [DID Primer](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/draft-documents/did-primer.md) -[Extended](https://github.com/WebOfTrustInfo/rwot7-fall2018/blob/master/topics-and-advance-readings/did-primer-extended.md)
* [Decentralized IDentifers (DIDs)](https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf) 
   * [DID auth and the Little I-am-Me](https://medium.com/@markus.sabadello/did-auth-and-the-little-i-am-me-ec14d757ff09)
   * [Introduction to DID Auth](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/did-auth.md)
   — [[Markus Sabadello – Webinar 10](http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10/)]
* [A Universal Resolver for self-sovereign identifiers](https://medium.com/decentralized-identity/a-universal-resolver-for-self-sovereign-identifiers-48e6b4a5cc3c) [[**G**](https://github.com/decentralized-identity/universal-resolver)] [**[uniresolver.io](https://uniresolver.io/)**]
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
* [Identity Hubs Capabilities Perspective](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/identity-hubs-capabilities-perspective.md) - Identity Hubs currently proposed in the Decentralized Identity Foundation (DIF) are a subset of a general Decentralized Identifier (DID).
* [DIDs in DPKI](https://github.com/WebOfTrustInfo/rwot7/blob/master/topics-and-advance-readings/dids-in-dpki.md)





### Evernym[**^**](#Contents)

![](http://untangled.world/wp-content/uploads/2017/08/everynym-logo-1400x357.png)

* [Evernym](https://www.evernym.com/)[[**T**](https://twitter.com/evernym)] originally created the Sovrin codebase, founded in 2013.
* [Identity System Essentials](https://www.evernym.com/wp-content/uploads/2017/02/Identity-System-Essentials.pdf) 3/16 (Original Evernym Identity WP submitted to ID2020\RWoT workshop) 
* [Outlier Ventures invests in, becomes strategic partner of Evernym](https://coinreport.net/outlier-ventures-invests-becomes-strategic-partner-evernym/)[[**ϟ**](https://outlierventures.io/portfolio/evernym/)]
* [The Three Models of Digital Identity Relationships — How self-sovereign identity (SSI) is different, and why it’s better](https://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186)
* [Is Self-Sovereign Identity the ultimate GDPR compliance tool? [1\3]](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-9d8110752f89) [[**2**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-40db94c1c437)] [[**3**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-7296a3b07769)]

### The Sovrin Foundation[**^**](#Contents)

![](https://www.evernym.com/wp-content/uploads/2017/04/logo-large.png)

*   [[**F**](https://forum.sovrin.org/)orum] [[**C**](https://chat.sovrin.org/)chat][[**T**](https://twitter.com/SovrinID)witter][[**G**](https://github.com/sovrin-foundation/sovrin)ithub]
* [Founded](http://www.windley.com/archives/2016/09/announcing_the_sovrin_foundation.shtml) in [September](https://www.prnewswire.com/news-releases/sovrin-foundation-launches-first-dedicated-self-sovereign-identity-network-300336702.html) 2016, The [Sovrin](https://sovrin.org/)
 Foundation is creating a public instance of the Sovrin\Indy codebase; initially developed by [Evernym](#Evernym)
* [Sovrin Library](https://sovrin.org/library/)
* [Getting Started with Sovrin](https://sovrin.org/library/getting-started-with-sovrin/)
* [Sovrin: A Protocol and Token for Self-Sovereign Identity and Decentralized Trust](https://sovrin.org/wp-content/uploads/Sovrin-Protocol-and-Token-White-Paper.pdf)
* [Sovrin Network: What Goes on the Ledger?](https://sovrin.org/wp-content/uploads/2018/10/What-Goes-On-The-Ledger.pdf)
* [Sovrin Governance Framework](https://sovrin.org/library/sovrin-governance-framework/)
* [How Sovrin Works: A Technical Guide from the Sovrin Foundation](https://sovrin.org/wp-content/uploads/2018/03/How-Sovrin-Works.pdf)
* [Sovrin Test Network Trust Anchor Registration](https://s3.us-east-2.amazonaws.com/evernym-cs/sovrin-STNnetwork/www/trust-anchor.html)[[**F**](https://forum.sovrin.org/t/testing-on-the-sovrin-test-network-stn/643/17)]

#### Sovrin Stewards[**^**](#Contents)

The Sovrin ledger is operated by Stewards, trusted organizations within the ecosystem who have agreed to abide by the requirements in the [Sovrin Trust Framework](https://sovrin.org/library/sovrin-governance-framework/) and are responsible for operation the nodes that maintain the Sovrin distributed ledger.

Stewards also, as a group, accept or reject any changes to the ledger-specific portions of the Sovrin open source code by virtue of that role. They thus provide a counterbalance to the Sovrin architects who maintain the Indy code base.

[Aalto University](http://www.aalto.fi/en/)
| [Absa Group Limited](https://www.absa.africa/absaafrica/)
| [Amihan Global Strategies](https://amihan.net/)
| [ARTiFACTS](https://artifacts.ai/)
| [Attinad Software](http://attinadsoftware.com/)
| [ATB Financial](http://www.atb.com/Pages/default.aspx)
| [Best Innovation Group](http://www.big-fintech.com/)
| [BakerHostetler](https://www.bakerlaw.com/)
| [Cisco](https://www.cisco.com/)
| [Certisign](http://www.certisign.com.br/)
| [Crypto Valley Association](https://cryptovalley.swiss/)
| [CULedger](http://culedger.com/)
| [Danube Tech](https://danubetech.com/)
| [Datum](https://datum.org/)
| [Desert Financial Credit Union](https://www.desertschools.org/business)
| [Digicert](https://www.digicert.com/)
| [Digital Bazaar](https://digitalbazaar.com/)
| [estatus AG](https://www.esatus.com/)
| [Evernym](https://www.evernym.com/)
| [Finicity](https://www.finicity.com/)
| [First Education Credit Union](https://www.firstedfcu.com/)
| [Global Consent](http://www.consent.global/)
| [IBM](https://www.ibm.com/blogs/blockchain/2018/08/ibm-blockchain-trusted-identity-sovrin-steward-closed-beta-offering/)
| [InfoCert](https://infocert.digital/)
| [iRespond](http://irespond.org/)
| [KYC Chain](https://kyc-chain.com/)
| [OAS Staff Federal Credit Union](https://www.oasfcu.org/en/default.asp)
| [Perkins Cole](https://www.perkinscoie.com/)
| [ProSapien](https://www.prosapien.com/)
| [Qiy Foundation](https://www.qiyfoundation.org/)
| [Royal Credit Union](https://www.rcu.org/)
| [SICPA](https://www.sicpa.com/)
| [SITA](https://www.sita.aero/)
| [T-Labs](https://laboratories.telekom.com/)
| [The City of Osmio](https://osmio.ch/)
| [TNO](https://www.tno.nl/en/)
| [Truu](https://www.truu.id/)
| [TwinPeek](https://twinpeek.net/)
| [Tykn](https://tykn.tech/)
| [Veridium](https://veridiumid.com/)

#### Selected articles Windley.com [**^**](#Contents)

* [windley.com/tags/sovrin](http://www.windley.com/tags/sovrin)
* [An Internet for Identity](http://www.windley.com/archives/2016/08/an_internet_for_identity.shtml)
* [A Universal Trust Framework](http://www.windley.com/archives/2017/01/a_universal_trust_framework.shtml)
* [Building Your Business on Sovrin: Domain-Specific Trust Frameworks](http://www.windley.com/archives/2018/03/building_your_business_on_sovrin_domain-specific_trust_frameworks.shtml)
* [The Sovrin Foundation](http://www.windley.com/archives/2018/07/the_sovrin_foundation.shtml)
* [Decentralization in Sovrin](http://www.windley.com/archives/2018/10/decentralization_in_sovrin.shtml)
* [Self-Sovereign Identity and the Legitimacy of Permissioned Ledgers](http://www.windley.com/archives/2016/09/self-sovereign_identity_and_the_legitimacy_of_permissioned_ledgers.shtml)
* [The Sovrin Ecosystem](http://www.windley.com/archives/2018/11/the_sovrin_ecosystem.shtml) (Disambiguating between Evernym, Sovrin, and Indy)


### Hyperledger Indy[**^**](#Contents)

![](https://www.osiztechnologies.com/asset/oimages/hyperledger_indy/hyperledger_indy_02.png)

![](http://imgur.com/2LWlrgvl.png)\
[Linux Foundation -Blockchain for Business -INDY](https://www.edx.org/course/blockchain-for-business-an-introduction-to-hyperledger-technologies)

* [Hyperledger Indy - *Distributed Ledger and Utility Library*](https://www.hyperledger.org/projects/hyperledger-indy) [[**T**](https://twitter.com/Hyperledger)] [[**G**](https://github.com/hyperledger/indy-sdk)]
* [Hyperledger Indy — the Future of Decentralized Identity](https://medium.com/axiom-tech/hyperledger-indy-the-future-of-decentralized-identity-9de5c2459e4e)
* [Hyperledger Welcomes Project Indy](https://www.hyperledger.org/blog/2017/05/02/hyperledger-welcomes-project-indy) - ANN
* [The Rise of Self-Sovereign Identity - Hyperledger Indy](https://wso2.com/blog/research/the-rise-of-self-sovereign-identity-hyperledger-indy)
* [Indy Documentation Index - wiki.hyperledger.org](https://wiki.hyperledger.org/projects/indy/documentation)
* [indy.readthedocs.io](https://indy.readthedocs.io/) (under construction)
* [Ernesto.net - What goes on the Ledger](https://www.ernesto.net/ernesto-net-5-minute-course-on-indy-and-what-goes-on-the-blockchain-ledger/)
* [Ernesto.net - Hyperledger Indy Architecture](https://www.ernesto.net/hyperledger-indy-architecture/)
* The Linux Foundation's [Blockchain for Business](https://www.edx.org/professional-certificate/linuxfoundationx-blockchain-for-business) course may be freely audited and has a section about Indy.

#### Additional Indy Related[**^**](#Contents) 
* [Plenum Bzantine Fault Tolerant Protocol](https://github.com/hyperledger/indy-plenum/wiki)
   * "Byzantine fault tolerance is a sub-field of fault tolerance research inspired by the Byzantine Generals' Problem, which is a generalized version of the Two Generals' Problem."
* [HyperledgerIndyWGCall_2018-12-06](https://drive.google.com/file/d/1166XpTM8WgZVMN2ca53CRCJapZlAeUhM/view) Discussion of VON and Plenum Docs (with info graphics)
* [A Framework for Designing Cryptographic Key Management Systems](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-130.pdf)
* [An Accumulator Based on Bilinear Maps and Efficient Revocation for Anonymous Credentials](https://eprint.iacr.org/2008/539.pdf)
* [An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation](https://www.iacr.org/archive/eurocrypt2001/20450093.pdf)
* [Implementing Privacy by Design in Hyperledger Indy](https://www.infoq.com/news/2018/09/Hyperledger-Indy-Privacy)

##### IDEMix[**^**](#Contents)
* [What Zero Knowledge Poof Algorithm is used in Sovrin?](https://forum.sovrin.org/t/what-zero-knowledge-proof-algorithm-is-used-in-sovrin/71/2)
* [How is IDEMix Implemented in Sovrin\Indy?](https://forum.sovrin.org/t/how-idemex-is-implemented-in-sovrin-indy)
* [idemix in Hyperledger Fabric](https://hyperledger-fabric.readthedocs.io/en/release-1.3/idemix.html)
* [Concepts and Features of Privacy-Preserving Attribute-Based Credentials](https://github.com/p2abcengine/p2abcengine/wiki/Concepts-and-features)
* [AnonCreds: Anonymous credentials protocol implementation in python](https://github.com/hyperledger/indy-anoncreds) [[Usecase](https://github.com/hyperledger/indy-anoncreds/blob/master/docs/anoncred-usecase1.pdf)]


### Selected 'Rebooting Web of Trust' Whitepapers[**^**](#Contents) 
* [WebofTrust.info/papers.html](https://www.weboftrust.info/papers.html)
* [Rebranding the Web of Trust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/rebranding-web-of-trust.pdf) Original RWoT whitepaper
* [Framework for the Comparison of Identity Systems](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/Framework-for-Comparison-of-Identity-Systems.md)
* [A Primer on Functional Identity](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/functional-identity-primer.md)
* [The DCS Theorem](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/dcs-theorem/The-DCS-Theorem.md) — We use the triangle to show decentralized consensus systems can have _Decentralization_, _Consensus_, or _Scale_, but not all three properties simultaneously.
* [Identity Crisis: Clear Identity through Correlation](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/identity-crisis.pdf)
* [Decentralized Key Management System](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2017/blob/master/topics-and-advance-readings/dkms-decentralized-key-mgmt-system.md)
* [Rebooting the Web of Trust VII: Toronto (September 2018)](https://github.com/WebOfTrustInfo/rwot7) - More recent thoughts.
* [SSI: A Roadmap for Adoption](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/a-roadmap-for-ssi.md)

### RWoT Use Cases[**^**](#Contents)
—infogrphic workflow examples 
* [Amira 1.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/amira.md)
* [Re-Imagining What Users Really Want](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2017/blob/master/final-documents/what-users-really-want.md)
* [Joram 1.0.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2016/blob/master/final-documents/joram-engagement-model.pdf)
* [Powering the Physician-Patient Relationship with HIE of One Blockchain Health IT](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/physician-patient-relationship.pdf)
* [Protecting Digital Identities in Developing Countries](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/protecting-digital-identities-in-developing-countries.pdf)
* [Opportunities Created by the Web of Trust for Controlling and Leveraging Personal Data](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/satisfying-real-world-use-cases.pdf)


### Evernym\Sovrin\Indy Adoption[**^**](#Contents)

* [Verified Organization Network](https://vonx.io/) [[**G**](https://github.com/bcgov/von)] [[**>**](#Canada)]
   * "an initiative by the government of British Columbia to create a trusted network of organizational data. It allows organizations to claim credentials that are part of their own digital identity, using a component called [TheOrgBook](https://theorgbook.pathfinder.gov.bc.ca/en/home)[[**G**]](https://github.com/bcgov/theorgbook) that lists entities with their associated public verifiable claims.
   * [Demonstrating the Verifiable Organizations Network (VON)](https://docs.google.com/document/d/1wNnXdQKUtWnx--xw3VQ9Fr2TDa0kUNIBSMmFGR4uoMg/edit#heading=h.kphtj2c176xb)
   * [bcdevexchange.org/opportunities](https://bcdevexchange.org/opportunities)
* [Tykn *The Future of Resilient Identity*](https://tykn.tech/) [[**T**](https://twitter.com/Tykn_tech)][[**G**](https://github.com/tykntech)][[**D**](https://docs.google.com/document/d/1pNRO6aOb5eK4s8PVv7yS4x9TkqrGglCJ4jebU1F3Yzo/edit#)] (Indy\Sovrin)
* [Illinois Blockchain Initiative](https://illinoisblockchain.tech/) — [partners with Evernym to launch birth registration pilot](https://illinoisblockchain.tech/illinois-partners-with-evernym-to-launch-birth-registration-pilot-f2668664f67c)
* [News Release: DHS S&T Awards $749K to Evernym for Decentralized Key Management Research and Development](https://www.dhs.gov/science-and-technology/news/2017/07/20/news-release-dhs-st-awards-749k-evernym-decentralized-key) (Department of Homeland Security)
* [Evernym and R3 Partner to Apply Self-Sovereign Identity to Financial Services](http://www.paymentsjournal.com/evernym-r3-partner-apply-self-sovereign-identity-financial-services/)
* [Sovrin Foundation, Ontology and Evernym Collaborate on Interoperable Decentralized Identity Networks](https://globenewswire.com/news-release/2018/10/23/1625715/0/en/Sovrin-Foundation-Ontology-and-Evernym-Collaborate-on-Interoperable-Decentralized-Identity-Networks.html)
* [SecureKey Technologies to explore interoperability between Verified.Me and Hyperledger Indy](https://securekey.com/press-releases/hyperledger-indy/)
* [Evernym rolls with auto industry association MOBI to promote SSI in automotive and IoT](https://globenewswire.com/news-release/2018/10/05/1617425/0/en/Evernym-rolls-with-auto-industry-association-MOBI-to-promote-SSI-in-automotive-and-IoT.html)
* [15 Industry Leaders Join Evernym’s Global Accelerator to Build the Future of Digital Identity.](https://globenewswire.com/news-release/2018/11/07/1647044/0/en/15-Industry-Leaders-Join-Evernym-s-Global-Accelerator-to-Build-the-Future-of-Digital-Identity.html)
   > Founding members of the Accelerator include industry leading organizations ATB Financial, IAG, Irish Life, the International Federation of Red Cross, Spark New Zealand, Truu and three provincial and state governments. Collectively, these organizations represent the interests of 100's of millions of individuals worldwide.
* [IOTA and Evernym Launch Collaboration Aimed at Making the Internet of Things More Secure](https://globenewswire.com/news-release/2017/08/31/1106292/0/en/IOTA-and-Evernym-Launch-Collaboration-Aimed-at-Making-the-Internet-of-Things-More-Secure.html)
* [Digital Identity Innovator Helps Non-Profits Get on the Identity Blockchain](https://globenewswire.com/news-release/2018/09/25/1575928/0/en/Digital-Identity-Innovator-Helps-Non-Profits-Get-on-the-Identity-Blockchain.html)
   >Evernym is opening its Accelerator program to Non Profit Organization (NPOs) applications. Evernym will waive the $50,000 membership fee it normally charges to participate in the program. A panel of judges will select the successful applicants. The first group of awards will be announced before December 2018 and will include 5 organizations. Further NPO cohorts are already planned for 2019.\
   >The World Bank estimates over 1 billion persons, usually the most vulnerable, are without formal identity.
* [The Sovrin Foundation Names Cisco Founding Steward](https://globenewswire.com/news-release/2018/06/21/1527830/0/en/The-Sovrin-Foundation-Names-Cisco-Founding-Steward.html)
* [CULedger partners with decentralized identity innovator Evernym to create MyCUID](https://www.cuinsight.com/press-release/culedger-partners-decentralized-identity-innovator-evernym-create-mycuid)
* [Self Sovereign Identity and MyData](https://medium.com/@apoikola/self-sovereign-identity-and-mydata-e1f996a9451)
  * [Mydata](http://mydata.org/) [[**T**](https://twitter.com/mydataorg)] [[**D**](https://mydata.org/papers/)] [[**D**](https://mydata.org/declaration/)]
    * goal: to empower individuals with their personal data, thus helping them and their communities develop knowledge, make informed decisions, and interact more consciously and efficiently with each other as well as with organisations."
  * [Consent](http://www.consent.global/)[[**ϟ**](https://sovrin.org/steward/global-consent/)] — "platform for trusted personal data applications and services, using Ethereum smart contracts to implement decentralized identifiers, verified credentials, consent receipts, a web of trust, and exchange of assets and value." 
* [Legal Entity Identifier blockchained by a Hyperledger Indy implementation of GraphChain](http://www.graphchain.io/MTSR2018.pdf)
  >The main idea behind GraphChain is to use blockchain mechanisms on top of an abstract RDF graphs. This paper presents an implementation of GraphChain in the Hyperledger Indy framework. The whole setting is shown to be applied to the RDF graphs containing information about Legal Entity Identifiers (LEIs).

### DID Adoption [**^**](#Contents)

* [@ChristopherA on DID adoption](https://twitter.com/ChristopherA/status/989122017348784130)
   > "22/ Over a dozen companies and organizations, using multiple blockchains (Bitcoin, Ethereum, Hyperledger, etc.), have committed to deploying DIDs, including IBM, Microsoft, Digital Bazaar, Consensys, Evernym, Learning Machine, British Columbia, and more:" —[How blockchain could solve the internet privacy problem](https://www.computerworld.com/article/3267930/blockchain/how-blockchain-could-solve-the-internet-privacy-problem.html)
* [Veres One DID Method 1.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/did-method-veres-one.md) — a permissionless public ledger designed specifically for the creation and management of decentralized identifiers (DIDs)
* [Blockstack DID Spec](https://github.com/blockstack/blockstack-core/blob/master/docs/blockstack-did-spec.md)[**[ϟ](https://forum.blockstack.org/t/did-method-at-identity-foundation/4287/9)**]
* [Spidchain](http://www.spidchain.com/) [[**wp**](https://drive.google.com/file/d/0B89WE3IIHmy1Z0ZSSWVmVEtaaG8/view)]
   * "offers a platform for self-sovereign identity, including desktop and mobile apps for end-users. It uses Decentralized Identifiers (DIDs) - backed by optionally Bitcoin or Ethereum - to implement a marketplace for verifiable claims. The Spidchain applications allow individuals to create, recover, and revoke DIDs, to authenticate, to sign and verify files and claims, and more."
* [U.S. Department of Homeland Security funds four Blockchains](https://bravenewcoin.com/insights/u-s-department-of-homeland-security-funds-four-blockchain-companies-developing-new-cyber-security-technology)
* [IBM-Paving the Road to Self-Sovereign Identity with Blockchain, Open Standards](https://www.ibm.com/blogs/think/2017/10/self-sovereign-id-blockchain/)
* [SecureKey](http://securekey.com/): [partners with IBM](http://www-03.ibm.com/press/us/en/pressrelease/51841.wss) to enable a new digital identity and attribute sharing network based on Hyperledger Fabric blockchain.
* Microsoft: [Decentralized Identity—Own and control your identity](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE2DjfY) [[Coindesk](https://www.coindesk.com/microsoft-is-pushing-new-blockchain-id-products-but-theres-pushback-too)]
* [Identity at Coinbase: Welcoming the Distributed Systems team](https://blog.coinbase.com/identity-at-coinbase-welcoming-the-distributed-systems-team-d929dd64de2e) 

![](http://imgur.com/PXGV6Xyl.png)

#### Decentralized Identity Foundation[**^**](#Contents) 

On May 22 at Consensus 2017 the formation of the Decentralized Identity Foundation (DIF) [was announced](https://www.ethnews.com/decentralized-identity-foundation-announces-formation-at-consensus-2017):
* [Conensus 2017 - Building an Foundation for Decentralized Identity](https://www.youtube.com/watch?v=l5laRZfn8AI) (video)
* [Decentralized Identity Foundation](http://identity.foundation/) (DIF) [[**G**](https://github.com/decentralized-identity)] [[**T**](https://twitter.com/DecentralizedID)] [[**B**](https://medium.com/decentralized-identity)] 
* [Decentralized Identity Foundation Grows To 56 Members In Our First Year](https://medium.com/decentralized-identity/decentralized-identity-foundation-grows-to-56-members-in-our-first-year-3ec117e811d8)

So now we have the DID, which is gaining adoption and may be universally resolved. That is only one, albeit important, aspect of a decentralized identity. In order for those DID to be interoperable across different networks will require some agreement on standards for other related protocols. 


### Research Papers
* [A Conceptual Analysis on Sovrin](https://www.researchgate.net/publication/323144927_A_Conceptual_Analysis_on_Sovrin)
* [Evernym Research Collection *2016 Archive*](https://web.archive.org/web/20170206161655/http://www.evernym.com/our-research/)

### Reports[**^**](#Contents)
* [A Comprehensive Evaluation of the Identity Management Utility Sovrin](https://dutchblockchaincoalition.org/uploads/pdf/Blockchain-Sovrin-rapport.pdf)
* [How Blockchain Revolutionizes Identity Management](https://www.accenture-insights.nl/en-us/articles/how-blockchain-will-revolutionize-identity-management)
* [Blockchain: Evolving Decentralized Identity Design](https://www.gartner.com/doc/3834863/blockchain-evolving-decentralized-identity-design)
* [White Paper: Canada’s Digital ID Future - A Federated Approach](https://www.cba.ca/embracing-digital-id-in-canada)
* [IDENTITY MATTERS](https://cboxxtest.files.wordpress.com/2017/09/cboxxidentitymatters04.pdf)
* [Accenture: ID2020: DIGITAL IDENTITY with Blockchain and Biometrics](https://www.accenture.com/us-en/insight-blockchain-id2020)
* [r3- Identity in Depth](https://www.r3.com/wp-content/uploads/2017/06/Identity_indepth_r3.pdf)

### Video[**^**](#Contents)
* [Phil Windley on the Sovrin Network](https://www.youtube.com/watch?v=IxQUL2ztFi8)
* [Self-Sovereign Identity with Hyperledger Indy\Sovrin- Calvin Cheng - FOSSASIA 2018](https://www.youtube.com/watch?v=hfyIZu3_fw8)
* [Hyperledger Indy introduction with Indy Agents Demo](https://www.youtube.com/watch?v=llwfb5Ut5sg)
* [Hyperledger Indy Demo Screencast](https://www.youtube.com/watch?v=9WZxlrGMA3s&t=93s)
* [Architectural Overview of Indy Wallets](https://www.youtube.com/watch?v=Km4IoUdb3Lc)
* [Indy Demo by IBM](https://www.youtube.com/watch?v=cz-6BldajiA)

### Podcasts
* [MyData Podcast](https://mydata.org/podcast/)

### Sources[**^**](#Contents)
* [windley.com/tags/sovrin](http://www.windley.com/tags/sovrin)
* [/awesome-decentralized-id](/README.md)
* [/WebOfTrustInfo](https://github.com/WebOfTrustInfo/)
* [/peacekeeper/blockchain-identity](https://github.com/peacekeeper/blockchain-identity)
* [/blockchain-id.toml](/blockchain-id.toml)

### Brought to you by: [The Crypto Library—Super Source](https://github.com/infominer33/Crypto-library)

BTC— 1GvkjHtiy9LUjVkStnEAXxjhcoS56aCokY
 
![](http://imgur.com/xMd9r0rl.png)       ![http://crypt0library.net](http://imgur.com/0rvKAhll.png)

DOGE— DSzMxfABB8EwKiumzV7YHhS7HTvWAyM7QF

![](https://i.imgur.com/0zBLoUP.png)
