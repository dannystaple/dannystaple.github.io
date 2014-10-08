---
layout: post
title: Programming Rants - PEP 370
tags: [python, programming, rants]
---
There are things that infurate me when coding - things that aren't quite right. I could be wrong, I'm willing to learn, but this is stuff that annoys me.

# What kind of things annoy me?

When programming - this stuff generally annoys me:

* API's and language features that don't make sense.
* Things that are inconsistent.
* Stuff with missing help/documentation or misleading documentation.
* Things that are platform incompatible without some very good reason.
* Code that is over complicated (modular for heavens sake, then I can look at different parts of its workings).

# Who am I to complain?

I am computer programmer professionally, and have been for over a decade. I've been working professionally with Python solidly for about 5 years, and with other languages and tools since 2000. I studied Applied Computing and AI at uni, and I've been coding since I was 8 with the Commodore 64 and a speccie. I preferred the 64 - superior graphics, but I hated its BASIC variant. As a kid I'd always wanted the beeb BASIC variant, with the 64's sprite system. I loved the Amiga's.

I liked embedding assembly in BASIC and into C, until in about 1998 I released how unmaintainable that makes stuff, and that probably it belongs to driver code and gaming inner loops. Although C will normally do.

I've professionally written console games, database apps, web sites/web apps, Set top box apps. I've unprofessionally programmed phones, microcontrollers (more AVR/Arduino than PIC) on robots, games, web apps and scratched itches with code.

I use (in unequal measure) Linux, Windows, Mac and I've spent time on Solaris, IRIX and VMS (not again thanks).

I do most of my coding in C and Python these days, although I am often playing with other languages for fun or to challenge myself a bit.

I can be quite opinionated.

# Python Site Dirs - Pep 370 - Mar 2013

This PEP, which has been implemented and is in major versions of python, has one major flaw that really winds me up. For no apparent reason, it has OS inconsistencies.

<http://www.python.org/dev/peps/pep-0370/>

## WHY?

The core of the PEP is a directory structure to support site packages, per user, and can also probably be subverted to do so per project or per hudson-build (we have our reasons, and virtual-env would be way overkill).

However, we also work on Windows and Linux. Python has a great feature in that the vast majority of its code works on both. Plenty of the setup steps can be similar, apart from the gaping difference between BASH and DOS (subject for another rant - but DOS is the worst command line ever, even VMS makes it look bad).

So here is the part that bothers me in detail:

> user data directory
>
> Usually the parent directory of the user site directory. It's meant for Python version specific data like config files, docs, images and translations.
>
> Unix (including Mac)~/.local/lib/python2.6
> Windows %APPDATA%/Python/Python26

Note first that the ~/.local/lib and %APPDATA%/Python is different. I could perhaps live with this - obviously ~/.<blah> and %APPDATA%/<blah> represent the normal conventions on both OS's (treating Mac as just Unix variant for now).

This is all fine for now. But it is the inner bit that I don't like at all. The specific python version (we know we have a few on our servers) directory has no reason that I can see to be different. Windows/DOS do not play well with arbitrary dots (well ntfs makes this less legacy but still), and Un*x doesn't really care. So be consistent. Why did it have to have a dot, and different capitalization?

# Why is this a problem?

Like all inconsistencies, it increases the number of special cases needed to deploy a program anywhere. In the interest of keeping code clean, simple and maintainable - special cases should be reduced. Worse still - this is special case code that anyone facing a similar task will write, and write again somewhere else. There is already plenty of annoying special case code here - so perhaps this seemed inexpensive there. So a pointless inconsistency, now set in stone, and perpetuated into python 3.

The Zen of python has the following line in it:

"Special cases aren't special enough to break the rules."

However, this could go two ways - is it that we shouldn't have a special case for each OS? Or is that python should go out of its way to "do as the Romans do", and behave the way other software does on the platforms even if that reduces the portability of python code?
