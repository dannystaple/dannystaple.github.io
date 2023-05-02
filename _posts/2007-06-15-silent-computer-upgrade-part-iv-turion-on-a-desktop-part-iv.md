---
created: 2007-07-15 11:55:30
description: Silent Computer Upgrade - Part 4
tags: [pc, upgrade, silent, amd, cpu, turion, sempron, ubuntu, linux, bootdisk, gigabyte, motherboard, freedos]
title: Silent Computer Upgrade - Part 4
layout: post
---
{% include JB/setup %}

In the last post, In the [previous article](/2007/06/13/silent-computer-upgrade-part-iii-the-recovery), I'd managed to recover the non-booting motherboard and get back to a booting computer, using the Turion CPU.
The AMD Turion 64 ML-30 cpu is intended for a laptop, so uses less electrical power and runs cooler than a desktop CPU, while giving me enough computing power for the work I do on this computer.
This means I could use a smaller fan and a smaller power supply for the computer. This reduces its sound, and its energy usage.

I decided to give Windows XP a go as Linux did not seem to offer any powernow/CnQ. 
I installed XP, along with the full compliment of up to date hardware drivers including the Motherboard and CPU.
I then downloaded and ran the AMD tools to show clocking, voltage and use. No CnR here.

Since CnR/Powernow was not going to step the speed up, I had to manually set it to the right speed.
My next thing was to try increase that multiplier successfully to 8. If I leave the voltage on the BIOS setting "Normal", it appears to work fine.
Considering that Normal may be seriously undervolting, this is odd. Selecting a CPU voltage of 1.35v (as I expect for the Lancaster core my chip is based on) resulted in CMOS checksum errors on boot.
But I now got it running on 8x multiplier - the full 1.6Ghz.

Running speedfan showed some welcome results. It was generally running at about 34, although some more intense stuff peaked it once at 48C.
However, as PWMConfig under Linux had shown, speedfan dangled the possibility of automatic fan control and software adjustments, but failed to change the speed of any of the fans when the settings were adjusted.
This I have heard before regarding the GA-k8ns (754).

With this all finished - there were some things I would later sort out.
Firstly, I am not happy that the base of the standard socket 754 heatsink is making any contact with the core, and the thermal grease was being used more like a complete thermal transmission - it is not designed to behave like that, and under load the processor core may overheat.
I therefore ordered a ThermalTake fan designed specifically for this purpose - the Cl-P0312 Mobile Athlon 64 cooler. I ordered this from ThermalTech.co.uk. I will mention its fitting when it arrives.

Also the case power supply was noisy, and so I had a spare quiet supply. 
I replaced the massive 600W power supply - with 3 fans with a smaller "COLORSit Silent Technology" 350 watt low noise power supply, with one large fan only.
This made a fair gain in noise and power usage reduction, as well as further lowering the case heat.

The one remaining noisy area is the GPU fan. This is a Geforce 6600.
I found the ThermalTake Schooner, and ordered the part - a fanless GPU Cooler. More on that later.
