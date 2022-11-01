// for Arduino Nano

int lowstop = 7;
int highstop = 10;
int PUL=13; //define Pulse pin
int DIR=14; //define Direction pin


volatile int rpmMot = 0;

unsigned long motRotation = 0;

String eff="off";

void setup(){
   Serial.begin(9600);
   pinMode(lowstop,INPUT);   //micro switch pin 7, full loose.
   pinMode(highstop,INPUT);   //micro switch pin 10, full tight.
   
   pinMode(05, INPUT); 
   attachInterrupt(digitalPinToInterrupt(05), rpm_Mot, RISING); //pin D2 is interrupt 0 (INT.0).
  
   pinMode(PUL,OUTPUT);
   pinMode(DIR,OUTPUT);
  
  }    
 
void loop(){
  
   if(millis() - motRotation >= 2000)
   rpmMot = 0.0; 
   
   Serial.print ("rpmMot");
   Serial.print ( rpmMot );
   
   if (rpmMot < 1) {off();}
   if (rpmMot > 0 && rpmMot < 100) { anticlock() ;}
   if (rpmMot >= 100 && rpmMot <= 150) { off();}
   if (rpmMot > 150) { clockwise() ;}
   
  }



void rpm_Mot(){
   rpmMot  = (60000.0/(millis()-motRotation));
   motRotation = millis();
  }
   

void off(){   
   digitalWrite(DIR,LOW);
 
   digitalWrite(PUL,LOW);
   delayMicroseconds(100);
   digitalWrite(PUL,LOW);
   delayMicroseconds(100);
   loop();
   }

void anticlock(){
   if (digitalRead(lowstop) == LOW) {
    for (int i=0; i<1584; i++)    //Forward 1 turn steps
  { 
    digitalWrite(DIR,LOW);
   
    digitalWrite(PUL,HIGH);
    delayMicroseconds(100);
    digitalWrite(PUL,LOW);
    delayMicroseconds(100);
   }
   }
  }
 

void clockwise(){
   if (digitalRead(highstop) == LOW) {
    for (int i=0; i<1584; i++)    //Forward 1 turn steps
   { 
    digitalWrite(DIR,HIGH);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
 
    digitalWrite(PUL,HIGH);
    delayMicroseconds(100);
    digitalWrite(PUL,LOW);
    delayMicroseconds(100);
   }
   }
  }
   
