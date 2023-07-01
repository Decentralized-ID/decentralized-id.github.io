---
title: Guardianship
description: "How SSI meets the lifecycle stages (Inception, Creation, Usage and Termination) of guardianship."
excerpt: >
  Applying the developed models of guardianship, using the flexibility of Verifiable Credentials and the trusted mechanisms of sharing VCs, can provide the ability to add guardianship credentials into the travel process (or not) without breaking the existing approach and complicating the technical details defined in the Blueprint.
toc: false
layout: single
permalink: /application/guardianship/
canonical_url: "https://decentralized-id.com/application/guardianship/"
categories: ["Uses"]
tags: ["Guardianship","Delegation","Sovrin Foundation","Trust over IP"]
last_modified_at: 2023-07-02
---

## Main
* [Whitepaper] [On Guardianship in Self-Sovereign Identity](https://newsletter.identosphere.net/p/identosphere-138-new-wef-report-mef) 2023-04 Sovrin 
  > This paper, published by the Sovrin Guardianship Working Group, explores the guardianship relationship and how it fits in with the overall SSI “web of trust.” It presents risks, benefits and approaches to implementation of Guardianship for SSI use cases.
* [Let’s Go - Together!: Does international travel only ever involve independent adults?](https://trustoverip.org/blog/2021/11/24/lets-go-together/) 2021-11-24 ToIP
  > Applying the developed models of guardianship, using the flexibility of Verifiable Credentials and the trusted mechanisms of sharing VCs, can provide the ability to add guardianship credentials into the travel process (or not) without breaking the existing approach and complicating the technical details defined in the Blueprint.
* [Guardianship In Self-Sovereign Identity](http://thedinglegroup.com/blog/2020/11/30/guardianship-in-self-sovereign-identity) 2020-11-30 The Dingle Group
  > While there are long standing legal precedents and processes around the assignment, management and revocation of guardianships, these requirements were not met by existing digital identity management solutions. With SSI, this mechanism now exists.  SSI can work in conjunction with traditional identity and credential management systems while being able to integrate into existing legal processes and provides a robust mechanism for revocation.
* [Video] [Vienna Digital Identity Meetup #17](https://vimeo.com/482803989) 2020-11-23 Digital Identity from Vienna
  > Guardianship is a complex topic, with many subtleties and layers [...]  In this first event on this topic, Philippe has provided an overview of how SSI and Guardianship fit together and how SSI meets the lifecycle stages (Inception, Creation, Usage and Termination) of guardianship.

## Development
* [Common Delegation Patterns in the Verifiable Credential Ecosystem](https://kyledenhartog.com/delegation-in-verifiable-credentials/) 2021-06-22 Kyle Den Hartog
  > did you know that there are three ways in which you can utilize VCs and DIDs to enable delegation [...] look to the [ZCAP-LD data model](https://w3c-ccg.github.io/zcap-ld/) which is designed especially for these concepts.
* [Guardianship Showcase - The Sovrin Working Group Tech Requirements and Implementation Guidelines](https://iiw.idcommons.net/4G/_Guardianship_Showcase_-_The_Sovrin_Working_Group_Tech_Requirements_and_Implementation_Guidelines) 2021-05-06 John Phillips, Jo Spenser IDCommons, IIW 
  > Sovrin is looking to promote the governance process and where guardianship fits in. The IdRamp wallet is an example of how the wallet could provide helpful features. 
  * [Guardianship, SSI, and the Sovrin Guardianship WG - Update for IIW #32](https://docs.google.com/presentation/d/1aGTPmlno3WScpSYMs1HLhWsrVRx9B-I0yhOQsRgmqRw/edit?usp=sharing)
    > 1. Jurisdictions are essential [to Guardianship]
    > 2. Work with existing laws
    > 3. Build Guardianship on Verifiable Credentials
    > 4. Build a mental model
    > 5. Don’t build Guardianship [solely] on wallets
* [Identity Escrow - Accountability AND Privacy](https://iiw.idcommons.net/11I/_Identity_Escrow_-_Accountability_AND_Privacy) 2021-05-06 Sam Curren, Ken Ebert, Suresh Batchu, Kiran Addepalli
  > 1. Can the escrow hold the "Proof of the information" as opposed to the information itself.
  > 2. Mortgage Service - might seem to be an authorization to access the data directly or the issuer present directly.
  > 3. What gets put into escrow is flexible.
  > 4. Trigger event or a lockbox kind of capability. How is the claim released to relying parties? How does it eliminate mischief and false claims.
  > 5. There needs to be some accountability on the service provider to claim false releases. Automation may not be able to completely eliminate false triggers, some level of human intervention for complex cases.
* [Why you know less about Guardianship than you think (because we ALL know less about Guardianship than we think)](https://iiw.idcommons.net/20L/_Why_you_know_less_about_Guardianship_than_you_think_(because_we_ALL_know_less_about_Guardianship_than_we_think)) 2021-05-06 Jo Spencer, John Phillips, Sterre den Breeijen [presentation](https://docs.google.com/presentation/d/1aGTPmlno3WScpSYMs1HLhWsrVRx9B-I0yhOQsRgmqRw/edit?usp=sharing)
  > 1. In 2019 the Sovrin Foundation published a whitepaper on Guardianship; transitioned into the Working Group
  > 2. APAC and NA/EMEA WG meetings
  > 3. 2 key documents from the WG are going to be published by Sovrin Foundation - [https://sovrin.org/a-deeper-understanding-of-implementing-guardianship/](https://sovrin.org/a-deeper-understanding-of-implementing-guardianship/)
  > 4. Implementation guidelines
  > 5. Technical requirements
  > 6. Why are we looking at Guardianship and SSI?
  > 7. Guardianship is a part of life - we are rarely fully self-sovereign or independent
  > 8. Guardianship is not a part of SSI at this moment - is a missing ingredient in our digital lives
  > 9. The group thought guardianship was a simple concept
  > 10. Small set of SSI building blocks …
  > 11. Gap between use cases and requirements was too broad (see slides)
  > 12. A mental model for guardianship was required (see IIW30 and IIW31 for further context)
* [A Deeper Understanding of Implementing Guardianship](https://sovrinid.medium.com/a-deeper-understanding-of-implementing-guardianship-9a8ab749db90)  2021-04-22 Sovrin Foundation 
  > The first paper is called the [Guardianship Credentials Implementation Guidelines](https://drive.google.com/file/d/1vBePVx8n3MRDWcePkwVDya9ab4BHEyU_/view?usp=sharing) and its purpose is to provide readers with the background they need to implement IT systems that support various kinds of guardianship. [...]\
  > The second paper is called [Guardianship Credentials Technical Requirements](https://drive.google.com/file/d/1M21PznPAd0H6z1t4ODl-jiEoXZjEhwcb/view?usp=sharing) which was developed by the technical requirements working group within the SGWG. The purpose of this document is twofold: i) provide principles under which guardianship scenario designs and requirements are considered and defined; and ii) provide technical requirements for SSI solutions that offer the capability of guardianship.
* [The Sovrin Working Group Tech Requirements and Implementation Guidelines](https://docs.google.com/presentation/d/1aGTPmlno3WScpSYMs1HLhWsrVRx9B-I0yhOQsRgmqRw/edit?usp=sharing) 2021-04-20 John Phillips, Jo Spenser
  > Sovrin is looking to promote the governance process and where guardianship fits in.  The IdRamp wallet is an example of how the wallet could provide helpful features.

## Literature
* [Practical Verifiable Encryption and Decryption of Discrete Logarithms](https://link.springer.com/chapter/10.1007/978-3-540-45146-4_8) 2003 Jan Camenisch & Victor Shoup 
  > This is the first verifiable encryption system that provides chosen ciphertext security and avoids inefficient cut-and-choose proofs. The presented protocols have numerous applications, including key escrow, optimistic fair exchange, publicly verifiable secret and signature sharing, universally composable commitments, group signatures, and confirmer signatures.
