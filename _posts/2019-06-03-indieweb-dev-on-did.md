---
title: "FreeNode IRC #indieweb-dev on IIW RWoT and DID's"
description: "Conversation about RWoT and DIDs at #indieweb-dev on Freenode"
date: "2019-06-03T11:22:33-23:00"
categories: ["Specs-Standards"]
tags: ["P2P", "IndieAuth","IndieWeb","Rebooting WoT", "IIW","DID"]
permalink: /specs-standards/indieweb-dev-on-did/
---

## Contents
* [Links](#links)
  * [In-Chat Links](#in-chat-links)
    * [Peer to Peer DIDs](#peer-to-peer-dids)
    * [IndieAuth](#indieauth)
* [#indieweb-dev on RWoT-DIDs 2019-03-02](#indieweb-dev-on-rwot-dids-2019-03-02)
* [#indieweb-dev on IIW 2018-08-19](#indieweb-dev-on-iiw-2018-08-19)

## Links 

* [indieweb.org/discuss#Join_Discussions](https://indieweb.org/discuss#Join_Discussions)
* [Matrix bridge to #dev channnel chat (via riot.im)](https://riot.im/develop/#/room/#freenode_#indieweb-dev:matrix.org)
* [#indieweb-dev on DIDs 2019-03-02-chat log](https://freenode.logbot.info/indieweb-dev/20190302)
* [#indieweb-dev on IIW 2018-08-19-chat log](https://freenode.logbot.info/indieweb-dev/20180819)

### Related

* [The Decentralized Identifier (DID) in the DNS](https://datatracker.ietf.org/doc/draft-mayrhofer-did-dns/)

### In-chat Links

* https://docs.ipfs.io/guides/concepts/dnslink/
  * DNSLink uses DNS TXT records to map a domain name (like ipfs.io) to an IPFS address. Because you can edit your DNS records, you can use them to always point to the latest version of an object in IPFS (remember that an IPFS object’s address changes if you modify the object). Because DNSLink uses DNS records, the names it produces are also usually easy to type and read.
  * A DNSLink address looks like an IPNS address, but it uses a domain name in place of a hashed public key:
* [indieweb.org/checkin#Posting_checkins_from_clients](https://indieweb.org/checkin#Posting_checkins_from_clients)

#### Peer-to-Peer DIDs

* [Comparing WebIDs and DIDs](https://docs.google.com/document/d/1SwSWIOOujRCdrwVyrKojwAvQVp-wJJ9P6NBiuQ3bDN4/edit)
* [Peer to Peer DIDs](https://github.com/WebOfTrustInfo/rwot8-barcelona/blob/master/topics-and-advance-readings/P2P-DID.md)
* [dhh1128.github.io/peer-did-method-spec/index.html](https://dhh1128.github.io/peer-did-method-spec/index.html)
    * [#grafting-peer-dids-into-another-did-method-namespace](https://dhh1128.github.io/peer-did-method-spec/index.html#grafting-peer-dids-into-another-did-method-namespace) 

#### IndieAuth

<iframe width="560" height="315" src="https://www.youtube.com/embed/EeCNlB7v08I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* [indieauth.spec.indieweb.org](https://indieauth.spec.indieweb.org)  
  * IndieAuth is an identity layer on top of OAuth 2.0 [RFC6749], primarily used to obtain an OAuth 2.0 Bearer Token [RFC6750] for use by [Micropub] clients. End-Users and Clients are all represented by URLs. IndieAuth enables Clients to verify the identity of an End-User, as well as to obtain an access token that can be used to access resources under the control of the End-User.  
* [W3C Working Group Note 23 January 2018](https://w3.org/TR/2018/NOTE-indieauth-20180123)
  * An IndieAuth implementation can implement one or more of the roles of an IndieAuth server or client. This section describes the conformance criteria for each role.
  * Listed below are known types of IndieAuth implementations.
  * 2.1.1 Authorization Endpoint
    * An IndieAuth Authorization Endpoint is responsible for obtaining authorization or authentication consent from the end user and generating and verifying authorization codes.
  * 2.1.2 Token Endpoint
    * An IndieAuth Token Endpoint is responsible for generating and verifying OAuth 2.0 Bearer Tokens.
  * 2.1.3 Micropub Client
    * A Micropub client will attempt to obtain an OAuth 2.0 Bearer Token given an IndieAuth profile URL, and will use the token when making Micropub requests.
  * 2.1.4 IndieAuth Client
    * An IndieAuth client is a client that is attempting to authenticate a user given their profile URL, but does not need an OAuth 2.0 Bearer Token.
* [aaronparecki.com - Oath for the Open Web](https://aaronparecki.com/2018/07/07/7/oauth-for-the-open-web)
  * OAuth has become the de facto standard for authorization and authentication on the web. Nearly every company with an API used by third party developers has implemented OAuth to enable people to build apps on top of it.
  * While OAuth is a great framework for this, the way it has ended up being used is much more centralized and closed than prior efforts like OpenID 1. Every service that spins up an OAuth-enabled API ends up being its own isolated system. For example, if I want to build an app that can read someone's step count from FitBit, I have to first go register as a developer on FitBit's website in order to get API keys to use with their OAuth API
* [indieweb/indieauth #23#issuecomment-414152219](https://github.com/indieweb/indieauth/issues/23#issuecomment-414152219)
  * 21:13 **Loqi** - [Zegnat] The table above has been updated with new statistics. This shows that `rel="manifest"` are equally as likely to be found on client pages as `h-x-app`. This Web App Manifests may be a more logical alternative than previously realised.
* [indieweb/wordpress-indieauth #127/files#diff-F81F3DFF36BF04B7A070D642C858E883](https://github.com/indieweb/wordpress-indieauth/pull/127/files#diff-F81F3DFF36BF04B7A070D642C858E883)
  * **dshanske** commented on Feb 24- Returns a jf2 h-card in the token return on verification so the client can display name and user avatar on an application

## indieweb-dev on RWoT-DIDs 2019-03-02

[![](https://imgur.com/A4IPjIi.png)](https://freenode.logbot.info/indieweb-dev/20190302)

* [#indieweb-dev on DIDs 2019-03-02-chat log](https://freenode.logbot.info/indieweb-dev/20190302)
  * 16:14 [@sandhawke](https://twitter.com/sandhawke) - I don't think I have that level of interest to attend IIW - but I happen to be at RWoT right now, and that seems like a sweet spot for me to work on while I'm here. I just made this:
  * 16:14 [@sandhawke](https://twitter.com/sandhawke) - [Comparing WebIDs and DIDs](https://docs.google.com/document/d/1SwSWIOOujRCdrwVyrKojwAvQVp-wJJ9P6NBiuQ3bDN4/edit)
  * 16:14 [@sandhawke](https://twitter.com/sandhawke) - which should perhaps have a column for IndieAuth
  * 16:15 [@sandhawke](https://twitter.com/sandhawke) -although it's not quite the same type of thing, it kina is
  * 16:15 [@sandhawke](https://twitter.com/sandhawke) -Anyway - DIDs seem to have a lot of momentum, so I'm inclined to fit webids & indieauth, which I much prefer, into the DID world
  * 16:16 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -DIDs lost me when they make the assumption that blockchains are the only resolution mechanism
  * 16:16 [@sandhawke](https://twitter.com/sandhawke) -In person everyone here denies that, and they seem to welcome other mechanisms.
  * 16:17 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -any examples yet?
  * 16:17 [@sandhawke](https://twitter.com/sandhawke) -Yes, "peer"
  * 16:17 [@sandhawke](https://twitter.com/sandhawke) -[Peer to Peer DIDs](https://github.com/WebOfTrustInfo/rwot8-barcelona/blob/master/topics-and-advance-readings/P2P-DID.md)
  * 16:18 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -Even just reading w3c-ccg.github.io/did-primer/#the-format-of-a-did-0 they casually drop a mention of blockchain as the only option
  * 16:18 [@sandhawke](https://twitter.com/sandhawke) -[dhh1128.github.io/peer-did-method-spec/index.html](https://dhh1128.github.io/peer-did-method-spec/index.html)
  * 16:18 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -I'd recommend revising that sentence if they want to not have people think that
  * 16:18 [@sandhawke](https://twitter.com/sandhawke) -Yes, I know, and they know.
  * 16:19 [@sandhawke](https://twitter.com/sandhawke) -But the best solution IMHO is just deploy something as nice and simple as indieauth
  * 16:19 [@sandhawke](https://twitter.com/sandhawke) -But I agree there's a culture clash
  * 16:19 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -From what I understand they have no interest in relying on DNS so that takes them completely out of the realm of working with current browsers or anything like IndieAuth
  * 16:20 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -in theory you could make a dns resolver method for did and use domain names as the identifier and get close to something like IndieAuth
  * 16:20 [@sandhawke](https://twitter.com/sandhawke) -Right.
  * 16:21 [@sandhawke](https://twitter.com/sandhawke) -And it doesn't matter if they want that
  * 16:21 [@sandhawke](https://twitter.com/sandhawke) -The end-users benefit
  * 16:22 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -The other thing missing from DID is the authorization framework that comes with IndieAuth since it's built on OAuth 2.0
  * 16:22 [@sandhawke](https://twitter.com/sandhawke) -They're working on DID-Auth, trying to figure out what that means. There are two papers about that this weekend, one from Microsoft.
  * 16:23 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -The DID and OIDC groups weren't even getting along very well and while OIDC is way overkill for what we use IndieAuth for, its still more similar to IndieAuth than blockchain stuff is
  * 16:24 [@sandhawke](https://twitter.com/sandhawke) -I agree re "way overkill", so I want to show how simple it can be. They're not the first "way overkill" people in identity / authn / authz.
  * 16:25 [@sandhawke](https://twitter.com/sandhawke) -I mean -- maybe I should just go watch netflix -- this might be a silly waste of time, but I'm here, and it's a lot of smart and motivate people, so I can't help but wonder about trying to steer them a bit.
  * 16:26 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -I would be very interested in what you come up with. I haven't had much luck in any of these conversations so far
  * 16:27 [@sandhawke](https://twitter.com/sandhawke) -fair enough :-) Is indieauth.spec.indieweb.org pretty much up-to-date with your thinking?
  * 16:28 [@sandhawke](https://twitter.com/sandhawke) -( sad not to see a change log from https://w3.org/TR/2018/NOTE-indieauth-20180123 )
  * 16:28 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) -Yep and https://aaronparecki.com/2018/07/07/7/oauth-for-the-open-web is a good explanation too
  * 16:28 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - oh did I forget a change log section? I'll try to add that
  * 16:29 [@sandhawke](https://twitter.com/sandhawke) - +1
  * 16:30 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - If video is more your thing, I gave this talk at the W3C workshop [youtube.com/watch?v=EeCNlB7v08I](https://youtube.com/watch?v=EeCNlB7v08I)
  * 16:30 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - its nice and short
  * 16:34 [@sandhawke](https://twitter.com/sandhawke) - cool, pulling out headphones and wathching...
  * 16:45 [@sandhawke](https://twitter.com/sandhawke) - ha - amused to hear Wendy's voice moderating the session
  * 16:52 [@sandhawke](https://twitter.com/sandhawke) - I don't understand the value of public apps being identified
  * 16:52 [@sandhawke](https://twitter.com/sandhawke) - (good video)
  * 16:59 [@sandhawke](https://twitter.com/sandhawke) - I guess there's some attack it's intended prevent.
  * 17:01 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - Yeah that's from OAuth. Prevents redirect interception by registering the redirect URL, and also helps the user not get phished
  * 20:28 [[jacky]](https://indieweb.org/User:Jacky.wtf) - tbh as much as I'm for the whole DiD and what not
  * 20:28 [[jacky]](https://indieweb.org/User:Jacky.wtf) - DNS is _not_ going anywhere
  * 20:29 [[jacky]](https://indieweb.org/User:Jacky.wtf) - as least for the people I aim to build for (like myself and then family to an extent)
  * 20:29 [[jacky]](https://indieweb.org/User:Jacky.wtf) - DNS is straight-forward and more-or-less "reliable"
  * 20:30 [[jacky]](https://indieweb.org/User:Jacky.wtf) - the only other idea I've seen thus far that was 'usable' has been [docs.ipfs.io/guides/concepts/dnslink](https://docs.ipfs.io/guides/concepts/dnslink)
  * 20:30 [[jacky]](https://indieweb.org/User:Jacky.wtf) - (which still relies on DNS but one could augment a local DNS resolver to intercept these lookups)
  * 20:51 [[tantek]](https://indieweb.org/User:Tantek.com) - listens intently. (also welcome (back) sandhawke!)
  * 20:55 [[jacky]](https://indieweb.org/User:Jacky.wtf) - I don't know / wonder if a solution that's speech-friendly will arise
  * 20:55 [[jacky]](https://indieweb.org/User:Jacky.wtf) - like if I can't say it out loud, it's incredibly hard to share
  * 20:55 [[jacky]](https://indieweb.org/User:Jacky.wtf) - sure, I can just share a link
  * 21:00 [[tantek]](https://indieweb.org/User:Tantek.com) - speechfriendly++
  * 21:00 [[Loqi]](https://indieweb.org/Loqi) - speechfriendly has 1 karma over the last year
  * 21:05 [[swentel]](https://indieweb.org/User:Realize.be) - [tantek], yeah, I figured that it might be a useful link for people looking for my 'main' feed
  * 21:06 [[swentel]](https://indieweb.org/User:Realize.be) - also because currently in aperture, rel="feed" is ignored. So if people search feeds on realize.be, they will get microformats, but that's on my homepage, which is kind of useless
  * 21:06 [[swentel]](https://indieweb.org/User:Realize.be) - which makes me wonder whether I should remove microformat markup on the homepage maybe
  * 21:08 [[swentel]](https://indieweb.org/User:Realize.be) - (to be more specific, xray underneath ignores rel="feed", but that's technical detail)
  * 21:09 [[swentel]](https://indieweb.org/User:Realize.be) - other than that, fun experiments today with checkins and geocache, I'm getting excited by the location stuff in indigenous :)
  * 21:10 [[jacky]](https://indieweb.org/User:Jacky.wtf) - hm so I saw a question about indieauth and "data", like in comparison to how OAuth2 gives you a blob of info post login
  * 21:11 [[jacky]](https://indieweb.org/User:Jacky.wtf) - IndieAuth doesn't have to do that thanks to MF2; you can just pull what you need from their h-card but now I wonder
  * 21:11 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - jacky: we actually started experimenting with this
  * 21:11 [[jacky]](https://indieweb.org/User:Jacky.wtf) - would it make sense to show a specialized page in the value of the 'me' page? that changes b/c on the authenticated app?
  * 21:11 [[jacky]](https://indieweb.org/User:Jacky.wtf) - aaronpk: oh?
  * 21:12 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - trying to remember where we documented it? it was a quick thing during IWC Austin
  * 21:12 [[jacky]](https://indieweb.org/User:Jacky.wtf) - oh man
  * 21:12 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - GWG added it to wordpress and I added it to Quill
  * 21:12 [[swentel]](https://indieweb.org/User:Realize.be) - hmm, GWG opened an issue for me indigenous, there's probably a link there, let me check
  * 21:12 [[swentel]](https://indieweb.org/User:Realize.be) - indieweb/indieauth #31
  * 21:12 [[Loqi]](https://indieweb.org/Loqi) - [dshanske] #31 Returning Profile Data
  * 21:13 [[jacky]](https://indieweb.org/User:Jacky.wtf) - nice
  * 21:13 [[swentel]](https://indieweb.org/User:Realize.be) - that's at least the indieauth thing
  * 21:13 [[swentel]](https://indieweb.org/User:Realize.be) - maybe there's more?
  * 21:13 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - yep thanks
  * 21:13 [[jacky]](https://indieweb.org/User:Jacky.wtf) - [indieweb/indieauth #23#issuecomment-414152219](https://github.com/indieweb/indieauth/issues/23#issuecomment-414152219)
  * 21:13 [[Loqi]](https://indieweb.org/Loqi) - [Zegnat] The table above has been updated with new statistics. This shows that `rel="manifest"` are equally as likely to be found on client pages as `h-x-app`. This Web App Manifests may be a more logical alternative than previously realised.
  * 21:13 [[Loqi]](https://indieweb.org/Loqi) - Further devel...
  * 21:13 [[GWG]](https://indieweb.org/User:David.shanske.com) - Although Zegnat pointed out it should be nickname not name
  * 21:13 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - hrm I don't think it should be "nickname"
  * 21:13 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - Hardly “should be”
  * 21:14 [[jacky]](https://indieweb.org/User:Jacky.wtf) - that makes sense
  * 21:14 [[jacky]](https://indieweb.org/User:Jacky.wtf) - b/c name is so vague
  * 21:14 [[jacky]](https://indieweb.org/User:Jacky.wtf) - vs 'username', 'nickname', 'given name'
  * 21:14 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - display name is more accurate
  * 21:14 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - More like: I ** wondered if it should be more clear to expect a “display name” rather than a personal name (which I feel `name` is often used for)** 
  * 21:15 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - the other reason for doing this is it means it's easier to return private/sensitive profile data to apps without having to have a way to serve protected data from your home page
  * 21:15 [[GWG]](https://indieweb.org/User:David.shanske.com) - aaronpk, I agree with the idea and am willing to change to display name. It is still new and easy to adjust.
  * 21:15 [[jacky]](https://indieweb.org/User:Jacky.wtf) - aaronpk: right 
  * 21:15 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - aaronpk, yes, that was a bit part of my reasoning over on GitHub :)
  * 21:15 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - please comment with more details if you think I didn’t make that clear
  * 21:16 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - s/a bit/a big/
  * 21:16 [[GWG]](https://indieweb.org/User:David.shanske.com) - If someone gives it another +1 I'll go make a PR
  * 21:16 [[swentel]](https://indieweb.org/User:Realize.be) - Hmm, I like name tbh :)
  * 21:16 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - I also don't necessarily think "name" is a bad property for this, just need to make it clear that there is no expectation of a "real name" or "full name"
  * 21:16 [[swentel]](https://indieweb.org/User:Realize.be) - as it's consistent then
  * 21:16 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - there isn't any expectation of that in this stuff anyway so I don't really see the problem
  * 21:17 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - Except I felt there may have been an expectation of that in JF2, aaronpk. And the issue seemed to suggest using JF2 cards.
  * 21:17 [[GWG]](https://indieweb.org/User:David.shanske.com) - aaronpk, what if someone requests the theoretical profile scope?
  * 21:17 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - Zegnat: what gave you the idea of that from jf2? jf2 shouldn't be defining any new semantics on top of the mf2 properties
  * 21:18 [[swentel]](https://indieweb.org/User:Realize.be) - GWG, do you have a link to the commit in wordpress?
  * 21:18 [[swentel]](https://indieweb.org/User:Realize.be) - Just for inspiration
  * 21:18 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - “full/formatted name of the person or organisation” is the mf2 definition
  * 21:18 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - Also, it feels to me like people have been using `name` on their h-cards a lot for full name currently
  * 21:19 [[GWG]](https://indieweb.org/User:David.shanske.com) - [indieweb/wordpress-indieauth #127/files#diff-F81F3DFF36BF04B7A070D642C858E883](https://github.com/indieweb/wordpress-indieauth/pull/127/files#diff-F81F3DFF36BF04B7A070D642C858E883)
  * 21:19 » [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) now has 3–5 seconds IRC delay, so discussing is going to be hard
  * 21:19 [[swentel]](https://indieweb.org/User:Realize.be) - thanks
  * 21:20 [[tantek]](https://indieweb.org/User:Tantek.com) - hmm - we've been through this renaming loop before. name is display name, no need to ever change to "display name".
  * 21:21 [[Zegnat]](https://indieweb.org/User:Vanderven.se_martijn) - I do not want to change the name property in mf2 here [tantek]. I just want it to be clear that the minimal info returned from an IndieAuth endpoint is a display name specifically (and further names (?) may be available under something like a profile scope)
  * 21:21 [[tantek]](https://indieweb.org/User:Tantek.com) - in the past other formats have tried to make distinctions between "display name" "full name" etc. and it just results in bad UX. in practice people enter into "name" what they want displayed. period. no need to futz or handwring about bikeshedding the property. it works
  * 21:22 [[tantek]](https://indieweb.org/User:Tantek.com) - Zegnat, calling something display name then implies that other "name"s are not "display" and it just confuses people (implementers, users etc.)
  * 21:22 [[swentel](https://github.com/swentel) - GWG, I've documented my experimental geo:uri;h=card on [indieweb.org/checkin#Posting_checkins_from_clients]](https://indieweb.org/checkin#Posting_checkins_from_clients) (but I'm not sure if that's the right place :/) **** 
  * 21:22 [[tantek]](https://indieweb.org/User:Tantek.com) - there is never a need in practice to ever "be clear" about "is a display name specifically"
  * 21:22 [[swentel]](https://indieweb.org/User:Realize.be) - just wanted to make sure it exists at least
  * 21:22 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - side note: openid connect has "name", "family_name", "given_name", "middle_name" and "nickname" all under the "profile" scope, and tbh is an example of what tantek is talking about where the only one actually used is just "name" 
  * 21:22 [[tantek]](https://indieweb.org/User:Tantek.com) - that's a hypothetical concern from which no one has ever documented any actual harm ever
  * 21:22 [[GWG]](https://indieweb.org/User:David.shanske.com) - swentel, link to that under Micropub experimental as well.
  * 21:23 [[swentel]](https://indieweb.org/User:Realize.be) - GWG, on micropub extensions?
  * 21:23 [[GWG]](https://indieweb.org/User:David.shanske.com) - Swentel, yes, excuse me.
  * 21:23 [[swentel]](https://indieweb.org/User:Realize.be) - Ok, maybe it's better to move it there completely
  * 21:24 [[tantek]](https://indieweb.org/User:Tantek.com) - aaronpk is correct, and opendid connect even there screwed up (inserted Western-centric assumptions by I'm sure the 100% Western white male openid connect "designers) by renaming vCard's "additional name" into "middle_name".
  * 21:24 [[tantek]](https://indieweb.org/User:Tantek.com) - openidconnect--
  * 21:24 [[Loqi]](https://indieweb.org/Loqi) - openidconnect has -1 karma over the last year
  * 21:24 [[GWG]](https://indieweb.org/User:David.shanske.com) - Do we have a theoretical use case for more than minimal data yet?
  * 21:24 [[tantek]](https://indieweb.org/User:Tantek.com) - westerncentricassumptions--
  * 21:24 [[Loqi]](https://indieweb.org/Loqi) - westerncentricassumptions has -1 karma over the last year
  * 21:26 [[GWG]](https://indieweb.org/User:David.shanske.com) - I return name, url, and photo because that was the minimum needed for a client to display. I am happy to return more behind a profile scope the day someone wants it
  * 21:26 [[tantek]](https://indieweb.org/User:Tantek.com) - (note: " middle" is a layout/order specific label, not a semantic. in the past these same kinds of 100% Western white male format designers would have "first_name" "middle_name" "last_name", there's plenty of examples of bad old dead formats with that, programming examples in various "5 minutes to make your own social network!" type stuff etc.) 
  * 21:26 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - GWG: I'd hold off on anything further with this until we get more publishers and consumers of it
  * 21:27 [[jacky]](https://indieweb.org/User:Jacky.wtf) - r^
  * 21:27 [[GWG]](https://indieweb.org/User:David.shanske.com) - aaronpk, I planned on it
  * 21:27 [[GWG]](https://indieweb.org/User:David.shanske.com) - I just was curious about uses
  * 21:27 [[GWG]](https://indieweb.org/User:David.shanske.com) - I have bigger problems right now
  * 21:27 [[tantek]](https://indieweb.org/User:Tantek.com) - swentel - I think if you put rel="alternate" on the link to your h-feed page then it may be discoverable. I believe rel=feed was deprecated (even dropped by WHATWG HTML for lack of interest / implementations)
  * 21:28 [[swentel]](https://indieweb.org/User:Realize.be) - [tantek], oh, interesting, I'll give that a try yes!
  * 21:28 [[GWG]](https://indieweb.org/User:David.shanske.com) - Really? I just added a bunch of rel feeds
  * 21:28 [[GWG]](https://indieweb.org/User:David.shanske.com) - I can't keep up
  * 21:29 [[GWG]](https://indieweb.org/User:David.shanske.com) - I thought alternate was an alternative view of the same page and feed was a different page
  * 21:29 [[GWG]](https://indieweb.org/User:David.shanske.com) - What is rel-feed?
  * 21:29 [[Loqi]](https://indieweb.org/Loqi) - rel-feed is the standard for linking to multiple (potentially alternative) h-feeds from a site's homepage using the code rel="feed" on those links indieweb.org/rel-feed
  * 21:30 [[jacky]](https://indieweb.org/User:Jacky.wtf) - yeah same
  * 21:30 [[jacky]](https://indieweb.org/User:Jacky.wtf) - re: G WG
  * 21:31 [[tantek]](https://indieweb.org/User:Tantek.com) - no feed discovery is done via rel=alternate type="insert your feed mime type here"
  * 21:31 [[tantek]](https://indieweb.org/User:Tantek.com) - like since forever
  * 21:31 [[GWG]](https://indieweb.org/User:David.shanske.com) - That's the way I am using and consuming it
  * 21:31 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - whoa swentel indieweb.org/Micropub-extensions#Location_checkin_information
  * 21:31 [[tantek]](https://indieweb.org/User:Tantek.com) - folks here have been trying to get rel=feed off the ground again but TBH I'm unsure about it's feasibility
  * 21:31 [[GWG]](https://indieweb.org/User:David.shanske.com) - What is feed discovery?
  * 21:31 [[Loqi]](https://indieweb.org/Loqi) - feed discovery is a way to, given someone's home page, discover their feed or feeds that they publish indieweb.org/feed_discovery
  * 21:31 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - that's like an embedded h-card in a geo URL?
  * 21:31 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - URI
  * 21:31 [[swentel]](https://indieweb.org/User:Realize.be) - aaronpk, yeah, works great .. (at least for me)
  * 21:32 [[GWG]](https://indieweb.org/User:David.shanske.com) - aaronpk, yes it is
  * 21:32 [[tantek]](https://indieweb.org/User:Tantek.com) - aaronpk you had it right 🙂
  * 21:32 [[swentel]](https://indieweb.org/User:Realize.be) - I can post checkins and geocaches now from indigenous, with pictures, all in one go :)
  * 21:32 [[swentel]](https://indieweb.org/User:Realize.be) - it's GREAT ;)
  * 21:32 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - [tantek]: re: geo URI? I thought URLs had to be resolvable
  * 21:32 [[tantek]](https://indieweb.org/User:Tantek.com) - swentel++ wow
  * 21:32 [[Loqi]](https://indieweb.org/Loqi) - swentel has 27 karma in this channel over the last year (48 in all channels)

## #indieweb-dev on IIW 2018-08-19

[![](https://imgur.com/MvrlESD.png)](https://freenode.logbot.info/indieweb-dev/20180819)

* [#indieweb-dev on IIW 2018-08-19-chat log](https://freenode.logbot.info/indieweb-dev/20180819)
  * 17:08 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - No, IIW
  * 17:09 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - but all the OAuth IETF people will be there
  * 17:09 [[tantek]](https://indieweb.org/User:Tantek.com) - IETF people take IETF i-d more seriously than rando domain with proposals
  * 17:09 [[kevinmarks]](http://www.kevinmarks.com/) - IIW is a good place to socialize specs certainly
  * 17:09 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - I wonder how much of this I can write in the next 2 hours
  * 17:09 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - need a name tho
  * 17:10 [[kevinmarks]](http://www.kevinmarks.com/) - OpenAppID
  * 17:10 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - Oh no
  * 17:11 [[kevinmarks]](http://www.kevinmarks.com/) - I was being facetious
  * 17:11 [[tantek]](https://indieweb.org/User:Tantek.com) - [kevinmarks]: based on what evidence of successful specs to come out of IIW socialization?
  * 17:11 [[tantek]](https://indieweb.org/User:Tantek.com) - kevinmarks++
  * 17:11 [[Loqi]](https://indieweb.org/Loqi) - kevinmarks has 7 karma in this channel over the last year (30 in all channels)
  * 17:11 [[tantek]](https://indieweb.org/User:Tantek.com) - OpenAppID++
  * 17:11 [[Loqi]](https://indieweb.org/Loqi) - OpenAppID has 1 karma over the last year
  * 17:11 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - OAuth came out of IIW
  * 17:11 [[kevinmarks]](http://www.kevinmarks.com/) - OAuth 1.0 had a lot of groundwork done at IIW
  * 17:11 [[kevinmarks]](http://www.kevinmarks.com/) - yes
  * 17:12 [[tantek]](https://indieweb.org/User:Tantek.com) - no that's a myth. OAuth came out of a mailing list started by Blaine at Twitter
  * 17:12 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - A lot of it was done at IIW regardless of where it started exactly
  * 17:12 [[tantek]](https://indieweb.org/User:Tantek.com) - the actual work was done by a small set of folks on a limited-write, public-readable mailing list
  * 17:12 [[kevinmarks]](http://www.kevinmarks.com/) - yes, but getting the yahoo and Google people in the room with him at IIW really helped
  * 17:12 [[tantek]](https://indieweb.org/User:Tantek.com) - it was an interesting model of standards development by email
  * 17:13 [[tantek]](https://indieweb.org/User:Tantek.com) - OAuth did not "come out of" IIW
  * 17:13 [[tantek]](https://indieweb.org/User:Tantek.com) - that's the myth
  * 17:13 [[kevinmarks]](http://www.kevinmarks.com/) - that helped get the mutual trust necessary to contribute to the mailing list
  * 17:13 [[tantek]](https://indieweb.org/User:Tantek.com) - it came out of a limited-write, publicly readable mailing list started by Blaine
  * 17:13 [[kevinmarks]](http://www.kevinmarks.com/) - I didn't say that, I said "a good place to socialize specs"
  * 17:13 [[tantek]](https://indieweb.org/User:Tantek.com) - aaronpk said that
  * 17:14 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - What I meant was OAuth would not have succeeded if it had not been discussed at IIW
  * 17:14 [[kevinmarks]](http://www.kevinmarks.com/) - I dragged several google auth people across the street to IIW, then they joined the mailing list
  * 17:15 [[kevinmarks]](http://www.kevinmarks.com/) - the real bonding experience was them hotpatching the spec and mitigating the replay attack at that foo camp
  * 17:16 [[tantek]](https://indieweb.org/User:Tantek.com) - yes the Open Web Foo hotpatching of OAuth 1 to fix the security problems was key
  * 17:16 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - I need a name that gets across that client registration is replaced by DNS
  * 17:16 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - I would use “implicit client registration” if “implicit” didn’t already have existing meaning in OAuth
  * 17:17 [[tantek]](https://indieweb.org/User:Tantek.com) - "URL client registration" ?
  * 17:17 [[kevinmarks]](http://www.kevinmarks.com/) - Zero Registration per ZeroConf
  * 17:18 [[tantek]](https://indieweb.org/User:Tantek.com) - or NoReg per NoSQL
  * 17:19 [[tantek]](https://indieweb.org/User:Tantek.com) - shortened to "NR"
  * 17:19 [[tantek]](https://indieweb.org/User:Tantek.com) - how do you handle client registration? we use NR for that
  * 17:19 [[tantek]](https://indieweb.org/User:Tantek.com) - "ZR" works just as well
  * 17:19 **sknebel** - client lookup?
  * 17:21 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - PKCE is a great name because it’s easily googleable and also pronounceable (pixie)
  * 17:23 [[tantek]](https://indieweb.org/User:Tantek.com) - aaronpk: Zero Registration shortened to: ZoRg
  * 17:23 [[tantek]](https://indieweb.org/User:Tantek.com) - all the Fifth Element fans will love it
  * 17:23 [[aaronpk]](https://indieweb.org/User:Aaronparecki.com) - zorg omg
  * 17:24 [[tantek]](https://indieweb.org/User:Tantek.com) - YES