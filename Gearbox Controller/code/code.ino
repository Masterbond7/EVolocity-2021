/*

Gearbox controller code

 */

volatile unsigned long long int 
timeAtPulse = 0, timeAtPrevPulse = 0;

int
highSensor = 7, lowSensor = 4, pulse = 11, dir = 10, stepDel = 10;

bool
dirHighAllowed, dirLowAllowed, shifting;

float rpm = 0;


void setup() {
  
  Serial.begin(115200);
  
  pinMode(highSensor, INPUT);
  pinMode(lowSensor, INPUT);
  pinMode(pulse, OUTPUT);
  pinMode(dir, OUTPUT);
  
  attachInterrupt(0, setLastPulse, RISING);

  delay(1000);
  
}


void loop() {

  /* Works out the motor's current RPM */ 
  if (millis() - timeAtPulse >= 1000) {
    rpm = 0;
  }
  else {
    rpm = 1000/float(timeAtPulse - timeAtPrevPulse)*60;
  }
 

  /* Determines if and what direction the motor should spin */
  if (rpm > 0 && rpm <= 1500) {
    shifting = true;
    digitalWrite(dir, HIGH);
  }
  else if (rpm >= 2500) {
    shifting = true;
    digitalWrite(dir, LOW);
  }
  else {
    shifting = false;
  }
  

  /* Determines whether the stepper motor is allowed to spin HIGH */
  if (digitalRead(highSensor) == HIGH && digitalRead(dir) == HIGH) {
    dirHighAllowed = false;
  }
  else {
    dirHighAllowed = true;
  }

  /* Determines whether the stepper motor is allowed to spin LOW */
  if (digitalRead(lowSensor) == HIGH && digitalRead(dir) == LOW) {
    dirLowAllowed = false;
  }
  else {
    dirLowAllowed = true;
  }

  
  /* If it safe to spin the motor, it will pulse the stepper motor to turn it */
  if (shifting && dirHighAllowed && dirLowAllowed) {
    digitalWrite(pulse, HIGH);
    delayMicroseconds(stepDel);
    digitalWrite(pulse, LOW);
    delayMicroseconds(stepDel);

    Serial.print("Shifting gear: True");
  }
  else {
    Serial.print("Shifting gear: False");
  }

  Serial.println("  RPM: "+String(rpm));
  
}


/* ISR for setting the time which the hall effect sensor last got a pulse */
void setLastPulse() {
  
  timeAtPrevPulse = timeAtPulse;
  timeAtPulse = millis();
  
}
