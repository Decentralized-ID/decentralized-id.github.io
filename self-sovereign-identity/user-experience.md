# How would self-sovereign identity work for the user?
Adapted from [A gentle introduction to self-sovereign-identity](https://bitsonblocks.net/2017/05/17/gentle-introduction-self-sovereign-identity/) by [@antonylewis](https://github.com/antonylewis). I think this could use some polishing, but this is a good start, and a good example of a basic necessary SSI explainer.

You would have an app on a smartphone or computer, some sort of “identity wallet” where identity data would be stored on the hard drive of your device, or with an agent of your choosing, but crucially not stored in a central repository.

Your identity wallet would start off empty with only a self-generated Decentralized identifier (DID).

At this stage, no one else in the world knows about this identification number. No one issued it to you. You created it yourself. It is self-sovereign. The laws of big numbers and randomness ensure that no one else will generate the same identification number as you.

You then use this identification number, along with your identity claims, and get attestations from relevant authorities.

You can then use these attested claims as your identity information.

Claims would be stored by typing text into standardised text fields, and saving photos or scans of documents.

Proofs would be stored by saving scans or photos of proof documents. However this would be for backward compatibility, because digitally signed attestations remove the need for proofs as we know them today.

Attestations – and here’s the neat bit – would be stored in this wallet too. These would be machine readable, digitally signed pieces of information, valid within certain time windows. The relevant authority would need to sign these with digital signatures – for example, passport agencies, hospitals, driving licence authorities, police, etc.

Need to know, but not more: Authorities could provide “bundles” of attested claims, such as “over 18”, “over 21”, “accredited investor”, “can drive cars” etc, for the user to use as they see fit. The identity owner would be able to choose which piece of information to pass to any requester. For example, if you need to prove you are over 18, you don’t need to share your date of birth, you just need a statement saying you are over 18, signed by the relevant authority.

Sharing this kind of data is safer both for the identity provider and the recipient. The provider doesn’t need to overshare, and the recipient doesn’t need to store unnecessarily sensitive data – for example, if the recipient gets hacked, they are only storing “Over 18” flags, not dates of birth.

Even banks themselves could attest to the person having an account with them. We would first need to understand what liability they take on when they create these attestations. I would assume it would be no more than the liability they currently take on when they send you a bank statement, which you use as a proof of address elsewhere.

Data sharing
Data would be stored on the person’s device (as pieces of paper are currently stored at home today), and then when requested, the person would approve a third party to collect specific data, by tapping a notification on their device, We already have something similar to this – if you have ever used a service by “linking” your Facebook or LinkedIn account, this is similar – but instead of going to Facebook’s servers to collect your personal data, it requests it from your phone, and you have granular control over what data is shared.

<a href="https://infominer.id"><img src="https://infominer.id/android-chrome-256x256.png" align="right" width="170" height="170"/></a>

## [infominer.id](https://infominer.id)  ([**^**](#contents))
* [github.com/infominer33/DecentralizedID](https://github.com/infominer33/DecentralizedID)
* [infominer.id/DecentralizedID/self-sovereign-identity](https://infominer.id/DecentralizedID/self-sovereign-identity)
* [infominer.id/DecentralizedID](https://infominer.id/DecentralizedID)
