---
published: false
---

# Bridging the Gap

* [OpenID Connect for W3C Verifiable Credential Objects](https://iiw.idcommons.net/2F/_OpenID_Connect_for_W3C_Verifiable_Credential_Objects) by Oliver Terbu, Torsten Lodderstedt, Kristina Yasuda, Adam Lemmon, Tobias Looker

Slides: [https://www.slideshare.net/TorstenLodderstedt/openid-connect-for-w3c-verifiable-credential-objects](https://www.slideshare.net/TorstenLodderstedt/openid-connect-for-w3c-verifiable-credential-objects)

- Have been incubated in OpenID Foundation and DIF’s joint Self-Issued OpenID Provider WG - contact Kristina ([kristina.yasuda@microsoft.com](mailto:kristina.yasuda@microsoft.com) for participation details)

* [Integrating FIDO with Verifiable Credentials (8.30 am start)](https://iiw.idcommons.net/10E/_Integrating_FIDO_with_Verifiable_Credentials_(8.30_am_start)) by David Chadwick

* [The Use of FIDO2 and Verifiable Credentials (David Chadwick)](https://youtube.com/watch?v%3Dl3taGxBdrRU)

W3C Web Authentication (FIDO2) provides a mechanism for strong authentication whilst W3C Verifiable Credentials provide a mechanism for strong identification and authorisation. Together they make an unbeatable pair for identity management.

Prof. David Chadwick presented work on sharing W3C Verifiable Crendentials via FIDO2 key setup with issuers of credentials.  In a nutshell, the holder and issuer use the WebAuthN protocol to strongly authenticate before the issuer protects the credentials with its signature.  Upon providing credentials to a relying party, the issuer (acting in an IDP capacity, so they must be online) will verify the identity of the holder via FIDO2 WebAuthN so that the credentials (or selected claims in the credentials for selective disclosure) can be shared with the relying party.  Ephemeral keys are created to bind the holder with such credentials shared to the relying party/verifier.  The relying party/verifier can use X.509 certs to confirm that the issuer is valid by checking the signature on the derived credential from the holder.



* [SIOP Use-cases - IIW Spring 2021](https://docs.google.com/presentation/d/1a0C4HvVYwwwDqSw3tgPNhy9Iqyufy9oZdnMgl7rQ9Vc/edit%23slide%3Did.p)

- Continuity of a service
- Offline Authentication
- Speed, reduced latency
- Choice, Portability
- Privacy

* [Mapping FHIR JSON resource to W3C Vaccination vocabulary : A semantic data pipeline](https://iiw.idcommons.net/index.php?title%3D12H/_Mapping_FHIR_JSON_resource_to_W3C_Vaccination_vocabulary_:_A_semantic_data_pipeline%26action%3Dedit%26redlink%3D1) by John Walker

* [DID chooser for SIOP](https://iiw.idcommons.net/20A/_DID_chooser_for_SIOP) by tom jones & friends

* [https://docs.google.com/presentation/d/1OaMecHecTUexv1skJZoYzJoHKYH8H03REFpFstLRjPg/edit?ts=607b7e5d#slide=id.gd2c45a9dcd_7_21](https://docs.google.com/presentation/d/1OaMecHecTUexv1skJZoYzJoHKYH8H03REFpFstLRjPg/edit?ts%3D607b7e5d%23slide%3Did.gd2c45a9dcd_7_21)

Goal is to allow folks to pick their DID they want to use for a website.
“Subject choosing which DID to present”.

Use case:
A user goes to an RP, and decides to register for return visits.
RP can’t offer folks the Nascar Problem (too many IDP logos on the login screen).

Select a Wallet vs Select a Wallet and Identifier.

What happens when SIOP arrives?
We will need a DID chooser.

Some wallets will hold credentials for multiple identifiers, some will hold only 1.

An RP offers users multiple options for registration (Google, Facebook, Yahoo…. And coming soon… Personal)

RP should disclose their ID and why they are asking the user for what data.

Options we consider:

- [https://w3c-ccg.github.io/credential-handler-api/](https://w3c-ccg.github.io/credential-handler-api/)
- [https://w3c-ccg.github.io/vp-request-spec/#format](https://w3c-ccg.github.io/vp-request-spec/%23format)
- [https://specs.bloom.co/wallet-and-credential-interactions/](https://specs.bloom.co/wallet-and-credential-interactions/)
- [https://github.com/w3c-ccg/universal-wallet-interop-spec/issues/84](https://github.com/w3c-ccg/universal-wallet-interop-spec/issues/84)
