---
description: New Toy - DLink DSM-G600 NAS Box
tags: [nas, dsm-g600, dlink, linux, powerpc, hacking, hackable, sbc, modding, uclibc,
  busybox, gadgets]
title: New Toy - DLink DSM-G600 NAS Box
layout: post
---
{% include JB/setup %}

I recently bought the DSM-G600 on Amazon, a small and inexpensive Wireless Enabled NAS - Network Attached Storage. It is a tiny box - about the size of router, maybe a little taller. It has a wireless aerial at the back, a set of lights on the front, an Ethernet port, power socket and a cavity for an IDE hard drive inside it. The box also has one USB2 port which can play as a USB2 host. That already gave me ideas - I know it can support USB2 drives, but how about a DVD Burner for backups directly from the NAS, or connecting my printer to it? Well early days yet...

This is where it starts to get fun. I bought a 250Gb hard drive for the cavity and let the drive start up and initialise the drive. Immediately it grabs an IP address via DHCP my local network and starts whirring away. The manual gives details on finding an initialising it for my network so I can give it a permanent address.

Initially the box shares the drive as a windows share, and has a web interface to edit the settings, although this interface has a couple or quirks that mean it only works in Internet Explorer. The interface allows me to set up users and access restrictions, enable FTP access and other small operations as well as monitoring the health and temperature of the drive.

# Hackable

However, I bought this device for more than just storing files. This box has a hacking community around it, and under the hood it is simply a Linux kernel running the busybox set of tools built with uclibc on flash storage. The drive is actually partitioned into one great big Ext2 Linux partition. Don't worry if that does not yet mean a lot to you - what it simply means is that this box is hackable, and could possibly be used for an SBC - Single Board Computer.

The hardware consists of a 170Mhz PowerPC based processor, 32MB of RAM and 4MB of Flash ROM. This may sound limited, but it is a tiny cheap box, and now probably has a huge hard drive attached to it! It may be perfect for a tiny home server sitting in the corner.

The drive as its shared can have a single file placed on it named "fun_plug". This harmless seeming name allows you to do something quite interesting - it is a shell script, running in a busybox equivalent of a Bourne Unix shell. You can run commands from this script. It runs every time the box is restarted. The next step is to get some of my own tools on the box so I can run those.

I have had it long enough to have done plenty with the box, and will be blogging my hacks so far with it here. I will give you the links to start you off though..

# Links

* [DSMG600 Wiki](http://dsmg600.info/start) - This is the home of the hacker community, including a wiki, and a forum to discuss it.
* [Howto use fun_plug](http://dsmg600.info/howto:fun_plug)

