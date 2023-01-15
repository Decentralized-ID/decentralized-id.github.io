# Trust Frameworks

## Contents

- 800-63-3
- DIACC

## Links

* [Digital Identity and Attributes Trust Framework](https://stateofidentity.libsyn.com/digital-identity-and-attributes-trust-framework) State of Identity

Do you trust technology and government to protect your data? On this week's State of Identity podcast, host, Cameron D'Ambrosi is joined by Gareth Narinesingh, Head of Digital Identity at HooYu to discuss the bridge between payments and identity wallets, the UK's next big push in adopting shared identity standards, and the foundation of decentralized identity verification across Web3 applications and the metaverse.
* [The Ukrainian War, PKI, and Censorship](https://www.windley.com/archives/2022/03/the_ukrainian_war_pki_and_censorship.shtml) Phil Windley

PKI has created a global trust framework for the web. But the war in Ukraine has shone a light on its weaknesses. Hierarchies are not good architectures for building robust, trustworthy, and stable digital systems.
* [Digital Caribou looks at the future trends impacting Digital Identity](https://medium.com/caribou-digital/diagnostic-trends-shaping-the-future-of-digital-identification-181724c40068)
  > 1. The state of the art in digital identification are trust frameworks that accommodate diverse technologies, systems and stakeholders
  > 2. Risks remain even within the most rigorous trust framework:
  > 3. Achieving inclusion requires addressing both technical and political dimensions
  > 4. Trust frameworks are complicated so getting governance right requires an ecosystems approach
  > 5. Building the future of digital identification means reckoning with an analogue past
* [Trust Frameworks](https://medium.com/mattr-global/learn-concepts-trust-frameworks-ad96a4427991)
  > Trust frameworks are a foundational component of the web of trust. A trust framework is a common set of best practice standards-based rules that ensure minimum requirements are met for security, privacy, identification management and interoperability through accreditation and governance. These operating rules provide a common framework for ecosystem participants, increasing trust between them.
* [The trust infrastructure of self-sovereign identity ecosystems](https://ssi-ambassador.medium.com/the-trust-infrastructure-of-self-sovereign-identity-ecosystems-551f46ed9e2c)
  > The trust infrastructure is concerned with the question of how and why the presented information can be trusted. It defines the rules for all stakeholders and enables legally binding relationships with the combination of governance frameworks, which are built on top of trust frameworks.
  > 
  > includes a section on the core components of identity architecture that includes a graphic [based on a post by Phil Windley](https://www.windley.com/archives/2020/09/the_architecture_of_identity_systems.shtml)
* [Battle of the Trust Frameworks with Tim Bouma & Darrell O’Donnell](https://northernblock.io/battle-of-the-trust-frameworks-with-tim-bouma-darrell-odonnell) Northern Block

1. Levels of Assurance (LOA): an introduction to LOAs as they relate to Digital Identity and why they’re an important part of the recipe in achieving digital trust. Tim and Darrell give us some practical examples of LOAs.
2. The Concept of Trust: how do we define trust at a high-level and how do we differentiate between technical and human trust? How can we build trust with credential issuers but also with credential holders?
3. The World of Trust Frameworks: what are trust frameworks and what are different types of frameworks being deployed in both the public and private sectors? How are organizations trying to monetize trust frameworks? What’s going right, and what’s going wrong with the way trust frameworks are being implemented?
4. The Importance of Open Source for Trust Creation: why is open source important for achieving digital sovereignty? Is open source the only way to improve transparency, flexibility and accountability?
* [Good Health Pass Ecosystem Trust Architecture: DIDs and X.509 Trust Registries with Ecosystem Governance Frameworks](https://iiw.idcommons.net/23F/_Good_Health_Pass_Ecosystem_Trust_Architecture:_DIDs_and_X.509_Trust_Registries_with_Ecosystem_Governance_Frameworks) by Drummond Reed, Scott Perry, Darrell O’Donnell

Governance, Trust Registry, Ecosystem, Transitive Trust, Architecture

Presentation Deck: [GHP Ecosystem Trust Architecture PDF](https://drive.google.com/file/d/1Hgh5JvrM7aUCmg5q6KIXzvpVIcgfhTjr/view?usp=sharing)

- Proposed Trust Interoperability (Global) for the Good Health Pass (GHP) Ecosystem
- Kaliya Young & Rebecca Distler - Working Group Co-Leads
- Trust in the system - focus for today’s discussion.
- Principles - [https://www.goodhealthpass.org/wp-content/uploads/2021/02/Good-Health-Pass-Collaborative-Principles-Paper.pdf](https://www.goodhealthpass.org/wp-content/uploads/2021/02/Good-Health-Pass-Collaborative-Principles-Paper.pdf)
- Blueprint Outline - [https://www.goodhealthpass.org/wp-content/uploads/2021/03/GHPC-Interoperability-Blueprint-Outline-v2.pdf](https://www.goodhealthpass.org/wp-content/uploads/2021/03/GHPC-Interoperability-Blueprint-Outline-v2.pdf)
- Global Problems inhibiting world travel. Many emerging instances of GHP related ecosystems. GHP establishing an umbrella for all GHP-compliant ecosystems.
- Relying on the ToIP Trust stack as an architectural blueprint
- Ecosystem Governance Framework is at the top of a governance and technical stack.
- Some specific Ecosystems need to accommodate x.509 certificate and VC constructs.
- ToIP Stack diagram is undergoing new changes - some new terminology being discussed at IIW.
- Governance and Trust Framework terms are being used as synonyms but we conveyed that Governance Frameworks are over arching of subject Trust Frameworks.
- GHP wll be a General Ecosystem Governance Framework. Overseeing Specific EGFs..
- 
    
    
    
- It is likely to have a GHP compliance but only on the lightweight tenets of interoperability.
- We are introducing a trust registry infrastructure that works with all GHP-compliant ecosystems.
- Issuers within an ecosystem will be included in a trust registry.
- Each Ecosystem must publish its governance framework and make its trust registry available
- All issuers need to be recognized by a governance framework and included in a trust registry
- The second principle is that each specific EGF will identify its trust registry with a DID and specify its trust registry service endpoint(s) in its associated DID document
- The third principle is that each VC issued under a specific EGF will identify its issuer with either:
- a DID
- a URI (for X.509 certificates)
- The final principle is that each VC issued under a specific EGF will identify its type with a type URI. That field will be using common semantics.
- With this architecture, all we need is a simple trust registry protocol to answer the question:
- Is this issuer
- authorized to issue this VC type
- under this specific EGF?
- GOOD - is a pass
- BETTER - may be purpose-limited (“trivial” example -

Links from chat:

- Bart Suichies to Everyone : the eidas demo is here: [https://essif.adaptivespace.io/](https://essif.adaptivespace.io/)

* [https://gitlab.grnet.gr/essif-lab/infrastructure/fraunhofer/deliverables](https://gitlab.grnet.gr/essif-lab/infrastructure/fraunhofer/deliverables) not sure if this an open repo

* [https://gitlab.grnet.gr/essif-lab/infrastructure/fraunhofer/deliverables/-/blob/master/api_documentation/train-atv-1.0.0-swagger.yaml](https://gitlab.grnet.gr/essif-lab/infrastructure/fraunhofer/deliverables/-/blob/master/api_documentation/train-atv-1.0.0-swagger.yaml)

* [https://gitlab.grnet.gr/essif-lab/infrastructure/fraunhofer/train_project_summary](https://gitlab.grnet.gr/essif-lab/infrastructure/fraunhofer/train_project_summary)

- Drummond Reed to Everyone : See the anti-coercion section of the original ToIP RFC: [https://github.com/hyperledger/aries-rfcs/blob/master/concepts/0289-toip-stack/README.md](https://github.com/hyperledger/aries-rfcs/blob/master/concepts/0289-toip-stack/README.md)
- Sterre den Breeijen to Everyone : [https://blockchain.tno.nl/blog/verify-the-verifier-anti-coercion-by-design/](https://blockchain.tno.nl/blog/verify-the-verifier-anti-coercion-by-design/) Blog on anti-coercion by my colleague Oskar van Deventer
- Bart Suichies to Everyone : @judith: [https://gitlab.grnet.gr/essif-lab/infrastructure/fraunhofer/train_project_summary](https://gitlab.grnet.gr/essif-lab/infrastructure/fraunhofer/train_project_summary)
- Darrell O'Donnell to Everyone : TRAIN - [https://essif-lab.eu/essif-train-by-fraunhofer-gesellschaft/](https://essif-lab.eu/essif-train-by-fraunhofer-gesellschaft/)
- Drummond Reed to Everyone : Bart, I am totally on board with the human-readable element for GHP. Happy to chat more with you about that. There is a lot of focus on that in the [Consistent User Experience drafting group](https://wiki.trustoverip.org/display/HOME/Consistent+User+Experience+Drafting+Group)
[Pan-Canadian Trust Framework](https://diacc.ca/wp-content/uploads/2016/08/PCTF-Overview-FINAL.pdf)
* [Towards a Better Digital Identity Trust Framework in Aotearoa](https://digitalidentity.nz/2022/09/21/towards-a-better-digital-identity-trust-framework-in-aotearoa/) Digital Identity NZ

It’s a great pleasure to share with you DINZ Reflections Report, a seminal piece of work that DINZ’s Digital Identity Trust Framework working group has developed over several months.
* [Trust Frameworks? Standards Matter](https://medium.com/@trbouma/trust-frameworks-standards-matter-47c946992f44) Tim Bouma
  > He points at the NIST documents about it [Developing Trust Frameworks to Support Identity Federations](https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8149.pdf) published in 2018. He also points at the Canadian government’s definition of standards.
  > 
  > “a document that provides a set of agreed-upon rules, guidelines or characteristics for activities or their results. Standards establish accepted practices, technical requirements, and terminologies for diverse fields.”  He goes on to highlight a lot of the work being done in Canada and where it all sits relative to being a standard - “In closing, there are lots of trust frameworks being developed today. But to be truly trusted, a trust framework needs to either apply existing standards or become a standard itself.”

* [Pan-Canadian Trust Framework (PCTF) – Overview](https://northernblock.io/pan-canadian-trust-framework/)

Right now, we are alpha testing the framework with different kinds of actors, both public and private, and with assessors. Through this process, we’re going to learn what may need to change, and what may not need to change. We’re going to get real knowledge there. I will say that what we’re seeing already, is that DIACC and our priorities are really driven by members.


* [Trinsic Basics: What Is a Trust Registry?](https://trinsic.id/trinsic-basics-what-is-a-trust-registry/) Trinsic

Trust registries also need to be interoperable. The [Trust Over IP Foundation](https://www.trustoverip.org/) has a [specification](https://github.com/trustoverip/tswg-trust-registry-tf) for an interoperable trust registry, and ours is the first implementation of this spec. Because of this, Trinsic’s Trust Registry Service is architected so that one ecosystem could reference or incorporate a trust registry from a separate ecosystem if needed.


## Trust Registries

* [Managing Trust and Reputation via Trust Registries](https://www.continuumloop.com/managing-trust-and-reputation-via-trust-registries/) Continuum Loop

The concept behind a Trust Registry is that a Wallet needs to know which decentralized identifiers (DIDs) to “trust” as a source of truth. At many levels, this “trust” translates to “authority” – knowing that somebody, centralized or decentralized, is responsible for maintaining a list of trusted DIDs.
