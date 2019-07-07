---
layout: single
title:  "InfoHub Contributors: Using Minimal Mistakes"
description: "Contributing to the InfoHub via GitHub, Jekyll and Minimal Mistakes."
excerpt: >
  Since I've created four GitHub organizations for these public-domain educational resources, I needed to make it clear for others to understand and join in on the fun. You are presented with an review of how I'm using Minimal Mistakes to Publish Content for Free via GitHub Pages.
header:
  image: assets/img/minimal-mistakes-quickstart-header.png
  teaser: assets/img/minimal-mistakes-teaser.png
  og_image: assets/img/minimal-mistakes-teaser.png
  caption: "Minimal Mistakes Setup and [Quick-Start](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)."
tags: 
  - Public-Domain
  - Open-Source
  - Jekyll
  - CSS
  - JavaScript
  - Configuration
  - MinimalMistakes
  - GitHub-Pages
  - Web-Pub
  - Web-Working
toc_sticky: false
classes: wide
#authors: 
#  - "<a href='https://infominer.id'>Infominer</a>"
#  - "<a href='https://www.caballerojuan.com'>JuanSC</a>"
permalink: using-minimal-mistakes/
categories: [InfoHub, SourceCrypto, Web-Work-Tools, DIDecentral, Learn-Crypto-Trading, Contributors-Guide]
published: true
last_modified_at: 2019-06-26T11:22:33-23:00
---

Since I've created four GitHub organizations for these public-domain educational resources, I needed to make it clear for others to understand and join in on the fun.

## Using Minimal Mistakes

Each site is set up a little different, and will have its own version of this post, eventually.

[GitHub Pages Starter Pack: Minimal Mistakes](https://web-work.tools/github-pages-starter-pack/#minimal-mistakes){: .btn .btn--info .align-center}

If you peruse the resource linked above, you'll find there are a number of integrations and potential use-cases that I've yet to explore, practically speaking.

## [infominer33/infominer33.github.io](https://github.com/infominer33/infominer33.github.io)

![](https://imgur.com/iOb9STH.png)


## Directory Structure

```
minimal-mistakes
├── _data                      # data files for customizing the theme
|  ├── navigation.yml          # main navigation links
|  └── ui-text.yml             # text used throughout the theme's UI
├── _includes
|  ├── analytics-providers     # snippets for analytics (Google and custom)
|  ├── comments-providers      # snippets for comments
|  ├── footer                  # custom snippets to add to site footer
|  ├── head                    # custom snippets to add to site head
|  ├── feature_row             # feature row helper
|  ├── gallery                 # image gallery helper
|  ├── group-by-array          # group by array helper for archives
|  ├── nav_list                # navigation list helper
|  ├── toc                     # table of contents helper
|  └── ...
├── _layouts
|  ├── archive-taxonomy.html   # tag/category archive for Jekyll Archives plugin
|  ├── archive.html            # archive base
|  ├── categories.html         # archive listing posts grouped by category
|  ├── category.html           # archive listing posts grouped by specific category
|  ├── collection.html         # archive listing documents in a specific collection
|  ├── compress.html           # compresses HTML in pure Liquid
|  ├── default.html            # base for all other layouts
|  ├── home.html               # home page
|  ├── posts.html              # archive listing posts grouped by year
|  ├── search.html             # search page
|  ├── single.html             # single document (post/page/etc)
|  ├── tag.html                # archive listing posts grouped by specific tag
|  ├── tags.html               # archive listing posts grouped by tags
|  └── splash.html             # splash page
├── _sass                      # SCSS partials
├── assets
|  ├── css
|  |  └── main.scss            # main stylesheet, loads SCSS partials from _sass
|  ├── images                  # image assets for posts/pages/collections/etc.
|  ├── js
|  |  ├── plugins              # jQuery plugins
|  |  ├── vendor               # vendor scripts
|  |  ├── _main.js             # plugin settings and other scripts to load after jQuery
|  |  └── main.min.js          # optimized and concatenated script file loaded before </body>
├── _config.yml                # site configuration
├── Gemfile                    # gem file dependencies
├── index.html                 # paginated home page showing recent posts
└── package.json               # NPM build scripts
```

### CSS - Stylesheets

At the moment, I'm quite CSS agnostic. One thing at a time.. However, if you wanted to add a little style to the page, I might not complain. This is how the sytlesheets are named \ organized.

* [mmistakes.github.io/minimal-mistakes/docs/stylesheets/](https://mmistakes.github.io/minimal-mistakes/docs/stylesheets/)
The theme’s assets/css/main.css file is built from several SCSS partials located in _sass/ and is structured as follows:

```
minimal-mistakes
├── _sass
|  └── minimal-mistakes
|     ├── vendor               # vendor SCSS partials
|     |   ├── breakpoint       # media query mixins
|     |   ├── magnific-popup   # Magnific Popup lightbox
|     |   └── susy             # Susy grid system
|     ├── _animations.scss     # animations
|     ├── _archive.scss        # archives (list, grid, feature views)
|     ├── _base.scss           # base HTML elements
|     ├── _buttons.scss        # buttons
|     ├── _footer.scss         # footer
|     ├── _masthead.scss       # masthead
|     ├── _mixins.scss         # mixins (em function, clearfix)
|     ├── _navigation.scss     # nav links (breadcrumb, priority+, toc, pagination, etc.)
|     ├── _notices.scss        # notices
|     ├── _page.scss           # pages
|     ├── _print.scss          # print styles
|     ├── _reset.scss          # reset
|     ├── _sidebar.scss        # sidebar
|     ├── _syntax.scss         # syntax highlighting
|     ├── _tables.scss         # tables
|     ├── _utilities.scss      # utility classes (text/image alignment)
|     └── _variables.scss      # theme defaults (fonts, colors, etc.)
├── assets
|  ├── css
|  |  └── main.scss            # main stylesheet, loads SCSS partials in _sass


```

>To make basic tweaks to theme’s style Sass variables can be overridden by adding to `<your_project>/assets/css/main.scss`. For instance, to change the link color used throughout the theme add:

```yaml
$link-color: red;
```
### [_variables.scss](https://github.com/infominer33/infominer33.github.io/blob/master/_sass/minimal-mistakes/_variables.scss)


There are a number of other variables, you may find by following the link. These are the variables I have changed, so far. Before messing with CSS please check the variables, to be sure you aren't doing too much work!

```css

/*
   Colors
   ========================================================================== */

$gray: #7a8288 !default;
$dark-gray: mix(#000, $gray, 40%) !default;
$darker-gray: mix(#000, $gray, 60%) !default;
$light-gray: mix(#fff, $gray, 50%) !default;
$lighter-gray: mix(#fff, $gray, 90%) !default;

$background-color: #fff !default;
$code-background-color: #fafafa !default;
$code-background-color-dark: $light-gray !default;
$text-color: $dark-gray !default;
$muted-text-color: mix(#fff, $text-color, 35%) !default;
$border-color: $lighter-gray !default;
$form-background-color: $lighter-gray !default;
$footer-background-color: $lighter-gray !default;

$primary-color: #6f777d !default;
$success-color: #3fa63f !default;
$warning-color: #d67f05 !default;
$danger-color: #ee5f5b !default;
$info-color: #3b9cba !default;
$focus-color: $primary-color !default;
$active-color: mix(#fff, $primary-color, 80%) !default;

/* YIQ color contrast */
$yiq-contrasted-dark-default: $dark-gray !default;
$yiq-contrasted-light-default: #fff !default;
$yiq-contrasted-threshold: 175 !default;
$yiq-debug: false !default;

/* brands */
$behance-color: #1769ff !default;
$bitbucket-color: #205081 !default;
$dribbble-color: #ea4c89 !default;
$facebook-color: #3b5998 !default;
$flickr-color: #ff0084 !default;
$foursquare-color: #0072b1 !default;
$github-color: #171516 !default;
$gitlab-color: #e24329 !default;
$instagram-color: #517fa4 !default;
$lastfm-color: #d51007 !default;
$linkedin-color: #007bb6 !default;
$mastodon-color: #2b90d9 !default;
$pinterest-color: #cb2027 !default;
$reddit-color: #ff4500 !default;
$rss-color: #fa9b39 !default;
$soundcloud-color: #ff3300 !default;
$stackoverflow-color: #fe7a15 !default;
$tumblr-color: #32506d !default;
$twitter-color: #55acee !default;
$vimeo-color: #1ab7ea !default;
$vine-color: #00bf8f !default;
$youtube-color: #bb0000 !default;
$xing-color: #006567 !default;

/* links */
$link-color: mix(#000, $info-color, 15%) !default;
$link-color-hover: mix(#000, $link-color, 25%) !default;
$link-color-visited: mix(#fff, $link-color, 15%) !default;
$masthead-link-color: $primary-color !default;
$masthead-link-color-hover: mix(#000, $primary-color, 25%) !default;
$navicon-link-color-hover: mix(#fff, $primary-color, 75%) !default;

```


### Fonts

I've done nothing about [fonts](https://www.smashingmagazine.com/2015/11/using-system-ui-fonts-practical-guide/) yet, but I mean to.

* [smashingmagazine.com/2015/11/using-system-ui-fonts-practical-guide](https://www.smashingmagazine.com/2015/11/using-system-ui-fonts-practical-guide/)
* [web.archive.org - medium.com/designing-medium/system-shock-6b1dc6d6596f](https://web.archive.org/web/20160209004426/https://medium.com/designing-medium/system-shock-6b1dc6d6596f)
  >The obvious way to use system fonts in CSS is to… just list all of the ones you can imagine by name:
  >
  >font-family: "San Francisco", "Roboto", "Segoe UI";
  >
  >(The way CSS works, if the first font is not present, the second one will be tried, and so on. Since it’s not common for an operating system to have more than one of these fonts installed, only one will be selected.)
  >
  >We also need to take care of the older systems, including a fallback to use a generic sans serif font if nothing matches before:
  >
  >font-family: "San Francisco", "Roboto", "Segoe UI", "Helvetica Neue", "Lucida Grande", sans-serif;
  >

So, I'm not 100% but it seems that we have some default fonts installed, based upon the most popularly supported?

### JavaScript

* [mmistakes.github.io/minimal-mistakes/docs/javascript/](https://mmistakes.github.io/minimal-mistakes/docs/javascript/)

```
minimal mistakes
├── assets
|  ├── js
|  |  ├── plugins
|  |  |   ├── gumshoe.js                     # simple scrollspy
|  |  |   ├── jquery.ba-throttle-debounce.js # rate-limit functions
|  |  |   ├── jquery.fitvids.js              # fluid width video embeds
|  |  |   ├── jquery.greedy-navigation.js    # priority plus navigation
|  |  |   ├── jquery.magnific-popup.js       # responsive lightbox
|  |  |   └── smooth-scroll.js               # make same-page links scroll smoothly
|  |  ├── vendor
|  |  |   └── jquery
|  |  |       └── jquery-3.4.1.js
|  |  ├── _main.js                           # jQuery plugin settings and other scripts
|  |  └── main.min.js                        # concatenated and minified theme script
```


## Configuration

This will be most useful if you decide to clone and work on the theme locally. I have cloned the minimal mistakes theme, and am running it directly via jekyll. I have not used the remote theme or the gem-based theme method, for this particular repository.

These _config.yml and Gem settings ar particular to that method. You should even be able to copy all the files from the minimal mistakes to your own empty repository, and noticing my configuration settings be able to create your own site. However, [Minimal Mistakes Quickstart Guide](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/) is quite adequate to the task.

This guide is designed to familiarize those interested in contributing to the InfoHub, so that you may see how it is put together.


### [_config.yml](https://github.com/infominer33/infominer33.github.io/raw/master/_config.yml)

These are the most important settings for Infominer.id

```yaml
# Welcome to Jekyll!
# Theme Settings
#
# Review documentation to determine if you should use `theme` or `remote_theme`
# https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/#installing-the-theme

# theme                  : "minimal-mistakes-jekyll"
# remote_theme           : "mmistakes/minimal-mistakes"
minimal_mistakes_skin    : "mint" # "air", "aqua", "contrast", "dark", "dirt", "neon", "mint", "plum", "sunrise"

# Site Settings
locale                   : "en-US"
title                    : "InfoHub"
title_separator          : "|"
name                     : "⧉ Infominer"
description              : "Infominer on Bitcoin History, Self-Sovereign Identity, Blockchain Development and other Web Technologies."
url                      : "https://infominer.id"
baseurl                  : ''
repository               : "infominer33/infominer33.github.io"
github                   : [metadata]
teaser                   : "/assets/img/info-og.png"
logo                     : "/assets/icons/android-chrome-512x512.png"
masthead_title           : "Research Driven Content"
# breadcrumbs            : false # true, false (default)
words_per_minute         : 200
search                   : true
search_full_content      : false # CHANGE TO true AT YOUR OWN RISK
search_provider          : # lunr (default), algolia, google

# Social Sharing
twitter:
  username               : "infominer33"

# Analytics
analytics:
  provider               : google # false (default), "google", "google-universal", "custom"
  google:
    tracking_id          : UA-132558656-1
    anonymize_ip         : true

# Site Author
author:
  name             : "Infominer"
  avatar           : "https://i.imgur.com/S1UmInX.gif"
  links:
    - label: "Email"
      icon: "fas fa-fw fa-envelope-square"
      url: "mailto:infominer@protonmail.com"
    - label: "Keybase"
      icon: "fab fa-fw fa-keybase"
      url:  "https://keybase.io/infominer"
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/infominer33/"
    - label: "Twitter"
      icon: "fab fa-fw fa-twitter-square"
      url: "https://twitter.com/infominer33"
    - label: "Discord"
      icon: "fab fa-fw fa-discord"
      url: "https://discord.gg/ahTuPMY"
    - label: "Telegram"
      icon: "fab fa-fw fa-telegram"
      url: "https://t.me/InfoMiner33"
   # - label: "Bitcoin"
    #  icon: "fab fa-fw fa-bitcoin"
     # url: 

# Site Footer
footer:
  links:
    - label: "Inf⧉Hub"
      icon: "fa fa-fw fa-cube"
      url: "https://infominer.id"
    - label: "Email"
      icon: "fas fa-fw fa-envelope-square"
      url: "mailto:infominer@protonmail.com"
    - label: "Keybase"
      icon: "fab fa-fw fa-keybase"
      url:  "https://keybase.io/infominer"
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/infominer33/"
    - label: "Twitter"
      icon: "fab fa-fw fa-twitter-square"
      url: "https://twitter.com/infominer33"
    - label: "Discord"
      icon: "fab fa-fw fa-discord"
      url: "https://discord.gg/ahTuPMY"
    - label: "Telegram"
      icon: "fab fa-fw fa-telegram"
      url: "https://t.me/InfoMiner33"
    

# Sass/SCSS
sass:
  sass_dir: _sass
  style: compressed # http://sass-lang.com/documentation/file.SASS_REFERENCE.html#output_style


# Outputting
permalink: /:categories/:title/
paginate: 9 # amount of posts to show
paginate_path: /page:num/
timezone: # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones


# Plugins (previously gems:)
plugins:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jemoji
  - jekyll-include-cache
  - jekyll-optional-front-matter
  - jekyll-readme-index
  - jekyll-redirect-from
  - jekyll-mentions

  
jekyll-mentions:
  base_url: https://twitter.com

# mimic GitHub Pages with --safe
whitelist:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-gist
  - jekyll-feed
  - jemoji
  - jekyll-include-cache
  - jekyll-optional-front-matter
  - jekyll-readme-index
  - jekyll-redirect-from
  - jekyll-mentions


# Defaults
defaults:
  # _posts
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: # true
      share: true
      related: true
      sidebar:
        title: "⧉Info⧉"
        nav: "infonav"
      toc: true
      toc_label   : "Contents"
      toc_icon    : "link"
      toc_sticky  : true
```      


### [Gemfile](https://github.com/infominer33/infominer33.github.io/raw/master/Gemfile)

These Gem settings are necessary to build [infominer.id](https://infominer.id) locally, when testing larger changes.

```yaml
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins


# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-paginate"
  gem "jekyll-sitemap"
  gem "jekyll-gist"
  gem "jekyll-feed"
  gem "jemoji"
  gem "jekyll-include-cache"
  gem "jekyll-target-blank"
  gem "jekyll-optional-front-matter"
  gem "jekyll-readme-index"
  gem "jekyll-redirect-from"
  gem "jekyll-seo-tag"
  gem "jekyll-mentions"
  gem 'jekyll-algolia'
  gem "html-proofer"
end
```

## Content

Posts are the blog posts... straight-forward enough. Pages are individual, and not connected in a feed. Having a blog feed is better for discoverability \ accessibility than using individual pages. 

### Front Matter

I'll use this post as an example, and give a more detailed explanation here, where you are most likely to need one, should you decide to contribute a 'finished' piece of content.

**Every Post or Page must have front matter.** Without front-matter, jekyll won't read it. That's why you might see empty front-matter in some of the source files.

```yaml
---
layout: single # this is the layout I always use, except in special cases.
title:  "Contributors Guide: How I use Minimal Mistakes - 2019"
description: "Contributing to the InfoHub via GitHub Pages, Jekyll and Minimal Mistakes."
excerpt: >
  This guide will introduce you to how some of these sites operate, to encourage participation. You are presented with an overview of how I'm using Minimal Mistakes, and Publishing Content for Free via GitHub Pages.
```

The `excerpt` is what social media uses in the preview, when sharing... and it also is used in the blog feed for preview text.


```yaml
header:
  teaser: https://imgur.com/xeWd7Zz.png
  image: https://infominer.id/assets/img/minimal-mistakes-teaser.png
  caption: "Minimal Mistakes Setup and [Quick-Start](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)."
```

The `teaser` image is used in the blog feed, and for related posts.
`image` is for the header image. `og_image` may be optionally used, if you want a different social media image than your header image.

The only way to have a uniform capitalization guide I could live with is to capitalize all tags, and capitalize categories as would be officially recognized, or simply first letter capital.

```yaml
tags: 
  - INFOHUB
  - CONTRIBUTORS-GUIDE
  - PUBLIC-DOMAIN
  - OPEN-SOURCE
  - SOURCECRYPTO
  - DECENTRALIZED-ID
  - JEKYLL
  - MINIMAL-MISTAKES
  - SETUP
  - GITHUB-PAGES
  - WEB-WORK
authors: 
  - "<a href='https://infominer.id'>Infominer</a>"
  - "<a href='https://www.caballerojuan.com'>JuanSC</a>"
permalink: how-i-use-minmal-mistakes/
categories: [InfoHub, SourceCrypto, Web-Work-Tools, DIDecentral, Learn-Crypto-Trading]
published: true
last_modified_at: 2019-06-25T11:22:33-23:00
---
```

If you edit an existing post, you can add your name in the authors front matter like i've done here.  Permalink is the way I decide which is the official link, and I set canonical once I feel good about the name structure.

### Header Video

```yaml
header:
  video:
    id: 212731897
    provider: google-drive
```

### Defaults

You may recall this section from `_config.yml`

```yaml
# Defaults
defaults:
  # _posts
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: # true
      share: true
      related: true
      sidebar:
        title: "⧉Info⧉"
        nav: "infonav"
      toc: true
      toc_label   : "Contents"
      toc_icon    : "link"
      toc_sticky  : true
```

I'll be honest, I haven't intentionally set up defaults for posts and pages... I've mostly been doing everything manually. Eventually I'll go through and clean all that up so the default settings are default, and there are minimal manual settings in the frontmatter.

Pages work basically the same, except for the naming structure and where they are located.



## Responsive Video

* [minimal-mistakes/docs/helpers/#responsive-video-embed](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#responsive-video-embed)

I primarily use the youtube video helper. 

```liquid
{% raw %}{% include video id="XsxDH4HcOWA" provider="youtube" %}{% endraw %}
```

```liquid
{% raw %}{% include video id="212731897" provider="vimeo" %}{% endraw %}
```

```liquid
{% raw %}{% include video id="1u41lIbMLbV53PvMbyYc9HzvBug5lNWaO" provider="google-drive" %}{% endraw %}
```

You could also introduce a video header, if you have a high quality video.


## Syntax Highlighting


* [jekyllrb.com/docs/liquid/tags/#code-snippet-highlighting](https://jekyllrb.com/docs/liquid/tags/#code-snippet-highlighting)
* [minimal-mistakes/markup-syntax-highlighting/](https://mmistakes.github.io/minimal-mistakes/markup-syntax-highlighting/)
  * [help.github.com / creating-and-highlighting-code-blocks](https://help.github.com/en/articles/creating-and-highlighting-code-blocks)


In this document I'm highlighting code syntax, and for certain code, the codeblock markdown doesn't work unless you indicate the syntax.

![](https://imgur.com/uIw9IqD.png)

### Raw Liquid Code

![](https://imgur.com/46fWL5t.png)

![](https://imgur.com/Gn2RWmN.png)

## [Figure Images](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#figure)

This allows you to create an image that will fill the width of the content column.

```
{% raw %}{% include figure image_path="https://sourcecrypto.pub/images/interlinked.png" alt="sourcecrypto.pub" caption="[SourceCrypto.pub](https://sourcecrypto.pub)" %}{% endraw %}
```

## Utility Classes

[This page](https://mmistakes.github.io/minimal-mistakes/docs/utility-classes/) will show you how to create buttons and notices.
: .notice}

## Feature

This technique can be used to introduce feature rows or individual feature images in any post or layout. In fact, an entire page could be built with just these settings.

You may include these variables:

>* `image_path` - Required - Full path to image eg: /assets/images/filename.jpg. Use absolute URLS for those hosted externally.
>* `image_caption` - Optional - Caption for image, Markdown is supported eg: `“Image from Unsplash”
>* `alt` - Optional - Alternate text for image.
>* `title` - Optional - Content block title.
>* `excerpt` - Optional - Content block excerpt text. Markdown is allowed.
>* `url` - Optional - URL that the button should link to.
>* `btn_label` - Optional - Button text label. 	more_label in UI Text data file.
>* `btn_class` - Optional - Button style. See [utility classes](https://mmistakes.github.io/minimal-mistakes/docs/utility-classes/) for options.


More information: [minimal-mistakes/docs/helpers/#feature-row](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#feature-row)

### [infominer33.github.io/index.html](https://github.com/infominer33/infominer33.github.io/blob/master/index.html)


Frontmatter for feature images:

```yaml
intro:
  - image_path: https://infominer.id/assets/img/infohub-contributors-thumb.png
    alt: "Contributors Guide"
    title: "Contributors Guide: Introduction"
    excerpt: "This contributors introduction is to encourage participation, with minimal barriar to entry. Quickstart for [GitHub](https://github.com/infominer33), [Twitter](https://twitter.com/SourceCrypto), and [Discord](https://discord.gg/29mZwPQ) Contributions."
    url: "/contributors-intro/"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row:
  - image_path: "https://sourcecrypto.pub/bitcoin-history/assets/img/elems10.png"
    alt: "erights.org - CapTP Ops: provideFor() ‘98"
    title: "Bitcoin History - Smart Contracts"
    excerpt: "From Szabo and E Lang - to Ethereum, the DAO, Smart Signatures, and the Cambrian Explosion."
    url: "https://sourcecrypto.pub/bitcoin-history/smart-contracts/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: "https://sourcecrypto.pub/images/thecryptoconomy-podcast_guy-swann.png"
    alt: "Down the @TheCryptoconomy Rabbithole"
    title: "Guy Swan - @TheCryptoconomy Essential Episods"
    excerpt: "Audio for Hundreds of Essential Bitcoin Articles. @TheCryptoconomy - Guy Swan..... These Podcasts are essential. So I made an index of them, organized by topic."
    url: "https://sourcecrypto.pub/blog/thecryptoconomy-podcast-deep-dive/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: "https://web-work.tools/images/github-pages.jpeg"
    alt: "GHPages Starter Pack"
    title: "GitHub Pages Starter Pack"
    excerpt: "Publishing a Website via GitHub pages is free, and easy. Everything you need to get going in one place + extended resources."
    url: "https://web-work.tools/github-pages-starter-pack/"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row2:
  - image_path: "https://web-work.tools/images/pgp-og.png"
    alt: "cypherpunk essentials"
    title: "Using PGP, Escrow, and Cryptocurrency Keysignatures"
    excerpt: "Asymmetric Encryption: Phil Zimmerman, PGP, Bitcoin and Ethereum key-signatures, Escrow, SSL, Various Apps and Resourses."
    url: "https://web-work.tools/practical-public-key-crypto/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: "https://sourcecrypto.pub/rare-digital-art/img/Salvador-Pepe-rare-Pepe-auction-1-13-18.jpeg"
    alt: "Digital Rare"
    title: "Rare Pepe - Bitcoin History"
    excerpt: "Starting in October 2014, users on the /r9k/ (robot9000) board on 4chan began referring to original illustrations and photoshops of Pepe the Frog as 'Rare Pepes'; sharing the 'rare' images of Pepe as if they were trading cards, some of which were posted with watermarks to retain their value."
    url: "https://sourcecrypto.pub/bitcoin-history/rare-pepe/"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: "https://web-work.tools/images/content-creation.png"
    alt: "Resources for Content Creation"
    title: "Resources for Content Creation"
    excerpt: "All kinda tools for images and editing and handy stuff to assist with content creation."
    url: "https://web-work.tools/content-creation/"
    btn_label: "Read More"
btn_class: "btn--primary"
```

### [Home](https://github.com/infominer33/infominer33.github.io/raw/master/_layouts/home.html) Layout

You can see in this markup exactly how my home-page is generated:

```html
---
layout: archive
---

{% raw %}{{ content }}{% endraw %}

<h2>Featured</h2>

{% raw %}{% include feature_row id="intro" type="center" %}{% endraw %}

<h2 class="archive__subtitle">{{ site.data.ui-text[site.locale].recent_posts | default: "Recent Posts" }}</h2>

{% raw %}{% for post in paginator.posts %}{% endraw %}
{% raw %}  {% include archive-single.html %}{% endraw %}
{% raw %}{% endfor %}{% endraw %}

<h2>InfoHub Featured</h2>

{% raw %}{% include feature_row id="feature_row" %}{% endraw %}

{% raw %}{% include feature_row id="feature_row2" %}{% endraw %}

{% raw %}{% include social-share.html %}{% endraw %}
```




## Social Share

I modified this to include the 'Edit this page' button, and some cryptocurrency addresses.


<script src="https://github.com/infominer33/infominer33.github.io/raw/master/_includes/social-share.html"></script>

```html
<section class="page__share">
  <h4>ON GITHUB</h4>
  <p><a href="https://github.com/infominer33/infominer33.github.io/blob/master/{{ page.path }}" class="edit">Edit this page <i class="fa fa-pencil"></i></a></p>
    {% raw %}{% if site.data.ui-text[site.locale].share_on_label %}{% endraw %}
  <h4 class="page__share-title">{{ site.data.ui-text[site.locale].share_on_label | default: "Share on" }}</h4>
    {% raw %}{% endif %}{% endraw %}
  <a href="https://twitter.com/intent/tweet?{% if site.twitter.username %}via={{ site.twitter.username | url_encode }}&{% endif %}text={{ page.title | url_encode }}%20{{ page.url | absolute_url | url_encode }}" class="btn btn--twitter" onclick="window.open(this.href, 'window', 'left=20,top=20,width=500,height=500,toolbar=1,resizable=0'); return false;" title="{{ site.data.ui-text[site.locale].share_on_label | default: 'Share on' }} Twitter"><i class="fab fa-fw fa-twitter" aria-hidden="true"></i><span> Twitter</span></a>
  <a href="https://www.facebook.com/sharer/sharer.php?u={{ page.url | absolute_url | url_encode }}" class="btn btn--facebook" onclick="window.open(this.href, 'window', 'left=20,top=20,width=500,height=500,toolbar=1,resizable=0'); return false;" title="{{ site.data.ui-text[site.locale].share_on_label | default: 'Share on' }} Facebook"><i class="fab fa-fw fa-facebook" aria-hidden="true"></i><span> Facebook</span></a>
  <a href="https://www.linkedin.com/shareArticle?mini=true&url={{ page.url | absolute_url | url_encode }}" class="btn btn--linkedin" onclick="window.open(this.href, 'window', 'left=20,top=20,width=500,height=500,toolbar=1,resizable=0'); return false;" title="{{ site.data.ui-text[site.locale].share_on_label | default: 'Share on' }} LinkedIn"><i class="fab fa-fw fa-linkedin" aria-hidden="true"></i><span> LinkedIn</span></a>
  <a href="https://www.reddit.com/submit?url={{ page.url | relative_url }}&title={{ page.title }}" class="btn btn--reddit" title="{{ site.data.ui-text[site.locale].share_on_label }} Reddit"><i class="fab fa-fw fa-reddit" aria-hidden="true"></i><span> Reddit</span></a>
  <p><img src="https://infominer.id/assets/img/1pLr.gif"/></p>
  <h4>SUPPORT THE CAUSE</h4>
    <p>Feel free to <a href="mailto:infominer@protonmail.com">contact me</a>!</p>
    <p>Especially if you're interested in <a href="https://web-work.tools/services/#iso-clients-who-want-bitcoin-related-content">bitcoin related content</a> and/or research!</p>
    <!-- Beginning of tippin.me Button -->
    <p><div id="tippin-button" data-dest="infominer33"></div>
    <script src="https://tippin.me/buttons/tip.js" type="text/javascript"></script></p>
    <!-- End of tippin.me Button -->
  <table class="table table-bordered table-hover table-condensed">
      <thead>
      <tr>
        <th title="Field #1">Bitcoin</th>
        <th title="Field #2">DOGE</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td>1A1DZfw4VgpHCgnMjnmfDnMjddKf8xdYbd</td>
        <td>DQKkzfJjqnXUD8Z7C3e84vKzvghPe9dXSa</td>
      </tr>
      <tr>
        <td><img src="https://imgur.com/yXLLm9Bl.png" width="150"></td>
        <td><img src="https://imgur.com/z316u0c.png" width="150"></td>
      </tr>
    </tbody>
  </table>  
</section>
```

## Thank You for Stopping By


That's it!

Hope you've found this informative.

Over time, it will become more detailed, and include all the bits I haven't thoroughly explained \ understood.
