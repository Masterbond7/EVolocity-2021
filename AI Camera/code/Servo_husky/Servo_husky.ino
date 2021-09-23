#include <Servo.h>
#include <Wire.h>

Servo servo;
int deg = 90;
int tmp = 0;

void setup() {
    Serial.begin(9600);
    servo.attach(3);
    Wire.begin(16);
    Wire.onRequest(requestEvent);
}

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

void requestEvent() {
    int steering = servo.read();
    steering -= 90;
    steering *= 2;
    steering += 90;
    if (steering < 0) {steering = 0;}
    else if (steering > 180) {steering = 180;}
    Wire.write(servo.read()); // The angle the steering needs to go to
}
