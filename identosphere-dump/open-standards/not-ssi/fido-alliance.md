# Fido Alliance

* [LoginWithFIDO.com](https://loginwithfido.com/)
* [Consumer Research](https://fidoalliance.org/consumerresearch/)  
* [A WebAuthn Apache module?](https://hanszandbelt.wordpress.com/2022/05/05/a-webauthn-apache-module/) Hans Zandbelt
  > any sensible WebAuthn/FIDO2 Apache module would rely on an externally running “Provider” software component to offload the heavy-lifting of onboarding and managing users and credentials.
* [2021 FIDO Developer Challenge: Outcomes and Winners](https://fidoalliance.org/2021-fido-developer-challenge-outcomes-and-winners/)

1. Gold Winner – [Lockdrop](https://lockdrop.com/)
2. Silver Winner – [Shaxware](https://www.shaxware.com/)
3. Bronze Winner – SoundAuth ([Trillbit](https://www.trillbit.com/)

This year’s FIDO Developer Challenge reached a successful conclusion, with a ceremonial event during [Authenticate 2021](https://authenticatecon.com/event/authenticate-2021-conference/) of the ceremony is available now, and we’re pleased to share more detailed stories of the three finalists as well as the rest of the teams that made it to the final stage.
* [Integrating FIDO with Verifiable Credentials (8.30 am start)](https://iiw.idcommons.net/10E/_Integrating_FIDO_with_Verifiable_Credentials_(8.30_am_start)) by David Chadwick

* [The Use of FIDO2 and Verifiable Credentials (David Chadwick)](https://youtube.com/watch?v=l3taGxBdrRU)

W3C Web Authentication (FIDO2) provides a mechanism for strong authentication whilst W3C Verifiable Credentials provide a mechanism for strong identification and authorisation. Together they make an unbeatable pair for identity management.

Prof. David Chadwick presented work on sharing W3C Verifiable Crendentials via FIDO2 key setup with issuers of credentials.  In a nutshell, the holder and issuer use the WebAuthN protocol to strongly authenticate before the issuer protects the credentials with its signature.  Upon providing credentials to a relying party, the issuer (acting in an IDP capacity, so they must be online) will verify the identity of the holder via FIDO2 WebAuthN so that the credentials (or selected claims in the credentials for selective disclosure) can be shared with the relying party.  Ephemeral keys are created to bind the holder with such credentials shared to the relying party/verifier.  The relying party/verifier can use X.509 certs to confirm that the issuer is valid by checking the signature on the derived credential from the holder.
* [Fido Passkey](https://www.pingidentity.com/en/resources/blog/post/how-fido-passkeys-accelerate-passwordless-future.html)
* * [What is FIDO? Infographic](https://www.scmagazine.com/resource/identity-and-access/what-is-fido)

- [How passkeys pave the way for passwordless authentication](https://www.scmagazine.com/resource/identity-and-access/how-passkeys-pave-the-way-for-passwordless-authentication)
* [FIDO: Everything You Need to Know About Fast Identity Online](https://www.pingidentity.com/en/company/blog/posts/2021/fast-identity-online-fido.html)
* [Use Fido2 Passwords Authentication with Azure AD](https://damienbod.com/2022/01/17/use-fido2-passwordless-authentication-with-azure-ad/) Damion Bod

This article shows how to implement FIDO2 passwordless authentication with Azure AD for users in an Azure tenant.
* [Charting an Accelerated Path Forward for Passwordless Authentication Adoption](https://fidoalliance.org/charting-an-accelerated-path-forward-for-passwordless-authentication-adoption/) FIDO

* [The paper introduces](https://media.fidoalliance.org/wp-content/uploads/2022/03/How-FIDO-Addresses-a-Full-Range-of-Use-CasesFINAL.pdf) multi-device FIDO credentials, also informally referred to by the industry as “passkeys,” which enable users to have their FIDO login credentials readily available across all of the user’s devices.
* [FIDO passkeys are an existential threat to fintech startups](https://werd.io/2022/fido-passkeys-are-an-existential-threat-to-fintech-startups)

by definition, screen scraping requires storing a user’s financial system passwords in clear text. Nonetheless, you can bet that every system that integrates with payroll systems, and almost every system that integrates with banks (at a minimum), uses the technique. The US has badly needed [open banking style standards](https://standards.openbanking.org.uk/api-specifications/) for years.
* [FIDO Alliance Supports Biden Administration EO on Cybersecurity](https://fidoalliance.org/fido-alliance-supports-biden-administration-eo-on-cybersecurity/)

There have been a number of high profile attacks against critical American infrastructure in recent months, including the Solarwinds supply chain attack that exposed much of the government to potential risk. Top of mind in recent days is the ransomware attack against Colonial Pipeline, which significantly impacted the flow of refined oil across America. These attacks expose the vulnerability of critical infrastructure in the United States, and the Biden Administration is issuing federal directives that will minimize or eliminate risk.
