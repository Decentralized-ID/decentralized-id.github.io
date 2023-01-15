---
published: false
---

# Standards

* [FYI: What makes a standard ‘world class’?](https://lists.w3.org/Archives/Public/public-credentials/2021Aug/0213.html) Michael Herman (Trusted Digital Web) (Saturday, 14 August)
  > - A world class standard should have well-defined objectives that respond to real needs in a timely manner.
  > - Its technical content should be complete and accurate.
  > - It should be easy to understand (or as easy as the subject matter allows!) and easy to implement.
  > - Its requirements should be expressed clearly and unambiguously.
  > - It should be validated.
  > - It should be well-maintained.
  > 
  > Reference: [A Guide To Writing World Class Standards](https://www.etsi.org/images/files/Brochures/AGuideToWritingWorldClassStandards.pdf)
* [Trust Frameworks? Standards Matter](https://medium.com/@trbouma/trust-frameworks-standards-matter-47c946992f44) Tim Bouma
  > He points at the NIST documents about it [Developing Trust Frameworks to Support Identity Federations](https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8149.pdf) published in 2018. He also points at the Canadian government’s definition of standards.
  > 
  > “a document that provides a set of agreed-upon rules, guidelines or characteristics for activities or their results. Standards establish accepted practices, technical requirements, and terminologies for diverse fields.”  He goes on to highlight a lot of the work being done in Canada and where it all sits relative to being a standard - “In closing, there are lots of trust frameworks being developed today. But to be truly trusted, a trust framework needs to either apply existing standards or become a standard itself.”
* [Open standards should be developed openly](https://blog.weareopen.coop/open-standards-should-be-developed-openly-1f0cf552308d) WeAreOpen
  > Open standards should be developed openly because not enough people work to ensure that equity is central to innovation and development. We believe that openness is an attitude, and one which bears fruit over time from which everyone can benefit.

* [Global Standards Mapping Initiative](https://www.continuumloop.com/global-standards-mapping-initiative/) ContinuumLoop

This past November, the GBBC released [The Global Standards Mapping Initiative 2.0](https://gbbcouncil.org/wp-content/uploads/2021/11/GBBC-GSMI-2.0-Report-1.pdf), updating the [standards published in 2020](https://gbbcouncil.org/wp-content/uploads/2020/10/GSMI-Legal-Regulatory-Report.pdf). The GBBC is a strong proponent of standardization and intends to serve as a baseline for establishing frameworks and standards that will allow for adoption and innovation.
* [Premature Standardization & Interoperability](https://www.continuumloop.com/premature-standardization-interoperability/) Continuum Loop

Here’s my premise – we don’t have standards nor interoperability – at least not as people really need. We have been through a process that is powerful and good – but what we have is what I call “premature standardization.” It’s a great start but nowhere near where things will be.

* [Trinsic Basics: What Are SSI Standards?](https://trinsic.id/what-are-ssi-standards/)
  > There are two kinds of standards that Trinsic implements to enable interoperability and avoid vendor lock-in: data model standards and protocol standards.

* [Manifesto: Rules for standards-makers](http://scripting.com/2017/05/09/rulesForStandardsmakers.html)
  > I've used all kinds of formats and protocols in a long career as a software developer, even created a few. My new manifesto summarizes what I've learned about what works and what doesn't.


* [Linked Data Security](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0134.html) ([slide deck](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/att-0134/2021-Linked-Data-Security.pdf)
  > The attached slide deck provides a basic overview (with examples) of Linked Data Security as well as the specifications in that orbit. The W3C CCG is  actively developing a number of these specifications.
* [Roadmap: Verifiable Trust Standards](https://lists.w3.org/Archives/Public/public-credentials/2021Mar/0014.html)
  > Green - General data format standards
  > Yellow - Vocabulary standards (I the mislabeled VC work)
  > Magenta - Protocol standards (I mislabeled DID Resolution)
  > Red - Low-level cryptographic primitives
  > Purple - General crypto packaging/protocol standards
  > Orange - Application layer standards



### OMG
* [OMG ISSUES RFI FOR DISPOSABLE SELF-SOVEREIGN IDENTITY STANDARD](https://www.omg.org/news/releases/pr2021/01-21-21.htm)
  > This RFI aims to gain a better understanding of the self-sovereign identity space. In particular, the Blockchain PSIG is exploring the potential for standards setting in the area of contextually constrained or ‘disposable’ self-sovereign identity arrangements, building on top of existing W3C standards for self-sovereign identity [DID] and verifiable credentials [VC]. The aim of this RFI is to determine whether new standards for this specific aspect of self-sovereign identity are necessary, desirable and timely, and are not already being developed elsewhere. (The RFI)
A [public presentation on the Disposable Self-sovereign Identity RFI](https://www.brighttalk.com/webcast/12231/461001) will be held on February 3, 2021 at 11:00 AM ET.
  > The Object Management Group® (OMG®) is an international, open membership, not-for-profit technology standards consortium, founded in 1989. OMG standards are driven by vendors, end-users, academic institutions and government agencies. OMG Task Forces develop enterprise integration standards for a wide range of technologies and an even wider range of industries.


## Agents

* [Agent Frameworks & Infrastructure (“Layer 2”)](https://identity.foundation/faq/#agent-frameworks-infrastructure-layer-2)

* [Mobile Agent Development FAQ](https://iiw.idcommons.net/1L/_Mobile_Agent_Development_FAQ) by Horacio Nunez
  > - What’s the best place to start creating your own mobile agent?
  > - How do you get updates once you ship your first version?
  > - Do I actually have to support a fork for every mobile agent I create?
  > - Do I need to use a Mediator?


## Schema.org 

* [Schema.org is ten!](http://blog.schema.org/2021/06/schemaorg-is-ten.html)

Schema.org was founded on the idea of making it easier and simpler for the ordinary, everyday sites that make up the web to use machine-readable data, and for that data to enable an ecosystem of applications used by millions of people. While it's hard to predict exactly what the next decade will bring, if we can all keep these founding concerns in mind as we improve, refine and curate our growing collection of schemas, we'll be doing our part to continue improving the web.



## JSON

* [JSON is Robot Barf](https://www.windley.com/archives/2021/09/json_is_robot_barf.shtml) Windley

JSON has its place. But I think we're overusing it in places where a good notation would serve us better.

## Blockcerts

* [Blockcerts V3 release](https://community.blockcerts.org/t/blockcerts-v3-release/3022)
  > The main change is the alignment with the [W3C Verifiable Credentials specification 3](https://www.w3.org/TR/vc-data-model/).
  > 
  > Regarding the standard itself metadata and display are entering the default standard. metadata comes in replacement of metadataJson and remains a stringified JSON that will allow consumers to register specific data which are too unique for issuances to be defined in the context.
  > 
  > display brings in [a little bit of novelty 2](https://github.com/blockchain-certificates/cert-schema/blob/master/cert_schema/3.0/displaySchema.json#L6) images or pdfs, in addition to the more classic HTML.
* [Blockcerts v3 release, a Verifiable Credentials implementation](https://lists.w3.org/Archives/Public/public-credentials/2021Dec/0051.html)  Julien Fraichot (Monday, 13 December)
  > I am excited to share with you today the release of [Blockcerts](https://www.blockcerts.org/) V3. As you may already know the earlier versions of Blockcerts were architected by Kim H. Duffy through Learning Machine and leveraged the Open Badge standard.
  > 
  > We have followed through with the initial [ideas established at RWOT 9 in Prague in December 2019, to align Blockcerts with the Verifiable Credential specification](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/final-documents/BlockcertsV3.md).

### XSL SDI

* [XSL Labs: Your Data Belongs to You](https://www.xsl-labs.io/whitepaper/white_paper_en.pdf)

The SDI technology constitutes a very important example of decentralized counter-power to the web giants. The SDI maintains to keep the practicality of a unique identifier while guaranteeing the security of the data and the user's sovereignty over it


## Oberon protocol

* [Better and more secure methods for API authentication](https://iiw.idcommons.net/1D/_Better_and_more_secure_methods_for_API_authentication) by Michael Lodder

Presentation slides: [https://docs.google.com/p>resentation/d/1UO25DzVmq25ya2S4_tV5UKTSP6NtBggln9vP1TEXSzE/edit](https://docs.google.com/presentation/d/1UO25DzVmq25ya2S4_tV5UKTSP6NtBggln9vP1TEXSzE/edit)

Goal of the Oberon protocol when building an API:

- Super effective: no separate session token to required for accessing the API; very fast to issue and verify tokens; 128 bytes required per message
- Privacy preserving
- No new crypto, uses BLS signature keys and Pointecheval saunders Construction

### Timestamping

* [Trusted Timestamping Part 3: Family of Standards](https://medium.com/finema/trusted-timestamping-part-3-family-of-standards-f0c89a5e97ab) Nunnaphat Songmanee Finema

Read more about timestamping and its concepts at [Trusted Timestamping Part 1: Scenarios](https://medium.com/finema/trusted-timestamping-part-1-scenarios-9bf4a7cc2364) and [Trusted Timestamping Part 2: Process and Safeguards](https://medium.com/finema/trusted-timestamping-part-2-process-and-safeguards-f75286a0c370).

Family of standards related to timestamping

## GAIN

- [Nat has a presentation](https://nat.sakimura.org/2021/09/14/announcing-gain/)
- There is a [linked in Group](https://www.linkedin.com/groups/12559000/)

## JWP

* [JSON Web Proofs BoF at IETF 114 in Philadelphia](https://self-issued.info/?p=2286)
- [Chair Slides](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-json-web-proofs-chair-drafts-00) – [Karen O’Donoghue](https://twitter.com/kodonog) and [John Bradley](https://twitter.com/ve7jtb)
- [The need: Standards for selective disclosure and zero-knowledge proofs](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-the-need-standards-for-selective-disclosure-and-zero-knowledge-proofs-00) – [Mike Jones](https://twitter.com/selfissued)
- [What Would JOSE Do? Why re-form the JOSE working group to meet the need?](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-the-need-standards-for-selective-disclosure-and-zero-knowledge-proofs-00) – [Mike Jones](https://twitter.com/selfissued)
- [A Look Under the Covers: The JSON Web Proofs specifications](https://datatracker.ietf.org/meeting/114/materials/slides-114-jwp-json-web-proofs-initial-drafts-00) – Jeremie Miller


### ONDC
* [ONDC: An Open Network for Ecommerce](https://www.windley.com/archives/2022/08/ondc_an_open_network_for_ecommerce.shtml) Phil Windley
* [Open Network for Digital Commerce](https://en.wikipedia.org/wiki/Open_Network_for_Digital_Commerce) is a non-profit established by the Indian government to develop open ecommerce. The goal is to end platform monopolies in ecommerce using an open protocol called [Beckn](https://developers.becknprotocol.io/). I'd never heard of Beckn before. From the reaction on the VRM mailing list, not many there had either.



### BBS Creds
- [aries-rfcs/0646-bbs-credentials#drawbacks](https://github.com/hyperledger/aries-rfcs/tree/main/features/0646-bbs-credentials#drawbacks)
- [Zero-Knowledge Proofs Do Not Solve the Privacy-Trust Problem of Attribute-Based Credentials: What if Alice Is Evil?](https://ieeexplore.ieee.org/document/9031545) IEEE


## C2PA
* [FYI: C2PA Releases Specification of World’s First Industry Standard for Content Provenance](https://lists.w3.org/Archives/Public/public-credentials/2022Jan/0207.html)  Leonard Rosenthol (Wednesday, 26 January)

Just wanted to update folks here that the C2PA has released version 1.0 of their specification at [https://c2pa.org/specifications/specifications/1.0/index.html](https://c2pa.org/specifications/specifications/1.0/index.html).  As previously mentioned, it includes native support for VC’s for use in identification of actors (be they human, organizations, etc.).  Thanks to everyone here for their input on our work and helping us to deliver.

