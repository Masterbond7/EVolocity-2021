#include <Servo.h>
#include <Wire.h>

Servo servo;
int desired_angle, current_angle, increment_angle, increment_delay, delta_angle, remainder_angle;

union u_tag {
    unsigned short int Int;
    char Char;
} positionData;

void setup() {
    positionData.Int = 0;
    
    increment_angle = 5;
    increment_delay = 30;
    current_angle = 90;
    
    servo.attach(3);
    servo.write(current_angle);
    
    Wire.begin(18);  
    Wire.onReceive(receiveData);

    Serial.begin(9600);
}

void loop(){
    if (current_angle > desired_angle) { current_angle -= increment_angle; }
    else if (current_angle < desired_angle) {current_angle += increment_angle; }
    servo.write(current_angle);
    delay(increment_delay);
}

void receiveData(int num_bytes) {
    positionData.Char = Wire.read();
    //positionData.Int = 180 - positionData.Int;//(180.0f/256.0f)

    desired_angle = positionData.Int;
    delta_angle = desired_angle - current_angle;
    remainder_angle = delta_angle % increment_angle;
    
    if (remainder_angle) {
        current_angle += delta_angle % increment_angle;
        servo.write(current_angle);
        delay(increment_delay);
    }

    Serial.println(desired_angle);
}
