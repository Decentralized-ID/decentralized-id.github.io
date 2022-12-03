---
published: false
---

# Hyperledger umbrella

### DIDs Fabric and Decentralized Networking

* [DEON](https://www.hyperledger.org/blog/2020/11/05/deon-a-hyperledger-based-decentralized-off-grid-network) is a new Hyperledger project focused in off-line communication networks, independent of internet infrastructure. This could be used to enable networks of devices to communicate peer-to-peer (without the need to ‘phone home’ over the internet), inter-enterprise consortia networks, and enabling user-centric data sharing in a more secure and private fashion.
### Aries

* [GlobaliD releases new open source applications](https://medium.com/global-id/globalid-shares-ssi-code-at-the-internet-identity-workshop-446debec43e7)

They open source their open-sourced iOS and Android native Aries frameworks and donated them to the Hyperledger Aries project.

They also shared their Dynamic Governance API using GlobaliD Groups.
* [Add support for "did:indy" to Hyperledger Indy Node and Indy VDR](https://digital.gov.bc.ca/marketplace/opportunities/code-with-us/e3dd1605-cc1d-4c30-a9ee-245940bccd0d) </>Code With Us

Accpting Applications until 1/10 4:00 PM PST

The total funding for the challenge is $70,000CDN and is divided into 4 phases. The first 3 phases require the use of Python working on the [Indy Node](https://github.com/hyperledger/indy-node).

* [Blockchain Trilemma for Decentralized Identity: Learning from Hyperledger Indy](https://arxiv.org/pdf/2204.05784.pdf) Paul Dunphy, OneSpan, Cambridge, UK

The current credential verification process relies on transaction processing by a ledger with transaction processing bottlenecks, which may constrain the ideal of non-repudiation.

* [Tutorials](https://aries.js.org/guides/tutorials) Aries JavaScript Docs
  > First we’re going to create a holder Agent, this will be the Agent that receives the membership credential. During their life, the holder will collect many different verifiable credentials. Memberships, ID-cards, even purchasing records.
* [Why Are Governments Choosing Hyperledger?](https://northernblock.io/governments-are-choosing-aries-indy-ursa/) Northern Block
  > - Open Data Standards (W3C’s DID & VC Standards)
  > - Open Tech Standards (Hyperledger Aries, Indy, Ursa)
  > - Achieving W3C-Compliance on Aries and Indy

* [Building a Hyperledger Indy Network](https://iiw.idcommons.net/1H/_Building_a_Hyperledger_Indy_Network_-_Questions,_discussion,_etc.) - Questions, discussion, etc. by Lynn Bendixsen

Slides link: [https://docs.google.com/presentation/d/1sUG4297GiRcUdu4aqQnc0Op0LMhbwiqy9LIAINHfSFQ/edit#slide=id.p1](https://docs.google.com/presentation/d/1sUG4297GiRcUdu4aqQnc0Op0LMhbwiqy9LIAINHfSFQ/edit%23slide%3Did.p1)

Links to guides for creating your own Indy network:

High level:

* [https://github.com/trustoverip/utility-foundry-wg](https://github.com/trustoverip/utility-foundry-wg)

Technical details (implementation):

* [https://docs.google.com/document/d/1Tg4dAEtC78TxG9AsIby_CfpbeOicK_YMKznSQOvtIVU/edit](https://docs.google.com/document/d/1Tg4dAEtC78TxG9AsIby_CfpbeOicK_YMKznSQOvtIVU/edit)
* [Indicio launches blockchain-enabled network for identity](https://indicio.tech/blog/indicio-launches-blockchain-enabled-network-for-identity/)
  > “Our clients asked for a stable, fully-staffed network based on Hyperledger Indy— one that could provide the  Service Level Agreements their customers need for mission-critical workloads,” said Heather Dahl, CEO of Indicio. “Today, we are excited to announce that this MainNet is open for business.”
  > 
  > “This is the network we need to accelerate adoption of passwordless zero trust ecosystems for enterprise customers” said Mike Vesey, President of [IdRamp](https://idramp.com), a leader in decentralized identity and a Genesis Node Operator on the Network.
* [https://northernblock.io/products/ssi-enterprise-cloud/](https://northernblock.io/products/ssi-enterprise-cloud/). In this video, we will demonstrate how to create new Verifiable Credentials with custom schemas using the NB Orbit enterprise app. Once the credential schema is created and the attribute fields specified, the enterprise user can then publish a credential definition to whatever root of trust they are using, in our case a Hyperledger Indy network.

* [How to Create New Verifiable Credentials with Customizable Schemas](https://www.youtube.com/watch?v%3D3JR6_tQYhgk)
  > In this video, we will demonstrate how to create new Verifiable Credentials with custom schemas using the NB Orbit enterprise app. 
  > 
  > Once the credential schema is created and the attribute fields specified, the enterprise user can then publish a credential definition to whatever root of trust they are using, in our case a Hyperledger Indy network.
- [Anonymous Credential Part 1: Brief Overview and History](https://medium.com/finema/anonymous-credential-part-1-brief-overview-and-history-c6679034c914)
  > An anonymous credential (Anoncred), which is also known as an attribute-based credential (ABC), is a concept for a digital credential that provides a credential holder maximal privacy and an ability to selectively disclose their personal information.
- [Anonymous Credential Part 2: Selective Disclosure and CL Signature](https://medium.com/finema/anonymous-credential-part-2-selective-disclosure-and-cl-signature-b904a93a1565)
  > selective disclosure and an anonymous credential (Anoncred) relies on an efficient signature scheme that supports multiple messages with a single signature. One such signature scheme is known as CL signature that is named after its Jan Camenisch and Anna Lysyanskaya […] CL signature popularized Anoncreds, and it also served as a cryptographic building block in Identity Mixer (Idemix) and Hyperledger Indy projects.
* [Forbes “Blockchain 50” Shows Enterprise Blockchain’s Footprint and Impact, with Hyperledger Tech Leading The Pack](https://www.hyperledger.org/blog/2021/02/02/once-again-forbes-blockchain-50-shows-enterprise-blockchains-footprint-and-impact-with-hyperledger-technologies-leading-the-pack)
  > Declaring that blockchain has “gone mainstream,” Forbes today released its 2021 “Blockchain 50,” featuring companies that have at least $1 billion in revenues or are valued at $1 billion or more and “lead in employing distributed ledger technology.” And, once again, half of the companies on the list are using Hyperledger technology.* [Why Distributed Ledger Technology (DLT) for Identity?](https://www.hyperledger.org/blog/2021/04/21/why-distributed-ledger-technology-dlt-for-identity) Hyperledger
  > To understand why DLT is useful for identity, we need to go back to the basics—paper credentials, how that model has worked for 1000s of years, and how the use of DLTs with verifiable credentials allows us to transition the great parts—security and privacy—of that model to the digital age.
* [Panel: Start Simple to Scale Decentralized Identity](https://hgf2021.sched.com/event/j3ej%23new_tab) HGF2021 • Indicio

Liquid Avatar Technologies and Indicio.tech will share how together they are transitioning the current KABN ID solution to verifiable credentials by building the Liquid Avatar Verifiable Credentials Ecosystem utilizing Hyperledger Aries, Ursa, and Indy.

* [hyperledger-labs/business-partner-agent: The Business Partner Agent allows to manage and exchange master data between organizations](https://github.com/hyperledger-labs/business-partner-agent)

Join the discussion: [https://chat.hyperledger.org/channel/business-partner-agent](https://chat.hyperledger.org/channel/business-partner-agent)

There was some discussion about the way to present such a profile, especially the way it is currently implemented as an endpoint in the did document pointing to a https ressource (json-ld document served using normal https).

One alternative, to create a DIDcomm-based protocol for public profile was discussed and would be a good alternative at the cost of every client having to be able to speak DIDcomm.

* [https://github.com/hyperledger/aries-rfcs/blob/master/concepts/0430-machine-readable-governance-frameworks/README.md](https://github.com/hyperledger/aries-rfcs/blob/master/concepts/0430-machine-readable-governance-frameworks/README.md)

* [Setting up Mediator Agent in Ubuntu — (.Net Core service in Linux Box)](https://rangesh.medium.com/setting-up-mediator-agent-in-ubuntu-net-core-service-in-linux-box-b874bb409eed) Rangesh

In a Self Sovereign Environment supported by Hyperledger Indy / Aries agent framework, Mediator Agent is one of the essential components that acts as postman service between Issuer /Verifier Aries Agent and Mobile Agent.

* [Become a Node Operator](https://indicio.tech/blog/be-a-part-of-the-most-dynamic-network-community-in-decentralized-identity/) Indicio
  > we’ve seen a rapid rise in demand for robust, stable, and professionally maintained networks to support decentralized identity solutions. It’s not a surprise: decentralized identity’s moment has arrived. That’s why we’ve been hard at work creating Hyperledger Indy networks upon which developers all over the world are building, testing, and launching their solutions.
* [Hyperledger Ursa code review](https://www.hyperledger.org/hyperledger-ursa/2022/05/31/hyperledger-ursa-code-review) Hyperledger

Rooted in a “trust but verify” mindset, several Canadian public sector entities and [Interac](https://www.interac.ca/en/) (Canada’s interbank network) sponsored a project at the [Digital Identity Laboratory of Canada](https://idlab.org/) (IDLab) to perform a security and cryptography code review of Hyperledger Ursa  (full report is available [here](https://www.hyperledger.org/wp-content/uploads/2022/05/URSA-IDLab-Code-Review.pdf)).
* [Introducing Hyperledger Aries Framework JavaScript 0.2.0](https://www.hyperledger.org/blog/2022/07/06/introducing-hyperledger-aries-framework-javascript-0-2-0) Hyperledger

The new Hyperledger Aries Framework JavaScript release (0.2.0) contains some incredible steps forward. Especially in our goal to make the framework AIP 2.0 compliant. AIP 2.0 compliance will not only ensure the framework supports the latest standards and protocols, but it will also greatly increase interoperability and make it more useful outside of the Hyperledger Indy ecosystem.
* [Hyperledger Aries Graduates To Active Status; Joins Indy As “Production Ready”](https://www.hyperledger.org/blog/2021/02/26/hyperledger-aries-graduates-to-active-status-joins-indy-as-production-ready-hyperledger-projects-for-decentralized-identity)

“This approval is further evidence that Hyperledger Aries is a breakout success for the Hyperledger community,” said Brian Behlendorf, General Manager for Blockchain, Healthcare and Identity at the Linux Foundation. “Convergence on common libraries for the exchange of credentials will help speed the development of urgently-needed solutions and systems, ranging from education to finance to the fight against the pandemic. Aries is key to that convergence.”
* [Hyperledger Aries Graduates To Active Status](https://www.hyperledger.org/blog/2021/02/26/hyperledger-aries-graduates-to-active-status-joins-indy-as-production-ready-hyperledger-projects-for-decentralized-identity)

The TSC commended the Aries project during the meeting for the project’s highly diverse contributors. Achieving a high number of organizations contributing to a project at Hyperledger is often a challenge. Congratulations are due to those participating in and supporting the Aries Project.

* [The Pathway to Becoming a Hyperledger Maintainer](https://www.hyperledger.org/blog/2021/11/03/the-pathway-to-becoming-a-hyperledger-maintainer)
  > In this blogpost I’m going to share what it’s like to be a maintainer for the Hyperledger Aries project. You’ll learn how you can start contributing and maybe even set yourself on a path to becoming a maintainer.
* [Indicio Wins British Columbia Code With Us Challenge to Upgrade Hyperledger Indy](https://indicio.tech/indicio-wins-british-columbia-code-with-us-challenge-to-upgrade-hyperledger-indy/)
  > Most of Hyperledger Indy’s development occurred prior to the completion of the standard DID Specification by the W3C and, as a result, identifiers written to one network are currently not resolvable on other networks. A new did:indy DID Method will fix that and make it easier for decentralized identity products and services to interoperate across different Indy networks.
* [Hyperledger SSI Ecosystem](https://dev.to/jakubkoci/hyperledger-ssi-ecosystem-4j2p) Jakubkoci

There are three projects under the Hyperledger umbrella related to digital identity. Hyperledger Indy, Aries, and Ursa. [...] describe their purpose and how they’re related to each other.

## Aries \ Indy \ AnonCreds the dialogue continues

* [Learnings from Aries, Indy and Various Verifiable Credential Implementations](https://northernblock.io/learnings-from-aries-indy-and-various-verifiable-credential-implementations/) Northern Block

Standards such as OIDC and mDL are all now in dialogue with W3C, AnonCreds, Aries, etc. Mobile is a predominant technology, just like the way laptops were once upon a time. To reduce consumer friction and drive adoption, convergence of all these different technologies is required inside a mobile environment


* [Indicio completes Hyperledger Indy DID Method—A Milestone in the Evolution of DID Interop](https://indicio.tech/indicio-completes-hyperledger-indy-did-method-a-milestone-in-the-evolution-of-decentralized-identity-network-interoperability/)

The Indy DID Method paves the way for Hyperledger Indy credentials to scale globally by allowing Indy networks to seamlessly interoperate and create a “network-of-networks” effect.


* [Our Approach to Resources on-ledger](https://blog.cheqd.io/our-approach-to-resources-on-ledger-25bf5690c975): Using the capabilities of the DID Core specification for standards-compliant resource lookup

Decentralised Identifiers (DIDs): are often stored on ledgers (e.g., [cheqd](https://github.com/cheqd/node-docs/blob/adr-008-resources-updates/architecture/adr-list/adr-002-cheqd-did-method.md), [Hyperledger Indy](https://hyperledger.github.io/indy-did-method/), distributed storage (e.g., [IPFS](https://ipfs.io/) in [Sidetree](https://identity.foundation/sidetree/spec/)), or non-ledger distributed systems (e.g., [KERI](https://keri.one/)). Yet, DIDs can be stored on traditional centralised-storage endpoints (e.g., [did:web](https://w3c-ccg.github.io/did-method-web/), [did:git](https://github-did.com/)).

* [Hyperledger Aries is the Present and the Future of Internet-Scale Trusted Verifiable Credential Ecosystems](https://indicio.tech/hyperledger-aries-is-the-present-and-the-future-of-internet-scale-trusted-verifiable-credential-ecosystems/) Indicio

While no technology runs perfectly on every device, a signal strength of Aries, AnonCreds, and Indy is that they work on the vast majority of current devices and systems, including $35 smart phones and low powered IOT/embedded devices. They represent the most inclusive way into this technology, which is an important factor in their popularity.

* [AnonCreds Indy-Pendence](https://blog.cheqd.io/anoncreds-indy-pendence-4946367469d4) Cheqd

Part 1: Decoupling the reliance on Hyperledger Indy and creating more extensible AnonCreds Objects with cheqd.



* [Investing in Verifiable Credentials, Technical Interoperability and Open Source](https://www.hyperledger.org/blog/2022/08/23/investing-in-verifiable-credentials-technical-interoperability-and-open-source) Hyperledger

As our approach evolves, we also remain keen to support open source solutions that interoperate with other national and international efforts. There is no dominant design yet, no one network or technology, so we must remain nimble and flexible in our exploration. We also need to coexist with existing identity solutions that millions of British Columbians already rely upon.


* [IDunion Introduction and AMA (there will be another one tomorrow!)](https://iiw.idcommons.net/12D/_IDunion_Introduction_and_AMA_(there_will_be_another_one_tomorrow!)) by Andre Kudra + available IDunion crew!

* [IDunion](https://idunion.org/?lang%3Den) enables self-determined identities based on Self-Sovereign Identity (SSI) technologies Hyperledger Indy and Hyperledger Aries. The aim of the IDunion organisation is to create an open ecosystem for decentralised identity management, which can be used  worldwide and is based on European values and regulations. IDunion is also a [project](https://www.digitale-technologien.de/DT/Redaktion/DE/Standardartikel/SchaufensterSichereDigIdentProjekte/Schaufensterprojekte/sdi-projekt_idunion.html) co-funded by the [German Federal Ministry of Economic Affairs (BMWi)](https://www.bmwi.de/Navigation/EN/Home/home.html) as part of the [Showcases Secure Digital Identities program](https://www.digitale-technologien.de/DT/Navigation/DE/ProgrammeProjekte/AktuelleTechnologieprogramme/Sichere_Digitale_Identitaeten/sichere_digitale_ident.html). We gave an introduction covering

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

DEMO:  [https://www.youtube.com/watch?v=09-LOHPTHWs](https://www.youtube.com/watch?v%3D09-LOHPTHWs)

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
* [Hyperledger Mentorship Spotlight: Hyperledger Aries Integration to Support Fabric as Blockchain Ledger](https://www.hyperledger.org/blog/2021/12/06/hyperledger-mentorship-spotlight-hyperledger-aries-integration-to-support-fabric-as-blockchain-ledger)

The Hyperledger Mentorship Program is a structured hands-on learning opportunity for new developers who may otherwise lack the opportunity to gain exposure to Hyperledger open source development and entry to the technical community.

* [Hyperledger KochiOrgBook Meetup](https://www.youtube.com/watch?v=HU0zXKiFYD0) (modeled after [VONx.io](https://vonx.io/)), in collaboration with Wipro, CUSAT, and KBA.
  > “KochiOrgBook is a Verifiable Organization Network for the city of Kochi [India]. It is a technology demonstrator to launch a DID based utility compliant with the ToIP standards to enable trusted digital verification for various associations within the city of Kochi.”

* [Getting Internet Identity Right 30 Years On](https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2NvaW5kZXNrLXJlcG9ydHM/episode/Z2lkOi8vYXJ0MTktZXBpc29kZS1sb2NhdG9yL1YwL1B2ZTZ1WThCazZjM24zckdUVVdaQ2YyWGJwQnNuWTBra3N0WWlFOFhBNUk?ep=14) Money ReImagined with Brian Behlendorf.
  > Michael Casey and Sheila Warren talk to Hyperledger Executive Director Brian Behlendorf about self-sovereign identity, the topic of this week's column. A developer whose three-decade career has seen him deeply involved in efforts to foster a more open internet, Brian grasps, like few others, the nuances of how human beings should live within a rapidly changing digital economy.
* [Hyperledger completes development of DID:Indy Method and advances toward a network of networks](https://www.hyperledger.org/blog/2022/05/02/hyperledger-identity-community-completes-development-of-didindy-method-and-advances-toward-a-network-of-networks) Howland & Bluhm - Linux Foundation

With the groundwork complete, networks and agent frameworks now need to incorporate the Indy:DID Method. This community adoption will increase the viability of the Indy and Aries project stack and position it to be the globally dominant way to issue and share verifiable credentials in a multi-ledger world.

* [EU Grant to Help Building Blockchain Infrastructure](https://sphereon.com/news-and-insights/sphereon-wins-an-eu-essif-lab-grant/). Sphereon
  > We’ll be providing a Presentation Exchange that creates interoperability between W3C DIF-compliant Verifiable Credentials and Hyperledger Aries-based Verifiable Credentials for the European Blockchain Services Infrastructure (EBSI).

* [Talking on Aries Bifold, building a community effort around an open source mobile wallet in React Native](https://iiw.idcommons.net/23I/_Talking_on_Aries_Bifold,_building_a_community_effort_around_an_open_source_mobile_wallet_in_React_Native) by James Ebert

Hyperledger Aries – Aries Bifold – Aries-Framework-Javascript – React Native

Slides: [https://docs.google.com/presentation/d/1XKrgnUUF7nZI-bOqWMKijKZHWThsIjFkVkfPIVy3gkY/edit?usp=sharing](https://docs.google.com/presentation/d/1XKrgnUUF7nZI-bOqWMKijKZHWThsIjFkVkfPIVy3gkY/edit?usp%3Dsharing)

Repo: [https://github.com/hyperledger/aries-mobile-agent-react-native](https://github.com/hyperledger/aries-mobile-agent-react-native)

User Group Meetings: [https://wiki.hyperledger.org/display/ARIES/Aries+Bifold+User+Group+Meetings](https://wiki.hyperledger.org/display/ARIES/Aries%2BBifold%2BUser%2BGroup%2BMeetings)

Rocketchat: [https://chat.hyperledger.org/channel/aries-bifold](https://chat.hyperledger.org/channel/aries-bifold)

Aries-Framework-Javascript: [https://github.com/hyperledger/aries-framework-javascript](https://github.com/hyperledger/aries-framework-javascript)

rn-indy-sdk: [https://github.com/AbsaOSS/rn-indy-sdk](https://github.com/AbsaOSS/rn-indy-sdk)

Discussion on the following topics:

- Face recognition capabilities and discussion
- Discussion of project goals
- Brief demo of current state
- Questions on Ionic vs React Native
- React Native is more broadly adopted
- Need to start somewhere
- Does Aries Bifold plan to support BBS+? Yes, planning on utilizing Aries Askar and surrounding components to enable these capabilities.
- What is the MVP of Aries Bifold?
- Connections
- Coordinate-mediation protocol support
- Credential Exchange
- Revocation
- Aries Bifold interoperability
- AIP 1.0 and AIP 2.0 support
- Aries Agent Test Harness capabilities
- Componentization of Aries Bifold
- Allows the inclusion of the project in existing apps.
- Helps with separation of concerns.
- Use of React Redux
- Packaging and monorepos.

* [...]

Karim Stekelenburg: [https://github.com/microsoft/react-native-tscodegen](https://github.com/microsoft/react-native-tscodegen)

* [SITA uses blockchain, decentralized identity for pilot license verification](https://www.ledgerinsights.com/sita-blockchain-decentralized-identity-for-pilot-license/) Ledgerinsights

Using the [self-sovereign identity](https://www.ledgerinsights.com/tag/self-sovereign-identity/) solution Hyperledger Aries, almost everything works peer to peer between the license issuer and the pilot and between the pilot and the verifier.

* [An automatized Identity and Access Management system for IoT combining SSI and smart contracts](https://arxiv.org/pdf/2201.00231.pdf) Montassar Naghmouchi, Hella Kaffel, and Maryline Laurent

This paper proposes a blockchain-based identity and access management system for IoT – specifically smart vehicles- as an example of use-case, showing two interoperable blockchains, Ethereum and Hyperledger Indy, and a self-sovereign * [Hyperledger Identity Screencast: Social Recovery for Passwords and Secrets](https://www.youtube.com/watch?v%3D1c05mFuEQ5s)

A demonstration of using social recovery for things like recovery passwords of self-sovereign identity digital wallets. The website [http://passguardian.com](https://www.youtube.com/redirect?event%3Dvideo_description%26redir_token%3DQUFFLUhqbnFXWC1vZEVSZS11Ynl1ZGpBRk1uMUN6VnhnUXxBQ3Jtc0tuRjRPbmFSOEVqU1FNSEJDMml0WXYzUjlmRUdyZk5lVWJSc2p1QnFHV0pMZzNfVlBpNVJ0UGZvY2pEVUlzTFA1LWJlQUU0Q190akpyQndJWmU3bDZranNJVUZxZi1JX2pJb2I1SEtpRXB0cjhCQWNNdw%26q%3Dhttp%253A%252F%252Fpassguardian.com)​ is used to show how a secret can be encoded and distributed as shards, and then later some of the shards combined to restore the secret. This video is part of a [Linux Foundation course on Hyperledger Identity](https://training.linuxfoundation.org/training/introduction-to-hyperledger-sovereign-identity-blockchain-solutions-indy-aries-and-ursa/), published on edX.
identity model.
* [Technical Design and Development of a Self-Sovereign Identity Management Platform for Patient-Centric Healthcare Using Blockchain Technology](https://blockchainhealthcaretoday.com/index.php/journal/article/view/196%23.Yjkahet3YEM.twitter) Blockchain Healthcare Today

To manage patient’s self-sovereign identity, we leveraged the Hyperledger Indy blockchain framework to store patient’s decentralized identifiers (DIDs) and the schemas or format for each credential type. In contrast, the credentials containing patient data are stored “off-ledger” in each person’s wallet and accessible via a computer or smartphone. We used Hyperledger Aries as a middleware layer (API) to connect Hyperledger Indy with the front-end, which was developed using a JavaScript framework, ReactJS (Web Application) and React Native (iOS Application).
