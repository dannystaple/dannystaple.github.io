---
created: 2008-06-02 09:09:13
description: Power and data transmission
tags: [power, diy, electronics, computing, computer, pc]
title: Power and data transmission
layout: post
---
{% include JB/setup %}


As I have been looking at wiring up my flat, I have been thinking of ways to conserve power and space - cable space that is. There is nothing I am more interested in right now than ways to banish "wall warts" - the many, many small 12v DC adaptors. Nearly every device has one, my mobile phone, landline phone, the NAS, monitor, printer, microcontroller dev boards/programmers, guitar effects units. The list actually goes on and on.


Even the PC has its switched power supply supplying DC to most of the components. Why am I having to convert to DC over and over?


So I started looking at alternatives. Could one decent switched power supply sort this out?

I am aware of the issues. First - each of those power supplies has different voltage and wattage outputs for device requirements. Devices must not be overloaded, or underpowered .Also, any solution must not load up one mains plug over its own rating. cables for power delivery must be safe and have the correct wire pitch and insulation. It needs to be able to safely deal with surges, and for my requirements work out as a relatively inexpensive product.

The system needs to be in the market presently, or shortly available (in the next 6 months). It should also, preferably link up with the data solution, as a number of devices also have a data line to go with them, although the data requirement is not really essential.

I have come across a few potential ideas for this, some are products on the market, some are things I could homebrew. That is an interesting trade off, as while I like doing homebrew, this is electrical power, and although the voltages are low, a semi-permanent installation like this needs to be bulletproof. Also, it needs to be fairly readily expandable, and an off-the-shelf solution is going to be somewhat easier.

That then throws up one last problem, is that the availability needs to be good. I do not want to invest in a system that will disappear in a couple of years, that was created by one obscure group or company - the system needs to be pretty standard, and the standards well documented. Preferably not too heavily patent encumbered.


Tricky customer aren't I?

# Possible Solutions

## Wiring a 12 volt rail through the house

An old friend lives in a house out in the moors, where he generates his own power through both a diesel generator and a wind turbine. The house came with very old wiring, not really suitable for safe use at 240 volts. He hired an electrician to wire the 240 volts, and converted the old wiring into a 12 volt DC system.

### Pros

* The system was there, readily available. This included wiring, and old style electrical sockets.
* Takes up little space.

## Cons

* My own flat and most others have no such system, and while I would condone new builds to have some such line, it would be very expensive and messy to retrofit.
* Devices that take less than 12 volts will have to have regulators, and devices which take a little more will be a problem.
* The lines will be pretty noisy, and therefore additional smoothing is probably required at device endpoints.
* No data lines.

In conclusion, while it suits him well, it is probably not appropriate for myself.

## Greenplug

Greenplug are a company producing a single power unit to replace many power units. They are also courting consumer electronics manufacturers to try and get them to ship Greenplug cables instead of wall warts.

### Pros
* This is a set of good look devices.
* This has potential if it is supported by the manufacturers.
* Negotiable power - means that devices will be able to request power, no switches or matching.
* Power saving - devices may be able to inform the greenplug when they go into a low power mode or have stopped charging.
* Based on a hybrid USB universal connector.
* Can offer basic USB power for normal USB powered devices.


### Cons
* Not yet available in shops.
* Likely to be expensive.
* Hubs do not have many ports.
* Manufacturer support not yet available.
* Only one company is currently building parts, although there may come a point where it is simply licensed commodity technology.

This is a possible solution, although I would have to wait a while for it to become available.

## PoweredUSB

This is a standard created by a consortium of companies, designed for use in the EPOS (Electronic point of sale) realm for retail groups.

### Pros
* A standard supported by a number of major players, including IBM and MS.
* Offers a power management system like Greenplug.
* Connectors come with clip on parts to make a more secure power connection.
* Offers data and power.

### Cons
* This has crippling patent encumbrance and may be extremely expensive due to this. This includes the power management system.
* Not widely available - most devices are only in EPOS realm.
* Standards for device connection are not agreed upon yet, with different manufacturers using different methods.
* Not really available for consumer level usage.
 
 In conclusion this is not really a player. The expense, encumbrance, the lack of standardisation for end points and distance from consumer devices is a bit of a put off. For now, this is not an option.

## PoE and 802.3af

This first sounded like a bit of a joke, an April fools. But it turns out this is a real and readily available way to send both power and data over a single cable. It is also a standard, implementable by many.

### Pros
* Readily available - I can go to Google and find devices to purchase right now.
* Works with existing Ethernet networks - 10/100.
* Reasonably cheap with low, mid and high end ranges.
* Fully standardised with a few satellite standards.
* Homebrews well documented and circuits available.
* Scales through voltages based on a resistance.
* Done properly is still compatible with non POE devices.
* Been used in the field for a while.
* Uses very common and cheap Ethernet Rj45 plugs, and standard Cat5 cabling.

### Cons
* done very cheaply it is not compatible with non POE devices.
* The voltage selection seems to only be negotiable at start up, and cannot adapt to device requirements like the Greenplug.
* May not be compatible with gigabit Ethernet apart from high end range.
* Ethernet network may not be available (but in my case it is).
* Will probably need splitters at end points for all the devices that do not yet use PoE.
* Ethernet connectors and splitters considered relatively large when compared with Greenplug.
* Not usable directly for USB powered devices.

This is probably the most appealing solution yet. There are even whole thin-client terminals based on PoE.

# Readers Call to action

I am relatively sure that I have only covered a very small portion of the possible ways to do this, and there are more to consider.

So do you know any systems? Could you advise me, or tell me your experiences with these devices? Maybe you are a company with products like this trying to make yourself known - in which case you are free to leave a comment on this article with a link back to your site.

# Links
* [Greenplug - One Plug To Rule Them All](http://greenplug.us/news/item/bmV3czUxMzg3NTE5YTk4M2Q=)
* [Powered USB on Wikipedia](http://en.wikipedia.org/wiki/PoweredUSB)
* [Powered USB site](http://www.poweredusb.org/index.html)
* [Power Over Ethernet on Wikipedia](http://en.wikipedia.org/wiki/802.3af)
