/*

Total steps between limit switches finder

 */

int
highSensor = 7, lowSensor = 4, pulse = 11, dir = 10, stepDel = 10, stepCount = 0;

void setup() {
  
  Serial.begin(115200);

  pinMode(highSensor, INPUT);
  pinMode(lowSensor, INPUT);
  pinMode(pulse, OUTPUT);
  pinMode(dir, OUTPUT);


  dir = LOW;

  while (digitalRead(lowSensor) == LOW) {
    pulse();
  }

  dir = HIGH;

  while (digitalRead(highSensor) == LOW) {
    pulse();
    stepCount++;
  }

  Serial.println("Total steps: "+String(stepCount));

}

void pulse() {
  digitalWrite(pulse, HIGH);
  delayMicroseconds(stepDel);
  digitalWrite(pulse, LOW);
  delayMicroseconds(stepDel);
}
