# Non SSI Identity Standards

## Contents

- OpenID
- FIDO
- OAuth
- SCIM
- SAML
- KMIP
- Secure QR Code

## OpenID


* [Registration - OpenID Foundation Virtual Workshop](https://openid.net/2021/03/01/registration-open-for-openid-foundation-virtual-workshop-april-29-2021/) April 29, 2021

updates on all active OpenID Foundation Working Groups as well the OpenID Certification Program
OpenID Specs Up for Review

* [Public Review Period for Second Proposed RISC Profile Implementer’s Draft](https://openid.net/2022/07/05/public-review-period-for-second-proposed-risc-profile-implementers-draft/)

This specification defines event types and their contents based on the [SSE Framework](https://openid.net/specs/openid-risc-profile-specification-1_0-02.html%23SSE-FRAMEWORK) that are required to implement Risk Incident Sharing and Coordination.

## FIDO

* [2021 FIDO Developer Challenge: Outcomes and Winners](https://fidoalliance.org/2021-fido-developer-challenge-outcomes-and-winners/)

1. Gold Winner – [Lockdrop](https://lockdrop.com/)
2. Silver Winner – [Shaxware](https://www.shaxware.com/)
3. Bronze Winner – SoundAuth ([Trillbit](https://www.trillbit.com/)

This year’s FIDO Developer Challenge reached a successful conclusion, with a ceremonial event during [Authenticate 2021](https://authenticatecon.com/event/authenticate-2021-conference/) of the ceremony is available now, and we’re pleased to share more detailed stories of the three finalists as well as the rest of the teams that made it to the final stage.
* [Integrating FIDO with Verifiable Credentials (8.30 am start)](https://iiw.idcommons.net/10E/_Integrating_FIDO_with_Verifiable_Credentials_(8.30_am_start)) by David Chadwick

* [The Use of FIDO2 and Verifiable Credentials (David Chadwick)](https://youtube.com/watch?v%3Dl3taGxBdrRU)

W3C Web Authentication (FIDO2) provides a mechanism for strong authentication whilst W3C Verifiable Credentials provide a mechanism for strong identification and authorisation. Together they make an unbeatable pair for identity management.

Prof. David Chadwick presented work on sharing W3C Verifiable Crendentials via FIDO2 key setup with issuers of credentials.  In a nutshell, the holder and issuer use the WebAuthN protocol to strongly authenticate before the issuer protects the credentials with its signature.  Upon providing credentials to a relying party, the issuer (acting in an IDP capacity, so they must be online) will verify the identity of the holder via FIDO2 WebAuthN so that the credentials (or selected claims in the credentials for selective disclosure) can be shared with the relying party.  Ephemeral keys are created to bind the holder with such credentials shared to the relying party/verifier.  The relying party/verifier can use X.509 certs to confirm that the issuer is valid by checking the signature on the derived credential from the holder.


## OAuth

## SCIM

## SAML

## KMIP

## Secure QR Code
