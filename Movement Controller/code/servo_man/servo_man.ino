#include <Servo.h>

Servo servo;
int deg;

void setup() {
    servo.attach(3); 
    Serial.begin(9600);
}

void loop(){
    deg = Serial.parseInt();
    if (deg != 0) {
        servo.write(deg);    
    }
}
