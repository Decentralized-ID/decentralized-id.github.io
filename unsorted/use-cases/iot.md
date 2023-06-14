---
published: false
---

# IOT

## Explainer 

* [Distributed Ledger Technologies, IAM, and the Truth in Things](https://www.youtube.com/watch?v=VV2rLgH9TUE) 2019-06-27 Identiverse Robert Brown
  > The Internet of Things has a problem with data silos – it’s difficult for data to move across domains and prove where it came from. Users of IoT data must understand how Things were made and kept up-to-date if they are to know the data received is truthful. Yet keeping Things healthy is not the sole responsibility of a single actor; components of a Thing may be shared amongst hardware and software vendors, system integrators, retailers, system operators, owners, regulators or third parties. Safety and security rests with all involved in authorizing updates, how and when they are applied as well as the right to repair when Things are no longer officially supported. Shared device lifecycle assurance is the basis for verifiable service histories of Things which give data provenance. When data can be proven to originate from reliable sources, its value increases while reducing the risk of using it. Enabling third parties to build value from data would unlock the true value of IoT which in turn could fund its upkeep. This talk will outline how identity and shared ledger technology have key roles to building Truth in Things for a sustainable IoT.
* [Alternatives to the CompuServe of Things](https://www.windley.com/archives/2021/07/alternatives_to_the_compuserve_of_things.shtml) 2021-07 Phil Windley
  > The current model for connected things puts manufacturers in between people and their things. That model negatively affects personal freedom, privacy, and society. Alternate models can provide the same benefits of connected devices without the societal and personal costs.

* [Why Machines Need Self-Sovereign Identities](https://www.peaq.com/blog/why-machines-need-self-sovereign-identities) Peaq
  > As the world becomes even more connected and more machines are hooked up to the internet, the ability for machines to move, trade and interact securely and efficiently becomes increasingly important to life and business. Today’s centralized networks do not enable this. Machines today exist on closed, permission-based environments which massively limit which other machines can be interacted with, what machines can do and where they can go.

* [Why is Trusted Identity Important in IoT Commerce?](https://dlt.mobi/why-is-trusted-identity-important-in-iot-commerce/)
  > The evident solution is to imbue connected entities with unique, tamper-evident, self-sovereign, [Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/?mc_cid=1a98f7f0e4&mc_eid=UNIQID), developed by the [W3C](https://www.w3.org/?mc_cid=1a98f7f0e4&mc_eid=UNIQID), anchored in a decentralized trust network. For MOBI’s community, this is the [Integrated Trust Network, or ITN](http://dlt.mobi/itn?mc_cid=1a98f7f0e4&mc_eid=UNIQID).

* [Self-Sovereign Identity and IoT – insights from the Sovrin Foundation](https://insureblocks.com/ep-146-self-sovereign-identity-and-iot-insights-from-the-sovrin-foundation/) Insureblocks
  > Michael Shea is the Managing Director of the Dingle Group and the Chair of Sovrin Foundation’sSSI in IoT Working Group. In this podcast we discussed the white paper he authored on Self Sovereign Identity and IoT. To explain the opportunities SSI can provide to IoT, Michael introduces us to three profiles: Jamie (machine to person), Bob (machine to machine) and Bessie the cow (digital twin).

* [Relationships in the Self-Sovereign Internet of Things](https://www.windley.com/archives/2020/12/relationships_in_the_self-sovereign_internet_of_things.shtml)
  > DIDComm-capable agents provide a flexible infrastructure for numerous internet of things use cases. This post looks at Alice and her digital relationship with her F-150 truck. She and the truck have relationships and interactions with the people and institutions she engages as she co-owns, lends and sells it. These and other complicated workflows are all supported by a standards-based, open-source, protocol-supporting system for secure, privacy-preserving messaging.

* [APPLYING CONCEPTS FROM SELF SOVEREIGN IDENTITY TO IOT DEVICES](https://www.theinternetofthings.eu/tim-weingartner-oskar-camenzind-identity-things-applying-concepts-self-sovereign-identity-iot) IOT dot EU
  > Devices are equipped by the manufacturer with an identity stored in a trusted execution environment (TEE) and secured by a blockchain. This identity can be used to trace back the origin of the device. During the bootstrapping process on the customer side, the identity registration of the device is updated in the blockchain. This process is performed by a so-called registrar. Smart contracts prevent unsolicited transfer of ownership and track the history of the device. Besides proof of origin and device security our concept can be used for device inventory and firmware upgrade.

* [Easier IoT Deployments with LoraWan and Helium](https://www.windley.com/archives/2022/04/easier_iot_deployments_with_lorawan_and_helium.shtml) 2022-04 Phil Windley
  > Unlike a Wifi network, you don't put the network credentials in the device, you put the devices credentials (keys) in the network. Once I'd done that, the sensor started connecting to hotspots near my house and transmitting data. Today I've been driving around with it in my truck and it's roaming onto other hotspots as needed, still reporting temperatures.

* [Digital Twins and Self-Sovereign Identity: Build the next generation of Simulation with privacy preservation](https://iotpractitioner.com/digital-twins-and-self-sovereign-identity-build-the-next-generation-of-simulation-with-privacy-preservation/) IOT Practicioner
  > Managing IoT devices and user identities as well as the relationships among various devices and their digital twins face significant challenges. First, a lack of Identity Credential and Access Management (ICAM) standards for IoT creates proprietary standards and a lack of interoperability. Second, the operational lifecycle of IoT devices complicates integration of traditional ICAM. Lastly, ICAM technology must adapt to the proliferation of connected devices. This evolution requires a digital trust framework and the decentralized architecture of Self-Sovereign Identity (SSI).

* [Smart Property](https://www.windley.com/archives/2021/08/smart_property.shtml) Windley
  > Smart property is much more than the anemic connected things we have now. Smart property imagines a world where every thing participates in digital communities and ecosystems, working through programmable agents under the owners control.

### Digital Twins

* [Digital Twins and Self-Sovereign Identity: Build the next generation of Simulation with privacy preservation](https://iotpractitioner.com/digital-twins-and-self-sovereign-identity-build-the-next-generation-of-simulation-with-privacy-preservation/) IOT Practicioner
  > The rise in the use of advanced analytics, machine learning (ML) and Artificial Intelligence (AI) and the Internet of Things (IoT) today have driven the technology of simulation into the concept of the digital twin. Digital twins are generally defined as a virtual digital model of a physical system that is used to make better decisions about the real world physical system. Digital twins are usually intertwined with sensors and include a two-way interaction between the physical and digital twin.

## Hackathon Entries

* [Decentralized Identity of Things](https://blog.darrenjrobinson.com/decentralized-identity-of-things/) Winner Microsoft Decentralized Identity Hackathon
  > In a real world scenario we anticipate a software based wallet for Decentralized Identity of Things. That would allow automation of online stores to obtain verifiable credentials programmatically. 

* [DIDoT - DID of Things. Decentralized Identity of Things](https://devpost.com/software/did-of-things-didot-allergen-management-in-food-shopping). 
  > Allergen management in food shopping. Based on the concept of ‘things’ having verifiable credentials. [...] Our proposed solution requires a virtual wallet that can be orchestrated programmatically. We discussed how other self sovereign solutions have this capability and confirmed with the AAD Verifiable Credentials hackathon support team that this capability is not available.

## Company Stories
* [More Security in the Internet of Things – Thanks to ETO](https://www.etogruppe.com/en/news/news-from-eto/more-security-in-the-internet-of-things-thanks-to-eto.html) ETO [github](https://gitlab.com/anchor-bundle/angular-webapp)
  > The ETO GRUPPE has set itself the goal of automating communication in the Internet of Things (IoT) and, on top of that, making it more secure against access and manipulation. To achieve this, these "things" - machines, devices or vehicles - must first be given a unique identity. The solution of the innovative corporate group consists of a new type of network and authentication processes that have what it takes to revolutionize the way we use the Internet today. ETO uses a network of distributed digital identities (DIDs) and verifiable credentials (VCs). A side benefit from the perspective of human Internet users: they regain data sovereignty over their personal data. The ETO solution will enable secure logins on both the Internet and the Internet of Things (IoT)

* [Trust but Verify](https://stateofidentity.libsyn.com/trust-but-verify) Liminal Podcasts
  > Peter Padd, Co-Founder & CEO at Fortifyedge shares how he's built Zero Trust authentication software that provides IoT device OEM's with password-free authentication utilizing Tiny Machine Learning at the edge.

* [Capitalizing on Self-Sovereign Identity for Machines](https://venafi.com/blog/capitalizing-self-sovereign-identity-machines-part-one) [Part One]
  > By providing a means to globally define an indisputable link between a machine and its machine identity across different sites, networks and businesses, we can secure IoT like never before.
  > 
  > The filancore integration for Verifiable Credentials is available now. You can learn more from the [Venafi Marketplace](https://marketplace.venafi.com/details/verifiable-credentials-for-iot/).

## Protocols

* [Picos at the Edge](https://www.windley.com/archives/2021/11/picos_at_the_edge.shtml) 2021-11 Phil Windley
  > You can play with this first hand at [NoFilter.org](https://nofilter.org/), which brands itself as a "the world's first unstoppable, uncensorable, undeplatformable, decentralized freedom of speech app." There's no server storing files, just a set of Javascript files that run in your browser. Identity is provided via [Metamask](https://metamask.io/) which uses an Ethereum address as your identifier. [I created some posts on NoFilter](https://nofilter.org/#/0xdbca72ed00c24d50661641bf42ad4be003a30b84) to explore how it works.


## Infographic

* [Now Animals too can have their own #decentralizedidentity to help them send their status updates](https://twitter.com/debimr75/status/1347915348293533699)  Debajani Mohanty
  > to the rightful owner from their #IoT devices. #Decentralized #digitalidentity for #IoT devices would lead to #SmartFarming
  > ![](https://pbs.twimg.com/media/ErTBmLrXIAYCFpT?format=jpg)

## Organization
* [Self-Sovereign Digital Twins](https://dlt.mobi/self-sovereign-digital-twins/) mobi
  > A Citopia Self-Sovereign Digital Twin™ (SSDT™) is a digital twin whose controller has the ability to participate as an autonomous economic agent in trusted Web3 transactions.
* [Battery Passport and the Battery Self-Sovereign Digital Twin](https://dlt.mobi/battery-passport-the-battery-ssdt/) Mobi
  > Similarly, a [battery passport](https://dlt.mobi/battery-passport) is nothing but a presentation of data points about a particular battery – who manufactured it, its physical and chemical composition, its current state of health, whether it was refurbished or repurposed from another battery, and so on.
* [LFPH tackles the next frontier in Open Source Health Technology: The rise of Digital Twins](https://www.lfph.io/2022/08/29/lfph-tackles-the-next-frontier-in-open-source-health-technology-the-rise-of-digital-twins/) 2022-08-29 Linux Foundation Public Health
  > To create a pairing between the digital world and the real world, a digital twin leverages real time data, such as smart sensor technology, coupled with analytics, and often artificial intelligence (AI) in order to detect and prevent system failures, improve system performance, and explore innovative uses or functional models.
* [Digital Twin Consortium](https://www.digitaltwinconsortium.org/)
  > Digital Twin Consortium drives the awareness, adoption, interoperability, and development of digital twin technology. Through a collaborative partnership with industry, academia, and government expertise, the Consortium is dedicated to the overall development of digital twins. We accelerate the market by propelling innovation and guiding outcomes for technology end-users.

## User experience
* [#ResistIoT: IoT as a medium for surveillance](https://wider.team/2021/04/21/resistiot/) wider team 2021-04-21
  > - Clinical technology as workplace surveillance. Hospital providers talk about their frustration with connected technologies because it feels like their every motion is being monitored and tracked, used by bosses to evaluate their speed and cost efficiency.
  > - Civic technologies as government surveillance. From [Oakland’s corner traffic cameras](https://www.aclunc.org/blog/how-fight-stop-oaklands-domain-awareness-center-laid-groundwork-oakland-privacy-commission) leading to mass rallies to [Boston Police](https://www.independent.co.uk/life-style/gadgets-and-tech/news/robots-police-dog-spot-boston-dynamics-a9218491.html) [tests](https://reason.com/2019/11/26/massachusetts-police-test-out-robot-dogs-is-dystopia-on-its-way/) and [NYPD robot dogs](https://www.theverge.com/2021/2/24/22299140/nypd-boston-dynamics-spot-robot-dog), IoT is deep in the creepy depths of [the uncanny valley](https://en.wikipedia.org/wiki/Uncanny_valley). 2019-11-26
  > - Consumer technology as commercial surveillance. Alexa, Google, and Apple know too much about you and use it to sell adjacent services.

## Paper

* [IoT Swarms + SSI in constrained networks](https://docs.google.com/presentation/d/15ix2vzR_Dq9xcs-8OY0qBjapy9dpY-WdRKph9SiEY-0/edit?usp=sharing) [source](https://iiw.idcommons.net/12E/_IoT_Swarms_+_SSI_in_constrained_networks) - [paper](https://arxiv.org/abs/2107.10232) Geovane Fedrecheski, Laisa C. P. Costa, Samira Afzal, Jan M. Rabaey, Roseli D. Lopes, Marcelo K. Zuffo
  > One of the challenges identified by this last paper is the overhead of using SSI, which poses a challenge for adoption on constrained IoT networks. For example, while the Long Range (LoRa) communication, often used in IoT systems, only allows payloads of up to 240 bytes, a single DID Document typically occupies 500 bytes or more. Similarly, messages using DIDComm tend to use at least 1 kilobyte, which prevents its use on constrained networks.<br>Figure 1. Binary versions of DIDComm and DID Documents are needed to allow transmission in LoRa networks. The payload, in blue, is a DID Document. The overhead, in orange, is the protocol overhead due to the message signature.
  > 
  > A low-overhead approach for self-sovereign identity in IoT	We present a low-overhead mechanism for self-sovereign identification and communication of IoT agents in constrained networks. Our main contribution is to enable native use of Decentralized Identifiers (DIDs) and DID-based secure communication on constrained networks, whereas previous works either did not consider the issue or relied on proxy-based architectures. We propose a new extension to DIDs along with a more concise serialization method for DID metadata. Moreover, in order to reduce the security overhead over transmitted messages, we adopted a binary message envelope. We implemented these proposals within the context of Swarm Computing, an approach for decentralized IoT. Results showed that our proposal reduces the size of identity metadata in almost four times and security overhead up to five times. We observed that both techniques are required to enable operation on constrained networks.	

* [Self-Sovereign Identity for IoT Devices](https://dltc.spbu.ru/images/articles/Kulabukhova2019_Chapter_Self-SovereignIdentityForIoTDe_compressed.pdf) 2019 Nataliia Kulabukhova, Andrei Ivashchenko, Iurii Tipikin, and Igor Minin
  > in our point of view, a lot of development groups are working in parallel on the similar topics, yet it is not clear what is going on inside. In this paper we will try to define the differences and discuss both pros and cons of using such commonly known technologies as Sovrin based upon the Hyperledger Indy technology, Civic, Jolocom, uPort and some others. Besides, we’ll tackle the idea of using the SSI for inanimate object and how it can be constructed in this way.

## Government

* [SSI In IoT, The SOFIE Project](https://www.thedinglegroup.com/blog/2021/4/6/ssi-in-iot-the-sofie-project) The Dingle Group
  > For the 22nd Vienna Digital Identity Meetup* we hosted three of the lead researchers from the [EU H2020](https://ec.europa.eu/programmes/horizon2020/) funded The [SOFIE Project](https://www.sofie-iot.eu/).  The SOFIE Project wrapped up at the end of last year a key part of this research focused on the the use of SSI concepts in three IoT sectors (energy, supply chain, and mixed reality gaming) targeting integrating SSI in without requiring changes to the existing IoT systems.


