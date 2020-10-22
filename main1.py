
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin.firestore import SERVER_TIMESTAMP
from dht_test import temp_hum
import time
import serial
from hello import arduino
import csv
#from camera import density
from firebase import firebase
import json
import datetime
time = datetime.datetime.now().strftime("%H:%M")
from ubidots import post_request
from motor import motor

firebase = firebase.FirebaseApplication('https://gps-app-285100.firebaseio.com/', None)
TOKEN = "BBFF-XpndKSTy3FweBRzQ04I1K9BQTYeb48"  # Put your TOKEN here
DEVICE_LABEL = "Raspberry"  # Put your device label here 
# Use a service account
i=0
ser=serial.Serial("/dev/ttyUSB0",9600)
cred = credentials.Certificate('a.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
with open('weather_station.txt',mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["temp","hum","soil","light","rain","Density"])
while True:
    i+=1
    temp,hum=temp_hum()
    while (temp =="error"):
        temp,hum=temp_hum()
#    if temp>50:
#       motor()
    motor()
    s=arduino()
    if i>1:
        rain=s["rain"]
        soil=s["Soil"]
        lum=s["Light Intensity"]
    else:
        rain,soil,lum=0,0,0

    doc_ref = db.collection(u'Monitoring_Data').document(str(i))
    doc_ref.set({
        u'Temperature': temp,
        u'humidity': hum,
        u'date': SERVER_TIMESTAMP,
        u'moisture': soil,
        u'light': lum,
        u'rain': rain
    })

    time = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S-UTC-1")
    density=85
    dict={}
    dict["temperature"]=temp
    dict["humidity"]=hum
    dict["light"]=lum
    dict["moisture"]=soil
    dict["rain"]=rain
    dict["tree"]=density
    post_request(dict,DEVICE_LABEL,TOKEN)
    firebase.put('gps-app-285100', 'temperature', temp)
    firebase.put('gps-app-285100', 'moisture', int(soil))
    firebase.put('gps-app-285100', 'rain', int(rain))
    firebase.put('gps-app-285100', 'humidity', hum)
    firebase.put('gps-app-285100', 'light', int(lum))
    firebase.put('gps-app-285100', 'date', time)
    firebase.put('gps-app-285100', 'tree', density)
    with open('weather_station.txt',mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([str(temp),str(hum),soil,lum,rain])




