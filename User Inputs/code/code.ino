void start() {
	Serial.begin(9600);
	pinmode(A10, INPUT);
}

void loop() {
	Serial.println(digitalRead(A10));
}