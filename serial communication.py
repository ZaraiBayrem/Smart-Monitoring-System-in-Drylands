import serial 
import time 
ser=serial.Serial("/dev/ttyUSB0",9600)

#to_encoded=to
def arduino():
 #  ser.write(to_encoded)
    dict={}
    if(ser.in_waiting > 0):
#    while True:
        l=ser.readline().decode('ascii').rstrip('\r\n')
        print(l)
        dict["Light Intensity"]=l
       #print arduino msg 
        s=ser.readline().decode('ascii').rstrip('\r\n')
        time.sleep(2)
        dict["Soil"]=s
            #print(json.loads(line))
        time.sleep(2) 
        r=ser.readline().decode('ascii').rstrip('\r\n')
        dict["rain"]=r
        return dict
#arduino()
