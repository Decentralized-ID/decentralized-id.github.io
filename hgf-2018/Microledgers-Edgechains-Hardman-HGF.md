---
title: Microledgers and Edge-Chains — A Primer 
description: A Transcript of Daniel Hardman of Evernym Presenting at Hyperledger Global Forum — 2018
image: "https://infominer.id/images/edge-card.png"
---

# Hyperledger Global Forum 2018 — Microledgers and Edge-Chains 
**A Primer - Daniel Hardman, Evernym**

---

<code>Editors Note: I've taken to working on youtube transcripts for podcasts and videos whos content is valuable and not readily accessible in text form, so that it will be easier for anyone to reference. -<a href="https://infominer.id">infominer</a></code>


* [github.com/infominer33/DecentralizedID](https://github.com/infominer33/DecentralizedID)
* [infominer.id/DecentralizedID](https://infominer.id/DecentralizedID)

---

[Evernym](https://evernym.com)’s Chief Architect [Daniel Hardman](https://www.evernym.com/team/daniel-hardman/) takes the Hyperledger community through Evernym’s work on Microledgers and Edge-Chains Architecture. Attendees will gain insight into the theory, applications and evolution in Hyperledger Indy along with a practical discussion of their potential.

<img src="https://i.imgur.com/H5ijP94.png"/>\
<sup><a href="https://www.youtube.com/watch?v=iK5vd7-b1zA&list=PL0MZ85B_96CGkWnEvdPy5sB4VRcH2XWuP&index=100">Youtube: Hyperledger Global Forum- Microledgers and Edge-Chains: A Primer- Daniel Hardman, Evernym</a></sup>

* [Daniel Hardman, Chief Architect - Evernym](https://hgf18.sched.com/event/G8sN/microledgers-and-edge-chains-a-primer-daniel-hardman-evernym)
  > Daniel Hardman has a quarter century of experience in enterprise software. As a technical director or chief architect, he’s led engineering teams at small startups, an incubator, and a continent-spanning business unit at a Fortune 500 company. He founded a dot com a few years back, serving as CEO and later CTO before selling the business. Daniel designed and personally coded complex scheduling software that runs the biggest supercomputers on the planet. He also worked on big data systems that use natural language processing and machine learning/AI to impute reputation to the entire observable internet. He is a member of Infraguard, has training in cybersecurity, and has spoken at industry conferences such as RSA. Daniel has an MBA plus a master’s degree in computational linguistics. He holds numerous patents and is a prolific blogger.

## Contents

* [Microledgers and Edge-Chains](#microledgers-and-edge-chains-)
* [A Personal Arc](#a-personal-arc-)
* [Blockchain— the new centralization](#blockchain-the-new-centralization-)
* [Where Blockchain is Needed (or Not)](#where-blockchain-is-needed-or-not-)
* [Microledgers](#microledgers-)
* [How Blockchain is Still Relevant](#how-blockchain-is-still-relevant-)
* [App Centralization Continuum](#app-centralization-continuum-)
* [Teleomergent - More than a decentralized app](#teleomergent---more-than-a-decentralized-app-)
* [Dapps vs Edgechain Protocols](#dapps-vs-edgechain-protocols-)
* [Defining an Edgechain Protocol](#defining-an-edgechain-protocol-)
* [A Familiar Example—Buying a House](#a-familiar-examplebuying-a-house-)
* [Trust Ping Protocol](#trust-ping-protocol-)
* [Tic Tac Toe](#tic-tac-toe-)
* [DID method for peer (private pairwise) DIDs](#did-method-for-peer-private-pairwise-dids-)
* [Peer DID Method Spec](#peer-did-method-spec-)
* [Megaphone Protocol](#megaphone-protocol-)
* [Call to Action](#call-to-action-)
* [Q&A](#qa-)
* [Home](https://infominer.id)

## Microledgers and Edge-Chains [**^**](#contents)
**Lightly edited transcript from Youtube.**

<img src="https://i.imgur.com/Hu9v2Md.png"/>

Okay, I think we'll go ahead and get started. There are likely to be people trickling in, if they're like I am. If I didn't have to be here speaking I would take my time getting in the next session after lunch feeling a little bit sluggish... but anyway, they'll come in and and we'll already be in the presentation.

My name is Daniel Hardman, hopefully you've if you read about this session you might know a little bit about my background. I work with Hyperledger Indy project, mostly. I'm a maintainer there, and I also work for, well so I have a day job with Evernym... and then a side gig, where I work on the technical governance part of the Sovrin Foundation, which is closely connected to the Indy project.

Anyway, today I'm going to talk about some concepts that have been marinating in my mind and in the minds of some people that I work with for quite a while. Not all these ideas are originally mine I want to give credit where credit is due.

Lots of other smart people have been talking and thinking about this as well I'm just a spokesman for a lot of other people, and hopefully the title intrigued you a little bit. 

Microledger's and edge-chains: I'm going to demystify that, and when you walk away I hope you're gonna think of this as not so much a super technical session that you've been to but instead a session that kind of has some intriguing ideas for you to think about later in whatever you're doing.

## A Personal Arc [**^**](#contents) 

<img src="https://i.imgur.com/5aXEDkg.png"/>

I'd like to start by taking you on a little bit of a personal journey. I started working in blockchain two and a half years ago, and when I first became aware of the basic concepts of how blockchain worked and so forth I became really excited about how blockchain had solved a bunch of problems

and how I was going to go conquer the world with all this new technology and it was awesome and that was a I lasted in that phase of my acquaintance with blockchain for, I don't know, several months but I start to encounter practical problems with some of the blockchain stuff I was doing. 

and I hope as I describe the rest of this arc you'll smile a little bit to yourselves, and say, yeah I've kind of been through the same thing. 

in a way this is kind of like the Gartner hype cycle you know there's the the spike of excitement and then the trough of disillusionment. 

<img src="https://i.imgur.com/BsTgEd0.png"/>

I went through learning about some of the performance and scaling issues that we had to deal with, and some of the complexity. 

and then I started to realize that putting data on the blockchain had certain repercussions that I didn't always want to deal with, and that there needed to be some very careful thought about how we encrypted data.

<img src="https://i.imgur.com/kdoyUEq.png"/>

and then I realized encrypting it wasn't enough, it just plain shouldn't be there at all. and so hopefully you guys are recognizing these kinds of patterns in your own thinking here and then I got into the whole all regulatory compliance of GDPR thing and gee this is getting harder and
harder.

<img src="https://i.imgur.com/V5cyLYb.png"/>

Then I and several of my companions discovered this notion of microledgers, and we feel like it was kind of an aha moment for us. So I'll explain what microledgers are and I think you'll see how that's relevant to this arc when I'm done.

Let me just point out that that same kind of arc that I just described in my own thinking we're seeing unfold in lots of different ways in the whole blockchain space. 

<img src="https://i.imgur.com/oVC0WwF.png"/>

All of the things on this list here are examples of projects where somebody has thought hard about the original blockchain paradigm, and tweaked something in an interesting way because
of that same arc, and you know the tweaks are different. 

* plasma is about taking smart contracts off the blockchain
* triple signed receipts is about preserving confidence in data but not having to keep a full history even though you have a strong proof that you're at the right state anyway 

they all different things up there and if you don't know about all those, I didn't know about all of them either until I went and researched this talk, and I was looking for patterns. 

I knew about some of them and I found some others there but the point is that I think the whole industry is going through a maturation phase where we're realizing that there's certain aspects of what blockchain can do that we love, and there's other aspects of what blockchain gives us that we don't love so much and we're trying to kind of wrestle against those constraints 

<img src="https://i.imgur.com/ZBiVQ0J.png"/>

These are the two things that I think these arcs all have in common, mine and and the things on the previous slide:  they're all trying to do less with the central big blockchain in some creative way so that they can keep the special value out of the blockchain but not have some of its downsides.

## Blockchain— the new centralization [**^**](#contents)

I want to just point out something I went and looked just for fun I went and looked up architecture diagrams with Google. I was looking for old client-server architecture diagrams okay and these are just three that I picked at random out of the Google image search results list 

<img src="https://i.imgur.com/yYUdvNr.png"/>

you see that client-server is kind of this old paradigm where we have this notion of a centralized thing, and client-server equals bad, right?

we've been down that road we don't like that anymore, but here's what's interesting I also went and searched for some architecture diagrams about blockchain and some blockchain supposed to be highly decentralized and lo and behold there are lots and lots of evidence in these diagrams that blockchain is actually it just almost the exact same thing 

<img src="https://i.imgur.com/py6olR5.png"/>

now there's some things about blockchain that are different I'm not arguing that they're identical but the point is there is this phenomenon sometimes that blockchain has been used in a way that's far more centralized than we like to admit yes there are nodes that spread the load around and yes the nodes create this notion of diverse or I mean diffuse trust and yet all of those nodes can be treated as one bundle in the middle 

and in fact in a lot of architecture diagrams that you see in presentations at this conference and any other conference you will see a little graphic that represents the blockchain and a bunch of arrows coming to it from all over the place and what's that that's centralization 

## Where Blockchain is Needed (or Not) [**^**](#contents)

<img src="https://i.imgur.com/ugjLkS9.png"/>

so we don't necessarily need the blockchain for everything that we think we need it for the Vitalik, back in April, I'll let you read that quote there, well actually I'm going to read it because it's such a good one:

>Blockchains.. are a far less efficient computer and database than technologies that have existed for over 40 years... efficiency is not what block chains are built for - [Vitalik Buterin, April 2018](https://www.youtube.com/watch?v=jJt3yag96fU)

if you actually go and look up that quote he does a comparison of how much it costs to do certain kinds of computations on Ethereum versus AWS, and it's about a million to one difference in efficiency.

>"Let's say you and I, we are happy to do some transactions with each other.. We don't really need to use the blockchain unless we disagree with each other... Why would you need the mediator if you are actually in accordance...?" - Arther Gervais (Founder of Liquidity Netowrk), June 2018

Then founder of Liquidity Network, in June. This is a really good quote: - bottom line is this notion, you know what? Why would you need a mediator if you're actually agreeing with each other? 

now there's an answer to that question but there's also, that question exposes some interesting things to think about. 

I think smart people in the industry are starting to question some basic assumptions. 

<img src="https://i.imgur.com/ZfhYNAD.png"/>

here's my picture of an architecture that's centralized in blockchain oriented you got the blockchain in the middle here and you got the arrows coming to it right this is how I was thinking about my own particular problem which was the identity management relationship management problem that's at the core of identity when I first came into this world and if you see, 

we've got two parties that each have a relationship and want to trust each other we have  Alice we have Bob and Alice needs to know some things about her view of this relationship and she also needs to know some things about Bob's view of the relationship okay and these two views of the world


what's symmetrical and complimentary but they're using the blockchain in the middle as the trusted intermediary and like I said this view of the world sort of works but it chafed on me and it became increasingly uncomfortable as I learned some of the drawbacks and challenges to it 

## Microledgers [**^**](#contents)

<img src="https://i.imgur.com/kX93eTU.png"/>

Here's what I evolved to, and this is what I want to talk to you about, is the microledger notion. In this notion you still have a blockchain, and blockchain does have relevance it's highly relevant, but it's not the main mediator of the relationship between Alice and Bob.

Alice and Bob talk to each other directly and then they have this kind of back-channel thing that they can use to interact with the blockchain to the extent that they need to and I'm gonna talk about what they really need the blockchain for but it's not as much as we thought at least as much as I thought to begin with 

so when you have this kind of a relationship what you have is two parties that are kind of at the edge of the old diagram, instead of the thing that's in the middle, you have the things that are at the edges okay and these things at the edge are talking to each other. this is how I get the concept of an edge chain 

that's where that word in the title of the presentation comes from, is the notion that you can have some of the same characteristics of a blockchain, you can have high trust and tamper resistance, and diffuse patterns of communication and so forth. but, you don't have the blockchain sitting in the middle of it. it's all happening out at the edges

<img src="https://i.imgur.com/c0mtJW0.png"/>


okay so this evolves even further: if you have this person Alice having relationships with multiple people, she
continues to have these lateral side relationships. she doesn't have them through the blockchain. 

now you might be saying well wait a minute if you take the blockchain and all those big arrows out what is it even useful for?

## How Blockchain is Still Relevant [**^**](#contents)

<img src="https://i.imgur.com/uJ1Kkwq.png"/>

In my case it's useful for certain problems that require external trust. For example, there has to be a place where I can announce that a credential, upon which identity is based, has been revoked.  The world needs to test for that condition when they're seeing credentials presented. 

I know that there's people out here who aren't in the identity space. I think there's analogs to this in in non-identity world too. 

There's certain things that you need to consult the blockchain for. The main things that aren't on this list are things like: 
  * talking to each other
  * storing things
  * doing computation
  * interacting
None of that stuff has to go through smart contracts or any of that. It just has to have a few very small things that make this possible. 

Besides revoking credentials, in the identity space: 
  * You have to be able to revoke a device: If you leave your phone in on the backseat of an uber you need to be able to quickly say don't let anybody use that phone to impersonate me. 
  * you need to be able to discover parties that are intending to be public 
  * you need a secret rendezvous spot: so if you think of secret agents that you know they're heading off into enemy territory, and they agree that if if they're not back by such-and-such a time, then they're going to meet in the square at midnight, or whatever...
You can use a blockchain kind of like that: agree that we'll rendezvous on the blockchain if we lose track of one another, or have to repair a relationship and we can't do it by direct conversation.

It turns out that Merkel proofs of state integrity between these two parties can be relevant. 

This last one is where I get the name micro ledger for this talk. That is, the way that these two parties interact with each other, has to have some characteristics of proveability and tamper-resistance even though it's not on the main blockchain. 

You can do that by doing some very simple (well it's not very simple... it's simple compared to other stuff) crypto on your local hard drive..

When you interact with the other, passing them Merkel proof-of-state and having them check it against what they have.

you end up knowing with confidence that both of you have the same thing, and and you haven't drifted or misinterpreted one another. 

You end up basically having a tiny little ledger on your machine for the relationship. Alice would have one for the relationship she has with Bob. I'm talking tiny, I'm talking 5k 10k little tiny files. 

They're not massive, they don't last necessarily forever, they don't store any significant amounts of information, but they just have an orderly sequence of hashes that show how state has evolved that's the micro ledger concept.

## App Centralization Continuum [**^**](#contents)

<img src="https://i.imgur.com/lnKUizp.png"/>

After we started playing with this idea I started to see things a little bit different this is my journey again but I thought instead of it being kind of a time sequence I saw it as a continuum of centralization and I really think that's where my mental journey took me is I started out thinking blockchain was cool and I'm going to be decentralized but I wasn't really very decentralized in my thinking and took me a long time to get there 

you know I started over with "put it all in the blockchain" which isn't so far away from traditional client-server 

then you start seeing people talking about sub chains and side chains and things like that that's an example of moving farther to the right on the continuum 

then you hear people talking about well just anchor it on the blockchain now we're starting to get pretty far over to the towards the right if you go all the way over to the right you have a pure edge chain where you really don't need the blockchain at all.

I don't think I'm gonna write any software that looks completely at that end of the continuum. I think the blockchain introduces some characteristics of trust that I really need but I think I can get pretty far over here get all the benefits from blockchain that I really care about but not have hardly any of the drawbacks or complications and the only price is complexity darn it

okay so I put up here on this picture, also I have gaps right here and edge chain protocols. when I first started exploring this notion of the edge chain, I was calling the thing that we were building a dApp. because it's a decentralized app, of course. but I realized that what the industry is calling a dApp is actually pretty far over to this side because it's typically running everything through a smart contract that does centralize computation. 

there are dApps that aren't that way, so the DAP thing moves over towards the right. There are some gaps that get maybe almost this far, but you you can take it all the way over here, and I think if you go way over to the right side it's not really fair to call that a dApp because it's pretty different from what the industry thinks a dApp is. 

## Teleomergent - More than a decentralized app [**^**](#contents)

<img src="https://i.imgur.com/1E6jCjZ.png"/>

I'm gonna give you some examples here in just a minute. Just for kicks, I'm gonna introduce a new word to you, because this is why I'm excited about the right end of that continuum. I think that the things on the right end of that continuum have this characteristic.

this is a big word, you know, a $24.00 word. but it's "telly-o-mergent." If you're familiar with the word [teleology](https://www.merriam-webster.com/dictionary/teleology) or [telonomy](https://www.merriam-webster.com/dictionary/teleonomy),  this has the notion that you have order from chaos. 

Okay? but, it's not order that's decreed by some central party it's order that arises spontaneously. Teleonomy is used in discussions about evolution and biology and how a very complex ecosystem can manifest really sophisticated patterns of behavior even though there's not anybody out there telling the Zebras which direction to run when the Lions chase them 

so you may have also heard the word chaotic before and you may have run into the notion of Adam Smith's invisible hand in the economy it's the notion that you give a bunch of independent actors the right incentives and lo and behold the free market causes an interesting dynamic to emerge that's useful 

and that's what I think is the true characteristic at the far right side is that you give independent agents the ability to interact and these agents find useful ways to interact according to a protocol. 

## Dapps vs Edgechain Protocols [**^**](#contents)

this is just a little compare and contrast I think I'm gonna skip over this suffice it to say that daps and edge chains have a lot in common but I think there's some interesting differences 

<img src="https://i.imgur.com/cVg6gFH.png"/>

and I'll maybe during Q&A; we can come back to this slide if you have questions about it, but let me now actually give you some examples of what I'm talking about.

## Defining an Edgechain Protocol [**^**](#contents)

<img src="https://i.imgur.com/vIDt6iO.png"/>

When you define an edge chain protocol you have to answer these four questions:

* what are the roles in my protocol?
* what types of messages do we exchange?
* what stage or sequencing rules apply?
* and how our trust and incentives managed?

## A Familiar Example—Buying a House [**^**](#contents)

<img src="https://i.imgur.com/XEpCvty.png"/>

so here's a really familiar example, okay? no tech involved. how do you buy a house? What are the roles in buying a house?

well you have a buyer and a seller, and the realtor for the buyer and the realtor for the seller. you have a home inspector, you have a title company. 

these are roles, and by the way, buying a house is a protocol. You can't just go order a title, insurance, on some arbitrary home, because that would be out of order for the, it's not the sequence. 

You have to start by doing step one and then you go to step two and then you go to step three right and the parties in this interaction have responsibilities they can do certain things, and not other things. 

The kinds of messages that get exchanged in this protocol: we have an offer to buy, a counter-offer, an acceptance or rejection, a home report, a title search. These are messages. 

What are the state rules that apply? well this is an example state machine I drew. You start by negotiating and you can go round and round in circles in negotiating, eventually you exit the negotiating phase. you're in the preparing phase where you order a title search and a home report and all these things and anyway you end up consummating the deal or not consummating it 

That is an edge protocol. 

Why is it an edge protocol? 

There's no blockchain involved, right? it's people out at the edge.

There's a hundred thousand things like this, ordering a hamburger is a protocol. You can't just walk up to somebody nd say, "here's seven twenty five." You have to walk up to him and say, "I want number three on the menu," then give him $7.25 after they ask you "is that to go or not?" "to go" right? 
There's this whole protocol involved in that, that we all know. The reason I'm harping on this is because all kinds of business problems are solved by protocols all the time, and in fact, they're mostly edge protocols. 

That's a cool thing if you can just hook them up to blockchain for just the parts that you need them for, and not all of it. The weight of what you're building goes way down. 

## Trust Ping Protocol [**^**](#contents)

<img src="https://i.imgur.com/pUnUIiD.png"/>

Here's a simple edge protocol that's techy. this one is relevant to the identity space. This is the trust ping protocol, and in Indy there is a HIPE (which is like an RFC) about how you ping another person. 

You have their DID, for them that's their identifier, and given that identifier you should be able to reach out and talk to that person. 

So how do you do it? According to the whole Indy technology should be able to do it no matter what transport you're used to send messages whether it's HTTP or mail or Bluetooth or whatever. 

You should know some things when you engage in this trust ping about whether the person on the other side is trustworthy and how much trust might have been eroded by the kind of mechanisms you used in between you. 

There's a HIPE about that, you can see the roles, the pinger and the pingee; and the message types. 

let me give you a quick demo of this protocol. I'm gonna start up an indie agent, and that agent is going to be listening on email, and I'm going to talk to it by email, and I'm gonna use the trust ping protocol to to interact with it. 

<img src="https://i.imgur.com/SA01z4J.png"/>

This is the [trust ping protocol documentation](https://github.com/hyperledger/indy-hipe/pull/67), and the trust ping documentation says that if I want to ping somebody this is the kind of JSON message I need to send it. 

So, I'm gonna send it one. Let's go over here to my email, and I'll bring up my little trust ping. nothing up my sleeve. here's the the JSON that I'm sending, which is just a direct copy and paste out of this HIPE here... so that's the that's the stuff that I sent.

and let's see... message was sent. that's good. now what we've got to see is if the message is going to come back... there we go. 

<img src="https://i.imgur.com/qe7MocA.png"/>

so the agent on the other side pinged me back and let's see what it sent me: it sent me an aim style message. 

This is the JSON that I got back, it says "hi" from Indy agent. So, I've just engaged in a protocol. 

Now what does blockchain add to this? I could do this entirely without blockchain, but there's some things I wouldn't have: I wouldn't have confidence in the other sender. Somebody could sit in between me in this protocol and mess with my mind, right? be a man-in-the-middle.

So most of the protocol is not modified, but by adding a little bit of blockchain pixie dust, I'll call it, I can increase the trust behind this protocol.  

That's the kind of thing that I'm seeing over and over again as I get my head wrapped around this paradigm is you start with a paradigm that's really not very blockchain heavy, and then you say "what are the things that's wonderful about blockchain, that I need to add into this? and how can I do it as light as possible?" 

## Tic Tac Toe [**^**](#contents)

<img src="https://i.imgur.com/Ym9zesW.png"/>

okay so on to the next thing... here. Tic Tac Toe. We could also play tic-tac-toe. I'm gonna wait and see if I have enough time. I'll do a demo of tic-tac-toe if you feel like it later. but anyway I have a demo of that if you want to. this one was not there's no blockchain goodness on this this is all the way to the complete right side is being a pure hedge protocol because you don't need a blockchain to play tic-tac-toe okay.

## DID method for peer (private pairwise) DIDs [**^**](#contents)

<img src="https://i.imgur.com/T3nCl47.png"/>

This is a more serious one. What if you want to manage a relationship? Alice and Bob live across the world, they use complicated technologies. Each of them has different technologies. One of them has a laptop, and a cell phone; and the other one has a desktop computer at work, and two cell phones, and something in the cloud. 

They want to talk to each other and there's different pieces of software running on all these different things at different version levels and all this kind of stuff. 

How does Alice tell Bob: "you shouldn't accept messages anymore from my old cell phone that I just sent to the recycling"? 

I think they told me they were gonna wipe the hard drive on it but I just don't trust I'm gonna tell Bob not to do that. How does Alice say, "I upgraded my own world here, and I've got a new device, and now if I send messages from that device you
should trust them."

how does Alice say I'm gonna rotate my keys? all of these are concerns of managing a relationship, and you need a protocol to manage a relationship... and guess what? it's mostly an edge protocol. 

## Peer DID Method Spec [**^**](#contents)

This is a more serious one that has pretty high stakes. I've been working on a method to describe how DIDs can be created, and the DID docs associated with those DIDs can be shared.

You can see the the roles here are the participants in the relationship and there's some message types that are described here there's actually a [DID method spec draft](https://dhh1128.github.io/peer-did-method-spec/index.html) and I'll show that to you really briefly here and you can go look it up yourself later if you want to 

<a href="https://dhh1128.github.io/peer-did-method-spec/index.html"><img src="https://imgur.com/QlhWEmfl.png" /></a>


I'll give you the URL and you can go read it, but there's this whole spec behind this, and this is what has caused, I think, the most ruminating on the concept of a microledger... because the microledger as a persistence mechanism could provide high trust to back the did method that I'm mentioning. 

## Megaphone Protocol [**^**](#contents)

Let me go on to another one that's maybe a little bit more interesting so this is just an imaginary one but I think I'd love if somebody in the audience wants to build this I'd be super excited and I would buy your app.

<img src="https://i.imgur.com/wzji3sc.png"/>

A megaphone protocol, what I'd like is something where if I'm sitting on the beach in Indonesia and a tsunami happens... I can grab my phone and push a button and say "run a tsunamis coming" and my phone contacts all the phones all around the resort where I'm staying which in turn contact all the phone's a mile inland and everybody starts running not just the people who can see the wave. Would that be cool? 

I want basically a virtual megaphone, but here's a "why do I need blockchain?" there's a really good answer to this, I can't build this right now, because if everybody had a real megaphone in real life you'd have problems with people using it irresponsibly, wouldn't you? 

So there's a trust problem, I can use blockchain to require people to put stake, or put their identity in escrow against their responsible behavior. So that a person can say, when it's a life-or-death situation, "I need an EpiPen right now!"

I'm willing to you know have a hundred dollars on the line or I'm willing to have my identity disclosed if I am shown to use that irresponsibly and that protocol can hook back to the blockchain as a basis for that trust but most of everything that's happening is all out on the edge. 

you can see some of the other ones, you know, "my child is lost at Disneyland," or "I'm desperate to get on this plane as somebody in this line willing to send me to sell me their plane ticket 4000 euros?" 

any of these kinds of things could be done with this kind of protocol, and you would just need peer-to-peer communication in your app. Or you could have the app go back to the cloud and talk to other apps through the cloud, if you needed to.

that would be more centralized but anyway there's some roles in this a speaker a listener and a relay so you could have an app and a person could talk through your app to another phone that was close to you and so the word would spread right if anybody's interested there's a link to the concept doc when you download the slides you can go read more about that protocol 

## Call to Action [**^**](#contents)

<img src="https://i.imgur.com/xLHfZ7b.png"/>

I hope that I haven't gone too too deep, I've tried to stay really high-level and I hope that I've been general enough that even if you're not in the Indy space, the identity space, you're thinking a little bit to yourself yeah maybe there's some ways that I'm taking for granted 

that we need to use the blockchain for something... and maybe I should think from the other direction instead start thinking about the problem as an edge protocol problem and then say how do I sprinkle the the magic pixie dust a blockchain just enough to get the properties of trust or the constraints that I need 

what I've found is that this is a very liberating experience. Two and a half years in, a lot of the problems that I initially thought were really yucky, I'm now thinking, "well if I flip it on its head I can get what I need to and I
don't have the performance problem or I don't have the scaling problem or I don't have the centralization and trust problem or the regulatory problem. 

So I want to encourage you to do that. Think in terms of the edge, with a blockchain as a useful foundation that you can refer to but not necessarily as the place where it all happens. You don't have to compute everything in a smart contract. 

there are some problems that you must use blockchain for but I'm just saying use it wisely, and not just peanut butter spread it on everything. 

I would love to get some people here to work with me on this peer did method I think it's a very high value for the identity space that's one specific to my area of expertise so with that I'll go back and demo something if you want or we can go into QA I think we got about ten minutes
left which is good 

## Q&A [**^**](#contents)

<img src="https://i.imgur.com/HNmcUfN.png"/>

I was trying hard to not go till the very last second well it doesn't necessarily have to be a person but some entity on the edge yeah and I'm really using the term edge of course is really vague but what I mean by it mostly is it's not the thing in the center of the architecture diagram okay and then the second question the concept of the micro ledger is there any concept of persisting the final values of the micro ledger onto a blockchain yeah so this is if I go back to let's see the notion of anchoring something on a blockchain a number of people in industry are exploring different ways to do that and one of the things you could anchor on a blockchain is a micro ledger so if you needed to prove for example to a third party let's say Alice and Bob are interacting and it's it's a private personal relationship but let's say Bob doesn't fully trust Alice and maybe he's afraid that alice is gonna steal all of his cool music for his next album even because he's been sharing it with her so
he goes and he anchors some things on
the blockchain to provide evidence so
that if anybody ever you know if there's
ever an argument there's a third party
that's a witness that kind of a thing
and there's other kinds of use cases
like that too
hi so obviously it's a communication
protocol so I'm wondering if there was
any thoughts about communication
recording or if it could be useful in
any way I know there have been papers
for TLS communication recording but
obviously it's not easy to do at this
point with TLS and HTTPS so is there any
ideas about communication recording
between the agents or da DS and how it
could be possibly useful so that's an
interesting question I used to work at
Blue Coat which makes a line of products
actually blue coats been acquired by
Symantec so if you look this up now
online you're gonna have to look under
Symantec but anyway blue coat makes a
made a product called an SSL visibility
appliance and what it is is a
deliberately constructed
man-in-the-middle attack on a TLS
session so an enterprise does some fancy
magic with certificates to make it so
that when you inside the enterprise talk
to somebody outside the enterprise that
appliance catches the traffic and it man
in the Middle's both of you neither side
can tell that there's this thing in the
middle and the whole point of it is make
the TLS channel visible so that the
enterprise can look for malware that's
coming into the environment and stuff
like that so where I'm going with this
is that same kind of technique could be
used in agent to agent communication
however you would have to get the
consent of both ends of the conversation
you don't have the ability like you do
in an enterprise to simply say well
every browser in our enterprise is going
to accept this certificate authority
therefore nobody's going to get any
warnings when they click and and stuff
like that so self sovereign identity
technologies provide a protection
against that kind of sniffing happening
invisibly but it could be done and the
old the other thing I was going to say
is there's also a hype
a proposal about message tracing this is
cooperative voluntary message tracing
where people are trying to troubleshoot
a complex interaction and they say hey
please tell me when you get this message
and forward it on so that I can see
what's happening parties don't have to
follow it and but it's somewhat related
to recording so I I guess I can only
think of two those two comments about
the recording concept maybe we can talk
some more after Danny I actually have a
follow-up question and what what
happened here so I'm sure you're
familiar with signal in signal low using
a double ratchet it's right in Triple D
filmin and they create that end-to-end
encryption so how does this really
different when it comes to peer-to-peer
and then just creating that encryption
because you just mentioned that if
you're going to man in the middle attack
I'm quite familiar with what Bluecoat
does I work at Symantec as well so you
have access to the private key you are
able to record a session and then you're
able to replay it
so basically acting as a proxy so how
does this does not apply in this
scenario because if I'm able to actually
sit in between let's say I hold the
network and then I compromise one of the
parties then this is basically just a
broken channel well first of all indie
communication there's a this has not
been implemented but the hype has been
accepted is adopting signals double
ratchet algorithm so forward secrecy and
so forth is a property of the
communication channel the same way it
would be with signal the did method spec
that I talked about here one of the key
characteristics that it has is that when
you created did you must create it by
deriving it from the public key of a key
pair that exists and the reason that
that requirement exists is because you
don't want if you had it if you did well
let me take you down a different path if
if you started a D ID as just like let's
say some UUID and then later you
associated it with keys what could
happen is you could start it and a
person who's proactive and malicious
could notice what your D ID is
but you haven't asserted keys and jump
in and create the kind of man in a
middle situation that we're really
worried about here but because DIDS
require you to derive the thing from the
key the the did value from the key there
is no point in time where the creator of
the did is vulnerable to the man in the
middle attack that's only a partial
answer to your question let's talk about
it after yeah I had yet another
follow-up on this thread so the ietf has
a existing internet standard called the
host identity protocol and it does
exactly the same thing the intention
there is because right now in networks
there's the IP address is the identity
but this is not verifiable so they made
this protocol with the intention that it
existed to be compatible with the
Internet's tcp/ip stack so there is no
tie to and etherion network or a hyper
ledger implementation it's just part of
the general Internet can you give me
some context as to why this is existing
separate from that and we don't just use
the host identity protocol existing on
the internet already so that's a great
question there's several different
answers that are all kind of related
that kind of add up the first thing is
that this communication mechanism has to
work on things besides the Internet
so not everything has IP addresses and
still we have to be able to communicate
we certainly live in a highly IP centric
world but there's plenty of use cases
that are outside that the second thing
is that like with certificates my
understanding of the host identity
technology is that it focuses on servers
now of course it could be used for
clients and stuff too but TLS in general
even though it has
the option of identifying both parties
is almost a hundred percent used to
identify only the server side of an
interaction so when you want to identify
the client side what do you do you have
this great channel but you don't use
certificates you have an entirely
different mechanism which is
browser-based sessions and cookies and
all this other stuff to identify the
other party you log in you present some
credentials and I think the same kind of
phenomenon maybe is undermining some of
the value of that protocol where it's
it's going to be applied whether the
protocol is written that way or not it's
going to be applied just to identify
things that have a permanent presence
does it does it work for mobile phones
that are changing IP addresses
constantly and that are refreshing their
software and all that other stuff I
don't know enough to know maybe we can
can you share a link with me or
something and I'll go learn some more
about it
state channels are on my list of we're
right here
well state channels yeah the state
channels are an example of this kind of
thinking yeah I have one question
concerning the etch chain protocols as I
understood you you suggest we make small
protocols and different apps but what
when I want to glue them together
because they together build higher-level
protocols would I then try to make the
glue in the blockchain so things that
those protocols need store it there or
would I define let's say super H J chain
protocol
well yeah protocols are one of those
things that can be understood at there's
there's lower level ones and higher
level ones just like there's the OSI
stack and so forth in networking and you
can combine logical entities into bigger
constructs to make higher-level
protocols something that you said kind
of gets at this slide that I skipped
over one of the things that's different
between DAPs and edge chain protocols is
that edge chain protocols there there's
no set of apps that you have to have you
just need to have software that is
capable of playing all of the roles in
your protocol and it could be written by
ten different people and there could be
ten different providers of one of the
roles if you wanted right so think about
like buying a house we don't have only
one place that you go to get all the the
actors in the buy a house protocol and
yet DAPs are typically written where you
write a DAP that implements the whole
thing and so that's a little bit of a
paradigm shift
yeah yeah yeah
theirs doesn't have to be implemented on
server so it's not exactly micro
services but it's like that in the sense
that it's a bunch of little granular
things hi thanks this was really
interesting I was going to offer a bit
of nitpicking for the megaphone protocol
I think if you don't take in
consideration economic pressure
I think the protocol probably fall apart
because some people will be in such
situations that they'll be willing to
trade what they consider their important
identity to spam people nearby and
there'll be markets that will probably
show up saying hey if you can if you do
this for us we'll give you some money
and people might burn through their
identity because they don't see the
value of it or maybe they will try and
stack up multiple identities as much as
they can
obviously we we would expect this the
product or the system the overall
underlying self sovereign identity
system not to allow that but I think if
you don't count factor in economic
pressures especially for those of us who
are very poor like you won't be able to
expect some of the ways that the
protocol will be manipulated
that's good comment the the concept
document includes the notion that
megaphones have a volume and you can
select the volume if you say look I'm
tired and hungry and I'm a mom in an
airport and I have a baby and I need to
change the baby's diaper and I forgot a
diaper that's not a life-threatening
crisis so you don't need
life-threatening volume and so there's
probably different staking for different
levels of volume but I think there's
still you're right that there's
potential for abuse which is maybe one
of the reasons that nobody's been
working on it yet
okay well I think we should declare the
the session over and I'll be up here if
anybody wants to ask more questions a
couple of you asked me questions that I
want to get some more information about
if you just come and talk to me that'd
be great and thanks for your attention I
appreciate it


---

* [github.com/infominer33/DecentralizedID](https://github.com/infominer33/DecentralizedID)
* [infominer.id/DecentralizedID](https://infominer.id/DecentralizedID)
* [infominer.id](https://infominer.id)

