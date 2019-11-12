import pyfirmata
from firebase import firebase
import time
firebase= firebase.FirebaseApplication('https://myfirst-869f2.firebaseio.com')
board = pyfirmata.Arduino('/dev/ttyACM0')
sensor_pin = board.get_pin('a:4:i')
it = pyfirmata.util.Iterator(board)
it.start()
while True:
    input_state = sensor_pin.read()
    #print(input_state)
    #a = int(input_state)*100
    #print(a)
    time.sleep(0.2)
    if(input_state != None):
        a = float(input_state)*1000
        print(int(a))
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
        
        
        
        
'''
result = firebase.post('Smoke', 'hello')
print(result)
import time;
ts = time.time()
a = int(ts)
print(a)

'''
        
    
    
