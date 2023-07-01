---
layout: archive
title: New Content
author_profile: false
sidebar:
  - title: "Identity Decentralized"
    image: "/images/the-world-map-from-a-binary-code.webp"
    image_alt: "Binary Globe Image by GDj"
    nav: "didnav"
share: true
classes: wide
permalink: new/
toc: false
published: false
---

{% assign modified = site.posts | sort: 'date' | reverse %}
{% for post in modified %}
    {{post.date}}
	{% include archive-single.html type='list' %}
{% endfor %}	