#!/usr/bin/python
#--------------------------------------   
#
# Raspberry Pi HAT 8 Channel ADC V 1.1 - MCP3208 - SPI
#
# Microchip MCP3208 chip
#
# Author : V. R. Iglesias
# Date   : 30/10/2016
#
# http://www.nationelectronics.com/
#
#
# Type the following to run the script:
#
# sudo python adcdemo.py
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

# The linux-raspberrypi kernel update to 4.9.43 changes the SPI default 
# max speed from 100KHz to 125MHz. You had to set the max speed manualy.

# Setting the max speed
spi.max_speed_hz = 200000

while True:

  c0 = ReadADCChannel(0)
  c1 = ReadADCChannel(1)
  c2 = ReadADCChannel(2)
  c3 = ReadADCChannel(3)
  c4 = ReadADCChannel(4)
  c5 = ReadADCChannel(5)
  c6 = ReadADCChannel(6)
  c7 = ReadADCChannel(7)

  # results
  print "--------------------------------------------"
  print("Channel 0 : {} ({}V)".format(c0, Volts(c0, 2, Vref)))
  print("Channel 1 : {} ({}V)".format(c1, Volts(c1, 2, Vref)))
  print("Channel 2 : {} ({}V)".format(c2, Volts(c2, 2, Vref)))
  print("Channel 3 : {} ({}V)".format(c3, Volts(c3, 2, Vref)))
  print("Channel 4 : {} ({}V)".format(c4, Volts(c4, 2, Vref)))
  print("Channel 5 : {} ({}V)".format(c5, Volts(c5, 2, Vref)))
  print("Channel 6 : {} ({}V)".format(c6, Volts(c6, 2, Vref)))
  print("Channel 7 : {} ({}V)".format(c7, Volts(c7, 2, Vref)))

  # Wait
  time.sleep(5)
 
