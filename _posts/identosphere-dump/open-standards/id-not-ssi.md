---
published: false
---

# Existing ID Standards Based Tech

## Explainer
### Identity not SSI

* [FIDO: Everything You Need to Know About Fast Identity Online](https://www.pingidentity.com/en/company/blog/posts/2021/fast-identity-online-fido.html)
* [Directory of Products That Assess Identification Documents and Verify Identity Version 2.0](https://diacc.ca/2021/05/03/directory-of-products-that-assess-identification-documents-and-verify-identity-version-2-0/)

This [Directory](https://diacc.ca/2020/05/21/directory-products-assess-identification-documents-verify-identity/) is designed to provide an overview of providers’ solutions which use government issued photo identification cards, combined with biometric facial scans, to establish Digital Identity.

* [101 Session: OpenID Connect](https://iiw.idcommons.net/1B/_101_Session:_OpenID_Connect) by Mike Jones

Described at: [https://openid.net/connect/](https://openid.net/connect/)

Built on standards: OAuth 2.0 and JWT

See the presentation at [https://self-issued.info/?p=2167](https://self-issued.info/?p%3D2167).

* [101 Session: OAuth2](https://iiw.idcommons.net/2B/_101_Session:_OAuth2) by Aaron Parecki

* [https://aaronparecki.com/tag/iiw](https://aaronparecki.com/tag/iiw)

* [https://aaronparecki.com/tag/oauth2](https://aaronparecki.com/tag/oauth2)

* [OAuth 2.0 Simplified](https://aaronparecki.com/oauth-2-simplified/) is a guide to OAuth 2.0 focused on writing clients that gives a clear overview of the spec at an introductory level.

In 2017, I published a longer version of this guide as a book, available on [oauth.com](https://oauth.com/) as well as [a print version](https://oauth2simplified.com). The book guides you through building an OAuth server, and covers many details that are not part of the spec. I published this book in conjunction with [Okta](https://developer.okta.com/).

* [https://speakerdeck.com/aaronpk/oauth-101-internet-identity-workshop-xxxi](https://speakerdeck.com/aaronpk/oauth-101-internet-identity-workshop-xxxi)

* [How OAuth Works](https://www.youtube.com/watch?v%3Dg_aVPdwBTfw%26list%3DPLRyLn6THA5wN05b3qJ6N0OpL3YbritKI-) 12 videos

* [101 Session: UMA - User Manged Access](https://iiw.idcommons.net/3B/_101_Session:_UMA_-_User_Managed_Access) by Eve Maler and George Fletcher


* [OpenID Connect Claims Aggregation](https://iiw.idcommons.net/5B/_OpenID_Connect_Claims_Aggregation) by Nat Sakimura, Edmund Jay, Kristina Yasuda
[2021-04-21_OpenID Connect Claims Aggregation](https://docs.google.com/presentation/d/1w-rmwZoLiFWczJ4chXuxhY0OsgHQmlIimS2TNlce4UU/edit?usp%3Dsharing)

* [OpenID Connect 4 Identity Assurance](https://iiw.idcommons.net/10J/_OpenID_Connect_4_Identity_Assurance) by Torsten Lodderstedt
  > [https://www.slideshare.net/TorstenLodderstedt/openid-connect-4-identity-assurance-at-iiw-32](https://www.slideshare.net/TorstenLodderstedt/openid-connect-4-identity-assurance-at-iiw-32)
  > 
  > Jacob Dilles proposed to allow RPs to use handles for pre-configured eKYC requests. I filled an issue for discussion by the WG ([https://bitbucket.org/openid/ekyc-ida/issues/1245/pre-configured-claims-ekyc-requests](https://bitbucket.org/openid/ekyc-ida/issues/1245/pre-configured-claims-ekyc-requests).

* [OpenID Connect: Session Management vs Privacy](https://iiw.idcommons.net/11M/_OpenID_Connect:_Session_Management_vs_Privacy) by David Waite

To recap:

- Front-channel logout is simple
- …but brittle and doesn’t give good security guarantees
- Back-channel logout is robust
- …but difficult to implement/support, can still miss signals
- Session Management is useful for some apps
- …but is broken in many browsers

On their own independent schedules, all browsers have either broken or have plans to break state sharing via cross-site iframes to limit user tracking - arguably making the Session Management approach unusable.

* [Browser APIs to enable OpenID Session Management and Privacy](https://iiw.idcommons.net/13L/_Browser_APIs_to_enable_OpenID_Session_Management_and_Privacy) by Sam Goto

How does logout in OIDC happen?

- Classification problem - browsers do not know it is a logout now
- Easiest way
- Browser asks for a user consent
- Hard from a permission implementation perspective
- Tim: No issues with this idea
- If user logged into several OPs, user will not look to all the ones they log out from
- Option2
- Browser classifies signing-in event
- On log out does not prompt the user and IdP has no incentives to lie
- RPs get to determine if they want to log the user out or not
- Whether you can swap generic frame with fenced frame, frame can see it’s own cookies
- May not be able to pass any parameters that you need to pass; no link decoration for framed frame
- Subdomains also considered, but not well thought out
- Logout URL - other option to add, but more work for RP: Resource metadata. Specification - not much adoption. It just feels like a place where RP metadata could be declared which could be useful in this context of the RP defining its metadata (e.g. what IDP it uses
- [draft-jones-oauth-resource-metadata-01 - OAuth 2.0 Protected Resource Metadata (ietf.org)](https://tools.ietf.org/html/draft-jones-oauth-resource-metadata-01)
- On digression: [https://cloudidentity.com/blog/wp-content/uploads/2013/01/3252.image_5F00_04277494.png](https://cloudidentity.com/blog/wp-content/uploads/2013/01/3252.image_5F00_04277494.png)
- Messy real-life situation - sign in to AAD with OIDC and WS-fed; register something at sign-in. From a user, same account, does not matter which protocol is used
- What needs more to be discussed what log out means to the user
- User does not understand when they log out from office, they also log out from Azure
- Also a developer choice
- Relevant one, but not much browsers can do about
- If a bigger picture is browser wants to be in the middle, browser can do something in this area too.
- Ugly part of logout - mechanisms to allow the range of services
- IdP does not need to send back list of all RPs user is logging out from
- Idea not entirely off for IdP to tell a browser from there it wants to log user out from
- Browser have confident of the user intent
- Prompt the user for the intent - never a good idea
- Logout API that community can control a behaviour of
- You call it, browser logs it, and tell where the user left of
- Browser observes the login - passively. Heuristics - what if the browser has not seen it..
- some of this is already starting to show up in chrome canarie
- [https://chromium-review.googlesource.com/c/chromium/src/+/2837551](https://chromium-review.googlesource.com/c/chromium/src/%2B/2837551)
- If domain name ETLD of the issuer is the same as IdP, automatically logs out

* […]

- Looks like we can preserve session management if we figure out logout
- Next would be good to see pseudo code with concrete scenario and sequence diagrams
- Pseudo text: [https://github.com/WICG/WebID/blob/main/cookies.md#logout](https://github.com/WICG/WebID/blob/main/cookies.md%23logout)
- Prototype is being built
- AOB? At IIW?
- Understand what third party cookies actually mean - no cookies at all? Partition cookies going away. The way firefox is doing it?

* [TMI BFF: OAuth Token Mediating and session Information Backend For Frontend](https://iiw.idcommons.net/23B/_TMI_BFF:_OAuth_Token_Mediating_and_session_Information_Backend_For_Frontend) by Vittorio Bertocci & Brian Campbell (but mostly Vittorio)

OAuth, Javascript, Backend Infrastructure

When there is an alternative, it is more secure to keep tokens out of the browser.

Specifically talking about clients which are divided between a front end or javascript app, and backend supporting systems specifically for that/those apps

Questions on whether this would also apply equivalently to native apps, which may have different capabilities and infrastructure requirements. It likely does work, but

OAuth in the browser can be complicated and ASs don’t necessarily provide sufficient security features, support web interaction

Bespoke workarounds acquiring tokens on the backend and passing to the frontend. Implementers may have security issues and not understand how to map best current practices

TMI BFF

1. Backend gets and stores tokens, javascript frontend gets a cookie
2. Request to backend for access (scopes, potentially resource)
3. Backend returns the token, requests new token with appropriate scope, etc.

* [...]

What is the scope - acquiring a token for direct API access, not necessarily prescriptive for BFF architectures which put all API interactions through BFF. (DW) raised issue that simply converting OAuth calls in a remote party to local API calls protected by a cookie disables some security protections provided by OAuth tokens (XSRF), so some sort of BFF best practices may be needed to prevent footguns.
* [The State of Identity on the Web](https://medium.com/mattr-global/the-state-of-identity-on-the-web-cffc392bc7ea) Mattr
  > This article discusses how the success of Open ID Connect shaped the state of identity on the web, how new web standards enable a new model, and describes a bridge between those worlds: [OIDC Credential provider](https://mattrglobal.github.io/oidc-client-bound-assertions-spec/).
  > This cycle perpetuates the dominance of a few major IdPs and likewise forces users to keep choosing from the same set of options or risk losing access to all of their online accounts. In addition, many of these IdPs have leveraged their role as central intermediaries to increase surveillance and user behavior tracking, not just across their proprietary services, but across a user’s entire web experience.
  > [...]
  > [OIDC Credential Provider](https://mattrglobal.github.io/oidc-client-bound-assertions-spec/) allows you to extend OIDC to allow IdPs to issue reusable VCs about the end-user instead of simple identity tokens with limited functionality. It allows end-users to request credentials from an OpenID Provider and manage their own credentials in a [digital wallet](https://learn.mattr.global/concepts/digital-wallets) under their control.

* OpenID: [Public Review Period for Proposed Final OpenID Connect Client-Initiated Backchannel Authentication (CIBA) Core Specification](https://openid.net/2021/06/07/public-review-period-for-proposed-final-openid-connect-client-initiated-backchannel-authentication-ciba-core-specification/)

* OpenID: [Public Review Period for Two Proposed SSE Implementer’s Drafts](https://openid.net/2021/06/07/public-review-period-for-two-proposed-sse-implementers-drafts/)

* [Matt Flynn: Information Security | Identity & Access Mgmt.](http://360tek.blogspot.com/2021/06/bell-labs-colonial-pipeline-and-multi.html)
* [Introducing: The OAuth 2 Game](https://auth0.com/blog/introducing-the-oauth-2-game/)

It features two dice, one for grants and another for application types. Throw the dice and consult the instructions to discover whether the combination of grant and application type you obtained happens to be a good one! Play a few times, and before you know it, you’ll be familiar with the most common combinations!
* [Police in Latin America are turning activists’ phones against them](https://restofworld.org/2021/latin-america-phone-security/)

Experts say that seized devices have become a trove of information for authorities cracking down on social movements and opposition leaders.

* [Calls for New FTC Rules to Limit Businesses’ Data Collection and Stop Data Abuse](https://anonyome.com/2021/07/calls-for-new-ftc-rules-to-limit-businesses-data-collection-and-stop-data-abuse/)

“I want to sound a note of caution around approaches that are centered around user control. I think transparency and control are important. I think it is really problematic to put the burden on consumers to work through the markets and the use of data, figure out who has their data, how it’s being used, make decisions … I think you end up with notice fatigue; I think you end up with decision fatigue; you get very abusive manipulation of dark patterns to push people into decisions.

* [Huge data leak shatters the lie that the innocent need not fear surveillance](https://www.theguardian.com/news/2021/jul/18/huge-data-leak-shatters-lie-innocent-need-not-fear-surveillance)

Few pause to think that their phones can be transformed into surveillance devices, with someone thousands of miles away silently extracting their messages, photos and location, activating their microphone to record them in real time.

Such are the capabilities of Pegasus, the spyware manufactured by NSO Group, the Israeli purveyor of weapons of mass surveillance.

* [NSO rejects](https://www.theguardian.com/news/2021/jul/18/response-from-nso-and-governments) this label. It insists only carefully vetted government intelligence and law enforcement agencies can use Pegasus, and only to penetrate the phones of “legitimate criminal or terror group targets”

* [10 assertions about the future of social](https://werd.io/2021/10-assertions-about-the-future-of-social)

We can’t solve identity. There will never be a single identity that we use across the web. Instead, there may be open protocols that allow us to auth with different providers.
* [Apple announces first states signed up to adopt driver’s licenses and state IDs in Apple Wallet](https://www.apple.com/newsroom/2021/09/apple-announces-first-states-to-adopt-drivers-licenses-and-state-ids-in-wallet/)

Arizona, Connecticut, Georgia, Iowa, Kentucky, Maryland, Oklahoma, and Utah are among the first states to bring state IDs and driver’s licenses in Wallet to their residents
* [Decentralized Finance & Self-sovereign Identity: A tale of decentralization, a new paradigm of trust](https://gataca.io/insights/decentralized-finance-self-sovereign-identity-a-tale-of-decentralization-a-new-paradigm-of-trust)
* [How Social Engineering Has (And Hasn’t) Evolved Over Time](https://auth0.com/blog/how-social-engineering-has-and-hasnt-evolved-over-time/) auth0

In short: you can deploy all the technological measures you want, but unless you address the human element, an attacker can defeat your defenses with a simple phone call or email.

* [My Take on the Misframing of the Authentication Problem](https://kyledenhartog.com/misframing-authn/) Kyle Den Hartog

If you haven’t [read this paper](https://www.cl.cam.ac.uk/~fms27/papers/2012-BonneauHerOorSta-password--oakland.pdf) before you design an authentication system you’re probably just reinventing something already created or missing a piece of the puzzle

* [...]

can anyone point me to an academic research paper or even some user research that tells me the probability that a user’s password will be discovered by an attacker in the next year? What about the probability that the user shares their password with a trusted person because the system wasn’t deployed with a delegation system? Or how about how the probability will drop as the user reuses their password across many websites? Simply put I think we’ve been asking the wrong question

* [Developers: SMS Authentication is Challenging](https://medium.com/magiclabs/building-sms-authentication-c2cabccbd5f8) Magic Labs

SMS (Short Message Service) messaging¹, despite a number of material challenges, has broad adoption, international regulations, and support across platforms.

* [The Things to Keep in Mind about Auth](https://developer.okta.com/blog/2021/10/29/things-to-keep-in-mind-about-auth) Okta

* [The OpenID Foundation Welcomes Visa to the Board of Directors](https://openid.net/2021/12/07/the-openid-foundation-welcomes-visa-to-the-board-of-directors/) OpenID

Visa’s leadership in global payments and identity services as well as their longstanding commitment to standards will be of great value as we tailor our strategy to this moment.
* [Self-Sovereign Identity Working Group](https://europeanblockchainassociation.org/eba-working-group-self-sovereign-identity-eussi/) European Blockchain Association in collaboration with the European Commission

Right now, many enterprises and organisations are building their own SSI solutions by implementing the existing standards and protocols. Since all these parties do similar work and have to face similar problems, it is critical for the community to share these learnings and experiences openly.

* [Participate in Alberta's First Verifiable Digital Credentials Pilot](https://pilot.atbventures.com/) ATB Ventures and Govt Alberta

As a part of the pilot, you will add your MyAlberta Digital ID as a verifiable credential to your mobile digital wallet (on your smartphone) and use this digital credential to open an ATB Pay As You Go Account - Digital Credential account with ATB Financial.

* [Okta Joins the OpenID Foundation Board to Further Advance Open Identity Standards](https://openid.net/2021/12/10/okta-joins-the-openid-foundation-board-to-further-advance-open-identity-standards/) OpenID

“OpenID Connect is one of the most adopted identity standards, providing essential functionality to core solutions across the industry,” said Vittorio Bertocci, Principal Architect, Auth0.
* [Building a low-code, opinionated approach to plug & play login](https://medium.com/magiclabs/building-a-low-code-opinionated-approach-to-plug-and-play-login-21bb30dca9a4) Magic Labs

Magic Login Form represents a new onboarding experience for end-users, so we wanted to revamp our own onboarding experience for developers to match. Learning about auth can quickly derail any developer’s good day. Striking the balance between good UX and good security can just boggle the mind.

* [Use Fido2 Passwords Authentication with Azure AD](https://damienbod.com/2022/01/17/use-fido2-passwordless-authentication-with-azure-ad/) Damion Bod

This article shows how to implement FIDO2 passwordless authentication with Azure AD for users in an Azure tenant.

* [What is Knowledge-based Authentication (KBA)?](https://www.pingidentity.com/en/company/blog/posts/2022/what-is-knowledge-based-authentication-kba.html) Ping Identity

When you set up a new account, you are often asked to create a password and choose a security question and answer (e.g., What is your mother's maiden name?). Answering security questions based on personal information when you log in to an app or system is called knowledge-based authentication (KBA).

* [A Responsible Reporting Nightmare: Right-clicking is Not a Crime](https://me2ba.org/a-responsible-reporting-nightmare-right-clicking-is-not-a-crime/) Me2Ba

This is a story of a politician who cried “hacker” after a reporter informed a state agency that sensitive information was embedded in their website’s HTML source code1. While we wish this was a joke or fictional story it, unfortunately, is not. If the state of Missouri does move forward with the prosecution this state action would sound the alarm for researchers and reporters resulting in a chilling effect on the practice of responsible reporting.

* [OpenID Foundation Publishes Whitepaper on Open Banking](https://openid.net/2022/03/18/openid-foundation-publishes-whitepaper-on-open-banking/) OpenID

The paper documents the international movement towards Open Banking, Open Finance, and secure, consent driven access to all user data. It describes the OpenID Foundation and in particular the Financial-Grade API (FAPI) Working Group’s experience with Open Banking ecosystems internationally.

* [Charting an Accelerated Path Forward for Passwordless Authentication Adoption](https://fidoalliance.org/charting-an-accelerated-path-forward-for-passwordless-authentication-adoption/) FIDO

* [The paper introduces](https://media.fidoalliance.org/wp-content/uploads/2022/03/How-FIDO-Addresses-a-Full-Range-of-Use-CasesFINAL.pdf) multi-device FIDO credentials, also informally referred to by the industry as “passkeys,” which enable users to have their FIDO login credentials readily available across all of the user’s devices.

* [Open Badges is now on the plateau of productivity](https://dougbelshaw.com/blog/2022/03/18/open-badges-fers/) Doug Belshaw

We’re no longer in the stage of “imagine a world…” but rather “here’s what’s happening, let’s talk about how this could be useful to you”.

* [​​Cloudflare’s investigation of the January 2022 Okta compromise](https://blog.cloudflare.com/cloudflare-investigation-of-the-january-2022-okta-compromise/)

Our [understanding](https://twitter.com/toddmckinnon/status/1506184721922859010) is that during January 2022, hackers outside Okta had access to an Okta support employee’s account and were able to take actions as if they were that employee. In a screenshot shared on social media, a Cloudflare employee’s email address was visible, along with a popup indicating the hacker was posing as an Okta employee and could have initiated a password reset.

* [OpenID Foundation Publishes Whitepaper on Open Banking](https://openid.net/2022/03/18/openid-foundation-publishes-whitepaper-on-open-banking/)

The OpenID Foundation is pleased to share its new whitepaper, “[Open Banking, Open Data and Financial-Grade APIs](https://openid.net/wordpress-content/uploads/2022/03/OIDF-Whitepaper_Open-Banking-Open-Data-and-Financial-Grade-APIs_2022-03-16.pdf)”. The paper documents the international movement towards Open Banking, Open Finance, and secure, consent driven access to all user data. It describes the OpenID Foundation and in particular the Financial-Grade API (FAPI) Working Group’s experience with Open Banking ecosystems internationally.


* [FIDO passkeys are an existential threat to fintech startups](https://werd.io/2022/fido-passkeys-are-an-existential-threat-to-fintech-startups)

by definition, screen scraping requires storing a user’s financial system passwords in clear text. Nonetheless, you can bet that every system that integrates with payroll systems, and almost every system that integrates with banks (at a minimum), uses the technique. The US has badly needed [open banking style standards](https://standards.openbanking.org.uk/api-specifications/) for years.

Disasters in the World of Data

* [Facebook Is Receiving Sensitive Medical Information from Hospital Websites](https://themarkup.org/pixel-hunt/2022/06/16/facebook-is-receiving-sensitive-medical-information-from-hospital-websites)

* [Facebook and Anti-Abortion Clinics Are Collecting Highly Sensitive Info on Would-Be Patients](https://themarkup.org/pixel-hunt/2022/06/15/facebook-and-anti-abortion-clinics-are-collecting-highly-sensitive-info-on-would-be-patients)

* [Tech on Juneteenth: Some tech firms perpetuate modern-day slavery by using prison labor](https://benwerd.medium.com/tech-on-juneteenth-c45822aa53f7)


* [What Is Account Creation Fraud?](https://www.pingidentity.com/en/resources/blog/post/what-is-account-creation-fraud.html)

* [Balancing User Experience and Security](https://www.pingidentity.com/en/resources/blog/post/balancing-user-experience-ux-and-security.html)

* [Digital Identity Wallets auf Basis eIDAS 2.0 Ecosystem](https://www.comuny.de/digital-identity-wallets-auf-basis-eidas-2-0-ecosystem/)


Women’s Rights and Technology Intersection feel very poinient this week

* [Section 230 Is a Last Line of Defense for Abortion Speech Online](https://www.wired.com/story/section-230-is-a-last-line-of-defense-for-abortion-speech-online/) Wired

Democrats who have been misguidedly attacking Section 230 of the Communications Decency Act need to wake up now. If they don’t [start listening](https://www.thedailybeast.com/want-to-fix-big-tech-stop-ignoring-sex-workers) to the warnings of human rights experts, [sex workers](https://papers.ssrn.com/sol3/papers.cfm?abstract_id%3D4095115), LGBTQ+ folks, and [reproductive rights](https://freedomnetworkusa.org/app/uploads/2020/09/FNUSA-Joins-EARN-IT-Act-Coalition-letter-9.09.2020.pdf) groups, Democrats could help right-wing zealots achieve their goal: mass censorship of online content about abortion.

* [On Abortion and Data](https://www.mydata.org/2022/06/30/on-abortion-and-data/) MyData

A basic insight of MyData is that the current systems of data are asymmetrical, imbalanced, and unfair. A basic motivation of MyData is to fix this by addressing business, legal, technical, and societal aspects of those systems.

## Identity not SSI

* [Fixing Web Login](https://www.windley.com/archives/2022/06/fixing_web_login.shtml) Phil Windley

Like the "close" buttons for elevator doors, "keep me logged in" options on web-site authentication screens feel more like a placebo than something that actually works. Getting rid of passwords will mean we need to authenticate less often, or maybe just don't mind as much when we do.

* [Getting Started with Ceramic](https://blog.ceramic.network/getting-started-with-ceramic/)

In this beginner-friendly guide, I'll give you all the tools and knowledge needed to integrate the [Ceramic Network](https://developers.ceramic.network/) into your Web 3 [dapps](https://ethereum.org/en/dapps/).

The Ceramic Network is a decentralized data network that aims to bring composable data to Web 3 dapps. There are many types of data that Ceramic can work with, but for this guide we can treat Ceramic like a decentralized NOSQL document database.

* [ADOPTING NEW TECH: HOW TO GIVE YOUR TEAM THE BEST CHANCES OF SUCCESS](https://www.theengineroom.org/adopting-new-tech-how-to-give-your-team-the-best-chances-of-success/) The Engine Room

From our past work in this area, we have seen that slow and steady wins the race: for new policies, practices, and technologies to become part of workflows, staff need to be able to learn how to use new tools and incorporate them into their daily work practices — and be supported in doing so.

* [WHAT WE’VE LEARNED THROUGH OUR SUPPORT FOR ORGANISATIONS WORKING ON BUILDING DIGITAL COMMUNITIES](https://www.theengineroom.org/what-weve-learned-through-our-support-for-organisations-working-on-building-digital-communities/) The Engine Room

Maintaining an online community is a lot of work, in both the short term and the long term. It requires setting aside time, human resources and tech infrastructure to keep things running smoothly. Here are some questions and ideas that can help you assess what it may take to maintain the online community you’re trying to build:

* [What is FIDO? Infographic](https://www.scmagazine.com/resource/identity-and-access/what-is-fido)

- [How passkeys pave the way for passwordless authentication](https://www.scmagazine.com/resource/identity-and-access/how-passkeys-pave-the-way-for-passwordless-authentication)
- [InfoCert has been recognized Representative Vendor in Gartner’s Market Guide for Electronic Signature 2022](https://infocert.digital/infocert-has-been-recognized-representative-vendor-in-gartners-market-guide-for-electronic-signature-2022/)
- [GBG: The State of Digital Identity 2022](https://www.gbgplc.com/media/heqgqhur/gbg-state-of-digital-identity-2022.pdf)
- Security and satisfaction: Gaining from The Great Switch
- Digital identity’s next step: Mobile and alternative data
- Identity fraud: It’s a matter of when, not if
- Young adults: The biggest victims of identity fraud?
- Fraud and financial services
- Time to build trust in a digital world

* [Daon-Neustar Partnership Combines Voice Authentication With Phone Number Verification](https://findbiometrics.com/daon-neustar-partnership-voice-authentication-phone-number-verification-508261/)

Bad News

* [Widespread Okta phishing campaign impacts over 130 organizations](https://www.scmagazine.com/brief/identity-and-access/widespread-okta-phishing-campaign-impacts-over-130-organizations)

* [LastPass Reports a Breach: Identity News Digest](https://findbiometrics.com/lastpass-reports-a-breach-identity-news-digest-508262/)


* [Fido Passkey](https://www.pingidentity.com/en/resources/blog/post/how-fido-passkeys-accelerate-passwordless-future.html)

* [Security pros say the cloud has increased the number of identities at their organizations](https://www.scmagazine.com/analysis/cloud-security/security-pros-say-the-cloud-has-increased-the-number-of-identities-at-their-organizations)

* [Experian Joins iProov and Deloitte in UK’s Digital ID Program](https://mobileidworld.com/experian-joins-iproov-and-deloitte-in-uks-digital-id-program/)

* [Rohingya seek reparations from Facebook for role in massacre](https://apnews.com/article/technology-business-bangladesh-myanmar-c5af9acec46a3042beed7f5e1bc71b8a) APNews

The platform, Amnesty says, wasn’t merely a passive site with insufficient content moderation. Instead, Meta’s algorithms “proactively amplified and promoted content” on Facebook, which incited violent hatred against the Rohingya beginning as early as 2012.

* [The OpenID Connect Logout specifications are now Final Specifications](https://self-issued.info/?p%3D2298)

The OpenID Connect Logout specifications are now Final Specifications

Thanks to all who helped us reach this important milestone! This was originally [announced on the OpenID blog](https://openid.net/2022/09/12/the-openid-connect-logout-specifications-are-now-final-specifications/).

* [Call it data liberation day: Patients can now access all their health records digitally](https://www.statnews.com/2022/10/06/health-data-information-blocking-records/) Statnews

Under [federal rules](https://www.healthit.gov/buzz-blog/information-blocking/information-blocking-eight-regulatory-reminders-for-october-6th) taking effect Thursday, health care organizations must give patients unfettered access to their full health records in digital format. No more long delays. No more fax machines. No more exorbitant charges for printed pages.

