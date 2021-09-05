#include <Servo.h>
#include "HUSKYLENS.h"
#include "SoftwareSerial.h"

Servo servo;
int deg = 90;
int tmp = 0;

HUSKYLENS huskylens;
SoftwareSerial huskyserial(4,5); //Huskylens's TX 4, RX 5


int adjustment_px = 160; // The distance in pixels from the far left of the screen to the center of the screen
float px_to_deg = 0.1875; // half screen fov * half screen res

void setup() {
    Serial.begin(9600);
    servo.attach(3);
    servo.write(90);

    huskyserial.begin(9600);
    while (!huskylens.begin(huskyserial)) { delay(100); }
}

void loop() {
    if (!huskylens.request()) { /*Serial.println(F("Please recheck the connection."));*/ }
    else if(!huskylens.isLearned()) { /*Serial.println(F("Nothing learned."));*/ }
    else if(!huskylens.available()) { /*Serial.println(F("No block or arrow on the screen."));*/ }
    else {
        while (huskylens.available()) {
            HUSKYLENSResult result = huskylens.read();
            deg -= int(((result.xCenter-adjustment_px)*px_to_deg*0.2));
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
}
