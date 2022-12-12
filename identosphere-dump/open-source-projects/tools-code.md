---
published: false
---


## Schema

* [Announcing Schema Markup Validator: validator.schema.org (beta)](http://blog.schema.org/2021/05/announcing-schema-markup-validator.html)

SDTT is a tool from Google which began life as the [Rich Snippets Testing Tool](https://developers.google.com/search/blog/2010/09/rich-snippets-testing-tool-improvements) back in 2010. Last year Google [announced plans](https://developers.google.com/search/blog/2020/07/rich-results-test-out-of-beta) to migrate from SDTT to successor tooling, the [Rich Results Test](https://search.google.com/test/rich-results), alongside plans to "deprecate the Structured Data Testing Tool". The newer Google tooling is focused on helping publishers who are targeting specific schema.org-powered [search features](https://developers.google.com/search/docs/guides/search-gallery) offered by Google, and for these purposes is a huge improvement as it contextualizes many warnings and errors to a specific target application.

## Semantics
* [The Importance of Data Inputs and Semantics for SSI with Paul Knowles [Podcast]](https://northernblock.io/semantics-for-ssi-with-paul-knowles/)
  > The platform was an incredibly federated platform when I built it because I didn’t know that SSI existed. So as soon as I found that ecosystem, I tore up the rulebook and said, “This isn’t going to work; I have to rebuild it.”

## QR

* [Gordian QR Tool Supports Vaccine Records, 2FAs, Cryptoseeds, and More](https://www.blockchaincommons.com/projects/Releasing-QRTool/) Blockchain Commons
  > Some possible architectural issues arise from using QR codes for confidential data, such as the fact that you’re actually transmitting the data (not a proof of the data), that the QRs tend to contain all of the data (not just a selection), and that there’s no way to rescind a QR or expire it. Those issues will have to be dealt with at a foundational level as we figure out what can safely be encoded as a QR — and more importantly how to offer restricted proofs rather than complete information.

## Mobile Agent Dev
* [App Framework for Mobile Agent Dev - “No more forking”](https://iiw.idcommons.net/22A/_App_Framework_for_Mobile_Agent_Dev_-_%2522No_more_forking%2522) by Horacio Nunez

This session had the objective to present a solution to the problem of forking when developing new mobile agents. With the current starting kits available in the community it is very easy to start a path where it is almost impossible to retrofit updates to the kit back into our custom agent.

The solution consists in using a framework-first approach and ensuring that custom code can reside exclusively outside of the framework, thus ensuring updates can be executed more easily.

The following link can be used as the public url for the project:

* [https://www.notion.so/App-Framework-for-Mobile-Agent-Development-No-more-forking-52ebe4e5635d400eb225b0ed537404d8](https://www.notion.so/App-Framework-for-Mobile-Agent-Development-No-more-forking-52ebe4e5635d400eb225b0ed537404d8)


### Caribou - Research \ Advisory
Digital Caribou shares their thoughts on [Digital Transformation and inclusion](https://medium.com/caribou-digital/transformation-in-a-digital-age-9068338fd778) - very good thinking for all of us working on digital identity.

> We believe that the emphasis on transformation as both process and effects is particularly important, especially as although digitization and digitalization are well underway, accelerated by the response to COVID-19 (remote working, payments, etc.), these are not inevitable processes. They are the results of human decisions. Similarly, the effects of these are not inevitable, either.
* [The human impact of identity exclusion in financial service](https://medium.com/caribou-digital/the-human-impact-of-identity-exclusion-in-financial-services-ce1e0d769389) Caribou Digital
  > we spoke to a range of participants who are or who have felt excluded from financial systems for different reasons and we’ll be sharing these stories over the next few months. This research is the foundation for Women in Identity to build an Identity Code of Conduct — a set of guiding principles and a framework for inclusive ID-product development.
* [Digital Identity for Development — and protection](https://medium.com/caribou-digital/digital-identity-for-development-and-protection-d92716f24bb6) Caribou Digital
  > the deployment of digital identification systems needs to get smarter about understanding the political interests and risks that shape the contexts in which identification systems are used — our [ID Ecosystem Mapping tool](https://medium.com/caribou-digital/kenyas-identification-ecosystem-7cbc2ee27) supports risk assessment arising from the deployment of digital identification systems.

## General Dev
* [Technical Debt](https://www.continuumloop.com/technical-debt/)
  > - Technical Debt – Seth covers it well but missed a major cause of technical debt. That being the shortcuts that are taken to meet deadlines and requirements – with the hope/fantasy that we’ll go back and do them right later (hint: we never do).
  > - Project Debt
  > - Why saying NO to those simple things may be the best thing. For some hints on how to do that see [Say No With Grace](https://www.continuumloop.com/say-no-with-grace/).
* [The Journey of an SSI Developer](https://academy.affinidi.com/the-journey-of-an-ssi-developer-6ef4f642779c) Affinidi
* [Clear is better than clever](https://dave.cheney.net/2019/07/09/clear-is-better-than-clever) Cheney.net

“why would I read your code?” To be clear, when I say I, I don’t mean me, I mean you. And when I say your code I also mean you, but in the third person. So really what I’m asking is, “why would you read another person’s code?”
* [Contributing to Complex Projects](https://mitchellh.com/writing/contributing-to-complex-projects) Mitchell H

Inspiration - for folks engaging with new code

As a frequent open source maintainer and contributor, I’m often asked: where do you start? How do you approach a new project with the goal of making meaningful changes? How can you possibly understand the internals of a complex project?


### Civic

* [Introducing New Tools for Creators to Build Trusted Communities](https://www.civic.com/blog/introducing-new-tools-for-creators-to-build-trusted-communities/) CIVIC

Our goal is to make the process of building trust easier and more effective for creators. With that in mind, we’re sharing an overview of our plan to address the pain points of creators and marketplaces in the NFT space using identity tools.

### Ceramic

* [An authentication system built with Ceramic & self.id](https://github.com/dabit3/decentralized-identity-example) dabit3

This project implements a user authentication flow leveraging an Ethereum wallet for single sign on capabilities across all of Web3.

The technologies used are [DID (decentralized identifiers)](https://www.w3.org/TR/did-core/), [Ceramic](https://ceramic.network/), [3id-connect](https://github.com/ceramicstudio/3id-connect), and [Self.ID](https://developers.ceramic.network/tools/self-id/overview/)
* [Building capability-based data security for Ceramic](https://blog.ceramic.network/capability-based-data-security-on-ceramic/)

The 3Box Labs team recently published a new standard for creating capability containers for accessing decentralized data to the Chain Agnostic Standards Alliance. Capability containers are an approach for managing advanced data security and permissions, commonly referred to as “Object Capabilities” or “OCAPs.”

This new standard is currently in development for use on Ceramic. Once deployed in a future version of the protocol, it will allow Ceramic to be fully compatible with the new Sign-in with Ethereum (SIWE) specification as well as provide advanced data flow control features for resources stored on the Ceramic network.
* [The next architecture for building Web3 data apps](https://blog.ceramic.network/the-next-architecture-for-building-web3-data-applications/) Ceramic

We're replacing the popular IDX runtime with a more powerful set of tools for building applications on Ceramic including DID DataStore, DataModels, and Self.ID.


## Entrustient
* [No Code Solution Using Self-Sovereign Identity on Redundant Blockchains](https://www.pressrelease.cc/2021/12/02/entrustient-launches-the-first-no-code-solution-for-trusted-decentralized-digital-identity-using-self-sovereign-identity-on-redundant-blockchains/) Entrustient

Our goal was to put the power back into the hands of users who do not have any coding knowledge or experience, to accelerate the time to configure and launch an entire Trusted Decentralized Digital Identity peer-to-peer ecosystem



### Sphereon
* [PRESENTATION EXCHANGE WITH SIOP V2](https://sphereon.com/solution/dif-presentation-exchange-with-siop-v2/)

Sphereon has developed a Typescript/Javascript Library  that implements the functionality described in the [DIF Presentation Exchange](https://identity.foundation/presentation-exchange/) specification.

### bloom

* [Introducing SSI SDK](https://bloom.co/blog/introducing-ssi-sdk/) Bloom

- @bloomprotocol/vc
- @bloomprotocol/ecdsa-secp256k1-signature-2019
- @bloomprotocol/ecdsa-secp256k1-verification-key-2019
- @bloomprotocol/elem-did-legacy-non-anchored
- @bloomprotocol/waci-core
- @bloomprotocol/waci-jose
- @bloomprocotol/waci-kit-react
- @bloomprotocol/presentation-exchange
- @bloomprotocol/credential-manifest

### Ringaile
* [How to write verifiable credentials in golang](https://ringaile.medium.com/how-to-write-verifiable-credentials-in-golang-7447234d5c16)
Note: the code is written following the 
[Verifiable Credentials Data Model 1.0](https://www.w3.org/TR/vc-data-model/)
You can find full code here: 
[https://github.com/ringaile/ver-cred](https://github.com/ringaile/ver-cred)

### EPS
* [EPS for SSI (Self-Sovereign Identity)](https://kokumai.medium.com/eps-for-ssi-self-sovereign-identity-8c742e2b1d02)
  > In my earlier post, I failed to refer specifically to the people working for Self-Sovereign Identity and the likes of blockchain that support the distributed/decentralised storage of secrets. [...] you might all be interested to hear that the key function of Expanded Password System is to convert images to high-entropy codes that work as very long passwords and also as the seeds of symmetric/asymmetric cryptographic keys.

### Dillo-DID Plugin Dillo Browser

* [Dillo plugin for DID URLs](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0038.html) Charles E. Lehner
  > I would like to announce dillo-did, a plugin for the Dillo web browser implementing support for DIDs. This plugin enables navigating to DID URLs in Dillo and viewing the resolved/dereferenced DID documents and resources like web pages. The implementation of the DID functionality used is from ssi/DIDKit.


### Godidy
* [@mfosterio · Apr 29](https://twitter.com/mfosterio/status/1520130657468440576) Twitter

I created a DID at [http://GoDiddy.com](https://t.co/QhwQhqUz0k) did:key:z6MkfxFPD3vwny367HZVQoqUnKatH4RTHEitcbEdvxst3nZm#z6MkfxFPD3vwny367HZVQoqUnKatH4RTHEitcbEdvxst3nZm DIDs are important in Self Sovereign Identity. You can learn about DIDs 

### ownyourdata
* [Semantic Overlay Architecture](https://www.ownyourdata.eu/en/semantic-overlay-architecture/) Own Your Data

We have documented the [functionality of SOyA](https://ownyourdata.github.io/soya/) in a W3C-conforming Specifiation and the full source code is available under the MIT License [on Github](https://github.com/OwnYourData/soya/). Examples and an introduction how to use SOyA is [available in a dedicated Tutorial](https://github.com/OwnYourData/soya/blob/main/tutorial/README.md)


### T-Systems
* [Self Sovereign Identity (SSI) at T-Systems MMS: Interview mit Mujtaba Idrees, T-Systems MMS](https://www.youtube.com/watch?v%3DA311QHASy5Y) 7min video on YouTube

► Dr. Ivan Gudymenko, Subject Matter Lead SSI and Confidential Computing, T-Systems MMS

►Mujtaba Idrees, Advanced Software Engineer, T-Systems MMS

► [Credentials as a Service Providing Self Sovereign Identity as a Cloud Service Using Trusted Execution Environments](https://ieeexplore.ieee.org/document/9610297)

### KidOYO
* [Engineer your world this summer: K-University student + teacher opportunities are live!](https://kidoyo.com/join) KidOYO

Whether a beginning learner, or interested in advanced concepts like Game Development, Hardware Prototyping, or Competitive Coding, you will find tools, lessons and mentors


### Aztec

* [Introducing Noir: The Universal Language of Zero-Knowledge](https://medium.com/aztec-protocol/introducing-noir-the-universal-language-of-zero-knowledge-ff43f38d86d9) Aztec Network

Noir is a Rust-based domain specific language (DSL) for creating and verifying zero-knowledge proofs. It’s the easiest way to write zk applications that are compatible with any proving system.

