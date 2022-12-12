# Hyland Creds

* [Hyland, Dataswift and Case Western Reserve University partner to advance web-based verifiable credential storage](https://news.hyland.com/hyland-dataswift-and-case-western-reserve-university--partner-to-advance-web-based-verifiable-credential-storage/) Hyland Credentials

The initial phase of the partnership involved building a web-based interface that enables users to easily store and manage their verifiable credentials by uploading them to a user-owned, encrypted personal data account (PDA), an innovative privacy-preserving solution developed by Dataswift, another strategic partner of xLab. That account is the storage system of a personal data server legally owned by users themselves and comes with a Data Passporting function that can be called upon by any application, allowing users to license their data on demand, quickly and securely, with any relevant party.
* [Blockcerts v3 release, a Verifiable Credentials implementation](https://lists.w3.org/Archives/Public/public-credentials/2021Dec/0051.html)  Julien Fraichot (Monday, 13 December)

I am excited to share with you today the release of [Blockcerts](https://www.blockcerts.org/) V3. As you may already know the earlier versions of Blockcerts were architected by Kim H. Duffy through Learning Machine and leveraged the Open Badge standard.

We have followed through with the initial [ideas established at RWOT 9 in Prague in December 2019, to align Blockcerts with the Verifiable Credential specification](https://github.com/WebOfTrustInfo/rwot9-prague/blob/master/final-documents/BlockcertsV3.md).

The main change is the alignment with the [W3C Verifiable Credentials specification 3](https://www.w3.org/TR/vc-data-model/).

Regarding the standard itself metadata and display are entering the default standard. metadata comes in replacement of metadataJson and remains a stringified JSON that will allow consumers to register specific data which are too unique for issuances to be defined in the context.

display brings in [a little bit of novelty 2](https://github.com/blockchain-certificates/cert-schema/blob/master/cert_schema/3.0/displaySchema.json%23L6) images or pdfs, in addition to the more classic HTML.

