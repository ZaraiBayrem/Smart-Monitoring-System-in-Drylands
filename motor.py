import RPi.GPIO as GPIO
from time import sleep


# Definition des pins
M1_En = 18
M1_In1 = 23
M1_In2 = 24



# Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [M1_En, M1_In1, M1_In2]


# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)

# Voir aide dans le tuto
M1_Vitesse = GPIO.PWM(M1_En, 100)

M1_Vitesse.start(100)



def sens1(moteurNum) :
    GPIO.output(Pins[1], GPIO.HIGH)
    GPIO.output(Pins[2], GPIO.LOW)
    print("Moteur", moteurNum, "tourne dans le sens 1.")


def arret(moteurNum) :
    GPIO.output(Pins[1], GPIO.LOW)
    GPIO.output(Pins[2], GPIO.LOW)
    print("Moteur", moteurNum, "arret.")


    print("Moteurs arretes.")



def motor():
    # Exemple de motif de boucle
    sens1(1)
    sleep(3)
    arret(1)
