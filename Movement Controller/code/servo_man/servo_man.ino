#include <Servo.h>

Servo servo;
int desired_angle, current_angle, increment_angle, increment_delay, delta_angle, remainder_angle;

void setup() {
    increment_angle = 5;
    increment_delay = 25;
    current_angle = 0;
    
    servo.attach(3); 
    servo.write(current_angle);
    
    Serial.begin(9600);
}

void loop(){
    if (Serial.available()) { 
        desired_angle = Serial.parseInt();
        delta_angle = desired_angle - current_angle;
        remainder_angle = delta_angle % increment_angle;
        
        if (remainder_angle) {
            current_angle += delta_angle % increment_angle;
            servo.write(current_angle);
            delay(increment_delay);
        }
    }

    if (current_angle > desired_angle) { current_angle -= increment_angle; }
    else if (current_angle < desired_angle) {current_angle += increment_angle; }
    servo.write(current_angle);
    delay(increment_delay);
}
