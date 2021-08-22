#include <Servo.h>

Servo servo;
int deg = 90;
int tmp = 0;

void setup() {
    Serial.begin(9600);
    servo.attach(3);
}

void loop() {
    while (Serial.available() > 0) {
        deg -= int((Serial.parseFloat()*0.25));
    
        if (servo.read() < deg) {
            for (int i = deg; deg > servo.read(); --deg) {
                servo.write(deg);
            }    
        } else if (servo.read() > deg) {
            for (int i = deg; deg < servo.read(); ++deg) {
                servo.write(deg);
            }  
        }
    }
}
