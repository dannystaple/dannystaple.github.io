---
created: 2007-07-14 11:55:30
description: Silent Computer Upgrade - Part II
tags: [pc, upgrade, silent, amd, cpu, turion, sempron, ubuntu, linux, bootdisk, gigabyte, motherboard, freedos]
title: Silent Computer Upgrade - Part II
layout: post
---
{% include JB/setup %}

In the [previous article](/2007/06/13/silent_computer_upgrade), I'd left things on a bit of cliffhanger with a motherboard that no longer booted.

After yesterdays disaster, and a day at my day-job worrying slightly about if I had actually managed to flash the motherboard BIOS out of working order, I came home to attempt a very tricky, and potentially risky operation.
  
To recap, I had decided to attempt to fit a Turion 64 ML-30 into the Socket 754 Gigabyte GA-K8NS motherboard.
I had managed to fit it, run the OS, and could not get power now.
By default it was running at 800Mhz. So I decided to grab the latest F19 BIOS from Gigabyte, flashed the board, and it would power down before post (power on self test). 

My suspicion was that the new BIOS update removed the code to recognise the Turion.
I decided to try and revert the BIOS back. My madcap plan (hatched yesterday) was to use the Sempron to boot the board, flash it, then put the Turion back in.

So I used my laptop to download the BIOS, and as before, created a boot CD using freedos to flash the BIOS
After this, I then had to get the Sempron back in.
The problem now was that I had used the same heatsink for the Turion, and slathered it in a lot of heat transfer compound (HTC), which I had currently run out of and so did not want to waste.
I only needed the Sempron to run just long enough to flash the BIOS.
  
The boot CD drive is a USB CDROM, and yesterday, when it would not POST I reset the BIOS via the clear CMOS jumper.
So I would also have to go into the BIOS Setup menu and change the boot options.
So I had to hatch another plan to quickly cool the Sempron without cleaning all the HTC put on the heatsink for the Turion.
My plan was simple - I had an older CPU fan and heatsink to hand which had been used to cool an Athlon XP processor.
It was not quite a big enough heatsink, but it might do for a short term.
So I pushed it on (sandwiching a layer of HTC between the heatsinks copper pad and the Sempron's heat spreader), plugged it in, and started the machine.
  
The great news is it booted, and I managed to get the settings changed, and the F18 BIOS flashed, although I had kept a finger against the heatsink, which began to get pretty warm (not yet hot).
I depowered the box, put the Turion and heatsink back in, and got the warm glow of watching it boot normally.
Disaster averted, although feeling a little miffed that the recognition codes had been removed.

Now since I had reflashed, I decided to hit the "load optimized defaults" option and enable "Top Performance" in the BIOS Settings, which then set all of the CPU frequency control and voltage settings to auto.
Hoping this would give me powernow, I booted the OS.
It all booted, but sadly, still running at 800Mhz with no speed stepping. Out of time to tinker, I will have to find a solution to this tomorrow.
Clearly - the most recent BIOS is not the right solution though...
