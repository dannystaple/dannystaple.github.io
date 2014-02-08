---
description: DLink DSM-G600 next steps
tags: [nas, computer, linux, telnet, sed, network, gadgets, dsm-g600, busybox, pc, hackable, sbc, modding, powerpc]
title: DLink DSM-G600 next steps
layout: post
---
{% include JB/setup %}

# Simple fun_plug test

So continuing my work with this box, since it was hackable, I decided the first thing to do was to try a simple test of the fun_plug system mentioned before.

I created a very, very simple script:

    #!/bin/sh
    echo Testing &gt;/mnt/HD_a2/fun_plug_active.log


The script is simple enough. The first line tells the system that this file is to be run as a shell with the interpreter at /bin/sh.

The next line simply puts the text "Testing" into the file */mnt/HD_a2/fun_plug_active.log*.

I uploaded it to the box as /HD_a2/fun_plug using FTP, and then set permissions on that to 777, making the file executable. Rebooting the box should leave a new file on the drive at /mnt/HD_a2/fun_plug_active.log containing the word "Testing".

# Getting a move on

Now I was truly cooking. The modding community around this box had figured out cross compiling to this box, and so created a number of binaries (compiled programs) for it already. The first to get was a telnet client, so I could actually interact with the system without waiting for fun_plug to run on a reboot.

I already have a Linux box as well as Cygwin (a way to run some linux based operations in windows) on a windows box. You still require windows to interact with the web front end on the box, which only works properly in Internet Explorer.

# Understanding Busybox

The recommended (by the community) way to get telnet on this box is to use a busybox binary with additional telnet and sed components. Busybox, which I briefly mentioned in my previous post, is a modular system offering many common Linux commands and utilities in a small binary. It is designed to stay resident, have no (or few) external library dependencies, and be very small. All of the commands then run from this binary. It is perfect for use on embedded devices like this.

Busybox has an interesting way to identify which module is being called. You can run busybox directly, with the required command as a first parameter. However, the recommended way is to use a symbolic link (a file that links to the content of another file) which has the required modules name - this then conveniently means pointing the path at a directory of these symlinks allows them to be run as if they were all individual binary commands. Busybox commands are largely compatible with normal Linux/GNU equivalents, but are understandably lighter, so some less used or inappropriate (very intensive) options will be stripped away.

The box already has a busybox binary of its own, but that is somewhat limited. I grabbed the binary from <http://download.dsmg600.info/busybox-telnetd-1.2.1.tar.bz2>. Following the community guide, I used 7zip to extract it to a folder.

You should now end up with a couple of files - busybox, sed and a readme.txt.

The readme.txt is very handy, it actually contains information on getting telnet running with this set. I copied over the binaries to the root of the disk on the box, and placed the commands mentioned in the readme into the fun_plug script.

## About Telnet

Telnet allows remote access to a box via a command line, it is a simple and lightweight protocol and has been around for many, many years. However, on this box, it requires a few changes to groups, users and security in the configuration.

The box uses a standard Linux configuration, in that it stores users and groups in files in the /etc directory as plain text files. However, these files are stored in a compressed image in the flash, and then expanded to a ramdisk on boot. Therefore, we must use fun_plug to make the changes on boot, before the telnet service is started.

Sed is a tool designed to modify text files. It means "stream editor" where the input text is considered a simple stream of text coming at the processor. It has a fairly esoteric and complex syntax based on regular expressions - and I generally have to regularly refer to a regular expression cheat sheet. Regular expressions are a shorthand way to denote changes to text, operations like search and replace.

Luckily, I did not have to think too much about the sed scripts, as the G600 community had already come up with them. However, I will explain them.

    #!/bin/sh
    if [ ! -e /mnt/HD_a2/ash ]; then
      ln -s /mnt/HD_a2/busybox /mnt/HD_a2/ash
    fi
    if [ ! `grep root /etc/shadow` ]; then
      echo kontroll.`grep admin /etc/shadow` &gt;&gt; /etc/shadow
      /mnt/HD_a2/sed -i -e 's/kontroll.admin/root/' /etc/shadow
    fi
    /mnt/HD_a2/sed -i -e 's/root:.*/root:x:0:0:Linux User,,,:\/:\/mnt\/HD_a2\/ash/' /etc/passwd
    cd /dev &amp;&amp; /mnt/HD_a2/busybox makedevs ptyp c 2 0 0 9
    cd /dev &amp;&amp; /mnt/HD_a2/busybox makedevs ttyp c 3 0 0 9
    /mnt/HD_a2/busybox telnetd &amp;


The first line, as above, expresses that this script should be run by /bin/bash.

The next line checks for the existence of the file /mnt/HD_a2/ash. Ash is another shell interpreter, somewhat more friendly than raw sh. It is what a user will get when the telnet in. If it does not exist (the "!" is a negative test), then "ln -s" is used to create one of the symlinks I discussed above. This symlink to busybox will run the module ash in busybox.

"fi" simply ends an if statement.

The existence of a "root" user in the file /etc/shadow is tested for - grep is a tool to find regular expressions in files, and /etc/shadow is one of the user configuration files under /etc which contains users and encrypted passwords. This negative test leads to the use of echo to append the admin users details to the end of the file again. The word "kontroll." is used as a placeholder, so the next operation which uses Sed to switch kontroll.admin for root gives us a standard root user.

Sed is then used to set up a default shell (the ash shell) so the user can log on. If at this point you want to add another user (beyond root) and allow them to logon, you should create a user from the front interface, and then add an entry to set a shell for them. I added myself, as I do not always want to be root.

Next, a telnet session needs a terminal device to attach itself to. A command makedev (in busybox) is used to create those devices.

Finally, the telnet service is started.

After the box is rebooted, I was able to log in with telnet. This now means I can start to do a lot more to manipulate the box.

My plans included getting an SVN server running on the box, with trac - although apache is too heavy, their may be another way to do that. The community website mentions getting Debian and Gentoo environments running on this box.

# Links

* [New Toy - DLink DSM-G600 NAS Box - First Part of this series]({% post_url 2008-03-16-new-toy-dlink-dsm-g600-nas-box %})
* [DSMG600Wiki Howto use fun_plug](http://dsmg600.info/howto:fun_plug)
* [DSMG600Wiki How-to enable telnet](http://dsmg600.info/howto:telnet)

