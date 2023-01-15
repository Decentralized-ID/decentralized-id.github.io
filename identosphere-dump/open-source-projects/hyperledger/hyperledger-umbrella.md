---
published: false
---

# Hyperledger umbrella

### DIDs Fabric and Decentralized Networking

* [DEON](https://www.hyperledger.org/blog/2020/11/05/deon-a-hyperledger-based-decentralized-off-grid-network) is a new Hyperledger project focused in off-line communication networks, independent of internet infrastructure. This could be used to enable networks of devices to communicate peer-to-peer (without the need to ‘phone home’ over the internet), inter-enterprise consortia networks, and enabling user-centric data sharing in a more secure and private fashion.

* [Add support for "did:indy" to Hyperledger Indy Node and Indy VDR](https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/e3dd1605-cc1d-4c30-a9ee-245940bccd0d) </>Code With Us

Accpting Applications until 1/10 4:00 PM PST

The total funding for the challenge is $70,000CDN and is divided into 4 phases. The first 3 phases require the use of Python working on the [Indy Node](https://github.com/hyperledger/indy-node).

* [Blockchain Trilemma for Decentralized Identity: Learning from Hyperledger Indy](https://arxiv.org/pdf/2204.05784.pdf) Paul Dunphy, OneSpan, Cambridge, UK

The current credential verification process relies on transaction processing by a ledger with transaction processing bottlenecks, which may constrain the ideal of non-repudiation.



* [GlobaliD releases new open source applications](https://medium.com/global-id/globalid-shares-ssi-code-at-the-internet-identity-workshop-446debec43e7)
  > They open source their open-sourced iOS and Android native Aries frameworks and donated them to the Hyperledger Aries project.
  > 
  > They also shared their Dynamic Governance API using GlobaliD Groups.
* [Tutorials](https://aries.js.org/guides/tutorials) Aries JavaScript Docs
  > First we’re going to create a holder Agent, this will be the Agent that receives the membership credential. During their life, the holder will collect many different verifiable credentials. Memberships, ID-cards, even purchasing records.
* [Why Are Governments Choosing Hyperledger?](https://northernblock.io/governments-are-choosing-aries-indy-ursa/) Northern Block
  > - Open Data Standards (W3C’s DID & VC Standards)
  > - Open Tech Standards (Hyperledger Aries, Indy, Ursa)
  > - Achieving W3C-Compliance on Aries and Indy

* [Building a Hyperledger Indy Network](https://iiw.idcommons.net/1H/_Building_a_Hyperledger_Indy_Network_-_Questions,_discussion,_etc.) - Questions, discussion, etc. by Lynn Bendixsen

Slides link: [https://docs.google.com/presentation/d/1sUG4297GiRcUdu4aqQnc0Op0LMhbwiqy9LIAINHfSFQ/edit#slide=id.p1](https://docs.google.com/presentation/d/1sUG4297GiRcUdu4aqQnc0Op0LMhbwiqy9LIAINHfSFQ/edit#slide=id.p1)

Links to guides for creating your own Indy network:

High level:

* [https://github.com/trustoverip/utility-foundry-wg](https://github.com/trustoverip/utility-foundry-wg)

Technical details (implementation):

* [https://docs.google.com/document/d/1Tg4dAEtC78TxG9AsIby_CfpbeOicK_YMKznSQOvtIVU/edit](https://docs.google.com/document/d/1Tg4dAEtC78TxG9AsIby_CfpbeOicK_YMKznSQOvtIVU/edit)
* [https://northernblock.io/products/ssi-enterprise-cloud/](https://northernblock.io/products/ssi-enterprise-cloud/). In this video, we will demonstrate how to create new Verifiable Credentials with custom schemas using the NB Orbit enterprise app. Once the credential schema is created and the attribute fields specified, the enterprise user can then publish a credential definition to whatever root of trust they are using, in our case a Hyperledger Indy network.

* [How to Create New Verifiable Credentials with Customizable Schemas](https://www.youtube.com/watch?v=3JR6_tQYhgk)
  > In this video, we will demonstrate how to create new Verifiable Credentials with custom schemas using the NB Orbit enterprise app. 
  > 
  > Once the credential schema is created and the attribute fields specified, the enterprise user can then publish a credential definition to whatever root of trust they are using, in our case a Hyperledger Indy network.

* [Forbes “Blockchain 50” Shows Enterprise Blockchain’s Footprint and Impact, with Hyperledger Tech Leading The Pack](https://www.hyperledger.org/blog/2021/02/02/once-again-forbes-blockchain-50-shows-enterprise-blockchains-footprint-and-impact-with-hyperledger-technologies-leading-the-pack)
  > Declaring that blockchain has “gone mainstream,” Forbes today released its 2021 “Blockchain 50,” featuring companies that have at least $1 billion in revenues or are valued at $1 billion or more and “lead in employing distributed ledger technology.” And, once again, half of the companies on the list are using Hyperledger technology.* [Why Distributed Ledger Technology (DLT) for Identity?](https://www.hyperledger.org/blog/2021/04/21/why-distributed-ledger-technology-dlt-for-identity) Hyperledger
  > To understand why DLT is useful for identity, we need to go back to the basics—paper credentials, how that model has worked for 1000s of years, and how the use of DLTs with verifiable credentials allows us to transition the great parts—security and privacy—of that model to the digital age.



* [hyperledger-labs/business-partner-agent: The Business Partner Agent allows to manage and exchange master data between organizations](https://github.com/hyperledger-labs/business-partner-agent)

Join the discussion: [https://chat.hyperledger.org/channel/business-partner-agent](https://chat.hyperledger.org/channel/business-partner-agent)

There was some discussion about the way to present such a profile, especially the way it is currently implemented as an endpoint in the did document pointing to a https ressource (json-ld document served using normal https).

One alternative, to create a DIDcomm-based protocol for public profile was discussed and would be a good alternative at the cost of every client having to be able to speak DIDcomm.









* [Investing in Verifiable Credentials, Technical Interoperability and Open Source](https://www.hyperledger.org/blog/2022/08/23/investing-in-verifiable-credentials-technical-interoperability-and-open-source) Hyperledger

As our approach evolves, we also remain keen to support open source solutions that interoperate with other national and international efforts. There is no dominant design yet, no one network or technology, so we must remain nimble and flexible in our exploration. We also need to coexist with existing identity solutions that millions of British Columbians already rely upon.


* [IDunion Introduction and AMA (there will be another one tomorrow!)](https://iiw.idcommons.net/12D/_IDunion_Introduction_and_AMA_(there_will_be_another_one_tomorrow!)) by Andre Kudra + available IDunion crew!

* [IDunion](https://idunion.org/?lang=en) enables self-determined identities based on Self-Sovereign Identity (SSI) technologies Hyperledger Indy and Hyperledger Aries. The aim of the IDunion organisation is to create an open ecosystem for decentralised identity management, which can be used  worldwide and is based on European values and regulations. IDunion is also a [project](https://www.digitale-technologien.de/DT/Redaktion/DE/Standardartikel/SchaufensterSichereDigIdentProjekte/Schaufensterprojekte/sdi-projekt_idunion.html) co-funded by the [German Federal Ministry of Economic Affairs (BMWi)](https://www.bmwi.de/Navigation/EN/Home/home.html) as part of the [Showcases Secure Digital Identities program](https://www.digitale-technologien.de/DT/Navigation/DE/ProgrammeProjekte/AktuelleTechnologieprogramme/Sichere_Digitale_Identitaeten/sichere_digitale_ident.html). We gave an introduction covering

- The IDunion consortium consists of 37 partners - other major partners have already signaled interest in participating
- Our solution is enabled by the distributed ledger technology (DLT) and the concept of self-sovereign identities (SSI)
- Instead of a central authority, trust is organized via a DLT network, which works as a decentralized PKI system
- In recent months, in addition to intensive research, we have developed a DLT test network including governance structure, 35+ use cases and numerous software components for the allocation, verification and management of digital identity data developed
- In the future, the identity network will be managed by a European cooperative in which every institution in the EU can participate
- In total, we are working on 35 use cases in the areas of eGovernment, education, finance, industry/IOT, eCommerce/mobility, IAM, and eHealth

* [IDunion Introduction and AMA (same as on day 2!)](https://iiw.idcommons.net/24D/_IDunion_Introduction_and_AMA_(same_as_on_day_2!)) by Andre Kudra + available IDunion crew!

IDunion | SSI | Identity | Consortium | Cooperative | Germany | Europe | BWMi

Discussion notes, key understandings, outstanding questions, observations, and, if appropriate to this discussion: action items, next steps:

* [BC Gov Collaboration on the Business Partner Agent, sharing our Roadmap (Create Creds, Issue them, Verify them, Hold them, publish them, ZKPs, Selective Disclosure)](https://iiw.idcommons.net/24A/_BC_Gov_Collaboration_on_the_Business_Partner_Agent,_sharing_our_Roadmap-Create_Creds,_Issue_them,_Verify_them,_Hold_them,_publish_them,_ZKPs,_Selective_Disclosure-) by Matthew Hall + Available Collaborators

Business partner agent, credential management, issuers, verifiers, holders, digital wallet

Practical session, what we are actually building today using the hyper ledger Aries tools

Some interesting points

- Viewing organizations as Issuers, Verifiers and Holders
- Talked about the complexity of defining a verifiable credential, I.e. what are you attesting to?
- Went over the need to make it easier for users to be able to create credential schemas and credential definitions without having to gain understanding about the tech.
- Question was asked about where do we start, do we have to bootstrap the first credential? And we went over being able to start with existing governance structures, and the trust that is already accepted there to issue the first credentials.
- I gave a demo of our prototype that shows three actors (Mine, Bank, Verifier) doing a credential exchange flow between them

Links:

DEMO:  [https://www.youtube.com/watch?v=09-LOHPTHWs](https://www.youtube.com/watch?v=09-LOHPTHWs)

Connect with Us: [https://chat.hyperledger.org/channel/business-partner-agent](https://chat.hyperledger.org/channel/business-partner-agent)

Repo: [https://github.com/hyperledger-labs/business-partner-agent/projects/1](https://github.com/hyperledger-labs/business-partner-agent/projects/1)

* [Hyperledger Forum Recap – Identity Proofing, and Passwordless User-friendly Digital Identity](https://idramp.com/hyperledger-forum-recap-identity-proofing-and-passwordless-user-friendly-digital-identity/)

IdRamp presented with Oracle at [Hyperledger Global Forum](https://events.linuxfoundation.org/hyperledger-global-forum/) June 2021. The event focused on enterprise use of blockchain technologies using the 15 projects that fall under the Hyperledger “greenhouse”. Keynotes and speakers shared their insights on the current state of enterprise blockchain adoption across several hot topics including central bank digital currencies (CBDCs), non fungible tokens (NFTs), and most importantly– identity.

* [Anonyome Labs Joins the Indicio MainNet](https://anonyome.com/2021/05/anonyome-labs-joins-the-indicio-mainnet/)

Here, we go through how we went about standing up our Indico node. In brief:

- The Indicio MainNet is an enterprise-grade ledger for use by decentralized identity applications.
- We brought up the node using AWS Elastic Cloud Computing (EC2) instances within a Virtual Private Cloud (VPC).
- We pulled the validator algorithms from the open-source project, [Hyperledger Indy](https://www.hyperledger.org/use/hyperledger-indy).
- A supporting machine operates the command line interface used to perform steward operations onthe ledger.
- We used security groups at the network interface level to create a firewall.
- We set up monitoring in AWS CloudWatch using a variety of bash scripting in conjunction with Ubuntu and AWS provided utilities.
- We created a regular maintenance schedule.



* [Getting Internet Identity Right 30 Years On](https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2NvaW5kZXNrLXJlcG9ydHM/episode/Z2lkOi8vYXJ0MTktZXBpc29kZS1sb2NhdG9yL1YwL1B2ZTZ1WThCazZjM24zckdUVVdaQ2YyWGJwQnNuWTBra3N0WWlFOFhBNUk?ep=14) Money ReImagined with Brian Behlendorf.
  > Michael Casey and Sheila Warren talk to Hyperledger Executive Director Brian Behlendorf about self-sovereign identity, the topic of this week's column. A developer whose three-decade career has seen him deeply involved in efforts to foster a more open internet, Brian grasps, like few others, the nuances of how human beings should live within a rapidly changing digital economy.
* [Hyperledger completes development of DID:Indy Method and advances toward a network of networks](https://www.hyperledger.org/blog/2022/05/02/hyperledger-identity-community-completes-development-of-didindy-method-and-advances-toward-a-network-of-networks) Howland & Bluhm - Linux Foundation

With the groundwork complete, networks and agent frameworks now need to incorporate the Indy:DID Method. This community adoption will increase the viability of the Indy and Aries project stack and position it to be the globally dominant way to issue and share verifiable credentials in a multi-ledger world.


* [An automatized Identity and Access Management system for IoT combining SSI and smart contracts](https://arxiv.org/pdf/2201.00231.pdf) Montassar Naghmouchi, Hella Kaffel, and Maryline Laurent

This paper proposes a blockchain-based identity and access management system for IoT – specifically smart vehicles- as an example of use-case, showing two interoperable blockchains, Ethereum and Hyperledger Indy, and a self-sovereign * [Hyperledger Identity Screencast: Social Recovery for Passwords and Secrets](https://www.youtube.com/watch?v=1c05mFuEQ5s)

A demonstration of using social recovery for things like recovery passwords of self-sovereign identity digital wallets. The website [http://passguardian.com](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnFXWC1vZEVSZS11Ynl1ZGpBRk1uMUN6VnhnUXxBQ3Jtc0tuRjRPbmFSOEVqU1FNSEJDMml0WXYzUjlmRUdyZk5lVWJSc2p1QnFHV0pMZzNfVlBpNVJ0UGZvY2pEVUlzTFA1LWJlQUU0Q190akpyQndJWmU3bDZranNJVUZxZi1JX2pJb2I1SEtpRXB0cjhCQWNNdw&q=http%3A//passguardian.com)​ is used to show how a secret can be encoded and distributed as shards, and then later some of the shards combined to restore the secret. This video is part of a [Linux Foundation course on Hyperledger Identity](https://training.linuxfoundation.org/training/introduction-to-hyperledger-sovereign-identity-blockchain-solutions-indy-aries-and-ursa/), published on edX.
identity model.
* [Technical Design and Development of a Self-Sovereign Identity Management Platform for Patient-Centric Healthcare Using Blockchain Technology](https://blockchainhealthcaretoday.com/index.php/journal/article/view/196#.Yjkahet3YEM.twitter) Blockchain Healthcare Today

To manage patient’s self-sovereign identity, we leveraged the Hyperledger Indy blockchain framework to store patient’s decentralized identifiers (DIDs) and the schemas or format for each credential type. In contrast, the credentials containing patient data are stored “off-ledger” in each person’s wallet and accessible via a computer or smartphone. We used Hyperledger Aries as a middleware layer (API) to connect Hyperledger Indy with the front-end, which was developed using a JavaScript framework, ReactJS (Web Application) and React Native (iOS Application).
