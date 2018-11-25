# The Sovrin\Indy\DID Foundations, Architecture, and Ecosystem -DRAFT

// Will gather here all resources that specifically relate to Sovrin, and Indy. Gradually this file will grow with Sovrin related material. While '[awesome-decentralized-id](/readme.md)' will be gradually shed of some resources which are more specific to sovrin\indy and less so to the greater decentralized-id ecosystem.
### Contents
* [Introduction](#Introduction)
* [Self Sovereign Identity—SSI](#Self-Sovereign-Identity)
* [Evernym](#Evernym)
* [The Sovrin Foundation](#The-Sovrin-Foundation)
  * [Windley.com](#Windley)
* [Hyperledger Indy](#Hyperledger-Indy)
  * [Idemix](#IDEMix)
* [Video](#Video)
* [RWoT Whitepapers](#Selected-Rebooting-Web-of-Trust-Whitepapers)
  * [RWoT Use Cases](#RWoT-Use-Cases) -infographic workflow
* [World Wide Web Consortium—W3C](#World-Wide-Web-Consortium)
  * [DID the Decentralized Identifier](#DID-the-Decentralized-Identifier) 
* [GDPR](#EU-General-Data-Protection-Regulation-Act)
* [Indy \ Sovrin Adoption](#Indy\Sovrin-Adoption)
  * [DID Adoption](#DID-Adoption)
* [Sources](#Sources)

### Introduction

 Additional history and background information may be found at [awesome-decentralized-id](/README.md).

* [Christopher Allen](http://www.lifewithalacrity.com/)[[**T**](https://twitter.com/ChristopherA)][[**git**](https://github.com/ChristopherA)] details the overarching history of internet idenitity standards in his seminal work: 
   **[The Path to Self-Soverereign Identity](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)**[[**3**](https://www.coindesk.com/path-self-sovereign-identity/amp/)].
 

 **[IIW-Wiki](http://iiw.idcommons.net/Main_Page)** | **[identitywoman.net](https://identitywoman.net/)** | **[windley.com-#identity](http://www.windley.com/tags/identity.shtml)** | **[WoTinfo](https://github.com/WebOfTrustInfo/)**
* [Decentralized Identity Foundation](http://identity.foundation/) (DIF) [[**github**](https://github.com/decentralized-identity)] [[**twitter**](https://twitter.com/DecentralizedID)] [[**blog**](https://medium.com/decentralized-identity)] 

### Self Sovereign Identity[**^**](#Contents)

![](http://imgur.com/3zz62kpl.png)

* [WebOfTrustInfo/self-sovereign-id](https://github.com/WebOfTrustInfo/self-sovereign-identity)
* [Self-Sovereign Identity: Why Blockchain?](https://www.ibm.com/blogs/blockchain/2018/06/self-sovereign-identity-why-blockchain/)
* [A Technlogy-Free Definition of Self-Sovereign Identity (SSI)](https://github.com/jandrieu/rebooting-the-web-of-trust-fall2016/raw/master/topics-and-advance-readings/a-technology-free-definition-of-self-sovereign-identity.pdf) 
* [Self-Sovereign Identity Principles](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md)
* [Inevitable Rise of Self-Sovereign Identity](https://sovrin.org/wp-content/uploads/2018/03/The-Inevitable-Rise-of-Self-Sovereign-Identity.pdf)
* [Experts talk Self-Sovereign Identity](https://www.coindesk.com/experts-talk-self-sovereign-identity-implementing-systems/)
* [Self-Sovereign Identity — wiki.p2pfoundation](https://wiki.p2pfoundation.net/Self-Sovereign_Identity)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">0/ “Self-Sovereign Identity: A Progress Report”…</p>&mdash; Christopher Allen (@ChristopherA) <a href="https://twitter.com/ChristopherA/status/989120215702261761?ref_src=twsrc%5Etfw">April 25, 2018</a></blockquote>

### Evernym[**^**](#Contents)

![](http://untangled.world/wp-content/uploads/2017/08/everynym-logo-1400x357.png)

* [Evernym](https://www.evernym.com/) ([**twitter**](https://twitter.com/evernym)) originally created the codbase that became Sovrin, and is now Indy.
* [The Three Models of Digital Identity Relationships — How self-sovereign identity (SSI) is different, and why it’s better](https://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186)
* [Is Self-Sovereign Identity the ultimate GDPR compliance tool? [1\3]](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-9d8110752f89) [[**2**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-40db94c1c437)] [[**3**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-7296a3b07769)]

### The Sovrin Foundation[**^**](#Contents)

![](https://www.evernym.com/wp-content/uploads/2017/04/logo-large.png)

* The [Sovrin](https://sovrin.org/)
 Foundation is creating a public instance of [Hyperledger](#Hyperledger-Indy) Indy's code; initially developed by [Evernym](#Evernym)\
  [[**Forum**](https://forum.sovrin.org/)] [[**Slack**](https://sovrin-slack-signup.herokuapp.com/)][[**Twitter**](https://twitter.com/SovrinID)][[**Github**](https://github.com/sovrin-foundation/sovrin)]
* [Sovrin Library](https://sovrin.org/library/)
* [Getting Started with Sovrin](https://sovrin.org/library/getting-started-with-sovrin/)
* [Sovrin: A Protocol and Token for Self-Sovereign Identity and Decentralized Trust](https://sovrin.org/wp-content/uploads/Sovrin-Protocol-and-Token-White-Paper.pdf)
* [Sovrin Network: What Goes on the Ledger?](https://sovrin.org/wp-content/uploads/2018/10/What-Goes-On-The-Ledger.pdf)
* [Sovrin Governance Framework](https://sovrin.org/library/sovrin-governance-framework/)
* [How Sovrin Works—A Technical Guide from the Sovrin Foundation](https://sovrin.org/wp-content/uploads/2018/03/How-Sovrin-Works.pdf)
* [Sovrin Test Network Trust Anchor Registration](https://s3.us-east-2.amazonaws.com/evernym-cs/sovrin-STNnetwork/www/trust-anchor.html)[[**Forum**](https://forum.sovrin.org/t/testing-on-the-sovrin-test-network-stn/643/17)]

#### Selected readings from Windley.com [**^**](#Contents)
* [An Internet for Identity](http://www.windley.com/archives/2016/08/an_internet_for_identity.shtml)
* [A Universal Trust Framework](http://www.windley.com/archives/2017/01/a_universal_trust_framework.shtml)
* [The Case for Decentralized Identity](http://www.windley.com/archives/2017/08/the_case_for_decentralized_identity.shtml)
* [Building Your Business on Sovrin: Domain-Specific Trust Frameworks](http://www.windley.com/archives/2018/03/building_your_business_on_sovrin_domain-specific_trust_frameworks.shtml)
* [The Sovrin Foundation](http://www.windley.com/archives/2018/07/the_sovrin_foundation.shtml)
* [Decentralization in Sovrin](http://www.windley.com/archives/2018/10/decentralization_in_sovrin.shtml)


### Hyperledger Indy[**^**](#Contents)

![](https://www.osiztechnologies.com/asset/oimages/hyperledger_indy/hyperledger_indy_02.png)

![](http://imgur.com/2LWlrgvl.png)
[Linux Foundation -Blockchain for Business -INDY](https://www.edx.org/course/blockchain-for-business-an-introduction-to-hyperledger-technologies)

* [Hyperledger Indy - *Distributed Ledger and Utility Library*](https://www.hyperledger.org/projects/hyperledger-indy) [[**twitter**](https://twitter.com/Hyperledger)] [[**wiki**](https://wiki.hyperledger.org/projects/indy/documentation)] [[**git**](https://github.com/hyperledger/indy-sdk)]
* [Hyperledger Welcomes Project Indy](https://www.hyperledger.org/blog/2017/05/02/hyperledger-welcomes-project-indy) - ANN
* [The Rise of Self-Sovereign Identity - Hyperledger Indy](https://wso2.com/blog/research/the-rise-of-self-sovereign-identity-hyperledger-indy)
* [Plenum Bzantine Fault Tolerant Protocol](https://github.com/hyperledger/indy-plenum/wiki)
   * "Byzantine fault tolerance is a sub-field of fault tolerance research inspired by the Byzantine Generals' Problem, which is a generalized version of the Two Generals' Problem."
* [An Accumulator Based on Bilinear Maps and Efficient Revocation for Anonymous Credentials](https://eprint.iacr.org/2008/539.pdf)
* [An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation](https://www.iacr.org/archive/eurocrypt2001/20450093.pdf)
* [SecureKey Technologies to explore interoperability between Verified.Me and Hyperledger Indy](https://securekey.com/press-releases/hyperledger-indy/)
* The Linux Foundation's [Blockchain for Business](https://www.edx.org/professional-certificate/linuxfoundationx-blockchain-for-business) edx course may be freely audited and has a section on Indy.
* [Implementing Privacy by Design in Hyperledger Indy](https://www.infoq.com/news/2018/09/Hyperledger-Indy-Privacy)


#### IDEMix -Zero Knowledge Proof's in Evernym\Indy[**^**](#Contents)

>Our zero-knowledge proofs are part of the [Idemix protocol](http://domino.research.ibm.com/library/cyberdig.nsf/papers/EEB54FF3B91C1D648525759B004FBBB1/%24File/rz3730_revised.pdf), where they are used to prove the possession of [Camenisch-Lysyanskaya credentials](https://eprint.iacr.org/2001/019.pdf). We also use zero-knowledge proofs in the revocation protocol, which is based on [cryptographic accumulators](https://eprint.iacr.org/2008/539.pdf). —*[What Zero Knowledge Poof Algorithm is used in Sovrin?](https://forum.sovrin.org/t/what-zero-knowledge-proof-algorithm-is-used-in-sovrin/71/2)*

>Identity Mixer is not directly (re)implemented by Sovrin, but its cryptographic foundations are very similar, and Sovrin’s implementation includes most of its extended features (predicates, multi-credential, revocation, advanced issuance…). One of the researchers who helped to create Identity Mixer is on Sovrin’s Technical Governance Board and has offered insight to keep the implementations aligned on goals and methods. 
>—*[How is IDEMix Implemented?](https://forum.sovrin.org/t/how-idemex-is-implemented-in-sovrin-indy/)*

* [IBM Identity Mixer](https://www.zurich.ibm.com/identity_mixer/) | [blog](https://idemix.wordpress.com/)
  * [idemix in Hyperledger Fabric](https://hyperledger-fabric.readthedocs.io/en/release-1.3/idemix.html)
* [Concepts and Features of Privacy-Preserving Attribute-Based Credentials](https://github.com/p2abcengine/p2abcengine/wiki/Concepts-and-features)
* [AnonCreds: Anonymous credentials protocol implementation in python](https://github.com/hyperledger/indy-anoncreds) [[Usecase](https://github.com/hyperledger/indy-anoncreds/blob/master/docs/anoncred-usecase1.pdf)]

### Video[**^**](#Contents)
* [Phil Windley on the Sovrin Network](https://www.youtube.com/watch?v=IxQUL2ztFi8)
* [Self-Sovereign Identity with Hyperledger Indy\Sovrin- Calvin Cheng - FOSSASIA 2018](https://www.youtube.com/watch?v=hfyIZu3_fw8)


### Selected 'Rebooting Web of Trust' Whitepapers[**^**](#Contents) 
* [WebofTrust.info/papers.html](https://www.weboftrust.info/papers.html)
* [Rebooting the Web of Trust VII: Toronto (September 2018)](https://github.com/WebOfTrustInfo/rwot7)
* [Framework for the Comparison of Identity Systems](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/Framework-for-Comparison-of-Identity-Systems.md)
* [A Primer on Functional Identity](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/topics-and-advance-readings/functional-identity-primer.md)
* [The DCS Theorem](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/dcs-theorem/The-DCS-Theorem.md) — We use the triangle to show decentralized consensus systems can have _Decentralization_, _Consensus_, or _Scale_, but not all three properties simultaneously.
* [Identity Crisis: Clear Identity through Correlation](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/identity-crisis.pdf)
* [Decentralized Key Management System](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2017/blob/master/topics-and-advance-readings/dkms-decentralized-key-mgmt-system.md)
* [SSI: A Roadmap for Adoption](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/a-roadmap-for-ssi.md)

#### RWoT Use Cases[**^**](#Contents)
—infogrphic workflow examples 
* [Amira 1.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/amira.md)
* [Re-Imagining What Users Really Want](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2017/blob/master/final-documents/what-users-really-want.md)
* [Joram 1.0.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2016/blob/master/final-documents/joram-engagement-model.pdf)
* [Powering the Physician-Patient Relationship with HIE of One Blockchain Health IT](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/physician-patient-relationship.pdf)
* [Protecting Digital Identities in Developing Countries](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/protecting-digital-identities-in-developing-countries.pdf)
* [Opportunities Created by the Web of Trust for Controlling and Leveraging Personal Data](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/satisfying-real-world-use-cases.pdf)

### World Wide Web Consortium[**^**](#Contents)

![](http://imgur.com/Lz6RTysl.png)

* [World Wide Web Consortium(W3C)](https://www.w3.org/) [[**twitter**](https://twitter.com/w3c)] [[**github**](https://github.com/w3c)]
* [Credentials Community Group](https://www.w3.org/community/credentials/)[[**blog**](https://w3c-ccg.github.io/)]  
* [Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/)
   * [Verifiable Claims Working Group Charter](https://www.w3.org/2017/vc/charter.html)
* [The W3C CREDENTIALS COMMUNITY GROUP](https://www.w3.org/community/credentials/) | [W3C CCG](https://w3c-ccg.github.io/)
* [Verifiable Claims Data Model 1.0](https://w3c.github.io/vc-data-model/) [[**github**](https://github.com/w3c/vc-data-model)]
* [Verifiable Claims Use Cases 1.0](https://w3c.github.io/vc-use-cases/)
* [JSON-LD 1.0, W3C Recommendation](https://www.w3.org/TR/json-ld/)
* [opencreds.org — Identity Credentials 1.0](https://opencreds.org/specs/source/identity-credentials/)
* [DIGITAL VERIFICATION COMMUNITY GROUP](https://www.w3.org/community/digital-verification/)[[**github**](https://sea-region.github.com/w3c-dvcg)]

### DID the Decentralized Identifier[**^**](#Contents) 

* [w3c- Decentralized Identifiers (DIDs) v0.11](https://w3c-ccg.github.io/did-spec/)
* [DID Primer](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/draft-documents/did-primer.md) -[Extended](https://github.com/WebOfTrustInfo/rwot7-fall2018/blob/master/topics-and-advance-readings/did-primer-extended.md)
* [Decentralized IDentifers (DIDs)](https://www.w3.org/2018/vocabws/presentations/Sabadello.pdf) 
   * [DID auth and the Little I-am-Me](https://medium.com/@markus.sabadello/did-auth-and-the-little-i-am-me-ec14d757ff09)
   * [Introduction to DID Auth](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/did-auth.md)
   * [Introduction to DID Auth for SSI – Markus Sabadello – Webinar 10](http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10/)
* [A Universal Resolver for self-sovereign identifiers](https://medium.com/decentralized-identity/a-universal-resolver-for-self-sovereign-identifiers-48e6b4a5cc3c)
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
* [Identity Hubs Capabilities Perspective](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/identity-hubs-capabilities-perspective.md) - Identity Hubs currently proposed in the Decentralized Identity Foundation (DIF) are a subset of a general Decentralized Identifier (DID).
* [DIDs in DPKI](https://github.com/WebOfTrustInfo/rwot7/blob/master/topics-and-advance-readings/dids-in-dpki.md)


### EU General Data Protection Regulation Act[**^**](#Contents)

* [Blockchains and Data Protection in the European Union](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3080322)
* [IBM — How blockchain could address five areas associated with GDPR compliance](https://www-01.ibm.com/common/ssi/cgi-bin/ssialias?htmlfid=61014461USEN)
* [GDPR - A reflection on the 'self-sovereign identity' and the Blockchain](https://www.linkedin.com/pulse/gdpr-reflection-self-sovereign-identity-blockchain-nicolas-ameye/)
* [GDPR and Privacy by Design, What developers need to know](https://medium.com/@sphereidentity/gdpr-and-privacy-by-design-what-developers-need-to-know-fa5a936da65a)
* [Privacy by Design The 7 Foundational Principles](https://www.ipc.on.ca/wp-content/uploads/Resources/7foundationalprinciples.pdf) 
* [When GDPR Becomes Real, and Blockchain is no longer fairydust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/gdpr.md)
* [Digital Identity Management in the Context of GDPR & Sovrin —Why Data Privacy Matters & How to Protect It](https://blog.tykn.tech/digital-identity-management-in-the-context-of-gdpr-sovrin-43028247378b)
* [Self-Sovereign Privacy By Design](https://github.com/sovrin-foundation/protocol/blob/master/self_sovereign_privacy_by_design_v1.md)


### Indy\Sovrin Adoption[**^**](#Contents)

* [Tykn *The Future of Resilient Identity*](https://tykn.tech/) [[**twitter**](https://twitter.com/Tykn_tech)][[**github**](https://github.com/tykntech)][[**Extended Overview**](https://docs.google.com/document/d/1pNRO6aOb5eK4s8PVv7yS4x9TkqrGglCJ4jebU1F3Yzo/edit#)] (Indy\Sovrin)
* [Illinois Blockchain Initiative](https://illinoisblockchain.tech/) — [partners with Evernym to launch birth registration pilot](https://illinoisblockchain.tech/illinois-partners-with-evernym-to-launch-birth-registration-pilot-f2668664f67c)

#### DID Adoption [**^**](#Contents)
* [@ChristopherA on DID adoption](https://twitter.com/ChristopherA/status/989122017348784130)
   > "22/ Over a dozen companies and organizations, using multiple blockchains (Bitcoin, Ethereum, Hyperledger, etc.), have committed to deploying DIDs, including IBM, Microsoft, Digital Bazaar, Consensys, Evernym, Learning Machine, British Columbia, and more:" —[How blockchain could solve the internet privacy problem](https://www.computerworld.com/article/3267930/blockchain/how-blockchain-could-solve-the-internet-privacy-problem.html)
* [Veres One DID Method 1.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/did-method-veres-one.md) — a permissionless public ledger designed specifically for the creation and management of decentralized identifiers (DIDs)
* [Blockstack DID Spec](https://github.com/blockstack/blockstack-core/blob/master/docs/blockstack-did-spec.md)[**[*](https://forum.blockstack.org/t/did-method-at-identity-foundation/4287/9)**]
* [Spidchain](http://www.spidchain.com/) [[**wp**](https://drive.google.com/file/d/0B89WE3IIHmy1Z0ZSSWVmVEtaaG8/view)]
   * "offers a platform for self-sovereign identity, including desktop and mobile apps for end-users. It uses Decentralized Identifiers (DIDs) - backed by optionally Bitcoin or Ethereum - to implement a marketplace for verifiable claims. The Spidchain applications allow individuals to create, recover, and revoke DIDs, to authenticate, to sign and verify files and claims, and more."


### Sources[**^**](#Contents)
* [/awesome-decentralized-id](/README.md)
* [IIW-Wiki](http://iiw.idcommons.net/Main_Page)
* [wiki.idcommons.net](http://wiki.idcommons.net/Main_Page)
* [/WebOfTrustInfo](https://github.com/WebOfTrustInfo/)
* [/peacekeeper/blockchain-identity](https://github.com/peacekeeper/blockchain-identity)
* [/blockchain-id.toml](/blockchain-id.toml)
* [identitywoman.net](https://identitywoman.net/)
* [windley.com/tags/identity](http://www.windley.com/tags/identity.shtml)
