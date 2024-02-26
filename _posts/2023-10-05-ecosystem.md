---
title: Ecosystem Overview
description: A high level view of the Verifiable Credentials ecosystem.
permalink: /ecosystem/
categories: ["About"]
excerpt: This page includes a breakdown of the Web Standards, Protocols,Open Source Projects, Organizations, Companies, Regions, Government and Policy surrounding Verifiable Credentials and Self Sovereign Identity.
last_modified_at: 2024-02-26
---

**Note to reader**
**This is a Work in Progress, and should not be taken as authoritative or comprehensive.**
_Internal Links in Italic_
{: .notice--info}

## Open Standards
### [*Decentralized Identifiers*]({{site.baseurl}}/web-standards/w3c/decentralized-identifier/) 

- [*Explainer*]({{site.baseurl}}/web-standards/w3c/decentralized-identifier/#Explainer) 
- [*Literature*]({{site.baseurl}}/web-standards/w3c/decentralized-identifier/#literature) 
- [*DID* Methods]({{site.baseurl}}/web-standards/w3c/decentralized-identifier/did-methods/) 
- [*Supporting* Tech]({{site.baseurl}}/web-standards/w3c/decentralized-identifier/#Supporting) 
  - [*DIDAuth*]({{site.baseurl}}/projects/decentralized-identity-foundation/did-authentication/) 
- [*Critique*]({{site.baseurl}}/self-sovereign-identity/critique-caution/) 

### Verifiable Credentials

- [*Explainer*]({{site.baseurl}}/web-standards/w3c/verifiable-credentials/#About) 
- [*Comparisons*]({{site.baseurl}}/web-standards/w3c/verifiable-credentials/#Comparisons) 
- Varieties
  - Data Integrity
    - [*JSON*-LD LD-Proof]({% link _posts/web-standards/DIDs-and-VCs/2023-09-08-VC-Data-Integrity_LD-Proofs.md %}) (w3c) 
    - [*JSON*-LD ZKP BBS+]({% link _posts/web-standards/DIDs-and-VCs/2023-09-08-VC-Data-Integrity_LD-Proofs.md %}) (w3c) 
  - [*JOSE / COSE*]({% link _posts/web-standards/DIDs-and-VCs/2023-09-08-VC_JOSE-COSE.md %})  
    - [JSON SD-JWT](https://www.ietf.org/id/draft-terbu-sd-jwt-vc-02.html) (ietf) 
    - [JWP](https://www.ietf.org/archive/id/draft-jmiller-jose-json-web-proof-00.html) (ietf) 
  - [*ZKP-CL*]({% link _posts/web-standards/DIDs-and-VCs/2023-09-08-VC-ZKP-CL.md %}) (Hyperledger) 

### Related

- [*JSON-LD*]({{site.baseurl}}/web-standards/w3c/json-ld/) (W3C) 
- [JSON](https://datatracker.ietf.org/doc/html/rfc8259) (IETF) 
- [*BBS*]({{site.baseurl}}/web-standards/w3c/verifiable-credentials/data-integrity-bbs+/#blum-blum-shub) (SIAM 1986) 

### Exchange Protocols

- [*DIDComm*]({% link _posts/open-source-projects/2020-11-26-DID-communications.md %}) (DIF) 
- [*CHAPI*]({{site.baseurl}}/web-standards/exchange-protocol/#CHAPI) (DIF) 
- [*OIDC4VC*]({{site.baseurl}}/web-standards/openid/openid-connect/#Verifiable Credentials) (OpenID) 
- [*mDL*]({{site.baseurl}}/web-standards/mobile-drivers-license-mdl-iso-18013/) (ISO/IEC) 
- [*WACI-Pex*]({{site.baseurl}}/web-standards/exchange-protocol/#WACI) (DIF) 
- [*VC-HTTP-API*]({{site.baseurl}}/web-standards/exchange-protocol/#VC%20Api) (CCG) 

### Authorization Protocols

- [zCap](https://w3c-ccg.github.io/zcap-spec/) (w3c) 
- [UCAN](https://github.com/ucan-wg/spec/) (Fission, Bluesky, Protocol Labs) 
- [GNAP](https://datatracker.ietf.org/wg/gnap/about/) (IETF) 
- [OAuth](https://www.ietf.org/rfc/rfc6749.txt) (IETF) 

### ISO Standards

- [mDL](https://www.iso.org/standard/69084.html) (ISO/IEC 18013-5) 
- [JTC 1/SC 17/WG 3 - Travel Documents](https://standards.iteh.ai/catalog/tc/iso/58084a13-b883-4f4a-a372-7a5f9e4dca60/iso-iec-jtc-1-sc-17-wg-3) (ISO/IEC) 
- [ISO 27001](https://www.iso.org/standard/27001) 

### Data Stores

- [Encrypted Data Vaults](https://identity.foundation/edv-spec/) - EDV (DIF) 
- [Decentralized Web Node](https://identity.foundation/decentralized-web-node/spec/) - DWN (DIF) 

### Trust Frameworks

- [800-63-3](https://pages.nist.gov/800-63-3/) (NIST) 
- [*PCTF*]({{site.baseurl}}/government/canada/pctf/) (DIACC) 

### Non SSI Identity Standards

- [*OpenID*]({{site.baseurl}}/organizations/openid/) (OpenID) 
- [FIDO](https://fidoalliance.org/) (FIDO) 
- [OAuth](https://datatracker.ietf.org/wg/oauth/about/) (IETF) 
- [SCIM](https://datatracker.ietf.org/wg/scim/about/) (IETF) 
- [SAML](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) (OASIS) 
- [KMIP](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=kmip) (OASIS) 
- [*WebAuthN*]({{site.baseurl}}/web-standards/w3c/webauthn/) (W3C) 
- [Secure QR Code](https://docs.oasis-open.org/esat/sqrap/v1.0/csd01/sqrap-v1.0-csd01.html) (OASIS) 
- Blockchain Standards
    - [ISOTC 307](https://www.iso.org/committee/6266604.html) (ISO) 
    - [CEN/CLC/JTC 19](https://standards.cencenelec.eu/dyn/www/f?p=205:7:0::::FSP_ORG_ID:2702172&cs=148F2B917E4B67BCFD6FE36CE0EA923AC) (CEN/EENTLIC) 
    - [*ERC-EIP*]({{site.baseurl}}/blockchain/ethereum/#erc-eip) (Ethereum) 

## Code-Bases

### Open Source Projects

- [*Universal Resolver*]({{site.baseurl}}/projects/decentralized-identity-foundation/identifiers-and-discovery/#universal-resolver) (DIF) 
- [KERI]({%link _posts/open-source-projects/2020-11-22-keri.md %}) (DIF) 
- [Other Tools & Libraries](https://github.com/decentralized-identity) (DIF) 
- [ESSIF-Lab](https://essif-lab.eu/) (ESSIF-Lab) 
- [*Aires*]({{site.baseurl}}/projects/hyperledger/aries/) (Hyperledger) 
- [*Indy*]({{site.baseurl}}/projects/hyperledger/indy/) (Hyperledger) 
- [Ursa]({%link _posts/open-source-projects/2021-04-16-ursa.md%}) (Hyperledger) 
- [Other Tools & Libraries](https://wiki.hyperledger.org/display/IWG) (Hyperledger) 
- [Blockcerts]({%link _posts/web-standards/2020-01-07-blockcerts.md%}) (Hyland) 

### Company Code

- [Walt.id](https://github.com/walt-id) 
- [Verite](https://github.com/circlefin/verite) 
- [SpruceID](https://github.com/spruceid) 

## Organizations

### International Standard Development Organizations [SDO]

- [*W3C*]({{site.baseurl}}/_posts/web-standards/2020-11-09-world-wide-web-consortium_w3c.md) 
- [IETF](https://ietf.org) 
- [OASIS](https://www.oasis-open.org/) 
- [ITU-T](https://www.itu.int/en/ITU-T/Pages/default.aspx) 
- [ISO](https://www.iso.org/home.html)/[IEC](https://iec.ch/homepage) 

### National Government/Standard Setting Bodies

- [NIST](https://www.nist.gov/) 
- [The Standards Council of Canada](https://www.scc.ca/) 
- [BSI](https://www.bsi.bund.de/EN/Home/home_node.html)  - The Federal Office for Information Security, Germany

### Community Organizations

- [*W3C - CCG*]({{site.baseurl}}/_posts/web-standards/2023-05-15-credentials-community-group.md) 
- [*DIF*]({{site.baseurl}}/_posts/organizations/2019-03-07-identity-foundation.md) 
- [*ToIP*]({{site.baseurl}}/_posts/organizations/2023-06-05-TOIP.md) 
- [ADIA](https://adiassociation.org/) 
- [Kantara](https://kantarainitiative.org/) 
- [*MyData*]({%link _posts/organizations/2019-04-04-mydata.md%}) 
- [*DIACC*]({%link _posts/government/canada/2020-12-04-diacc.md%}) 
- [*ID2020*]({%link _posts/organizations/2021-04-15-id2020.md%}) 
- [*OpenID Foundation*]({%link _posts/organizations/2023-08-12-openid.md%}) 
- [Internet Safety Labs](https://internetsafetylabs.org) 
- [*GLEIF*]({%link _posts/organizations/2021-04-16-gleif.md%}) 
- [*Hyperledger Foundation*]({%link _posts/organizations/2020-10-11-hyperledger.md%}) 
- [FIDO Alliance](https://fidoalliance.org/) 
- [OASIS](https://www.oasis-open.org/) 

### SSI Networks

- [DizmeID](https://www.dizme.io/) 
- [*Sovrin*]({%link _posts/organizations/2019-03-09-sovrin-foundation.md%}) 
- [BedRock](https://bedrock-consortium.github.io) 
- [*ONT*]({%link _posts/web3/2020-11-11-ontology.md%}) 
- [Velocity](https://www.velocitynetwork.foundation/) 
- [*GlobalID*]({%link _posts/companies/2023-03-02-GlobalID.md%}) 
- [Dock](https://dock.io) 
- [ITN](https://dlt.mobi/itn/) , Mobi

## Companies

- [*Microsoft*]({%link _posts/companies/2019-03-08-microsoft.md%})  - Azure / Entra

### EU SSI Startups

- [*MyDex*]({%link _posts/companies/2023-03-08-MyDex.md%}) 
- [*MeeCo*]({%link _posts/companies/2020-11-04-meeco.md%}) 
- [*ValidatedID*](%link _posts/companies/2023-03-12-ValidatedID.md%) 
- [Bloqzone](https://bloqzone.com/) 
- [Procivis](https://www.procivis.ch/en/home) 
- [Gataca](https://gataca.io/) 

### US SSI Startups

- [Dock](https://www.dock.io/) 
- [Anonoyome](https://anonyome.com/) 
- [*GlobalID*]({%link _posts/companies/2023-03-02-GlobalID.md%}) 
- [*Hyland*]({%link _posts/companies/2020-11-08-hyland-credentials.md%}) 
- [*Magic*]({%link _posts/companies/2023-03-06-MagicLabs.md%}) 
- [*IDRamp*](%link _posts/companies/2023-03-03-IDramp.md%) 
- [*Indicio*]({%link _posts/companies/2023-03-04-Indicio.md%}) 
- [*Verified Inc*](https://www.verified.inc/) (formerly UNUMID) 
- [*Animo*](https://animo.id/) 
- [*Mattr*]({%link _posts/companies/2020-11-03-mattr.md%}) 
- [*Liquid Avatar*](https://www.liquidavatar.com/) 
- [*Hedera*](https://hedera.com/) 
- [*IOTA*](https://www.iota.org/solutions/digital-identity) 
- [*Trinsic*]({%link _posts/companies/2020-11-08-trinsic.md%}) 
- [*Transmute*]({%link _posts/companies/2020-11-04-transmute.md%}) 
- [*Spruce*](%link _posts/companies/2023-03-10-Spruce.md%) 
- [*Disco.xyz*](%link _posts/companies/2023-05-14-disco.xyz.md%) 

### Asia SSI Startups

- [Affinidi](https://www.affinidi.com/) 
- [ZADA](https://zada.io/) 
- [Dhiway](https://dhiway.com/) 
- [Ayanworks](https://www.ayanworks.com/) 
- [NewLogic](https://newlogic.com/) 

### Africa SSI Startups

- [FlexID](https://flexfintx.com/) 
- [Diwala](https://www.diwala.io/) 

### Acquisitions

- [Avast-Evernym-SecureKey](https://www.ledgerinsights.com/avast-acquires-second-blockchain-decentralized-identity-provider-securekey/) 

### Analyst Firms

- [KuppingerCole](https://www.kuppingercole.com/) 
- [Forrester](https://www.forrester.com/bold) 
- [Gartner](https://www.gartner.com/en) 

### Consulting Firms

- [Deloitte](https://www.deloitte.com/) 
- [Accenture](https://www.accenture.com/) 
- [McKinsey](https://www.mckinsey.com/) 
- BCG

### IAM Industry

- [Ping](https://www.pingidentity.com/en.html) (TomaBravo rollup) 
- [Okta](https://www.okta.com/) 
- [Auth0](https://auth0.com/) 
- [ForgeRock](https://seekingalpha.com/article/4560880-forgerock-acquisition-thoma-bravo-continues-roll-up-in-identity-and-access-management-space) (TomaBravo rollup) 
- [IDENTOS](https://www.identos.com/) 
- [SailPoint](https://www.sailpoint.com/) (TomaBravo rollup) 

## Policies/Regulations (by region)

- [FATF](https://www.fatf-gafi.org/en/home.html) 

### Europe

- [*Data Governance Act*]({%link _posts/government/europe/2023-06-10-data-governance-act.md%}) 
- [*GDPR*]({%link _posts/government/europe/2019-03-01-gdpr.md%}) 
- [*eIDAS1*]({%link _posts/government/europe/2020-01-06-eIDAS.md%}) 
- [*eIDAS2*]({{site.baseurl}}/government/europe/eu/eidas/#eidas-20) 
- [*UK Data Protection*](https://www.gov.uk/data-protection) 

### [Asia](https://www.apacdigitalid.org/en/)

### [*USA*](({{site.baseurl}}/government/india/)) 

- [COPPA](https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa) 
- [Privacy Act](https://www.hhs.gov/foia/privacy/index.html) 
- [California SB786](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB786) 

### [*India*]({{site.baseurl}}/government/india/) 

### [*Canada*]({{site.baseurl}}/government/canada/) 

- [*Pan Canadian Trust Framework (PCTF)*]({{site.baseurl}}/government/pctf/) 

## Government Initiatives

### US

- [*SVIP*]({{site.baseurl}}/government/usa/dhs/) 
- [National Cybersecurity Strategy](https://www.whitehouse.gov/wp-content/uploads/2023/03/National-Cybersecurity-Strategy-2023.pdf) 

### Germany

- [IDUnion](https://idunion.org/?lang=en) 

### UK

- [Scotland](https://blogs.gov.scot/digital/wp-content/uploads/sites/5/2019/05/Digital-Identity-Scotland-Attribute-Standards-31-May-2019.pdf) 
- [UK Digital Strategy](https://www.gov.uk/government/publications/uks-digital-strategy/uk-digital-strategy) 

### EU

- eIDAS2 
  - [Large Scale Pilots](https://utimaco.com/news/blog-posts/eidas-20-moving-closer-european-digital-identity-wallet-ediw-and-pilot)  
  - [*Architecutre* and Reference Framework]({{site.baseurl}}/government/europe/eu/eidas/#eu-digital-identity-framework) 
- [*EBSI*]({{site.baseurl}}/government/europe/eu/ebsi-essif/) 
- [*ESSIF*-Lab]({{site.baseurl}}/history/2020s/early/essif-lab/) 
- [*Catalonia*]({{site.baseurl}}/government/europe/#catalonia) 
- Switzerland

### APAC

- [*New Zealand*]({{site.baseurl}}/government/new-zealand/) 
- [*Australia*]({{site.baseurl}}/government/australia/) 
- [Singapore](https://www.developer.tech.gov.sg/our-digital-journey/digital-government-exchange/files/DGX%20DIWG%202022%20Report%20v1.5.pdf) 
- [South Korea](https://www.w3.org/community/did-kr/) 

### Canada

- [*BCGov*]({{site.baseurl}}/government/canada/bcgov/) 
- [*Alberta*]({{site.baseurl}}/government/canada/#alberta) 
- [*Ontario*]({{site.baseurl}}/government/canada/#ontario) 

### LatAm

- [LACCHAIN](https://www.lacchain.net/) 

## Real-World Implementation

- **Government Issued ID**
  - Passport [eMRTD](https://www.icao.int/Meetings/TAG-MRTD/TagMrtd22/TAG-MRTD-22_WP24-rev-2.pdf)/[DTC](https://www.icao.int/Security/FAL/TRIP/PublishingImages/Pages/Publications/Guiding%20core%20principles%20for%20the%20development%20of%20a%20Digital%20Travel%20Credential%20%20%28DTC%29.PDF) (ICAO)
  - [Immigraion](https://www.slideshare.net/aniltj/us-digital-immigration-credentials-overview) (USCIS) 
  - [mDL](https://www.aamva.org/topics/mobile-driver-license#?wst=4a3b89462cc2cff2cbe0c7accde57421) (US AAMVA)  [not SSI standards conformant]
  - [IDCard](https://www.iata.org/en/services/travel-agency-program/idcard/) (IATA / Switzerland) 
- **Trust Registries & Directories**
  - [TRAIN](https://www.ngi.eu/blog/2022/07/28/verifying-identity-management-credentials-with-train/) (ToIP) 
  - [Regi-Trust](https://www.sparkblue.org/Regi-TRUST) (UNDP) 
  - [OrgBook BC](https://www.orgbook.gov.bc.ca/search) (BCGov) 
- [*SupplyChain/Trade*]({{site.baseurl}}/application/supply-chain/) 
  - [*GS1*]({{site.baseurl}}/web-standards/gs1/) 
  - [*GLEIF*]({{site.baseurl}}/organizations/gleif/) 
- **Banking**
  - [Bonifi](https://bonifii.com/) 
- [*COVID*]({{site.baseurl}}/application/covid-19/) 
  - [NYState](https://covid19vaccine.health.ny.gov/excelsior-pass-update) 
  - [VCI](https://vci.org/) 
  - [*CCI*]({{site.baseurl}}/application/covid-19/lfph_cci_good-health-pass/) 
  - DTCC
  - [DIVOC](https://divoc.digit.org/) 
- **Enterprise**
- [*Healthcare*]({{site.baseurl}}/application/healthcare/) 
- [*Learning/Career/Education*]({{site.baseurl}}/application/education/) 
  - [Jobs for the Future](https://jff.org) 
  - [Velocity Network](https://www.velocitynetwork.foundation/) 
  - [Learning Economy Foundation](https://www.learningeconomy.io/) 
  - [TLN - Trusted Learner Network](https://tln.asu.edu/) 
- **[KYC]({%link _posts/application/2023-06-15-kyc.md%})**
- **Real Estate**
  - [Rental](https://domilabs.io/) 
- [*Travel*]({{site.baseurl}}/application/travel/) 
- [*Humanitarian*]({{site.baseurl}}/application/humanitarian/) 
- **Energy**
- [*IoT*]({{site.baseurl}}/application/IOT/) 
- [*Guardianship*]({{site.baseurl}}/application/guardianship/) 
- [*Wallets*]({{site.baseurl}}//development/wallets/#ecosystem) 

## Types (by type+topic)

- [*Research* Papers/Academic Literature]({{site.baseurl}}/resources/literature/) 
  - [Turing Institute Research: Privacy & Trust](https://www.turing.ac.uk/research/research-areas/privacy-trust)
- **Events**
  - [*IIW*]({{site.baseurl}}/workshops/internet-identity-workshop/) 
  - [*RWoT*]({{site.baseurl}}/workshops/rebooting-web-of-trust/) 

## Topics 

- [*Biometrics*]({{site.baseurl}}/development/biometrics/) 
- [*Privacy*]({{site.baseurl}}/self-sovereign-identity/privacy/) 
- [*Human* Rights]({{site.baseurl}}/development/ethics-rights-sovereignty/) 
- [*User* Experience]({{site.baseurl}}/development/user-experience/) 
- [*Business*]({{site.baseurl}}/development/business/) 
- [*Critiques*]({{site.baseurl}}/self-sovereign-identity/critique-caution/) 
- [*Future*]({{site.baseurl}}/application/future/) 

## Web3, DWeb, & Other Tech (by focus)

- [*Web3*]({{site.baseurl}}/web-3/) 
  - [*Web3 and SSI*]({{site.baseurl}}/web-3/id/)  
  - [*DAO*]({{site.baseurl}}/web-3/dao/) 
  - [*Decentralization*]({{site.baseurl}}/development/decentralization/) 
  - [*Metaverse*]({{site.baseurl}}/web-3/metaverse/) 
  - [*NFT*]({{site.baseurl}}/web-3/nft/) 
  - [*SBT*]({{site.baseurl}}/web-3/nft/#soulbound-tokens) 
  - [*DeFi*]({{site.baseurl}}/web-3/defi/) 
- **Organizations**
  - [*Ethereum* Enterprise Alliance*]({{site.baseurl}}/web-3/ethereum/baseline/) 
  - [Fission](https://www.fissionlabs.com/) 
  - [Protocol Labs](https://protocol.ai/)
- **DWeb**
  - [*Secure* Suttlebutt]({{site.baseurl}}/decentralized-web/scuttlebot/) 
  - [Bluesky](https://bsky.app/)
  - [*Web5*]({{site.baseurl}}/projects/tbd/web5/) 
  - [*Handshake*]({{site.baseurl}}/decentralized-web/handshake/) 
- Blockchain Ecosystems
  - [*Bitcoin*]({{site.baseurl}}/blockchain/bitcoin/) 
  - [*Ethereum*]({{site.baseurl}}/blockchain/ethereum/) 
