void setup() {
    Serial.begin(9600);

    pinMode(2, INPUT_PULLUP); // D-pad up
    pinMode(3, INPUT_PULLUP); // D-pad left
    pinMode(4, INPUT_PULLUP); // D-pad right
    pinMode(5, INPUT_PULLUP); // D-pad down
    pinMode(6, INPUT_PULLUP); // ???
    pinMode(7, INPUT_PULLUP); // ???
    pinMode(8, INPUT_PULLUP); // ???
    pinMode(9, INPUT_PULLUP); // B
    pinMode(10, INPUT_PULLUP); // Right paddle
    pinMode(11, INPUT_PULLUP); // A
    pinMode(12, INPUT_PULLUP); // Left paddle
    pinMode(20, INPUT_PULLUP); // X
    pinMode(21, INPUT_PULLUP); // Y
    pinMode(17, INPUT_PULLUP); // X-Box button

    pinMode(16, OUTPUT); // Power bulb
    pinMode(15, OUTPUT); // Steering power (+5V)

    pinMode(A0, INPUT); // Steering

    digitalWrite(16, HIGH); // Bulb
    digitalWrite(15, HIGH); // Steering power (+5V)
}

void loop() {
    if (digitalRead(2) == LOW) {Serial.print("D-pad up, ");} 
    if (digitalRead(3) == LOW) {Serial.print("D-pad left, ");} 
    if (digitalRead(4) == LOW) {Serial.print("D-pad right, ");} 
    if (digitalRead(5) == LOW) {Serial.print("D-pad down, ");} 
    
    if (digitalRead(6) == LOW) {Serial.print("UNDEFINED 1, ");} 
    if (digitalRead(7) == LOW) {Serial.print("UNDEFINED 2, ");} 
    if (digitalRead(8) == LOW) {Serial.print("UNDEFINED 3, ");}
    
    if (digitalRead(9) == LOW) {Serial.print("B, ");}  
    if (digitalRead(11) == LOW) {Serial.print("A, ");} 
    if (digitalRead(20) == LOW) {Serial.print("X, ");} 
    if (digitalRead(21) == LOW) {Serial.print("Y, ");} 

    if (digitalRead(12) == LOW) {Serial.print("Left padle, ");} 
    if (digitalRead(10) == LOW) {Serial.print("Right padle, ");} 

    if (digitalRead(17) == LOW) {Serial.print("X-Box button, ");} 

    Serial.println(analogRead(A0));
}
