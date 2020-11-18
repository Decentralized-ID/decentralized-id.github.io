---
date: 2020-11-17
title: Dragonchain & Factor
description: "Blockchain technology for decentralized identity management"
excerpt: >
    On Factor/MyFii DID, the identity factors are decentralized to the individual owners. Individual users hold their own identity information in granular form as “factors”. Factors can be any data attributed to an individual and can be based on verifications by one or more external 3rd parties, or they can be self-declared/self-certified. These factors can then be provided to other parties needing identity verification. These factors can also be held within smart contracts with controlled and metered access.
layout: single
permalink: blockchain/dragonchain-factor/
canonical_url: 'https://decentralized-id.com/blockchain/dragonchain-factor/'
categories: ["Companies","Blockchain"]
tags: ["Dragonchain","Blockchain"]
header:
  image: /images/dragonchain-factor-header.png
  teaser: /images/dragon-teaser.png
  og_image: /images/dragon_factor_og.png
last_modified_at: 2020-11-17
toc: true
# •
---

Guest post by [Holly Jolly Jeffrey](https://twitter.com/hodldrgn) ([Linkedin](https://www.linkedin.com/in/jeffrey-neijenhuis/)) and Dragonchain Founder\CEO [Joe Roets](https://www.linkedin.com/in/j0j0r0/).{: .notice--info}

## Technology Overview 

As enterprises continuously digitize their businesses, there is an increasing need for security and trust built around digital identities. Current identification systems are siloed and enterprises are having major challenges to manage Personal Identifiable Information (PII) in an increasingly regulated environment (eg. GDPR). On top of that, privacy and control of their data is becoming a greater concern for users as well. Factor is using blockchain technology that allows users to authenticate to a website or other service with a secure cryptographic signing mechanism. No username or password will be necessary or required for the sign in process. 

Dragonchain itself provides for “protection of business data” which can also be used to protect PII/privacy data for users. We do this by stripping the business payload of every transaction before the business’ block goes to the network for verification. In Dragon Net (see Dragonchain architecture), the  proof is decentralized, not the data. This means that all transaction data may be proven in the future to explicit parties without unnecessary exposure.

### Structural approach to privacy and data protection

This separation is a structural approach to the privacy and data protection issue which does not rely on guesses of safety against unknown attack vectors in cryptographic functions. This model allows the business to use best practices devops and existing staff to protect their data.

On Dragonchain, the proof is decentralized, not the data. All transactions are verified in blocks from 5 different contexts in Context Based Verification on Dragon Net. This allows the business to decentralize or share the data as necessary for their particular business model, yet have a proofing system scaled for Enterprise.

On Factor/MyFii DID, the identity factors are decentralized to the individual owners. Individual users hold their own identity information in granular form as “factors”. Factors can be any data attributed to an individual and can be based on verifications by one or more external 3rd parties, or they can be self-declared/self-certified. These factors can then be provided to other parties needing identity verification. These factors can also be held within smart contracts with controlled and metered access.

<iframe width="560" height="315" src="https://www.youtube.com/embed/_6Mzv1CPMXQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Compatibility with W3C standards?

Factor was developed prior to W3C standardization, but we expect to provide mappings and support for W3C standards via our MyFii integration. Dragonchain and Factor are designed to be interoperable with traditional and blockchain systems. Dragonchain holds multiple interoperability and scalability patents that are employed in the Factor/DID system. The systems are literally interoperable with any other system via standard RESTful service API integration.

<br>
<img src="https://i.imgur.com/Bo1JB2V.jpg" alt="Factor decentralized identity logo" style="width:200px;"/>
<br>

### Features & Specifications 

Factor is a blockchain based identity and access solution that allows users to take control of their identity and eliminates the risk for enterprises to store PII (e.g. risk of data breaches, and GDPR compliance). Delivered as a service, built on top of the Dragonchain platform, Factor Identity authenticates users to applications using public key encryption. Third party Factor Identity Providers confirm claims or factors about a user without sharing the actual data, it de-risks the storage of PIIs associated with users and data breaches. 

This identity solution does not store personal identifiable information, instead, the hashes of the actions are recorded into our decentralized system. This makes it virtually impossible to hack all of the business data because it’s not stored in one location. It also provides better access control and management to the data. Individuals or companies can control who has the ability to view and edit data, reducing unauthorized access. 

Factor provides a better solution than what federated identity provides: businesses can manage and update a person’s consumable identity components or factors into one place. The verification process of Factor relies on third party Factor Identity Providers who are able to verify sensitive data for businesses. Factor has logic built into its system that can update their data once a Factor Identity Provider verifies the data. This can create ease and reduce costs for businesses and end users, for example in handling KYC between multiple banks for the same customer. 

### Protection against quantum attacks?

When it comes to legitimate concerns in regards to future quantum attacks, “The answer is in the architecture of the software itself. Considerations of possible Quantum compute attack are very focused on the cryptographic side of the equation. Yet, if you segregate the actual data from exposure on a public chain, the data will be structurally secure. I would never, ever, put sensitive information like customer’s personal information or military and Space Force information anywhere near an actual public blockchain, encrypted or not, as this data will be subject to all manner of attacks. The data should be segmented and separated away from exposure on a public blockchain. The proof could be affected by quantum, but if any of the many other quantum-resistant algorithms work, you can also apply those at any level.

It’s like some of the things that happened during the Cold War. Both sides would attack each other's data or systems and the other side would not know for years that this had happened. When it comes to blockchain based proof, just knowing that something was stolen or tampered with would be remarkably valuable. At the very least you would be able to measure the level of security. As an example, would my enemy spend three billion dollars to attack this particular part that I'm about to 3D print on a ship?

You can also look back and see direct evidence for simultaneous forks on Bitcoin, Ethereum, Ethereum Classic, (and every other Interchain) overlapping the block time for the transaction in question'', - Joe Roets, Dragonchain Founder & Architect explains.

## Factor benefits:

* Determine where data will be stored, including the geographic region, and allow for tighter control over jurisdictions where nodes are operated. 
* Keep data private and ensure it never leaves the private blockchain unless explicitly granted, or by including references to the underlying data (stored elsewhere) in the form of a hash value in the payload. 
* Comply with requests to be forgotten. This is accomplished by removing the underlying data (“off-chain”) reference via a hash value. 
* Filter access control to applications, providing selective exposure of specific factors. 
* Eliminate liabilities, such as the retention of PII or other sensitive data. 

### With Factor an individual user can:

* Prove you are over 21 without exposing your full Drivers License or Passport.
* Prove you reside in a particular region without exposing your address.
* Prove you have a valid email, without exposing the address.
* Replace identifiers such as a phone number or email address which were never designed to be safely used for logins

## Case Studies

### Case Study 1 - SafePass and Covid-19

In the first quarter of 2020, Dragonchain was able to partner with Medek Health Systems. The city of Apopka was looking for an application to help enable employees get back to work, as safely as possible. Medek Health Systems leveraged Dragonchain to ensure privacy and personal medical data of individuals is respected.

In the application, a medical assessment provides directions on next steps to take. Should an individual go into quarantine? Or perhaps consider getting tested or seeking medical help for having Covid-19 symptoms? After completing a questionnaire, a medical risk score is assigned to a user. Users of the application are even able to use telemedicine for Covid-19, and have access to medical professionals directly through the app. 

Every step along the way is recorded and validated on Dragonchain’s hybrid blockchain protocol. A combination of ledgering and smart contracts is used to trace the workflow, and provide proof of the pre-described workflow. The system takes into consideration new methods and tests to become available over time, making it a flexible solution. Individuals are able to proof their employee or other authority that the prescribed process has been followed. Within a matter of weeks the application was launched in the Google Play Store and the Apple App store. Medek Health Systems continues to integrate more blockchain based solutions into the application, including our decentralized identity solution Factor.

* [Learn more about SafePass](https://www.bizjournals.com/orlando/news/2020/05/15/heres-how-this-app-lets-customers-know.html)

### Case Study 2 - Decentralized Identity in Social Media

[Den](https://den.social) (social media platform) will integrate with Factor, Dragonchain’s privacy focused decentralized identity technology. Doing this allows for the verification of the identity of Denizens with controlled exposure to Den and the world. The identity system will provide protection against impersonation with cryptographically signed messages and actions. 

Lairs will be able to limit use based upon identity Factors, and will allow a community to decide whether their Lair will be made up of users that are identified, anonymous, or a mix of both. This also allows the creation of a model for an anonymous account economy.

* [Read the Den whitepaper](https://drive.google.com/file/d/1LRe0Cv7bBaSeuDO7knxDst4IQVeTfjJu/view)

## Resources

* [Learn more about Factor](https://dragonchain.com/business/factor/) 
* [Self Sovereign Identity and Decentralized Identity](https://dragonchain.com/blog/decentralized-identity-self-sovereign-identity-explained)
* [Quick Take on Decentralized Identity](https://dragonchain.com/blog/quick-take-decentralized-identity)
* [Dragonchain Spins-off Decentralized Identity Solutions and Services](https://dragonchain.com/blog/factor-spin-off-myfii)
* [Interchain™ Between Blockchains and Traditional Systems](https://dragonchain.com/blog/interchain)
* [Remain Sovereign with Blockchain Interoperability](https://dragonchain.com/blog/blockchain-interoperability)
* [Quantum computing and data protection with blockchain.](https://dragonchain.com/blog/quantum-computing-data-protection-blockchain)
* [Dragonchain architecture and whitepaper](https://dragonchain.com/Dragonchain-Architecture.pdf)

