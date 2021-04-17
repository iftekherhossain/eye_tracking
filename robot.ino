char data = 0;
int speedr = 100; //Baam
int speedl = 113; //Daan
void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  forward();
}
void forward() {
  digitalWrite(2, 1);
  digitalWrite(3, 0);
  digitalWrite(4, 1);
  digitalWrite(5, 0);
  analogWrite(6, speedr);
  analogWrite(7, speedl);
}

void backward() {
  digitalWrite(2, 0);
  digitalWrite(3, 1);
  digitalWrite(4, 0);
  digitalWrite(5, 1);
  analogWrite(6, speedr);
  analogWrite(7, speedl);
}

void right() {
  digitalWrite(2, 0);
  digitalWrite(3, 1);
  digitalWrite(4, 1);
  digitalWrite(5, 0);
  analogWrite(6, speedr);
  analogWrite(7, speedl);
}
void left() {
  digitalWrite(2, 1);
  digitalWrite(3, 0);
  digitalWrite(4, 0);
  digitalWrite(5, 1);
  analogWrite(6, speedr);
  analogWrite(7, speedl);
}

void stopp(){
  digitalWrite(2, 1);
  digitalWrite(3, 0);
  digitalWrite(4, 1);
  digitalWrite(5, 0);
  analogWrite(6, 0);
  analogWrite(7, 0);
}