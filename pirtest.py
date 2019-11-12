import pyfirmata
#from firebase import firebase
import time
#firebase= firebase.FirebaseApplication('https://myfirst-869f2.firebaseio.com')
board = pyfirmata.Arduino('/dev/ttyACM0')
sensor_pin = board.get_pin('d:2:i')
it = pyfirmata.util.Iterator(board)
it.start()

while True:
    flag = 15
    input_state = sensor_pin.read()
    ts = time.time()
    c = int(ts)
    #flag = 10
        #print(c)
        
    str2 = str(c)
##        str3 = " "
    #str0 = str1 + " " + str2
    #print(input_state)
    if(input_state == True):
        str1 = str("1")
        str0 = str1 + " " + str2
        print(str0)
    else:
        str1 = str("0")
        str0 = str1 + " " + str2
        print(str0)
        flag = flag-2
        print(flag)
    time.sleep(2)

    if(flag == 0):
        print("hello")
        flag = 1
        
    
  #  if(input_state == False):
       # var1 = int(time.time())
        #flag1 = 0
        
        
