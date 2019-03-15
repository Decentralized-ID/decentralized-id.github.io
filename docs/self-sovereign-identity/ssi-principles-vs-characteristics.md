# A Comparison Between SSI Principles, and Characteristics

In April of 2016, Christopher Allen published "[The Path to Self Sovereign Identity](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/ThePathToSelf-SovereignIdentity.md)." 

>The idea of digital identity has been evolving for a few decades now, from centralized identities to federated identities to user-centric identities to self-sovereign identities. However, even today exactly what a self-sovereign identity is, and what rules it should recognize, aren’t well-known.
>
>This article seeks to begin a dialogue on that topic, by offering up a definition and a set of principles as a starting point for this new form of user-controlled and persistent identity of the 21st century.

His article details the history of digital identity standards, and the user experience accompanying those standards. After describing from where we've come, Allen draws from leading thought on digital identity to compose the [Principles of Self Sovereign Identity](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md). 

That October, [Joe Andrieu](https://github.com/jandrieu) submitted [A Technology‐Free Definition of Self‐Sovereign Identity](https://github.com/jandrieu/rebooting-the-web-of-trust-fall2016/raw/master/topics-and-advance-readings/a-technology-free-definition-of-self-sovereign-identity.pdf) to the third Rebooting the Web of Trust Design Workshop.

>1 No disrespect to Christopher Allen’s opening to the conversation, The Path to Self Sovereign Identity [...] It gets a lot right, but leaves a few requirements out, e.g., recoverability and zero cost, and conflates “identities” and claims in an ambiguous manner.

Andrieu explores what people need from self-sovereign identity, independant from technology. An important consideration, for Joe, is realizing UN Sustainable Development Goal 16.9 “Providing every last person on the planet with a legal identity by 2030." 

>In order to fund, co‐develop, and eventually deploy a global self‐sovereign solution to UN Sustainable Development Goal 16.9, it would be prudent to begin with an explicit requirements process independent of any specific technology.

In conclusion, we are offered : **Control**. **Acceptance**. **Zero Cost**.

I'd like to review the <i>the fundamental characteristics of self‐sovereign identity</i> as detailed by Joe Andreiu, and compare each of the <i>principles</i> individually to ensure that all of the essentials are considered.

---

### Fundamental Characteristics of Self-Sovereign Identity

#### CONTROL 
* **Self‐sovereign identities are controlled by the individual:**
   * **Self‐generatable and Independent:** Individuals must be able to create identity information without asking for permission and be able to assert identity information from any authority. The resulting identity must have the same technical reliability as those provided by well‐known, “official” sources. The observer, of course, is always free to decide whether or not a given piece of information is meritorious, but the information must be able to be verified as a non‐repudiatable statement of correlation using exactly the same mechanisms regardless of source. Further, individuals must be able to present self‐generated identity information without disclosing that the authority in the claim is the subject of the claim. 
   * **Opt‐in**: The affordance for asserting identity information starts with the individual. While an individual may present claims from known or accepted third party authorities, it is the individual who asserts that the claim applies to them. Self‐sovereign identities begin with the will of the individual, with the intentional presentation of identity information. 
   * **Minimal Disclosure**: Individuals should be able to use services with minimal identity information. Features that depend on enhanced correlation must be understood by the average user. Such features should be permissioned with the highest granularity, so functions independent of correlation work equally well alongside those dependent on it. It is not acceptable to deny services because of a refusal to provide unrelated information. 
   * **Non‐participation**: Individuals must be able to choose to not provide identity information for services where it isn’t absolutely required.  Any spontaneous identifiers necessary for a service to function, such as cookies or session ids, must use the same infrastructure for consent, persistence, transience, and disclosure as if provided by the individual. 
   * **Opt‐out**: Individuals should be able to opt‐out of identifying records post‐facto as a matter of course.  People should be able to stop the use of a correlating identity information by request. Some transactions necessarily require long term retention of identity information, such as financial transactions, purchases, and shipments. Actions that create permanent records should be clearly marked and communicated such that the retention is expected and understood by the average person. All other actions which leverage a self‐sovereign identity should be de‐correlated on‐demand and said identifiers should no longer be used to correlate that individual across contexts. 
   * **Recoverable**: Sovereign identities must be robust enough to be recovered even if hard drives are lost, wallets stolen, or birth certificates lost in a fire. Self‐sovereign identities must provide a way for individuals to recover and reassert that existing identify information applies to them even in the face of complete loss of credentials. This may be challenging given current technical proposals, but the point of this paper is to explore the non‐technical requirements of a self‐sovereign identity. To fully address the needs of UN Sustainable Development Goal 16.9, identity assurance can’t depend on pieces of paper, devices, or other artifacts that can be lost, stolen, destroyed, and falsified. 

#### ACCEPTANCE 
* **Self‐sovereign identities are accepted wherever observers correlate individuals across contexts.** 
   * **Standard**: There is an open, public standard managed through a formal standards body, free to use by anyone without financial or intellectual encumbrance. Simple The core standard (schema, serialization, and protocols) must be atomically minimal, providing the barest data set, allowing complexity to emerge not from a complicated data model but from a multiplicity of information types, authorities, and observations. 
   * **Non‐repudiatable**: Individual claims should be cryptographically signed to assure non‐repudiatable statements of correlation. Long term, public and semi‐public ledgers should be used to record claims that become statistically impossible to falsify over time. Self‐sovereign identities, at a minimum depend on cryptographic assurances, and most likely will be further enabled by non‐repudiatable public ledgers. 
   * **Reliable**: Access to self‐sovereign identities must be at least as reliable as access to the Internet. It should not rely on any individual or group of centralized servers, connections, or access technologies. Substantially Equivalent Above all, self‐sovereign identities must meet the needs of legacy identity observers at least as well as current solutions. If the core architecture is inherently less capable than existing approaches there is little hope of systemic adoption. 

#### ZERO COST 
* **Finally, any proposed standard for self‐sovereign identity must be adoptable at absolutely minimal cost.**
   * Not only must it be free of licensing encumbrances, it must be implementable with readily available, inexpensive, commodity hardware running common operating systems. If it can’t be achieved using today’s commodity products, then we must help manufacturers incorporate what we need.  

     **In order to reach every last person on the planet**—the explicit target of UN Sustainable Development Goal 16.9—**self‐sovereign identity must be realizable at massive scale with close to zero marginal cost**. 
     
The systems we use to make sense of the resulting identity transactions will provide more than enough consulting, software, and hardware revenue to finance the development of the core enabling technology. Just as the web browser was a zero cost entry into a vast economic and innovation engine of the world‐wide web, so too must self‐sovereign identity begin with the most cost‐effective on‐ramp that can be engineered. 

---

### Principles of Self-Sovereign Identity

Now we'll review Christopher Allen's [Principles of Self Sovereign Identity](https://github.com/WebOfTrustInfo/self-sovereign-identity/blob/master/self-sovereign-identity-principles.md) one at a time to see how well the characteristics compare.

>1. **Existence.** *Users must have an independent existence.* Any self-sovereign identity is ultimately based on the ineffable “I” that’s at the heart of identity. It can never exist wholly in digital form. This must be the kernel of self that is upheld and supported. A self-sovereign identity simply makes public and accessible some limited aspects of the “I” that already exists.

I believe, the *Existance* principle is well represented by the first bulletpoint under the characteristic of *Control*, Self‐generatable and Independent.

>2. **Control.** *Users must control their identities.* Subject to well-understood and secure algorithms that ensure the continued validity of an identity and its claims, the user is the ultimate authority on their identity. They should always be able to refer to it, update it, or even hide it. They must be able to choose celebrity or privacy as they prefer. This doesn’t mean that a user controls all of the claims on their identity: other users may make claims about a user, but they should not be central to the identity itself. 

The principle of Control must be well represented, since the characteristic of *Control* has the following 5 sub-points: **Self Generatable and Independent**, **Opt-In**, **Minimal Disclosure**, **Non-participation**, **Opt-out**, **Recoverable**.

>3. **Access.** *Users must have access to their own data.* A user must always be able to easily retrieve all the claims and other data within his identity. There must be no hidden data and no gatekeepers. This does not mean that a user can necessarily modify all the claims associated with his identity, but it does mean they should be aware of them. It also does not mean that users have equal access to others’ data, only to their own.
>4. **Transparency**. *Systems and algorithms must be transparent.* The systems used to administer and operate a network of identities must be open, both in how they function and in how they are managed and updated. The algorithms should be free, open-source, well-known, and as independent as possible of any particular architecture; anyone should be able to examine how they work.

Access and Transparency are not not explicitly represented in the Characteristics of SSI. The *Control* characteristic should be examined in relation.

>5. **Persistence.** *Identities must be long-lived.* Preferably, identities should last forever, or at least for as long as the user wishes. Though private keys might need to be rotated and data might need to be changed, the identity remains. In the fast-moving world of the Internet, this goal may not be entirely reasonable, so at the least identities should last until they’ve been outdated by newer identity systems. This must not contradict a “right to be forgotten”; a user should be able to dispose of an identity if he wishes and claims should be modified or removed as appropriate over time. To do this requires a firm separation between an identity and its claims: they can't be tied forever.
>6. **Portability.** *Information and services about identity must be transportable.* Identities must not be held by a singular third-party entity, even if it's a trusted entity that is expected to work in the best interest of the user. The problem is that entities can disappear — and on the Internet, most eventually do. Regimes may change, users may move to different jurisdictions. Transportable identities ensure that the user remains in control of his identity no matter what, and can also improve an identity’s persistence over time.
>7. **Interoperability.** *Identities should be as widely usable as possible.* Identities are of little value if they only work in limited niches. The goal of a 21st-century digital identity system is to make identity information widely available, crossing international boundaries to create global identities, without losing user control. Thanks to persistence and autonomy these widely available identities can then become continually available.

These principles could be more closely examined against the sub-points of the *Acceptance* characteristic.

>8. **Consent.** *Users must agree to the use of their identity.* Any identity system is built around sharing that identity and its claims, and an interoperable system increases the amount of sharing that occurs. However, sharing of data must only occur with the consent of the user. Though other users such as an employer, a credit bureau, or a friend might present claims, the user must still offer consent for them to become valid. Note that this consent might not be interactive, but it must still be deliberate and well-understood.
>9. **Minimalization.** *Disclosure of claims must be minimized.* When data is disclosed, that disclosure should involve the minimum amount of data necessary to accomplish the task at hand. For example, if only a minimum age is called for, then the exact age should not be disclosed, and if only an age is requested, then the more precise date of birth should not be disclosed. This principle can be supported with selective disclosure, range proofs, and other zero-knowledge techniques, but non-correlatibility is still a very hard (perhaps impossible) task; the best we can do is to use minimalization to support privacy as best as possible. 

I think these two principles are well represented by the *Control* characteristic.

>10. **Protection.** *The rights of users must be protected.* When there is a conflict between the needs of the identity network and the rights of individual users, then the network should err on the side of preserving the freedoms and rights of the individuals over the needs of the network. To ensure this, identity authentication must occur through independent algorithms that are censorship-resistant and force-resilient and that are run in a decentralized manner. 

This is an important principle that I don't think is represented in the Characteristics.

### Conclusion

This review leaves me with more questions than answers. I'm not sure if we should implement the best parts of the *Characteristics* into the *Principles*, or the other way around.

I'm willing to make an attempt at bringing these together if no one else jumps at the chance. However, I'd like to gather some feedback. I'm tempted to use the Characteristics as the foundation, and simply incorporate any principles not well represented. However, I'm not sure if "Control, Acceptance, and Zero Cost" are the best way to divide them up. 


Research Based Content **—[infominer.id](https://infominer.id)**
