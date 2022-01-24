#include <Servo.h>
#include <Wire.h>

Servo servo;
bool data_received = false;

union u_tag {
    unsigned short int Int;
    char Char;
} positionData;


void setup() {
    servo.attach(3);
    Wire.begin(20);  
    Wire.onReceive(receiveData);
    positionData.Int = 0;
}

void loop(){
    if (data_received) { servo.write(servo.read()); }
}

void receiveData(int num_bytes) {
    positionData.Char = Wire.read();
    //positionData.Int *= (180.0f/256.0f);
    servo.write(positionData.Int);

    data_received = true;
}
