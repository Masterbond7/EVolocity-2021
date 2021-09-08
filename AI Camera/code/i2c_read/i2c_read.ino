#include <Wire.h>

int deg = 90;

void setup() {
    Wire.begin();
    Serial.begin(9600);
}

void loop() {
    Wire.requestFrom(16, 1);
    while (Wire.available()) {
        deg = Wire.read();
        Serial.print(deg);   
    }
    delay(200);
}
