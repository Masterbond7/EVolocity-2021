#include <Wire.h>

void setup() {
    Serial.begin(9600);
    Wire.begin(17);
    Wire.onRequest(sendData);

    pinMode(2, INPUT_PULLUP); // D-pad up
    pinMode(3, INPUT_PULLUP); // D-pad left
    pinMode(4, INPUT_PULLUP); // D-pad right
    pinMode(5, INPUT_PULLUP); // D-pad down
    pinMode(6, INPUT_PULLUP); // ???
    pinMode(7, INPUT_PULLUP); // ???
    pinMode(8, INPUT_PULLUP); // ???
    pinMode(9, INPUT_PULLUP); // B
    pinMode(10, INPUT_PULLUP); // Right paddle
    pinMode(11, INPUT_PULLUP); // A
    pinMode(12, INPUT_PULLUP); // Left paddle
    pinMode(A6, INPUT); // X
    pinMode(A7, INPUT); // Y
    pinMode(17, INPUT_PULLUP); // X-Box button

    pinMode(16, OUTPUT); // Power bulb
    pinMode(15, OUTPUT); // Steering power (+5V)

    pinMode(A0, INPUT); // Steering

    digitalWrite(16, HIGH); // Bulb
    digitalWrite(15, HIGH); // Steering power (+5V)
}

void loop() {
    if (digitalRead(2) == LOW) {Serial.print("D-pad up, ");} 
    if (digitalRead(3) == LOW) {Serial.print("D-pad left, ");} 
    if (digitalRead(4) == LOW) {Serial.print("D-pad right, ");} 
    if (digitalRead(5) == LOW) {Serial.print("D-pad down, ");} 
    
    if (digitalRead(6) == LOW) {Serial.print("UNDEFINED 1, ");} 
    if (digitalRead(7) == LOW) {Serial.print("UNDEFINED 2, ");} 
    if (digitalRead(8) == LOW) {Serial.print("UNDEFINED 3, ");}
    
    if (digitalRead(9) == LOW) {Serial.print("B, ");}  
    if (digitalRead(11) == LOW) {Serial.print("A, ");} 
    if (analogRead(A6) < 512) {Serial.print("X, ");} 
    if (analogRead(A7) < 512) {Serial.print("Y, ");} 

    if (digitalRead(12) == LOW) {Serial.print("Left padle, ");} 
    if (digitalRead(10) == LOW) {Serial.print("Right padle, ");} 

    if (digitalRead(17) == LOW) {Serial.print("X-Box button, ");} 

    Serial.println(analogRead(A0));
}

byte steering;
union u_tag {
    unsigned int Int;
    byte Byte[2];
} wheelData;
byte finalBytes[3];

void sendData() {
    steering = analogRead(A0) / 4; // Get steering angle between 0-255

    wheelData.Int = 0;
    if (digitalRead(2) == LOW) {wheelData.Int += 1;} //D-Pad Up
    if (digitalRead(3) == LOW) {wheelData.Int += 2;} //D-Pad Left 
    if (digitalRead(4) == LOW) {wheelData.Int += 4;} //D-Pad Right
    if (digitalRead(5) == LOW) {wheelData.Int += 8;} //D-Pad down
    
    if (digitalRead(6) == LOW) {wheelData.Int += 16;} //UNDEFINED 1
    if (digitalRead(7) == LOW) {wheelData.Int += 32;} //UNDEFINED 2
    if (digitalRead(8) == LOW) {wheelData.Int += 64;} //UNDEFINED 3
    
    if (digitalRead(9) == LOW) {wheelData.Int += 128;}  // B
    if (digitalRead(11) == LOW) {wheelData.Int += 256;} // A
    if (analogRead(A6) < 512) {wheelData.Int += 512;}   // X
    if (analogRead(A7) < 512) {wheelData.Int += 1024;}   // Y

    if (digitalRead(12) == LOW) {wheelData.Int += 2048;} //Left paddle
    if (digitalRead(10) == LOW) {wheelData.Int += 4096;} //Right paddle

    if (digitalRead(17) == LOW) {wheelData.Int += 8192;} //X-Box button

    // TODO: Optimize this
    finalBytes[0] = steering;
    finalBytes[1] = wheelData.Byte[0];
    finalBytes[2] = wheelData.Byte[1];
    
    Wire.write(finalBytes, 3);
}
