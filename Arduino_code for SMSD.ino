
  #include <SPI.h> // SPI
  #include <MFRC522.h> // RFID

#define SS_PIN 10
#define RST_PIN 9

// Déclaration 
MFRC522 rfid(SS_PIN, RST_PIN); 

// Tableau contentent l'ID
byte nuidPICC[4];


int sensorlum =A0;
const int sensorMin = 0;     // sensor minimum
const int sensorMax = 1024;
int sensorPin = A1;  
int sensorValue;  
int limit = 300; 

int ledwarning = 5; 
int ledaccept = 6;  
 
const int pwm = 7 ; //initializing pin 2 as pwm
const int in_1 = 8 ;
const int in_2 = 2 ;
int Vallum ;



void setup() {
    Serial.begin(9600);
   pinMode(pwm,OUTPUT) ; //we have to set PWM pin as output
   pinMode(in_1,OUTPUT) ; //Logic pins are also set as output
   pinMode(in_2,OUTPUT) ;
   pinMode(4, INPUT);
   pinMode(13, INPUT);
   pinMode(ledwarning, OUTPUT);    
   pinMode(ledaccept, OUTPUT);   

  // Init SPI bus
  SPI.begin(); 

  // Init MFRC522 
  rfid.PCD_Init(); 
}
void loop() {
  
  
        Vallum=analogRead(sensorlum) ;
        
       
        Serial.println(Vallum);        
/********************************/
 int sensorReading = analogRead(A5);
  Serial.println(sensorReading);
/*****************/
  sensorValue = analogRead(sensorPin);
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);

    
     Serial.println(sensorValue);                      
                       
      //For Clock wise motion , in_1 = High , in_2 = Low
      analogWrite(pwm,128 ) ; 
     if(digitalRead(4)==LOW && digitalRead(3)==HIGH ){
   //For brake
    digitalWrite(in_1,HIGH) ;
   digitalWrite(in_2,LOW) ;
    delay(4);
   digitalWrite(in_1,LOW) ;
   digitalWrite(in_2,LOW) ;
  
   
   }else if(digitalRead(4)==HIGH && digitalRead(3)==LOW )
  {
     
   digitalWrite(in_1,LOW) ;
   digitalWrite(in_2,HIGH) ;

    delay(4);
   digitalWrite(in_1,LOW) ;
   digitalWrite(in_2,LOW) ;
  
   
   }else if((digitalRead(4)==LOW && digitalRead(3)==LOW )||(digitalRead(4)==HIGH && digitalRead(3)==HIGH )){
   
   
   //For brake
   digitalWrite(in_1,LOW) ;
   digitalWrite(in_2,LOW) ;
   }
     // Initialisé la boucle si aucun badge n'est présent 
  if ( !rfid.PICC_IsNewCardPresent()) 
    return;

  // Vérifier la présence d'un nouveau badge 
  if ( !rfid.PICC_ReadCardSerial())
    return;

  // Enregistrer l'ID du badge (4 octets) 
  for (byte i = 0; i < 4; i++) 
  {
    nuidPICC[i] = rfid.uid.uidByte[i];
  }
  
  // Affichage de l'ID 
 // Serial.println("Un badge est détecté");
 // Serial.println(" L'UID du tag est:");
  for (byte i = 0; i < 4; i++) 
  {
  //  Serial.print(nuidPICC[i], HEX);
   // Serial.print(" ");
  }
  
  if( (nuidPICC[0]==0x80)&&(nuidPICC[1]==0xD6)&(nuidPICC[2]==0xAC)&&(nuidPICC[3]==0x79)){
     //   Serial.print("OPEN");
          digitalWrite(ledwarning, HIGH);   // turn the LED on (HIGH is the voltage level)        
          digitalWrite(ledaccept, LOW);
  
  }else{
     //   Serial.print("WARNING");
         digitalWrite(ledaccept, HIGH);   // turn the LED on (HIGH is the voltage level)
          digitalWrite(ledwarning, LOW);
        
  }  
//  Serial.println();

  // Re-Init RFID
  rfid.PICC_HaltA(); // Halt PICC
  rfid.PCD_StopCrypto1(); // Stop encryption on PCD 
  
 }
 

 
