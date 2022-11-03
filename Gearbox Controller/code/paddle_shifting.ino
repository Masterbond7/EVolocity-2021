/*

Gearbox controller code

 */

volatile unsigned long long int 
timeAtPulse = 0, timeAtPrevPulse = 0;

int
highSensor = 7, lowSensor = 4, pulse = 11, dir = 10, stepDel = 10, 
stepsPerGear = /* total steps/number of gears */;

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
  if (millis() - timeAtPulse >= 600) { // If time between a pulse is long enough for 
    rpm = 0;                           // 100 RPM or below it will set RPM to 0
  }
  else {
    rpm = 1000/float(timeAtPulse - timeAtPrevPulse)*60; // Works out RPM based on time 
  }                                                     // between magnet pulses


  /* Gets shifting paddle input */
  if (/* Left paddle */) {
    stepsLow += stepsPerGear;
  }

  if (/* Right paddle */) {
    stepsHigh += stepsPerGear;
  }

  /* Determines net steps */
  stepsNet = stepsHigh - stepsLow;

  /* Based on the net steps; determines how the stepper motor should spin */
  if (stepsNet < 0) {
    shifting = true;
    digitalWrite(dir, LOW);
    stepsLow--;
  }
  else if (stepsNet > 0) {
    shifting = true;
    digitalWrite(dir, HIGH);
    stepsHigh--;
  }
  else {
    shifting = false;
    stepsLow = 0;
    stepsHigh = 0;
  }
  

  /* If it safe to spin the motor, it will pulse the stepper motor to turn it */
  if (shifting && dirHighAllowed && dirLowAllowed && rpm > 0) {
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
