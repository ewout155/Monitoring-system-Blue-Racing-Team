import serial
import pynmea2
import json
import paho.mqtt.client as mqtt
import string
from time import sleep

port = "/dev/ttyS0"

sensorData = {'lat': 0, 'lng': 0, 'v': 0}

def logData(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
	print "Time: %s, Latitude: %s, DirectionLatitude: %s, Longitude: %s, DirectionLongitude: %s, Altitude: %s %s, Satellites: %s, Speed: %s"  % (msg.timestamp,round(msg.latitude,6),msg.lat_dir,round(msg.longitude,6),msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats,msg.horizontal_dil)
        file = open("/home/pi/Code/data_log.csv", "a")
        file.write("Time: %s, Latitude: %s, DirectionLatitude: %s, Longitude: %s, DirectionLongitude: %s, Altitude: %s %s, Satellites: %s, Speed: %s\n" % (msg.timestamp,round(msg.latitude,6),msg.lat_dir,round(msg.longitude,6),msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats,msg.horizontal_dil))

def mqttPost(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        sensorData['lat'] = round(msg.latitude,6)
        sensorData['lng'] = round(msg.longitude,6)
        sensorData['v'] = msg.horizontal_dil
        broker_address="localhost"
        client = mqtt.Client("RaspberryPi_GPS")
        client.connect(broker_address)
        client.subscribe("pi/sensors")
        client.loop_start()
        client.publish("pi/sensors_gps", json.dumps(sensorData),)
        client.loop_stop()
	sleep(1)

serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
    str = serialPort.readline()
# Log data to Excelsheet
    logData(str)
# Mosquitto mqtt broker
# mosquitto_sub -p 1883 -h 192.168.178.15 -t "pi/sensors_gps"
    mqttPost(str)

