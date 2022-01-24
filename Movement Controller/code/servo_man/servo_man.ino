#include <Servo.h>

Servo servo;
int deg;

void setup() {
    servo.attach(3); 
    Serial.begin(9600);
}

void loop(){
    /*deg = Serial.parseInt();
    if (deg != 0) {
        servo.write(deg);    
    }*/
    for (int i = 0; i < 180; i+=5){
      servo.write(i);
      delay(25);
    }
    for (int i = 180; i > 0; i-=5){
      servo.write(i);
      delay(25);
    }
}
