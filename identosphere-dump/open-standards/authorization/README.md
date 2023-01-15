# Authorization Protocols

* [VC HTTP Authorization Conversation](https://lists.w3.org/Archives/Public/public-credentials/2021Jun/0009.html) Adrian Gropper June 2

The diversity of our community is a plus. To begin a conversation on VC access controls, I suggest this short intro to the differences between OAuth 2.0 and GNAP:

* [https://www.ietf.org/archive/id/draft-ietf-gnap-core-protocol-05.html#name-compared-to-oauth-20](https://www.ietf.org/archive/id/draft-ietf-gnap-core-protocol-05.html#name-compared-to-oauth-20)

My goal is to arrive at a shared understanding of what would be minimum needed to support both OAuth2 and GNAP for securing access to a VC.


## oCap
- [Hygiene for a computing pandemic: separation of VCs and ocaps/zcaps](https://lists.w3.org/Archives/Public/public-credentials/2020Dec/0028.html)
    - You *could* implement zcap-ld on top of VCs…
    - However, you're actually squishing together what should be a separation of concerns in a way that will become *unhygienic*. Like a lack of proper biological hygiene, the result is sickness in our computing systems.
    - The observation of "these things seem so similar though!" is true, but you can already make that claim even if you're just looking at the linked data proofs layer. VCs and zcap-ld diverge from there for two very separate purposes: what is said, and what is done.
* [CCG Call about ZCaps and OCaps](https://w3c-ccg.github.io/meetings/2021-01-13/audio.ogg) ([minutes](https://w3c-ccg.github.io/meetings/2021-01-13/))

This week’s CCG teleconference had a great discussion about object capabilities

> Alan Karp:  I've been doing capabilities since I reinvented them in 1996 and I want to make sure we get it right, because when newbies start to use them there are plenty of mistakes that can be made
> 
> [...]
> A capability or an OCAP is an unforgeable, transferable, permission to use the thing it designates ... it combines designation with authorization

* [Building capability-based data security for Ceramic](https://blog.ceramic.network/capability-based-data-security-on-ceramic/)
  > The 3Box Labs team recently published [a new standard for creating capability containers](https://github.com/ChainAgnostic/CAIPs/pull/74) for accessing decentralized data to the [Chain Agnostic Standards Alliance](https://github.com/ChainAgnostic/CASA). Capability containers are an approach for managing advanced data security and permissions, commonly referred to as “Object Capabilities” or “OCAPs.”
- [The impact of self-sovereign identity on the cybersecurity world](https://blog.avast.com/impact-of-self-sovereign-identity-on-cybersecurity)
* [The Challenging New World of Privacy & Security](https://youtu.be/JmlvOKg_dS4?t=780) Atlanta Innovation Forum (Enterprise)
featuring folks from MSFT, GSM, and Michael Becker. The video looks at the range of risks present in managing identity assets.  Its focus is coming from the enterprise-level perspective. 

* [a few thoughts about zcaps](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0036.html) Nikos Fotiou

I was reading zcaps draft, as well as related work, mostly macaroons ([https://research.google/pubs/pub41892/](https://research.google/pubs/pub41892/).

Something that I found confusing  about capability documents is that they do not make clear the actions they concern. For example from this [](https://w3c-ccg.github.io/zcap-ld/#example-1)[https://w3c-ccg.github.io/zcap-ld/#example-1](https://w3c-ccg.github.io/zcap-ld/#example-1) it is not clear that this is a capability for "driving a car".

* [Manu Responds:](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0037.html)

We are still trying to figure out how to explain these things to people.

Capabilities-based systems are not a new concept; they're decades old at this

point. The challenge has always been in communicating why they're useful and

have a place in modern security systems.

The Encrypted Data Vault work uses zcaps, and it's there that we're trying

hard to explain to developers how to use it:

* [https://identity.foundation/confidential-storage/#introduction](https://identity.foundation/confidential-storage/#introduction)

* [The "Verifiable" Economy [was RE: a few thoughts about zcaps]](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0047.html) Michael Herman (Trusted Digital Web) (Monday, 5 April)

After ruminating on ZCAPs, VCs, DIDs, and DID Documents over Easter dinner, it occurred to me that we're on the verge of creating a model for a "verifiable" economy...

![https://www.notion.soimages/image3.png](https://www.notion.soimages/image3.png)

* [Capability Authorization-enabled Decentralized Object Model [was RE: The "Verifiable" Economy [was RE: a few thoughts about zcaps]]](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0062.html) Michael Herman (Trusted Digital Web) (Wednesday, 7 April)

I see all of this converging into a Capability Authorization-enabled Decentralized Object Model.  “More news at 11…”

![https://www.notion.soimages/image1.png](https://www.notion.soimages/image1.png)

Updates on Kepler including implementing support for [CACAO-ZCAPs](https://github.com/spruceid/cacao-zcap), improved the `put` function to make it easier to store objects of different types, and added support for listing objects by prefix: [kepler-sdk#40](https://github.com/spruceid/kepler-sdk/pull/40) [kepler#115](https://github.com/spruceid/kepler/pull/115).

* [The ezcap library](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0038.html) - Manu Sporny
  > Now might be a good time to announce some open source tooling a few of us have been working on related to zcaps that is being created to simplify the developer experience when developing with zcaps.
* [ezcap (pronounced "Easy Cap")](https://github.com/digitalbazaar/ezcap) - An easy to use, opinionated Authorization Capabilities (zcap) client library for the browser and Node.js.

## UCAN

[ucan-wg](https://github.com/ucan-wg)
* [Lightweight Credentials for Offers with UCAN](https://blog.fission.codes/lightweight-credentials-ucan/)

these are the types of use cases that we think can be created and enabled across the web as an open, interoperable standard. And some of it crosses into the work we're doing as [part of the Decentralized Identity Foundation](https://blog.fission.codes/fission-demo-day-may-2021/), too.

- [User Controlled Authorization Network](https://github.com/ucan-wg/spec/) model and how it contrasts with decentralized approaches
- APAC/ASEAN Community Call now a colloaborative initative between DIF and ToIP, launched Thursday 26th May 2022, kicking off with an IIW34 recap. ([Recording](https://us02web.zoom.us/rec/share/5FW6hVoZc1kVJiFL4NNCRZg7625h-1UsC1xCY8Mb7cLXQpO2yDW566woLoA5IZA.MUVPrrNr_k3PXxDl)
A couple weeks ago Amber Case came and spoke about “[Calm Technology](https://www.youtube.com/watch?v=Ngyfa4_NuPI)” at the TOIP Human Experience Working Group ([HXWG](https://wiki.trustoverip.org/display/HOME/Human+Experience+Working+Group)
