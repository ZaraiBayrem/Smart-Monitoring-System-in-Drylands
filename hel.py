import simplejson as json
import serial
ser=serial.Serial("/dev/ttyACM0",9600)
import time

#to_encoded=to

buffer = ""

 #  ser.write(to_encoded)
while True:
    #if(ser.in_waiting > 0):
     #   line=json.loads(ser.readline().text);
        #deserializeJson(doc, input, Filter(line));
      #  print(line)

       #send E to arduino
       #ser.write(to_encoded)
    try:
        buffer = ser.readline()
        print (buffer)
        data = json.loads(buffer)
        print (data["Soil moisture"])
        s = data["Soil moisture"]
        print(s)
        print (data["Rain"])
        r = data["Rain"]
        print(r)
            #rcv = dummy.split()
            #print(rcv)
        buffer = ""
        print(" ")
    except json.JSONDecodeError:
        print ("Error : try to parse an incomplete message")
