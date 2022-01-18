
// Arduino Ultrasoninc Sensor HC-SR04
// Using HC-SR04 Module



#define trigPin1 21 //attach pin 21 Arduino to pin Trig of HC-SR04
#define trigPin2 20 //attach pin 20 Arduino to pin Trig of HC-SR04
#define trigPin3 19 //attach pin 19 Arduino to pin Trig of HC-SR04
#define trigPin4 18 //attach pin 18 Arduino to pin Trig of HC-SR04

#define echoPin1 6 // attach pin 6 Arduino to pin Echo of HC-SR04
#define echoPin2 8 // attach pin 8 Arduino to pin Echo of HC-SR04
#define echoPin3 9 // attach pin 9 Arduino to pin Echo of HC-SR04
#define echoPin4 10 // attach pin 10 Arduino to pin Echo of HC-SR04

// defines variables
long duration; // variable for the duration of sound wave travel
int distance1; // variable for the distance measurement
int distance2;
int distance3;
int distance4;

void setup() {
  pinMode(trigPin1, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin1, INPUT); // Sets the echoPin as an INPUT

  pinMode(trigPin2, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin2, INPUT); // Sets the echoPin as an INPUT

  pinMode(trigPin3, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin3, INPUT); // Sets the echoPin as an INPUT

  pinMode(trigPin4, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin4, INPUT); // Sets the echoPin as an INPUT
  
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  
}
void loop() {
  // Clears the trigPin condition
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin1, HIGH);
  // Calculating the distance
  distance1 = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  
  delayMicroseconds(50);

  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  duration = pulseIn(echoPin2, HIGH);
  distance2 = duration * 0.034 / 2; 

  delayMicroseconds(50);

  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);
  duration = pulseIn(echoPin3, HIGH);
  distance3 = duration * 0.034 / 2; 

  delayMicroseconds(50);

  digitalWrite(trigPin4, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin4, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin4, LOW);
  duration = pulseIn(echoPin4, HIGH);
  distance4 = duration * 0.034 / 2; 
 
  Serial.print("Distance1: ");
  Serial.print(distance1);
  Serial.println(" cm");

  Serial.print("Distance2: ");
  Serial.print(distance2);
  Serial.println(" cm"); 

  Serial.print("Distance3: ");
  Serial.print(distance3);
  Serial.println(" cm"); 

  Serial.print("Distance4: ");
  Serial.print(distance4);
  Serial.println(" cm\n"); 

  delayMicroseconds(50);
}

  
