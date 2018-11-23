# Awesome Decentralized Identity
**DID, Blockchain and Self-Sovereign Identity Resources v0.5**

Gratitude to those who are working to make our identity experience, and the world, a better place.

[Collaboration Welcome](https://github.com/infominer33/awesome-decentralized-id/blob/master/contributing.md)

![](https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/Internet_dog.jpg/220px-Internet_dog.jpg)

>Imagine a world where you are in direct control of your personal information; a world where you can limit and control how much information you share while retaining the ability to transact in the world. This is self-sovereign identity, and it is already here. Blockchain is the underlying technology paving the path to self-sovereign identity through decentralized networks. It ensures privacy and trust, where transactions are secure, authenticated and verifiable and endorsed by relevant, permissioned participants.  [Jerry Cuomo -IBM](https://techcrunch.com/2017/09/10/the-promise-of-managing-identity-on-the-blockchain/)

### Contents

* [History](#History)
  * [Internet Identity Workshop—IIW](#Internet-Identity-Workshop) 
  * [#Rebooting-Web-of-Trust (RWoT)](#Rebooting-the-Web-Of-Trust)
  * [Bitnation and the United Nations](#Bitnation-and-the-United-Nations)
    * [ID2020 and the GDPR](#ID2020-and-the-GDPR)
* [Resources](#Resources)
  * [World Wide Web Consortium—W3C](#World-Wide-Web-Consortium)
    * [DID the Decentralized Identifier ](#DID-the-Decentralized-Identifier) 
  * [EU GDPR](#EU-General-Data-Protection-Regulation-Act)
  * [Self Sovereign Identity—SSI](#Self-Sovereign-Identity)
  * [Evernym](#Evernym)
  * [The Sovrin Foundation](#The-Sovrin-Foundation)
    * [Windley](#Windley)
    * [Tykn Tech](#Tykn-Tech)
  * [Hyperledger Indy](#Hyperledger-Indy)
    * [Idemix](#IDEMix)
  * [IBM](#IBM)
  * [Ethereum—Protocol](#Ethereum)
    * [Ethereum Apps](#Ethereum-Identity-Applications)
  * [State Led Identity Initiatives](#State-Led-Initiatives)
    * [Canada](#Canada)
    * [Netherlands](#Netherlands)
    * [Spain](#Spain)
    * [Switzerland](#Switzerland)
    * [Estonia](#Estonia)
  * [Assorted Decentralized \ Blockchain ID Initiatives](#Assorted-Decentralized-\-Blockchain-ID-Initiatives)
  * [Data Wallet \ Marketplaces](#Data-Wallet-\-Marketplaces)
  * [Decentralized Identity Foundation—DIF](#Decentralized-Identity-Foundation)
  * [Reports](#Reports)
  * [Research Papers](#Research-Papers)
  * [RWoT Use Cases](#RWoT-Use-Cases) —infogrphic workflow examples
  * [Resources](#Resources)
  * [People](#People)


*Link abbreviations: (**f**)orum, (**t**)witter, (**g**)ithub, (**wp**)whitepaper, (**b**)log, (**c**)hat, (**d**)ocumentation.

Numbered links are supporting information for a given subject not easily categorized*

## History

First we'll go over some history, to give the decentralized identity story some context.

![](https://www.yubico.com/wp-content/uploads/2013/10/IIW-blog.jpg)

### Internet Identity Workshop

In 2005, [Kaliya Young](https://identitywoman.net/)[[**t**](https://twitter.com/IdentityWoman)], [Phil Windley](https://windley.com)[[**t**](https://twitter.com/windley)], [Drummond Reed](https://www.evernym.com/)[[**t**](https://twitter.com/drummondreed)], and [Doc Searls](http://blogs.harvard.edu/doc/)[[**1**](https://blogs.harvard.edu/doc/2013/10/14/iiw-challenge-1-sovereign-identity-in-the-great-silo-forest/)][[**t**](https://twitter.com/dsearls)] hosted the first [Internet Identity Workshop](http://www.internetidentityworkshop.com/)(IIW)[[**t**](https://twitter.com/idworkshop)] in Berkeley to discuss "architectural and governance proposals for Internet-wide identity services and their underlying philosophies." -[Announcing IIW 2005](https://identitywoman.net/announcing-the-internet-identity-workshop-iiw2005/)

Since then, the IIW has met bi-anually, actively supporting the development of the identity software-ecosystem, including [OpenID](http://wiki.openid.net)('05), OpenID [2.0](http://wiki.openid.net/w/page/12995215/OpenID%20Authentication%202-1)('06), [OAuth](https://en.wikipedia.org/wiki/OAuth)('10), [FIDO](https://fidoalliance.org/)('13) and OpenID [Connect](https://en.wikipedia.org/wiki/OpenID_Connect)('14). The heart of the internet identity community has been with empowering users and self-sovereign principles, since the early days.

* [*What is Sovereign Source Authority?*](https://www.moxytongue.com/2012/02/what-is-sovereign-source-authority.html) shows an early use of 'sovereign' in relation to our internet identities. The term "Self Sovereign Identity" started becoming widely used in 2014.[[**2**](https://www.tokencommons.org/Windhover-Principles-for-Digital-Identity-Trust-Data.html)][[**3**](https://hubculture.com/hubs/47/news/689/)] 
* [Christopher Allen](http://www.lifewithalacrity.com/)[[**t**](https://twitter.com/ChristopherA)][[**g**](https://github.com/ChristopherA)] details the overarching history of internet idenitity standards in his seminal work: **[The Path to Self-Soverereign Identity](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)**[[**4**](https://www.coindesk.com/path-self-sovereign-identity/amp/)].
* [Not Just Who They Say We Are: Claiming our identity on the Internet](https://vimeo.com/207961532)- short film on the “Identerati” at IIW[[**5**](https://www.prweb.com/releases/identitymovie/iiw2017/prweb14161721.htm)]
   * Identirati is a term for those working in the identity ecosystem dating back to at least 2006:
      >"[identirati](https://www.zdnet.com/article/the-identity-silo-paradox/)[[**6**](https://www.forgerock.com/blog/who-are-the-identerati)]" have been working on standards and methods that are based on the premise of opening up those [id data] silos 
* **More information** on iid standard history: **[IIW-Wiki](http://iiw.idcommons.net/Main_Page)** | **[identitywoman.net](https://identitywoman.net/)** | **[windley.com-#identity](http://www.windley.com/tags/identity.shtml)** | **[WoTinfo](https://github.com/WebOfTrustInfo/)**

8/14 The [Credentials Community Group](https://www.w3.org/community/credentials/)[[**7**](https://w3c-ccg.github.io/)] forms, hosted by [World Wide Web Consortium(W3C)](https://www.w3.org/)[[**t**](https://twitter.com/w3c)][[**g**](https://github.com/w3c)] : "to forge a path for a secure, decentralized system of credentials that would empower both individual people and organizations on the Web to store, transmit, and receive digitally verifiable proof of qualifications and achievements." —proposed by [Manu Sporney](http://manu.sporny.org/)[[**t**](https://twitter.com/manusporny)][[**8**](https://digitalbazaar.com/)]

 
![](http://imgur.com/GdYLQjzl.png)

### Rebooting the Web Of Trust

In relation to SSI, '[Web of Trust](https://en.wikipedia.org/wiki/Web_of_trust)' is a network of relationships that attest to our identity claims. *Each party attesting to your identity information becomes a strand in your web of trust.*

The first Rebooting Web of Trust ([RWoT](http://www.WebOfTrust.info)[[**g**](https://github.com/WebOfTrustInfo/)])  workshop was held during [November 2015](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust); attracting the likes of Vitalik Buterin, Peter Todd, Gregory Maxwell, Joel Dietz, Christopher Allen, and Jon Callas, [according to Andreas Antonopolis](https://news.bitcoin.com/andreas-antonopoulos-case-reputation-identity-systems/). 

The goal of the initial workshop, was to create 5[[**wp**](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/topics-and-advance-readings/README.md)] technical white papers: [[5 WoT-usecases](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/satisfying-real-world-use-cases.pdf)][[Decentralized PKI](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/dpki.pdf)][[Smart Signatures](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/smart-signatures.pdf)(Bitcoin inspired)][[Creating a New World of Trust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/whats-the-next-step.pdf)][[Rebranding the Web of Trust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/rebranding-web-of-trust.pdf)]:

>The Web of Trust is a buzzword for a new model of decentralized self-sovereign identity. It’s a phrase that dates back almost twenty-five years, the classic definition derives from PGP [...] the vibrant blockchain community is also drawing new attention to the concept we aim to reboot it.

![](https://upload.wikimedia.org/wikipedia/en/thumb/2/27/Sustainable_Development_Goals_chart.svg/787px-Sustainable_Development_Goals_chart.svg.png)

### Bitnation and the United Nations 

9\15 [Bitnation](https://bitnation.co/) "seeks to establish the concept of '*world citizenship*' via a bitcoin based identity, offering '[*blockchain emergency IDs*](https://refugees.bitnation.co/)' to refugees.[[**9**](https://www.newsbtc.com/2015/09/09/bitnation-taps-blockchain-tech-to-aid-refugees/)] The same month, the UN unveiled it's *Agenda for Sustainable Development*

* [Transforming our world: the 2030 Agenda for Sustainable Development](https://sustainabledevelopment.un.org/post2015/transformingourworld)
> **Goal 16.9 By 2030, provide legal identity for all, including birth registration**
* [DIGITAL IDENTITY AS A BASIC HUMAN RIGHT](https://impakter.com/digital-identity-basic-human-right/)
* [AID:Tech](https://aid.technology)[[**t**]](https://twitter.com/aidtechnology) — "is a voucher and digital identity solution for refugees. A digital record of a person's identity is stored on a smart card, along with various additional information. Blockchain technology is used to distribute all resources in a highly traceable manner."

#### ID2020 and the GDPR

![](http://imgur.com/ymviAssl.png)

[4/16](https://edps.europa.eu/data-protection/data-protection/legislation/history-general-data-protection-regulation_en) the EU adopted the GDPR, enacted as law May 2018. The second RWoT workshop ran in conjunction with the UN's [ID2020](https://id2020.org/) Summit in New York that [May](https://press.pwc.com/News-releases/id2020-to-kick-start-digital-identity-summit-at-un-with-pwc-support./s/9fe11be5-cbd8-486b-b4d2-d798f486d0f2). There are an estimated 1.5 billion without a legal identity.[[**10**](https://id2020.org/news/2016/12/2/identity-20)] Without a legal identity it is very difficult to recieve any services, aide, or to advance ones station in life. 

During the RWoT\ID2020 Workshop[[**11**](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/topics-and-advance-readings/README.md)] the DID identifier began to emerge:
* [Clearer Identity Through Correlation](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/identity-crisis.pdf)
* [Physician Patient Relationship](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/physician-patient-relationship.pdf) -Blockchains and DIDs for physician-patient interactions.
* [Protecting Digital ID in Developing Countries](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/protecting-digital-identities-in-developing-countries.pdf)
* [Smarter Signatures](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/smarter-signatures.pdf)
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
   >"Respect Network is conducting a research project for the U.S. Department of Homeland Security, HSHQDC-16-C-00061, to analyze the applicability of blockchain technologies to a decentralized identifier system. Our thesis is that blockchains, or more generically distributed ledgers, are a potentially powerful new tool for “identity roots” — the starting points for an Internet identity. However “blockchain identity” may not fully address the core security and privacy principles needed in a complete identity system. In this case DIDs — Decentralized Identifiers rooted on a distributed ledger — may end up being a foundational building block for higher level identity management solutions. 
* At this point in time DLT innovation, the United Nations Sustainable Development Goals, and the EU GDPR all came together supporting a core identirati tenant: Eliminating id data silos and empowering users regarding personal digital identity. 

## Resources

### World Wide Web Consortium

![](http://imgur.com/Lz6RTysl.png)

* [World Wide Web Consortium(W3C)](https://www.w3.org/)[[**t**](https://twitter.com/w3c)][[**g**](https://github.com/w3c)]
* [Credentials Community Group](https://www.w3.org/community/credentials/)[[**b**](https://w3c-ccg.github.io/)]  
* [Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/)
   * [Verifiable Claims Working Group Charter](https://www.w3.org/2017/vc/charter.html)
* [The W3C CREDENTIALS COMMUNITY GROUP](https://www.w3.org/community/credentials/) | [W3C CCG](https://w3c-ccg.github.io/)
* [Verifiable Claims Data Model 1.0](https://w3c.github.io/vc-data-model/)[[**g**](https://github.com/w3c/vc-data-model)]
* [Verifiable Claims Use Cases 1.0](https://w3c.github.io/vc-use-cases/)
* [JSON-LD 1.0, W3C Recommendation](https://www.w3.org/TR/json-ld/)
* [opencreds.org — Identity Credentials 1.0](https://opencreds.org/specs/source/identity-credentials/)
* [DIGITAL VERIFICATION COMMUNITY GROUP](https://www.w3.org/community/digital-verification/)[[**g**](https://sea-region.github.com/w3c-dvcg)]

#### DID the Decentralized Identifier 

* [w3c- Decentralized Identifiers (DIDs) v0.11](https://w3c-ccg.github.io/did-spec/)
* [DID Primer](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/draft-documents/did-primer.md)
* [Decentralized IDentifers (DIDs)](https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf) 
* DID Auth
   * [DID auth and the Little I-am-Me](https://medium.com/@markus.sabadello/did-auth-and-the-little-i-am-me-ec14d757ff09)
   * [Introduction to DID Auth](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/did-auth.md)
   * [Introduction to DID Auth for SSI – Markus Sabadello – Webinar 10](http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10/)
* [A Universal Resolver for self-sovereign identifiers](https://medium.com/decentralized-identity/a-universal-resolver-for-self-sovereign-identifiers-48e6b4a5cc3c)
* [@ChristopherA on DID adoption](https://twitter.com/ChristopherA/status/989122017348784130)
   > "22/ Over a dozen companies and organizations, using multiple blockchains (Bitcoin, Ethereum, Hyperledger, etc.), have committed to deploying DIDs, including IBM, Microsoft, Digital Bazaar, Consensys, Evernym, Learning Machine, British Columbia, and more:" —[How blockchain could solve the internet privacy problem](https://www.computerworld.com/article/3267930/blockchain/how-blockchain-could-solve-the-internet-privacy-problem.html)
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
* [Veres One DID Method 1.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/did-method-veres-one.md) — a permissionless public ledger designed specifically for the creation and management of decentralized identifiers (DIDs)

### EU General Data Protection Regulation Act

* [Blockchains and Data Protection in the European Union](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3080322)
* [IBM — How blockchain could address five areas associated with GDPR compliance](https://www-01.ibm.com/common/ssi/cgi-bin/ssialias?htmlfid=61014461USEN)
* [GDPR - A reflection on the 'self-sovereign identity' and the Blockchain](https://www.linkedin.com/pulse/gdpr-reflection-self-sovereign-identity-blockchain-nicolas-ameye/)
* [GDPR and Privacy by Design, What developers need to know](https://medium.com/@sphereidentity/gdpr-and-privacy-by-design-what-developers-need-to-know-fa5a936da65a)
* [Privacy by Design The 7 Foundational Principles](https://www.ipc.on.ca/wp-content/uploads/Resources/7foundationalprinciples.pdf)
* [When GDPR Becomes Real, and Blockchain is no longer fairydust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/gdpr.md)
* [Privacy Impact Assesment (PIA)](https://en.wikipedia.org/wiki/Privacy_Impact_Assessment) — a process which assists organizations in identifying and minimizing the privacy risks of new projects or policies.

### Self Sovereign Identity

![](http://imgur.com/3zz62kpl.png)

* [WebOfTrustInfo/self-sovereign-id](https://github.com/WebOfTrustInfo/self-sovereign-identity)
* [Self-Sovereign Identity: Why Blockchain?](https://www.ibm.com/blogs/blockchain/2018/06/self-sovereign-identity-why-blockchain/)
* [A Technlogy-Free Definition of Self-Sovereign Identity (SSI)](https://github.com/jandrieu/rebooting-the-web-of-trust-fall2016/raw/master/topics-and-advance-readings/a-technology-free-definition-of-self-sovereign-identity.pdf) 
* [Self-Sovereign Identity Principles](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md)
* [Inevitable Rise of Self-Sovereign Identity](https://sovrin.org/wp-content/uploads/2018/03/The-Inevitable-Rise-of-Self-Sovereign-Identity.pdf)
* [Experts talk Self-Sovereign Identity](https://www.coindesk.com/experts-talk-self-sovereign-identity-implementing-systems/)
* [Self-Sovereign Privacy By Design](https://github.com/sovrin-foundation/protocol/blob/master/self_sovereign_privacy_by_design_v1.md)
* [Self-Sovereign Identity — wiki.p2pfoundation](https://wiki.p2pfoundation.net/Self-Sovereign_Identity)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">0/ “Self-Sovereign Identity: A Progress Report”…</p>&mdash; Christopher Allen (@ChristopherA) <a href="https://twitter.com/ChristopherA/status/989120215702261761?ref_src=twsrc%5Etfw">April 25, 2018</a></blockquote>

### Evernym

![](http://untangled.world/wp-content/uploads/2017/08/everynym-logo-1400x357.png)

* [Evernym](https://www.evernym.com/) [[**t**](https://twitter.com/evernym)]
* [The Three Models of Digital Identity Relationships — How self-sovereign identity (SSI) is different, and why it’s better](https://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186)
* [Is Self-Sovereign Identity the ultimate GDPR compliance tool? [1\3]](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-9d8110752f89) [[**2**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-40db94c1c437)][[**3**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-7296a3b07769)]

### The Sovrin Foundation

![](https://www.evernym.com/wp-content/uploads/2017/04/logo-large.png)

* The [Sovrin](https://sovrin.org/)[[**f**](https://forum.sovrin.org/)][[**c**](https://sovrin-slack-signup.herokuapp.com/)][[**t**](https://twitter.com/SovrinID)][[**g**](https://github.com/sovrin-foundation/sovrin)][[**d**](https://sovrin.org/library/)]
 Foundation is creating a public instance of [Hyperledger](#Hyperledger-Indy) Indy's code, which was initially developed by [Evernym](#Evernym)
* [Getting Started with Sovrin](https://sovrin.org/library/getting-started-with-sovrin/)
* [Sovrin: digital identities in the blockchain era](https://sovrin.org/library/sovrin-digital-identities-in-the-blockchain-era/)
* [Sovrin: A Protocol and Token for Self-Sovereign Identity and Decentralized Trust](https://sovrin.org/wp-content/uploads/Sovrin-Protocol-and-Token-White-Paper.pdf)
* [Sovrin Governance Framework](https://sovrin.org/library/sovrin-governance-framework/)
* [How Sovrin Works—A Technical Guide from the Sovrin Foundation](https://sovrin.org/wp-content/uploads/2018/03/How-Sovrin-Works.pdf)
* [Sovrin Network: What Goes on the Ledger?](https://sovrin.org/wp-content/uploads/2018/10/What-Goes-On-The-Ledger.pdf)
* [Sovrin Test Network Trust Anchor Registration](https://s3.us-east-2.amazonaws.com/evernym-cs/sovrin-STNnetwork/www/trust-anchor.html)[[**f**](https://forum.sovrin.org/t/testing-on-the-sovrin-test-network-stn/643/17)]

#### Windley
* [The Sovrin Foundation](http://www.windley.com/archives/2018/07/the_sovrin_foundation.shtml)
* [A Universal Trust Framework](http://www.windley.com/archives/2017/01/a_universal_trust_framework.shtml)
* [Is Sovrin Decentralized?](http://www.windley.com/archives/2017/09/is_sovrin_decentralized.shtml)
* [Decentralization in Sovrin](http://www.windley.com/archives/2018/10/decentralization_in_sovrin.shtml)
* [Decentralization and Distributed Ledgers](http://www.windley.com/archives/2016/08/decentralization_and_distributed_ledgers.shtml)
* [An Internet for Identity](http://www.windley.com/archives/2016/08/an_internet_for_identity.shtml)
* [The Case for Decentralized Identity](http://www.windley.com/archives/2017/08/the_case_for_decentralized_identity.shtml)
* [Building Your Business on Sovrin: Domain-Specific Trust Frameworks](http://www.windley.com/archives/2018/03/building_your_business_on_sovrin_domain-specific_trust_frameworks.shtml)


##### Tykn Tech

![](http://imgur.com/1uO0AWll.png)

* [Tykn *The Future of Resilient Identity*](https://tykn.tech/) | [twitter](https://twitter.com/Tykn_tech) | [github](https://github.com/tykntech)
* [Tykn: Extended Overview](https://docs.google.com/document/d/1pNRO6aOb5eK4s8PVv7yS4x9TkqrGglCJ4jebU1F3Yzo/edit#)
* [Digital Identity Management in the Context of GDPR & Sovrin —Why Data Privacy Matters & How to Protect It](https://blog.tykn.tech/digital-identity-management-in-the-context-of-gdpr-sovrin-43028247378b)


### Hyperledger Indy

![](https://www.osiztechnologies.com/asset/oimages/hyperledger_indy/hyperledger_indy_02.png)

* [Hyperledger Indy - *Distributed Ledger and Utility Library*](https://www.hyperledger.org/projects/hyperledger-indy) | [twitter](https://twitter.com/Hyperledger) | [wiki](https://wiki.hyperledger.org/projects/indy/documentation)
* [The Rise of Self-Sovereign Identity - Hyperledger Indy](https://wso2.com/blog/research/the-rise-of-self-sovereign-identity-hyperledger-indy)
* [Hyperledger Welcomes Project Indy](https://www.hyperledger.org/blog/2017/05/02/hyperledger-welcomes-project-indy)
* [Plenum Bzantine Fault Tolerant Protocol](https://github.com/hyperledger/indy-plenum/wiki)
   * "Byzantine fault tolerance is a sub-field of fault tolerance research inspired by the Byzantine Generals' Problem, which is a generalized version of the Two Generals' Problem."
* [An Accumulator Based on Bilinear Maps and Efficient Revocation for Anonymous Credentials](https://eprint.iacr.org/2008/539.pdf)
* [An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation](https://www.iacr.org/archive/eurocrypt2001/20450093.pdf)
* [SecureKey Technologies to explore interoperability between Verified.Me and Hyperledger Indy](https://securekey.com/press-releases/hyperledger-indy/)
* The Linux Foundation's [Blockchain for Business](https://www.edx.org/professional-certificate/linuxfoundationx-blockchain-for-business) edx course may be freely audited has a section about Indy. 


#### IDEMix 
  — Zero Knowledge Proof's in Evernym—Indy

>Our zero-knowledge proofs are part of the [Idemix protocol](http://domino.research.ibm.com/library/cyberdig.nsf/papers/EEB54FF3B91C1D648525759B004FBBB1/%24File/rz3730_revised.pdf), where they are used to prove the possession of [Camenisch-Lysyanskaya credentials](https://eprint.iacr.org/2001/019.pdf). We also use zero-knowledge proofs in the revocation protocol, which is based on [cryptographic accumulators](https://eprint.iacr.org/2008/539.pdf). —*[What Zero Knowledge Poof Algorithm is used in Sovrin?](https://forum.sovrin.org/t/what-zero-knowledge-proof-algorithm-is-used-in-sovrin/71/2)*

>Identity Mixer is not directly (re)implemented by Sovrin, but its cryptographic foundations are very similar, and Sovrin’s implementation includes most of its extended features (predicates, multi-credential, revocation, advanced issuance…). One of the researchers who helped to create Identity Mixer is on Sovrin’s Technical Governance Board and has offered insight to keep the implementations aligned on goals and methods. 
>—*[How is IDEMix Implemented?](https://forum.sovrin.org/t/how-idemex-is-implemented-in-sovrin-indy/)*

* [IBM Identity Mixer](https://www.zurich.ibm.com/identity_mixer/) | [blog](https://idemix.wordpress.com/)
  * [idemix in Hyperledger Fabric](https://hyperledger-fabric.readthedocs.io/en/release-1.3/idemix.html)
* [Concepts and Features of Privacy-Preserving Attribute-Based Credentials](https://github.com/p2abcengine/p2abcengine/wiki/Concepts-and-features)
* [AnonCreds: Anonymous credentials protocol implementation in python](https://github.com/hyperledger/indy-anoncreds)
* [Anoncred — Usecase](https://github.com/hyperledger/indy-anoncreds/blob/master/docs/anoncred-usecase1.pdf)


### IBM

* [github.com/IBM-Blockchain-Identity](https://github.com/IBM-Blockchain-Identity)
* [How do we start tackling the existing identity problem](https://www.ibm.com/blogs/blockchain/2018/06/how-do-we-start-tackling-the-existing-identity-problem/)
* [Swipe Right on Verifiably Credentials](https://developer.ibm.com/code/2018/05/22/swipe-right-on-verifiable-credentials/)
* [WISeKey fully deployed its CertifyID integrating Digital Identity with Blockchain technology](https://globenewswire.com/news-release/2018/07/11/1535718/0/en/WISeKey-fully-deployed-its-CertifyID-integrating-Digital-Identity-with-Blockchain-technology.html)
* [SecureKey](http://securekey.com/): [partners with IBM](http://www-03.ibm.com/press/us/en/pressrelease/51841.wss) to enable a new digital identity and attribute sharing network based on Hyperledger Fabric blockchain.


### Ethereum

![](http://imgur.com/Fc6Hoo9l.png)

* [Decentralized Digital Identity on Ethereum](www.slideshare.net/FabriceCroiseaux/ethcc-2018-decentralized-digital-identity-on-ethereum) -SlideShare
* [ERC725](https://github.com/ethereum/EIPs/issues/725) | [ERC735](https://github.com/ethereum/EIPs/issues/735)
   * proposals in the Ethereum community to standardize smart contracts for certain identity-related operations such as key management, as well as signing transactions, documents, and "claims", which may be attested by third parties or self-asserted.
* [Proof-of-Individuality](http://proofofindividuality.online/) — how to prove a person only has one account
   * [Anti-Sybil Protocol using virtual pseudonym parties](https://medium.com/@unlisted/anti-sybil-protocol-using-virtual-pseudonym-parties-10276fcf3b20)
* [Different Approaches to Ethereum Identity Standards](https://medium.com/uport/different-approaches-to-ethereum-identity-standards-a09488347c87) 
* [Managing Identity with a UI—ERC-725](https://medium.com/originprotocol/managing-identity-with-a-ui-for-erc-725-5c7422b38c09)
* [Ethereum ERC725 Blockchain Based, Self-Sovereign Identity Management](https://bitcoinexchangeguide.com/ethereum-erc725-blockchain-based-self-sovereign-identity-management/)
* [A Decentralized Approach to Blockcerts Credential Revocation](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/blockcerts-revocation.md)
* [DEVCON1: Digital Identity](https://www.youtube.com/watch?v=QpaTOvAhLR4) — video from DEVCON1

#### Ethereum Identity Applications 
* [uPort](https://www.uport.me/) [[**g**](https://github.com/uport-project/)][[**t**](https://twitter.com/uport_me)]
   * [Ethereum studio ConsenSys launches 'Internet-of-People' with digital IDs and assets secured on Ubuntu phones](http://www.ibtimes.co.uk/ethereum-studio-consensys-launches-internet-people-digital-ids-assets-secured-unbuntu-phones-1542620)
   * [Year in Review. What's to come in 2018](https://medium.com/uport/uport-year-in-review-whats-to-come-in-2018-15ccb9214439)
* [Nuggets](http://www.nuggets.life/) [[**wp**](https://nuggets.life/images/Nuggets-White-Paper.pdf)]
   * "is a blockchain platform giving users a single biometric tool for login, payment and identity verification. It stores an individual's information in a "personal cloud" in "zero-knowledge blockchain storage".
* [Jolocom](http://jolocom.com/) 
   * a "SmartWallet" for everyone to own their personal digital identity, using [Social Linked Data](https://github.com/solid/solid-spec), WebID, and verifiable claims standards, as well as Ethereum smart contracts. 
* [Democracy Earth Foundation](http://democracy.earth/) | [github](https://github.com/DemocracyEarth/paper)| [sovereign.software](http://sovereign.software/)
   * developing "Sovereign", a blockchain direct democracy tool using "vote" tokens to grant democratic participation rights to every human. A proof-of-individuality (POI) process based on peer-to-peer validation establishes that a self-sovereign identity is uniquely tied to a single person. The project introduces a number of interesting socio-technical concepts such as "Social Smart Contract", "Initial Rights Offering", and "Cryptographically Induced Equality". Cooperation is happening with other decentralized identity initiatives such as Blockstack and uPort.
* [Ockam](https://www.ockam.io/) — creating a ERC20 based platform that registers IOT devices to a blockchain to solve systemic security and interoperability problems.


### State Led Initiatives

* [Identity Validation as a Public Sector Digital Service?](https://blog.aniljohn.com/2014/07/identity-validation-as-a-public-sector-digital-service.html)
* [Federal Funding for Blockchain Security and Identity Verification Technologies](https://blog.aniljohn.com/2015/12/federal-gov-funds-for-identity-r-and-d.html)

#### Canada
* [White Paper: Canada’s Digital ID Future - A Federated Approach](https://www.cba.ca/embracing-digital-id-in-canada)
* [BCGov Verifiable Organization Network – Impressive Client Demo](https://www.continuumloop.com/bcgov-verifiable-organization-network/)
* [Verified Organization Network](https://vonx.io/) | [github](https://github.com/bcgov/von) 
   * "an initiative by the government of British Columbia to create a trusted network of organizational data. It allows organizations to claim credentials that are part of their own digital identity, using a component called [TheOrgBook](https://github.com/bcgov/theorgbook) that lists entities with their associated public verifiable claims."

#### Netherlands
* [TU Delft helps develop digital ID for use on your phone](https://www.tudelft.nl/en/2018/tu-delft/tu-delft-helps-develop-digital-id-for-use-on-your-phone/)
* [Self-Sovereign Identity Systems for Humanitarian Interventions—A Case Study on Protective Cash Transfer Programs](https://repository.tudelft.nl/islandora/object/uuid:6cdb5450-9a81-47a9-8ffa-f9bd77c72448/datastream/OBJ1/download)
* [Deployment of a Blockchain-Based Self-Sovereign Identity - Delft](https://arxiv.org/pdf/1806.01926.pdf)
* [TrustChain: A Sybil-resistant scalable blockchain - Presentation](http://msn.iecs.fcu.edu.tw/report/download.php?)
* [Dutch Blockchain Coalition](https://www.dutchdigitaldelta.nl/en/blockchain) | [Action Agenda](https://dutchdigitaldelta.nl/uploads/pdf/Dutch-Blockchain-Coalition-action-agenda-ENG.pdf)

#### USA
* [Illinois Blockchain Initiative](https://illinoisblockchain.tech/) — [partners with Evernym to launch birth registration pilot](https://illinoisblockchain.tech/illinois-partners-with-evernym-to-launch-birth-registration-pilot-f2668664f67c)


#### Spain
* [Alastria](https://alastria.io/) [[**g**](https://github.com/alastria/alastria-identity)] 
   * a non-profit consortium building a national blockchain ecosystem for Spain. The security and veracity of information will be ensured through the identification of natural and legal persons, while at the same time allowing citizens to have control over their personal information in a transparent way following the guidelines set by the European Union.

#### Switzerland
* [Zug ID: Exploring the First Publicly Verified Blockchain Identity](https://medium.com/uport/zug-id-exploring-the-first-publicly-verified-blockchain-identity-38bd0ee3702)

#### Estonia
* [Estonia National Blockchain-ID](https://e-estonia.com/solutions/e-identity/id-card/) | [id.ee](https://www.id.ee/)
   * [Estonian Blockchain ID Security Flaw](https://www.mccarthy.ca/en/insights/blogs/cyberlex/estonian-blockchain-based-id-card-security-flaw-raises-issues-about-identity)

### Assorted Decentralized \ Blockchain ID Initiatives
* [Danube Tech](http://danubetech.com/) — digital identity and personal data, including personal agents, semantic graphs, and blockchain | [xdi](https://xdi2.org) | [navigator](https://github.com/projectdanube/xdi2)
* [Cambridge Blockchain](http://cambridge-blockchain.com/) — Blockchain for validating secure digital identity documents, processing electronic signatures, and recording transactions."
* [Identity at Coinbase: Welcoming the Distributed Systems team](https://blog.coinbase.com/identity-at-coinbase-welcoming-the-distributed-systems-team-d929dd64de2e)
* [Proof of Authority](https://blockonomi.com/proof-of-authority/)
* [Blockstack](https://blockstack.org/) [[**g**](https://github.com/blockstack)][[**f**](https://forum.blockstack.org/)][[**b**](https://blockstack.org/blog)][[**t**](https://twitter.com/blockstack)]
   * a network of computers that collectively maintain a global registry of domain names, public keys, and cryptographic hashes. With this registry, Blockstack serves as a decentralized domain name system (DNS) and a decentralized public key infrastructure (PKI).
   * [Onename](https://onename.com/) — "a product built on Blockstack that allows people to register identities"
* [Shocard](https://shocard.com/) — "Blockchain-Based Mobile Identity Platform"
* [Mydata](http://mydata.org/)[[**t**]](https://twitter.com/mydataorg)[[d]](https://mydata.org/papers/) [declaration](https://mydata.org/declaration/)
   * goal: to empower individuals with their personal data, thus helping them and their communities develop knowledge, make informed decisions, and interact more consciously and efficiently with each other as well as with organisations."
   * [Consent](http://www.consent.global/)[[**12**](https://sovrin.org/steward/global-consent/)] — "platform for trusted personal data applications and services, using Ethereum smart contracts to implement decentralized identifiers, verified credentials, consent receipts, a web of trust, and exchange of assets and value." 
* [Authenteq](http://authenteq.com/)[[**t**](https://twitter.com/authenteq)] — enables users to create their own sovereign digital IDs which are stored encrypted in a blockchain.
* [JLinc](https://www.jlinc.com/") — registers cryptographic public keys on the Stellar blockchain.
* [CheapID](http://guptaoption.com/cheapid/)
* [Deloitte SmartID](http://www.deloitte.co.uk/smartid/)
* [Internet of People](https://iop.global/) — "an open, decentralized infrastructure consisting of device-to-device communication, blockchain tokens, profile servers, and other components."
* [Blockchain Helix](http://blockchain-helix.com)[[**ico**](https://ico.helix-orange.com/)][[**wp**](https://ico.helix-orange.com/wp-content/uploads/2018/08/HELIX-Orange_Whitepaper_v1.5.pdf)]
   * "Identity as a Service", "Data as a Service" and "Blockchain as a Service" The company offers to increase the speed of KYC/AML processes while hughly decreasing the cost 
* [The Humanized Internet](http://www.thehumanizedinternet.org/) — "to defend the rights of vulnerable people, and give every human being worldwide secure, sovereign control over their own digital identity."
* [Civic](https://www.civic.com/) launches: [identity.com](https://identity.com)[[**g**](https://github.com/identity-com/)][[**b**](https://www.civic.com/blog/identity-com-first-open-source-update/)]
* [Mooti](https://mooti.co/) | [docs](https://docs.mooti.co/)
   * offers an "identity chain" technology that makes it possible to issue and revoke verified claims using elliptic curve cryptography (curve25519, secp256k1) and includes privay-enhancing features
* [Banqu](http://www.banquapp.com/) —"focuses on establishing 'economic identity' for those who are excluded from the global economy."
* [Vida Identity](https://getvida.io) — "enables distributed key revocation and reissuance. Access to data is always permissioned across applications and services."
* [ÆTERNITY](http://aeternity.com/) | [github](https://github.com/aeternity/protocol) 
   * Is focusing on improved smart contract capabilities such as better scalability and easier integration of off-chain data. It offers an identity architecture where every account has a unique ID number, and unique names can be registered and linked to arbitrary data such as addresses on the blockchain. Schema.org's data structures are used for representing data about persons and organizations."
   * [Schema](https://schema.org) — a collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet. Schema.org vocabulary can be used with many different encodings, including RDFa, Microdata and JSON-LD. These vocabularies cover entities, relationships between entities and actions, and can easily be extended through a well-documented extension model. Over 10 million sites use Schema.org to markup their web pages and email messages. Many applications from Google, Microsoft, Pinterest, Yandex and others already use these vocabularies to power rich, extensible experiences."
* [Spidchain](http://www.spidchain.com/) | [whitepaper](https://drive.google.com/file/d/0B89WE3IIHmy1Z0ZSSWVmVEtaaG8/view)
   * "offers a platform for self-sovereign identity, including desktop and mobile apps for end-users. It uses Decentralized Identifiers (DIDs) - backed by optionally Bitcoin or Ethereum - to implement a marketplace for verifiable claims. The Spidchain applications allow individuals to create, recover, and revoke DIDs, to authenticate, to sign and verify files and claims, and more."
* [Reddcoin — Redd-ID](https://www.reddcoin.com/service/redd-id/) | [forum](https://www.reddcointalk.org/) | [PoSV whitepaper](https://www.reddcoin.com/papers/PoSV.pdf)
   * a naming service that allows usernames to be registered on the Reddcoin blockchain.
* [Pro-civis](https://procivis.ch) — "e-government as a service" platform called "eID+". It enables citizens to get an official, electronic Citizen-ID on a mobile app, which can be used for secure and convenient login to websites, and the electronic signing and safe storage of documents. Verification providers such as state authorities can use a web backend or an API to attest to the correctness of a citizen's personal data. 
   * The platform includes the [Vetri](https://vetri.global/) wallet and marketplace. 'Earn extra income and rewards by joining the data economy.'"
* [Cicada](https://github.com/the-laughing-monkey/cicada-platform)
   * a Dapp platform built for a "direct democracy" use case. It envisions using iris scans to generate decentralized universal identifiers ("HUIDs") for every human on the planet, a method referred to as "biocryptics". "HUIDs" can have "sub-IDs" to support selective disclosure. PII can be stored in an "info wallet". Key parts of the system also include smart contracts, zero-knowledge proofs, mixnets, and more."
* [BitID](https://github.com/bitid/bitid) — an authentication protocol based on Bitcoin identities, supported by some of the Bitcoin wallets. It authenticates Bitcoin addresses by signing a cryptographic challenge 
* [Blockcerts](https://www.blockcerts.org) — open standard for issuing and verifying blockchain-based official records; The project offers  open-source libraries, tools, and mobile apps. MIT has [issued](https://www.insidehighered.com/news/2017/10/19/mit-introduces-digital-diplomas) digital certificates based on this standard.
* [Keyp](https://keyp.io/) —"Welcome to Europe’s fastest growing open digital identity ecosystem."
* [I/O Digital Foundation](https://iodigital.io/) | [whitepaper](https://simplebooklet.com/iocoinwhitepaper#page=0)
   * "offers a Proof-of-Stake blockchain called Decentralised Input Output Name Server (DIONS). It will enable applications such as identity and alias registration, storage of legal documents, key exchange, and encrypted messaging."
* [iRespond](https://www.irespond.org/)
* [World Identity Netowork —Blockchain for Impact](https://win.systems/)
* [Mooti](https://mooti.co/) - Mooti is reimagining the security and utility of personally identifiable information and authentication based on our self-sovereign identity solutions, asymmetrical encryption, and blockchain technology.


### Data Wallet \ Marketplaces

* [Pillar Project](http://pillarproject.io) | [grey—paper](https://pillarproject.io/documents/Pillar-Gray-Paper.pdf)
   * planning to offer a "Personal Data Locker" consisting of a wallet, browser, and token exchange. Personal assets will be put on a blockchain, and "Pillar" tokens will be issued."
* [Aversafe](https://www.aversafe.com/) —"allows individuals to store personal details, work history, certificates and achievements. It leverages a permissioned blockchain for trusted audit and participation in the storage of attestation data separate from the actual data stored"
* [Datum](https://datum.org) | [whitepaper](https://datum.org/assets/Datum-WhitePaper.pdf)
   * "network allows anyone to store structured data on a smart contract blockchain. Data can optionally be bought and sold on a marketplace using the DAT token. Datum leverages BigchainDB and IPFS as data storage backends. All data is encrypted and protected using AES256-GCM.
* [ONTology](https://ont.io/) | [github](https://github.com/ontio/ontology-DID)— "a "Distributed Trust Network" which combines a cross-chain identity system, peer-to-peer data transmission, data authorization mechanisms, distributed data storage, attestation, and various industry-specific modules. It also includes an Ontology Crypto Package (OCP) and an Ontology Marketplace (OM)."
* [We can do better than selling our data](http://blogs.harvard.edu/doc/2018/09/18/data/)-Doc Searls(*IIW*)

### Decentralized Identity Foundation 

![](http://imgur.com/PXGV6Xyl.png)

* [Decentralized Identity Foundation](http://identity.foundation/) (DIF) [[**g**](https://github.com/decentralized-identity)][[**t**](https://twitter.com/DecentralizedID)][**b**](https://medium.com/decentralized-identity)] 
* the following links highlight *something each member adds* to the DID ecosystem:
   - Members include: [Microsoft](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE2DjfY), [uPort](https://github.com/uport-project/ethr-did/blob/develop/docs/index.md), [IBM](https://www.ibm.com/blogs/blockchain/2018/06/self-sovereign-identity-why-blockchain/), [Sovrin](https://github.com/sovrin-foundation/sovrin/blob/master/spec/did-method-spec-template.html), [SecureKey](https://www.ibm.com/blogs/blockchain/2018/05/self-sovereign-identity-our-recent-activity-as-a-sovrin-steward/), [Blockstack](https://github.com/blockstack/blockstack-core/blob/feature/docs-bns/docs/blockstack_naming_service.md#decentralized-identifiers-dids), [Evernym](https://www.evernym.com/wp-content/uploads/2017/07/What-Goes-On-The-Ledger.pdf), [Hyperledger](https://github.com/hyperledger/indy-sdk/blob/master/doc/getting-started/getting-started.md), [Civic](https://www.civic.com/solutions/kyc-services/), [Accenture](https://www.accenture.com/us-en/insight-blockchain-id2020), [Danube](https://github.com/projectdanube/xdi2), [netki](https://bravenewcoin.com/insights/netki-launches-digital-id-solution-which-bitt-is-using-with-central-banks-in-the-caribbean), [RSA](https://www.rsa.com/en-us/research-and-thought-leadership/rsa-labs), [Consent](https://sovrin.org/steward/global-consent/), [IOTA](https://medium.com/@iotasuppoter/iota-the-case-of-decentralized-digital-identity-de7b95042c12), [Mooti](https://www.cio.com/article/3147358/it-industry/ibm-building-blockchain-ecosystem.html), [r3](https://www.gemalto.com/press/pages/gemalto-and-r3-pilot-blockchain-technology-to-put-users-in-control-of-their-digital-id.aspx), [Authenteq](https://venturebeat.com/2018/08/30/authenteq-launches-blockchain-identity-verification-to-stop-online-trolls/), [Blockchain-foundry](https://www.blockchainfoundry.co/blockchain-foundry-inc-announces-new-software-release-for-blockchain-based/), [Validatedid](https://www.validatedid.com/vidchain-the-future-of-digital-identity/), [1kosmos](https://onekosmos.com/product-details/), [gamecredits](https://medium.com/@gamecredits/introducing-blinking-blink-identity-management-on-the-blockchain-9258c7d76a8d)[[*](https://blinking.id)], [auth0](https://auth0.com/), [jolocom](https://stories.jolocom.com/jolocom-brings-blockchain-identity-to-privacy-week-berlin-acdaee665f0), [Enigma](https://blog.enigma.co/off-chain-identity-claims-with-enigma-2d5b23c31f92), [Humanized-internet](https://www.thehumanizedinternet.org/), [Pillar](https://pillarprojectfoundation.org/blog/announcing-the-pillar-project/), [id2020](https://id2020.org/manifesto/), [Nuggets](https://www.mobilepaymentstoday.com/news/identity-and-payments-platform-nuggets-partners-with-iot-company/).

* [Decentralized Identity Foundation Grows To 56 Members In Our First Year](https://medium.com/decentralized-identity/decentralized-identity-foundation-grows-to-56-members-in-our-first-year-3ec117e811d8)
* [*Identity Hubs Capabilities Perspective*](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/identity-hubs-capabilities-perspective.md) - Identity Hubs currently proposed in the Decentralized Identity Foundation (DIF) are a subset of a general Decentralized Identifier (DID).

![](https://oneworldidentity.com/wp-content/uploads/2018/10/companies.png)

2018 Identity Landsacpe brought to you by: [One World Identity](https://oneworldidentity.com/) — independent advisory and digital strategy consultancy focused on trust and the data economy.

### Reports
* [Global Blockchain Identity Management Market 2018-2022](https://www.technavio.com/report/global-blockchain-identity-management-market-analysis-share-2018)
* [How Blockchain Revolutionizes Identity Management](https://www.accenture-insights.nl/en-us/articles/how-blockchain-will-revolutionize-identity-management)
* [Digital Identity: the current state of affairs](https://www.bbvaresearch.com/wp-content/uploads/2018/02/Digital-Identity_the-current-state-of-affairs.pdf)
* [Blockchain: Evolving Decentralized Identity Design](https://www.gartner.com/doc/3834863/blockchain-evolving-decentralized-identity-design)
* [White Paper: Canada’s Digital ID Future - A Federated Approach](https://www.cba.ca/embracing-digital-id-in-canada)
* [IDENTITY MATTERS](https://cboxxtest.files.wordpress.com/2017/09/cboxxidentitymatters04.pdf)
* [Accenture: ID2020: DIGITAL IDENTITY with Blockchain and Biometrics](https://www.accenture.com/us-en/insight-blockchain-id2020)
* [Privacy-Preserving Authentication, Another Reason to Care about Zero-Knowledge Proofs —slideshare](https://www.slideshare.net/eralcnoslen/privacypreserving-authentication-another-reason-to-care-about-zeroknowledge-proofs)
* [r3- Identity in Depth](https://www.r3.com/wp-content/uploads/2017/06/Identity_indepth_r3.pdf)


### Research-Papers
* [Establishing Identity Without Certification Authorities](http://irl.cs.ucla.edu/~yingdi/pub/papers/Ellison-OldFriend-USENIX-Security-1996.pdf)
* [A First Look at Identity Management Schemes on the Blockchain](https://arxiv.org/pdf/1801.03294.pdf)
* [ChainAnchor — Anonymous Identities for Permissioned Blokchains](http://connection.mit.edu/wp-content/uploads/sites/29/2014/12/Anonymous-Identities-for-Permissioned-Blockchains2.pdf)
* [Decentralizing Privacy: Using Blockchain to Protect Personal Data](http://web.media.mit.edu/~guyzys/data/ZNP15.pdf)
* [TOWARDS SELF-SOVEREIGN IDENTITY USING BLOCKCHAIN TECHNOLOGY](http://essay.utwente.nl/71274/)
* [Self-sovereign Identity –	Opportunities and Challenges for the Digital Revolution](https://arxiv.org/pdf/1712.01767.pdf)
* [The Knowledge Complexity Of Interactive Proofs](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.419.8132&)
* [SCPKI: A Smart Contract-based PKI and Identity System](http://www0.cs.ucl.ac.uk/staff/M.AlBassam/publications/scpki-bcc17.pdf)

### Selected *Rebooting Web of Trust* [Whitepapers](https://www.weboftrust.info/papers.html) 
* [Creating the New World of Trust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/whats-the-next-step.pdf)
* [Framework for the Comparison of Identity Systems](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/Framework-for-Comparison-of-Identity-Systems.md)
* [A Primer on Functional Identity](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/functional-identity-primer.md)
* [The DCS Theorem](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/dcs-theorem/The-DCS-Theorem.md) — We use the triangle to show decentralized consensus systems can have _Decentralization_, _Consensus_, or _Scale_, but not all three properties simultaneously.
* [Identity Crisis: Clear Identity through Correlation](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/identity-crisis.pdf)
* [Decentralized Public Key Infrastructure](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/dpki.pdf)
* [SSI: A Roadmap for Adoption](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/a-roadmap-for-ssi.md)

#### RWoT Use Cases
  —infogrphic workflow examples 
* [Amira 1.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/amira.md)
* [Re-Imagining What Users Really Want](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2017/blob/master/final-documents/what-users-really-want.md)
* [Joram 1.0.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2016/blob/master/final-documents/joram-engagement-model.pdf)
* [Powering the Physician-Patient Relationship with HIE of One Blockchain Health IT](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/physician-patient-relationship.pdf)
* [Protecting Digital Identities in Developing Countries](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/protecting-digital-identities-in-developing-countries.pdf)
* [Opportunities Created by the Web of Trust for Controlling and Leveraging Personal Data](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/satisfying-real-world-use-cases.pdf)

### Video
* [Is Blockchain the Future of Digital Identity?](https://youtu.be/Aub5dNpj2_k) -CB Insights
* [Identity and Blockchain Technology](https://www.youtube.com/watch?v=Aub5dNpj2_k)
* [Phil Windley on the Sovrin Network](https://www.youtube.com/watch?v=IxQUL2ztFi8)
* [Self-Sovereign Identity with Hyperledger Indy\Sovrin- Calvin Cheng - FOSSASIA 2018](https://www.youtube.com/watch?v=hfyIZu3_fw8)


### People

* [Manu Sporny](https://digitalbazaar.com/blog/) | [twitter](https://twitter.com/manusporny)
* [Markus Sabadello —Peacekeeper](https://danubetech.com/)  [uniresolver.io](https://uniresolver.io/) | [twitter](https://twitter.com/peacekeeper) | [github](https://github.com/peacekeeper) | [medium](https://medium.com/@markus.sabadello)

### Resources
* [wiki.idcommons.net](http://wiki.idcommons.net/Main_Page)
* [/WebOfTrustInfo](https://github.com/WebOfTrustInfo/)
* [/peacekeeper/blockchain-identity](https://github.com/peacekeeper/blockchain-identity)
* [blockchain-id.toml](https://github.com/infominer33/awesome-decentralized-id/blob/master/blockchain-id.toml)

---

### Brought to you by: [The Crypto Library—Super Source](https://github.com/infominer33/Crypto-library)


A few of us are building a library of crypto knowledge on a discord server. Now those resources are migrating to github, to become a database and power web-portal\chat bot. I began working on this document after entering all of the DID resources I could find into [blockchain-id.toml](https://github.com/infominer33/awesome-decentralized-id/blob/master/blockchain-id.toml).  

Self-Sovereign Identity is one of my favorite subjects, which is how this became the [Crypto-library](https://github.com/infominer33/Crypto-library)'s first side-project. 


#### BTC— 1GvkjHtiy9LUjVkStnEAXxjhcoS56aCokY
 
![](http://imgur.com/xMd9r0rl.png)       ![http://crypt0library.net](http://imgur.com/0rvKAhll.png)

—infominer@protonmail.com
