int num = 0;
//int tempnum = 0;

void setup() {
    Serial.begin(9600);
    pinMode(6, OUTPUT);
}

void loop() {
    //tempnum = Serial.parseInt();
    //if (tempnum != 0) { num = tempnum; }
    if (Serial.available()) {
        num = Serial.parseInt();
        analogWrite(6, num);    
    }
}
