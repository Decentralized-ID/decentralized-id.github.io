---
layout: single
title: Twitter Query
permalink: /twitter/
toc: false
classes: wide
---

{% for row in site.data.ssitw102820 %}
  <h3><a href="{{ row.Link }}">{{ row.Time }}</a> <a href="https://twitter.com/{{ row.User }}"><b>@{{ row.User }}</b></a></h3>
  <p><sup>Likes: <a href="{{ row.Link }}/likes">{{ row.Favorites }}</a> Following: <a href="https://twitter.com/{{ row.User }}/following/">{{ row.Following }}</a> Followed: <a href="https://twitter.com/{{ row.User }}/followers/">{{ row.Followers }}</a> {% if row.Retweets != "0" %}Retweets: <a href="{{ row.Link }}/retweets">{{ row.Retweets }}</a>{% endif %} {% if row.ReplyURL != "[]" and row.ReplyURL != blank %} - <a href="{{ row.ReplyURL }}">Reply to</a>{% endif %}</sup></p>
  <blockquote>{{ row.Text }}</blockquote>
  {% if row.Urls != "[]" %}
    {% assign lnks = row.Urls | split: "," %}
    {% assign urlt = row.UrlTitle | split: "," %}
    {% assign urld = row.UrlDesc | split: "," %}
    {% assign urli = row.UrlImg | split: "," %}
    {% assign foo = 0 %}
    {% for lnk in lnks %}{% assign ln = lnk | remove: "[" | remove: "]" | remove: "'" | remove: '"' %}{% assign urt = urlt[foo] | remove: "[" | remove: "]" | remove: "'" | remove: '"' | remove: 'None'  %}{% assign urd = urld[foo] | remove: "[" | remove: "]" | remove: "'" | remove: '"' | remove: 'None' %}{% assign uri = urli[foo] | remove: "[" | remove: "]" | remove: "'" | remove: '"' | remove: 'None' %}
<a href="{{ ln }}">{% if urt != blank %}{{ urt }}{% else %}{{ ln }}{% endif %}</a>
{% if urd != blank %}<blockquote>{{ urd | remove: "[" | remove: "]" | remove: "'" | remove: '"' }}</blockquote>{% endif%} 
{% if uri != blank %}<img src="{{ uri }}"/>{% endif%}{% assign foo = foo | plus: 1 %}
    {% endfor %}
  {% endif %}
  {% assign htags = row.Hashtags | split: "', '" %}
  {% for h in htags %}<a href="https://twitter.com/hashtag/{{ h | remove: "['" | remove: "']" }}">#{{ h | remove: "['" | remove: "']" }}</a> {% endfor %}
  {% if row.ImageUrls != "[]" %}
  {% assign imgs = row.ImageUrls | split: "', '" %}
  {% for img in imgs %}<img src="{{ img | remove: "['" | remove: "']" }}">{% endfor %}
  {% endif %}
{% endfor %}

