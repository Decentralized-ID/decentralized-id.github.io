### 7 Myths of Self-Sovereign-Identity

This October, Tim Ruff of Evernym published the [7 Myths of Self-Sovereign Identity](https://medium.com/evernym/7-myths-of-self-sovereign-identity-67aea7416b1), to clear up some common misconceptions about SSI. The 7 Tim highlights are an excellent start to SSI myth busting. Which other myths need busted? What is the best way to succinctly and completely relate the seven listed here?

#### Myth 1: Self-sovereign means self-attested.

Self-Sovereign means having ownership over your own credentials. However, we are still dependent on others to verify specifics about who we are. Self-attested credentials provide your personal opinion, preferences and consent. Proof of specific attributes commonly requires a trusted third party to verify and attest to.

#### Myth 2: SSI attempts to reduce government’s power over an identity owner.

Many people are reminded of the Sovereign Citizens movement, that asserts its sovereign independence from presiding governments. Self-sovereign identity, on the other-hand, enables a private, encrypted connection between a government and their citizens. That connection, mutual and revokable by either party, can support mutual authentication, communication, and datasharing; independent from change of address or phone numbers.

#### Myth 3: SSI creates a national or “universal ID” credential.

SSI is not meant to supplant a national ID system. As mentioned previously, governments can use SSI to improve existing identity systems, whether national, regional, or otherwise. SSI does not replace the trust of government or any other organization; rather SSI makes possible stronger, more flexible and verifiable connections between existing organizations, members, governments and constituents. SSI will, however, make possible identification for those who are unable to access any from a local government, including refugees and other displaced people.

#### Myth 4: SSI gives absolute control over identity.

SSI gives its owner control over some aspects of identity, but not all. The digital wallet, DIDs, interaction history, consent receipts, private keys, and self-attested credentials are under complete control of the owner.

Connections, relationships, and third-party issued credentials are not entirely self-sovereign, nor should they be. Like real-world relationships, all parties involved have some degree of control over the continuation of the relationship.

With Sovrin\Indy-style SSI, digital credentials can be held by the SSI owner in a self-sovereign digital wallet, and can still be revoked by their issuers, without the credentials being removed from the wallet.

#### Myth 5: There’s a “main” verifier of credentials.

With real SSI there is no third party in the middle verifying each credential added to a wallet. Identity proofing services can provide a valuable service, but its a lot simpler when government and financial institutions issue verifiable credentials directly to identity owners.

If want to use that credential somewhere other than where it was issued from, it can be instantly verified by any relying party I share it with, without having to check with the issuer.

#### Myth 6: There’s a built-in method of authenticating.

SSI isn't dependent upon any particular means of authentication. It offers a protocol supporting any authentication method that two (or more) parties opt to use. One implementation might use facial or voice biometrics while another uses proof of location, and another simply exchanges digitally signed attestations, which are incredibly strong.


#### Myth 7: User-centric identity is the same as SSI.

User-centric identity gaves the user greater control than before, and that’s great! However, it never realized its original intent — user independence — and it actually left large intermediaries with even more power than before. Facebook and Google, the biggest beneficiaries of the move to user-centric identity, would call their services user-centric.

Even the term gives it away: you’re still a user and not the owner, and that means the underlying service is siloed or federated, not self-sovereign. Of course with SSI there are services provided by third parties, such as cloud agent hosting and relationship management apps and tools, but they are modular and replaceable.
