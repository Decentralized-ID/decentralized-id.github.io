# The Evolution of Self Sovereign Identity (Draft Seeking Feedback)

;TLDR A start at examining leading thought around SSI since 2016, and presenting the idea of "modularizing" essential components of SSI documentation.

---

Christopher Allen's seminal work, [The Path to Self Sovereign Identity](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/ThePathToSelf-SovereignIdentity.md) continues to be an important and influential document for the Self Sovereign Identity community and movement. Rightly so, Allen does a superb job of outlining where digital identity has come from and where its going. However, Christopher intended for the [Principles of SSI](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md), gathered from the leading thought on digital identity, to be the start of a conversation.

In order to stimulate the discussion, I've been going through a [/infominer33/self-sovereign-identity](https://github.com/infominer33/self-sovereign-identity) and organizing some thoughts on SSI since Christopher's 2016 post. There are a few different ways to approach and describe SSI. What I aim to do is come up with a list of different "SSI Cases" to modularize the treatment of the subject. This will allow each to contribute in the way that makes most sense for themselves, rather than trying to discuss SSI as a whole in a single whitepaper.

That October, [Joe Andrieu](https://github.com/jandrieu) submitted [A Technology‐Free Definition of Self‐Sovereign Identity](https://github.com/jandrieu/rebooting-the-web-of-trust-fall2016/raw/master/topics-and-advance-readings/a-technology-free-definition-of-self-sovereign-identity.pdf) to the third Rebooting the Web of Trust Design Workshop. Within it, he describes the Characteristics of SSI: **Control**, **Acceptance**, and **Zero Cost**.

>1 No disrespect to Christopher Allen’s opening to the conversation, The Path to Self Sovereign Identity [...] It gets a lot right, but leaves a few requirements out, e.g., recoverability and zero cost, and conflates “identities” and claims in an ambiguous manner.

I decided to put the **10 Principles of SSI** up next to Joe Andrieu's **Characteristics of SSI** 

* [SSI Principles vs. Characteristics](https://github.com/infominer33/awesome-decentralized-id/blob/master/self-sovereign/ssi-principles-vs-characteristics.md)

Which should also be considered against:

* [Self-Sovereign Bill of Rights](self-sovereign-identity-bill-of-rights.md) - lifeID (founded by [Chris Boscolo](https://github.com/cboscolo)) adapted the 10 Principles of Self-Sovereign Identity into a [Bill of Rights](https://medium.com/@lifeID_io/lifeid-self-sovereign-identity-bill-of-rights-d2acafa1de8b) that all self-sovereign identity solution should uphold.

* [Schutte's Take](https://github.com/infominer33/self-sovereign-identity/blob/master/Schutte-on-SSI.md) which offers criticism on the 10 principles.


I think all of this thought should be consolidated into a cohesive declaration of ssi. The idea is to come up with list of phinciples, or characteristics, or rights, that is as complete as possible, while also as concise as possible. There are a few 10 pointed lists, I'm ok with combining them as necessary and if it turns into 19, for example, I'm ok w that. I'd rather err on the side of too much and pare it down gradually, than to not include enough.  

* Next, there are the [7 Myths of SSI](https://github.com/infominer33/self-sovereign-identity/blob/master/7-myths-of-self-sovereign-identity.md) from Timothy Ruff's recent blog post. I've extracted them from his two part series into a concise document. There are surely other myths, and perhaps folk who have encountered them first hand will have some comment on the matter. And my condensed version of his myths could surely be improved upon.

* A gentle introduction to self-sovereign-identity by @antonylewis has a great section, [How would self-sovereign identity work for the user?](https://github.com/infominer33/awesome-decentralized-id/blob/master/self-sovereign/user-experience.md) that I've extracted into github, in order to make a suitable document based upon it. I need to check on certain specifics, basically I want to re-write that section so I saved it here for that purpose.

* [How to Convince Dad* of the Importance of Self-Sovereign Identity](https://github.com/WebOfTrustInfo/rwot7/blob/master/final-documents/convincing-dad.md)
   * \*and your sister and your daughter and your best friend and your nephew (SSI Use-Cases)

^^^ This could also be modularized

Other content highlighted in [/WebOfTrustInfo/self-sovereign-identity](https:github.com/WebOfTrustInfo/self-sovereign-identity) that I haven't had a chance to fully review, yet:

* [Identity and Digital Self-Sovereignty](https://medium.com/learning-machine-blog/identity-and-digital-self-sovereignty-1f3faab7d9e3#.3jcgvnbok) - Blog post by [Natalie Smolenski](https://medium.com/@nsmolenski)

* [SSI: A Roadmap for Adoption](https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-spring2018/blob/master/final-documents/a-roadmap-for-ssi.md) from Rebooting the web of trust, Spring 2018. 
  > This document proposes the formation of a short-term team to develop consistent messaging for the Self-Sovereign Identity (SSI) market.



### What I'm hoping for:

This is a modular breakdown of SSI documentation I would like to facilitate:
(each, perhaps, around 800-1200 words) 

1. History of Digital Identity. Along the lines of Christopher Allen

2. "How SSI works for the User" something along the line of how Antony Lewis 
   - At its essence, this describes "ssi architecture" so to speak: 'wallet', 'identifier', 'credential' etc and how it interelates 

3. "Principles of SSI" whatever you wanna call it, a complete, concise, and "exhaustive" list of foundational SSI principles or progress in that direction.

4. SSI Why Blockchain?

5. Myths of SSI

6. SSI Use Cases. (a'la "how to convince dad")
   - This uses the foundation "how SSI works for the USER" to go into more specific details of real life UX

I'm not limited to those 6, and I'm not glued to that order, but thats a general goal, and "how I would do it."  We have the foundations of some core SSI content\documentation that I think will improve SSI education\onboarding. Just as in modularizing a codebase, modularizing SSI documentation will make it easier for any aspect to be improved as needed. I hope for these to become living community driven documents. Personally, I'm good at collecting, organizing, and digesting information, but am new to the SSI community, so I'm sure there's plenty I'm not considering.

I can see that I'll need to spend a lot more time with this content, am just learning my way around it right now.  

I'm not the most qualified, I just have time and motivation. (Specifically, sometimes I write about Self-Sovereign Identity. But I want to write about it in an accurate way, which is difficult to do until some order is made of all this material.)

<a href="https://infominer.id"><img src="https://infominer.id/android-chrome-256x256.png" align="right" width="170" height="170"/></a>

## [infominer.id](https://infominer.id)  ([**^**](#contents))
* [github.com/awesome-decentralized-id](https://github.com/infominer33/awesome-decentralized-id)
* [infominer.id/awesome-decentralized-id/](https://infominer.id/awesome-decentralized-id/)


