#include <Servo.h>
#include <Wire.h>

Servo servo;

union u_tag {
    unsigned short int Int;
    char Char;
} positionData;

void setup() {
    servo.attach(3);
    Wire.begin(18);  
    Wire.onReceive(receiveData);
    positionData.Int = 0;
}

void loop(){
    
}

void receiveData(int num_bytes) {
    positionData.Char = Wire.read();
    //positionData.Int *= (180.0f/256.0f);
    servo.write(positionData.Int);
}
