---
published: false
---

# WorkingGroupNewsletterDigest

## DID Working Group

* [https://www.w3.org/2019/did-wg/](https://www.w3.org/2019/did-wg/) - Website

* [https://lists.w3.org/Archives/Public/public-did-wg/](https://lists.w3.org/Archives/Public/public-did-wg/) - LIst Archives

Hot Threads

* [Current status of DID Core implementations (June 2021)](https://lists.w3.org/Archives/Public/public-did-wg/2021Jun/0012.html)

Our latest implementation report for DID Core is available here:

* [https://w3c.github.io/did-test-suite/#spec-statement-summary](https://w3c.github.io/did-test-suite/%23spec-statement-summary)

Here are the remaining items that the WG needs to discuss on the upcoming call:

#1: Are the hl, relativeRef, and service implementations independent enough?

* [...]

#2: Are we letting the JSON serialization keep unimplemented features?

* [...]

#3: What are we going to do with deactivated, nextUpdate, and nextVersionId?

* [Negative press related to DIDs and VCs](https://lists.w3.org/Archives/Public/public-did-wg/2021Jun/0032.html) Manu Sporny (29 June)

Just drawing your attention towards this:

* [https://twitter.com/harryhalpin/status/1409615372538548227](https://twitter.com/harryhalpin/status/1409615372538548227)

![https://www.notion.soimages/image2.png](https://www.notion.soimages/image2.png)

* [https://lists.w3.org/Archives/Public/semantic-web/2021May/0177.html](https://lists.w3.org/Archives/Public/semantic-web/2021May/0177.html)

These are things that I would expect we would normally just ignore, but I've received a number of private emails over the tweet above from various decision making parties inside the EU requesting that we respond publicly to theses sorts of accusations.

The accusations are being taken seriously by some because Harry Halpin is ex-W3C staff. Also note that he his company is developing "competing technology" to DIDs and VCs.

Just raising awareness here as Harry's campaign is having a negative effect on adoption of VCs and DIDs.

Ted Thibodeau Jr Shares

it was not the only nor the first related tweet emanating from Harry --

* [https://twitter.com/search?q=W3C%20(DID%20OR%20%22Verifiable%20Credentials%22%20OR%20VCs)%20(from%3Aharryhalpin)&src=typed_query&f=live](https://twitter.com/search?q%3DW3C%2520(DID%2520OR%2520%2522Verifiable%2520Credentials%2522%2520OR%2520VCs)%2520(from%253Aharryhalpin)%26src%3Dtyped_query%26f%3Dlive)

Nor has he limited his commentary to Twitter --

* [https://www.google.com/search?q=W3C+(DID+OR+%22Verifiable+Credentials%22+OR+VCs)+%22harry+halpin%22](https://www.google.com/search?q%3DW3C%2B(DID%2BOR%2B%2522Verifiable%2BCredentials%2522%2BOR%2BVCs)%2B%2522harry%2Bhalpin%2522)

* [Subject Identifiers (IETF SECEVENT)](https://lists.w3.org/Archives/Public/public-did-wg/2021Apr/0017.html) Justin Richer (9 April)

The Security Events working group in the IETF (SECEVENT) has a standards-track draft for describing “subject identifiers” in various contexts.

* [https://tools.ietf.org/id/draft-ietf-secevent-subject-identifiers-07.html](https://tools.ietf.org/id/draft-ietf-secevent-subject-identifiers-07.html)

In short, it’s a way to say “this item is an email and here’s its value”, or “this item is an issuer/subject pair, here are those values”. This is useful in a variety of contexts where you want to identify someone but might have a variety of ways to do so.

I spoke with the editor of the draft to propose that we add a “did” format into this document, now that DID core is reasonably stable and the CR is published. She agreed that it would make sense but would rather have the experts in the DID community propose the actual text for the added section.

## Credentials Community Group

* [https://github.com/w3c-ccg/](https://github.com/w3c-ccg/meetings) - GitHub

* [https://www.w3.org/community/credentials/](https://www.w3.org/community/credentials/) - W3C Community Page

* [https://lists.w3.org/Archives/Public/public-credentials/](https://lists.w3.org/Archives/Public/public-credentials/) - Mailing List Arcives

* [https://w3c-ccg.github.io/](https://w3c-ccg.github.io/) - GItHub Pages Site

Hot Threads

* [2 special topics IIWs](https://lists.w3.org/Archives/Public/public-credentials/2021Jun/0293.html) Kaliya IDwoman

we are pulling together these as an experiment based on feedback from the community in the closing circle of the last IIW.

1) User-Experience and SSI on July 22nd. 8am - 2pm pacific time.

* [www.eventbrite.com/e/159946001797/?discount=CCG_25](http://www.eventbrite.com/e/159946001797/?discount%3DCCG_25)

2) The Business of SSI on August 4th 8am-2pm pacific time.

* [https://www.eventbrite.com/e/the-business-of-ssi-an-iiw-special-topic-12-day-virtual-event-tickets-161249943923](https://www.eventbrite.com/e/the-business-of-ssi-an-iiw-special-topic-12-day-virtual-event-tickets-161249943923)

We also have [IIW33 set now as a virtual event October 12-14](https://www.eventbrite.com/e/internet-identity-workshop-iiwxxxiii-33-2021b-tickets-160257990965) - we had too much uncertainty around travel for folks outside the US who are now 50% of attendees, delta+ variants, fires in California at that time of year and wanting to provide hybrid participation options and not having time.


* [Fake CDC vax cards now being sold to anti-vaxxers](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0077.html)  Moses Ma (Thursday, 8 April)

Just wanted to share this with those working on C19 vax certs:

From: [https://www.infosecurity-magazine.com/news/scammers-sell-fake-covid19/](https://www.infosecurity-magazine.com/news/scammers-sell-fake-covid19/)

The security firm DomainTools claims to have seen authentic-looking CDC cards selling for as little as $20 each on domains like covid-19vaccinationcards[.]com, which features a Let’s Encrypt TLS certificate. “Though selling a printed card is not necessarily illegal, the pricing, logo and cardstock of these ‘vaccination records’ demonstrate a level of intent to pass as legitimate cards from the CDC,” explained DomainTools senior security researcher, Chad Anderson.

and

From: [https://www.tomsguide.com/news/fake-covid-vaccination-cards](https://www.tomsguide.com/news/fake-covid-vaccination-cards)

Israeli security firm Check Point reports that fake American and Russian vaccination certificates are being sold online for between $100 and $200. Fake COVID-19 negative test results cost as little as $25, while (likely fake) COVID-19 vaccine sells for about $500 per vial.

* [Vaccination Certificate Test Suite](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0081.html)  Manu Sporny (Thursday, 8 April)

As some of you know, a few of the members in the W3C Credentials Community Group have been working on a Vaccination Certificate Vocabulary[1]. The World Health Organization has recently published a Release Candidate data model dictionary for Smart Vaccination Cards[2]. The CCG has also been working on a Verifiable Credentials HTTP API[3].

The WHO guidance covers 28 types of vaccines that we (as a global society)

depend on, including Measles, Smallpox, Polio, Yellow Fever, COVID-19, and

others. We (Digital Bazaar) thought it might be interesting to see if we could

create an interoperability test suite for the WHO Smart Vaccination Card work using the tools listed above.

...

- A test suite containing 1,624 tests covering the

28 vaccine types in the WHO vocabulary.

- 7 independent vendor implementations issuing and

verifying each others WHO Smart Vaccination Cards.

- 1,623 passing tests demonstrating true

interoperability!

You can view the latest Vaccination Certificate test suite report here:

* [https://w3id.org/vaccination/interop-reports](https://w3id.org/vaccination/interop-reports)



* [Regarding CBOR-LD Web Transports](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0100.html)  Orie Steele (Saturday, 10 April)
  > I pushed up this small demo showing how to transport JSON-LD as CBOR-LD over QR Code and Web NFC.
* [transmute-industries/cbor-ld-web-transports](https://github.com/transmute-industries/cbor-ld-web-transports) github
* [CBOR-LD stabilization (was: Re: Regarding CBOR-LD Web Transports)](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0127.html)  Manu Sporny (Wednesday, 21 April)
  > Digital Bazaar has a few updates to share with the community.
  > 
  > 1. With a huge thank you to Dave Longley, a new version of the CBOR-LD library, with generalized and stable algorithms, and that works in the browser and node.js, has been released:
  > 
  > [https://github.com/digitalbazaar/cborld](https://github.com/digitalbazaar/cborld)
  > 
  > 2. We have split out the CBOR-LD command line interface into a separate project:
  > 
  > [https://github.com/digitalbazaar/cborld-cli/tree/initial](https://github.com/digitalbazaar/cborld-cli/tree/initial)
  > 
  > 1. DB has released a CBOR-LD to QR Code image library for encoding and decoding Verifiable Presentations:
  > 
  > [https://github.com/digitalbazaar/vpqr](https://github.com/digitalbazaar/vpqr)
  > 
  > 1. After some consultation with Mattr and Transmute, we've settled on a base32 alphanumeric QR Code encoding that is 10% more  space efficient than base64url byte mode. This is important because this format is compatible with hundreds of QR Code readers on the market. Every QR Code reader that we've tested has worked with this new format.

* [Zero Trust Architecture in the White House Executive Order on Cybersecurity](https://lists.w3.org/Archives/Public/public-credentials/2021May/0062.html) Adrian Gropper (Friday, 14 May)

Please read Section 3 in the EO

* […]

It may be time for us to explain Zero-Trust Architecture relationship to

VCs and DIDs. My not-so-hidden agenda includes priority for considering

authorization and delegation in our protocol work but our diverse community of security experts will surely make this a much broader discussion.

* [Executive Order on Improving the Nation’s Cybersecurity](https://comms.wiley.law/e/knewjcfglctwt7w/a7406307-5755-44fa-a5c5-22dd04d9e9a7)

Sec. 3.  Modernizing Federal Government Cybersecurity.

(a)  To keep pace with today’s dynamic and increasingly sophisticated cyber threat environment, the Federal Government must take decisive steps to modernize its approach to cybersecurity, including by increasing the Federal Government’s visibility into threats, while protecting privacy and civil liberties.  The Federal Government must adopt security best practices; advance toward Zero Trust Architecture; accelerate movement to secure cloud services, including Software as a Service (SaaS), Infrastructure as a Service (IaaS), and Platform as a Service (PaaS); centralize and streamline access to cybersecurity data to drive analytics for identifying and managing cybersecurity risks; and invest in both technology and personnel to match these modernization goals.

* [One subject, 2 VCs, 2 duplicate properties](https://lists.w3.org/Archives/Public/public-credentials/2021May/0075.html) Michael Herman (Trusted Digital Web) (Tuesday, 18 May)

*   Erin is the Subject of 2 Verifiable Credentials: VC1 and VC2

*   VC1 has 2 properties: "age" and "hairColor"

*   VC2 has the same 2 properties (by name): "age" and "hairColor"

Questions

1.  Assuming VC1 and VC2 apply/are valid at the same instant in time, can the value of the "age" property (or the "hairColor" property) be different in V1 compared to V2?

2.  What makes sense? ...what is realistic? ...how should VCs behave in this regard?

* [RE: Cryptographically Enforceable Issuer Policies (forked](https://lists.w3.org/Archives/Public/public-credentials/2021May/0108.html) Joosten, H.J.M. (Rieks) (Friday, 21 May)

Before answering your question, let me tell you this is still stuff we are coming to grips with - it is the subject of a masters thesis that Naveena Anaigoundanpudur Karthikeyan is working on with TNO. So what I write below are ideas that I still need to see verified.

* [...]

parties that issue credentials under such a policy must (be able to) determine

*   That he attributes that a KeySmith uses to generate decryption keys are sufficient for expressing its policy

*   That the process that the KeySmith uses to validate the attributes that parties provide as they request a decryption key, provides sufficient assurance that the (cryptograhpic) evaluation of the policy is also valid. And I think this is the trickiest part.

From: Steve Magennis

Subject: RE: One subject, 2 VCs, 2 duplicate properties

... forking the conversation r.e. Cryptographically Enforceable Issuer Policies @Joosten, H.J.M. (Rieks), how would it be  determined if a Verifier satisfies policy conditions? Really interesting idea.

* [CCG 101 - Help us know what is needed!](https://lists.w3.org/Archives/Public/public-credentials/2021May/0150.html) Victor Syntez (Tuesday, 25 May)

I've invited you to fill out the following form:

CCG 101 - Help us know what’s needed!

To fill it out, visit:

* [https://docs.google.com/forms/d/e/1FAIpQLSe3OakcEg8IfWXYALg10eiii2hiLKq2vXC-yazpPk0QVzIMzQ/viewform?vc=0&amp;c=0&amp;w=1&amp;flr=0&amp;usp=mail_form_link](https://docs.google.com/forms/d/e/1FAIpQLSe3OakcEg8IfWXYALg10eiii2hiLKq2vXC-yazpPk0QVzIMzQ/viewform?vc%3D0%26amp;c%3D0%26amp;w%3D1%26amp;flr%3D0%26amp;usp%3Dmail_form_link)

* [CCG updates to cgbot and scribe-tool](https://lists.w3.org/Archives/Public/public-credentials/2021May/0169.html)  Manu Sporny (Sunday, 30 May)

New CCG infrastructure features:

- Auto-presence - No one is required to present+ themselves any more. The cgbot does it for us now, saving our feeble sausage fingers from being over exerted.
- The Ryan Grant, Who We All Know And Love, Would Like To Know Where The Raw Transcripts Are Feature - When the cgbot closes out the meeting, it will let everyone in IRC know where the raw transcripts, audio, and video files are so anyone can download them and/or remix them to spread CCG propaganda. This will hopefully also save Heather from having to document yet another piece of tribal CCG knowledge.
- The You Exist Even Though You're Not in people.json Feature - When someone is present+'d, which is anyone that joins the call now thanks to auto-presence, that person will show up in the attendees list. This achieves two things 1) the poor minutes publisher can update the people.json at their leisure instead of being blocked by it whenever a new person shows up to a call, and 2) we get a more accurate record of attendees.
- The Fellow Jitser Invisibility Decloaker Feature - If you join the meeting with a new browser, or in Incognito mode, and you change your name from "Fellow Jister" to your preferred name, you never show up in the attendee list. People that change their names now show up in the attendee list. If you want to stay pseudonymous just give yourself an unrecognizable name... like "Robot Overlord".

* [...]

These are baby steps towards an attempt at auto-transcription and auto-publication of minutes. There are a few things that aren't automated yet (like auto-detecting the meeting name)... ETA on those upgrades is unknown since all these upgrades are on a best effort basis.

* [[CEIP] Draft paper on Cryptographically Enforceable Issuer Policies](https://lists.w3.org/Archives/Public/public-credentials/2021May/0170.html)  Joosten, H.J.M. (Rieks) May 30

my colleague Sterre and I drafted [a paper that we provisionally called Cryptographically Enforceable Issuer Policies](https://docs.google.com/document/d/1c8kIUqB2BBzM3usfD0_s5wu_z6K2KndzJ4uK_oZcPOs/edit?usp%3Dsharing), which describes our current thinking on this topic.

The paper isn’t finished. We need more text in the ‘discussions’ section, and hope that by making the draft available we’ll get the discussions that we (or you?) can describe in there. Also, we might have missed stuff that you as a reader need for a proper understanding of what this is all about, and to start pondering for what (other) purposes all this might be used. Or why this proposal is a very bad idea that we should not spend any more time on.

* [VC HTTP Authorization Conversation](https://lists.w3.org/Archives/Public/public-credentials/2021Jun/0009.html) Adrian Gropper June 2

The diversity of our community is a plus. To begin a conversation on VC access controls, I suggest this short intro to the differences between OAuth 2.0 and GNAP:

* [https://www.ietf.org/archive/id/draft-ietf-gnap-core-protocol-05.html#name-compared-to-oauth-20](https://www.ietf.org/archive/id/draft-ietf-gnap-core-protocol-05.html%23name-compared-to-oauth-20)

My goal is to arrive at a shared understanding of what would be minimum needed to support both OAuth2 and GNAP for securing access to a VC.

* [Identifiers in Verifiable Credentials](https://lists.w3.org/Archives/Public/public-credentials/2021Jun/0023.html) Kerri Lemoie June 6

"When expressing statements about a specific thing, such as a person, product, or organization, it is often useful to use some kind of identifier so that others can express statements about the same thing. This specification defines the optional id property for such identifiers. The id property is intended to unambiguously refer to an object, such as a person, product, or organization. Using the id property allows for the expression of statements about specific things in the verifiable credential."

In the credentialSubject property it seems clear that the id can represent the subject that the claim is about but I’m not clear on the uses for the optional id in the vc assertion. It would be helpful to learn about some examples or suggested uses.

For some context: in VC-EDU, we’re discussing Open Badges as VCs. Open Badges have historically mostly been verified via issuer hosted URLs.  One of the reasons to move away from hosted URLs is to remove the dependence on the issuer for verification. However, there may continue to be use cases for when an Open Badge should still be verified through its hosted url.

* [Selective Disclosure of lists](https://lists.w3.org/Archives/Public/public-credentials/2021Jun/0048.html) David Chadwick June 8

The user's VC has a property with a list of values (e.g. names of role holders). The user only wants to disclose n of m of this list to the verifier.

How can the verifier determine the difference between

i) a list with only n entries

ii) a list that has more than n entries but the user has withheld some of them.

Then we have the case where

iii) the list is genuinely empty because e.g. the role, has not been assigned to anyone yet, and

iv) the user does not want to tell the verifier any of the list values.

Re: Understanding @contexts and credentialSchemas Jun 10

This won't be a complete answer, but at the time of publication I believe that field was used in 2 ways.

1. with json schema, see this for example -

* [https://w3c-ccg.github.io/vc-json-schemas/](https://w3c-ccg.github.io/vc-json-schemas/)

2. with hyperledger indy zkp-cl signature vc's

In both cases, "credentialSchemas" was more about the VC data shape and type, whereas contexts and JSON-LD are best used only for semantics.

There are other tools like SHACL that can help do linked data shape constraints, perhaps someone might use them with credentialSchemas in the future.

but AFAIK, "credentialSchemas" is focused on the credential data shape. And "@context" is focused on the semantics and term definitions used in the credential.

OS

On Wed, Jun 9, 2021 at 5:15 PM Kerri Lemoie <klemoie@concentricsky.com>

wrote:

> Hello all,

>

> I’m reviewing this: [https://www.w3.org/TR/vc-data-model/#data-schemas](https://www.w3.org/TR/vc-data-model/%23data-schemas)

>

> Could folks please explain to me the uses of credentialSchemas in

> comparison to @context files in JSON-LD? Is it that @context files name the

> attributes and credentialSchemas provide the information about how to

> validate the data/semantics?

* [California Digital Vaccine Record based on VCs](https://lists.w3.org/Archives/Public/public-credentials/2021Jun/0191.html) Heather Vescent June 18

May be of interest: [https://www.latimes.com/california/story/2021-06-18/california-unveils-system-to-provide-digital-covid-19-vaccine-records](https://www.latimes.com/california/story/2021-06-18/california-unveils-system-to-provide-digital-covid-19-vaccine-records)

SMART Health Card Framework: [https://vci.org/about#smart-health](https://vci.org/about%23smart-health)

To achieve this purpose, the founding members of VCI™ have collaborated to develop (1) the SMART Health Cards Framework Implementation Guide based on the World Wide Web Consortium (W3C) Verifiable Credential and Health Level 7 (HL7) SMART on FHIR standards, and (2) the SMART Health Cards: Vaccination & Testing Implementation Guide.

If you are in California, you can get your vaccine record here: [https://myvaccinerecord.cdph.ca.gov/](https://myvaccinerecord.cdph.ca.gov/)

* [Re: The dangers of using VCs as permission tokens (was: PROPOSALs for VC HTTP API call on 2021-06-22)](https://lists.w3.org/Archives/Public/public-credentials/2021Jun/0244.html) Manu Sporny

On 6/24/21 12:35 PM, Kyle Den Hartog wrote:

> Agreed, when it comes to the number of checks that occur it's much greater

> because of the delegation. With that in mind, looking at the semantics only

> of the system VCs in my opinion weren't optimally designed for permission

> tokens. This difference between the two requires that an implementation

> that wants to support both claims tokens and permissions tokens has to

> grapple with the different mental model that arise when trying to stuff

> these things together. This introduces additional complexity. Additionally

> it leads to weird statements that are being made where it's difficult to

> tell if the VC is behaving like a claims token or a permissions token.

Yes, exactly this. Exactly what Kyle states above is the reason why it's so complicated (and thus dangerous) to use VCs as permissions tokens.

This is one of the primary reasons that we separated out the Authorization Capabilities work from the Verifiable Credentials work. Things get really complicated when you start mixing authz/authn/claims/permissions into a Verifiable Credential. Just because you can do it doesn't mean you should.

Much of the complexity that gets created in such a system that mixes all those concepts together goes away when you clearly separate claims tokens from permissions tokens.

I suggest that folks take a look at Kyle's post to see how intractable the problem becomes when you don't do proper separation of concerns and depend on attributes to convey permissions:

* [https://kyledenhartog.com/example-authz-with-VCs/](https://kyledenhartog.com/example-authz-with-VCs/)