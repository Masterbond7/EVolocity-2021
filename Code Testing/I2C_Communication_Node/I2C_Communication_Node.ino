#include <Wire.h>

int a = 1;

void setup() {
    Wire.begin(1);
    Wire.onRequest(requestCode);
}

void loop() {
    delay(100);
}

void requestCode() {
    Wire.write(a++);
}
