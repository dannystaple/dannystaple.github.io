---
created: 2003-03-17 05:08:00
description: Replacing a Power Supply For an Older Compaq TFT Monitor
tags: [computers, electronics]
title: Replacing a Power Supply For an Older Compaq TFT Monitor
layout: post
---
{% include JB/setup %}

![compaq TFT monitor]({{ site.baseurl }}/images/compaq_tft_monitor.jpg)
Some time ago I bought a second user Compaq TFT monitor. I had to spend a little time getting a power supply to get it running. These power supplies are notoriously difficult and expensive to get hold of, so I rigged my own.

These compaq flat screen monitors (not CRT technology) are now getting quite long in the tooth, but were great because they came in rack mount versions too. They would only really be found now on eBay - I would not really advise buying a Compaq TFT, but if you already have one, or have been given one, then this page contains advice on getting one working - specifically power supplies which can be hard to find for this model.

The monitor I used was a TFT5000, but this applies to a number of monitors made around 2003.

# Buying or Finding A Replacement Power Supply for a Compaq TFT 5000

Buying a power supply for these monitors turned out to be quite difficult, and will have become more difficult as the monitors have gotten older. As there are many newer, cheaper monitors, then it could be cheaper to buy another monitor, or at a push hack a power supply for it as I did below.

To order the supply, you will need the following compaq part number: 170427-001.
This is known as the "dual voltage power supply", and is a model that will work in the US and UK without an extra adapter.

Other markings on the dead supply that came with mine were the following: 634p - The power supply series, Australia Approval Number N15701, 5T23 E134642 listed, Level 3 LR58948 certified, 972455-00, LTE Product, S20162, S9754565, 91-56705 and Potrans Electrical Corp - the Taiwanese power supply specialist who manufactured the supply for Compaq. These are included to help other people looking for info find this information.

I am not affiliated or receiving any commission from the following suppliers -these details supplied to help a reader only. I am also not able to source any replacement supplies myself.
The original article had a number of suppliers, but most have since either disappeared off the internet or will no longer supply these parts.

Suppliers that may be able to help:

* <a href="http://www.trademoon.com">Trademoon Product Catalogue - Compaq Supply</a>
* <a href="http://www.powersourceonline.com/buy/170427--001-b-en.jsa">Buy & sell new, used and refurbished 170427-001 on PowerSourceOnline.com</a>

# Understanding the Compaq Power Connection

<img src="{{ site.baseurl }}/images/compaq_power_connection.png" />

The Compaq models - like the TFT 5000 (and 450) monitor are pretty expensive, and are hard to get service of parts for after HP acquiring compaq. Mine came without a power adaptor - which used a custom connector type - which was an expensive and rare part to replace.

Other monitors with missing power supplies are generally much simpler - and are often just a single cigar style power connector at 12v with a relatively high current. But this one is more specialist - the connector is the same as used for a PS2 mouse or keyboard - a 6 pin round connector.

(insert here)



My initial findings were that it has one 12v, 2amp and a 5v/2.5a supply, I know which pins are the common. But it was pretty awkward to find out which of the other pins were which. The image beside this is a pin connection specification for the DC outputs of the AC power supply based on the info I found. The power supply is listed also as the dual voltage adaptor, it is suitable for the socket/plug for a Compaq TFT 5000, and possibly other models like the TFT450, LCD Monitor.

# Using A PC Power Supply
<img src="{{ site.baseurl }}/images/pc_drive_power_pins.gif" />

One good source of a 5v and 12v power rails with good stable current supplies are PC ATX power Supplies - these are fairly easily available, both new and old. Only two steps are required to convert one of these into a power supply usable on the Compaq Monitors.

First a connector needs to be correctly wired to it, and then second the power supply needs an on switch.

The diagram accompanying this section shows the wiring for one of the drive connectors from a PC power supply. Conveniently - it has a 12v rail, a 5v rail and dual ground rails. For detailed information on this connector type, take a look at <a href="http://www.pcguide.com/ref/power/sup/partsDrive-c.html">Drive Power Connectors</a>.


This can be done relatively safely, as it does not require opening the power supply. If you can find a standard drive socket, and wire this to a chopped off PS2 mouse or keyboard connector with the right connections, this is a relatively easy build. Be sure to test each connection made with a multimeter to ensure it is wired correctly and goes all the way through before connecting it to any AC outlet or the monitor.

The ATX power supply is powered on usually by a PC motherboard, but can be powered on without one. The ATX connector, the large square plug that goes into the motherboard, can be used to power this on by connecting Pin 14 to a ground pin - a diagram of this will be added. A simple pushbutton will do this.

# Reference Sites and Additional Info

The following sites have additional info I have found on this monitor.

* <a href="http://www.ciao.co.uk/Productinformation/Compaq_TFT_5000s__17460">TFT5000 Product description and specification</a>

## Note
This post has appeared before on the Orionrobots website and on squidoo - it has been removed from both and will be kept here.
