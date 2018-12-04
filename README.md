# Awesome Decentralized Identity [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
**DID, Blockchain and Self-Sovereign Identity Resources**
[<img src="https://i.imgur.com/zeYCNMS.jpg" align="right" width="150" height="140">](https://github.com/infominer33/Crypto-library)


![](https://i.imgur.com/9KpJRDr.png)

>Imagine a world where you are in direct control of your personal information; a world where you can limit and control how much information you share while retaining the ability to transact in the world. This is self-sovereign identity, and it is already here. Blockchain is the underlying technology paving the path to self-sovereign identity through decentralized networks. It ensures privacy and trust, where transactions are secure, authenticated and verifiable and endorsed by relevant, permissioned participants.  [-Jerry Cuomo](https://techcrunch.com/2017/09/10/the-promise-of-managing-identity-on-the-blockchain/) (IBM)


### Contents

* [A Note from the Editor](#A-Note-from-the-Editor)
* [History](#History)
  * [Internet Identity Workshop—IIW](#Internet-Identity-Workshop) 
  * [#Rebooting-Web-of-Trust (RWoT)](#Rebooting-the-Web-Of-Trust)
  * [Bitnation and the United Nations](#Bitnation-and-the-United-Nations)
    * [ID2020 and the GDPR](#ID2020-and-the-GDPR)
  * [Decentralized Identity Foundation—DIF](#Decentralized-Identity-Foundation)
 * [Resources](#Resources)
   * [Self Sovereign Identity—SSI](#Self-Sovereign-Identity)
   * [RWoT Whitepapers](#Selected-Rebooting-Web-of-Trust-Whitepapers)
      * [RWoT Use Cases](#RWoT-Use-Cases) -infographic workflow
   * [World Wide Web Consortium—W3C](#World-Wide-Web-Consortium)
     * [DID the Decentralized Identifier](#DID-the-Decentralized-Identifier) 
   * [Evernym](#Evernym)
   * [The Sovrin Foundation](#The-Sovrin-Foundation)
     * [Windley.com](#Selected-articles-from-Windley.com)
     * [Tykn Tech](#Tykn-Tech)
   * [Hyperledger Indy](#Hyperledger-Indy)
     * [Idemix](#IDEMix)
   * [IBM](#IBM)
   * [Ethereum—Protocol](#Ethereum)
     * [Ethereum Apps](#Ethereum-Identity-Applications)
   * [State Led Identity Initiatives](#State-Led-Initiatives)
     * [Canada](#Canada)
     * [Netherlands](#Netherlands)
     * [USA](#USA)
     * [Spain](#Spain)
     * [Switzerland](#Switzerland)
     * [Estonia](#Estonia)
   * [Assorted Decentralized \ Blockchain ID Related](#Assorted-Decentralized-\-Blockchain-ID-Related)
   * [Humanitarian](#Humanitarian)
   * [Structured Data Standards](#Structured-Data-Standards)
   * [Decentralized Public Key Infrastructure](#Decentralized-Public-Key-Infrastructure-(DPKI))
   * [Personal Data: Wallets, Marketplaces, etc](#Personal-Data-Wallets-Marketplaces-etc)
   * [GDPR](#EU-General-Data-Protection-Regulation-Act)
   * [Reports](#Reports)
   * [Research Papers](#Research-Papers)
   * [Videos](#Video)
   * [Sources](#Sources)

   

### A Note from the Editor[**^**](#Contents)

>Thanks to those who are working to make our identity experience, and the world, a better place.

—Information is not so easily organized in a linear fashion. This list is a by-product of an effort to enter the best blockchain, self-sovereign, and decentralized identity links into a database to will power a [web-app](https://github.com/infominer33/Crypto-library) for search, navigation by tags, and pages like this with pre-arranged information. The SuperSource will have comments, submissions, ratings and reactions; so that it can become a co-operative effort among those who get involved. Furthermore, the Crypto SuperSource will be a database of all types of crypto information, not only ID.

In the mean-time, after gathering all of the links I had already into [one collection](/blockchain-id.toml), I knew I could make an awesome list out of them sooner than a live demo of the app that is in progress.

I'm also working on [/awesome-sovrin](https://github.com/infominer33/awesome-decentralized-id/tree/master/awesome-sovrin/README.md) as a place to focus more on the Sovrin\Indy protocol and ecosystem. Ideally, I hope for these 'Awesome' lists to compliment each-other along with [/peacekeeper/blockchain-identity](https://github.com/peacekeeper/blockchain-identity/). It will take a bit of thinking, and perhaps some collaboration to decide the best way to do that.

//Pull Requests Welcome



## History[**^**](#Contents)

![](https://www.yubico.com/wp-content/uploads/2013/10/IIW-blog.jpg)

### Internet Identity Workshop[**^**](#Contents)

In 2005, [Kaliya Young](https://identitywoman.net/)[[**twitter**](https://twitter.com/IdentityWoman)], [Phil Windley](https://windley.com)[[**twitter**](https://twitter.com/windley)], [Drummond Reed](https://www.evernym.com/)[[**twitter**](https://twitter.com/drummondreed)][[**blog**](https://equalsdrummond.name/)], and [Doc Searls](http://blogs.harvard.edu/doc/)[[**twitter**](https://twitter.com/dsearls)][[**blog**](https://blogs.harvard.edu/doc)] hosted the first [Internet Identity Workshop](http://www.internetidentityworkshop.com/)(IIW)[[**twitter**](https://twitter.com/idworkshop)] in Berkeley to discuss "architectural and governance proposals for Internet-wide identity services and their underlying philosophies." -[Announcing IIW 2005](https://identitywoman.net/announcing-the-internet-identity-workshop-iiw2005/)

Since then, the IIW has met bi-anually, actively supporting the development of the identity software-ecosystem, including [OpenID](http://wiki.openid.net)('05), OpenID [2.0](http://wiki.openid.net/w/page/12995215/OpenID%20Authentication%202-1)('06), [OAuth](https://en.wikipedia.org/wiki/OAuth)('10), [FIDO](https://fidoalliance.org/)('13) and OpenID [Connect](https://en.wikipedia.org/wiki/OpenID_Connect)('14). 

IIW participants began the effort towards creating a truly "[user centric identity](https://www.networkworld.com/article/2304596/access-control/what-is--user-centric--identity-.html)," in contrast to identity solutions whos focus has been fulfilling the needs of the enterprise. The pioneers of decentralized identity, long struggled against the "identity silo paradox:" while the [identerati](https://www.zdnet.com/article/the-identity-silo-paradox/) continually work on solutions to break up these silos, the enterprise has a strong financial incentive to retain them.

* [Not Just Who They Say We Are: Claiming our identity on the Internet](https://vimeo.com/207961532)- short film on the “Identerati” of the IIW[[**4**](https://www.prweb.com/releases/identitymovie/iiw2017/prweb14161721.htm)]
   * [identirati](https://www.zdnet.com/article/the-identity-silo-paradox/)[[**5**](https://www.forgerock.com/blog/who-are-the-identerati)] is a term for those working on standards and methods based on the premise of opening up id data silos, dating back to at least 2006:
      > 
* **More information** on iid standards history: **[IIW-Wiki](http://iiw.idcommons.net/Main_Page)** | **[identitywoman.net](https://identitywoman.net/)** | **[windley.com-#identity](http://www.windley.com/tags/identity.shtml)** | **[WoTinfo](https://github.com/WebOfTrustInfo/)**

In [April of 2014](https://edps.europa.eu/data-protection/data-protection/legislation/history-general-data-protection-regulation_en), the European Parliament demonstrates strong support for the GDPR, which passes back and forth through the European Council, Commision and Parliment throught the rest of the year.

[8/14](https://www.w3.org/community/credentials/charter-20140808/) The [Credentials Community Group](https://www.w3.org/community/credentials/)[[**6**](https://w3c-ccg.github.io/)] forms, hosted by [World Wide Web Consortium(W3C)](https://www.w3.org/)[[**twitter**](https://twitter.com/w3c)][[**github**](https://github.com/w3c)] : "to forge a path for a secure, decentralized system of credentials that would empower both individual people and organizations on the Web to store, transmit, and receive digitally verifiable proof of qualifications and achievements." —proposed by [Manu Sporney](http://manu.sporny.org/)[[**twitter**](https://twitter.com/manusporny)][[**7**](https://digitalbazaar.com/)]

 [*What is Sovereign Source Authority?*](https://www.moxytongue.com/2012/02/what-is-sovereign-source-authority.html) shows an early use of 'sovereign' in relation to our internet identities. The term "Self Sovereign Identity" started becoming widely used in 2014.[[**1**](https://www.tokencommons.org/Windhover-Principles-for-Digital-Identity-Trust-Data.html)][[**2**](https://hubculture.com/hubs/47/news/689/)] 


<img src="https://sustainabledevelopment.un.org/content/images/image18_3741.jpg"/>


### Bitnation and the United Nations[**^**](#Contents) 

9\15 [Bitnation](https://bitnation.co/) "seeks to establish the concept of '*world citizenship*' via a bitcoin based identity, offering '[*blockchain emergency IDs*](https://refugees.bitnation.co/)' to refugees.[[**8**](https://www.newsbtc.com/2015/09/09/bitnation-taps-blockchain-tech-to-aid-refugees/)] 

The same month, the UN unveiled it's *Agenda for Sustainable Development*.


>* Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels
>* Substantially reduce corruption and bribery in all their forms
Develop effective, accountable and transparent institutions at all levels
>* **By 2030, provide legal identity for all, including birth registration**
>* Ensure public access to information and protect fundamental freedoms, in accordance with national legislation and international agreements
—Excerpt: [Transforming our world: the 2030 Agenda for Sustainable Development](https://sustainabledevelopment.un.org/post2015/transformingourworld) (*emphasis mine*)


* [DIGITAL IDENTITY AS A BASIC HUMAN RIGHT](https://impakter.com/digital-identity-basic-human-right/)
* [AID:Tech](https://aid.technology)[[**twitter**]](https://twitter.com/aidtechnology) — "is a voucher and digital identity solution for refugees. A digital record of a person's identity is stored on a smart card, along with various additional information. Blockchain technology is used to distribute all resources in a highly traceable manner."

![](http://imgur.com/GdYLQjzl.png)

### Rebooting the Web Of Trust[**^**](#Contents)

In relation to SSI, '[Web of Trust](https://en.wikipedia.org/wiki/Web_of_trust)' is a network of relationships that attest to our identity claims. *Each party attesting to your identity information becomes a strand in your web of trust.*

The first [Rebooting Web of Trust](http://www.WebOfTrust.info)(RWoT)  workshop was held during [November 2015](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust); attracting the likes of Vitalik Buterin, Peter Todd, Gregory Maxwell, Joel Dietz, Christopher Allen, and Jon Callas, [according to Andreas Antonopolis](https://news.bitcoin.com/andreas-antonopoulos-case-reputation-identity-systems/). 

[That workshop](https://github.com/WebOfTrustInfo/), produced 5 technical white papers: [5 WoT-usecases](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/satisfying-real-world-use-cases.pdf) | [Decentralized PKI](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/dpki.pdf) | [Smart Signatures](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/smart-signatures.pdf) | [Creating a New World of Trust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/whats-the-next-step.pdf)
  >The Web of Trust is a buzzword for a new model of decentralized self-sovereign identity. It’s a phrase that dates back almost twenty-five years, the classic definition derives from PGP [...] the vibrant blockchain community is also drawing new attention to the concept we aim to reboot it. - [Rebranding the Web of Trust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/rebranding-web-of-trust.pdf)


At the end of 2015, the Department of Homeland Security announced that it had funds available for the development of [Blockchain Security and Identity Verification Technologies](https://blog.aniljohn.com/2015/12/federal-gov-funds-for-identity-r-and-d.html).

### ID2020 and the GDPR[**^**](#Contents)

![](http://imgur.com/ymviAssl.png)

[Christopher Allen](http://www.lifewithalacrity.com/)[[**twitter**](https://twitter.com/ChristopherA)][[**github**](https://github.com/ChristopherA)] details the overarching history of internet idenitity standards in his seminal work (Also submitted to the ID2020\RWoT workshop):
*  **[The Path to Self-Soverereign Identity](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)**[[**3**](https://www.coindesk.com/path-self-sovereign-identity/amp/)] details the history of identity standards leading up to self-sovereign and details the 10 principles of self-sovereign identity.
  > I am part of the team putting together the first ID2020 Summit on Digital Identity at the United Nations

[4/16](https://edps.europa.eu/data-protection/data-protection/legislation/history-general-data-protection-regulation_en) the EU adopted the GDPR, enacted as law May 2018. The second RWoT workshop ran in conjunction with the UN's [ID2020](https://id2020.org/) Summit in New York that [May](https://press.pwc.com/News-releases/id2020-to-kick-start-digital-identity-summit-at-un-with-pwc-support./s/9fe11be5-cbd8-486b-b4d2-d798f486d0f2). 

>1.1 Billion people live without an officially recognized identity — This lack of recognized identification deprives them of protection, access to services, and basic rights. ID2020 is a public-private partnership dedicated to solving the challenges of identity for these people through technology. - id2020.org


Evident from [whitepapers](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/topics-and-advance-readings/README.md) submitted to the RWoT\ID2020 Workshop, the DID identifier had begun to emerge:
* [Decentralized Identifiers (DIDs) and Decentralized Identity Management (DIDM)](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/topics-and-advance-readings/DID-Whitepaper.md)
   >"Decentralized Identifiers (DID) stored in a permissioned blockchain enable principals to directly control their own identities with cryptographic proofs and secure, addressable network endpoints. DIDs further enable a Decentralized Identity Management (DIDM) infrastructure that will empower people and organizations to securely and confidentially manage and assert their identities."
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
   >"Respect Network is conducting a research project for the [U.S. Department of Homeland Security](https://bravenewcoin.com/insights/u-s-department-of-homeland-security-funds-four-blockchain-companies-developing-new-cyber-security-technology), HSHQDC-16-C-00061, to analyze the applicability of blockchain technologies to a decentralized identifier system. Our thesis is that blockchains, or more generically distributed ledgers, are a potentially powerful new tool for “identity roots” — the starting points for an Internet identity. However “blockchain identity” may not fully address the core security and privacy principles needed in a complete identity system. In this case DIDs — Decentralized Identifiers rooted on a distributed ledger — may end up being a foundational building block for higher level identity management solutions. -
* At this point in time DLT innovation, the United Nations Sustainable Development Goals, and the EU GDPR all came together supporting a core identirati tenant: Eliminating id data silos and empowering users regarding personal digital identity. 


### Decentralized Identity Foundation[**^**](#Contents) 

![](http://imgur.com/PXGV6Xyl.png)

* On May 22 at Consensus 2017 the formation of the Decentralized Identity Foundation (DIF) [was announced](https://www.ethnews.com/decentralized-identity-foundation-announces-formation-at-consensus-2017)
* [Conensus 2017 - Building an Foundation for Decentralized Identity](https://www.youtube.com/watch?v=l5laRZfn8AI) (video)
* [Decentralized Identity Foundation](http://identity.foundation/) (DIF) [[**github**](https://github.com/decentralized-identity)] [[**twitter**](https://twitter.com/DecentralizedID)] [[**blog**](https://medium.com/decentralized-identity)] 
  >A key piece of the decentralized identity equation is how people, organizations, and devices can be identified and located without centralized systems of identifiers (e.g. email addresses). DIF members are actively working on protocols and implementations that enable creation, resolution, and discovery of decentralized identifiers and names across decentralized systems, like blockchains and distributed ledgers.
* Members include: [Microsoft](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE2DjfY) | [uPort](https://github.com/uport-project/ethr-did/blob/develop/docs/index.md) | [IBM](https://www.ibm.com/blogs/blockchain/2018/06/self-sovereign-identity-why-blockchain/) | [Sovrin](https://github.com/sovrin-foundation/sovrin/blob/master/spec/did-method-spec-template.html) | [SecureKey](https://www.ibm.com/blogs/blockchain/2018/05/self-sovereign-identity-our-recent-activity-as-a-sovrin-steward/) | [Blockstack](https://github.com/blockstack/blockstack-core/blob/feature/docs-bns/docs/blockstack_naming_service.md#decentralized-identifiers-dids) | [Evernym](https://www.evernym.com/wp-content/uploads/2017/07/What-Goes-On-The-Ledger.pdf) | [Hyperledger](https://github.com/hyperledger/indy-sdk/blob/master/doc/getting-started/getting-started.md) | [Civic](https://www.civic.com/solutions/kyc-services/) | [Accenture](https://www.accenture.com/us-en/insight-blockchain-id2020) | [Danube](https://github.com/projectdanube/xdi2), [netki](https://bravenewcoin.com/insights/netki-launches-digital-id-solution-which-bitt-is-using-with-central-banks-in-the-caribbean) | [RSA](https://www.rsa.com/en-us/research-and-thought-leadership/rsa-labs) | [Consent](https://sovrin.org/steward/global-consent/) | [IOTA](https://medium.com/@iotasuppoter/iota-the-case-of-decentralized-digital-identity-de7b95042c12) | [Mooti](https://www.cio.com/article/3147358/it-industry/ibm-building-blockchain-ecosystem.html) | [r3](https://www.gemalto.com/press/pages/gemalto-and-r3-pilot-blockchain-technology-to-put-users-in-control-of-their-digital-id.aspx) | [Authenteq](https://venturebeat.com/2018/08/30/authenteq-launches-blockchain-identity-verification-to-stop-online-trolls/) | [Blockchain-foundry](https://www.blockchainfoundry.co/blockchain-foundry-inc-announces-new-software-release-for-blockchain-based/), [Validatedid](https://www.validatedid.com/vidchain-the-future-of-digital-identity/) | [1kosmos](https://onekosmos.com/product-details/) | [gamecredits](https://medium.com/@gamecredits/introducing-blinking-blink-identity-management-on-the-blockchain-9258c7d76a8d)[[*](https://blinking.id)] | [auth0](https://auth0.com/) | [jolocom](https://stories.jolocom.com/jolocom-brings-blockchain-identity-to-privacy-week-berlin-acdaee665f0) | [Enigma](https://blog.enigma.co/off-chain-identity-claims-with-enigma-2d5b23c31f92), [Humanized-internet](https://www.thehumanizedinternet.org/) | [Pillar](https://pillarprojectfoundation.org/blog/announcing-the-pillar-project/) | [id2020](https://id2020.org/manifesto/) | [Nuggets](https://www.mobilepaymentstoday.com/news/identity-and-payments-platform-nuggets-partners-with-iot-company/)
* [Decentralized Identity Foundation Grows To 56 Members In Our First Year](https://medium.com/decentralized-identity/decentralized-identity-foundation-grows-to-56-members-in-our-first-year-3ec117e811d8)
* [A Universal Resolver for self-sovereign identifiers](https://medium.com/decentralized-identity/a-universal-resolver-for-self-sovereign-identifiers-48e6b4a5cc3c) [[**^**](#DID-Auth)]**[[Uniresolver.io](https://uniresover.io)]**

## Resources

### Self Sovereign Identity[**^**](#Contents)

![](http://imgur.com/3zz62kpl.png)

* [WebOfTrustInfo/self-sovereign-id](https://github.com/WebOfTrustInfo/self-sovereign-identity)
* [Self-Sovereign Identity: Why Blockchain?](https://www.ibm.com/blogs/blockchain/2018/06/self-sovereign-identity-why-blockchain/)
* [A Technlogy-Free Definition of Self-Sovereign Identity (SSI)](https://github.com/jandrieu/rebooting-the-web-of-trust-fall2016/raw/master/topics-and-advance-readings/a-technology-free-definition-of-self-sovereign-identity.pdf) 
* [Self-Sovereign Identity Principles](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md)
* [Inevitable Rise of Self-Sovereign Identity](https://sovrin.org/wp-content/uploads/2018/03/The-Inevitable-Rise-of-Self-Sovereign-Identity.pdf)
* [Experts talk Self-Sovereign Identity](https://www.coindesk.com/experts-talk-self-sovereign-identity-implementing-systems/)
* [SSI Meetup](http://ssimeetup.org/)
* [Self-Sovereign Identity — wiki.p2pfoundation](https://wiki.p2pfoundation.net/Self-Sovereign_Identity)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">0/ “Self-Sovereign Identity: A Progress Report”…</p>&mdash; Christopher Allen (@ChristopherA) <a href="https://twitter.com/ChristopherA/status/989120215702261761?ref_src=twsrc%5Etfw">April 25, 2018</a></blockquote>

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
—infogrphic workflow
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
* [Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/) [[**Charter**](https://www.w3.org/2017/vc/charter.html)]
* [Verifiable Claims Data Model 1.0](https://w3c.github.io/vc-data-model/) [[**github**](https://github.com/w3c/vc-data-model)] [[**Use Cases**](https://w3c.github.io/vc-use-cases/)]
* [JSON-LD 1.0, W3C Recommendation](https://www.w3.org/TR/json-ld/)
* [opencreds.org — Identity Credentials 1.0](https://opencreds.org/specs/source/identity-credentials/)
* [DIGITAL VERIFICATION COMMUNITY GROUP](https://www.w3.org/community/digital-verification/)[[**github**](https://sea-region.github.com/w3c-dvcg)]

![](http://imgur.com/6MLNgXal.png)


#### DID the Decentralized Identifier[**^**](#Contents) 

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
* [@ChristopherA on DID adoption](https://twitter.com/ChristopherA/status/989122017348784130)
   > "22/ Over a dozen companies and organizations, using multiple blockchains (Bitcoin, Ethereum, Hyperledger, etc.), have committed to deploying DIDs, including IBM, Microsoft, Digital Bazaar, Consensys, Evernym, Learning Machine, British Columbia, and more:" —[How blockchain could solve the internet privacy problem](https://www.computerworld.com/article/3267930/blockchain/how-blockchain-could-solve-the-internet-privacy-problem.html)
* [Requirements for DIDs](https://github.com/WebOfTrustInfo/ID2020DesignWorkshop/blob/master/final-documents/requirements-for-dids.pdf)
* [Veres One DID Method 1.0](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/did-method-veres-one.md) [[**Site**](https://veres.one)][[**Overview**](https://docs.google.com/presentation/d/1bUZbtgdxKxTR1it10G9ZozYGD486qxZTBPuiOZjzoT4/edit#slide=id.g368b7a777c_1_0)] — a permissionless public ledger designed specifically for the creation and management of decentralized identifiers (DIDs)
* [Blockstack DID Spec](https://github.com/blockstack/blockstack-core/blob/master/docs/blockstack-did-spec.md)[**[*](https://forum.blockstack.org/t/did-method-at-identity-foundation/4287/9)**]
* [Identity Hubs Capabilities Perspective](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/identity-hubs-capabilities-perspective.md) - Identity Hubs currently proposed in the Decentralized Identity Foundation (DIF) are a subset of a general Decentralized Identifier (DID). 
* [On DIF Hubs and Sovrin Agents](https://forum.sovrin.org/t/on-dif-hubs-and-sovrin-agents/897?u=phil)

#### DID Auth[**^**](#Contents) 
   * [DID Auth and the Little I-am-Me](https://medium.com/@markus.sabadello/did-auth-and-the-little-i-am-me-ec14d757ff09)
   * [Introduction to DID Auth](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/did-auth.md)
   —[[Markus Sabadello – Webinar 10](http://ssimeetup.org/introduction-did-auth-markus-sabadello-webinar-10/)]
* [A Universal Resolver for self-sovereign identifiers](https://medium.com/decentralized-identity/a-universal-resolver-for-self-sovereign-identifiers-48e6b4a5cc3c) [[**github**](https://github.com/decentralized-identity/universal-resolver)] [**[uniresolver.io](https://uniresolver.io/)**]

![](http://imgur.com/XMaq5cil.png)

### Evernym[**^**](#Contents)

* [Evernym](https://www.evernym.com/) [[**twitter**](https://twitter.com/evernym)] [[**github**](https://github.com/evernym/sovrin)] Founded in 2013
* [Identity System Essentials](https://www.evernym.com/wp-content/uploads/2017/02/Identity-System-Essentials.pdf) (Original Evernym Identity WP) 3/2016
* [The Three Models of Digital Identity Relationships — How self-sovereign identity (SSI) is different, and why it’s better](https://medium.com/evernym/the-three-models-of-digital-identity-relationships-ca0727cb5186) 
* [Is Self-Sovereign Identity the ultimate GDPR compliance tool? [1\3]](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-9d8110752f89) [[**2**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-40db94c1c437)] [[**3**](https://medium.com/evernym/is-self-sovereign-identity-ssi-the-ultimate-gdpr-compliance-tool-7296a3b07769)]

![](https://cdn-images-1.medium.com/max/800/0*uVmDqgtCxuoeylQ4.png)

### The Sovrin Foundation[**^**](#Contents)
 
* [Founded](http://www.windley.com/archives/2016/09/announcing_the_sovrin_foundation.shtml) in [September](https://www.prnewswire.com/news-releases/sovrin-foundation-launches-first-dedicated-self-sovereign-identity-network-300336702.html) 2016, The [Sovrin](https://sovrin.org/)
 Foundation is creating a public instance of the Hyperledger [Indy](#Hyperledger-Indy) code, initially developed by [Evernym](#Evernym) [[**Forum**](https://forum.sovrin.org/)] [[**Slack**](https://sovrin-slack-signup.herokuapp.com/)][[**Twitter**](https://twitter.com/SovrinID)][[**Github**](https://github.com/sovrin-foundation/sovrin)]
* [Sovrin Library](https://sovrin.org/library/)
* [Getting Started with Sovrin](https://sovrin.org/library/getting-started-with-sovrin/)
* [Sovrin: A Protocol and Token for Self-Sovereign Identity and Decentralized Trust](https://sovrin.org/wp-content/uploads/Sovrin-Protocol-and-Token-White-Paper.pdf)
* [Sovrin Network: What Goes on the Ledger?](https://sovrin.org/wp-content/uploads/2018/10/What-Goes-On-The-Ledger.pdf)
* [Sovrin Governance Framework](https://sovrin.org/library/sovrin-governance-framework/)
* [How Sovrin Works—A Technical Guide from the Sovrin Foundation](https://sovrin.org/wp-content/uploads/2018/03/How-Sovrin-Works.pdf)
* [Sovrin Test Network Trust Anchor Registration](https://s3.us-east-2.amazonaws.com/evernym-cs/sovrin-STNnetwork/www/trust-anchor.html)[[**Forum**](https://forum.sovrin.org/t/testing-on-the-sovrin-test-network-stn/643/17)]


#### Selected articles from Windley.com [**^**](#Contents)
* [An Internet for Identity](http://www.windley.com/archives/2016/08/an_internet_for_identity.shtml)
* [A Universal Trust Framework](http://www.windley.com/archives/2017/01/a_universal_trust_framework.shtml)
* [Building Your Business on Sovrin: Domain-Specific Trust Frameworks](http://www.windley.com/archives/2018/03/building_your_business_on_sovrin_domain-specific_trust_frameworks.shtml)
* [The Sovrin Foundation](http://www.windley.com/archives/2018/07/the_sovrin_foundation.shtml)
* [Decentralization in Sovrin](http://www.windley.com/archives/2018/10/decentralization_in_sovrin.shtml)
* [Self-Sovereign Identity and the Legitimacy of Permissioned Ledgers](http://www.windley.com/archives/2016/09/self-sovereign_identity_and_the_legitimacy_of_permissioned_ledgers.shtml)


#### Tykn Tech[**^**](#Contents)

![](http://imgur.com/1uO0AWll.png)

* [Tykn *The Future of Resilient Identity*](https://tykn.tech/) [[**twitter**](https://twitter.com/Tykn_tech)] [[**github**](https://github.com/tykntech)]
* [Tykn: Extended Overview](https://docs.google.com/document/d/1pNRO6aOb5eK4s8PVv7yS4x9TkqrGglCJ4jebU1F3Yzo/edit#)
* [Digital Identity Management in the Context of GDPR & Sovrin —Why Data Privacy Matters & How to Protect It](https://blog.tykn.tech/digital-identity-management-in-the-context-of-gdpr-sovrin-43028247378b)


### Hyperledger Indy[**^**](#Contents)

![](https://www.osiztechnologies.com/asset/oimages/hyperledger_indy/hyperledger_indy_02.png)

* [Hyperledger Indy - *Distributed Ledger and Utility Library*](https://www.hyperledger.org/projects/hyperledger-indy) [[**twitter**](https://twitter.com/Hyperledger)] [[**wiki**](https://wiki.hyperledger.org/projects/indy/documentation)] [[**github**](https://github.com/hyperledger/indy-sdk)]
* [indy.readthedocs.io](https://indy.readthedocs.io/) (under construction)
* [Hyperledger Welcomes Project Indy](https://www.hyperledger.org/blog/2017/05/02/hyperledger-welcomes-project-indy) - ANN
* [The Rise of Self-Sovereign Identity - Hyperledger Indy](https://wso2.com/blog/research/the-rise-of-self-sovereign-identity-hyperledger-indy)
* [Plenum Bzantine Fault Tolerant Protocol](https://github.com/hyperledger/indy-plenum/wiki)
   * "Byzantine fault tolerance is a sub-field of fault tolerance research inspired by the Byzantine Generals' Problem, which is a generalized version of the Two Generals' Problem."
* [An Accumulator Based on Bilinear Maps and Efficient Revocation for Anonymous Credentials](https://eprint.iacr.org/2008/539.pdf)
* [An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation](https://www.iacr.org/archive/eurocrypt2001/20450093.pdf)
* [SecureKey Technologies to explore interoperability between Verified.Me and Hyperledger Indy](https://securekey.com/press-releases/hyperledger-indy/)
* The Linux Foundation's [Blockchain for Business](https://www.edx.org/professional-certificate/linuxfoundationx-blockchain-for-business) edx course may be freely audited and has a section on Indy.
* [Implementing Privacy by Design in Hyperledger Indy](https://www.infoq.com/news/2018/09/Hyperledger-Indy-Privacy)
* [Indy Demo by IBM](https://www.youtube.com/watch?v=cz-6BldajiA) (video)
* [Verified Organization Network](https://vonx.io/) [[**github**](https://github.com/bcgov/von)] [[**^**](#Canada)]
   * "an initiative by the government of British Columbia to create a trusted network of organizational data. It allows organizations to claim credentials that are part of their own digital identity, using a component called [TheOrgBook](https://github.com/bcgov/theorgbook) that lists entities with their associated public verifiable claims."



#### IDEMix -Zero Knowledge Proof's in Evernym\Indy[**^**](#Contents)

>Our zero-knowledge proofs are part of the [Idemix protocol](http://domino.research.ibm.com/library/cyberdig.nsf/papers/EEB54FF3B91C1D648525759B004FBBB1/%24File/rz3730_revised.pdf), where they are used to prove the possession of [Camenisch-Lysyanskaya credentials](https://eprint.iacr.org/2001/019.pdf). We also use zero-knowledge proofs in the revocation protocol, which is based on [cryptographic accumulators](https://eprint.iacr.org/2008/539.pdf). —*[What Zero Knowledge Poof Algorithm is used in Sovrin?](https://forum.sovrin.org/t/what-zero-knowledge-proof-algorithm-is-used-in-sovrin/71/2)*

>Identity Mixer is not directly (re)implemented by Sovrin, but its cryptographic foundations are very similar, and Sovrin’s implementation includes most of its extended features (predicates, multi-credential, revocation, advanced issuance…). One of the researchers who helped to create Identity Mixer is on Sovrin’s Technical Governance Board and has offered insight to keep the implementations aligned on goals and methods. 
>—*[How is IDEMix Implemented?](https://forum.sovrin.org/t/how-idemex-is-implemented-in-sovrin-indy/)*

* [IBM Identity Mixer](https://www.zurich.ibm.com/identity_mixer/) | [blog](https://idemix.wordpress.com/)
  * [idemix in Hyperledger Fabric](https://hyperledger-fabric.readthedocs.io/en/release-1.3/idemix.html)
* [Concepts and Features of Privacy-Preserving Attribute-Based Credentials](https://github.com/p2abcengine/p2abcengine/wiki/Concepts-and-features)
* [AnonCreds: Anonymous credentials protocol implementation in python](https://github.com/hyperledger/indy-anoncreds) [[Usecase](https://github.com/hyperledger/indy-anoncreds/blob/master/docs/anoncred-usecase1.pdf)]


### IBM[**^**](#Contents)

* [Paving the Road to Self-Sovereign Identity with Blockchain, Open Standards](https://www.ibm.com/blogs/think/2017/10/self-sovereign-id-blockchain/)
* [github.com/IBM-Blockchain-Identity](https://github.com/IBM-Blockchain-Identity) (Docker based tutorial sandbox env)
* [How do we start tackling the existing identity problem](https://www.ibm.com/blogs/blockchain/2018/06/how-do-we-start-tackling-the-existing-identity-problem/)
* [Swipe Right on Verifiably Credentials](https://developer.ibm.com/code/2018/05/22/swipe-right-on-verifiable-credentials/)
* [WISeKey fully deployed its CertifyID integrating Digital Identity with Blockchain technology](https://globenewswire.com/news-release/2018/07/11/1535718/0/en/WISeKey-fully-deployed-its-CertifyID-integrating-Digital-Identity-with-Blockchain-technology.html)
* [SecureKey](http://securekey.com/): [partners with IBM](http://www-03.ibm.com/press/us/en/pressrelease/51841.wss) to enable a new digital identity and attribute sharing network based on Hyperledger Fabric blockchain.


### Ethereum[**^**](#Contents)

![](http://imgur.com/Fc6Hoo9l.png)

* [Decentralized Digital Identity on Ethereum](www.slideshare.net/FabriceCroiseaux/ethcc-2018-decentralized-digital-identity-on-ethereum) -SlideShare
* [ERC725](https://github.com/ethereum/EIPs/issues/725) | [ERC735](https://github.com/ethereum/EIPs/issues/735)
   * proposals in the Ethereum community to standardize smart contracts for certain identity-related operations such as key management, as well as signing transactions, documents, and "claims", which may be attested by third parties or self-asserted.
* [Proof-of-Individuality](http://proofofindividuality.online/) — how to prove a person only has one account
   * [Anti-Sybil Protocol using virtual pseudonym parties](https://medium.com/@unlisted/anti-sybil-protocol-using-virtual-pseudonym-parties-10276fcf3b20)
* [Managing Identity with a UI—ERC-725](https://medium.com/originprotocol/managing-identity-with-a-ui-for-erc-725-5c7422b38c09)
* [Ethereum ERC725 Blockchain Based, Self-Sovereign Identity Management](https://bitcoinexchangeguide.com/ethereum-erc725-blockchain-based-self-sovereign-identity-management/)
* [DEVCON1: Digital Identity](https://www.youtube.com/watch?v=QpaTOvAhLR4) — video from DEVCON1

#### Ethereum Identity Applications[**^**](#Contents)
* [uPort](https://www.uport.me/) [[**github**](https://github.com/uport-project/)] [[**twitter**](https://twitter.com/uport_me)]
   * [Ethereum studio ConsenSys launches digital IDs and assets secured on Ubuntu phones](http://www.ibtimes.co.uk/ethereum-studio-consensys-launches-internet-people-digital-ids-assets-secured-unbuntu-phones-1542620)
   * [Year in Review. What's to come in 2018](https://medium.com/uport/uport-year-in-review-whats-to-come-in-2018-15ccb9214439)
* [Deloitte SmartID](http://www.deloitte.co.uk/smartid/) [[**github**](https://github.com/SmartIdentity/smartId-contracts)]
   * "Smart Identity uses the Ethereum blockchain to represent an identity using a smart contract, attributes can be added by the identity owner and are stored in hash form"
* [Nuggets](http://www.nuggets.life/) [[**wp**](https://nuggets.life/images/Nuggets-White-Paper.pdf)]
   * "is a blockchain platform giving users a single biometric tool for login, payment and identity verification. It stores an individual's information in a "personal cloud" in "zero-knowledge blockchain storage".
* [Jolocom](http://jolocom.com/) 
   * a "SmartWallet" for everyone to own their personal digital identity, using [Social Linked Data](https://github.com/solid/solid-spec), WebID, and verifiable claims standards via Ethereum smart contracts. 
* [Democracy Earth Foundation](http://democracy.earth/) [[**github**](https://github.com/DemocracyEarth/paper)] 
   * developing *[Sovereign](http://sovereign.software/)*, a blockchain direct democracy tool using "vote" tokens to grant democratic participation rights to every human. A proof-of-individuality (POI) process based on peer-to-peer validation establishes that a self-sovereign identity is uniquely tied to a single person. The project introduces a number of interesting socio-technical concepts such as "Social Smart Contract", "Initial Rights Offering", and "Cryptographically Induced Equality". Cooperation is happening with other decentralized identity initiatives such as Blockstack and uPort.


### State Led Initiatives[**^**](#Contents)

* [Identity Validation as a Public Sector Digital Service?](https://blog.aniljohn.com/2014/07/identity-validation-as-a-public-sector-digital-service.html)
* [EU BLOCKCHAIN OBSERVATORY AND FORUM—Workshop Report e-Identity](https://www.eublockchainforum.eu/sites/default/files/reports/workshop_5_report_-_e-identity.pdf)

#### Canada [**^**](#Contents)
* [White Paper: Canada’s Digital ID Future - A Federated Approach](https://www.cba.ca/embracing-digital-id-in-canada)
* [BCGov Verifiable Organization Network – Impressive Client Demo](https://www.continuumloop.com/bcgov-verifiable-organization-network/)
* [Verified Organization Network](https://vonx.io/) [[**github**](https://github.com/bcgov/von)] 
   * "an initiative by the government of British Columbia to create a trusted network of organizational data. It allows organizations to claim credentials that are part of their own digital identity, using a component called [TheOrgBook](https://github.com/bcgov/theorgbook) that lists entities with their associated public verifiable claims."

#### Netherlands[**^**](#Contents)
* [TU Delft helps develop digital ID for use on your phone](https://www.tudelft.nl/en/2018/tu-delft/tu-delft-helps-develop-digital-id-for-use-on-your-phone/)
* [Self-Sovereign Identity Systems for Humanitarian Interventions—A Case Study on Protective Cash Transfer Programs](https://repository.tudelft.nl/islandora/object/uuid:6cdb5450-9a81-47a9-8ffa-f9bd77c72448/datastream/OBJ1/download)
* [Deployment of a Blockchain-Based Self-Sovereign Identity - Delft](https://arxiv.org/pdf/1806.01926.pdf)
* [TrustChain: A Sybil-resistant scalable blockchain - Presentation](http://msn.iecs.fcu.edu.tw/report/download.php?)
* [Dutch Blockchain Coalition](https://www.dutchdigitaldelta.nl/en/blockchain) | [Action Agenda](https://dutchdigitaldelta.nl/uploads/pdf/Dutch-Blockchain-Coalition-action-agenda-ENG.pdf)

#### USA[**^**](#Contents)
* [Illinois Blockchain Initiative](https://illinoisblockchain.tech/) — [partners with Evernym to launch birth registration pilot](https://illinoisblockchain.tech/illinois-partners-with-evernym-to-launch-birth-registration-pilot-f2668664f67c)
* [U.S. Department of Homeland Security funds four Blockchains](https://bravenewcoin.com/insights/u-s-department-of-homeland-security-funds-four-blockchain-companies-developing-new-cyber-security-technology)


#### Spain[**^**](#Contents)
* [Alastria](https://alastria.io/) [[**github**](https://github.com/alastria/alastria-identity)] 
   * a non-profit consortium building a national blockchain ecosystem for Spain. The security and veracity of information will be ensured through the identification of natural and legal persons, while at the same time allowing citizens to have control over their personal information in a transparent way following the guidelines set by the European Union.

#### Switzerland[**^**](#Contents)
* [Zug ID: Exploring the First Publicly Verified Blockchain Identity](https://medium.com/uport/zug-id-exploring-the-first-publicly-verified-blockchain-identity-38bd0ee3702) (uport\ethereum)

#### Estonia[**^**](#Contents)
* [Estonia National Blockchain-ID](https://e-estonia.com/solutions/e-identity/id-card/) | [id.ee](https://www.id.ee/)
   * [Estonian Blockchain ID Security Flaw](https://www.mccarthy.ca/en/insights/blogs/cyberlex/estonian-blockchain-based-id-card-security-flaw-raises-issues-about-identity)

### Blockchain ID Initiatives [**^**](#Contents)
* [Danube Tech](http://danubetech.com/) — digital identity and personal data, including personal agents, semantic graphs, and blockchain [[**xdi**](https://xdi2.org)] [[**navigator**](https://github.com/projectdanube/xdi2)]
   * Founded by [Markus Sabadello (Peacekeeper)](http://mydata2016.org/speaker/markus-sabadello/) [[**twitter**](https://twitter.com/peacekeeper)] [[**github**](https://github.com/peacekeeper)] [[**blog**](https://medium.com/@markus.sabadello)]
* [Identity at Coinbase: Welcoming the Distributed Systems team](https://blog.coinbase.com/identity-at-coinbase-welcoming-the-distributed-systems-team-d929dd64de2e) [[**wired**](https://www.wired.com/story/coinbase-distributed-systems-acquisition/)]
* [Proof of Authority](https://blockonomi.com/proof-of-authority/)
* [Shocard](https://shocard.com/) — "Blockchain-Based Mobile Identity Platform"
* [Authenteq](http://authenteq.com/) [[**twitter**](https://twitter.com/authenteq)] [[**github**](https://github.com/authenteq)]
  * enables users to create their own sovereign digital IDs which are stored encrypted on [BigChainDB](http://docs.bigchaindb.com)
* [JLinc](https://www.jlinc.com/) — registers cryptographic public keys on the Stellar blockchain. 
   > "The founders have been at the center of a community of developers working on “user-centric digital identity for almost two decades."
* [Internet of People](https://iop.global/) — "an open, decentralized infrastructure consisting of device-to-device communication, blockchain tokens, profile servers, and other components." -Founded by [Fermat](http://www.fermat.org)
* [Blockchain Helix](http://blockchain-helix.com)[[**ico**](https://ico.helix-orange.com/)][[**wp**](https://ico.helix-orange.com/wp-content/uploads/2018/08/HELIX-Orange_Whitepaper_v1.5.pdf)]
   * "Identity as a Service", "Data as a Service" and "Blockchain as a Service" The company offers to increase the speed of KYC/AML processes while hughly decreasing the cost 
* [Civic](https://www.civic.com/) launches: [identity.com](https://identity.com)[[**github**](https://github.com/identity-com/)][[**blog**](https://www.civic.com/blog/identity-com-first-open-source-update/)]
* [Mooti](https://mooti.co/) | [docs](https://docs.mooti.co/)
   * offers an "identity chain" technology that makes it possible to issue and revoke verified claims using elliptic curve cryptography (curve25519, secp256k1) and includes privay-enhancing features
* [Spidchain](http://www.spidchain.com/) [[**wp**](https://drive.google.com/file/d/0B89WE3IIHmy1Z0ZSSWVmVEtaaG8/view)]
   * "offers a platform for self-sovereign identity, including desktop and mobile apps for end-users. It uses Decentralized Identifiers (DIDs) - backed by optionally Bitcoin or Ethereum - to implement a marketplace for verifiable claims. The Spidchain applications allow individuals to create, recover, and revoke DIDs, to authenticate, to sign and verify files and claims, and more."
* [Cicada](https://github.com/the-laughing-monkey/cicada-platform)
   * a Dapp platform built for a "direct democracy." envisions using iris scans to generate decentralized universal identifiers ("HUIDs") for every human on the planet, a method referred to as "biocryptics". "HUIDs" can have "sub-IDs" to support selective disclosure. PII can be stored in an "info wallet". Key parts of the system also include smart contracts, zero-knowledge proofs, mixnets, and more."
* [Keyp](https://keyp.io/) —"Welcome to Europe’s fastest growing open digital identity ecosystem."
* [I/O Digital Foundation](https://iodigital.io/) [**[whitepaper](https://simplebooklet.com/iocoinwhitepaper#page=0)**]
   * "offers a Proof-of-Stake blockchain called Decentralised Input Output Name Server (DIONS). It will enable applications such as identity and alias registration, storage of legal documents, key exchange, and encrypted messaging."

### Humanitarian[**^**](#Contents) 
* [iRespond](https://www.irespond.org/) -international non-profit organization dedicated to solving the identity problem using a unique digital biometric identity solution
* [The Humanized Internet](http://www.thehumanizedinternet.org/) — "to defend the rights of vulnerable people, and give every human being worldwide secure, sovereign control over their own digital identity."
* [CheapID](http://guptaoption.com/cheapid/) - identity standard designed for use in conflicted environment like those many refugees or disaster victims may find themselves in.
  * uses [State In A Box - Identity Services Architecture](http://guptaoption.com/4.SIAB-ISA.php)
* [World Identity Netowork](https://win.systems/)  —Blockchain for Impact [(BFI)-UN]((https://www.pvblic.org/blockchainforimpact))


### Structured Data Standards[**^**](#Contents) 

* [Blockcerts](https://www.blockcerts.org) — open standard for issuing and verifying blockchain-based official records; The project offers  open-source libraries, tools, and mobile apps. MIT has [issued](https://www.insidehighered.com/news/2017/10/19/mit-introduces-digital-diplomas) digital certificates based on this standard.
  * [A Decentralized Approach to Blockcerts Credential Revocation](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/blockcerts-revocation.md)
* [Schema](https://schema.org) — a collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet. Schema.org vocabulary can be used with many different encodings, including RDFa, Microdata and JSON-LD. These vocabularies cover entities, relationships between entities and actions, and can easily be extended through a well-documented extension model. Over 10 million sites use Schema.org to markup their web pages and email messages. Many applications from Google, Microsoft, Pinterest, Yandex and others already use these vocabularies to power rich, extensible experiences."
   * [ÆTERNITY](http://aeternity.com/) [[**github**](https://github.com/aeternity/protocol)]: using Schema's standards: "offers an identity architecture where every account has a unique ID number, and unique names can be registered and linked to arbitrary data such as addresses on the blockchain. Schema's are used for representing data about persons and organizations."
* [DIDs the Decentralized Identifiers of the W3C^](#DID-the-Decentralized-Identifier)


### Decentralized Public Key Infrastructure (DPKI)[**^**](#Contents) 
* [Blockstack](https://blockstack.org/) — [[**github**](https://github.com/blockstack)][[**forum**](https://forum.blockstack.org/)][[**blog**](https://blockstack.org/blog)][[**twitter**](https://twitter.com/blockstack)]
   * a network of computers that collectively maintain a global registry of domain names, public keys, and cryptographic hashes. With this registry, Blockstack serves as a decentralized domain name system (DNS) and a decentralized public key infrastructure (PKI).
   * [Onename](https://onename.com/) — "a product built on Blockstack that allows people to register identities"
* [Decentralized Public Key Infrastructure](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust/blob/master/final-documents/dpki.pdf)
* [DIDs in DPKI](https://github.com/WebOfTrustInfo/rwot7/blob/master/topics-and-advance-readings/dids-in-dpki.md)
* [SCPKI: A Smart Contract-based PKI and Identity System](http://www0.cs.ucl.ac.uk/staff/M.AlBassam/publications/scpki-bcc17.pdf)
* [KeyChains: A Decentralized Public-Key Infrastructure](https://drum.lib.umd.edu/bitstream/handle/1903/3332/0.pdf?sequence=1&isAllowed=y)
* [ClaimChain: Decentralized Public Key Infrastructure](https://www.researchgate.net/publication/318584251_ClaimChain_Decentralized_Public_Key_Infrastructure)
* [A Decentralized Public Key Infrastructure with Identity Retention](https://eprint.iacr.org/2014/803.pdf)
* [Privacy based decentralized Public Key Infrastructure
(PKI) implementation using Smart contract in
Blockchain](https://isrdc.iitb.ac.in/blockchain/workshops/2017-iitb/papers/paper-11%20-%20Decentralized%20PKI%20in%20blockchain%20and%20Smart%20contract.pdf)


### Personal Data: Wallets, Marketplaces, etc.[**^**](#Contents)

* [Mydata](http://mydata.org/) [[**twitter**](https://twitter.com/mydataorg)] [[**papers**](https://mydata.org/papers/)] [[**declaration**](https://mydata.org/declaration/)]
   * goal: to empower individuals with their personal data, thus helping them and their communities develop knowledge, make informed decisions, and interact more consciously and efficiently with each other as well as with organisations."
   * [Consent](http://www.consent.global/)[[**12**](https://sovrin.org/steward/global-consent/)] — "platform for trusted personal data applications and services, using Ethereum smart contracts to implement decentralized identifiers, verified credentials, consent receipts, a web of trust, and exchange of assets and value." 
* [Pillar Project](http://pillarproject.io)  [[**wp**](https://pillarproject.io/documents/Pillar-Gray-Paper.pdf)]
   * planning to offer a "Personal Data Locker" consisting of a wallet, browser, and token exchange. Personal assets will be put on a blockchain, and "Pillar" tokens will be issued."
* [Aversafe](https://www.aversafe.com/) —"allows individuals to store personal details, work history, certificates and achievements. It leverages a permissioned blockchain for trusted audit and participation in the storage of attestation data separate from the actual data stored"
* [Datum](https://datum.org) [[**wp**](https://datum.org/assets/Datum-WhitePaper.pdf)]
   * "network allows anyone to store structured data on a smart contract blockchain. Data can optionally be bought and sold on a marketplace using the DAT token. Datum leverages BigchainDB and IPFS as data storage backends. All data is encrypted and protected using AES256-GCM.
* [ONTology](https://ont.io/) [[**github**](https://github.com/ontio/ontology-DID)]— "a "Distributed Trust Network" which combines a cross-chain identity system, peer-to-peer data transmission, data authorization mechanisms, distributed data storage, attestation, and various industry-specific modules. It also includes an Ontology Crypto Package (OCP) and an Ontology Marketplace (OM)."
* [We can do better than selling our data](http://blogs.harvard.edu/doc/2018/09/18/data/)-Doc Searls(*IIW*)
* [Pro-civis](https://procivis.ch) — "e-government as a service" platform called "eID+". It enables citizens to get an official, electronic Citizen-ID on a mobile app. 
   * The platform includes the [Vetri](https://vetri.global/) wallet and marketplace. 'Earn extra income and rewards by joining the data economy.'"

![](https://oneworldidentity.com/wp-content/uploads/2018/10/companies.png)

2018 Identity Landsacpe brought to you by: [One World Identity](https://oneworldidentity.com/) — independent advisory and digital strategy consultancy focused on trust and the data economy.

### EU General Data Protection Regulation Act[**^**](#Contents)

* [Blockchains and Data Protection in the European Union](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3080322)
* [IBM — How blockchain could address five areas associated with GDPR compliance](https://www-01.ibm.com/common/ssi/cgi-bin/ssialias?htmlfid=61014461USEN)
* [GDPR - A reflection on the 'self-sovereign identity' and the Blockchain](https://www.linkedin.com/pulse/gdpr-reflection-self-sovereign-identity-blockchain-nicolas-ameye/)
* [GDPR and Privacy by Design, What developers need to know](https://medium.com/@sphereidentity/gdpr-and-privacy-by-design-what-developers-need-to-know-fa5a936da65a)
* [Privacy by Design The 7 Foundational Principles](https://www.ipc.on.ca/wp-content/uploads/Resources/7foundationalprinciples.pdf) 
* [When GDPR Becomes Real, and Blockchain is no longer fairydust](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/gdpr.md)
* [Digital Identity Management in the Context of GDPR & Sovrin —Why Data Privacy Matters & How to Protect It](https://blog.tykn.tech/digital-identity-management-in-the-context-of-gdpr-sovrin-43028247378b)
* [Self-Sovereign Privacy By Design](https://github.com/sovrin-foundation/protocol/blob/master/self_sovereign_privacy_by_design_v1.md)

### Reports[**^**](#Contents)
* [How Blockchain Revolutionizes Identity Management](https://www.accenture-insights.nl/en-us/articles/how-blockchain-will-revolutionize-identity-management)
* [Digital Identity: the current state of affairs](https://www.bbvaresearch.com/wp-content/uploads/2018/02/Digital-Identity_the-current-state-of-affairs.pdf)
* [Blockchain: Evolving Decentralized Identity Design](https://www.gartner.com/doc/3834863/blockchain-evolving-decentralized-identity-design)
* [White Paper: Canada’s Digital ID Future - A Federated Approach](https://www.cba.ca/embracing-digital-id-in-canada)
* [IDENTITY MATTERS](https://cboxxtest.files.wordpress.com/2017/09/cboxxidentitymatters04.pdf)
* [Accenture: ID2020: DIGITAL IDENTITY with Blockchain and Biometrics](https://www.accenture.com/us-en/insight-blockchain-id2020)
* [Privacy-Preserving Authentication, Another Reason to Care about Zero-Knowledge Proofs —slideshare](https://www.slideshare.net/eralcnoslen/privacypreserving-authentication-another-reason-to-care-about-zeroknowledge-proofs)
* [r3- Identity in Depth](https://www.r3.com/wp-content/uploads/2017/06/Identity_indepth_r3.pdf)
* [Global Blockchain Identity Management Market 2018-2022](https://www.technavio.com/report/global-blockchain-identity-management-market-analysis-share-2018)
* [A Comprehensive Guide to Self Sovereign Identity](https://ssiscoop.com/) - by Kaliya ['Identity Woman'](https://twitter.com/IdentityWoman) Young and [Heather Vescent](https://twitter.com/heathervescent)


### Assorted Thoughts
* [Decentralized Identity Trilemma](http://maciek.blog/decentralized-identity-trilemma/)
   >There seems to exist a trilemma in decentralized identity analogous to @Zooko's triangle. None of the existing solutions are at the same time: 1) privacy-preserving, 2) Sybil-resistant 3) self-sovereign -[[**twitter**](https://twitter.com/MaciekLaskus/status/1031859093072424960)]
   * [Maciek Laskus | BLOCKWALKS](https://www.youtube.com/watch?v=KAgJpQfQXxs) (video)
   * "[I designed](https://twitter.com/MaciekLaskus/status/1066780557906976768) an algorithm that mapped out people working on identity using Twitter data:" [Identity list](https://docs.google.com/spreadsheets/d/1hBBVA0-jqmRRZ_JFQ8HEck9tFub7crsqRzlBZWf01xg/edit?usp=sharing)
* [Proof of Thought (PoT)](https://bitcointalk.org/index.php?topic=4459113.0)
* [Queer Privacy](https://leanpub.com/queerprivacy)
   >Stories about using the Internet as a tool to find out more about yourself, and as a tool to express and empower; about the dangers of Internet censorship and about the practical realities of maintaining multiple distinct digital identities. 
* [@SarahJamieLewis Twitter on Identity](https://twitter.com/SarahJamieLewis/status/1041043532654542848)
   >Any technology which relies on the existence of, or attempts to create a, global, unique identity is oppressive by design. Stop" innovating" oppressive structures.


### Research-Papers[**^**](#Contents)
* [Establishing Identity Without Certification Authorities](http://irl.cs.ucla.edu/~yingdi/pub/papers/Ellison-OldFriend-USENIX-Security-1996.pdf)
* [A First Look at Identity Management Schemes on the Blockchain](https://arxiv.org/pdf/1801.03294.pdf)
* [ChainAnchor — Anonymous Identities for Permissioned Blokchains](http://connection.mit.edu/wp-content/uploads/sites/29/2014/12/Anonymous-Identities-for-Permissioned-Blockchains2.pdf)
* [Decentralizing Privacy: Using Blockchain to Protect Personal Data](http://web.media.mit.edu/~guyzys/data/ZNP15.pdf)
* [TOWARDS SELF-SOVEREIGN IDENTITY USING BLOCKCHAIN TECHNOLOGY](http://essay.utwente.nl/71274/)
* [Self-sovereign Identity –	Opportunities and Challenges for the Digital Revolution](https://arxiv.org/pdf/1712.01767.pdf)
* [The Knowledge Complexity Of Interactive Proofs](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.419.8132&)
* [A Conceptual Analysis on Sovrin](https://www.researchgate.net/publication/323144927_A_Conceptual_Analysis_on_Sovrin)



### Video[**^**](#Contents)
* [SSI Meetup Youtube Channel](https://www.youtube.com/channel/UCSqSTlKdbbCM1muGOhDa3Og)
* [The Story of Open SSI Standards - Drummond Reed](https://www.youtube.com/watch?v=RllH91rcFdE&feature=youtu.be&t=4m30s)
* [Is Blockchain the Future of Digital Identity?](https://youtu.be/Aub5dNpj2_k) -CB Insights
* [Identity and Blockchain Technology](https://www.youtube.com/watch?v=Aub5dNpj2_k)
* [Phil Windley on the Sovrin Network](https://www.youtube.com/watch?v=IxQUL2ztFi8)


### Podcasts[**^**](#Contents)
* [State of Identity](https://oneworldidentity.com/podcasts/)
* [Analytics Neat—Episode 37: What is a Decentralized Identity (DID)?](https://player.fm/series/analytics-neat/episode-37-what-is-a-decentralized-identity-did)
* [State Change #41 Unpacking Digital Identity](https://media.consensys.net/state-change-41-unpacking-digital-identity-christian-lundkvist-stephen-wilson-4fb5a75eb6ed)
* [MyData Podcast](https://mydata.org/podcast/)

### Sources[**^**](#Contents)
* [/awesome-sovrin](https://github.com/infominer33/awesome-decentralized-id/tree/master/awesome-sovrin)
* [IIW-Wiki](http://iiw.idcommons.net/Main_Page)
* [wiki.idcommons.net](http://wiki.idcommons.net/Main_Page)
* [/WebOfTrustInfo](https://github.com/WebOfTrustInfo/)
* [/peacekeeper/blockchain-identity](https://github.com/peacekeeper/blockchain-identity)
* [/blockchain-id.toml](https://github.com/infominer33/awesome-decentralized-id/blob/master/blockchain-id.toml)
* [identitywoman.net](https://identitywoman.net/)
* [windley.com/tags/identity](http://www.windley.com/tags/identity.shtml)


---

### Brought to you by: [The Crypto Library—Super Source](https://github.com/infominer33/Crypto-library)

BTC— 1GvkjHtiy9LUjVkStnEAXxjhcoS56aCokY

![](http://imgur.com/yXLLm9Bl.png) 

DOGE— DSzMxfABB8EwKiumzV7YHhS7HTvWAyM7QF

![](https://i.imgur.com/0zBLoUP.png) [<img src="https://i.imgur.com/zeYCNMS.jpg" align="right" width="150" height="140">](https://github.com/infominer33/Crypto-library)
