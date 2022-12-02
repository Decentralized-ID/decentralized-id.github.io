---
published: false
---
* [Open API for Interoperable Traceability](https://w3c-ccg.github.io/traceability-interop/openapi/%23overview) CCG
  > `resolve:dids - Grants permission to resolve DIDsissue:credentials - Grants permission issue Verifiable Credentialsverify:credentials - Grants permission verify Verifiable Credentialsread:credentials - Grants permission to get Verifiable Credentialsupdate:credentials - Grants permission to update the status of Verifiable Credentialsprove:presentations - Grants permission to prove Verifiable Presentationsverify:presentations - Grants permission verify Verifiable Presentationssubmit:presentations - Grants permission to submit Verifiable Presentations`

# Tools

* [Beginners Guide to JWTs](https://developer.okta.com/blog/2020/12/21/beginners-guide-to-jwt)
  > A JWT is a structured security token format used to encode JSON data. The main reason to use JWT is to exchange JSON data in a way that can be cryptographically verified. There are two types of JWTs:
> - JSON Web Signature (JWS)
> - JSON Web Encryption (JWE)
> The data in a JWS is public—meaning anyone with the token can read the data—whereas a JWE is encrypted and private. To read data contained within a JWE, you need both the token and a secret key.
* [The Importance of Data Inputs and Semantics for SSI with Paul Knowles [Podcast]](https://northernblock.io/semantics-for-ssi-with-paul-knowles/)
  > The platform was an incredibly federated platform when I built it because I didn’t know that SSI existed. So as soon as I found that ecosystem, I tore up the rulebook and said, “This isn’t going to work; I have to rebuild it.”
* [Webinar Series: rlogin Developer Workshop from RIF Identity](https://www.youtube.com/watch?v%3Do35EgZ4VH2Q)
  > rLogin allows web application developers to integrate blockchain technologies giving the user the power of data portability. After integrating rLogin you achieve:

- A back-end authenticating users by their wallet addressed - their Decentralized Identifiers.
- A registration model capable of requesting users for data stored in its user-centric cloud storage, the Data Vault.
- A front-end capable of interacting with any wallet that the user chooses, with a pre-designed user experience for registration and login.
- Compatibility with a unified platform where the user can control their identity and information, the RIF Identity Manager.
* [What is the VC-Generator App and How to Leverage it?](https://academy.affinidi.com/what-is-the-vc-generator-app-and-how-to-leverage-it-4fa5a54844f2)
  > In simple terms, the VC-Generator allows you to choose a credential type that needs to be issued or verified from a drop-down list and displays the associated VC schema.

Code: [https://github.com/swiss-ssi-group/MattrGlobalAspNetCore](https://github.com/swiss-ssi-group/MattrGlobalAspNetCore)
* [Present and and Verify Verifiable Credentials in ASP.NET Core Using Decentralized Identities and Mattr](https://damienbod.com/2021/05/10/present-and-verify-verifiable-credentials-in-asp-net-core-using-decentralized-identities-and-mattr/)

This article shows how use verifiable credentials stored on a digital wallet to verify a digital identity and use in an application. For this to work, a trust needs to exist between the verifiable credential issuer and the application which requires the verifiable credentials to verify. A blockchain decentralized database is used and MATTR is used as a access layer to this ledger and blockchain. The applications are implemented in ASP.NET Core.
* [Gordian QR Tool Supports Vaccine Records, 2FAs, Cryptoseeds, and More](https://www.blockchaincommons.com/projects/Releasing-QRTool/) Blockchain Commons
  > Some possible architectural issues arise from using QR codes for confidential data, such as the fact that you’re actually transmitting the data (not a proof of the data), that the QRs tend to contain all of the data (not just a selection), and that there’s no way to rescind a QR or expire it. Those issues will have to be dealt with at a foundational level as we figure out what can safely be encoded as a QR — and more importantly how to offer restricted proofs rather than complete information.
* [Build an SSI proof of concept in <30 minutes](https://iiw.idcommons.net/21G/_Build_an_SSI_proof_of_concept_in_30_minutes) by Riley Hughes

The session began with a short introduction to SSI, an introduction to Trinsic, and an overview of how to get started. Then, everybody present starting building an SSI proof of concept, creating issuers, verifiers, and schemas to learn first-hand how it all works. A step-by-step guide on how to replicate this session can be found at the following link:

* [https://www.notion.so/trinsic/Build-an-SSI-Proof-of-Concept-dae9d6e565eb4770be41b61d55e090cb](https://www.notion.so/trinsic/Build-an-SSI-Proof-of-Concept-dae9d6e565eb4770be41b61d55e090cb)
* [App Framework for Mobile Agent Dev - “No more forking”](https://iiw.idcommons.net/22A/_App_Framework_for_Mobile_Agent_Dev_-_%2522No_more_forking%2522) by Horacio Nunez

This session had the objective to present a solution to the problem of forking when developing new mobile agents. With the current starting kits available in the community it is very easy to start a path where it is almost impossible to retrofit updates to the kit back into our custom agent.

The solution consists in using a framework-first approach and ensuring that custom code can reside exclusively outside of the framework, thus ensuring updates can be executed more easily.

The following link can be used as the public url for the project:

* [https://www.notion.so/App-Framework-for-Mobile-Agent-Development-No-more-forking-52ebe4e5635d400eb225b0ed537404d8](https://www.notion.so/App-Framework-for-Mobile-Agent-Development-No-more-forking-52ebe4e5635d400eb225b0ed537404d8)

## Code

* [Auto-Generating Language-Specific Wrappers for Rust Libraries](https://iiw.idcommons.net/22E/_Auto-Generating_Language-Specific_Wrappers_for_Rust_Libraries) by Steve McCown

Rust, FFI, Code generation, language bindings, UDL

- Implementation of FFI that makes it easy to call Rust code
- Define API contracts using UDL
- Generates language specific code that’s idiomatic to the language used
- Tutorial documentation and source code: [https://github.com/sudoplatform-labs/ffi-tutorials](https://github.com/sudoplatform-labs/ffi-tutorials)
- Slides: [https://docs.google.com/presentation/d/183cn6NyrMUJLdid8-IoKmPZjVslmp4X0UvYIQvyeSBU/edit#slide=id.p1](https://docs.google.com/presentation/d/183cn6NyrMUJLdid8-IoKmPZjVslmp4X0UvYIQvyeSBU/edit%23slide%3Did.p1)
* [How We Test Our Android Code at Anonyome Labs](https://anonyome.com/2021/08/insight-how-we-test-our-android-code-at-anonyome-labs/)

At Anonyome Labs we value well-written code that has good tests. This is a guide on how we go about producing useful and meaningful tests for our Android code. Testing approach: SDK or app?
* [Falsehoods Programmers Believe About Names - With Examples](https://shinesolutions.com/2018/01/08/falsehoods-programmers-believe-about-names-with-examples/) Shine Solutions Group

In this post I’m going to list all 40 of Patrick’s original falsehoods, but give you an example (or two) drawn from my experiences working in this space. Ready? Let’s go!

1. People have exactly one canonical full name.
2. People have exactly one full name which they go by.
* [Technical Debt](https://www.continuumloop.com/technical-debt/)

A short note to point folks at Seth Godin’s recent podcast about Project Debt. He covers some great topics:

- Technical Debt – Seth covers it well but missed a major cause of technical debt. That being the shortcuts that are taken to meet deadlines and requirements – with the hope/fantasy that we’ll go back and do them right later (hint: we never do).
- Project Debt
- Why saying NO to those simple things may be the best thing. For some hints on how to do that see [Say No With Grace](https://www.continuumloop.com/say-no-with-grace/).

Give it a listen on [Overcast](https://overcast.fm/%2BL0YUSAwxA) (my fave) or  [Apple Podcasts](https://podcasts.apple.com/us/podcast/project-debt/id1345042626?i%3D1000536252965).
* [Dangling Domain From SDK Installed in 150+ Apple Apps Putting Kids, Families and Crypto Traders at Risk](https://me2ba.org/dangling-domain-from-sdk-installed-in-150-apple-apps-putting-kids-families-and-crypto-traders-at-risk/)

TLDR: The Me2B Alliance believes apps including the AskingPoint SDK should be safe from malicious redirects or other exploits.

* [Welcome to Dock’s API - Testnet Sandbox](https://blog.dock.io/welcome-to-docks-api-testnet-sandbox/)

You can test our API in the sandbox testnet by simply switching the toggle to test mode. To get started; create a free account, log into your dashboard and acquire your API key.
* [The Journey of an SSI Developer](https://academy.affinidi.com/the-journey-of-an-ssi-developer-6ef4f642779c) Affinidi

## HowTo

* [Rendering credentials in a human-friendly way](https://medium.com/mattr-global/rendering-credentials-in-a-human-friendly-way-e47f4a32fd4b) Mattr

For example, this update formats address fields to make them more readable; formats names and proper nouns where possible; makes URLs, telephone numbers and email addresses clickable; highlights images and icons for better trust and brand signaling; and creates basic rules for language localization that adjust to a user’s device settings.
* [Using Decentralized Identifiers (DIDs) Without a Digital Wallet](https://academy.affinidi.com/using-decentralized-identifiers-dids-without-a-digital-wallet-34646074ba42) Affinidi

there are many known DID methods, but most of them require you to have a [digital identity wallet](https://academy.affinidi.com/5-reasons-to-use-an-identity-wallet-c289ba2980cf) 🔒, where you will keep a seed ([private key](https://academy.affinidi.com/role-of-public-key-cryptography-in-self-sovereign-identity-8c2dc37a2bf3) 🔑.

While this may sound convenient for many of us, it comes with its shortcomings as well.

* [DIDComm Messaging through libp2p](https://medium.com/uport/didcomm-messaging-through-libp2p-cffe0f06a062) uPort

Peers would still use their peer ID for [libp2p](https://libp2p.io/) routing and authentication. Alice and Bob would exchange their [DID](https://www.w3.org/TR/did-core/) out of band and will be able to find their counterparty’s peer ID via their [DIDs](https://www.w3.org/TR/did-core/).

* [Introducing New Tools for Creators to Build Trusted Communities](https://www.civic.com/blog/introducing-new-tools-for-creators-to-build-trusted-communities/) CIVIC

Our goal is to make the process of building trust easier and more effective for creators. With that in mind, we’re sharing an overview of our plan to address the pain points of creators and marketplaces in the NFT space using identity tools.



* [An authentication system built with Ceramic & self.id](https://github.com/dabit3/decentralized-identity-example) dabit3

This project implements a user authentication flow leveraging an Ethereum wallet for single sign on capabilities across all of Web3.

The technologies used are [DID (decentralized identifiers)](https://www.w3.org/TR/did-core/), [Ceramic](https://ceramic.network/), [3id-connect](https://github.com/ceramicstudio/3id-connect), and [Self.ID](https://developers.ceramic.network/tools/self-id/overview/)
* [Implement Compound Proof BBS+ Verifiable Credentials Using ASP.NET Core and MATTR](https://damienbod.com/2021/12/13/implement-compound-proof-bbs-verifiable-credentials-using-asp-net-core-and-mattr/) Damien Bod

The ZKP BBS+ verifiable credentials are issued and stored on a digital wallet using a Self-Issued Identity Provider (SIOP) and OpenID Connect. A compound proof presentation template is created to verify the user data in a single verify.

Code: [https://github.com/swiss-ssi-group/MattrAspNetCoreCompoundProofBBS](https://github.com/swiss-ssi-group/MattrAspNetCoreCompoundProofBBS)
* [DTDL models - Azure Digital Twins | Microsoft Docs](https://docs.microsoft.com/en-us/azure/digital-twins/concepts-models)

MSFT does know how to do to JSON-LD they just pretend not to

DTDL is based on JSON-LD and is programming-language independent. DTDL isn't exclusive to Azure Digital Twins, but is also used to represent device data in other IoT services such as [IoT Plug and Play](https://docs.microsoft.com/en-us/azure/iot-develop/overview-iot-plug-and-play).
* [The Journey of an SSI Developer](https://academy.affinidi.com/the-journey-of-an-ssi-developer-6ef4f642779c) Affinidi

* [Building capability-based data security for Ceramic](https://blog.ceramic.network/capability-based-data-security-on-ceramic/)

The 3Box Labs team recently published a new standard for creating capability containers for accessing decentralized data to the Chain Agnostic Standards Alliance. Capability containers are an approach for managing advanced data security and permissions, commonly referred to as “Object Capabilities” or “OCAPs.”

This new standard is currently in development for use on Ceramic. Once deployed in a future version of the protocol, it will allow Ceramic to be fully compatible with the new Sign-in with Ethereum (SIWE) specification as well as provide advanced data flow control features for resources stored on the Ceramic network.
* [Create Verifiable Credentials Without Writing a Single Line of Code](https://blog.dock.io/verifiable-credentials-without-code/) Dock

* [Why the Indicio TestNet is the Best Way to Explore Decentralized Identity](https://indicio.tech/why-the-indicio-testnet-is-the-best-way-to-explore-decentralized-identity/)

Indicio Thought Leadership

* [The SSI Kit](https://walt.id/blog/p/ssi-kit) Walt ID

Introducing the SSI Kit, which offers developers and organisations an easy and fast way to use Self-Sovereign Identity (SSI).

* [The human impact of identity exclusion in financial service](https://medium.com/caribou-digital/the-human-impact-of-identity-exclusion-in-financial-services-ce1e0d769389) Caribou Digital

we spoke to a range of participants who are or who have felt excluded from financial systems for different reasons and we’ll be sharing these stories over the next few months. This research is the foundation for Women in Identity to build an Identity Code of Conduct — a set of guiding principles and a framework for inclusive ID-product development.

* [Auth0 Lab](https://twitter.com/Auth0Lab/status/1468974610058137604)

early experiment with Sign in With Ethereum + auth0

usernameless + passwordless auth

Support for [@MetaMask](https://twitter.com/MetaMask), walletlink

profile enriched with ENS + NFTs through [@graphprotocol](https://twitter.com/graphprotocol)

Interested? discuss [https://discord.gg/rkjYHWHJ](https://t.co/dVK1CTV2JC)
* [No Code Solution Using Self-Sovereign Identity on Redundant Blockchains](https://www.pressrelease.cc/2021/12/02/entrustient-launches-the-first-no-code-solution-for-trusted-decentralized-digital-identity-using-self-sovereign-identity-on-redundant-blockchains/) Entrustient

Our goal was to put the power back into the hands of users who do not have any coding knowledge or experience, to accelerate the time to configure and launch an entire Trusted Decentralized Digital Identity peer-to-peer ecosystem

* [tbDEX: A Liquidity Protocol v0.1](https://tbd54566975.ghost.io/introducing-tbdex/)

The tbDEX protocol facilitates decentralized networks of exchange between assets by providing a framework for establishing social trust, utilizing decentralized identity (DID) and verifiable credentials (VCs) to establish the provenance of identity in the real world.

* [How to Handle JWTs in Python](https://auth0.com/blog/how-to-handle-jwt-in-python/)

JSON Web Tokens, or JWTs for short, are all over the web. They can be used to track bits of information about a user in a very compact way and can be used in APIs for authorization purposes. This post will cover what JSON Web Tokens are and how to create JWTs in Python using the most popular JWT library: [PyJWT](http://pyjwt.readthedocs.io/). We are also going to see how you can sign and verify JWTs in Python using asymmetric algorithms.

* [2021 FIDO Developer Challenge: Outcomes and Winners](https://fidoalliance.org/2021-fido-developer-challenge-outcomes-and-winners/)

1. Gold Winner – [Lockdrop](https://lockdrop.com/)
2. Silver Winner – [Shaxware](https://www.shaxware.com/)
3. Bronze Winner – SoundAuth ([Trillbit](https://www.trillbit.com/)

This year’s FIDO Developer Challenge reached a successful conclusion, with a ceremonial event during [Authenticate 2021](https://authenticatecon.com/event/authenticate-2021-conference/) of the ceremony is available now, and we’re pleased to share more detailed stories of the three finalists as well as the rest of the teams that made it to the final stage.

* [Clear is better than clever](https://dave.cheney.net/2019/07/09/clear-is-better-than-clever) Cheney.net

“why would I read your code?” To be clear, when I say I, I don’t mean me, I mean you. And when I say your code I also mean you, but in the third person. So really what I’m asking is, “why would you read another person’s code?”

* [The next architecture for building Web3 data apps](https://blog.ceramic.network/the-next-architecture-for-building-web3-data-applications/) Ceramic

We're replacing the popular IDX runtime with a more powerful set of tools for building applications on Ceramic including DID DataStore, DataModels, and Self.ID.

* [Q&A with Gravity’s lead engineer: François Guérin](https://medium.com/gravity-earth/q-a-with-gravitys-lead-engineer-fran%25C3%25A7ois-gu%25C3%25A9rin-babb3659be86)

As the Lead Developer, a big part of my role is to build Gravity’s decentralized identity protocol and blockchain architecture on Tezos.

* [PRESENTATION EXCHANGE WITH SIOP V2](https://sphereon.com/solution/dif-presentation-exchange-with-siop-v2/)

Sphereon has developed a Typescript/Javascript Library  that implements the functionality described in the [DIF Presentation Exchange](https://identity.foundation/presentation-exchange/) specification.

* [Digital Identity for Development — and protection](https://medium.com/caribou-digital/digital-identity-for-development-and-protection-d92716f24bb6) Caribou Digital

the deployment of digital identification systems needs to get smarter about understanding the political interests and risks that shape the contexts in which identification systems are used — our [ID Ecosystem Mapping tool](https://medium.com/caribou-digital/kenyas-identification-ecosystem-7cbc2ee27) supports risk assessment arising from the deployment of digital identification systems.


* [Spruce Developer Update #11](https://sprucesystems.medium.com/spruce-developer-update-11-7766b44e1075)

* [Developers Guide to GPG and YubiKey](https://developer.okta.com/blog/2021/07/07/developers-guide-to-gpg) Okta

I’ll walk through configuring a YubiKey and highlight some of the things I’ve learned along the way.

* [What Is an API? How APIs Work (for Non-Developers)](https://auth0.com/blog/what-is-an-api-how-apis-work-for-non-developers/) Auth0

Learn how APIs can accelerate software development and delivery.

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

* [Introducing the Indicio DemoNet—a new decentralized network for product demonstration](https://indicio.tech/blog/introducing-the-indicio-demonet-a-new-decentralized-network-for-product-demonstration/) Indicio

The Indicio DemoNet joins the [Indicio TestNet](https://indicio.tech/indicio-testnet/), which is used for developing new technology releases, and the [Indicio MainNet](https://indicio.tech/indicio-mainnet/), which hosts mission-critical products and services. With the DemoNet, Indicio now provides a full suite of networks for decentralized identity development and deployment.
* [How to write verifiable credentials in golang](https://ringaile.medium.com/how-to-write-verifiable-credentials-in-golang-7447234d5c16)
Note: the code is written following the 
[Verifiable Credentials Data Model 1.0](https://www.w3.org/TR/vc-data-model/)
You can find full code here: 
[https://github.com/ringaile/ver-cred](https://github.com/ringaile/ver-cred)

* [Indicio.Tech releases Aries Mediator Agent](https://indicio.tech/blog/indicio-tech-advances-decentralized-identity-with-release-of-critical-open-source-technology/)
  > The Indicio Mediator Agent is the company’s latest contribution to Aries Cloud Agent Python (ACA-Py) and the Aries Toolbox. Following RFC 0211: Mediator Coordination, Indicio built on the work of the open-source community to make mediation interoperable and vendor agnostic. This expands the opportunities for mobile wallet implementations.
  > *[...]*
  > Indicio.tech is committed to becoming a resource-hub for decentralized identity, providing enterprise-grade open source tools to its clients and to the community. This includes the [Private Networks](https://indicio.tech/private-networks/) build service, the [Indicio TestNet](https://indicio.tech/indicio-testnet/), and a variety of customizable [training programs](https://indicio.tech/training-packages/).

* [Spruce Developer Update #5](https://sprucesystems.medium.com/spruce-developer-update-5-86d6f517a220)

This is so exciting to see what Wayne and his team are building.

> At Spruce, we’re building a product suite to manage all aspects of the data supply chain.
- [Tezos DID Method](https://did-tezos-draft.spruceid.com/) - Specifies VC compatible DID creation and management
- [DIDKit](https://sprucesystems.medium.com/introducing-didkit-an-identity-toolkit-e0dfa292f53d) - cross-platform toolkit for working with DIDs and VCs.
- [Credible](https://medium.com/@sprucesystems/spruce-developer-update-2-484368f87ee9) - Spruce’s credential wallet.
- Intake - onboarding tool \ secure document collection and processing.
* [@BartHanssens shares](https://twitter.com/BartHanssens/status/1319604882068787200):
  > proofs: https://w3c-ccg.github.io/ld-proofs, cryptosuite: https://w3c-ccg.github.io/ld-cryptosuite-registry, #GnuPG: signatures  https://gpg.jsld.org/contexts
* [EPS for SSI (Self-Sovereign Identity)](https://kokumai.medium.com/eps-for-ssi-self-sovereign-identity-8c742e2b1d02)
  > In my earlier post, I failed to refer specifically to the people working for Self-Sovereign Identity and the likes of blockchain that support the distributed/decentralised storage of secrets. [...] you might all be interested to hear that the key function of Expanded Password System is to convert images to high-entropy codes that work as very long passwords and also as the seeds of symmetric/asymmetric cryptographic keys.

* [Mental Models of JSON-LD and what a "Document Loader" really does](https://www.youtube.com/watch?v=-yUbMDft5O0)  Orie Steel
  > and terms like "dereferencing" that trip up even highly experienced senior developers that show up late to the Linked-Data party and its open-world model (complete with its own security model based on different availability assumptions).

* [Trinsic donates did-key.rs to I&D WG](https://medium.com/decentralized-identity/trinsic-donates-did-key-rs-to-i-d-wg-8a278f37bcd0)
  > DID:Key, originally specified in the W3C Credentials Community Group (CCG), is a DID “pseudo-method” that allows static, pre-existing, and/or pre-published public keys to function like traditional DIDs — they can be queried, stored, issued against, and resolved to return valid DID documents.
* [DIDKit v0.1 is Live.](https://sprucesystems.medium.com/didkit-v0-1-is-live-d0ea6638dbc9)
  > Most other options are subtly locked to a specific blockchain and its particularities, which a self-sovereign identity (SSI) novice is unlikely to notice until months into a project based on it. A few open-source libraries exist to sidestep this infrastructural lock-in, but these are more like primitives for assembling an SSI toolkit than ready-to-go, developer-friendly libraries. DIDKit, on the other hand, is ready to start processing real-world VCs with non-repudiable signatures right out the box.

* [Aries Mobile Agent SDK for Google Flutter](https://ayanworks.medium.com/announcing-arnima-fl-open-source-aries-flutter-mobile-agent-sdk-d3483744ffc8)
  > Exactly a year ago in Jan 2020, we announced ARNIMA — first ever Aries React Native Mobile Agent SDK that we made open source for the Self-Sovereign Identity ecosystem.
  > 
  > [...] We are very excited to announce [one more small open-source contribution](https://github.com/ayanworks/ARNIMA-flutter-sdk) from AyanWorks to the Aries community.



* [Announcing Pico Engine 1.0](https://www.windley.com/archives/2021/02/announcing_pico_engine_10.shtml)
  > In addition to the work on the engine itself, one of the primary workstreams at present is to complete Bruce Conrad's excellent work to use DIDs and DIDComm as the basis for inter-pico communication, called ACA-Pico (Aries Cloud Agent - Pico). [...] This work is important because it will replace the current subscriptions method of connecting heterarchies of picos with DIDComm. [...] because DIDComm is protocological, this will support protocol-based interactions between picos, including credential exchange.

* [ACA-Pico working group](https://docs.google.com/document/d/12dWUFyL7u6OQkhnPObJOOlV-U2LDoHpF-ZQLj3hXbjA/edit)

* [Picolab/aries-cloudagent-pico](https://github.com/Picolab/aries-cloudagent-pico)

* [New Tools to Support Production Deployments](https://trinsic.id/new-tools-to-support-production-deployments/)

* [Introduction to Trinsic’s APIs](https://trinsic.id/an-introduction-to-trinsics-apis/)
* [Provider](https://docs.trinsic.id/reference#assets) • [Credentials](https://docs.trinsic.id/reference#connections) • [Wallet](https://docs.trinsic.id/reference#connection)
* [Building and Securing a Go and Gin Web Application](https://developer.okta.com/blog/2021/02/17/building-and-securing-a-go-and-gin-web-application) Okta
  > Today, we are going to build a simple web application that implements a to-do list. The backend will be written in Go. It will use the Go Gin Web Framework which implements a high-performance HTTP server. The front end will use the Vue.js JavaScript framework to implement a single page application (SPA). We will secure it using Okta OAuth 2.0 authentication.
* [Dillo plugin for DID URLs](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0038.html) Charles E. Lehner
  > I would like to announce dillo-did, a plugin for the Dillo web browser implementing support for DIDs. This plugin enables navigating to DID URLs in Dillo and viewing the resolved/dereferenced DID documents and resources like web pages. The implementation of the DID functionality used is from ssi/DIDKit.
* [Status.trinsic.id](http://status.trinsic.id/)
  > View historical uptime: Using the status page, you can see the last 90 days of uptime of all our externally-facing services. You can also inspect individual incidents and view incident reports.Be notified of incidents: By clicking the “subscribe” button in the upper-left of the screen, you can have any downtime or incidents trigger a notification to your email or Slack workspace.

* [RIF’s Self Sovereign Identity Developer Library and Repos](https://rsci.app.link/)
- [RSK ID Repos](https://developers.rsk.co/rif/identity/#repos)
- [RIF Identity Documentation](https://developers.rsk.co/rif/identity/)

* [Transmute releases technical workbenches](https://medium.com/transmute-techtalk/transmute-releases-technical-workbenches-892f8140ac6e) by Orie Steele, Transmute
    > This new suite of tools is available for developers to experiment with today and includes:
    > 
    > - [Element Ropsten Workbench](http://staging.element.transmute.industries/)
    > - [Encrypted Data Vault Workbench](https://staging.data-vault.transmute.industries/)
    > - [DID Key Workbench](http://did.key.transmute.industries/)
    >
    > Transmute leverages these workbenches as part of our global trade solutions, where our customers benefit from verifiable data workflows and integrated capabilities. 

* [Mattr Releases JSON-LD Lint](https://mattr.global/new-to-json-ld-introducing-json-ld-lint/) By Emily Fry and Tobias Looker, Mattr Global
    > JSON-LD, based on the ubiquitous JSON technology, is rapidly gaining [adoption](https://w3techs.com/technologies/details/da-jsonld) on the web. [JSON-LD](https://json-ld.org/) is an innovation relevant to both [business minds](https://www.forbes.com/sites/forbestechcouncil/2019/02/25/why-is-json-ld-important-to-businesses/#565e8546e1bf) and developers alike.

### Code

* [IOTA DID - Alpha Release for Rust & Javascript](https://blog.iota.org/releasing-iota-identity-alpha-a-standard-framework-for-digital-identity-cebabd108b4f) of a standard framework for digital identity, based upon the W3C standards for DID decentralized identifiers and Verifiable Credentials, including the [full Rust implementation and Web Assembly bindings](https://github.com/iotaledger/identity.rs/). 

* [Selv identity wallet](https://github.com/iotaledger/selv-mobile)
* [IOTA Identity Experience Team](https://github.com/iota-community/X-Team_IOTA_Identity)

* [Spruce Systems introduces DIDKit](https://sprucesystems.medium.com/introducing-didkit-an-identity-toolkit-e0dfa292f53d)
  > DIDKit is a cross-platform toolkit for working with W3C Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs). It allows you to resolve and manage DID documents, and also manage the entire lifecycle of Verifiable Credentials including their issuance, presentation, and verification.
* [A repository of JSON Schemas for Verifiable Credentials](https://github.com/rsksmart/vc-json-schemas)
  > The Credential Schema is a document that is used to guarantee the structure, and by * [OpenID Foundation is Hiring a new Executive Director](https://openid.net/2020/11/17/openid-foundation-executive-director-job-description/)
  > The OpenID Foundation is seeking an Executive Director with the experience, skills, strategic vision, and commitment to advancing the Foundation’s open standards initiatives. This is a unique opportunity to lead a well-respected, member-driven, vendor-neutral, international standardization organization.

extension the semantics, of the set of claims comprising a Verifiable Credential. A shared Credential Schema allows all parties to reference data in a known way

* [Spruce Systems Developer Update #4](https://sprucesystems.medium.com/spruce-developer-update-4-cd6472c58fe1)

- The [Tezos DID Method](https://did-tezos-draft.spruceid.com/) specifies how Tezos can be used for DID creation and management, compatible with the issuance, storage, and verification of Verifiable Credentials.
- [DIDKit](https://sprucesystems.medium.com/introducing-didkit-an-identity-toolkit-e0dfa292f53d) is a cross-platform toolkit for working with W3C Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs).
- [Credible](https://medium.com/@sprucesystems/spruce-developer-update-2-484368f87ee9) is Spruce’s native credential wallet for the consumption, storage, and presentation of Verifiable Credentials on Android and iOS.
- Keylink is Spruce’s tool to link existing enterprise accounts to keypairs.
- Intake is a smarter onboarding tool for businesses via secure document collection and processing. These artifacts can then be used as evidence to generate and issue credentials to the counterparty that originally uploaded them.
* [Create Custom Verifiable Credentials with Affinidi’s Schema Manager](https://academy.affinidi.com/create-custom-verifiable-credentials-with-affinidis-schema-manager-86149b2d49d6) Affinidi

Overall, the creation of a new schema type via the SDK was not a straightforward process.

This is where Affinidi’s [Schema Manager](http://ui.schema.affinidi.com/) comes into play

* [Contributing to Complex Projects](https://mitchellh.com/writing/contributing-to-complex-projects) Mitchell H

Inspiration - for folks engaging with new code

As a frequent open source maintainer and contributor, I’m often asked: where do you start? How do you approach a new project with the goal of making meaningful changes? How can you possibly understand the internals of a complex project?

* [Will decision making improve if we understand the bias in the decision making unit?](https://www.mydigitalfootprint.com/2022/03/will-decision-making-improve-if-we.html) My Digital Footprint

At the most superficial level, we know that the expectations of board members drive decisions.  The decisions we take link to incentives, rewards and motivations and our shared values.

* [Are Transactional Relationships Enough?](https://www.windley.com/archives/2022/03/are_transactional_relationships_enough.shtml) Phil WIndley

Our online relationships are almost all transactional. A purely transaction digital life can't feel as rich and satisfying as one based on interactional relationships. As more of our relationships are intermediated by technology, finding ways to support interactional relationships will allow us to live authentic digital lives.

* [Verifiable Actions for signing and verifying VCs with DIDs](https://medium.com/@Transmute/verifiable-actions-for-signing-and-verifying-vcs-with-dids-a4176fb5ba3f) Transmute

This weekend I worked on making a [github action](https://github.com/features/actions) that can sign and verify verifiable credentials with decentralized identifiers.
* [@AnastasiaU · Apr 25](https://twitter.com/AnastasiaU/status/1518568893970894848)

8/ Animo ([@AnimoSolutions](https://twitter.com/AnimoSolutions) is DID/VC provider working on systems and infrastructure for SSI. They built this Aries CLI so you can play around and create invitations, schemas, and credentials.

* [https://agent-cli.animo.id/](https://agent-cli.animo.id/)

* [@mfosterio · Apr 29](https://twitter.com/mfosterio/status/1520130657468440576) Twitter

I created a DID at [http://GoDiddy.com](https://t.co/QhwQhqUz0k) did:key:z6MkfxFPD3vwny367HZVQoqUnKatH4RTHEitcbEdvxst3nZm#z6MkfxFPD3vwny367HZVQoqUnKatH4RTHEitcbEdvxst3nZm DIDs are important in Self Sovereign Identity. You can learn about DIDs [@bluesky_commons](https://twitter.com/bluesky_commons)
* [What does it take to develop human-centric solutions for the built environment?](https://mydata.org/2022/05/13/built-for-people/) MyData ([Video](https://www.youtube.com/watch?v%3DVCjW0_NAPmQ)

Building better, more human-centric solutions in smart cities starts by realising that citizens and their digital footprints are not merely aspects to monitor and evaluate. They are active participants in the cities we live and work together and need to be engaged in designing better cities and managing the data about themselves. This is not important only for respecting citizens’ rights, but it is crucial to building sustainable services and humane cities.
* [Scale Your Decentralized Identity Solution by Upgrading to the Indy DID Method](https://indicio.tech/scale-your-decentralized-identity-solution-by-upgrading-to-the-indy-did-method/) Indicio

Again, the Indy DID Method is not an optional upgrade. It’s a major development that delivers interoperability.

* [Semantic Overlay Architecture](https://www.ownyourdata.eu/en/semantic-overlay-architecture/) Own Your Data

We have documented the [functionality of SOyA](https://ownyourdata.github.io/soya/) in a W3C-conforming Specifiation and the full source code is available under the MIT License [on Github](https://github.com/OwnYourData/soya/). Examples and an introduction how to use SOyA is [available in a dedicated Tutorial](https://github.com/OwnYourData/soya/blob/main/tutorial/README.md)

* [An Introduction to Verifiable Credentials](https://verifiablecredential.io/learn) VerifiableCredential.io

Learn about verifiable credentials, then head to the playground to view examples, explore multiple use-cases and start using them.
* [Open Recognition is for every type of learning](https://blog.weareopen.coop/open-recognition-is-for-every-type-of-learning-ffd137a6fe17) From cold hard credentialing to warm fuzzy recognition

we want to explain what we talk about when we talk about Open Recognition. It builds on this [previous post](https://blog.weareopen.coop/what-is-open-recognition-anyway-9f38ec1f8629), and aims to move from the abstract to practicalities.


* [Self Sovereign Identity (SSI) at T-Systems MMS: Interview mit Mujtaba Idrees, T-Systems MMS](https://www.youtube.com/watch?v%3DA311QHASy5Y) 7min video on YouTube

► Dr. Ivan Gudymenko, Subject Matter Lead SSI and Confidential Computing, T-Systems MMS

►Mujtaba Idrees, Advanced Software Engineer, T-Systems MMS

► [Credentials as a Service Providing Self Sovereign Identity as a Cloud Service Using Trusted Execution Environments](https://ieeexplore.ieee.org/document/9610297)



Updates on Kepler including implementing support for [CACAO-ZCAPs](https://github.com/spruceid/cacao-zcap), improved the `put` function to make it easier to store objects of different types, and added support for listing objects by prefix: [kepler-sdk#40](https://github.com/spruceid/kepler-sdk/pull/40) [kepler#115](https://github.com/spruceid/kepler/pull/115).

* [EBSI Demo Day](https://ec.europa.eu/digital-building-blocks/wikis/display/EBSI/EBSI%2BDemo%2BDay) ([presentation](https://ec.europa.eu/digital-building-blocks/wikis/download/attachments/464979566/EBSI_Demo_Day.pdf)) ([video playlist](https://www.youtube.com/playlist?list%3DPLPMb0otsCuFLpE4UYiAZ_y3HhP2VX6q8O)

first time since the launch of [the Early Adopters Programme](https://ec.europa.eu/digital-building-blocks/wikis/x/DABXGw) in 2021, we are ready to showcase, in real-time and with real data, the outcomes of the EBSI multi-university pilot.
* [Engineer your world this summer: K-University student + teacher opportunities are live!](https://kidoyo.com/join) KidOYO

Whether a beginning learner, or interested in advanced concepts like Game Development, Hardware Prototyping, or Competitive Coding, you will find tools, lessons and mentors


* [Upgradeable Decentralized Identity - DID Method Traits](https://blog.spruceid.com/upgradeable-decentralized-identity/) SpruceID

DID method traits are testable properties about DID methods that can help implementers tame complexity and choose the right DID method(s) for their use case.

* [Indexing and Querying Revoked Verifiable Credentials](https://medium.com/51nodes/indexing-and-querying-revoked-verifiable-credentials-e229dc2781d4) 51 Nodes

this article describes a simple approach to revoke verifiable credentials and a decentralized and efficient way to index and query those revoked credentials using the [Graph protocol](https://thegraph.com/en/).

We consider the knowledge of Self-Sovereign Identity (SSI) and rudimentary knowledge of the [Ethr DID method](https://github.com/decentralized-identity/ethr-did-resolver/blob/master/doc/did-method-spec.md) as a requirement for understanding this article.



* [Keep Badges Weird is about breaking boundaries: How the KBW community is convening systems](https://blog.weareopen.coop/keep-badges-weird-is-about-breaking-boundaries-42afb0415826) WeAreOpenCoop

KBW helps people understand the badge landscape. The community is there to provide solidarity for badge champions and newbies. We do not assume prior knowledge of Open Badges or Verifiable Credentials. We recognise and celebrate those who can share their experience. Anyone interested in badges or integrating [Open Recognition](https://blog.weareopen.coop/what-is-open-recognition-anyway-9f38ec1f8629) are welcome to join.

* [chapi.io launches, includes VC playground](https://lists.w3.org/Archives/Public/public-credentials/2022Jun/0055.html) Manu Sporny CCG

TL;DR: chapi.io is a site that helps developers integrate Verifiable Credential issuance, holding, and presentation into their applications. It includes a playground that can issue arbitrary VCs to digital wallets (web and native). It also includes tutorials on how Web Developers can add CHAPI integration to their websites. All you need to try it out is a web browser.

Interoperability

* [JFF & VC-EDU Plugfest #1: Leaping Towards Interoperable Verifiable Learning & Employment Records](https://kayaelle.medium.com/jff-vc-edu-plugfest-1-892b6f2c9dfb) Kayaelle

With this badge, they qualify to participate in Plugfest #2 which will focus on issuing and displaying LER VCs. Plugfest #2 will take place in November 2022 with plans to meet in person the day before the [Internet Identity Workshop](https://internetidentityworkshop.com/) on November 14 in Mountainview, CA. If vendors are interested in Plugfest #2 and didn’t participate in Plugfest #1, there is still an opportunity to do so by fulfilling the same requirements listed above including the video and earning a Plugfest #1 badge.



OpenID Specs Up for Review

* [Public Review Period for Second Proposed RISC Profile Implementer’s Draft](https://openid.net/2022/07/05/public-review-period-for-second-proposed-risc-profile-implementers-draft/)

This specification defines event types and their contents based on the [SSE Framework](https://openid.net/specs/openid-risc-profile-specification-1_0-02.html%23SSE-FRAMEWORK) that are required to implement Risk Incident Sharing and Coordination.

* [Public Review Period for Proposed Final OpenID Connect Logout](https://openid.net/2022/07/05/public-review-period-for-proposed-final-openid-connect-logout-specifications/)

Unless issues are identified during the review that the working group believes must be addressed by revising the drafts, this review period will be followed by a seven-day voting period during which OpenID Foundation members will vote on whether to approve these drafts as OpenID Final Specifications.

* [Using a Theory of Justice to Build a Better Web3](https://www.windley.com/archives/2022/05/using_a_theory_of_justice_to_build_a_better_web3.shtml) Phil Windley

Summary: Building a better internet won't happen by chance or simply maximizing freedom. We have to build systems that support justice. How can we do that? Philosophy discussions are the black hole of identity. Once you get in, you can't get out. Nevertheless, I find that I'm drawn to them

* [Common Digital Identification Project Anonymous authentication system using Absolute Identifier & Decentralized OTP](https://www.sec.gov/comments/s7-07-22/s70722-20117318-268533.pdf)

* [Introducing Noir: The Universal Language of Zero-Knowledge](https://medium.com/aztec-protocol/introducing-noir-the-universal-language-of-zero-knowledge-ff43f38d86d9) Aztec Network

Noir is a Rust-based domain specific language (DSL) for creating and verifying zero-knowledge proofs. It’s the easiest way to write zk applications that are compatible with any proving system.

* [Spruce Developer Update #24](https://blog.spruceid.com/spruce-developer-update-24/)

- We recently added support for EIP-1271 (smart contract wallets) on our Python library ([siwe-py #30](https://github.com/spruceid/siwe-py/pull/30).
- There is ongoing work on supporting EIP-1271 in our Rust library as well, along with an API refactor ([siwe-rs #43](https://github.com/spruceid/siwe-rs/pull/43).
- We're updating dependencies in our NextAuth library ([siwe-next-auth-example #9](https://github.com/spruceid/siwe-next-auth-example/pull/9), [#14](https://github.com/spruceid/siwe-next-auth-example/pull/14)).
- We're finalizing various improvements to our Sign-In with Ethereum TypeScript library toward a v2.1 release.
* [...]
- We're adding support for did:jwk into ssi ([ssi #466](https://github.com/spruceid/ssi/pull/466).
- We've updated DIDKit to reflect the recent ssi refactor ([DIDKit #312](https://github.com/spruceid/didkit/pull/312).

Rebase

- We're making some additional changes and finalizing our Solana wallet flow ([rebase #32](https://github.com/spruceid/rebase/pull/32).