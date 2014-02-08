---
layout: post
description: Transport Your Favourite Apps To Any Windows PC
tags: [usb, software, windows, computer, open source]
title: About Portable Apps
---
{% include JB/setup %}

PortableApps is a neat bit of software that lets you install your favourite apps, along with their configuration and user settings onto a USB device or removable drive. It is free software for windows and I often use it to write and modify stuff on orionrobots.

#How To Put your favourite software on a Portable Drive

Being able to take your browser, music player or other software and its configuration with you when you go to other places with computers will save you time and frustration setting up and personalising.

At home, you probably have your browser (and other programs) set up with bookmarks for the things you like to read, it will have passwords and cookies for your main websites. You possibly have addons and plugins that are to your taste. If you are using Firefox, you may have even got used to closing it with tabs that will open where you left off again later. But when you go to work, you are on a different computer, with either a locked down desktop, or just having to go through the hassle of configuring it again. Perhaps you do not want to leave your favourite bookmarks or passwords on a work machine.

Using this tool, you can take your software with you, wherever you go. Using the right kind of USB drive, you can have it on your keychain, without which you do not leave the house!

How can you do this?

# What Is PortableApps? 
*About the best way to port your favourite free apps*

PortableApps is a platform and suite of tools for Windows which have a way to install software directly onto a memory card or USB pen drive on Windows machines. It includes an installation mechanism, a standard way to port tools to it with both their files and settings, and a launcher menu to run them.

When you download the initial bundle, a selection of common software is installed too, including OpenOffice, Firefox and Thunderbird. Additional software can be downloaded form the portable tools site and be installed too.

When you put a drive with Portable Apps installed into a computer, it will start up and show you a launcher menu with an icon in the system tray (bottom right). The applications are stored along with their settings and documents on the drive, so you can take this anywhere and have all the settings you are comfortable with and continue work. You could go from home to work, home to a library computer, or from a desktop to a laptop. The intention is the applications will always work the same way for you on many computers.

PortableApps requires some kind of memory card to run on. Portable apps will run on any Flash Drive, USB Drive or Memory card. I have run one for a long time on a 512Mb stick so a large memory device is not necessary, however, if you are looking to store media and email on one, then you will need a bigger space and should consider a larger 8 or 16Gb stick. 8Gb is currently the standard although drive size to cost ratios are constantly improving.

# How PortableApps can save you time

PortableApps is a real time saver when you need to use multiple computers.

Install your apps on a USB drive or portable hard drive, and take them anywhere.

Configure an application your way and take the config with you anywhere. This means any add-ons, bookmarks, passwords and accounts go with you.

Use a public computer without leaving a trace of your browsing or email accounts - takes the dodge factor out of internet cafe's

Use your favourite software even in places you cannot normally install stuff.

Take a certain number of documents or offline emails wherever you are, so you do not necessarily have to go on line to see them.

# What applications can I get with it?

There are many applications on PortableApps, and new ones are being added or upgraded relatively regularly.
Among my favourites are the following:

* Mozilla Firefox - The popular web browser - take your bookmarks, browsing history and passwords with you - don't leave them on someone else's machine!
* Mozilla Thunderbird - Capable portable email client - keep, manage and organise your email on the stick instead of leaving it on someone else's servers.
* Pidgin Portable - Take all your contacts and accounts with you, and also bring together all of your different IM accounts - can use MSN, ICQ, YahooIM and other IM logins together in one app.
* Sumatra PDF Reader - This is a fast PDF reader, it starts up much quicker than the leading alternative.
*PortableApps backup - okay this is actually part of the platform, but you would not want to store this much info somewhere without being able to back it up.
*OpenOffice portable - A whole and capable office suite that you can take anywhere, and configure for your needs.
* Putty portable - This is a tool that allows you (with the right setup) to interact with a computer from anywhere securely.

This selection of apps are just some of those you get bundled with the initial download.

# Where do I get PortableApps?

PortableApps can be downloaded at <http://portableapps.com>. It is also totally free.

There are currently three distributions, the small platform only 1mb, the 35Mb light suite, and the 114Mb full featured suite with many additional apps bundled.

PortableApps is distributed under an Open Source license known as the GPL - the Gnu Public License. This allows you to freely copy, share and modify this software.

If you are lucky enough to have the skills and time to contribute, or just want to scratch an itch, fix a bug, then the code is available to do this.

# How portable are they? 

These apps should run on any recent windows machine. Windows XP, 2k and Vista machines will have little or no problems running them. They are portable in terms of being able to store them on a key sized drive and move them about, but unfortunately not in the sense of being cross platform.

The applications are also subject to local security policies in the machines you wish to use them with. They may be usable with Work, School, Library or internet cafe machines, but some locations do not allow external drives or the ability to load applications from them.

# Do you need portable apps?

For some because they are multi-location, a tool like Portable Apps will soon become one of "How did I live without it", but for others this may be totally without use - perhaps they only have one computer, or perhaps they use a laptop to do everything.

Bear in mind this question applies to alternatives like U3 also.

>> jp1978 says:
>> This is one of those things I didn't know I needed until I heard about it. Free as in beer and free as in speech too!

>> Realitychick says:
>> I can't go without them any more.!
>> The first time my computer crashed and I could still get stuff done by switching to another (husband's) computer, I was hooked!


# Portable application security
*How to keep your data to yourself*

Portable Apps does not leave its configuration on the machines you use it with, so in this respect, your passwords, email, browsing history and other things stay on the card.

However, what if the memory device is lost or stolen? What happens to that data?

You should password protect your sensitive data, and the way to do this is through TrueCrypt. TrueCrypt allows you to create an encrypted secure area on a drive, for example a USB drive, and then load things from that drive only if you have a valid password. Without the password, the contents of the drive are unreadable. If you use the traveller disk mode, then you can automatically get the secure area mounted (after a password check) on machines you attach it to.

Some more expensive memory cards come with fingerprint readers or other methods of hardware enforced security - these are superb for securing data.

Whatever you do, using regular backups, and encrypting will mean that loosing the drive is not a nightmare, at least in terms of your data.

Many drives can be attached to your house keys, which should reduce the likelihood of you forgetting the drive in a public space.

# Troubleshooting 
*Sometimes things do not always work out*

One problem seen often is that the drive fails to autostart/autorun when plugged in, meaning the user has to go to My Computer and manually start the device.

* Have you ever used CD burning software or VMWare on Vista? Both may change a registry entry which even on uninstallation they may not change back.

  If you are using Windows Vista, and USB removable drives no longer autoboot, even with the autrorun.inf, then this is likely to be the case. I found the answer on a forum post which has since gone away (the forum no longer exists).

  This involves a registry change - only do this if you understand what the registry does:
Find the following key:

      HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer

  Change the value NoDriveTypeAutoRun to 000000fb hex.

  You will then need to log on again to see the change.
  
* If you are using Windows Vista, you may have changed the autorun control panel settings. Start control panel, search for autoplay and launch this. Ensure that the use autoplay for all media and devices box is ticked. Look for "software and games" and ensure this is set to either the default, or "Install or run program".

* If you have set up a Truecrypt Traveller disk for this, you will need to modify the autorun.inf for truecrypt to ensure the encrypted drive is mounted as a removable device.
  Use an editor to open the autorun.inf file. Look for the line that is similar to:
  
      open=TrueCrypt\TrueCrypt.exe /q background /e /v "data"
      
  And change it to:

      open=TrueCrypt\TrueCrypt.exe /q background /e /m rm /v "data"

  The "/m rm" line ensures the device is mounted as removable media, which can be made to autorun. Save this file, then try out the autorun.

* [More info on getting USB flash drives to autorun in Windows Vista](http://www.samlogic.net/articles/autorun-usb-flash-drive.htm)


# Alternatives
PortableApps is not the only software to offer functionality like this. Other software which achieves a similar function is the U3 Apps Suite, and Mojopac.

Mojopac is interesting, as instead of being a suite of apps built against a platform (PortableApps), it allows any application, and provides a virtual environment for them.
