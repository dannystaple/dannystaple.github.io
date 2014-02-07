---
created: 2007-06-13 11:55:30
description: Silent Computer Upgrade - Part II
tags: [pc, upgrade, silent, amd, cpu, turion, sempron, ubuntu, linux, bootdisk, gigabyte, motherboard, freedos]
title: Silent Computer Upgrade - Part II
layout: post
---
{% include JB/setup %}

 <p>
  In the <a href="silent_computer_upgrade.md">previous article</a>, I talked about some of the research I had done to prepare for this. Some real thought had gone into it before I even started buying the CPU and considering the other tools and parts needed. Any project like this should have a little research done, although as this project demonstrates, you will also sometimes have think up quite a bit on the fly.
 </p>
 <p>
  I first wanted to change the CPU, as I can change the power supply once everything else works. Unfortunately, I do not have any real means of measuring the wattage used by the setup, so I just estimated it. I am sure I could sit down and calculate it, but I had a 350 Watt supply at hand, and didn't want to buy another.
 </p>
 <h1 id="Tools">Tools</h1>
 <p>
  I now had the CPU and needed to make sure I had the other parts present. I had a basic computer toolkit, but most importantly needed these items:
 </p>
 <ul>
  <li>Screwdrivers - at least 1 posi, and also one with a socket fitting for stiff screws</li>
  <li>
   Anti Static Band - This should be clipped to an earthed item, even the computers case may be used as long as it is plugged in, but switched off. This is so you do not fry the computers parts with the natural static field surrounding your body. You may also get away with not using the band, and regularly grounding yourself by touching an earthed metal area.
  </li>
  <li>
   A good, well lit area to work - don't I always recommend this? It really is important, for safety, for being able to work without being obstructed, to work with enough elbow room, and with good lighting so you can really see what you are doing. I really cannot stress enough that this is worth having for any tinkering with robots, lego or computers.
  </li>
  <li>Tissues - there will be some heat transfer compound to wipe away, and I did a bit messy with it.</li>
  <li>
   Mini Vacuum cleaner + cotton wool buds - The inside of a computer, especially around the CPU fan and heatsink will get very dusty very quickly. Make sure you have something to clean it a bit with.
  </li>
  <li>Face Mask - if you are sensitive to dust, I would have one of these and wear it.</li>
 </ul>
 <p>
  <br/>
  Safety Goggles are generally not necessary for simple computer modifications/changes, at least not unless the soldering iron comes out or you go beyond the basics. However, if you are working with heat transfer compound, do not rub your eyes, and make sure you wash your hands well before consuming any food.
 </p>
 <p>
  Generally remember not to consume food or drink around a computer being worked on - coffee spilt on the motherboard would be a pretty nasty mess.
 </p>
 <p>
  These are the tools I started with, but I soon found the need for others. More on that when I get there.
 </p>
 <h1 id="Parts">Parts</h1>
 <p>
  Some basic parts I prepared for this, although this is not exhaustive, as with the tools, more things became required as I progressed.
 </p>
 <ul>
  <li>AMD Turion 64 ML-30 I bought last time</li>
  <li>Heat Transfer Compound</li>
  <li>Single fan quiet 350W Power Supply</li>
  <li>Anti-Static container to store removed Sempron CPU in.</li>
 </ul>
 <p>
 </p>
 <h1 id="Opening_up_the_computer">Opening up the computer</h1>
 <p>
  This is actually very simple, and with my case - a Cooler Master Centurion, it was a matter of undoing one thumbscrew on the top, sliding the top panel off, and then lifting off the side panel. This case is a real joy to work with - it also has turned edges to save cuts and scrapes from sharp corners.
 </p>
 <p>
  Just make sure you put whatever screws in a safe spot where you can find them later.
 </p>
 <h1 id="Removing_the_old_CPU">Removing the old CPU</h1>
 <p>
  The Sempron CPU already in the machine was, as mentioned earlier, getting pretty hot. I was using it with a genuine AMD Cooler and the heat transfer pad already present on it.
 </p>
 <p>
  I unclipped the cooler, and normally a gentle tug should free them of the CPU/Bracket. However, it was stuck fast. The heat transfer compound was very thin, and had also hardened somewhat. The problem with Socket 754 and later CPU's is that the plastic bracket the cooler clips in does not allow access to the CPU free lever.
 </p>
 <p>
  I had a choice of trying to run some software to really abuse the CPU and heat it up (like Prime 95, a suggestion on some websites), or to tug harder. I decided to gently tug harder. It is important here to make sure you are tugging completely vertically - any skew here will mess up the pins on the CPU, which is very bad news if you want to use it again. Luckily it came away safely (which considering I needed it again later was very important).
 </p>
 <p>
  However, the CPU was now securely fastened to that cooler, and currently my plan was to use this cooler again. How could I get the CPU off the cooler? Well the HTC would clearly soften if there was a little heat present. I did not want too intense or focussed heat like a soldering iron. So I needed something more gentle with a large surface area. My choice was a travel iron on a low setting.
 </p>
 <p>
  Since I am now applying heat, before I continued, I now made sure I had my goggles present.
 </p>
 <ul>
  <li>
   Travel Iron - these are much smaller than normal irons, and have a few heat settings. Put it on a lower one - try to stay between 40 and 60 degrees. DO NOT put water in the steam making area. Steam and CPU's do not get along well together.
  </li>
  <li>
   Safety Goggles - When heating (along with other things), there is a hazard of things spattering, and although HTC is not likely to, hot or cold, you really do not want that anywhere near your eyes.
  </li>
  <li>
   Clamp - A gentle clamp, which I padded with some foam normally used to pack motherboards, to hold the cooler in place.
  </li>
 </ul>
 <p>
  <br/>
  I put on the goggles, and clamped the cooler to the desk, then on a side of the cooler, I gently heated it up with the iron in one hand, and slowly slid off the Sempron with the other. I then cleaned the HTC from the heat spreader on the CPU, and put it into an anti-static bag.
 </p>
 <p>
  Since I was going to use the heatsink and fan, I then cleaned it up. I used tissue to wipe away the HTC while it was still soft, and then a mini vacuum with cotton wool buds to wipe away the dust bunnies.
 </p>
 <h1 id="Fitting_the_Turion_and_heatsink">
  Fitting the Turion and heatsink
 </h1>
 <p>
  Now here was an issue that the Silent PC Review article had mentioned. The Turion has not got a heat spreader like the Sempron, and unlike the older open core AMD processors it did not have foam separators. I wanted to be sure that the CPU die would not be damaged by the cooler.
 </p>
 <p>I initially though of pilfering the foam pads from a dormant Duron D600 I had, and use those as spacers. However, since that CPU was still last seen working, I preferred not to butcher it quite yet.</p>
 <p>I then eyed up the cooler that accompanied this Duron, but could not find a good way to mechanically attach it to the motherboard, which is a shame because it was a smaller fan. I also considered using a fan/heatsink combo from a graphics card. These were put aside for what seemed a much simpler option...</p>
 <p>My plan was to construct a paper gasket. This meant getting a pair of scissors, and some recycled paper - I often keep draft prints and similar paper so i can print on the back of it.</p>
 <ul>
  <li>Scissors - any decent scissors will do.</li>
  <li>Paper - Since you wont see it, it really does not matter what is printed on it. Perhaps one of those brochures that come through the door will do.</li>
 </ul>
 <p>
  <br/>
  I measured the CPU package size first, and then measured the inner rectangle needed to clear the die and the small surface mount components around it. I cut about 10 copies of the larger rectangle, and then cut the smaller rectangle from them by folding groups of them in half and cutting into them.
 </p>
 <p>
  I am not sure how many it took, but I put enough to clear the top of the core by a few millimetres, bearing mind that the paper will compress slightly as the pressure from the heatsink clamp comes into play.
 </p>
 <p>
  I then placed the CPU into the socket, put the gasket around the die, and placed the heatsink onto it. It was quite clear that the heatsink was riding too high on the plastic bracket, and so I would need more paper to meet it. This also made me realise I would need a lot of HTC. This is not good.
 </p>
 <h2 id="About_Heat_Transfer_Compound">About Heat Transfer Compound</h2>
 <p>
  HTC, also known as Thermal Grease is used to allow heat conductivity between metal surfaces, often used between a heatsink and a component needing the sink. It is not as good a conductor as the metal, and is generally used to ensure good thermal contact between two surfaces with no air bubbles or contamination.
 </p>
 <p>
  It is often shipped with heatsinks, with many now opting for a pad directly on the base of the heatsink so only a protective sleeve needs to be removed instead of a tube.
 </p>
 <p>
  HTC is not designed to bridge larger gaps, but more for surfaces which would be flush to each other but for the compound, possibly with some mechanical pressure.
 </p>
 <p>
  In this instance, the gap was too much, and although I opted for the HTC - this is not a good solution. I only used it like that for about 3 days.
 </p>
 <p>
  My advice to anyone else trying this is to purchase the ThermalTake heatsink designed for use with a Turion processor like I later did, or to find an aluminium or copper plate of the right thickness and dimensions to fit in the inner rectangle of the gaskets, using a little thermal grease as designed above and below the plate.
 </p>
 <h2 id="Back_to_fitting_the_heatsink">Back to fitting the heatsink</h2>
 <p>
  I literally smothered the die in HTC, and used a scrap of card to spread it into the gasket like butter. I regretted that when I needed to clean it away later.
 </p>
 <p>
  I then put the heatsink in, and felt the HTC being displaced as I wanted, then clipped the heatsink into place.
 </p>
 <h1 id="Powering_Up">Powering Up</h1>
 <p>
  I powered up the board, and the motherboard recognised it straight away. However, going to the motherboard health settings, I noted that the CPU temperature was climbing to 40 + C pretty quickly.
 </p>
 <p>
  I new that the thermal connection in the set up was not great, but I had another suspect - the Silent PC review mentioned that these processors were often overvolted by the motherboards, and sure enough it was. I changed the auto setting to the recommended 1.35v. The temperature began to drop nicely again.
 </p>
 <p>
  I then booted the OS. The first thing I noticed was that the speed is reported at 800Mhz which is half of the CPU's actual potential, and that no stepping seems permitted. Unfortunately the board does not properly support PowerNow on the Turion, so I shut down the OS and used the BIOS to change the multiplier. X8 was not good, although a CPU with an FSB of 200Mhz multiplied by 8 should be 1.6Ghz, the machine would power down after a minute. I then tried a few settings, and x7 with a somewhat increased FSB seemed to give me the correct 1.6Ghz.
 </p>
 <p>
  The problem with the Turion processors, is instead of the Desktop CPU's which use software drivers to clock down when there is little demand from a default state of full speed, the Turions will clock up when power is needed from a default state of a much lower speed.
 </p>
 <p>
  The BIOS did not show any setting to enable Cool N' Quiet or PowerNow technology that can be used to control an AMD CPU's speed with software. I booted Ubuntu, and tried to load the powernow-k8 module but received the message "Device not found". Checking the DMESG log there were a number of messages to the effect of this feature not being supported by my BIOS. Net result - no software controlled CPU stepping.
 </p>
 <p>
  However, the OS was now running fine, and stable. I did feel I was not getting the full potential to save power, but the temperature was very good, at between 32 and 35 degrees C.
 </p>
 <p>
  In an attempt to get BIOS support for this, I went to the Gigabyte (motherboard manufacturer) support site and downloaded the latest flash code. Now - I do not have any floppy drives, so I needed to make a bootable CD.
 </p>
 <h1 id="Making_the_bootable_flash_CD">Making the bootable flash CD</h1>
 <p>I used Ubuntu Linux for this. I unpacked the file downloaded from Gigabyte, and also downloaded a Freedos boot disk image to tailor to my needs. I used a boot disk known as "Ripcord".</p>
 <p>With this boot disk, I was able to mount it as a loopback vfat device, and copy the files from the gigabyte archive into it.</p>
```mkdir /mnt/bootdisk
mount /home/danny/freedos.img /mnt/bootdisk -t msdos -o loop```
 <p>
  <br/>
  You will need to run those commands as root, or by prefixing them with sudo as is the convention in Ubuntu.
 </p>
 <p>The files to copy from the gigabyte archive consisted of an autoexec.bat, a flash utility and the image itself. I then built a bootable CD using the disk image.</p>
 <p>I booted off the CD, flashed the BIOS and rebooted....</p>
 <h1 id="Disaster">Disaster</h1>
 <p>The motherboard would no longer boot. It would go through the graphics cards own boot screen, then immediately power down. No beep codes or error messages, just power down.</p>
 <p>I had a sneaking suspicion that the new update (F19 - with a change log message of "CPU Codes") might no longer support the Turion. It is a good job I kept the Sempron around, as I planned to try booting with that and reverting to an earlier F18 BIOS image the next day. I will tell you about that in the next part...</p>
 <h1 id="Links">Links</h1>
 <ul>
  <li><a href="Silent Computer Upgrade.html">Silent Computer Upgrade - Part I</a></li>
  <li><a href="http://www.silentpcreview.com/article300-page1.html">Silent PC Review - AMD Turion 64 on the Desktop</a></li>
  <li><a href="http://www.gigabyte.com.tw">Gigabyte support and product site</a></li>
  <li><a href="http://www.fdos.org/bootdisks/">FREEDOS Ripcord BootDisk</a></li>
 </ul>

