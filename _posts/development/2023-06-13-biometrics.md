---
title: Biometrics and Self Sovereign Identity
description: "How can biometrics help improve accessibility to critical services?"
excerpt: >
  Instead of putting PII and biometrics in the same database, we need to put them in different places, but prove that there's a link between the holder of a biometric cred and the holder of other PII.
layout: single
permalink: /development/biometrics/
canonical_url: "https://decentralized-id.com/development/biometrics/"
categories: ["Technology"]
tags: ["Biometrics"]
last_modified_at: 2023-06-09
toc: true
toc_sticky: false
---

## Explainer

* [My Voice is my Password](https://stateofidentity.libsyn.com/my-voice-is-my-password) 2022-04-21 State of Identity
  > How can biometrics help improve accessibility to critical services? On this week’s State of Identity podcast, host Cameron D’Ambrosi is joined by Chief Fraud Prevention Officer for security and biometrics at Nuance, Simon Marchand. Tune in for their discussion about the cutting edge of biometric voice recognition technology, and its potential to transform identity verification and the user experience across channels.
* [Survey Finds Customers Frustrated With Passwords, Open to Biometrics](https://findbiometrics.com/survey-finds-customers-frustrated-passwords-open-biometrics-7102106/) 2021-10-14 FindBiometrics
  > Passwords were a major point of contention in that regard, with a strong majority (68 percent) of consumers indicating that it is difficult to remember and key in a large number of passwords. Nearly half (44 percent) believe that biometric authenticators are easier to use, while 34 percent would prefer to use them as their primary means of identity
* [Exploring Facial Biometrics](https://diacc.ca/2020/12/16/exploring-facial-biometrics-what-is-it/) 2020-12-16 DIACC
  > Policymakers, privacy advocates, and regulators understand that new technologies are being added to existing facial biometric matching to render leaked personal data useless and ensure that any leaked biometric data is both isolated and encrypted to reduce the impacts on individuals from an identity fraud perspective. 

## Guidance
* [Guidance on the Acceptable Use of Biometrics – DIACC Special Interest Group Insights](https://diacc.ca/2022/01/13/guidance-on-the-acceptable-use-of-biometrics/) 2022-01-13 DIACC 
  > With input from public and private sector DIACC members and liaisons, the following guidance was created as a recommendation that the DIACC’s Trust Framework Expert Committee (TFEC) agreed to consider. Specified business, legal, and technical process requirements will be identified and considered by the TFEC for inclusion in future versions of the PCTF.

## Policy
* [China’s Supreme Court Bars Use of Facial Recognition Without Consent](https://findbiometrics.com/chinese-supreme-court-bars-use-facial-recognition-without-consent-073007/) 2021-07-30 FindBiometrics
	China’s highest court has issued a ruling that could significantly limit the scope of facial recognition programs in the country. To that end, the Supreme People’s Court has stated that […] The post China’s Supreme Court Bars Use of Facial Recognition Without Consent appeared first on FindBiometrics
* [Biden Reverses Trump Order to Expand DHS’s Biometrics Collection](https://findbiometrics.com/biden-reverses-trump-order-expand-dhss-biometrics-collection-070802/) 2021-07-08 FindBiometrics
  > In a move that is likely to please privacy advocates across the country, the Biden Administration has announced that it has officially rescinded a policy proposed by the Trump Administration that [would have considerably expanded](https://findbiometrics.com/proposed-policy-would-give-dhs-sweeping-powers-collect-biometric-data-092106/) the Department of Homeland Security’s (DHS) powers to collect biometric data from immigrants.

## Standards
* [Veridium Advocates for Use of NIST-approved Contactless Fingerprint Technologies](https://findbiometrics.com/veridium-advocates-use-nist-approved-contactless-fingerprint-technologies-090305/) 2021-08-02 FindBiometrics
	Veridium is encouraging more organizations to embrace contactless fingerprint technologies, especially now that the NIST has laid out comprehensive guidelines for those interested in doing so. Those guidelines debuted in March of this year, with the release of NIST Special Publication 500-334.

## Development

* [Biometric and digital identity](https://iiw.idcommons.net/3H/_Biometric_and_digital_identity) by Robert Mitwicki / Adrian Gropper
  * [Biometric Health Card](https://docs.google.com/document/d/1o_773vzcbtSf59oU-iRUfAy5WSz3Wn9JUAvi0hKHE48/edit)
    > The novel concept is to add a quantized face that is still human-verifiable to the digital credential presentation. The hash of the quantized face, but not the face itself, would be signed and verifiable as part of the digital credential represented by the QR code.
	> ![](https://lh3.googleusercontent.com/keep-bbsk/AO8PoW1894cZwApEW68I3k8gsrknhXdz-Xhy1S4wWWLWKl_VOE0vfYaYVY_bxYBfwfy5mljlg7TfoxVEeXMooGbExE9IfcuNx2R29roOqioDE5XsZsc=s512)

## Caution
* [Face Recognition Isn’t Just Face Identification and Verification: It’s Also Photo Clustering, Race Analysis, Real-time Tracking, and More](https://www.eff.org/deeplinks/2021/10/face-recognition-isnt-just-face-identification-and-verification) 2021-10 EFF
  > All forms of face recognition are a menace to privacy, free speech, and racial justice. This post explores many of the various kinds of face recognition, and explains why all must be addressed by laws.
* [the link between biometrics and PII needs careful management](https://lists.w3.org/Archives/Public/public-credentials/2021Sep/0000.html) 2021-09-01 Daniel Hardman 
	My takeaway: Instead of putting PII and biometrics in the same database, we need to put them in different places, but prove that there's a link between the holder of a biometric cred and the holder of other PII. I see companies like iRespond doing this, but I also seem some biometric applications that are more troubling.
	* [This is the real story of the Afghan biometric databases abandoned to the Taliban - MIT Technology Review](https://www.technologyreview.com/2021/08/30/1033941/afghanistan-biometric-databases-us-military-40-data-points/) 2021-08-30
* [Afghans scramble to delete digital history, evade biometrics](https://www.context.news/surveillance/afghans-scramble-to-delete-digital-history-evade-biometrics) 2021-08-17 Context News
  > Thousands of Afghans struggling to ensure the physical safety of their families after the Taliban took control of the country have an additional worry: that biometric databases and their own digital history can be used to track and target them.
* [Sexism in Facial Recognition Technology​](https://medium.com/berkman-klein-center/sexism-in-facial-recognition-technology-d5e547a6e7bc) 2021-05-05 Berkman Klien Center
  > The use of facial recognition by law enforcement agencies has become common practice, despite increasing reports of [false arrests](https://www.nytimes.com/2020/06/24/technology/facial-recognition-arrest.html) and [jail time](https://www.nytimes.com/2020/12/29/technology/facial-recognition-misidentify-jail.html). While there are various downsides to facial recognition technology being used at all, including fears of mass surveillance and invasion of privacy, there are flaws within facial recognition technologies themselves that lead to inaccurate results. One such major challenge for this still-burgeoning technology is gender-based inaccuracies.

## Company
* [Imageware to add Biometrics to Blockchain Powered Self Sovereign Identity (SSI)](https://imageware.io/imageware-to-add-biometrics-to-blockchainpowered-self-sovereign-identity-ssi/) 2021-10-24
“As individual safety and privacy concerns become more prevalent in our daily lives, it’s vital that we have better, more decentralized methods of giving individuals autonomy over their identities. By joining the Decentralized Identity Foundation and Trust Over IP groups, we’ll be able to leverage their network and resources in our efforts to further develop a portfolio of SSI integrated biometric solutions.”

## Product
* [Biometrics come to verifiable credentials with Applied Recognition and Sovrin Foundation](https://www.biometricupdate.com/202105/biometrics-come-to-verifiable-credentials-with-applied-recognition-and-sovrin-foundation) 2021-05 Biometric Update
  > Making wallet available, with support from companies like Applied Rec supplying biometrics that people can use for free, therefore extends Sovrin’s mission of supporting SSI. The companies generous enough to donate their technology to the wallet get commercial upside from next steps of service for banks and other organizations leveraging the open-source wallet, Raczkowski says.


