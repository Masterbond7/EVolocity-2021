#include <Servo.h>

Servo steeringServo;
int desired_angle, current_angle, increment_angle, increment_delay, delta_angle, remainder_angle;

void setup() {
    Serial.begin(9600);

    increment_angle = 5;
    increment_delay = 30;
    current_angle = 90;
    desired_angle = 90;

    steeringServo.attach(5);
    steeringServo.write(current_angle);

    pinMode(A7, INPUT);
}

void loop() {
    desired_angle = (int(float(analogRead(A7) * (180.0f/1024.0f))*-1)+180;
    delta_angle = desired_angle - current_angle;
    remainder_angle = abs(delta_angle) % increment_angle;

    if (remainder_angle) {
        if (delta_angle > 0) {current_angle += remainder_angle;}
        if (delta_angle < 0) {current_angle -= remainder_angle;}
        steeringServo.write(current_angle);
        delay(int(increment_delay*(float(remainder_angle)/5.0f)));
    }

    if (current_angle > desired_angle) { current_angle -= increment_angle; }
    else if (current_angle < desired_angle) { current_angle += increment_angle; }
    steeringServo.write(current_angle);
    delay(increment_delay);
}
