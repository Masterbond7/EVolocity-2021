
int loosestop = 18;
int tightstop = 19;
int mode = 5;
int PUL=9; //define Pulse pin
int DIR=6; //define Direction pin
int ENA=10; //define Enable Pin

volatile int rpmMot = 0;
volatile int rpmPreClutch = 0;
volatile int rpmPostClutch = 0;

unsigned long motRotation = 0;
unsigned long preRotation = 0;
unsigned long postRotation = 0;

String eff="off";

void setup(){
   Serial.begin(9600);
   pinMode(loosestop,INPUT);   //micro switch pin 3, full loose.
   pinMode(tightstop,INPUT);   //micro switch pin 4, full tight.
   pinMode(mode,INPUT);   //switch Sports mode, high sports,low economy.

   pinMode(7, INPUT_PULLUP); 
   attachInterrupt(digitalPinToInterrupt(7), rpm_Mot, RISING); //pin 7 is interrupt 4 (INT4).
   pinMode(1, INPUT_PULLUP);   
   attachInterrupt(digitalPinToInterrupt(1), rpm_PreClutch, RISING); //pin 1 is interrupt 3 (INT3). 
   pinMode(0, INPUT_PULLUP);  
   attachInterrupt(digitalPinToInterrupt(0), rpm_PostClutch, RISING); //pin 0 is interrupt 2 (INT2). 
   pinMode(PUL,OUTPUT);
   pinMode(DIR,OUTPUT);
   pinMode(ENA,OUTPUT);
  }    
 
void loop(){
   if (digitalRead(mode)== HIGH) {
   sports();}
   else economy();
  }

void sports(){
   if(millis() - motRotation >= 2000)
   rpmMot = 0.0; 
   if (rpmMot < 1) {off();}
   if (rpmMot > 0 && rpmMot < 280) { anticlock() ;}
   if (rpmMot >= 280 && rpmMot <= 320) { off();}
   if (rpmMot > 320) { clockwise() ;}
   loop();
  }

void economy(){
   if(millis() - motRotation >= 2000)
   rpmMot = 0.0;
   if (rpmMot < 1) {off();}
   if (rpmMot > 0 && rpmMot < 320) { anticlock();}
   if (rpmMot >= 320 && rpmMot <= 360) { off() ;}
   if (rpmMot > 360) { clockwise();}
   loop();
  }

void rpm_Mot(){
   rpmMot  = (60000.0/(millis()-motRotation));
   motRotation = millis();
  }
   
void rpm_PreClutch(){
   rpmPreClutch  = (60000.0/(millis()-preRotation));
   preRotation = millis();
  }

void rpm_PostClutch(){
   rpmPostClutch  = (60000.0/(millis()-postRotation));
   postRotation = millis();
  }

void off(){   
   digitalWrite(DIR,LOW);
   digitalWrite(ENA,LOW);
   digitalWrite(PUL,LOW);
   delayMicroseconds(100);
   digitalWrite(PUL,LOW);
   delayMicroseconds(100);
   loop();
   }

void anticlock(){
   if (digitalRead(loosestop) == HIGH) {
    for (int i=0; i<1584; i++)    //Forward 1 turn steps
  { 
    digitalWrite(DIR,LOW);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(100);
    digitalWrite(PUL,LOW);
    delayMicroseconds(100);
   }
   }
  }
 

void clockwise(){
   if (digitalRead(tightstop) == HIGH) {
    for (int i=0; i<1584; i++)    //Forward 1 turn steps
   { 
    digitalWrite(DIR,HIGH);
    digitalWrite(ENA,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(100);
    digitalWrite(PUL,LOW);
    delayMicroseconds(100);
   }
   }
  }
   
