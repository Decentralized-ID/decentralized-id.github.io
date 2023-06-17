---
layout: archive
title: Recently Updated Content
author_profile: false
sidebar:
  - title: "Identity Decentralized"
    image: "/images/the-world-map-from-a-binary-code.webp"
    image_alt: "Binary Globe Image by GDj"
    nav: "didnav"
share: true
classes: wide
name: recent
permalink: recent/
toc: false
---

{% assign modified = site.posts | sort: 'last_modified_at' | reverse %}
{% for post in modified %}
  {% unless forloop.index0 >= 80 %}
    {% include archive-single.html type='list' %}
  {% endunless %}
{% endfor %}	