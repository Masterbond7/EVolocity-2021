#include <Servo.h>
#include <Wire.h>

Servo servo;
int deg = 45;
int degtmp=90;
char a;

union u_tag {
    unsigned short int Int;
    char Char;
} positionData;
float position_float;

void setup() {
  Serial.begin(9600);
  servo.attach(3);
  Wire.begin(18);  
  Wire.onReceive(receiveData);
  positionData.Int = 0;
}

void loop(){
  /*Wire.requestFrom(17,1);
  positionData.Char = Wire.read();
  Serial.println(positionData.Char);
  degtmp = positionData.Int;
  degtmp *= 180/256;
  degtmp *= -1;
  degtmp += 180;
  if (degtmp > 0 && degtmp < 180) {deg=degtmp;}
  degtmp = deg;
  servo.write(deg);
  delay(100);*/
  //Serial.println(positionData.Int);
}

void receiveData(int num_bytes) {
    positionData.Char = Wire.read();
    position_float = positionData.Int;
    position_float *= (180.0f/252.f);
    //position_float *= -1; position_float += 180;
    positionData.Int = position_float;
    Serial.println(positionData.Int);
    servo.write(positionData.Int);
}
