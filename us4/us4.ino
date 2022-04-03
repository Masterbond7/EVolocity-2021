
// Arduino Ultrasoninc Sensor HC-SR04
// Using HC-SR04 Module

#include <Wire.h>

int trig, echo, distance;
long duration;

/*union u_tag {
    unsigned int Int[4];
} data;*/
int data[4];

void setup() {

  for (int i=0; i<4; i++) {

    trig = i + 18;
  
    if (i < 1) {
      echo = i + 6;
    }
    else {
      echo = i + 7;
    }

    pinMode(trig, OUTPUT); // Sets the trigPin as an OUTPUT
    pinMode(echo, INPUT); // Sets the echoPin as an INPUT
  }
  
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  Wire.begin(17);
  Wire.onRequest(sendData);

  
}
void loop() {
  
  for (int i=0; i<4; i++) {

    trig = i + 18;
  
    if (i < 1) {
      echo = i + 6;
    }
    else {
      echo = i + 7;
    }
    
    digitalWrite(trig, LOW);
    delayMicroseconds(2);
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig, LOW);
  
    duration = pulseIn(echo, HIGH);
    distance = duration * 0.034 / 2; 
    data[i] = distance;

    //Serial.print("Distance %d: %dcm", i, distance);
    Serial.print("Distance ");
    Serial.print(i);
    Serial.print(": ");
    Serial.println(distance);
  
    delayMicroseconds(50);
    
  }
}
void sendData() {
  Wire.write(data, 4);  
}

  
