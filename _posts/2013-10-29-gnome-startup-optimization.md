---
description: Gnome 3 Startup Optimization
tags: [computers, linux, fedora, fc19, gnome, gnome-shell]
title: Getting a Faster Gnome 3 Startup
layout: post
---
{% include JB/setup %}

It can take a while waiting for a Gnome 3 desktop - in my case Fedora 19, to start up, and run some of your favourite apps. We usually have 2 or 3 go to apps that define our working day. Here is how I sped up mine, and kept it secure.

{% excerpt_separator %}
So I've done an update, and it required a restart. I like to let it do the restart, walk away for a cup of tea, and have the machin ready for me to work again when I return - not return, log in, and then find I have to wait again. Impatient sort of fella I know. Otherwise, there is wait for it to start, grind, grind, grind, start my apps, grind, grind grind.. And finally I can work. By which time the air of relaxation from the cuppa is gone, along with the enthusiasm, or complete recall of what I was about to do.

All of this, and I want it kind of secure too. The rough plan is to set the machine up to auto login, and start up my favourite apps, then issue a lock screen too. So the desktop is locked (requiring a password), but with everything running. There is probably an insecure window of opportunity there - but I don't distrust coworkers that much, and for a home machine, my kids aren't yet that quick.

# Method

The key to this is using gnome-session-properties. Being Gnome - it doesn't have a button in the UI (Gnome are in the habit of taking all but the simplest functionality away at the moment - seems to be the UI fad). However, you can start it with a terminal, or Alt-F2 and type "gnome-session-properties". 

In this dialog you'll need to add a few things.

* First - secure it - click add, and set the name to something like "Lock on Start", and the command needs to be `gnome-screensaver-command --lock`. Comment as you wish. Click add.
* Next - add your apps. you may need to use a terminal, or menu editor to find the exact invokations tied to those icons. If firefox is part of your usual setup, `which firefox` on a terminal will give you the right invokation. Add each as a command in this list.
* Close this dialog.

Now start the normal settings - click on your username, then settings, then users. In users - unlock it, and set to auto-login your user. 

So when you start up - it will automatically log you in, then (and in slightly unknown order - but they don't wait around) start your apps and lock the screen. When you come back to your desk - unlock the screen - and your apps are there waiting for you to run them.

# References

* <a href="http://gnomeshell.wordpress.com/2011/08/28/manage-the-startup-applications/">Manage The Startup Applications | The Gnome Shell</a> - So intuitive I had to RTFM to find it - Gnome settings are not quite the GUI experience they once were.
* <a href="http://www.tejasbarot.com/2009/04/16/lock-your-screen-using-command-line/#axzz2j6WjixOg">Lock Your Screen using the command line @ All Linux User's Blog</a> - Quick handy reference there.

<!-- Place this tag where you want the widget to render. -->
<div class="g-post" data-href="https://plus.google.com/110194536319300332772/posts/ByvRcdVhaaQ"></div>
{%- endfilter %}

<!-- Place this tag in your head or just before your close body tag. -->
<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
