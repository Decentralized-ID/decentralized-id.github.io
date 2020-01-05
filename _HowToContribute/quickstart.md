---
title: "Contributors Quickstart (A Gentle Introduction to GitHub)"
excerpt: "Learn how to revise/add content to a page, or submit your first blog-post via web-browser."
tags: ["Quickstart","Tools", "GitHub Pages", "Minimal Mistakes"]
author: Infominer
author_profile: false
toc_sticky: true
date: 2019-07-13
last_modified_at: 2019-07-14T11:22:33-23:00
---

So far, we've covered quite a lot of ground in our contributors guides!

* [Welcome DIDecentral](https://didecentral.com/welcome/) - A high level overview of the projects we're working on.
* [Intro](https://didecentral.com/contributors-guide/intro/) - The easiest ways to participate with DIDecentral.
* [Quickstart](https://didecentral.com/contributors-guide/quickstart/) 
  * [Infobot Hello](https://didecentral.com/test/infobot-hello/) - Teplate for your first community blogpost.
* [Site Setup and Configuration](https://didecentral.com/contributors-guide/site-config/) - 'Everything' about how this site is configured. 
* [Social Curation Archive](https://didecentral.com/contributors-guide/discord-archive-howto/) - How to export discord history and integrate with Minimal Mistakes Jekyll.

What is needed is a quickstart guide, so that you don't have to read all of that to revise \ add a few links to a page, or even submit your first blog-post.


All that's required to follow this guide is a web-browser and a GitHub account. If you don't already have one, go ahead and [sign up](https://github.com/join) so you can follow along. 
{: .notice--primary}


If you've been following along with these posts from the beginning, you'll want to go back and review, since I forgot to wrap any liquid templating that I was showing in codesnippets with "raw tags" (see source for details). As a result, a significant portion of the value was lost to any early readers.
{: .notice--warning}


## Edit This Page

Feel free to submit test pull-requests while following along or exploring on GitHub.

![](https://imgur.com/txuSpMs.png)

Besides using social media, such as [twitter](https://didecentral.com/contributors-intro/#twitter--mention-and-hash-tags) or [discord](https://didecentral.com/contributors-intro/#contributing-via-discord), the simplest way to contribute to these web-sites is by clicking "Edit this page", which should be found at the bottom of every page run by DIDecentral.

If everything is properly set up on our side of things, you will find yourself transported from our website to that pages source file on GitHub.

<img src="https://didecentral.com/assets/images/edit-this-page.png" alt="Pencil Edit Button on GitHub Source File">

If you click the little pencil icon (red circle in above image), you will find a basic text editor and the pages source. If you don't have commit access to the repository, a patch copy of that file will be created in your github account where you can edit, and propose changes.

![](https://imgur.com/2UEOj9V.png)


## Front Matter

This is where configuration on the page level happens.   

```markdown
{% raw %}
---
title: "Welcome to DIDecentral Community Site and Social Archive"
description: "DIDecentral is a collaborative curation initiative aiming to create quality educational content related to Decentralized Identity: Principles, Specs, Code and Initiatives."

# the excerpt is what supplies preview text on the post-index.

excerpt: > 
  A high-level overview of our organization, its projects, and their general state of development.
header:
  image: /assets/images/didecentral-community-header.png
  teaser: /assets/images/didecentral-community-teaser.png
  caption: ""
tags: 
  - "Decentralized Identity"
  - "Web of Trust"
  - "Self Sovereign Identity"
  - Archive
  - How-To
categories: ["DIDecentral", "Welcome"]
author: Infominer  

#If you are making some revisions to existing content you can use the following example that will add a contributors section at the bottom of the page near tags and categories (be sure to uncomment and edit those lines to fit the situation of whatever page you are on).
authors: 
  - #"<a href='https://infominer.id'>Infominer</a>"
  - #"<a href='https://www.caballerojuan.com'>JuanSC</a>"

#If you want to change a permalink, you must add the current permalink to the `redirect_from` list,  or create one if it does not already exist.
permalink: welcome/
redirect_from:
  - welcome-didecentral/
  - welcome
  - welcome-didecentral
toc_sticky: true
published: true
last_modified_at: 2019-07-10T11:22:33-23:00
#Be sure to change the modified date. I create my own custom made-up time, with the actual date. You can simply ignore the time, and update the date, or use whatever you'd like for the time. Later, the most recently modified content will be featured.
---
{% endraw %}
```

In yaml documents, and the yaml front-matter of posts, the #hashtag is used for comments. Hopefully with the commented front-matter above, it's reasonably clear how the configuration of a page works. There are other page settings, but this covers all the essentials.


## Saving your changes

Once you've completed any edits, whether you've added a link or corrected a spelling error, leave a simple comment explaining what type of change you're proposing.

![](https://imgur.com/2s6Kspq.png)

Once you've submitted a change, GitHub compares the original with your proposed changes and asks if you'd like to create a pull-request.

![](https://imgur.com/rWSn2nr.png)

Assuming you're happy with the changes (in green at the bottom) go ahead and create a pull-request.

![](https://imgur.com/1ak7bhi.png)

Leave a comment explaining your changes. There is plenty of room to be as descriptive as you want in the pull-request comments, compared to the commit comment which is typically short.

## Checking on your Pull-Request

You should get an e-mail notifying you of any updates related to your pull-request. However, you can always see updates related to your open issues and pull-requests by clicking the GitHub logo at the top of any page on GitHub.

![](https://imgur.com/qAEcp7w.png)


That feed also includes notifications for any individuals you follow or repositories you watch.

![](https://imgur.com/EQQdzri.png)

Since the account I used to create this guide doesn't follow anyone or have any activity, here's an example of an active feed:

![](https://imgur.com/PBhPqtH.png)

If you don't have time to get into GitHub, don't feel obliged to read any further. Above should be plenty to begin making simple contributions, as you browse, without getting too technical.
{: .notice--primary}

## Fork didecentral.github.io

One advantage of forking the repository is that you can make as many changes as you like, and take as long as you want in your local repository. Then submit a pull-request when you're satisfied.

![](/assets/images/fork-repository.png)

Now you'll have a copy of the repository in your account.

![](https://imgur.com/8lNavU8.png)

## Write a Blog Post

Since you have full permissions to this repository, you can upload files or create them right in your browser!

This site is for the community. Anyone is welcome to sumbit a post. This should be a low-stakes environment where anyone could learn to use GitHub and GitHub Pages for the first time. 

Even if you just want to write about what brings you to DIDecentral, share what project you are working on. If you aren't currently working on anything identity related, that's fine, share what you'd like, use your imagination.

The idea is to be as welcoming as possible, and encourage people to try it out. Editing text files on GitHub is a gateway to digital transformation. 

You don't have to be very technical to get started. If you start with the simple things, after a while, you'll find that you're getting to know the lay of the land. It's possible to build from there to learn any number of technical skills, as @infominer33 has been discovering.

## authors.yml

If you're submitting a new post, or planning to make any contributions, why not add yourself to the [authors.yml](https://github.com/didecentral/community-website/edit/master/_data/authors.yml)? 

This way an "author profile" will be shown next to your posts. Later, we can modify the author profile template to include info about all of your contributions to the site, and eventually each author will have their own page made with user-generated Jekyll data.

![](https://imgur.com/9tXkp0t.png)


```yaml

Infobot:
  name        : "Info-bot"
  bio         : "Digital Helper"
  avatar      : "https://imgur.com/LPDefso.png"
  links:
    - label: "Email"
      icon: "fas fa-fw fa-envelope-square"
      url: "mailto:infominer@protonmail.com"
    - label: "Website"
      icon: "fas fa-fw fa-link"
      url: "https://infominer.id"
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/info-bot/"
    - label: "Twitter"
      icon: "fab fa-fw fa-twitter-square"
      url: "https://twitter.com/infominer33"
    - label: "Discord"
      icon: "fab fa-fw fa-discord"
      url: "https://discord.gg/29mZwPQ"
    - label: "Telegram"
      icon: "fab fa-fw fa-telegram"
      url: "https://t.me/InfoMiner33"

```

Simply copy-paste this example, removing any social networks you don't use, and if you don't see your preferred social networks listed, go to [fontawesome.com](https://fontawesome.com/icons/telegram?style=brands) to see how your favorite social site is labeled (mostly you can just use it's name and copy the format shown above).

Save your addition to `authors.yml`, and we'll cover pull-requests after submitting our post.

## Create New File

Now that you've added your info into the author data file, you are ready to create your first blog-post with DIDecentral.

![](https://imgur.com/lIn4hRm.png)


Click "Create new file" where the hand pointer is in the illustration, above the file listing, below the "watch" icon.

Name your post starting with the date, and then the title, with `-` dashes instead of spaces.

`YEAR-MONTH-DAY-title.md`


```html
{% raw %}

---
title:  "Hi I'm info-bot!"
author: Infobot
permalink: test/
---


**Hello world**, this is my first Jekyll blog post.

I hope you like it!

I'm an account that @infominer33 uses for experimenting with various features.

This post was written during the creation of our [Contributors Quickstart](/contributors-quickstart/) guide.

{% endraw %}

```

![](https://imgur.com/EMiBZzQ.png)

For now we'll just commit to the master branch, and submit a pull-request. However, in the future, we'll detail how to create (and merge back in) a new working branch, to leave the master branch in sync with its source while you work (especially helpful for bigger changes that might take a while). 

## Submit a Pull Request

Now that we've saved the file in our personal copy of the repository, lets create a pull-request and get it published. 

**Click the "Pull-Requests" tab on the upper left below your repository name:**

![](https://imgur.com/xlLx8s1.png)

**Then click the "New Pull Request" Button**

![](https://imgur.com/qWHet5w.png)

Any time you are creating a pull-request, remember, the `base repository` is wherever you're trying to send the suggested changes, and the `head repository` is wherever you've made the changes.

[![](https://imgur.com/PqpNCuRl.png)](https://imgur.com/PqpNCuR.png)

Once you're sure that you've included only changes you intended, and that you are making changes where you meant to, go ahead and "Create pull-request"

![](https://imgur.com/hZSoJVM.png)

Enter some comment and click "Create a pull-request" on this page: 

![](https://imgur.com/FMAUa8L.png)

Now the project collaborators will recieve a notice that a pull-request has been submitted, and within a day or so (hopefully sooner) you're pull-request will have been accepted, or at least commented on.

Should it take longer than you'd expect, visit [DIDecentral Discord Chat](https://discord.gg/eYm2XvZ) and check to see if anyone has seen your pull-request.

## Changes After Request is Submitted

After you submit a pull-request, you can continue to change the branch or repository where your pull-request originated, and any additional updates will be included in the request.
{ .notice}

Head over to [didecentral/community-website/pulls](https://github.com/didecentral/community-website/pulls) and you can see the active pull-requests.

Whether you were working from a personal copy of the site, or a patch automatically created by GitHub after clicking the "edit this page" button, you can get there from this page:

![](https://imgur.com/nCA1zfl.png)

Clicking [info-bot:patch-2](https://github.com/info-bot/didecentral.github.io/tree/patch-2) leads me to the patch that was created and I can edit to my hearts content, here, if I'd like those edits to be included in the same pull-request.

## Site Structure:

```
/_application
/_blockchain
/_multi-media
/_organizations
/_private-sector
/_public-sector
/_tech
/_resources # This line and above are "categories" as explained in discord archive post
/_data      # Data files including authors.yml, and navigation.yml
/assets     # images javascript and css live here.
/bookmark-donations  # Upload your bookmarks export file here.
/example-site  # Find example posts here.
/_includes  # Partials used to inject modularized html blocks into pages
/_layouts   # These are large partials defining the layout of different page types
/_pages     # These don't require a dated filename, or get added to the blog feed.
/_posts     # This is where you'll be submitting a blog post
/_sass
/_site       # This is the latest local build of the site, not the live version.
/_config.yml # Site Configuration
/Gemfile     # Local Site Configuration
/CNAME       # Site url
/index.html  
/favicon.ico
/README.md
```

## That's all for now

**Let us know in the comments if you have any questions!**

### More Info

* [jekyllrb.com/docs/posts](https://jekyllrb.com/docs/posts/)
* [What is the JAMstack?](https://jamstack.org/)
  >You may have already seen or worked on a JAMstack site! They do not have to include all attributes of JavaScript, APIs, and Markup. They might be built using by hand, or with Jekyll, Hugo, Nuxt, Next, Gatsby, or another static site generator... 