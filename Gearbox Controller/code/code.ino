/*

Gearbox controller code

 */

int 
pulse = 11, dir = 10, hallEffect = 2, highSensor = 7, lowSensor = 4,
hallEffectCount = 0, prevHighTime, highTime, highSpace,
stepDel = 10, samplePeriod = 500, pinState = LOW, inputsRecieved;

bool 
dirHighAllowed, dirLowAllowed, shifting = false;

float rpm;

static int prevPinState = LOW;

void setup() {
  pinMode(pulse, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(highSensor, INPUT);
  pinMode(lowSensor, INPUT);
  digitalWrite(dir, HIGH);
  
  Serial.begin(9600);
}

void loop() {

  inputsRecieved = 0;
  initLoopTime = millis();
  
  while (inputsRecieved < 2) {
    
    pinState = digitalRead(hallEffect); 
  
    /* Detects if the hall effect sensor recieves a new magnet pass */
    if (pinState == HIGH && prevPinState == LOW) {
  
      /* Determines the time between two magnet passes */
      highSpace = millis() - prevHighTime;
      prevHighTime = millis();
  
      /* Determines the rpm */
      rpm = 1000/float(highSpace)*60;

      inputsRecieved++;
    }
    /*
    else if (millis() - prevHighTime >= 5000) {
      rpm = 0;
      Serial.print("aaaaaaaaaaa");
    }
    */
    prevPinState = pinState;

    /* Stops the loop from waiting too long */
    if (millis() - initLoopTime >= 1000) {
      inputsRecieved = 2;
    }

  }

  /* Determines whether the motor is allowed to spin HIGH */
  if (digitalRead(highSensor) == HIGH && digitalRead(dir) == HIGH) {
    dirHighAllowed = false;
  }
  else {
    dirHighAllowed = true;
  }

  /* Determines whether the motor is allowed to spin LOW */
  if (digitalRead(lowSensor) == HIGH && digitalRead(dir) == LOW) {
    dirLowAllowed = false;
  }
  else {
    dirLowAllowed = true;
  }
  

  /* Determines what direction the stepper should spin */
  if (rpm == 0) {
    shifting = false;
  }
  else if (rpm < 2500) {
    digitalWrite(dir, HIGH);
    shifting = true;
  }
  else if (rpm <= 3000) {
    shifting = false;
  }
  else {
    shifting = true;
    digitalWrite(dir, LOW);
  } 

  
  if (shifting == true && dirHighAllowed == true && dirLowAllowed == true) {
    Serial.print("True  ");
    digitalWrite(pulse, HIGH);
    delayMicroseconds(stepDel);
    digitalWrite(pulse, LOW);
    delayMicroseconds(stepDel);
  }
  else {
    Serial.print("False ");
  }

  Serial.println(" "+String(digitalRead(lowSensor))+String(digitalRead(highSensor))+" "+String(dirLowAllowed)+String(dirHighAllowed)+" "+String(rpm)+" "+String(digitalRead(dir)) );
  
}

/* 

Steps size = 1.8, steps per rev 200
Thing go 6000rpm

5500
6000

  

*/
