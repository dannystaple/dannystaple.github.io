Part II - The recovery
--------------------------
After yesterdays disaster, and a day at my day-job worrying slightly about if I had actually managed to flash the motherboard BIOS out of working order, I came home to attempt a very tricky, and potentially risky operation.
  
To recap, I had decided to attempt to fit a Turion 64 ML-30 into the Socket 754 Gigabyte GA-K8NS motherboard. I had managed to fit it, run the OS, and could not get powernow. By default it was running at 800Mhz. So I decided to grab the latest F19 BIOS from Gigabyte, flashed the board, and it would power down before post (power on self test). 
  
My suspicion was that the new BIOS update removed the code to recognise the Turion. I decided to try and revert the BIOS back. My madcap plan (hatched yesterday) was to use the Sempron to boot the board, flash it, then put the Turion back in.

So I used my laptop to download the BIOS, and as before, created a boot CD using freedos to flash the BIOS. After this, I then had to get the Sempron back in. The problem now was that I had used the same heatsink for the Turion, and slathered it in a lot of HTC, which I had currently run out of and so did not want to waste. I only needed the Sempron to run just long enough to flash the BIOS. 
  
The boot CD drive is a USB CDROM, and yesterday, when it would not POST I reset the BIOS via the clear CMOS jumper. SO I would also have to go into the BIOS Setup menu and change the boot options. So I had to hatch another plan to quickly cool the Sempron without cleaning all the HTC put on the heatsink for the Turion. My plan was simple - I had an older CPU fan and heatsink to hand which had been used to cool an Athlon XP processor. It was not quite a big enough heatsink, but it might do for a short term. So I pushed it on (sandwiching a layer of HTC between the heatsinks copper pad and the SEmpron's heat spreader), plugged it in, and started the machine.
  
The great news is it booted, and I managed to get the settings changed, and the F18 BIOS flashed, although I had kept a finger against the heatsink, which began to get pretty warm (not yet hot). I depowered the box, put the Turion and heatsink back in, and got the warm glow of watching it boot normally. Disaster averted, although feeling a little miffed that the recognition codes had been removed.

Now since I had reflashed, I decided to hit the "load optimized defaults" option and enable "Top Performance" in the BIOS Settings, which then set all of the CPU frequency control and voltage settings to auto. Hopeing this would give me powernow, I booted the OS. It all booted, but sadly, still running at 800Mhz with no speed stepping. Out of time to tinker, I will have to find a solution to this tomorrow. Clearly - the most recent BIOS is not the right solution though...

--------------------------
Part III - Turion on desktop
--------------------------

I decided to give XP a go as Linux did not seem to offer any powernow/CnQ. 
I installed XP, along with the full complement of up to date hardware drivers including the Motherboard and CPU. I then downloaded and ran the AMD tools to show clocking, voltage and use. No CnR here.

Since CnR/Powernow was not going to step the speed up, I had to manually set it to the right speed. My next thing was to try increase that multiplier successfully to 8. If I leave the voltage on the BIOS setting "Normal", it appears to work fine. Considering that Normal may be seriously undervolting, this is odd. Selecting a CPU voltage of 1.35v (as I expect for the Lancaster core my chip is based on) resulted in CMOS checksum errors on boot. But I now got it running on 8x multiplier - the full 1.6Ghz.

Running speedfan showed some welcome results. It was generally running at about 34, although some more intense stuff peaked it once at 48C. However, as PWMConfig under Linux had shown, speedfan dangled the possibility of automatic fan control and software adjustments, but failed to change the speed of any of the fans when the settings were adjusted. This I have heard before regarding the GA-k8ns (754).

With this all finished - there were some things I would later sort out. Firstly, I am not happy that the base of the standard socket 754 heatsink is making any contact with the core, and the thermal grease was being used more like a complete thermal transmission - it is not designed to behave like that, and under load the processor core may overheat. I therefore ordered a ThermalTake fan designed specifically for this purpose - the Cl-P0312 Mobile Athlon 64 cooler. I ordered this from ThermalTech.co.uk. I will mention its fitting when it arrives.

Also the case power supply was noisy, and so I had a spare quiet supply, so I replaced the massive 600W power supply - with 3 fans with a smaller "COLORSit Silent Technology" 350 watt low noise power supply, with one large fan only. This made a fair gain in noise and  power usage reduction, as well as further lowering the case heat. The one remaining noisy area is the GPU fan. This is a Geforce 6600. I found the ThermalTake Schooner, and ordered the part - a fanless GPU Cooler. More on that later.


