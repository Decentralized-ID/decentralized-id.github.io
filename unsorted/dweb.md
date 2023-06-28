---
published: false
---

# Decentralized Web

* [Signing HTTP Messages](https://justinsecurity.medium.com/signing-http-messages-962510d65895) Justin Richer

It’s time to start implementing it and testing it out with applications of all stripes, and I invite all of you to join me in doing just that.
* [Simon Wilson writes about using IndieAuth with Datasette](https://simonwillison.net/2020/Nov/18/indieauth/)
  > IndieAuth is a spiritual successor to OpenID, developed and maintained by the IndieWeb community and based on OAuth 2. This weekend I attended IndieWebCamp East Coast and was inspired to try my hand at an imPplementation. datasette-indieauth is the result, a new plugin which enables IndieAuth logins to a Datasette instance.

* [@ProtoResearch](https://twitter.com/ProtoResearch) [Protocol Labs Research](https://twitter.com/ProtoResearch)

Looking to improve the DWeb? Take a look at our RFP-013: "Cryptonet Network Grants" and how you can be awarded up to $35,000 USD for solving research problems regarding cryptography: [https://grants.protocol.ai/prog/rfp-013_cryptonet_network_grants/](https://grants.protocol.ai/prog/rfp-013_cryptonet_network_grants/)

* [Social.Network, a decentralized alternative to traditional social media that gives its users ownership of their identity and digital assets, to launch first phase of its protocol on April 22nd](https://financialpost.com/globe-newswire/social-technologies-announces-launch-of-the-social-network-a-decentralized-platform-designed-to-transform-the-future-of-social-media-social-network-a-decentralized-alternative-to-traditional-social)
  > interested users will be able to create a self-sovereign identity on the platform by following the steps on the [social.network](https://t.co/xRbWzSrZQf) landing page (h/t [@SelfSovID](https://twitter.com/SelfSovID)
* [How to Sign Users In with IndieAuth](https://aaronparecki.com/2021/04/13/26/indieauth) Aaron Parecki 2021-04-13
  > IndieAuth is an extension of OAuth 2.0 that enables an individual website like someone's WordPress, Gitea or OwnCast instance to become its own identity provider. This means you can use your own website to sign in to other websites that support IndieAuth.

* [Credentials and HTTP-Sig authentication for Solid](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0029.html) Henry Story
  > Here is an extended version of the HTTP-Signature document I put together today, bringing in ideas that have emerged thinking about this over the past 3 months

* [IndieAuth Spec Updates 2020 by Aaron Parecki](https://aaronparecki.com/2020/12/03/1/indieauth-2020) 2020-12-03
  > This year, the IndieWeb community has been making progress on iterating and evolving the IndieAuth protocol. IndieAuth is an extension of OAuth 2.0 that enables it to work with personal websites and in a decentralized environment.
* [Secure Scuttlebutt Intro](https://iiw.idcommons.net/9A/_Secure_Scuttlebutt_Intro) by Charles E. Lehner

directed participants to website [https://scuttlebutt.nz/](https://scuttlebutt.nz/) and to the download page [https://scuttlebutt.nz/get-started/](https://scuttlebutt.nz/get-started/)

Participants downloaded an SSB app: Patchwork and/or Manyverse.

Convener introduced the concepts of SSB Rooms and Pubs, and proposed using Rooms for onboarding, referring to a public list of SSB rooms:

* [https://github.com/ssbc/ssb-server/wiki/#ssbrooms](https://github.com/ssbc/ssb-server/wiki/#ssbrooms)

* [https://ssbc.github.io/scuttlebutt-protocol-guide/](https://ssbc.github.io/scuttlebutt-protocol-guide/)

* [Kepler: Permissioned Replicated Storage for Decentralized Applications](https://iiw.idcommons.net/12J/_Kepler:_Permissioned_Replicated_Storage_for_Decentralized_Applications) by Charles Cunningham, Wayne Chang

Slides: [https://docs.google.com/presentation/d/1_oaVcx2IEbUEr9I-23Fd1e9ZMkIYtxpJe76zYq1oVZE/edit?usp=sharing](https://docs.google.com/presentation/d/1_oaVcx2IEbUEr9I-23Fd1e9ZMkIYtxpJe76zYq1oVZE/edit?usp=sharing)

* [Decentralized publication, micro-publication and moderation-- what the real pitfalls would be.](https://iiw.idcommons.net/24L/_Decentralized_publication,_micro-publication_and_moderation--_what_the_real_pitfalls_would_be.) by Kim Duffy, Juan Caballero

* [https://docs.google.com/presentation/d/1RMozl86wihBw8_rJvC97tUUjYVpTHk6aF8QOs_ng6l0/edit?usp=sharing](https://docs.google.com/presentation/d/1RMozl86wihBw8_rJvC97tUUjYVpTHk6aF8QOs_ng6l0/edit?usp=sharing)

Set-up Presentation:

- Silos and echo chambers?
- Countermeasures?
- Pink Checkmark system? Verify all accounts or continue 2-class system
- Can we still make money?
- Moderation
- Clients and API openness - on what axes will they compete? Can they compete on algos? Community curation?
- How important is authenticity? Each tweet signed?
- Editable cheeps?
- Delete cheeps?
- Mike Jones: Listening to Daniel’s ION presentation, I asked from the POV of a naïve person, what are these ION DIDs good for in the first place; his answer was
- Daniel wants identities that Twitter can’t take away from Donald Trump
- Child pornographers would also then be sovereign over their identifiers
- Kim: People select their own echo chambers
- Juan: Echo chamber / child porn dynamics have a lot in common (HBO Documentary “into the storm”)
- Erica: Social media as a way to advertise, finding markets. Want to market to people who are interested
- Small business, organic marketing, micro-commerce
- Bullying, social problems, child protection

* [...]

* [Secure Scuttlebutt Outro](https://iiw.idcommons.net/24P/_Secure_Scuttlebutt_Outro)

Secure Scuttlebutt, Decentralized Identifiers, Key Management

Dmitri expressed interest in SSB and reported using but then having lost their key (when switching/resetting devices?). Expressed Frustration (with the key recovery process). Have question, how could SSB use DIDs?

Charles responded that there is a draft PR on [DID Spec Registries](https://www.w3.org/TR/did-spec-registries/) adding a SSB DID method a few days ago.

* [https://github.com/w3c/did-spec-registries/pull/291](https://github.com/w3c/did-spec-registries/pull/291)

Dmitri Z. asked about other ways other than as a DID method.

Charles said SSB could be extended to support DIDs, but this would be a breaking change, which the community doesn’t seem to want, considering SSB’s message signing format as “set in stone”.

There could be other ways, such as making a new system that uses DIDs but inherits some of SSB’s design.

* [Kizuna, a private messenger app: for one-on-one or group conversations.](https://blog.holochain.org/mini-spotlight-kizuna-a-private-messenger-app/) Holochain

empowers people to message each other completely privately, without the involvement of a central server. The app is open-source and is being developed by a non-profit group called the [Holochain Institute of Japan](https://www.hcij.org/en/).


* [The DWeb Is An Ensemble Piece - Holochain Blog](https://blog.holochain.org/the-dweb-is-an-ensemble-piece/) Holochain

I witness demos of [Social Sensemaker](https://www.youtube.com/watch?v=OaaK6oXL6Ls) and [We](https://github.com/lightningrodlabs/we), working examples of Holochain apps that help groups create healthy online social spaces to work and play in

* [How Ethereal Engine is Unleashing the Power of the Immersive Web](https://www.linkedin.com/pulse/how-ethereal-engine-unleashing-power-immersive-web-etherealengine/) Ethereal Engine

In keeping with the DWeb Camp theme, we also demonstrated how decentralized identifiers, identity web wallets, and verified credentials can be powerfully leveraged in Ethereal Engine to enable an entirely new paradigm of [frictionless portable identity](https://www.etherealengine.com/blog-posts/metaverse-for-humans) that champions user privacy and dignity.
* [Ubikom Project](https://www.ubikom.cc)

Ubikom is free, open-source email framework based on the concept of [Self-Sovereign Identity.](https://sovrin.org/faq/what-is-self-sovereign-identity/) You own your identity (which, in this case, means your private key), and all the outgoing and incoming messages are encrypted and signed by default.

* [The Decentralized Web: An Introduction](https://blog.archive.org/2022/02/15/the-decentralized-web-an-introduction/) Archive.org 2022-02-15
  > Providing that baseline of knowledge is the goal of a series of six workshops called [“Imagining a Better Online World: Exploring the Decentralized Web](https://metro.org/decentralizedweb).”
* [The Battle for the Soul of the Web](https://www.theatlantic.com/technology/archive/2022/10/internet-archive-decentralized-web-web3-brewster-kahle/671647/) The Atlantic
  > Musings from, amongst other places, Unfinished Live and DWeb Camp all written up in the Atlantic.
  > 
  > Long before the NFT boom or the Web3 backlash, an unglamorous movement was under way. Where does it stand now?
* [Prepping for DWeb Camp](https://blog.holochain.org/preparing-for-dweb-camp/) HoloChain
  > On this theme, I’m particularly interested in one event, an attempt to [map the projects that make up the DWeb](https://gitlab.com/getdweb/dweb-camp-2022/-/issues/77) and look for opportunities for interoperability. This was a [vision](https://dwebcamp2019.sched.com/event/S4vH/building-bridges-connecting-tech-stacks-for-humane-ux) I carried with me to the last DWeb Camp, and I’m hoping to see more conversations about building bridges between networks.

## Solid - Inrupt

* [TBL: Out to Remake the Digital World](https://www.nytimes.com/2021/01/10/technology/tim-berners-lee-privacy-internet.html). 2021-01-10
  > A story appeared in the NY Times about Tim Berners-Lee’s vision for the web and Solid-Inrupt that are working towards fulfilling it. The article included a quote from Kaliya, and has stirred up an active thread on the CCG mailing list.

> Others say the Solid-Inrupt technology is only part of the answer. “There is lots of work outside Tim Berners-Lee’s project that will be vital to the vision,” said Kaliya Young, co-chair of the Internet Identity Workshop, whose members focus on digital identity.
> 
> Mr. Berners-Lee said that his team was not inventing its own identity system, and that anything that worked could plug into its technology.

* [Byline: Tim Berners-Lee wants to put people in control of their personal data.](https://lists.w3.org/Archives/Public/public-credentials/2021Jan/subject.html): Michael Herman 
  > He has technology and a start-up pursuing that goal. Can he succeed?
  > - Has anyone else looked at this article?
  > - Anyone familiar with TBL’s view of Decentralized Identity?
  > - Is there anyone from the Solid project or Inrupt a member of CCG?

- A *[solid](https://lists.w3.org/Archives/Public/public-credentials/2021Jan/thread.html)* [discussion is underway](https://lists.w3.org/Archives/Public/public-credentials/2021Jan/thread.html), including this [from Kayode Ezike](https://lists.w3.org/Archives/Public/public-credentials/2021Jan/0039.html)
  > when I developed solid-vc, I was operating mostly under the threat model of compromised cryptographic keys used to sign credentials via jsonld-signatures and a compromised Solid password.*
  > 
  > I don't want to bombard you all with too much information about this project in this thread, but for now I will share the [solid-vc repo](https://github.com/kezike/solid-vc) again as well as [my RWoT9 submission](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/solid-vc.md).

