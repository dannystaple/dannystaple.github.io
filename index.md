---
layout: page
title: Danny Staple
tagline: About Me
---
{% include JB/setup %}
I am proudly a Computer Geek - running the company [ODM Solutions Ltd](http://odmsolutions.co.uk) where I specialise in  automation and developer tools. I like Python and Linux, but use whatever is needed.

I am shamelessly into robots, and run a robotics website at [Orion Robots](http://orionrobots.co.uk). I tinker with the Arduino, electronics, Raspberry Pi and any other gadgety electronic things I can get my hands on - I was the kind of kid that took everything apart.

I am a father of two great kids.

I love SciFi, and some Fantasy as films, plays and books- I read a lot.

I play computer games, build stuff with Lego, grow plants occasionally and muse about all things.

I am a bit of a foodie - although I'd like to be a lighter one!

I have some interest in ethics, philosophy and politics - but try not to get too hung up about them as most people have already made up their minds and cannot change. My closest political description is I am passionate skeptic - I like things that are evidence based, and generally let people be. Believe what you want - just don't make it my problem.

This site collects together musings I've written on other sites, and will collect those I write that are related to neither robots or computer programming.

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

[Gardening](/gardening.html)
