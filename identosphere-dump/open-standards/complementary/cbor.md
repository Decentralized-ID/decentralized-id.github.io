# Concise Binary Object Representation (IETF)

* [Regarding CBOR-LD Web Transports](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0100.html)  Orie Steele (Saturday, 10 April)
  > I pushed up this small demo showing how to transport JSON-LD as CBOR-LD over QR Code and Web NFC.
* [transmute-industries/cbor-ld-web-transports](https://github.com/transmute-industries/cbor-ld-web-transports) github
* [CBOR-LD stabilization (was: Re: Regarding CBOR-LD Web Transports)](https://lists.w3.org/Archives/Public/public-credentials/2021Apr/0127.html)  Manu Sporny (Wednesday, 21 April)
  > Digital Bazaar has a few updates to share with the community.
  > 
  > 1. With a huge thank you to Dave Longley, a new version of the CBOR-LD library, with generalized and stable algorithms, and that works in the browser and node.js, has been released:
  > 
  > [https://github.com/digitalbazaar/cborld](https://github.com/digitalbazaar/cborld)
  > 
  > 2. We have split out the CBOR-LD command line interface into a separate project:
  > 
  > [https://github.com/digitalbazaar/cborld-cli/tree/initial](https://github.com/digitalbazaar/cborld-cli/tree/initial)
  > 
  > 1. DB has released a CBOR-LD to QR Code image library for encoding and decoding Verifiable Presentations:
  > 
  > [https://github.com/digitalbazaar/vpqr](https://github.com/digitalbazaar/vpqr)
  > 
  > 1. After some consultation with Mattr and Transmute, we've settled on a base32 alphanumeric QR Code encoding that is 10% more  space efficient than base64url byte mode. This is important because this format is compatible with hundreds of QR Code readers on the market. Every QR Code reader that we've tested has worked with this new format.
* [Mike Jones shares](https://self-issued.info/?p=2136) that CBOR (Concise Binary Object Representation)  is officially a [specification at IETF](https://www.rfc-editor.org/rfc/rfc8943) - woohoo! and it is a key part of [ISO’s mDL standard](https://www.iso.org/committee/45144.html) (date fields must use it).
  > The Concise Binary Object Representation (CBOR), as specified in RFC 7049, is a data format whose design goals include the possibility of extremely small code size, fairly small message size, and extensibility without the need for version negotiation.
* [https://youtu.be/fEBNGj377Vc](https://youtu.be/fEBNGj377Vc)
Second demo video using a different potential flow: [https://www.youtube.com/watch?v=fEBNGj377Vc](https://www.youtube.com/watch?v=fEBNGj377Vc)

Paper VC’s are hard to bring to parity with “digital VC’s”. The biggest issue is binding subject to holder and verifying that. There were also callouts on how do you prevent replication.

Traditionally, QR codes with the entire VC can be put onto a piece of paper. We proposed compression on those QR codes using CBOR-LD that reduces size of codes by 50%.

Alternative ways include adding VC’s into NFC chips and adding the NFC identifier as a claim to the VC preventing duplication. There is a cost overhead to this compared to paper but is a cost potentially worth occurring.
