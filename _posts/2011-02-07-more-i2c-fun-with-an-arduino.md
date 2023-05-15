---
date: 2011-02-07
layout: post
title: More i2c fun with an Arduino
tags: [london hackspace, i2c bus, arduino, mindstorms, lego nxt]
todo:
  - should this be on orionrobots?
---
- Mood: Happy
- Music: Infinity, by Sine
- Location: London, Uk

Yesterday, I attended a party at the hackspace. While there, I saw some great stuff:
- A guy using magnifier lenses and CD cases to split a laser beam
- Makerbots - a working cupcake 3d printer
- Nixie tube clocks
- Insane rubiks cubes - including a 7 sided one
- A 12W laser tube (wasn't fired up)

Myself, I was trying to link up an arduino with a Lego Mindstorms NXT Ultrasonic sensor.
This distance sensor has a protocol that is i2c, but is bitbanged by its own controller and may be a tad flakey.
I first had to find a way to connect it - I hacked through one of the rj12 cables, and with the help of another hacker (thanks Lester!), soldered a 6 pin header to it.
I then used a multimeter to determine which cable was which - my method was to search for the two pins marked as ground - which I found, and used to get what I think was the right orientation.

There is a VCC pin, and a VCC 5V pin - so far I connected both to 5v, although I may probe the NXT to see what it is actually doing on this pin.
There are 2 data pins - which the NXT hardware guide has as being Data and Clock - this is in the main hardware guide PDF.

I linked these up with the Arduino - using Analog pins 4 and 5 for the I2C pins as specified in the wired library, and connected across the ground and 5v pins.

The code was simply to send the address of the device (1 in 7 bit according to the lego guide), followed by byte 0 which should request the version.
Unfortunately at this point I was receiving a NACK for the address.

I swapped data and clock - and got the same.

I then wrote a program to sweep the 7 bit address range on the i2c bus, and saw nothing respond. Not good.
I spent a long time mucking with that and reverting to doing it with a known good i2c memory chip, still didn't see a good result.

It was only when getting home, and trying this with another arduino did I get something out of the memory chip -
so I may have done something to the first arduino - it's analog input pins still function as such - perhaps they no longer work as digital outputs...

I'll come around and try this sonar device again - but I may start with the somewhat more resilient I2c->usb converter first before doing in the pins of another arduino with it.
Still pretty happy - it is all learning, getting to know quirks of devices that may be i2c compatible, and enjoyed just being in the space.
