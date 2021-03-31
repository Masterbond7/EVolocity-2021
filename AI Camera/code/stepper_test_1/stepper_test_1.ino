  const int stepPin = 2; //X.STEP
  const int dirPin = 5; // X.DIR
  const int limPin = 9;
 
 void setup() {
  Serial.begin(9600);
 // Sets the two pins as Outputs
 pinMode(stepPin,OUTPUT);
 pinMode(stepPin+1,OUTPUT);
 pinMode(stepPin+2,OUTPUT); 
 pinMode(dirPin,OUTPUT);
 pinMode(dirPin+1,OUTPUT);
 pinMode(dirPin+2,OUTPUT);
 pinMode(limPin, INPUT);
 }


 
 void loop() {
 Serial.println(digitalRead(limPin));
 digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
 digitalWrite(dirPin+1,HIGH);
 digitalWrite(dirPin+2,HIGH);
 // Makes 200 pulses for making one full cycle rotation
 for(int x = 0; x < 1000; x++) {
   digitalWrite(stepPin,HIGH); 
   digitalWrite(stepPin+1,HIGH);
   digitalWrite(stepPin+2,HIGH);
   delayMicroseconds(500); 
   digitalWrite(stepPin,LOW); 
   digitalWrite(stepPin+1,LOW); 
   digitalWrite(stepPin+2,LOW);
   delayMicroseconds(500); 
 }
 delay(500); // One second delay
 
 digitalWrite(dirPin,LOW); //Changes the rotations direction
 digitalWrite(dirPin+1,LOW);
 digitalWrite(dirPin+2,LOW);
 // Makes 400 pulses for making two full cycle rotation
 for(int x = 0; x < 1000; x++) {
   digitalWrite(stepPin,HIGH); 
   digitalWrite(stepPin+1,HIGH);
   digitalWrite(stepPin+2,HIGH);
   delayMicroseconds(500); 
   digitalWrite(stepPin,LOW); 
   digitalWrite(stepPin+1,LOW); 
   digitalWrite(stepPin+2,LOW);
   delayMicroseconds(500); 
 }
 delay(500);
 }
