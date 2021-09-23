#include <Wire.h>

void setup() {
    Wire.begin();
    Serial.begin(9600);
}

void loop() {
    Wire.requestFrom(1, 1);
    while (Wire.available()) {
        Serial.print(Wire.read());
        Serial.print(" ");
    }
    Serial.println();
    delay(1000);
}
