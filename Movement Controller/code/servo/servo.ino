#include <Servo.h>
#include <Wire.h>

Servo servo;
int deg = 45;
int degtmp=90;

void setup() {
  Serial.begin(9600);
  servo.attach(3);
  Wire.begin();  
}

void loop(){
  //degtmp = Serial.read();//Wire.requestFrom(16, 1); 
  //if (degtmp > 0 && degtmp < 180) {deg=degtmp;}
  servo.write(deg);
  //Serial.write(deg); 
}
