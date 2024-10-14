cbpi4-DS2482S-800-1wireSensor

https://github.com/lwagy/cbpi4-DS2482S-800-1wireSensor/blob/main/DS2482S-8000%20Sensor.png

CraftBeerPi Sensor Addon

DS2482S-800 board using I2c interface.

Each board can manage 8 one wire temperature probes 3.5 or 5vdc

I2c allows up to 2 boards.

cbpi Parameters:

Sensor - i.e. 28-035205432f

Interval - Refresh seconds (default 4)

Offset - offset to temperature reading

Ignore Below - Ignore any temperature above  this value. i.e. -30

Ignore Above - Ignore any temperature below  this value. i.e. 120

cbpi Instalation:

pipx runpip cbpi4 install https://github.com/lwagy/cbpi4-DS2482S-800-1wireSensor.git

or

Clone from github

pipx runpip cbpi4 install ./cbpi4-DS2482S-800-1wireSensor



OFS Shell Install:

https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi

sudo apt-get update

sudo apt-get install owfs ow-shell

Edit owfs.conf to enable the I2C 1 Wire interface

sudo nano /etc/owfs.conf

Comment out the following line

# server: FAKE = DS18S20,DS2405

Find the following section

# USB device: DS9490

#server: usb = all

Insert the line below to enable i2c support. 

server: device = /dev/i2c-1

Find the section titled

######################### OWFS ##########################

Remove the hashes from the lines

mountpoint = /mnt/1wire

allow_other

Save your changes and exit the nano editor.

Create a folder where the 1 Wire devices will be mounted.

sudo mkdir /mnt/1wire

Reboot your Raspberry Pi

sudo reboot

Enable the owserver service

sudo systemctl enable owserver.service

