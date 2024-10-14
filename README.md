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

pipx runpip cbpi4 install https://github.com/lwagy/cbpi4-MCP23017-Actor.git

or

Clone from github

pipx runpip cbpi4 install ./cbpi4-MCP23017-Actor



