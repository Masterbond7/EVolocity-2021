#include <Servo.h>

Servo steeringServo;
byte inputBytes[3];
byte steeringByte;
int desired_angle, current_angle, increment_angle, increment_delay, delta_angle, remainder_angle;

void setup() {
    Serial.begin(9600);

    increment_angle = 5;
    increment_delay = 30;
    current_angle = 90;
    desired_angle = 90;

    steeringServo.attach(5);
    steeringServo.write(current_angle);
}

void loop() {
    if(Serial.available() > 0) {
        Serial.readBytes(inputBytes, 3); 
        steeringByte = inputBytes[0];
        desired_angle = int(float(steeringByte) * (180.0f/256.0f));  
    
        delta_angle = desired_angle - current_angle;
        remainder_angle = abs(delta_angle) % increment_angle;
    
        if (remainder_angle) {
            if (delta_angle > 0) {current_angle += remainder_angle;}
            if (delta_angle < 0) {current_angle -= remainder_angle;}
            steeringServo.write(current_angle);
            delay(increment_delay);
        }
    }

    if (current_angle > desired_angle) { current_angle -= increment_angle; }
    else if (current_angle < desired_angle) { current_angle += increment_angle; }
    steeringServo.write(current_angle);
    delay(increment_delay);
}
