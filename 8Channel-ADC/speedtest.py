#!/usr/bin/python
#--------------------------------------   
#
# Raspberry Pi HAT 8 Channel ADC V 1.1 - MCP3208 - SPI
#
# Microchip MCP3208 chip
#
# Author : V. R. Iglesias
# Date   : 04/06/2017
#
# http://www.nationelectronics.com/
#
#
# Type the following to run the script:
#
# sudo python speedtest.py
#
#--------------------------------------

import os
import spidev
import time

# Function to convert digital data to Volts
def Volts(data, places, Vref):
  return round((data * Vref) / float(4096), places)

# Function to read Digital Data from a MCP3208 channel
# Channel 0-7
def ReadADCChannel(channel):
  adc = spi.xfer2([6 + ((channel&4) >> 2),(channel&3) << 6, 0])
  data = ((adc[1] & 15) << 8) + adc[2]
  return data

# Reference Voltage, Jumper selected 5.0 (default), 3.3, 1.0, or 0.3 Volts
Vref = 5.0

# (jumper CE0 on) chip = 0 (default), (jumper CE1 on) chip = 1
chip = 0

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, chip)

# set the maximux speed
spi.max_speed_hz = 200000

#print("Max speed Hz : {}".format(spi.max_speed_hz))

start_time = time.time()

i = 0

num = 500000

while i < num:
  i = i + 1
  c0 = ReadADCChannel(0)

thetime = time.time() - start_time

print ("\n--- %s samples" % (num))

print ("\n--- %s seconds" % (thetime))

print ("\n--- %s ksps\n\n" % ( num / thetime / 1000))

