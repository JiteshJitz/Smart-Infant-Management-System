import RPi.GPIO as GPIO
import pyfirmata
from time import sleep
import datetime
from firebase import firebase
import Adafruit_DHT
import time
import urllib2, urllib, httplib
import json
import os 
from functools import partial

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

board = pyfirmata.Arduino('/dev/ttyACM0')

it = pyfirmata.util.Iterator(board)
it.start()

#firebase intializations
firebase = firebase.FirebaseApplication('https://myfirst-869f2.firebaseio.com', None)

#dht declarations
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#moisture declarations

sensor_pin0 = board.get_pin('a:4:i')

#smoke declareations

sensor_pin1 = board.get_pin('a:1:i')

#sound declarations

sensor_pin2 = board.get_pin('a:2:i')

#pirone declarations

sensor_pin = board.get_pin('d:2:i')

flag = 15








def dht():

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
                print('Temprature and Humidity values')
                #sleep(2)
		str_temp = ' {0:0.2f} '.format(temperature)
		str_hum  = ' {0:0.2f} '.format(humidity)
		ts = time.time()
                c = int(ts)
                str2 = str(c)
                str0 = str(temperature) + " " + str2
                str3 = str(humidity) + " " + str2
		print(str0)
		print(str3)
		ab = int(temperature)
		
                result = firebase.post('DHT11/Temperature',str(ab))
                result1 = firebase.post('DHT11/Humidity',str3)
                if(ab < 22 ):
                    notify = firebase.post('notification/Temperature', {'time':str2, 'value':str(str_temp), 'staus':'critical'})
                elif(ab > 23 and ab < 29):
                    notify = firebase.post('notification/Temperature', {'time':str2, 'value':str(str_temp), 'staus':'normal'})
                elif(ab > 30 and ab < 34):
                    notify = firebase.post('notification/Temperature', {'time':str2, 'value':str(str_temp), 'staus':'see temprature'})
                elif(ab > 35):
                    notify = firebase.post('notification/Temperature', {'time':str2, 'value':str(str_temp), 'staus':'very critical'})
                    notify = firebase.post('notification/Critical/temp', {'time':str2, 'value':str(str_temp), 'staus':'Temprature very critical'})
                else:
                    notify = firebase.post('notification/Temperature', {'time':str2, 'value':str(str_temp), 'staus':'normal'})
			
	else:
		print('Failed to get reading. Try again!')	
		sleep(10)
	#time.sleep(2)

	
def moist():
    
    
    input_state = sensor_pin0.read()
    print("Moisture Values")
    #print(input_state)
    #a = int(input_state)*100
    #print(a)
    time.sleep(0.2)
    if(input_state != None):
        a = float(input_state)*1000
        #print(int(a))
        
        b= int(a)
        
        ts = time.time()
        c = int(ts)
        #print(c)
        str1 = str(b)
        str2 = str(c)
##        str3 = " "
        str0 = str1 + " " + str2
        
        
        #result = firebase.post('PythonWala', str0)
        result = firebase.post('Moisture/value', str0)
        print(str0)
        
     
        
        
        if(b < 550):
            
            notify = firebase.post('notification/Moisture', {'time':str2, 'value':str(b), 'staus':'critical'})
            notify = firebase.post('notification/Critical/Moisture', {'time':str2, 'value':str(b), 'staus':'moisture level very critical'})
        
        else:
            notify = firebase.post('notification/Moisture', {'time':str2, 'value':str(b), 'staus':'normal'})
			
def smoke():
    
    input_state = sensor_pin1.read()
    time.sleep(0.2)
    if(input_state != None):
        a = float(input_state)*1000
        print('Smoke Values')
      #  print(int(a))
        b= int(a)
        ts = time.time()
        c = int(ts)
        str1 = str(b)
        str2 = str(c)
        str0 = str1 + " " + str2
        
        
        result = firebase.post('Smoke', str0)
        print(str0)
        
        if(b < 400):
            
            notify = firebase.post('notification/Smoke', {'time':str2, 'value':str(b), 'staus':'very critical'})
            notify = firebase.post('notification/Critical/Smoke', {'time':str2, 'value':str(b), 'staus':'smoke level very critical'})
        
        elif(b > 401 and b < 550):
            notify = firebase.post('notification/Smoke', {'time':str2, 'value':str(b), 'staus':'critical'}) 
        
        else:
            notify = firebase.post('notification/Smoke', {'time':str2, 'value':str(b), 'staus':'normal'})
            
            
def sound():
    
    input_state = sensor_pin2.read()
    time.sleep(0.2)
    if(input_state != None):
        a = float(input_state)*1000
        print('Sound Values')
       # print(int(a))
        b= int(a)
        ts = time.time()
        c = int(ts)
        str1 = str(b)
        str2 = str(c)
        str0 = str1 + " " + str2
        
        
        result = firebase.post('Sound', str0)
        print(str0)
        
        if(b < 400):
            
            notify = firebase.post('notification/Sound', {'time':str2, 'value':str(b), 'staus':'very critical'})
            notify = firebase.post('notification/Critical/Sound', {'time':str2, 'value':str(b), 'staus':'smoke level very critical'})
        
        elif(b > 401 and b < 550):
            notify = firebase.post('notification/Sound', {'time':str2, 'value':str(b), 'staus':'critical'}) 
        
        else:
            notify = firebase.post('notification/Sound', {'time':str2, 'value':str(b), 'staus':'normal'})
            
            
def pir1():
    
    
    
    input_state = sensor_pin.read()
    ts = time.time()
    c = int(ts)
    #flag = 10
        #print(c)
        
    str2 = str(c)
##        str3 = " "
    #str0 = str1 + " " + str2
    #print(input_state)
    #a = 0
    if(input_state == True):
        str1 = str("Movement")
        str0 = str1 + " " + str2
        print(str0)
        #a = str0
    else:
        str1 = str("No movement")
        str0 = str1 + " " + str2
        #a = str0
        print(str0)
        #flag = flag-2
        #print(flag)
    time.sleep(2)
'''
    if(flag == 0):
        print("Movement detected")
        flag = 15
        #print(a)
        
    '''
            

    
    


while True:
    
    dht()
    smoke()
    moist()
    sound()
    pir1()
    
	


