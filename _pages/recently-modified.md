---
title: "Recently Updated Content"
description: "Shows listing of posts in order of how recently they've been updated."
permalink: /updated/
layout: single
published: false
---


<ul>
{% assign posts = site.posts | sort: 'post.last_modified_at' %}
{% for post in posts %}
  <li>{{ post.title }} (original post date: {{ post.date }})</li>
{% endfor %}
</ul>