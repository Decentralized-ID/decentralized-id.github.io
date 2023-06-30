---
title: The Decentralized Web and Self Sovereign Identity
published: false
---

## General

* [The Decentralized Web: An Introduction](https://blog.archive.org/2022/02/15/the-decentralized-web-an-introduction/) 2022-02-15 Archive.org 
  > Providing that baseline of knowledge is the goal of a series of six workshops called [“Imagining a Better Online World: Exploring the Decentralized Web](https://metro.org/decentralizedweb).”
* [The DWeb Is An Ensemble Piece - Holochain Blog](https://blog.holochain.org/the-dweb-is-an-ensemble-piece/) 2022-09-19 Holochain
  > I witness demos of [Social Sensemaker](https://www.youtube.com/watch?v=OaaK6oXL6Ls) and [We](https://github.com/lightningrodlabs/we), working examples of Holochain apps that help groups create healthy online social spaces to work and play in
* [The Battle for the Soul of the Web](https://www.theatlantic.com/technology/archive/2022/10/internet-archive-decentralized-web-web3-brewster-kahle/671647/) 2022-10 The Atlantic
  > Musings from, amongst other places, Unfinished Live and DWeb Camp all written up in the Atlantic.
  > 
  > Long before the NFT boom or the Web3 backlash, an unglamorous movement was under way. Where does it stand now?

## Technique
* [Signing HTTP Messages](https://justinsecurity.medium.com/signing-http-messages-962510d65895) 2021-05-05 Justin Richer
  > A recent move towards consistency has been the adoption of Structured Field Values for HTTP. In short, structured fields allow HTTP headers to house simple, non-recursive data structures with unambiguous parsing and deterministic serialization. These aspects made it perfect for use within the HTTP message signatures specification.

## Application
* [Kizuna, a private messenger app: for one-on-one or group conversations.](https://blog.holochain.org/mini-spotlight-kizuna-a-private-messenger-app/) 2022-07-19 Holochain
  > empowers people to message each other completely privately, without the involvement of a central server. The app is open-source and is being developed by a non-profit group called the [Holochain Institute of Japan](https://www.hcij.org/en/).

## Solid - Inrupt

* [TBL: Out to Remake the Digital World](https://www.nytimes.com/2021/01/10/technology/tim-berners-lee-privacy-internet.html). 2021-01-10
  > A story appeared in the NY Times about Tim Berners-Lee’s vision for the web and Solid-Inrupt that are working towards fulfilling it. The article included a quote from Kaliya, and has stirred up an active thread on the CCG mailing list.
  > 
  > > Others say the Solid-Inrupt technology is only part of the answer. “There is lots of work outside Tim Berners-Lee’s project that will be vital to the vision,” said Kaliya Young, co-chair of the Internet Identity Workshop, whose members focus on digital identity.
  > 
  > Mr. Berners-Lee said that his team was not inventing its own identity system, and that anything that worked could plug into its technology.
* [Byline: Tim Berners-Lee wants to put people in control of their personal data.](https://lists.w3.org/Archives/Public/public-credentials/2021Jan/subject.html): Michael Herman 
  > He has technology and a start-up pursuing that goal. Can he succeed?
  > - Has anyone else looked at this article?
  > - Anyone familiar with TBL’s view of Decentralized Identity?
  > - Is there anyone from the Solid project or Inrupt a member of CCG?
  > - A *[solid](https://lists.w3.org/Archives/Public/public-credentials/2021Jan/thread.html)* [discussion is underway](https://lists.w3.org/Archives/Public/public-credentials/2021Jan/thread.html), including this [from Kayode Ezike](https://lists.w3.org/Archives/Public/public-credentials/2021Jan/0039.html)
  > when I developed solid-vc, I was operating mostly under the threat model of compromised cryptographic keys used to sign credentials via jsonld-signatures and a compromised Solid password.*
  > 
  > I don't want to bombard you all with too much information about this project in this thread, but for now I will share the [solid-vc repo](https://github.com/kezike/solid-vc) again as well as [my RWoT9 submission](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/topics-and-advance-readings/solid-vc.md).
* [Credentials and HTTP-Sig authentication for Solid](https://lists.w3.org/Archives/Public/public-credentials/2021Feb/0029.html) 2021-02 Henry Story
  > Here is an extended version of the HTTP-Signature document I put together today, bringing in ideas that have emerged thinking about this over the past 3 months

## IndieAuth
* [Simon Wilson writes about using IndieAuth with Datasette](https://simonwillison.net/2020/Nov/18/indieauth/) 2020-11-18
  > IndieAuth is a spiritual successor to OpenID, developed and maintained by the IndieWeb community and based on OAuth 2. This weekend I attended IndieWebCamp East Coast and was inspired to try my hand at an imPplementation. datasette-indieauth is the result, a new plugin which enables IndieAuth logins to a Datasette instance.
* [How to Sign Users In with IndieAuth](https://aaronparecki.com/2021/04/13/26/indieauth) 2021-04-13 Aaron Parecki
  > IndieAuth is an extension of OAuth 2.0 that enables an individual website like someone's WordPress, Gitea or OwnCast instance to become its own identity provider. This means you can use your own website to sign in to other websites that support IndieAuth.
* [IndieAuth Spec Updates 2020 by Aaron Parecki](https://aaronparecki.com/2020/12/03/1/indieauth-2020) 2020-12-03 Aaron Parecki
  > This year, the IndieWeb community has been making progress on iterating and evolving the IndieAuth protocol. IndieAuth is an extension of OAuth 2.0 that enables it to work with personal websites and in a decentralized environment.
