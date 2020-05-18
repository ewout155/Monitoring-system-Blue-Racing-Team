# Libraries
import serial
import json 
import paho.mqtt.client as mqtt
import string
from time import sleep
# Serial port microcontroller
port = "/dev/ttyACM0"
# Data strings 
Accu = {'v': 0, 'c': 0, 'p': 0, 't': 0}
AccuCel = {'cn1': 0, 'cv1': 0, 'ct1': 0, 
           'cn2': 0, 'cv2': 0, 'ct2': 0,
           'cn3': 0, 'cv3': 0, 'ct3': 0,
           'cn4': 0, 'cv4': 0, 'ct4': 0,
           'cn5': 0, 'cv5': 0, 'ct5': 0,
           'cn6': 0, 'cv6': 0, 'ct6': 0,
           'cn7': 0, 'cv7': 0, 'ct7': 0,
           'cn8': 0, 'cv8': 0, 'ct8': 0,
           'cn9': 0, 'cv9': 0, 'ct9': 0,
           'cn10': 0, 'cv10': 0, 'ct10': 0,
           'cn11': 0, 'cv11': 0, 'ct11': 0,
           'cn12': 0, 'cv12': 0, 'ct12': 0}
AccuCharging = {'vi': 0, 'ci': 0}
MotorControllers = {'r': 0, 'a': 0}
# Functions
# CAN-bus Accu
def mqttPostAccu(str):
    Accu['v'] = voltage
    Accu['c'] = current
    Accu['p'] = accuPercentage
    Accu['t']= temperature
    broker_address="localhost"
    client = mqtt.Client("RaspberryPi_Accu")
    client.connect(broker_address)
    client.subscribe("pi/sensors")
    client.loop_start()
    client.publish("pi/sensors_accu", json.dumps(Accu),)
    client.loop_stop()
    sleep(1)
# Cel level accu
def mqttPostAccuCel(str):
    AccuCel['cn1'] = celNumber1
    AccuCel['cn2'] = celNumber2
    AccuCel['cn3'] = celNumber3
    AccuCel['cn4'] = celNumber4
    AccuCel['cn5'] = celNumber5
    AccuCel['cn6'] = celNumber6
    AccuCel['cn7'] = celNumber7
    AccuCel['cn8'] = celNumber8
    AccuCel['cn9'] = celNumber9
    AccuCel['cn10'] = celNumber10
    AccuCel['cn11'] = celNumber11
    AccuCel['cn12'] = celNumber12
    AccuCel['cv1'] = celVoltage1
    AccuCel['cv2'] = celVoltage2
    AccuCel['cv3'] = celVoltage3
    AccuCel['cv4'] = celVoltage4
    AccuCel['cv5'] = celVoltage5
    AccuCel['cv6'] = celVoltage6
    AccuCel['cv7'] = celVoltage7
    AccuCel['cv8'] = celVoltage8
    AccuCel['cv9'] = celVoltage9
    AccuCel['cv10'] = celVoltage10
    AccuCel['cv11'] = celVoltage11
    AccuCel['cv12'] = celVoltage12
    AccuCel['ct1'] = celTemperature1
    AccuCel['ct2'] = celTemperature2
    AccuCel['ct3'] = celTemperature3
    AccuCel['ct4'] = celTemperature4
    AccuCel['ct5'] = celTemperature5
    AccuCel['ct6'] = celTemperature6
    AccuCel['ct7'] = celTemperature7
    AccuCel['ct8'] = celTemperature8
    AccuCel['ct9'] = celTemperature9
    AccuCel['ct10'] = celTemperature10
    AccuCel['ct11'] = celTemperature11
    AccuCel['ct12'] = celTemperature12

    broker_address="localhost"
    client = mqtt.Client("RaspberryPi_AccuCel")
    client.connect(broker_address)
    client.subscribe("pi/sensors")
    client.loop_start()
    client.publish("pi/sensors_accuCel", json.dumps(AccuCel),)
    client.loop_stop()
    sleep(1)
# Charge mode
def mqttPostCharging(str):
    AccuCharging['vi'] = voltageIn
    AccuCharging['ci'] = currentIn
    broker_address="localhost"
    client = mqtt.Client("RaspberryPi_AccuCharging")
    client.connect(broker_address)
    client.subscribe("pi/sensors")
    client.loop_start()
    client.publish("pi/sensors_accuCharging", json.dumps(AccuCharging),)
    client.loop_stop()
    sleep(1)
# Motor Controllers
def mqttPostMotorControllers(str):
    MotorControllers['r'] = RPS
    MotorControllers['a'] = angleAccelerationPaddle
    broker_address="localhost"
    client = mqtt.Client("RaspberryPi_MotorControllers")
    client.connect(broker_address)
    client.subscribe("pi/sensors")
    client.loop_start()
    client.publish("pi/sensors_motorControllers", json.dumps(MotorControllers),)
    client.loop_stop()
    sleep(1)
# Serial settings
ser = serial.Serial(port, baudrate = 9600, timeout = 1)
# Main loop
while True:
    data = ser.readline()
    #print data
    dataS = data.split(',')
    #print dataS
    # CAN-bus Accu:
    voltage = float(dataS[0][0:2])
    current = float(dataS[1][1:3])
    accuPercentage = float(dataS[2][1:3])
    temperature = float(dataS[3][1:3])

    # CAN-bus accu cel level:
    celNumber1 = float(dataS[4][1:3])
    celNumber2 = float(dataS[5][1:3])
    celNumber3 = float(dataS[6][1:3])
    celNumber4 = float(dataS[7][1:3])
    celNumber5 = float(dataS[8][1:3])
    celNumber6 = float(dataS[9][1:3])
    celNumber7 = float(dataS[10][1:3])
    celNumber8 = float(dataS[11][1:3])
    celNumber9 = float(dataS[12][1:3])
    celNumber10 = float(dataS[13][1:3])
    celNumber11 = float(dataS[14][1:3])
    celNumber12 = float(dataS[15][1:3])
    celVoltage1 = float(dataS[16][1:3])
    celVoltage2 = float(dataS[17][1:3])
    celVoltage3 = float(dataS[18][1:3])
    celVoltage4 = float(dataS[19][1:3])
    celVoltage5 = float(dataS[20][1:3])
    celVoltage6 = float(dataS[21][1:3])
    celVoltage7 = float(dataS[22][1:3])
    celVoltage8 = float(dataS[23][1:3])
    celVoltage9 = float(dataS[24][1:3])
    celVoltage10 = float(dataS[25][1:3])
    celVoltage11 = float(dataS[26][1:3])
    celVoltage12 = float(dataS[27][1:3])
    celTemperature1 = float(dataS[28][1:4])
    celTemperature2 = float(dataS[29][1:4])
    celTemperature3 = float(dataS[30][1:4])
    celTemperature4 = float(dataS[31][1:4])
    celTemperature5 = float(dataS[32][1:4])
    celTemperature6 = float(dataS[33][1:4])
    celTemperature7 = float(dataS[34][1:4])
    celTemperature8 = float(dataS[35][1:4])
    celTemperature9 = float(dataS[36][1:4])
    celTemperature10 = float(dataS[37][1:4])
    celTemperature11 = float(dataS[38][1:4])
    celTemperature12 = float(dataS[39][1:4])

    # CAN-bus accu while charging
    voltageIn = float(dataS[40][1:3])
    currentIn = float(dataS[41][1:3])

    # CAN-bus motorcontrollers
    RPS = float(dataS[42][1:3])
    angleAccelerationPaddle = float(dataS[43][1:3])

    mqttPostAccu(str)
    mqttPostAccuCel(str)
    mqttPostCharging(str)
    mqttPostMotorControllers(str)

    # Notes
    # To subscribe: mosquitto_sub -p 1883 -h <ip address> -t "<topic>"

    # Output strings:
    # {"current": 20.0, "accuPercentage": 83.0, "voltage": 40.0, "temperature": 25.0}
    # {"celVoltage": 2.0, "celTemperature": 50.0, "celNumber": 1.0}
    # {"voltageIn": 45.0, "currentIn": 3.0}
    # {"RPS": 20.0, "angleAccelerationPaddle": 45.0}
