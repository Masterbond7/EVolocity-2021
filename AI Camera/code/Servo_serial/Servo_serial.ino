#include <Servo.h>

Servo servo;
int deg = 0;
int tmp = 0;

void setup() {
    Serial.begin(9600);
    servo.attach(2);
}

void loop() {
    if (Serial.available()){
        tmp = Serial.parseInt();
        deg = (tmp * -1)+180;
        Serial.print(tmp); Serial.print(" ("); Serial.print(deg); Serial.println(")");
        servo.write(deg);
    }
}
