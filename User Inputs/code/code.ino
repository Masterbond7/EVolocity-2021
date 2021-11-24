#include <Wire.h>

void setup() {
	Serial.begin(9600);

    Wire.begin(19);
    Wire.onRequest(sendData);
 
    pinMode(A0, INPUT);  // Acc
    pinMode(A1, INPUT);  // Brk
	pinMode(A10, INPUT); // Hbrk
}

int acc_pos;
int brk_pos;
int hbrk_stat;

byte out_data[3];

void loop() {
    /*acc_pos = (analogRead(A0)-532)*(256.0/326.0); if (acc_pos <= 1) {acc_pos = 0;} if (acc_pos >= 256) {acc_pos = 255;}
    brk_pos = (analogRead(A1)-532)*(256.0/336.0); if (brk_pos <= 1) {brk_pos = 0;} if (brk_pos >= 256) {brk_pos = 255;}
    hbrk_stat = digitalRead(A10);

    out_data[0] = acc_pos;
    out_data[1] = brk_pos;
    out_data[2] = hbrk_stat;
    
    Serial.print("Accelerator Position: ");
    Serial.print(out_data[0]);
    Serial.print(", Break Position: ");
    Serial.print(out_data[1]);
    Serial.print(", Handbrake: ");
	Serial.println(out_data[2]);*/
}

void sendData() {
    acc_pos = (analogRead(A0)-532)*(256.0/326.0); if (acc_pos <= 1) {acc_pos = 0;} if (acc_pos >= 256) {acc_pos = 255;}
    brk_pos = (analogRead(A1)-532)*(256.0/336.0); if (brk_pos <= 1) {brk_pos = 0;} if (brk_pos >= 256) {brk_pos = 255;}
    hbrk_stat = digitalRead(A10);

    out_data[0] = acc_pos;
    out_data[1] = brk_pos;
    out_data[2] = hbrk_stat;
    
    Wire.write(out_data, 3);
}
