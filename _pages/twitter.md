---
layout: single
title: Twitter Query
permalink: /twitter/
toc: false
classes: wide
---

{% for row in site.data.10-27-2020decentralizeid %}
  <h3>{{ row.Text | truncate: 70 }}</h3>
  <p><sup><a href="{{ row.Link }}">{{ row.Time }}</a> - <a href="https://twitter.com/{{ row.User }}"><b>@{{ row.User }}</b></a> - Following: <a href="https://twitter.com/{{ row.User }}/following/">{{ row.Following }}</a> Followed: <a href="https://twitter.com/{{ row.User }}/followers/">{{ row.Followers }}</a> {% if row.Retweets != "0" %}Retweets: <a href="{{ row.Link }}/retweets">{{ row.Retweets }}</a>{% endif %}</sup></p>
  <blockquote>{{ row.Text }}</blockquote>
  {% assign htags = row.Hashtags | split: "', '" %}
  {% for h in htags %}<a href="https://twitter.com/hahstag/{{ h | remove: "['" | remove: "']" }}">#{{ h | remove: "['" | remove: "']" }}</a> {% endfor %}
{% endfor %}

