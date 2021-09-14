---
created: 2013-10-30 05:08:00
description: Using Twitter for blog comments
tags: [computers, internet, twitter, blogs]
title: Using Twitter for blog comments
---
{% filter markdown -%}

{% mark excerpt -%}
I am not the first person to consider using twitter for blog comments. I had the idea, searched for others that have tried it, considered the Pro's, Con's and the viability. I found it not viable for now - but some documentation will perhaps aid others thinking about it too. Read more to find out what I did.
{%- endmark %}

<h1>Idea</h1>

Instead of the usual blog comments area, embed a twitter timeline, using a hash of a blog title or something unique enough to be a hashtag to find blog followups. Have a canned template for responses - with my twitter @dannystaple name, and the hash. This way new comment could be added, responses can be made using the twitter system.

<h2>Pro's of idea</h2>
Comments are all identified by twitter users. Those that spam can be marked so.
Twitter do a reasonable amount of spam filtering and moderation.
The comments going through twitter give exposure of the discussion to followers of the people commenting.
I'd not have to keep my own user database and deal with spam registrations.
I'd not have to consider the style - can use the timeline defaults.

<h2>Con's of idea</h2>
Not everybody likes twitter - only those with accounts would comment.
Twitter does some moderation - but I'd not be able to do any more moderation on profane or spammy comments other than report to twitter.

<h1>Viability study plans</h1>
*   Generating the hash
*   making a plugin for hyde
*   Embedding a searchable twitter timeline - where it failed
*   Canned tweet templates

<h1>What happened in the viability study</h1>


<h1>Alternatives</h1>
* Discus
* Embed a single tweet - with intents
* Facebook
* G+ - which I settled on - write article, publish first, make a G+ post linking to it, embed the G+ post, republish. I can later automate it?
<h1>Reference</h1>
  * Twitter docs - embedding the timeline - https://dev.twitter.com/docs/embedded-timelines
  * https://dev.twitter.com/docs/intents#tweet-intent
  * Other blogs on the idea 
  * <a href="http://whowritesforyou.com/2011/10/11/use-twitter-for-post-comments-the-pros-and-cons/">Use Twitter For Post Comments? The Pros And Cons — First Today, Then Tomorrow</a>
  * 

{%- endfilter %}
