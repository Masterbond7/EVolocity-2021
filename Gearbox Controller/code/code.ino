int pulse = 11, 
dir = 10, 
hallEffect = 2,
highSensor = 7, 
lowSensor = 4,
stepDel = 10,
samplePeriod = 500,
count = 0;

bool dirHighAllowed, dirLowAllowed;

void setup() {
  pinMode(pulse, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(highSensor, INPUT);
  pinMode(lowSensor, INPUT);
  digitalWrite(dir, HIGH);
  Serial.begin(9600);
}

void loop() {

  if (digitalRead(highSensor) == HIGH) {
    dirHighAllowed = false;
    digitalWrite(dir, LOW);
  }
  else {
    dirHighAllowed = true;
  }

  if (digitalRead(lowSensor) == HIGH) {
    dirLowAllowed = false;
    digitalWrite(dir, HIGH);
  }
  else {
    dirLowAllowed = true;
  }

  if (dirHighAllowed == true || dirLowAllowed == true) {
    digitalWrite(pulse, HIGH);
    delayMicroseconds(stepDel);
    digitalWrite(pulse, LOW);
    delayMicroseconds(stepDel);
  }


  static uint32_t lastTime = 0;
  if (millis() - lastTime >= samplePeriod) {
    noInterrupts();
    unsigned int pulsesPerPeriod = count;
    count = 0;
    interrupts();
    Serial.println(pulsesPerPeriod);
    lastTime += samplePeriod;
  }
  
}

/* 

Steps size = 1.8, steps per rev 200

*/
