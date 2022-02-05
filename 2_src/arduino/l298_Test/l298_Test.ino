#define I1 1
#define I2 2
#define I3 3
#define I4 4
#define ENA 8
#define ENB 9

void setup() {
  // put your setup code here, to run once:
  pinMode(I1, OUTPUT);
  pinMode(I2, OUTPUT);
  pinMode(I3, OUTPUT);
  pinMode(I4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(I1, HIGH);
  digitalWrite(I2, LOW);
  digitalWrite(I3, LOW);
  digitalWrite(I4, HIGH);
  digitalWrite(ENA, HIGH);
  digitalWrite(ENB, HIGH);
  delay(1000); 
}
