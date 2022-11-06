#include <Servo.h>

Servo servo1;
Servo servo2;
int desired_angle, current_angle, increment_angle, increment_delay, delta_angle, remainder_angle, sensor_val;

void setup() {
    Serial.begin(9600);

    increment_angle = 5;
    increment_delay = 50;
    current_angle = 69;
    desired_angle = 69;

    servo1.attach(2);
    servo1.write(current_angle);
    servo2.attach(3);
    servo2.write(current_angle);

    pinMode(A7, INPUT);
}

void loop() {
    //535 - 850//800
    sensor_val = analogRead(A7);
    sensor_val -= 535;
    if (sensor_val < 0) { sensor_val = 0; }
    if (sensor_val > 315) { sensor_val = 315; }
    
    desired_angle = (int(float(sensor_val * (69.0f/315.0f)))*-1)+69;
    /*Serial.print("Signal: ");
    Serial.print(analogRead(A7));
    Serial.print(", Sensor val: ");
    Serial.print(sensor_val);
    Serial.print(", Angle: ");
    Serial.println(desired_angle);*/
    delta_angle = desired_angle - current_angle;
    remainder_angle = abs(delta_angle) % increment_angle;

    if (remainder_angle) {
        if (delta_angle > 0) {current_angle += remainder_angle;}
        if (delta_angle < 0) {current_angle -= remainder_angle;}
        servo1.write(current_angle);
        servo2.write(current_angle);
        delay(int(increment_delay*(float(remainder_angle)/5.0f)));
    }

    if (current_angle > desired_angle) { current_angle -= increment_angle; }
    else if (current_angle < desired_angle) { current_angle += increment_angle; }
    servo1.write(current_angle);
    servo2.write(current_angle);
    delay(increment_delay);
}
