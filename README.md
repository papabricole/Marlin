# Marlin 3D Printer Firmware for Monoprice Delta Mini

A fork of Marlin firmware (2.5.2) for the Monoprice MP Mini Delta 3d printer.

Since 2020-04-17 the Marlin branch 'bugfix-2.0.x' contains my changes and support the Monoprice Delta Mini, 
also known as 'Malyan M300'.
In order to activate all the necessary Marlin options, some compilation tricks are necessary. That's
why this repository still exist if you want to build your own config. 

[```Latest Release```](https://github.com/papabricole/Marlin/releases/download/2.0.5.3/firmware.zip)

<img alt="Monoprice Mini Delta" height="240" align="right"
 src="https://github.com/papabricole/Marlin/raw/malyan-m300/mpminidelta.png" />

## WARNINGS

You need to replace the 12V 5A power brick by a 12V 10A one. Otherwise the printer will be very instable and randomly crash.

## How to flash

M300 printers require flashing via SD card. Use the SD card that came with the printer if possible. The bootloader is very picky about SD cards.

 - Copy fcupdate.flg and firmware.bin to your SD card
 - Insert the SD card into your printer
 - Power-cycle the printer. The LED quickly flashes white while programming.
 - Remove the SD card and delete the files from the card to prevent an accidental re-flash.

## How to build your own config

This repo use github actions to build the firmware for you.

 1. Fork this repo
 2. On your forked repo, go to the 'Actions' tab and activate your workflows by clicking 'I understand my workflows, go ahead and run them'
 3. Edit Marlin/Configuration.h directly from github and make your changes
 4. Create a pull request
 5. Go back to the 'Actions' tab: a build action has been triggered
 6. When the Build Action is finished, download the 'firmware.zip' artifact
 7. Every time you update your pull request, a new build will be triggered