# Cryptonomica


[![](https://i.imgur.com/moVyrrt.png)](https://cryptonomica.github.io)

 * [Cryptonomica.net](https://cryptonomica.net) is an identity verification service based on [OpenPGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) and [Ethereum](https://www.ethereum.org) with legal framework and online dispute resolution for electronic contracts from London-based [court of arbitration](https://cryptonomica.net/#!/arbitration) 

## From [the Cryptonomica Whitepaper](https://github.com/Cryptonomica/cryptonomica/wiki/Cryptonomica-White-Paper#the-problem):

>### The Problem
>
>As stated in [Wikipedia](https://en.wikipedia.org/wiki/Pretty_Good_Privacy#Certificates):
>
>> All public key / private key cryptosystems have the same problem (The problem of correctly identifying a public key as belonging to a particular user), even if in slightly different guises and *no fully satisfactory solution is known*.
>
>Existing systems of keys-based digital signature for documents are based on a personal visit to a certification center.
>
>The key pair for the client is in many countries created by the certification center, and given to the client. In this case, a copy of the user's private key can remain in the certification center, i.e. not only user can have access to it. This problem is often not even realized by users.
Often the keys for the client-bank systems are created this way.
>
>Although signature verification is reliable only if no one else except the owner has access to private key.

[...]

>### Our Solution
>
>PGP's ["Web of trust"](https://en.wikipedia.org/wiki/Web_of_trust) was not a success, because, as stated [Wikipedia](https://en.wikipedia.org/wiki/Pretty_Good_Privacy#Web_of_trust):
> Users have been willing to accept certificates and check their validity *manually* or to simply accept them. *No satisfactory solution has been found for the underlying problem*
>
>We offer exactly the solution for this problem that is mentioned in Wikipedia as not yet found. We deny automatic key check, we are offering the user to check and download each key manually.
>
>We make verification of key owner's identity and store data about this verification: who, when, using which document made verification. And unlike in ['Web of trust']((https://en.wikipedia.org/wiki/Pretty_Good_Privacy#Web_of_trust)) there is an established procedure for key verification, i.e. known rules according to witch identity of the key owner have to be proven.
>
>The user can make the information of the key or keys in the database available to all other users of the database, or available only for specified users or user group. Accordingly database user will have access to data about keys of others users, which is open to all users or shared with him, (for some cases, i.e. for arbitrators, including scans on the paper documents)
>
>And we offer for the market the first legally relevant global system of public key's certification, that can be run around the world, or more precisely in all states where [Hague Convention Abolishing the Requirement for Legalisation for Foreign Public Documents 1961](https://www.hcch.net/en/instruments/conventions/full-text/?cid=41) ([Apostille Convention](https://en.wikipedia.org/wiki/Apostille_Convention)) and [United Nations Convention on the Recognition and Enforcement of Foreign Arbitral Awards 1958](http://www.uncitral.org/uncitral/en/uncitral_texts/arbitration/NYConvention.html) ([New York Convention 1958](https://en.wikipedia.org/wiki/Convention_on_the_Recognition_and_Enforcement_of_Foreign_Arbitral_Awards)) are recognized.
>
>We can provide a legal mechanism for recognizing digitally signed contracts in almost every country: every digital contract in the need can be "transformed" in arbitral award recognized under [The Convention on the Recognition and Enforcement of Foreign Arbitral Awards](http://www.uncitral.org/uncitral/en/uncitral_texts/arbitration/NYConvention.html), and using modern technologies (web-server, databases, videoconferencing, e-mail) make [international arbitration](https://en.wikipedia.org/wiki/International_arbitration) affordable even for small business and individual clients.


## Github Repos [**^**](#contents)
* <a href="https://github.com/Cryptonomica/cryptonomica" target="_blank">/Cryptonomica/cryptonomica</a> - Cryptonomica keys server
* <a href="https://github.com/Cryptonomica/cryptonomica.github.io" target="_blank">/Cryptonomica/cryptonomica.github.io</a> - Cryptonomica frontend
* <a href="https://github.com/Cryptonomica/arbitration-rules" target="_blank">/Cryptonomica/arbitration-rules</a> - Cryptonomica Arbitration Rules
* <a href="https://github.com/Cryptonomica/dappathon-tlv" target="_blank">/Cryptonomica/dappathon-tlv</a>
* <a href="https://github.com/Cryptonomica/Ethereum-IdentityVerification" target="_blank">/Cryptonomica/Ethereum-IdentityVerification</a> - Indentity verification and KYC for Ethereum blockchain
* <a href="https://github.com/Cryptonomica/ethnode.cryptonomica.net" target="_blank">/Cryptonomica/ethnode.cryptonomica.net</a> - Ethereum node with API on nodejs and web3.js
* <a href="https://github.com/Cryptonomica/Ethereum-IdentityProof" target="_blank">/Cryptonomica/Ethereum-IdentityProof</a> - Smart contract for Ethereum's account owner verification using Cryptonomica.net
* <a href="https://github.com/Cryptonomica/international-arbitration-law" target="_blank">/Cryptonomica/international-arbitration-law</a> - Repository for collecting information about international arbitration law and practice
