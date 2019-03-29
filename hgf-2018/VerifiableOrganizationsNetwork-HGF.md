---
title: Verifiable Organizations Network - A Production Government Deployment of Hyperledger Indy
description: Transcript of Presentation by John Jordan and Stephen Curran at HGF 2018
image: "https://infominer.id/images/VON.png"
---

# Hyperledger Global Forum 2018 — Verifiable Organizations Network 
**A Production Government Deployment of Hyperledger Indy**

---

<code>Editors Note: I've taken to working on youtube transcripts for podcasts and videos whos content is valuable and not readily accessible in text form, so that it will be easier for anyone to reference. -<a href="https://infominer.id">infominer</a></code>

---

-Published on Dec 27, 2018

[John Jordan](https://twitter.com/jljordan42), Province of British Columbia & [Stephen Curran](https://twitter.com/scurranC3I), [CloudCompass Computing](https://cloudcompass.ca/)

Learn about the Province of British Columbia's experience deploying the first Hyperledger Indy based production ecosystem.

The [Verifiable Organizations Network](https://vonx.io) (VON) enables governments and organizations to exchange data in trustworthy ways based on open standards and technology.

VON's founding members are governments who are, by law, trusted issuers of data about organizations. The Province of British Columbia, Province of Ontario and the Government of Canada have come together to create the initial services needed to establish VON. 

VON's founders have delivered new Indy-based open source components which form VON's backbone. [TheOrgBook](https://orgbook.gov.bc.ca/) is a publicly accessible repository of [verifiable claims](https://w3c.github.io/webpayments-ig/VCTF/charter/faq.html) about organizations. VON-X enables services to verify and issue credentials.

We present the Why, What and How including our strategy for bootstrapping VON using a two-sided market strategy.

<a href="https://youtu.be/g19VNv3DAd0"><img src="https://i.imgur.com/kODoTdj.png"/></a>

## Contents

* [Transcript](#transcript)
* [Introduction](#introduction)
* [Solving Problems](#solving-problems)
* [Collaboration](#collaboration)
* [Verifiable Proofs](#verifiable-proofs)
* [Chicken-or-Egg Dilemma](#chicken-or-egg-dilemma)
* [The Org Book](#the-org-book)
* [BCGov Org Book](#bc-gov-org-book)
* [Verifiable Credentials](#verifiable-credentials)
* [Production Network—Live 9-10-18](#production-networklive-9-10-18)
* [General Purpose](#general-purpose)
* [Ontario Org Book](#ontario-org-book)
* [Come to our Workshop](#come-to-our-workshop)
* [Bootstrapping Mechanism](#bootstrapping-mechanism)
* [dFlow](#dflow)
* [Just the First Step](#just-the-first-step)
* [Indy Catalyst](#indy-catalyst)
* [Serving the Public](#serving-the-public)
* [Q&A](#qa)
* [Home](https://infominer.id)

## Transcript

<code>**Editors Note** I just copy\pasted this youtube transcript, lightly edited for readability, and added screenshots for context.  -infominer</code>

**Pull Requests Welcome**

## Introduction

My name is John Jordan and I come from the province of British Columbia in Canada. This is my colleague Steven Curran we work together on this project.

I guess I'll just get started, and we'll have some slides, a demo, we should have some time for some questions

Ian is also here, one of our developers as well, he's a hyper ledger future developer. What we're gonna talk about today is what we're doing in the government of British Columbia, together with some of our peer provinces in the country — about how we're trying to solve some very long-standing difficult problems.

<img src="https://i.imgur.com/bf3lLTq.png"/>

>**we're gonna focus on business services today and talk about how the government can start to do the things that it does today in paper**, which it underpins the economy.
>
>**money exists because the government says so businesses exist because the government registers them and allows them to operate** and the laws and so forth of the of the government allow commerce to occur 
>
>**but we have no way of doing that in the digital economy right now** there's no business models in the digital economy other than basically buying stuff and getting your data exploited for advertising. so if you have a Visa card you're in. 
>
>otherwise there's no other really interesting transactions going on and I think big part of that is because **we don't have any way of extending the trust of government into the digital realm in a way that is trustworthy** 

<img src="https://i.imgur.com/BVVoGaA.png"/>

so we're going to talk about that this is our fun slide this is where we're from Canada with a variety of animals quite a lot of space we come from Victoria BC I norm I actually grew up in Ottawa which is around the beaver and people think that's kind of humorous but so there you go that's her that's
her 

<img src="https://i.imgur.com/UN0dT5b.png"/>

I also want to acknowledge that **I do all this work with [Carol Prest](https://www.linkedin.com/in/carol-prest-aa34b258/)** who is the registrar for BCS so I've been there for a couple years and **from day one we've been working together exploring how can we use the registry data as the foundational data for doing business.**  

Unfortunately she's not available she's in India right now, but having this business partnership and having her in her organization behind this, and having the discipline of trying to **solve problems for business people** is what is making this project really fun and also useful 

## Solving problems
<img src="https://i.imgur.com/MrIep94.png"/>

We're gonna focus on a problem here which is **how do we help small business** we have sort of a an example of Mary's bakery but **it could be any kind of business** construction mining whatever it is and the problem is that these business people are very excited about starting a business is an exciting time in life but they don't realize sometimes that **they have quite a lot of obligations that they must fill for government**

We have examples where our research teams have gone out and talked to restauranteurs and they have released a building and so forth it's the perfect spot everything is great **and then they realize oh I've got six months of permits and licenses to do because we had to bring it up to building code and they didn't realize this and then there's all these dependencies and they weren't ready to fund that building for six months** so those are like real stories **we'd like to try and minimize that kind of stuff** because we want them to start their businesses and grow.

<img src="https://i.imgur.com/FxeKL2D.png"/>

>you know the path is also very meandering and it can be in multiple different media you can be faxing you could be email you could be online you're in person and so forth.
>
>**All of this is a very difficult both for the business people but also on the government side**. We are also in different places verifying data all the time: who are you? whos business are you representing? Are you authorized to represent the businesses?

<img src="https://i.imgur.com/sIiI6Ni.png"/>

In the most complicated cases, for liquor and so forth, shareholders and employees have **criminal background checks.** They make sure that nobody owns more than 8 stores that sells liquor, and can take up to a year so.

## Collaboration

<img src="https://i.imgur.com/GM9FxgX.png"/>

We're collaborating with a couple of other jurisdictions. We're working with a team in **Ontario** and a
team **in the Government of Canada**, where I used to work, **The Procurement Agency**.

<img src="https://i.imgur.com/oPuhVyP.png"/>

**When we say working together, we're actually writing code together**. There's no MOUs, no steering committees, no work groups. They have a couple devs and the business person, we have a couple of devs and a business person. We sprint together, write code. 

All this stuff we're going to show you today has been co-developed, and significant portions have been done by each of the groups 

## Verifiable Proofs

<img src="https://i.imgur.com/0MS4yEs.png">

This is the journey that we'd like to enable, it's a journey that we know well. The government gives you something, you take that something to another institution, you use it to prove something and you get and you get the outcome.

In this case it's the incorporation information that's given to Mary, she goes to the bank and she can open a bank account. Turns out that's a very general pattern, and this is the pattern that we see in the verifiable credentials realm.

<img src="https://i.imgur.com/FNpnmLg.png"/>

So we have this pattern of: **holder** which *is a person or a business* but a business can't really hold something on their own. They have to have people holding it on behalf of the business. 

They presented to a verifier, which is earlier in the workflow, the verifier says bring your list of things in and prove to me who you are, and you have various permits and licenses and so forth. You then get to enter their form which is usually not that pleasant, and then you are issued something which you hold. 

**This is the pattern that we're very familiar with.**

We're sitting with a wallet full of these things. I have bank cards and identity cards and so forth and we're gonna explore how we can do that. 

When we discovered that **we were pretty excited** it was about a year ago that **we stumbled across Hyperledger Indy** after having done a little bit of work with fabric

So it was just Stephen and I on the team and we thought it looked promising, that there was this pattern here we could solve some of these hard problems we've been working on for years but we realized we didn't have any of the software for different organizations or people.

## Chicken-or-Egg Dilemma

<img src="https://i.imgur.com/hHn9SLm.png"/>

Somebody mentioned it this morning, the classic chicken and egg problem: we don't have any software out there that we can issue to our issuers, don't have software to issue. We realized, in this case government is a little bit special, which I don't like to say very often. 

It turns out our core business is issuing that's what we do every service we have is pretty much an issuer so we thought: what if we could give the services that we are dealing with in the business realm, somewhere to issue to? 

<img src="https://i.imgur.com/9IHbEkL.png"/>

We purposely picked business realm because if we're dealing with business data we're not triggering all the personal identifiable information problems. In the BC we call it FoIT, the Freedom of Information Act and Privacy Protection Act. When you get into personal data, of course it triggers all of that which, is good but makes it very complicated to play with new technologies. 

## The Org Book

<img src="https://i.imgur.com/6KxuQM9.png"/>

We just deal with open business data right now and we thought: what if we could create something where these issuers could issue data to? and it would be a public thing, and we call that **The Org Book.** 

This is a bootstrapping technique that we're copying from Facebook. We're just playing with one side of the market. **We're gonna deal with the supply side: the issuers of credentials, more commonly known as permits and licenses.**

<img src="https://i.imgur.com/o5KphnK.png"/>

Because they're public and because they're open we can create this directory of searchable verifiable data and we can build software for the issuers.

Our goal was how can we make it as easy as possible for existing services to be able to issue their credentials to this OrgBook starting with the foundational data of the registry, and we're going to show you that.

**When we started writing this code built on top of Hyperledger Indy we realized that there could be intermediate benefits.**

<img src="https://i.imgur.com/voKqoaF.png"/>

So first there's some public good, and the searching and finding of data will show you that. It turns out we can also create [api's](https://bcgov.github.io/MyGovBC-notification-server/docs/api-overview/) to allow that data to be searchable, and we created an [enterprise agent](https://github.com/bcgov/von_agent) for services to verify the data in The Org Book. 

So later when businesses have their own services for holding verifiable credentials, our issuers are ready.

<img src="https://i.imgur.com/AdYRiK9.png"/>

## BC Gov Org Book

Now I'm gonna hand it over to Stephen. This is what The Org Book looks like in British Columbia, so there's two instances and we'll show you them both but **this is the [British Columbia Org Book](https://orgbook.gov.bc.ca/en/home) and it's basically a kind of a Yelp type site.** 

<img src="https://i.imgur.com/nsurhhx.png"/>

**we've got five hundred twenty-five thousand active legal entities in British Columbia every one of them has a record in here** they have the credentials that the registries have issued to them 

<img src="https://i.imgur.com/ngfzaPh.png"/>

Let's do a search we're into chocolate because we're in Switzerland so we'll talk about a Vancouver Island chocolatier. Purdy's chocolates, we can take a look at them. Search capability names we've got other capabilities for what searches we can provide ways to filter and things. When we get into it, we can see some information that the registry publishes, so previously registered. 

<img src="https://i.imgur.com/0mcU9ru.png"/>

**9:41** This is all public data, this is all open data. This is exactly what they hang on their walls inside the restaurant and things like that, there's really no place in BC it is actually published but in a very obscure places, very difficult to find. We've actually, as a byproduct of doing this exercise, created a pretty useful facility for citizens to use to find businesses, so we can take a look at them.

## Verifiable Credentials

<img src="https://i.imgur.com/yMMHV01.png"/>

this one has a couple of credentials they actually have a corporate entity and then a couple of names they do business under so [they've got several credentials](https://orgbook.gov.bc.ca/en/organization/BC0057742/cred/1902355) we can see a timeline of when they've got the different credentials so we can take a look at those in it and as the history builds up we haven't loaded all the history of all BC companies yet some of that is on paper which is going to be more challenging but that's that's not for us to worry about but we can load them up so if we can look at our registration we can see an active credential 

<img src="https://i.imgur.com/vmZx8py.png"/>

<img src="https://i.imgur.com/umWHJO7.png"/>

so this is what a credential looks like online basically we present it with the key data that a person might be interested in and then at the bottom we can actually go [into the credential](https://orgbook.gov.bc.ca/en/organization/BC0057742/cred/1902355/verify) from an Hyperledger Indy perspective 

<img src="https://i.imgur.com/l3LCLnu.png"/>

so this is the schema if you as they call it on the one side the populated data for this particular version of the
credential and then down below we get some really fun stuff 

this allows any citizen to go and do the cryptography on
paper themselves to prove that this is a proven credential yeah and we say verified see the check up there that's
the that's the key 

<img src="https://i.imgur.com/47eUSiL.png"/>

## Production Network—Live 9-10-18

okay I think that's most of what we wanted to show so the idea here that we wanted to talk about a little bit was the title of this, **this is a production system, we've been live since the 10th of September** 

<img src="https://i.imgur.com/cHws3Sb.png"/>

there's a little story there so let's go back to the home page and let me talk about a couple of things there the current statistics those are actual statistics we actually recreated the credentials and loaded them this week 

so that's why **2.6 million were issued this week** we can do that the first weekend in September when we loaded it, it took 10 days to load the credentials so that kind of wasn't too good.

**we had Ontario coming behind us with about five times as many credentials** so we were a little nervous and did a couple of sprints to scale up its capabilities 

BCGov, which has [the developers exchange](https://bcdevexchange.org/), is a pretty progressive environment for developing code. We've got a Red Hat open shift [kubernetes](https://kubernetes.io/) based platform 

so basically we were able to use the capabilities of that platform to just spin up other instances and be able to scale up the the speed of loading and things like that so we got up to 

we're now about 12 hours to load the full data set so we're creating issuing and holding about 2600 credentials per minute so decent speed it's kind of weird because we are a single holder for all of these organizations these don't the organizations don't have their own wallet and the first vision and the first thing that Indy wanted to support was the idea of a person having a wallet 

so the database behind it was not the most scalable solution out of the box so the next thing we did as well to to make it scalable was to implement say an enterprise-grade wallet with Postgres in was the developer on that and we were pleased that yesterday his code was merged into the Indy SDK repo so it's now officially hyperledger code, which is kind of cool. So that's a contribution we've made to the to the ecosystem in Hyperledger Indy.

## General Purpose

<img src="https://i.imgur.com/rrQSzsd.png"/>

So one of the things you're seeing, is this is a BC site, but it's really very generic so what we've tried to do is make it completely agnostic of what the actual credentials that will be loaded in.

We do have the concept that it's a an organization so we've got names, we have addresses, the concept of addresses, we have the concept of credential types, we have the concept of dates in there... but other than that the structure is whatever the issuer happens to issue so, it's very flexible for others to use.

<img src="https://i.imgur.com/sewb1Aq.png">

so that search that's up there is you know it was a decent amount of work uses solar and and and so on but is very generic so that other entities other jurisdictions can take this and basically spin up their own instance of this relatively easily using this code and be able to take advantage of the loading the naming the searching the display all of this is flexible and localized localizable 

## Ontario Org Book

<img src="https://i.imgur.com/PMpdfJ8.png"/>

let's take a look at the Ontario one so [The Ontario Org Book](https://www.von.gov.on.ca/) looks quite different from BCS obviously the search panel is the same they have different things they want to show and what they they don't want to show 

<img src="https://i.imgur.com/wfCQNDT.png"/>

so for example in Ontario they didn't want to show the structure of a company they actually have a contract that charges for that so they weren't able to do that through this 

so every entity and every doing business as is a separate entity on this so because we were building with multiple jurisdictions in mind right 

<img src="https://i.imgur.com/L97WeSB.png"/>

from the start we've we built it to be pretty flexible and so you're able to construct it on your own have your own skinning language support there's multiple language support is in there built in already I think those were the main things

## Come to our Workshop

<img src="https://i.imgur.com/GwrN03q.png"/>

the two more things that I wanted to touch on: **come to our workshop on Friday and Saturday** and what we're actually doing is building out issuers and verifiers

  * [Hands-On with Verifiable Organizations Network - Part 1](https://www.youtube.com/watch?v=R5TB-goL3_o&list=PL0MZ85B_96CGkWnEvdPy5sB4VRcH2XWuP&index=108)
  * [Hands-On with Verifiable Organizations Network - Part 2](https://www.youtube.com/watch?v=j-lM2hNq1TI&list=PL0MZ85B_96CGkWnEvdPy5sB4VRcH2XWuP&index=107)

<img src="https://i.imgur.com/PE065NM.png"/>

So this is The Org Book, the central piece. What really is important is there's an API behind all this that a issuer of permits can use to learn about the company to fetch the credentials that are already there and have them proven and then issue credentials back to the org book.

A key part of this is that being easily able to extend this to many more permits and licensing providers could be within the government which we're working with.

<img src="https://i.imgur.com/cdI0NGO.png"/>

almost every project team we talked to says "oh we can use that!" so we're building that out and trying to make that as easy as possible so our workshop on Friday involves building an issue or verifier and actually deploying it out so you can create your issue your own credentials 

<img src="https://i.imgur.com/QyOUf4G.png"/>

## Bootstrapping Mechanism

the other side of it that we think is going to be really important is well this is a bootstrapping mechanism we've realized there can be some life to this in that we're going to create we're going to be creating a pub sub subscription service basically so that a business that gets a credential and verifies it can subscribe to that credential in the future and get notified when it changes 

so a big challenge in all government organizations is this ability to understand when things change and we think this can be a super light way for a business to get notified that: 

"hey these two businesses just merged they've started a new entity", "those two entities no longer exist they've been dissolved in this new entity exists you should know that" and 

so that webhook capability will just whatever you're subscribed to when when our credential changes we can notify you that it happened and then you can dig in to figure out how that affects your permit and licensing service 

## dFlow

the other piece that we'll show is thing called decentralized flow - [dFlow](https://dflow.orgbook.gov.bc.ca) 

<img src="https://i.imgur.com/a8WzejN.png"/>

so do you wanna go to that okay spicy wings we're gonna look at Spicy Wings. This is our dev site, this is just new, that we're playing with. This is a company that's got four different credentials from different organizations.

<img src="https://i.imgur.com/jUyJEIk.png"/>

They've got a registration a PST that's a tax number from the province, a clearance letter for workman's compensation for a worker's insurance, and a business license from a from an entity from a municipality. 

<img src="https://i.imgur.com/2fQTCap.png"/>

So with [dFlow](https://dflow.orgbook.gov.bc.ca) what we can do is basically what you're saying is I have a goal as a businessman I have a goal that I want a business license in the city of Surrey and it's going to be for a restaurant what have I got to do to accomplish that what other things do I need and 

<img src="https://i.imgur.com/YSIIWLQ.png"/>

what we've built here is a [dynamic workflow](https://github.com/bcgov/dFlow) that starts with the one you want I want a business license, and says "what are the prerequisites for getting a business license?" well that's been encaptured in the proof requests that the business requires before it will issue you the credential that they have to offer.

<img src="https://i.imgur.com/PpzN2E9.png"/>

**19:34** so we can look at that proof require and then iteratively go back to that proof request and walk back a step and walk back a step all the way back until we get to the starting point and 

<img src="https://i.imgur.com/XQK4hH3.png"/>

now we can display dynamically what does that company need in order to get a business licencse there their goal and then what have they already got that allows them to proceed 

<img src="https://i.imgur.com/FvA5vMU.png"/>

so basically this company the ones in blue they already have and they can take a look at it the ones in yellow they're able to acquire now because they have all the prerequisites they haven't got it yet but they have the prerequisites for it and the ones in red they don't have the prerequisites they're just going to get rejected so no need to start in on those already 

<img src="https://i.imgur.com/Pmtg8km.png"/>

the nice thing about this is all of these entities that are issuing credentials that are issuing permits and licenses don't have to know the whole journey that that's really hard to figure out all they have to know is what their prerequisites are and as soon as they express those in the form of a proof request we can dynamically walk that chain and figure out what what else they need compare that with what's in their wallet what credentials they already have and now we can give them a picture of where they are all right if we got a minute 

<img src="https://i.imgur.com/ZdQrDU3.png"/>

**21:15** one of the things we're going to do in the workshop is in spinning up your issue or verifier is you'll have to connect to and create ended transactions on Indy blockchain on a distributed ledger 

so this is a tool we created to be able to browse the network so we can look at in this case the four node network that we've got running we can look at the status of it 

**21:50** we can do some operations like look at the Genesis transaction but we can also dig in and look at what are the transactions that actually exist on the ledger at this time 

<img src="https://i.imgur.com/J6I6GkD.png"/>

we can do some searching for things and find all the ones that have tax in the name we can search by types of in this case we're looking for schema 

<img src="https://i.imgur.com/QfgNVr1.png"/>

so this gives you a really good way of actually being able to see what is on the ledger you know get an idea as you register an issue or verifier take a look at what's there 

so that's kind of a preview of the site and the ideas that have been emerging as a result of our work but there's a little bit more 

## Just the First Step

<img src="https://i.imgur.com/kO6nCGy.png"/>

**22:55** one of the things that we're trying to do is, it's helpful for BC businesses but BC businesses do business all around the world and we want our businesses to be able to interact digitally with everybody else and like Steven mentioned it's not just businesses but it's professionals and so forth 

<img src="https://i.imgur.com/8tyRlCK.png"/>

this model could work for professional engineering societies medical societies other kinds of things that have public accreditation that you need to check on 

<img src="https://i.imgur.com/3O2CKLa.png"/>

**23:27** so we have this idea where we think The Org Book helps us establish our local neighborhood. businesses are gaining their credentials and and that's kind of building up our local ecosystem 

<img src="https://i.imgur.com/aYIYVha.png"/>

That makes it easier for us to help them find their way like we just demonstrated because each of these issuers are going to automatically be able to express digitally the preconditions that are necessary for them to be able to allow you into their service and an issue a new permit/ 

## Indy Catalyst

We think that's pretty pretty cool and as a result of this learning we've we've come up with this generalized model that has been accepted as a sub project of Indy. 

<img src="https://i.imgur.com/p8BME5z.png"/>

We're calling that [Indy Catalyst](https://github.com/bcgov/indy-catalyst) because this is sort of a bootstrapping capability, and that'll comprised of the code-behind [The Org Book](https://github.com/bcgov/TheOrgBook) in a more generalized fashion, and the code behind the issuer verifier service that we've built which we call [von-X](https://github.com/PSPC-SPAC-buyandsell/von-x) but we'll give some other sub named as an Indy Catalyst component.

## Serving the Public

The big reason behind this is because I work for the government of BC, we're not a software development agency, were serving the public.

We want this to be part of a global capability, and
having a sustainable set of software in a well governed organization like Hyperledger, the Linux Foundation, we think is a good way to go. 
**24:50**
We think that as these neighborhoods grow, hopefully well become will create what we call the verifiable organization Network 
**25:01** 

<img src="https://i.imgur.com/ANXXvan.png"/>

so this is sort of a concept where if you can use these kinds of tools and it doesn't have to be Hyperledger Indy it could  be any system that is decentralized identifier—verifiable credential compliant

you'll be able to exchange verifiable data amongst businesses and that is really what we want to be able to do it's nice that they could come and do business with us like get the things they need but what's really more important is it that they transact amongst themselves that's what the economy lives.

That's the idea of the Verifiable Organisation Network and the coming code that we'll call a Hyperledger Indy Catalyst, so that is our talk for now. 

<img src="https://i.imgur.com/dbHSiO7.png"/>

## Q&A

**25:40** as Steven mentioned **we're having a workshop Friday and Saturday morning** and Ian and Steven and I'll do my best to help will walk you through actually creating an issue we're
creating schemas and doing your own decentralized workflow example.

**we're happy to take questions** just wanted to check any **prerequesites for the workshop**, any required software components to be installed before hand: 

>you need a browser and you need a **docker hub ID** but you know you could do that while you're there yeah so the prerequisites are a docker hub ID and then everything else can be done in a browser and we've got all the guidance and so on but you don't need anything else I don't think about **Chrome** is ideal right chrome is probably the best we're using a tool called play with docker so you don't have to install anything on your machine it's super cool I promise no biometrics

so you did mention the verifiable claim and you you implied standards and I just want to confirm with the audience here because we had a side discussion. 

>it's w3c compliant verifiable claims and then and so I don't want to ask about the the other adjuncts that the registrar and the verifier because you talk about those concepts but I'm trying to understand what standards you use or what you're developing on your own and what standards apply specifically the registrar?

right so right now it's Hyperledger Indy version of things but as they progress they'll they'll create the ID doc specs and the end verifiable credential base

but that's still emerging right in terms of how the agents communicate we're actually contributing quite a bit
to sort of this agent agent protocol and that's being done in the open as well right now in this sort of Hyperledger
Indy working groups but we want interoperability 

we'd like our citizens to have a choice so they could use a DID method of their choice they could use software of their choice when it gets to personal data or this data we think if that's where the marketplace will provide options for citizens and businesses like the holder software so whatever standards emerge we would want to support those and we're helping shape some of those as well so 

there isn't a specific standard for the agent agent protocol but it's a collaboration with the decentralized identity foundation and the w3c folks and the hyper ledger folks yeah one of the things we thought about as John alluded to early in the talk was oh we're gonna build this thing in our organizations they're gonna use our agent and they're gonna talk to our issuers and verifiers and we're gonna build all that stuff and then we realize no this is not what we should be doing we shouldn't be in the business of doing that we need to be in the business of issuing credentials 

so we have to build software for that we need to make do it in a way that allows them to change as little as they need to we don't want them to have to read recreate their world we want them to just be an adjunct on just like they use a printer to print the verified credential the permit or the license so they can hang it on the wall we just want them to stamp out a digital version of that that's signed cryptographically right and 

one of the things I say about that is like so this piece of software that we've been we sort of we take it for granted now but everything we've done is in the open every line of code every presentation every ticket it's all in github so it's all patchy 

I mentioned we're contributing to the Hyperledger thing but sort of a line I say is like if your system can produce a CSV of your permit or license data then you're in our box we'll take care of the rest 

you'll learn on the workshop that it's just an hour to to configure that thing to make it work for you and and that's how much work it takes kind of thing 

we're trying to make it as easy as possible because we're from government we know like it's basically impossible to do IT things so we wanted to like you know make that as simple as possible 

you have the concept of in this case the org book is the wallet right, and the issuers issued to it but it'll be using the same protocols in the future to issue two individual wallets which is the demand side right that sort of goes closely to the question I was going to ask 

which is one of the points of blockchain is usually to have nodes under control of multiple entities where are the actual nodes right now from what I understand they're all under the control of the BC government so could there be like variances like an NGO holding onto one of the nodes, the production systems using the sovereign network to store the DID 

there's a DID and a schema and a clerk read that you know credential definition and yeah on there but again in theory that could be another DID Network it's just there
aren't any other DID networks 

so we're not gonna run the network we don't want to be running node but we're not running the network um the the thing you remember with verifiable credentials is they don't go on the ledger so none of the data about the organization's or about individuals goes on the ledger it all goes into a wallet

the weird thing we are doing is we've got this community wallet concept but once people have their own wallet we'll be issuing to their wallet directly we won't we may continue to issue to our own community wallet but for public credentials but for any other for the credentials once they have a wallet will be issuing to that wallet and they will be able to use it wherever they need to use it in whatever jurisdiction has systems that allow it 

we are doing some collaboration with some folks from spark Telecom New Zealand that have a pretty nice implementation and we're using that as an opportunity to develop the early version of the agent agent protocol that's generalized 

so as soon as we get code that map we had originally that just had Ontario and and Ottawa on it will expand to include New Zealand so we're looking forward to that and others 

the schema you used for business registration is something that came from a standard about business registration or Ontario's doing the same one so that you guys just like get together in a darkroom and created or New Zealand I mean what happens with that 

it's a schema that we co-created with Canada and Ontario
but we also looked at like standards in Canada that have evolved like I've been in this business for very it's not an ISO no no no there isn't such a thing in the world for that for businesses other than like maybe schema.org but it's
really not sufficient yeah so we evolved it together and so far
it's working you know 

it's a bit tricky to get the minimal set but but again this helped with having multiple jurisdictions involved so we had a first, we did Ontario and we went wait this isn't gonna work we don't want that we're both Canadian entities we should be able to figure that out and that worked pretty well and then the other side of it was 

once we got into things like the the doing business as well that's totally uncharted territory no not really yeah been done and we came up with something, Ontario came up with something even better, and we balance back and forth to figure out what a real 

it's actually a relationship credential so we can have it point both ways the interesting thing there the thought process was a lot around we originally started oh you know how is The Org Book gonna show this and all that then we realized no that's not the right thinking what the thinking is is what is the business gonna want to do with this

what do they have to prove to somebody else and that's how you look at how how to build a credential is you stick it in the wallet of a business in this case or a person and figure out okay they've got to prove this to show that they're a
partnership to the bank how are they gonna do that and 

that's the sort of mindset we had in building credentials so we built this so that's where the relationship credential came from which is I was very happy about because it's basically the edge in a graph so I'm terminal like that idea 

the registration credentials are the nodes and this is a credential that demonstrates a linkage between the nodes of a knowning doing businesses name but that that those labels could be changed to is a director or as a beneficiary or any kind of relationship can be modeled this way between two things and so that generalizes the model to basically whatever you want which also gives it interesting properties in terms of visualization and analysis and relationship recommendation engines and that kind of stuff so it was fun hospital systems 

we're gonna be talking with man Revere you know that's what an interesting thing is that you know like if you look at you know College of Physicians and Surgeons and other kind of public statements my you know engineering societies they publish these things already so they could have a version of this and then that just becomes part of the overall ecosystem so that you can for example have a prescription issued by a doctor to patient that patient brings the prescription to a pharmacy the pharmacy asks proof but at the same time can look at that credential say oh I'm gonna look up that doctor in this in the public you know verify in public doc hub or whatever the heck they call it and and they can subscribe to those things too so they can always know if that doctor currently licensed maybe that doctor has a restriction on the kinds of things they can prescribe so I think it's like it's a it's complementary to the peer-to-peer transaction when you have these public sort of hubs of trusted data we don't have them loaded today now like you come to the workshop we could
build another interesting one we're looking at is evident evidence so another function and the provincial
government is mining inspections things 
like this so inspectors go out into the field out like offline and they are recording videos taking pictures making
notes and so forth and they would like to be able to be used data that they gather five you ten years from now and
be able to answer the question definitively it was this person using this device on this place at this time
and it data was unaltered well that's a credential you could have their phone issue a credential to an internal hub of
like this and you know ten years from now when there's a court case they can use that you can just ask for a proof
from it and at that point we know that it's unaltered and and we know who it was and we know what version it was and
what chunk of binary data was hashed in there
so we had to experiment with that that could be quite an interesting matter all right we're just about done any other
questions or great well hopefully some of you will come for a workshop and thanks for your time
[Applause]
