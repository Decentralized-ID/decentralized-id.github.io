---
layout: single
classes: wide
title: Blockchain Identity Reources - TOML
description: The beginnings of a tagged database for blockchain identity related resources.
permalink: toml/id-toml.html
---

My first page besides "home" with the minimal mistakes theme. All of my pages will migrate to minimal mistakes, and integrated, once I get the feel for it.

This page has two toml files from [infominer33/SourceCrypto](https://github.com/infominer33/SourceCrypto) embedded into it, with some help from [gist-it.appspot.com](https://gist-it.appspot.com)

## Wish List

* some simple way to check [infominer.id/DIDecentralized](https://infominer.id/DIDecentralized) against these lists, and output a list of links that have yet to be included.

* an app that will take a list of links as the input and output a toml file with title\description automatically populated based on metadata..

that would make it a lot easier.. then I just go in and fine tune each entry.

I suppose it would make the most sense to prioritize those objectives, rather than constructing everything by hand.

Scraping a list of links from wherever I want is simple.. so really the two things are checking a list of links against a toml file(s), outputting any links not found in the db already. Another script to construct a toml file grabbing metadata.

@MaciekLaskus suggested I include authors, which is true. I believe I intended to eventually:
  >what's really missing is tagging all of these resources by authors, co-authors, references/citations
  >
  > once this is done, topical tags can be derived algorithmically<br>
  >  [Enabling Author-Centric Ranking of Web Content](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.397.8960&rep=rep1&type=pdf)

## blockchain-id.toml

* [SourceCrypto/toml/application/blockchain-id.toml](https://github.com/infominer33/SourceCrypto/blob/master/toml/application/blockchain-id.toml)

<script src="https://gist-it.appspot.com/https://github.com/infominer33/SourceCrypto/raw/master/toml/application/blockchain-id.toml"></script>

## blockchain-id2.toml

* [SourceCrypto/toml/application/blockchain-id2.toml](https://github.com/infominer33/SourceCrypto/blob/master/toml/application/blockchain-id2.toml)

<script src="https://gist-it.appspot.com/https://github.com/infominer33/SourceCrypto/raw/master/toml/application/blockchain-id2.toml"></script>
