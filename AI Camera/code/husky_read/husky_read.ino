#include "HUSKYLENS.h"
#include "SoftwareSerial.h"

HUSKYLENS huskylens;
SoftwareSerial huskyserial(4,5); //Huskylens's TX 4, RX 5

int adjustment_px = 160; // The distance in pixels from the far left of the screen to the center of the screen
float px_to_deg = 0.1875; // half screen fov * half screen res

void setup() {
    Serial.begin(9600);
    huskyserial.begin(9600);
    
    while (!huskylens.begin(huskyserial)) { /*Serial.println(F("Please recheck the connection / protocol."));*/ delay(100); }
}

void loop() {
    if (!huskylens.request()) { /*Serial.println(F("Please recheck the connection."));*/ }
    else if(!huskylens.isLearned()) { /*Serial.println(F("Nothing learned."));*/ }
    else if(!huskylens.available()) { /*Serial.println(F("No block or arrow on the screen."));*/ }
    else {
        while (huskylens.available()) {
            HUSKYLENSResult result = huskylens.read();
            printResult(result);
        }
    }
}

void printResult(HUSKYLENSResult result){
    if (result.command == COMMAND_RETURN_BLOCK){ Serial.println((result.xCenter-adjustment_px)*px_to_deg); }
    /*else if (result.command == COMMAND_RETURN_ARROW){
        Serial.println(String()+F("Arrow:xOrigin=")+result.xOrigin+F(",yOrigin=")+result.yOrigin+F(",xTarget=")+result.xTarget+F(",yTarget=")+result.yTarget+F(",ID=")+result.ID);
    }
    else{
        Serial.println("Object unknown!");
    }*/
}
