---
published: false
---

# Web Standards

### IBC

https://github.com/cosmos/ibc/

## List
- aggregate well-known-did-1-of-a 1 of a (intermediate)
- aggregate did-spec-registries-1-of-a Signature Implementations 1 of many (intermediate)
- aggregate did-spec-registries-1-of-b did-method 1 of many (intermediate)


### W3C

Decentralized Identifier ✓
- Explainer ✓
- Literature +
- Methods ✓
- Tools \ Services 
- Critique ✓

Verifiable Credential 
- Explainer  ✓
- Comparisons  ✓
- Varieties
  - JSON-LD 
  - JSON-LD ZKP BBS+
  - JSON-JWT
  - ZKP-CL - [IIA] Indy Aries AnnonCreds
  - JWP

JSON-LD
- [Complementary] JSON-LD ✓ (W3C)

### Credentials Community Group

- [Exchange] CHAPI  ✓ (CCG)
- [Complementary] Cryptography > BBS ✓ (CCG)
- [Authorization] oCap/zCap ✓ (CCG)

### IETF

- [Complementary]  (IETF)
- [Authorization] GNAP ✓ (IETF)
- [Authorization] OAuth ✓ (IETF)
- [ID-Non-SSI] OAuth (IETF)
- [ID-Non-SSI] SCIM (IETF)

### OASIS

- [ID-Non-SSI] SAML (OASIS)
- [ID-Non-SSI] KMIP (OASIS)
- [ID-Non-SSI] Secure QR Code (OASIS)

### ISO/IEC
- mDL 18013-5 ✓ (ISO)
- 22030 ? 
- Working Group 3 - Travel Documents

### OpenID Foundation
- [Exchange] OIDC  ✓ (OpenID)
- [ID-Non-SSI] OpenID (OpenID)

### ISO
- [Exchange] mDL  ✓ (ISO)
- [Blockchain] ISOTC 307 ✓ (ISO)

### CEN/CENTLIC
- [Blockchain] CEN/CENTLIC ✓ (CEN)
- [Blockchain] ERC 725   (ERC-EIP)

### FIDO
- [ID-Non-SSI] FIDO (FIDO)

## VC

* [New search engine, mobile wallet, verifiable credentials and delivery technologies.](https://twitter.com/HUMBLPay/status/1574454647384813568) via Twitter ([ANN](https://www.globenewswire.com/en/news-release/2022/04/13/2421969/0/en/HUMBL-Selected-To-Pilot-Digital-Wallet-Program-On-Behalf-of-The-County-of-Santa-Cruz-California.html) 2022-04-13 HUMBL @HUMBLPay
*using verifiable credentials in their wallet.*
  > #HUMBL x GF2GO - San Diego, CA - [Pilot Program](https://www.youtube.com/watch?v=H_HAFEzmkWU) 

## DIDs
W3C Press Release - [Decentralized Identifiers (DIDs) v1.0 becomes a W3C Recommendation](https://www.w3.org/2022/07/pressrelease-did-rec) worth reading to see who contributed comments (and notice who didn’t)

For individuals in particular, DIDs can put them back in control of their personal data and consent, and also enable more respectful bi-directional trust relationships where forgery is prevented, privacy is honored, and usability is enhanced.

## DID Auth

* [SSI Interaction Patterns](https://www.windley.com/archives/2021/06/ssi_interaction_patterns.shtml)
  > While the DID Authn pattern is simple, it is not as flexible as we need in some situations. For more complicated scenarios, we can use verifiable credentials. The first scenario we’ll consider is where the same organization is issuing and verifying the credential.
  > ![](https://s3.amazonaws.com/revue/items/images/009/411/724/mail/Credential_Internal.png?1621957585)

* [The Time for Self-Sovereign Identity is Now](https://medium.com/learning-machine-blog/the-time-for-self-sovereign-identity-is-now-222aab97041b) Kim Hamilton Duffy, Learning Machine (Now Hyland Credentials)
Oldie but Goodie by Kim Hamilton Duffy from when she worked at Learning Machines
  > Technically, Verifiable Claims are claims made about a “subject” (identified by a digital identifier such as a DID) that are rendered tamper proof through digital signatures. The authenticity of digital signatures may, in turn, be established through issuer identifiers, which may also be expressed as DIDs.
* [The Verifiable Credential’s Model](https://trinsic.id/trinsic-basics-the-verifiable-credentials-model/)
  > At the core of every self-sovereign identity (SSI) use case is what we call the verifiable credentials model. This simple yet effective model helps conceptualize how verifiable credentials are exchanged between people and organizations.
* [According to](https://www.w3.org/TR/vc-data-model/) W3: "Verifiable credentials represent statements made by an issuer in a tamper-evident and privacy-respecting manner."
* [DID, in short for Decentralized Identifier, is basically a unique string of random numbers and letters](https://twitter.com/fennykyun/status/1564249472053514240) fennykyun
  > tldr\
  > :: DID is just an URI\
  > :: VC is a cryptographically verifiable credential using DID\ 
  > :: SSI is a self-sovereign and privacy-preserving identity 
  > :: Non-human (Machines, Bots, Goods, anything) also able to have DID, VC, and SSIs
