#!/usr/bin/python

from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer
from twisted.internet.task import LoopingCall

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

import sys
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
gpio = 4

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

########################
# DEF CALLBACK PROCESS #
########################
def updating_writer(a):
    
    log.debug("updating the context")
    context  = a[0]
    register = 3 #HOLDING REGISTER
    slave_id = 0x00
    address  = 0x00 #from 0x00 to 0x63
    values   = context[slave_id].getValues(register, address, count=2)
    print('GET VALUES: Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(values[0], values[1]))

    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio) #reading DHT11 values
    
    if humidity is None or temperature is None:
        humidity, temperature = (0, 0)

    values[0] = int(temperature)
    values[1] = int(humidity)
    context[slave_id].setValues(register, address, values)

def funct_coil(a):
    context  = a[0]
    register = 1 #COIL
    slave_id = 0x00
    address  = 0x00
    state = context[slave_id].getValues(register, address, count=1)
    
    if state == [True]:
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)

##############
# DATA STORE #
##############
store = ModbusSlaveContext(
    co = ModbusSequentialDataBlock(0, [False]*100), #COIL
    di = ModbusSequentialDataBlock(0, [False]*100), #DISCRETE INPUT
    hr = ModbusSequentialDataBlock(0, [3]*100), #HOLDING REGISTER
    ir = ModbusSequentialDataBlock(0, [4]*100)) #INPUT REGISTER
context = ModbusServerContext(slaves=store, single=True)

###################### 
# SERVER INFORMATION #
###################### 
identity = ModbusDeviceIdentification()
identity.VendorName = 'Pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
identity.ProductName = 'Pymodbus Server'
identity.ModelName = 'Pymodbus Server'

##############
# RUN SERVER #
############## 
time1 = 5 #seconds of delay
time2 = 1
loop1 = LoopingCall(f=updating_writer, a=(context,))
loop1.start(time1, now=False) #initially delay by time
loop2 = LoopingCall(f=funct_coil, a=(context,))
loop2.start(time2, now=False)
StartTcpServer(context, identity=identity, address=("192.168.1.52", 5020))

