---
created: 2005-04-05 06:35:50
description: Weekend Group Log still to come, and problems with XP
tags: []
title: Weekend Group Log still to come, and problems with XP
---
 <p>
  I am still waiting to log this weeks group. We actually went for doing a good fun robot brawling and racing day, using the
  {{wikilink("Lego+Manas", "Lego Manas", "Remote control Lego robot-like kits")}}
  to build robots and our small arena setup. Photos and full log to come.
 </p>
 <p>
  The reason the photos and the rest are on hold, is I have been having horrible troubles with a new motherboard and processor setup I bought. I invested in an AMD Sempron and a Gigabyte K8NS motherboard. Since fitting it, I was having trouble booting into Windows XP, and on a safe mode boot up, it stopped after loading "mup.sys". After a great deal of searching, it turns out that the next thing to load is a critical XP component - part of the kernel.
 </p>
 <p>
  This was worrying - as it could be hardware problems or conflicts, or it could simply be drivers. As I had recently used the same mobo and processor combination in another machine with no problems, I was worrying that I had missed something or let the processor overheat.
 </p>
 <p>
  There were suggestions to use the repair mode of windows setup - which didn't work, to try and reinstall - which always ended up the same way. After a few days of really playing with it - moving memory cards around, removing all the USB devices, stripping it down to basics, I finally saw a thread on the nForce chipset and this problem which suggested it was the nForce SW
  {{wikilink("IDEHardware", "IDE", "Integrated/Intelligent Drive Electronics")}}
  drivers, which are installed by the motherboard driver disk, but are optional when using the nVidia reference drivers.
 </p>
 <p>
  It turned out that was the culprit, and by not installing it, my system seems to be okay. Now one application I am wary of is Semantic Norton Systemworks - which was the last application installed before the whole thing started. I will be trying it with a little caution tonight.
 </p>
 <p>
  If it all works - I will be definitely blogging the weekends activities fully. Until then I don't have access to the computer with the photos on it.
 </p>
