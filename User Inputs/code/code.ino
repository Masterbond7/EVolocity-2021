void setup() {
	Serial.begin(9600);
    pinMode(A0, INPUT); // Acc
    pinMode(A2, INPUT); // Brk
	//pinMode(A10, INPUT);// Hbrk
}

void loop() {
    Serial.print("Accelerator Position: ");
    Serial.print(analogRead(A0));
    Serial.print(", Break Position: ");
    Serial.println(analogRead(A2));
    //Serial.print(", Handbrake: ");
	//Serial.println(digitalRead(A10));
}
