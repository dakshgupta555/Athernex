int vinPin = A0;
int voutPin = A1;

int A_pin = 2;
int B_pin = 3;
int Y_pin = 4;

void setup() {
  Serial.begin(9600);

  pinMode(A_pin, OUTPUT);
  pinMode(B_pin, OUTPUT);
  pinMode(Y_pin, INPUT);
}

void loop() {
  int vin_raw = analogRead(vinPin);
  int vout_raw = analogRead(voutPin);

  float vin = vin_raw * (5.0 / 1023.0);
  float vout = vout_raw * (5.0 / 1023.0);

  static int state = 0;

  int A = (state >> 1) & 1;
  int B = state & 1;

  digitalWrite(A_pin, A);
  digitalWrite(B_pin, B);

  delay(50);

  int Y = digitalRead(Y_pin);
  state = (state + 1) % 4;

  Serial.print(vin); Serial.print(",");
  Serial.print(vout); Serial.print(",");
  Serial.print(A); Serial.print(",");
  Serial.print(B); Serial.print(",");
  Serial.println(Y);

  delay(200);
}
