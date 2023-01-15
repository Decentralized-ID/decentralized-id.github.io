
* [OAuth2.0 and VCs](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0152.html) Nikos Fotiou
  > I would like to share with you a paper we have written and it will be presented at [IEEE ICCCN 2021](http://www.icccn.org/). You can find the paper here [https://arxiv.org/abs/2104.11515](https://arxiv.org/abs/2104.11515) We tried to couple OAuth 2.0 flows with JWT/JWS and VCs in order to implement capabilities-based access control. Our goal was to show gains with minimal changes. Some things that might be of interest:
  > 
  > - We used Proof-of-Possession Key Semantics for JSON Web Tokens (RFC 7800) instead of credentialSubject `id`
  > - We used OAuth 2.0 Demonstration of Proof-of-Possession at the Application Layer (DPoP),([https://datatracker.ietf.org/doc/draft-ietf-oauth-dpop/](https://datatracker.ietf.org/doc/draft-ietf-oauth-dpop/)) for proving VC ownership
  > - We discuss how Revocation list 2020 has better privacy properties compared to RFC 7662 (which can be used for examining the status of an access token)
* [101 Session: OAuth2](https://iiw.idcommons.net/2B/_101_Session:_OAuth2) by Aaron Parecki
* [OAuth 2.0 Simplified](https://aaronparecki.com/oauth-2-simplified/) is a guide to OAuth 2.0 focused on writing clients that gives a clear overview of the spec at an introductory level.
  > In 2017, I published a longer version of this guide as a book, available on [oauth.com](https://oauth.com/) as well as [a print version](https://oauth2simplified.com). The book guides you through building an OAuth server, and covers many details that are not part of the spec. I published this book in conjunction with [Okta](https://developer.okta.com/).

* [https://speakerdeck.com/aaronpk/oauth-101-internet-identity-workshop-xxxi](https://speakerdeck.com/aaronpk/oauth-101-internet-identity-workshop-xxxi)

* [How OAuth Works](https://www.youtube.com/watch?v=g_aVPdwBTfw&list=PLRyLn6THA5wN05b3qJ6N0OpL3YbritKI-) 12 videos

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



* OpenID: [Public Review Period for Two Proposed SSE Implementer’s Drafts](https://openid.net/2021/06/07/public-review-period-for-two-proposed-sse-implementers-drafts/)

* [Matt Flynn: Information Security | Identity & Access Mgmt.](http://360tek.blogspot.com/2021/06/bell-labs-colonial-pipeline-and-multi.html)
* [Introducing: The OAuth 2 Game](https://auth0.com/blog/introducing-the-oauth-2-game/)

It features two dice, one for grants and another for application types. Throw the dice and consult the instructions to discover whether the combination of grant and application type you obtained happens to be a good one! Play a few times, and before you know it, you’ll be familiar with the most common combinations!
* [The Nuts and Bolts of OAuth 2.0](https://aaronparecki.com/2020/12/22/14/oauth)

Aaron Parecki - Mr. OAuth has a new course out on Udemy

> 3.5 hours of video content, quizzes, as well as interactive exercises with a guided learning tool to get you quickly up to speed on OAuth, OpenID Connect, PKCE, best practices, and tips for protecting APIs with OAuth.

