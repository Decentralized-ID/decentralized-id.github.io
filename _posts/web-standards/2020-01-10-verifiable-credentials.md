---
title: Verifiable Credentials
tags: ["W3C", "CCG","VC-WG"]
categories: ["Web Standards"]
permalink: /specs-standards/verifiable-credentials/
redirect_from: /web-standards/verifiable-credentials/
last_modified_at: 2020-01-10
---

[![IIW26 Primer On DIDs and VCs](/images/iiw-verifiable-credentials.png)](https://docs.google.com/presentation/d/1GMQy4rI093c_9zojwLRgp2r-fTscpDUSfX-wqwBk4j4/edit#slide=id.g3605fe1474_2_0)
  > A new type of globally resolvable, cryptographically-verifiable identifier, registered directly on a distributed ledger (aka Blockchain)

* [A Gentle Introduction to Verifiable Credentials](https://www.evernym.com/blog/gentle-introduction-verifiable-credentials/)
  > But while digital records are nothing new, today’s credentials come with certain ‘cryptographic superpowers’ that make them tamperproof, secure, and verifiable. Whereas a simple digital copy of a car title can easily be edited, a verifiable digital credential is one that has been issued by a trusted authority for, and only for, its holder.
* [Categorizing Verifiable Credentials - Evernym](https://www.evernym.com/blog/categorizing-verifiable-credentials/)
Not all verifiable credentials are created the same. This post examines the categories of credentials and the architectural choices driving this variation.
* [A Verifiable Credentials Primer](https://github.com/WebOfTrustInfo/rwot7-toronto/blob/master/topics-and-advance-readings/verifiable-credentials-primer.md)
  > NOTE: "Verifiable Claims" are now known as "Verifiable Credentials". The W3C Verifiable Claims Working Group's experience with using the term "Verifiable Claims" demonstrated that it led to confusion in the marketplace. The group has since found consensus in shifting to use the term "Verifiable Credentials", which contain "Claims".

[![](https://i.imgur.com/S6ULDcB.png)](https://drive.google.com/file/d/1kJCDF_JcRihUQ5uRFbo47dEJPFsQB7FD/view)

* [Verifiable Credential Exchange](https://www.windley.com/archives/2018/12/verifiable_credential_exchange.shtml)
  > Multi-source identity (MSI) depends on issuing, exchanging, and verifying digital credentials. The specification for verifiable credentials is being formulated by the World Wide Web Consortium’s Verifiable Credentials Working Group. Verifiable credentials provide a standard way to express credentials in a way that is cryptographically secure, privacy respecting, and automatically verifiable.
* [Verifiable Claims Task Force Use Cases](https://opencreds.org/specs/source/use-cases/)
* [2018 Texas Bitcoin Conference in Austin, Texas.](https://www.youtube.com/watch?v=uDqLYv379gI)
  > 13:14 what if I was would like to prove that I had a certain diploma man if the university would basically state that I have a certain diploma because I asked them to and if they put the proof basically the fingerprint of that claim onto the blockchain then I can prove I am I have that certain diploma but why would I trust that because if I would say I have the diploma but you still have the same problem as we had using a scan the reason why you can trust it is because it was actually the university signing off on the fact that I have a certain diploma and how does that work in the end you will need those decentralized identifiers I talked about earlier to make sure that every piece of information on the blockchain is you are able to validate those and you are able to retrieve if you'd like the underlying data off chain
* [Intro to Verifiable Cliams by W3C VCWG Members -iiw.idcommons.net](http://web.archive.org/web/20171228060921/http://iiw.idcommons.net/2J/_Intro_to_Verifiable_Cliams_by_W3C_VCWG_Members)


## Application

* [SolidVC : a decentralized framework for Verifiable Credentials on the web](https://dspace.mit.edu/handle/1721.1/121667)
  > Credentials are an integral part of our lives, as they express our capabilities and enable access to restricted services and benefits. In the early 2010s, the Verifiable Claims Working Group of the World Wide Web Consortium (W3C) proposed a specification for what is now the Verifiable Credentials Data Model. This living specification, which is still in development, outlines a cogent framework for the issuance, storage, presentation, and verification of credentials on the Web. Many of the leading Verifiable Credentials projects leverage Distributed Ledger Technology (DLT), potentially compromising Web interoperability and sometimes exposing otherwise personal data. SolidVC is a decentralized Verifiable Credentials platform built with the open protocols of the Web. It is implemented on top of Solid, a Web framework developed at MIT in 2016 that allows decentralized applications to interact with personal user data to provide services in an access controlled environment.
* [Blockcerts V3 Proposal - Verifiable Credentials & Decentralized Identifiers](https://community.blockcerts.org/t/blockcerts-v3-proposal-verifiable-credentials-decentralized-identifiers/2221)
  > As the standards around Verifable Credentials are starting to take form, diferent favors of "verifable credentials-like" data structures need to make necessary changes to leverage on the rulesets outlined and constantly reviewed by knowledgeable communities such as the W3C. The purpose of this paper is to identify all of the changes needed for Blockcerts to comply with the Verifable Credentials (VCs) and Decentralized Identifers (DIDs) standards and to expand upon the additional benefts of using a blockchain in combination with Verifable Credentials. This paper is meant to act as an explainer in which a formal specifcation can be created. This paper proposes multiple implementation options for several properties. The intention is that we can engage the Blockcerts / Verifable Credential communities and see what fts best.
* [mattr.global/Verifiable Credential based Authentication via OpenID Connect](https://mattr.global/verifiable-credential-based-authentication-via-openid-connect/)
  * [bcgov/vc-authn-oidc](https://github.com/bcgov/vc-authn-oidc)
    > Verifiable Credential Authentication with OpenID Connect (VC-AuthN OIDC)
* [Full-text Search for Verifiable Credential Metadata on Distributed Ledgers](https://arxiv.org/abs/1909.02895)
* [Blockstack and Verifiable Credentials - Paris P2P Festival](https://p2p.paris/gen/attADzQJ92rNIv6B3-Blockstack_and_Verifiable_Credentials_-_Paris_P2P_Festival_.pdf)
* [Enabling Decentralised Identifiers and Verifiable Credentials for Constrained IoT Devices using OAuth-based Delegation](https://www.ndss-symposium.org/wp-content/uploads/diss2019_05_Lagutin_paper.pdf)
  > Abstract—Decentralised identifiers (DIDs) and verifiable credentials (VCs) are upcoming standards for self-sovereign privacypreserving identifiers and authorisation, respectively. This focus on privacy can help improve many services and open up new business models, but using DIDs and VCs directly on constrained IoT devices can be problematic due to the management and resource overhead. This paper presents an OAuth-based method to delegate the processing and access policy management to the Authorisation Server thus allowing also systems with constrained IoT devices to benefit from DIDs and VCs.
* [W3C Verifiable Credentials - Kent Branch](https://www.bcs.org/events/2019/october/w3c-verifiable-credentials-kent-branch/) - [pdf](https://cdn.bcs.org/bcs-org-media/4653/kent-w3c-verifiable-credentials-031019.pdf)
  > The speaker will introduce the W3C Verifiable Credentials Data Model, which was published as a Proposed Recommendation in September 2019. Verifiable Credentials are the latest development in identity management and are fundamentally different from today's federated identity management systems such as SAML and OpenID Connect.
  > 
  > David will describe the VC ecosystem and data model. He will then describe the prototype implementation which was built with colleagues from the University of Toulouse. They built a prototype system, which uses Fast Identity Online (FIDO) for user authentication, meaning that usernames and passwords are no longer needed. A pilot application was tested with a small sample of NHS patients and the speaker will present the results of this trial.
* [IBM Verify Credentials](https://docs.info.verify-creds.com)
  > With IBM Verify Credentials and our alpha components, you can begin your journey of exploring the benefits of decentralized identity. We have provided an interactive experience centered around the challenge of proving your identity while opening a financial account. Additionally, we will walk you through the development of your first end-to-end decentralized identity solution.
* [Verifiable credentials and libp2p](https://discuss.libp2p.io/t/verifiable-credentials-and-libp2p/206)
  > Hi - we’re looking into libp2p as a network stack for our application and exploring how we could integrate verifiable credentials (https://w3c.github.io/vc-data-model/ 2) infrastructure. A basic use case is that of a node being challenged to provide some specific credential to join the network. The bootstrap node handling the incoming connection should verify the credential with the issuer and complete the connection/bootstrap or terminate it.
* [Open Badges are Verifable Credentials](https://nbviewer.jupyter.org/github/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/open-badges-are-verifiable-credentials.pdf)
  > The Open Badges Specifcation is a vocabulary and set of protocols that describes credentials. The vocabulary can describe any achievement in terms of a common set of attributes and is most often used for educational or occupational credentials. At present in version 2.0, Open Badges defnes two verifcation methods: HostedBadge (requiring resources hosted on HTTP in specifc locations) and SignedBadge (using a JSON Web Signature, which references hosted Issuer Profle and CryptographicKey information).
  > 
  > The Blockcerts Open Badges Draft Extension introduced a verifcation method based on those used by Verifable Credentials for the specifc use case of blockchain-anchored credentials. This paper expands that work and proposes a new option that can reside alongside existing Open Badges verifcation methods.
* [OPEN BADGES ON THE BLOCKCHAIN](https://draftin.com/documents/1138961?token=hQ5q0mCHizZum8-pkDFYUZr4YFYOWMN01BPT-5uX00hAaGxYOAlgAlhyenat76hjNpTCs-CMWPI38KWn_omp0Oc)
  > This document gives an overview of the status, interesting companies and people regarding Verifiable Open Badges on the Blockchain. 
* [Addition of Proof Request/Response to a formal Verifiable Credentials specification](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/verifiable-credentials-proof-request.md)
  > The W3C Verifiable Credentials (hereafter VC) specification does not currently outline how credential data should be requested by a Verifier. This document outlines the approach taken at Workday and proposes it as an addition or companion to the VC spec.
  > 
  > At RWoT we wish to present our approach in order to get community feedback and consensus. Workday recently announced our credentialing platform and will shortly begin to issue credentials within our market verticals. We fully intend to support the community standards around credentialing and therefore wish to drive consensus in the community on a simple, standard approach for requesting and sharing VCs between a holder and verifier.
* [Workday Credentials & WayTo™ By Workday](https://credentials.workday.com/docs/overview/)
  > An issuer is any entity that wishes to relinqiush and publicly attest to the veracity of data pertaining to a user. Public attestation comes in the form of a digital signature. When an issuer offers a credential to a user, Workday Credentials cryptographically signs the data in each credential with the issuer's private key before offering it to the user. The signing key's corresponding public key is written to a public ledger and is declared as belonging to the issuer, so that anyone can use that public key to verify the signature embedded in a user's digital credentials and establish trust in a credential's authenticity.



## Code

* [Identity.com Verifiable Credential Library](https://www.npmjs.com/package/@identity.com/credential-commons)
  > This Javascript Library provides functionality around Verifiable Credentials (VC), a W3C standard. Enables Validators to issue, Credential Wallets to verify, filter and Requesters to verify credentials.
* [EDCI-Data-Model](https://github.com/european-commission-europass/EDCI-Data-Model)
  > The European Commission is developing the Europass Digital Credentials Infrastructure (EDCI) – a set of tools, services and software to support the issuance of authentic, tamper-proof digital credentials (such as qualifications and other learning achievements) across Europe. The EDCI is being developed as part of ongoing work to implement the new Europass Framework for supporting transparency of skills and qualifications in Europe.
* [gautamdhameja/substrate-verifiable-credentials](https://github.com/gautamdhameja/substrate-verifiable-credentials)
  > A minimal Substrate runtime for verifiable credentials' issuance and verification.
* [bcgov/TheOrgBook](https://github.com/bcgov/TheOrgBook)
  > A public repository of verifiable claims about organizations. A key component of the Verifiable Organization Network.

## CCG

* [Credentials Community Group](https://www.w3.org/community/credentials/) - [Website](https://w3c-ccg.github.io/) - [Mail archive](http://lists.w3.org/Archives/Public/public-credentials/)
  > The mission of the Credentials Community Group is to explore the creation, storage, presentation, verification, and user control of credentials. We focus on a verifiable credential (a set of claims) created by an issuer about a subject—a person, group, or thing—and seek solutions inclusive of approaches such as: self-sovereign identity; presentation of proofs by the bearer; data minimization; and centralized, federated, and decentralized registry and identity systems. Our tasks include drafting and incubating Internet specifications for further standardization and prototyping and testing reference implementations.
* [w3c-ccg/vc-extension-registry](https://github.com/w3c-ccg/vc-extension-registry)
REGISTRY: The Verifiable Credentials Extension Registry - w3c-ccg/vc-extension-registry
* [w3c-ccg/edu_occ_verifiable_credentials](https://github.com/w3c-ccg/edu_occ_verifiable_credentials)
WORK ITEM: Drafts and Ideas of Educational and Occupational Verifiable Credentials - w3c-ccg/edu_occ_verifiable_credentials
* [w3c-ccg/vc-examples](https://github.com/w3c-ccg/vc-examples)
WORK ITEM: Verifiable Credentials Examples. 

## VC-WG

* [W3C Verifiable Claims Working Group](https://www.w3.org/2017/vc/WG/) - [Mail Archives](https://lists.w3.org/Archives/Public/public-vc-wg/) - Technical discussion and public announcements for the Verifiable Claims Working Group
  > The mission of the Verifiable Claims Working Group (VCWG) is to make expressing and exchanging credentials that have been verified by a third party easier and more secure on the Web.
* [w3c/verifiable-claims](https://github.com/w3c/verifiable-claims)
W3C Verifiable Claims Working Group. 
* [Verifiable Credentials Data Model 1.0](https://w3c.github.io/vc-data-model/) - Expressing verifiable information on the Web - [w3c/vc-data-model](https://github.com/w3c/vc-data-model)
  > Verifiable Claims Data Model and Representations specification.
* [w3c/vc-use-cases](https://github.com/w3c/vc-use-cases)
Verifiable Claims Use Cases. 
* [Verifiable Credentials Implementation Guidelines 1.0](https://www.w3.org/TR/vc-imp-guide/) - [w3c/vc-imp-guide](https://github.com/w3c/vc-imp-guide)
  > Verifiable Claims WG - Verifiable Credentials Implementation Guidelines - w3c/vc-imp-guide
* [w3c/vc-test-suite](https://github.com/w3c/vc-test-suite)
Verifiable Claims WG Test Suite. 
  * [Verifiable Credentials Data Model Implementation Report 1.0](https://w3c.github.io/vc-test-suite/implementations/)
* [w3c/vctf](https://github.com/w3c/vctf) **Archived**
  > The Web Payments Interest Group's Verifiable Claims Task Force

## Sovrin

![](https://i.imgur.com/hpXr1Af.png)

* [https://drive.google.com/drive/u/0/folders/1UxLLugRQKuV8Mdvv_X9Y6ty4szSi5ZNU?ogsrc=32](https://drive.google.com/drive/u/0/folders/1UxLLugRQKuV8Mdvv_X9Y6ty4szSi5ZNU?ogsrc=32)

* [Verifiable Credentials 101 for SSI - Tyler Ruff - Webinar 11](http://ssimeetup.org/verifiable-credentials-101-ssi-tyler-ruff-webinar-11/)

Tyler Ruff, product manager at Evernym, will be our next guest to walk us through Verifiable Credentials in the context of Self-Sovereign Identity. He will cover how they are created, issued and shared, as well as cover some common technical questions.
